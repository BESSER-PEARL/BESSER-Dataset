import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sastm::RDBHostVariableReference,
    RDBHostVariableReference,
    RDBCursorStatement,
    sastm::RDBFetchCursorStatement,
    sastm::RDBOpenCursorStatement,
    RDBModifyStatement,
    sastm::RDBUpdateStatement,
    AggregateTypeDefinition,
    Project,
    NamedTypeDefinition,
    RDBConstraint,
    sastm::RDBRefIntegrity,
    sastm::RDBUniqueKey,
    sastm::RDBCheckConstraint,
    ActualParameterExpression,
    gastm::ByReferenceActualParameterExpression,
    gastm::ByValueActualParameterExpression,
    IncludeUnit,
    NameSpaceDefinition,
    sastm::RDBTableSpaceReference,
    RDBTableSpaceReference,
    UnaryOperator,
    gastm::AddressOf,
    gastm::Increment,
    gastm::BitNot,
    gastm::Negate,
    gastm::Decrement,
    gastm::Deref,
    gastm::Not,
    gastm::UnaryPlus,
    Literal,
    gastm::CharLiteral,
    gastm::RealLiteral,
    gastm::StringLiteral,
    gastm::BooleanLiteral,
    gastm::BitLiteral,
    gastm::IntegerlLiteral,
    QualifiedIdentifierReference,
    gastm::QualifiedOverData,
    gastm::QualifiedOverPointer,
    gastm::PostDecrement,
    gastm::PostIncrement,
    PrimitiveType,
    gastm::Byte,
    gastm::LongInteger,
    gastm::Integer,
    gastm::Boolean,
    gastm::LongDouble,
    gastm::ShortInteger,
    gastm::Float,
    gastm::WideCharacter,
    gastm::Double,
    gastm::Character,
    gastm::String,
    gastm::Void,
    StorageSpecification,
    gastm::PerClassMember,
    gastm::FunctionPersistent,
    gastm::FileLocal,
    gastm::NoDef,
    gastm::External,
    ForStatement,
    gastm::ForCheckAfterStatement,
    gastm::ForCheckBeforeStatement,
    AccessKind,
    gastm::Private,
    gastm::Protected,
    gastm::Public,
    sastm::RDBCloseCursorStatement,
    sastm::RDBDeleteStatement,
    gastm::AccessKind,
    gastm::DataType,
    gastm::StorageSpecification,
    gastm::OtherSyntaxObject,
    gastm::GASTMSemanticObject,
    gastm::GASTMSourceObject,
    gastm::GASTMObject,
    ProgramScope,
    OtherSyntaxObject,
    sastm::RDBIndexColumn,
    gastm::VirtualSpecification,
    gastm::Name,
    sastm::RDBIndex,
    gastm::FunctionMemberAttribute,
    sastm::RDBTrigger,
    sastm::RDBConstraint,
    gastm::CompilationUnit,
    AnnotationExpression,
    PreprocessorElement,
    SourceLocation,
    GASTMObject,
    gastm::GASTMSyntaxObject,
    Scope,
    gastm::FunctionScope,
    gastm::BlockScope,
    gastm::AggregateScope,
    gastm::ProgramScope,
    DefinitionObject,
    GlobalScope,
    gastm::GlobalScope,
    BinaryOperator,
    gastm::SpecificIn,
    gastm::SpecificLike,
    gastm::NotGreater,
    gastm::Assign,
    gastm::Divide,
    gastm::BitXor,
    gastm::Exponent,
    gastm::Less,
    gastm::Or,
    gastm::Equal,
    gastm::BitRightShift,
    gastm::Subtract,
    gastm::Add,
    gastm::Greater,
    gastm::SpecificGreaterEqual,
    gastm::Multiply,
    gastm::SpecificConcatString,
    gastm::BitLeftShift,
    gastm::SpecificLessEqual,
    gastm::BitOr,
    gastm::NotLess,
    gastm::BitAnd,
    gastm::And,
    gastm::NotEqual,
    gastm::Modulus,
    gastm::OperatorAssign,
    ActualParameter,
    gastm::MissingActualParameter,
    gastm::ActualParameterExpression,
    IdentifierReference,
    sastm::RDBTableAlias,
    sastm::RDBTableReference,
    sastm::RDBColumnReference,
    NameReference,
    gastm::IdentifierReference,
    gastm::TypeQualifiedIdentifierReference,
    gastm::QualifiedIdentifierReference,
    gastm::CatchBlock,
    CatchBlock,
    gastm::TypesCatchBlock,
    LoopStatement,
    gastm::DoWhileStatement,
    gastm::WhileStatement,
    gastm::ForStatement,
    gastm::VariableCatchBlock,
    BlockScope,
    LabelDefinition,
    gastm::SwitchCase,
    SwitchCase,
    gastm::DefaultBlock,
    gastm::CaseBlock,
    LabelAccess,
    gastm::Dimension,
    Dimension,
    ConstructedType,
    gastm::PointerType,
    gastm::CollectionType,
    gastm::RangeType,
    gastm::ReferenceType,
    gastm::ArrayType,
    AggregateScope,
    EnumLiteralDefinition,
    DataType,
    sastm::RDBRaw,
    sastm::RDBBoolean,
    sastm::RDBClob,
    sastm::RDBRowid,
    sastm::RDBTableType,
    sastm::RDBDataBaseType,
    sastm::RDBTimestamp,
    sastm::RDBChar,
    sastm::RDBVarchar,
    gastm::AggregateType,
    sastm::RDBNumber,
    sastm::RDBLong,
    gastm::EnumType,
    sastm::RDBString,
    sastm::RDBReal,
    sastm::RDBBlob,
    gastm::ExceptionType,
    sastm::RDBDecimal,
    sastm::RDBNClob,
    sastm::RDBInteger,
    sastm::RDBInt,
    sastm::RDBUserType,
    sastm::RDBViewType,
    sastm::RDBBFile,
    sastm::RDBFloat,
    gastm::ConstructedType,
    sastm::RDBDate,
    sastm::RDBCursorType,
    sastm::RDBTableSpaceType,
    gastm::PrimitiveType,
    gastm::DerivesFrom,
    DerivesFrom,
    gastm::NamedType,
    gastm::FormalParameterType,
    FormalParameterType,
    gastm::ByValueFormalParameterType,
    gastm::ByReferenceFormalParameterType,
    Type,
    gastm::LabelType,
    gastm::FunctionType,
    gastm::NameSpaceType,
    gastm::TypeReference,
    gastm::NameSpaceDefinition,
    AggregateType,
    gastm::UnionType,
    gastm::StructureType,
    gastm::ClassType,
    gastm::AnnotationType,
    NamedType,
    TypeDefinition,
    gastm::AggregateTypeDefinition,
    gastm::NamedTypeDefinition,
    gastm::TypeDefinition,
    DataDefinition,
    gastm::VariableDefinition,
    gastm::FormalParameterDefinition,
    gastm::BitFieldDefinition,
    Expression,
    gastm::NameReference,
    sastm::RDBHostVariableExpression,
    gastm::UnaryExpression,
    gastm::BinaryExpression,
    gastm::FunctionCallExpression,
    gastm::ArrayAccess,
    gastm::Literal,
    gastm::ConditionalExpression,
    gastm::LabelAccess,
    gastm::AggregateExpression,
    gastm::AnnotationExpression,
    gastm::RangeExpression,
    sastm::RDBSelectExpression,
    gastm::NewExpression,
    gastm::CastExpression,
    GASTMSyntaxObject,
    gastm::Expression,
    gastm::PreprocessorElement,
    gastm::Statement,
    gastm::DefinitionObject,
    gastm::Type,
    gastm::Comment,
    gastm::MacroDefinition,
    MacroDefinition,
    gastm::MacroCall,
    gastm::IncludeUnit,
    LabelType,
    gastm::LabelDefinition,
    NameSpaceType,
    FunctionMemberAttributes,
    FormalParameterDeclaration,
    Declaration,
    gastm::FormalParameterDeclaration,
    gastm::FunctionDeclaration,
    Definition,
    gastm::EnumLiteralDefinition,
    sastm::RDBTableDefinition,
    sastm::RDBCursorDefinition,
    sastm::RDBColumnDefinition,
    sastm::RDBUserDefinition,
    gastm::DataDefinition,
    sastm::RDBViewDefinition,
    sastm::RDBTableSpaceDefinition,
    gastm::SpecificTriggerDefinition,
    sastm::RDBDatabaseDefinition,
    TypeReference,
    gastm::NamedTypeReference,
    gastm::UnnamedTypeReference,
    Name,
    DeclarationOrDefinition,
    gastm::Declaration,
    gastm::Definition,
    gastm::DeclarationOrDefinition,
    gastm::EntryDefinition,
    VirtualSpecification,
    gastm::Virtual,
    gastm::NonVirtual,
    gastm::PureVirtual,
    gastm::FunctionMemberAttributes,
    FunctionScope,
    Statement,
    gastm::JumpStatement,
    sastm::RDBConnectStatement,
    gastm::LoopStatement,
    gastm::DeleteStatement,
    gastm::LabeledStatement,
    gastm::IfStatement,
    gastm::TerminateStatement,
    gastm::ContinueStatement,
    gastm::SwitchStatement,
    sastm::RDBCursorStatement,
    gastm::DeclarationOrDefinitionStatement,
    sastm::RDBSelectStatement,
    gastm::ReturnStatement,
    sastm::RDBModifyStatement,
    gastm::BlockStatement,
    gastm::TryStatement,
    sastm::RDBInsertStatement,
    gastm::ExpressionStatement,
    gastm::ThrowStatement,
    gastm::SpecificSelectStatement,
    gastm::BreakStatement,
    gastm::EmptyStatement,
    FormalParameterDefinition,
    gastm::FunctionDefinition,
    gastm::VariableDeclaration,
    CompilationUnit,
    GASTMSemanticObject,
    gastm::Scope,
    gastm::Project,
    SourceFile,
    GASTMSourceObject,
    gastm::SourceLocation,
    gastm::SourceFile,
    gastm::ActualParameter,
    gastm::BinaryOperator,
    gastm::UnaryOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sastm::rdbhostvariablereference_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBHostVariableReference)


def test_sastm::rdbhostvariablereference_constructor_exists():
    assert callable(sastm::RDBHostVariableReference.__init__)


def test_sastm::rdbhostvariablereference_constructor_args():
    sig = inspect.signature(sastm::RDBHostVariableReference.__init__)
    params = list(sig.parameters.keys())



def test_rdbhostvariablereference_is_not_abstract():
    assert not inspect.isabstract(RDBHostVariableReference)


def test_rdbhostvariablereference_constructor_exists():
    assert callable(RDBHostVariableReference.__init__)


def test_rdbhostvariablereference_constructor_args():
    sig = inspect.signature(RDBHostVariableReference.__init__)
    params = list(sig.parameters.keys())



def test_rdbcursorstatement_is_not_abstract():
    assert not inspect.isabstract(RDBCursorStatement)


def test_rdbcursorstatement_constructor_exists():
    assert callable(RDBCursorStatement.__init__)


def test_rdbcursorstatement_constructor_args():
    sig = inspect.signature(RDBCursorStatement.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbfetchcursorstatement_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBFetchCursorStatement)


def test_sastm::rdbfetchcursorstatement_constructor_exists():
    assert callable(sastm::RDBFetchCursorStatement.__init__)


def test_sastm::rdbfetchcursorstatement_constructor_args():
    sig = inspect.signature(sastm::RDBFetchCursorStatement.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbopencursorstatement_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBOpenCursorStatement)


def test_sastm::rdbopencursorstatement_constructor_exists():
    assert callable(sastm::RDBOpenCursorStatement.__init__)


def test_sastm::rdbopencursorstatement_constructor_args():
    sig = inspect.signature(sastm::RDBOpenCursorStatement.__init__)
    params = list(sig.parameters.keys())



def test_rdbmodifystatement_is_not_abstract():
    assert not inspect.isabstract(RDBModifyStatement)


def test_rdbmodifystatement_constructor_exists():
    assert callable(RDBModifyStatement.__init__)


def test_rdbmodifystatement_constructor_args():
    sig = inspect.signature(RDBModifyStatement.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbupdatestatement_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBUpdateStatement)


def test_sastm::rdbupdatestatement_constructor_exists():
    assert callable(sastm::RDBUpdateStatement.__init__)


def test_sastm::rdbupdatestatement_constructor_args():
    sig = inspect.signature(sastm::RDBUpdateStatement.__init__)
    params = list(sig.parameters.keys())



def test_aggregatetypedefinition_is_not_abstract():
    assert not inspect.isabstract(AggregateTypeDefinition)


def test_aggregatetypedefinition_constructor_exists():
    assert callable(AggregateTypeDefinition.__init__)


def test_aggregatetypedefinition_constructor_args():
    sig = inspect.signature(AggregateTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_project_is_not_abstract():
    assert not inspect.isabstract(Project)


def test_project_constructor_exists():
    assert callable(Project.__init__)


def test_project_constructor_args():
    sig = inspect.signature(Project.__init__)
    params = list(sig.parameters.keys())



def test_namedtypedefinition_is_not_abstract():
    assert not inspect.isabstract(NamedTypeDefinition)


def test_namedtypedefinition_constructor_exists():
    assert callable(NamedTypeDefinition.__init__)


def test_namedtypedefinition_constructor_args():
    sig = inspect.signature(NamedTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_rdbconstraint_is_not_abstract():
    assert not inspect.isabstract(RDBConstraint)


def test_rdbconstraint_constructor_exists():
    assert callable(RDBConstraint.__init__)


def test_rdbconstraint_constructor_args():
    sig = inspect.signature(RDBConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbrefintegrity_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBRefIntegrity)


def test_sastm::rdbrefintegrity_constructor_exists():
    assert callable(sastm::RDBRefIntegrity.__init__)


def test_sastm::rdbrefintegrity_constructor_args():
    sig = inspect.signature(sastm::RDBRefIntegrity.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbuniquekey_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBUniqueKey)


def test_sastm::rdbuniquekey_constructor_exists():
    assert callable(sastm::RDBUniqueKey.__init__)


def test_sastm::rdbuniquekey_constructor_args():
    sig = inspect.signature(sastm::RDBUniqueKey.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbcheckconstraint_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBCheckConstraint)


def test_sastm::rdbcheckconstraint_constructor_exists():
    assert callable(sastm::RDBCheckConstraint.__init__)


def test_sastm::rdbcheckconstraint_constructor_args():
    sig = inspect.signature(sastm::RDBCheckConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "RDBConstraintText" in params, "Missing parameter 'RDBConstraintText'"
    assert "RDBConstraintType" in params, "Missing parameter 'RDBConstraintType'"

def test_sastm::rdbcheckconstraint_has_RDBConstraintText():
    assert hasattr(sastm::RDBCheckConstraint, "RDBConstraintText")
    descriptor = None
    for klass in sastm::RDBCheckConstraint.__mro__:
        if "RDBConstraintText" in klass.__dict__:
            descriptor = klass.__dict__["RDBConstraintText"]
            break
    assert isinstance(descriptor, property)

def test_sastm::rdbcheckconstraint_has_RDBConstraintType():
    assert hasattr(sastm::RDBCheckConstraint, "RDBConstraintType")
    descriptor = None
    for klass in sastm::RDBCheckConstraint.__mro__:
        if "RDBConstraintType" in klass.__dict__:
            descriptor = klass.__dict__["RDBConstraintType"]
            break
    assert isinstance(descriptor, property)



def test_actualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(ActualParameterExpression)


def test_actualparameterexpression_constructor_exists():
    assert callable(ActualParameterExpression.__init__)


def test_actualparameterexpression_constructor_args():
    sig = inspect.signature(ActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::byreferenceactualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(gastm::ByReferenceActualParameterExpression)


def test_gastm::byreferenceactualparameterexpression_constructor_exists():
    assert callable(gastm::ByReferenceActualParameterExpression.__init__)


def test_gastm::byreferenceactualparameterexpression_constructor_args():
    sig = inspect.signature(gastm::ByReferenceActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::byvalueactualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(gastm::ByValueActualParameterExpression)


def test_gastm::byvalueactualparameterexpression_constructor_exists():
    assert callable(gastm::ByValueActualParameterExpression.__init__)


def test_gastm::byvalueactualparameterexpression_constructor_args():
    sig = inspect.signature(gastm::ByValueActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_includeunit_is_not_abstract():
    assert not inspect.isabstract(IncludeUnit)


def test_includeunit_constructor_exists():
    assert callable(IncludeUnit.__init__)


def test_includeunit_constructor_args():
    sig = inspect.signature(IncludeUnit.__init__)
    params = list(sig.parameters.keys())



def test_namespacedefinition_is_not_abstract():
    assert not inspect.isabstract(NameSpaceDefinition)


def test_namespacedefinition_constructor_exists():
    assert callable(NameSpaceDefinition.__init__)


def test_namespacedefinition_constructor_args():
    sig = inspect.signature(NameSpaceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbtablespacereference_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBTableSpaceReference)


def test_sastm::rdbtablespacereference_constructor_exists():
    assert callable(sastm::RDBTableSpaceReference.__init__)


def test_sastm::rdbtablespacereference_constructor_args():
    sig = inspect.signature(sastm::RDBTableSpaceReference.__init__)
    params = list(sig.parameters.keys())



def test_rdbtablespacereference_is_not_abstract():
    assert not inspect.isabstract(RDBTableSpaceReference)


def test_rdbtablespacereference_constructor_exists():
    assert callable(RDBTableSpaceReference.__init__)


def test_rdbtablespacereference_constructor_args():
    sig = inspect.signature(RDBTableSpaceReference.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_gastm::addressof_is_not_abstract():
    assert not inspect.isabstract(gastm::AddressOf)


def test_gastm::addressof_constructor_exists():
    assert callable(gastm::AddressOf.__init__)


def test_gastm::addressof_constructor_args():
    sig = inspect.signature(gastm::AddressOf.__init__)
    params = list(sig.parameters.keys())



def test_gastm::increment_is_not_abstract():
    assert not inspect.isabstract(gastm::Increment)


def test_gastm::increment_constructor_exists():
    assert callable(gastm::Increment.__init__)


def test_gastm::increment_constructor_args():
    sig = inspect.signature(gastm::Increment.__init__)
    params = list(sig.parameters.keys())



def test_gastm::bitnot_is_not_abstract():
    assert not inspect.isabstract(gastm::BitNot)


def test_gastm::bitnot_constructor_exists():
    assert callable(gastm::BitNot.__init__)


def test_gastm::bitnot_constructor_args():
    sig = inspect.signature(gastm::BitNot.__init__)
    params = list(sig.parameters.keys())



def test_gastm::negate_is_not_abstract():
    assert not inspect.isabstract(gastm::Negate)


def test_gastm::negate_constructor_exists():
    assert callable(gastm::Negate.__init__)


def test_gastm::negate_constructor_args():
    sig = inspect.signature(gastm::Negate.__init__)
    params = list(sig.parameters.keys())



def test_gastm::decrement_is_not_abstract():
    assert not inspect.isabstract(gastm::Decrement)


def test_gastm::decrement_constructor_exists():
    assert callable(gastm::Decrement.__init__)


def test_gastm::decrement_constructor_args():
    sig = inspect.signature(gastm::Decrement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::deref_is_not_abstract():
    assert not inspect.isabstract(gastm::Deref)


def test_gastm::deref_constructor_exists():
    assert callable(gastm::Deref.__init__)


def test_gastm::deref_constructor_args():
    sig = inspect.signature(gastm::Deref.__init__)
    params = list(sig.parameters.keys())



def test_gastm::not_is_not_abstract():
    assert not inspect.isabstract(gastm::Not)


def test_gastm::not_constructor_exists():
    assert callable(gastm::Not.__init__)


def test_gastm::not_constructor_args():
    sig = inspect.signature(gastm::Not.__init__)
    params = list(sig.parameters.keys())



def test_gastm::unaryplus_is_not_abstract():
    assert not inspect.isabstract(gastm::UnaryPlus)


def test_gastm::unaryplus_constructor_exists():
    assert callable(gastm::UnaryPlus.__init__)


def test_gastm::unaryplus_constructor_args():
    sig = inspect.signature(gastm::UnaryPlus.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_gastm::charliteral_is_not_abstract():
    assert not inspect.isabstract(gastm::CharLiteral)


def test_gastm::charliteral_constructor_exists():
    assert callable(gastm::CharLiteral.__init__)


def test_gastm::charliteral_constructor_args():
    sig = inspect.signature(gastm::CharLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gastm::realliteral_is_not_abstract():
    assert not inspect.isabstract(gastm::RealLiteral)


def test_gastm::realliteral_constructor_exists():
    assert callable(gastm::RealLiteral.__init__)


def test_gastm::realliteral_constructor_args():
    sig = inspect.signature(gastm::RealLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gastm::stringliteral_is_not_abstract():
    assert not inspect.isabstract(gastm::StringLiteral)


def test_gastm::stringliteral_constructor_exists():
    assert callable(gastm::StringLiteral.__init__)


def test_gastm::stringliteral_constructor_args():
    sig = inspect.signature(gastm::StringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gastm::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(gastm::BooleanLiteral)


def test_gastm::booleanliteral_constructor_exists():
    assert callable(gastm::BooleanLiteral.__init__)


def test_gastm::booleanliteral_constructor_args():
    sig = inspect.signature(gastm::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gastm::bitliteral_is_not_abstract():
    assert not inspect.isabstract(gastm::BitLiteral)


def test_gastm::bitliteral_constructor_exists():
    assert callable(gastm::BitLiteral.__init__)


def test_gastm::bitliteral_constructor_args():
    sig = inspect.signature(gastm::BitLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gastm::integerlliteral_is_not_abstract():
    assert not inspect.isabstract(gastm::IntegerlLiteral)


def test_gastm::integerlliteral_constructor_exists():
    assert callable(gastm::IntegerlLiteral.__init__)


def test_gastm::integerlliteral_constructor_args():
    sig = inspect.signature(gastm::IntegerlLiteral.__init__)
    params = list(sig.parameters.keys())



def test_qualifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(QualifiedIdentifierReference)


def test_qualifiedidentifierreference_constructor_exists():
    assert callable(QualifiedIdentifierReference.__init__)


def test_qualifiedidentifierreference_constructor_args():
    sig = inspect.signature(QualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_gastm::qualifiedoverdata_is_not_abstract():
    assert not inspect.isabstract(gastm::QualifiedOverData)


def test_gastm::qualifiedoverdata_constructor_exists():
    assert callable(gastm::QualifiedOverData.__init__)


def test_gastm::qualifiedoverdata_constructor_args():
    sig = inspect.signature(gastm::QualifiedOverData.__init__)
    params = list(sig.parameters.keys())



def test_gastm::qualifiedoverpointer_is_not_abstract():
    assert not inspect.isabstract(gastm::QualifiedOverPointer)


def test_gastm::qualifiedoverpointer_constructor_exists():
    assert callable(gastm::QualifiedOverPointer.__init__)


def test_gastm::qualifiedoverpointer_constructor_args():
    sig = inspect.signature(gastm::QualifiedOverPointer.__init__)
    params = list(sig.parameters.keys())



def test_gastm::postdecrement_is_not_abstract():
    assert not inspect.isabstract(gastm::PostDecrement)


def test_gastm::postdecrement_constructor_exists():
    assert callable(gastm::PostDecrement.__init__)


def test_gastm::postdecrement_constructor_args():
    sig = inspect.signature(gastm::PostDecrement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::postincrement_is_not_abstract():
    assert not inspect.isabstract(gastm::PostIncrement)


def test_gastm::postincrement_constructor_exists():
    assert callable(gastm::PostIncrement.__init__)


def test_gastm::postincrement_constructor_args():
    sig = inspect.signature(gastm::PostIncrement.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::byte_is_not_abstract():
    assert not inspect.isabstract(gastm::Byte)


def test_gastm::byte_constructor_exists():
    assert callable(gastm::Byte.__init__)


def test_gastm::byte_constructor_args():
    sig = inspect.signature(gastm::Byte.__init__)
    params = list(sig.parameters.keys())



def test_gastm::longinteger_is_not_abstract():
    assert not inspect.isabstract(gastm::LongInteger)


def test_gastm::longinteger_constructor_exists():
    assert callable(gastm::LongInteger.__init__)


def test_gastm::longinteger_constructor_args():
    sig = inspect.signature(gastm::LongInteger.__init__)
    params = list(sig.parameters.keys())



def test_gastm::integer_is_not_abstract():
    assert not inspect.isabstract(gastm::Integer)


def test_gastm::integer_constructor_exists():
    assert callable(gastm::Integer.__init__)


def test_gastm::integer_constructor_args():
    sig = inspect.signature(gastm::Integer.__init__)
    params = list(sig.parameters.keys())



def test_gastm::boolean_is_not_abstract():
    assert not inspect.isabstract(gastm::Boolean)


def test_gastm::boolean_constructor_exists():
    assert callable(gastm::Boolean.__init__)


def test_gastm::boolean_constructor_args():
    sig = inspect.signature(gastm::Boolean.__init__)
    params = list(sig.parameters.keys())



def test_gastm::longdouble_is_not_abstract():
    assert not inspect.isabstract(gastm::LongDouble)


def test_gastm::longdouble_constructor_exists():
    assert callable(gastm::LongDouble.__init__)


def test_gastm::longdouble_constructor_args():
    sig = inspect.signature(gastm::LongDouble.__init__)
    params = list(sig.parameters.keys())



def test_gastm::shortinteger_is_not_abstract():
    assert not inspect.isabstract(gastm::ShortInteger)


def test_gastm::shortinteger_constructor_exists():
    assert callable(gastm::ShortInteger.__init__)


def test_gastm::shortinteger_constructor_args():
    sig = inspect.signature(gastm::ShortInteger.__init__)
    params = list(sig.parameters.keys())



def test_gastm::float_is_not_abstract():
    assert not inspect.isabstract(gastm::Float)


def test_gastm::float_constructor_exists():
    assert callable(gastm::Float.__init__)


def test_gastm::float_constructor_args():
    sig = inspect.signature(gastm::Float.__init__)
    params = list(sig.parameters.keys())



def test_gastm::widecharacter_is_not_abstract():
    assert not inspect.isabstract(gastm::WideCharacter)


def test_gastm::widecharacter_constructor_exists():
    assert callable(gastm::WideCharacter.__init__)


def test_gastm::widecharacter_constructor_args():
    sig = inspect.signature(gastm::WideCharacter.__init__)
    params = list(sig.parameters.keys())



def test_gastm::double_is_not_abstract():
    assert not inspect.isabstract(gastm::Double)


def test_gastm::double_constructor_exists():
    assert callable(gastm::Double.__init__)


def test_gastm::double_constructor_args():
    sig = inspect.signature(gastm::Double.__init__)
    params = list(sig.parameters.keys())



def test_gastm::character_is_not_abstract():
    assert not inspect.isabstract(gastm::Character)


def test_gastm::character_constructor_exists():
    assert callable(gastm::Character.__init__)


def test_gastm::character_constructor_args():
    sig = inspect.signature(gastm::Character.__init__)
    params = list(sig.parameters.keys())



def test_gastm::string_is_not_abstract():
    assert not inspect.isabstract(gastm::String)


def test_gastm::string_constructor_exists():
    assert callable(gastm::String.__init__)


def test_gastm::string_constructor_args():
    sig = inspect.signature(gastm::String.__init__)
    params = list(sig.parameters.keys())



def test_gastm::void_is_not_abstract():
    assert not inspect.isabstract(gastm::Void)


def test_gastm::void_constructor_exists():
    assert callable(gastm::Void.__init__)


def test_gastm::void_constructor_args():
    sig = inspect.signature(gastm::Void.__init__)
    params = list(sig.parameters.keys())



def test_storagespecification_is_not_abstract():
    assert not inspect.isabstract(StorageSpecification)


def test_storagespecification_constructor_exists():
    assert callable(StorageSpecification.__init__)


def test_storagespecification_constructor_args():
    sig = inspect.signature(StorageSpecification.__init__)
    params = list(sig.parameters.keys())



def test_gastm::perclassmember_is_not_abstract():
    assert not inspect.isabstract(gastm::PerClassMember)


def test_gastm::perclassmember_constructor_exists():
    assert callable(gastm::PerClassMember.__init__)


def test_gastm::perclassmember_constructor_args():
    sig = inspect.signature(gastm::PerClassMember.__init__)
    params = list(sig.parameters.keys())



def test_gastm::functionpersistent_is_not_abstract():
    assert not inspect.isabstract(gastm::FunctionPersistent)


def test_gastm::functionpersistent_constructor_exists():
    assert callable(gastm::FunctionPersistent.__init__)


def test_gastm::functionpersistent_constructor_args():
    sig = inspect.signature(gastm::FunctionPersistent.__init__)
    params = list(sig.parameters.keys())



def test_gastm::filelocal_is_not_abstract():
    assert not inspect.isabstract(gastm::FileLocal)


def test_gastm::filelocal_constructor_exists():
    assert callable(gastm::FileLocal.__init__)


def test_gastm::filelocal_constructor_args():
    sig = inspect.signature(gastm::FileLocal.__init__)
    params = list(sig.parameters.keys())



def test_gastm::nodef_is_not_abstract():
    assert not inspect.isabstract(gastm::NoDef)


def test_gastm::nodef_constructor_exists():
    assert callable(gastm::NoDef.__init__)


def test_gastm::nodef_constructor_args():
    sig = inspect.signature(gastm::NoDef.__init__)
    params = list(sig.parameters.keys())



def test_gastm::external_is_not_abstract():
    assert not inspect.isabstract(gastm::External)


def test_gastm::external_constructor_exists():
    assert callable(gastm::External.__init__)


def test_gastm::external_constructor_args():
    sig = inspect.signature(gastm::External.__init__)
    params = list(sig.parameters.keys())



def test_forstatement_is_not_abstract():
    assert not inspect.isabstract(ForStatement)


def test_forstatement_constructor_exists():
    assert callable(ForStatement.__init__)


def test_forstatement_constructor_args():
    sig = inspect.signature(ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::forcheckafterstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::ForCheckAfterStatement)


def test_gastm::forcheckafterstatement_constructor_exists():
    assert callable(gastm::ForCheckAfterStatement.__init__)


def test_gastm::forcheckafterstatement_constructor_args():
    sig = inspect.signature(gastm::ForCheckAfterStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::forcheckbeforestatement_is_not_abstract():
    assert not inspect.isabstract(gastm::ForCheckBeforeStatement)


def test_gastm::forcheckbeforestatement_constructor_exists():
    assert callable(gastm::ForCheckBeforeStatement.__init__)


def test_gastm::forcheckbeforestatement_constructor_args():
    sig = inspect.signature(gastm::ForCheckBeforeStatement.__init__)
    params = list(sig.parameters.keys())



def test_accesskind_is_not_abstract():
    assert not inspect.isabstract(AccessKind)


def test_accesskind_constructor_exists():
    assert callable(AccessKind.__init__)


def test_accesskind_constructor_args():
    sig = inspect.signature(AccessKind.__init__)
    params = list(sig.parameters.keys())



def test_gastm::private_is_not_abstract():
    assert not inspect.isabstract(gastm::Private)


def test_gastm::private_constructor_exists():
    assert callable(gastm::Private.__init__)


def test_gastm::private_constructor_args():
    sig = inspect.signature(gastm::Private.__init__)
    params = list(sig.parameters.keys())



def test_gastm::protected_is_not_abstract():
    assert not inspect.isabstract(gastm::Protected)


def test_gastm::protected_constructor_exists():
    assert callable(gastm::Protected.__init__)


def test_gastm::protected_constructor_args():
    sig = inspect.signature(gastm::Protected.__init__)
    params = list(sig.parameters.keys())



def test_gastm::public_is_not_abstract():
    assert not inspect.isabstract(gastm::Public)


def test_gastm::public_constructor_exists():
    assert callable(gastm::Public.__init__)


def test_gastm::public_constructor_args():
    sig = inspect.signature(gastm::Public.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbclosecursorstatement_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBCloseCursorStatement)


def test_sastm::rdbclosecursorstatement_constructor_exists():
    assert callable(sastm::RDBCloseCursorStatement.__init__)


def test_sastm::rdbclosecursorstatement_constructor_args():
    sig = inspect.signature(sastm::RDBCloseCursorStatement.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbdeletestatement_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBDeleteStatement)


def test_sastm::rdbdeletestatement_constructor_exists():
    assert callable(sastm::RDBDeleteStatement.__init__)


def test_sastm::rdbdeletestatement_constructor_args():
    sig = inspect.signature(sastm::RDBDeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::accesskind_is_not_abstract():
    assert not inspect.isabstract(gastm::AccessKind)


def test_gastm::accesskind_constructor_exists():
    assert callable(gastm::AccessKind.__init__)


def test_gastm::accesskind_constructor_args():
    sig = inspect.signature(gastm::AccessKind.__init__)
    params = list(sig.parameters.keys())



def test_gastm::datatype_is_not_abstract():
    assert not inspect.isabstract(gastm::DataType)


def test_gastm::datatype_constructor_exists():
    assert callable(gastm::DataType.__init__)


def test_gastm::datatype_constructor_args():
    sig = inspect.signature(gastm::DataType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::storagespecification_is_not_abstract():
    assert not inspect.isabstract(gastm::StorageSpecification)


def test_gastm::storagespecification_constructor_exists():
    assert callable(gastm::StorageSpecification.__init__)


def test_gastm::storagespecification_constructor_args():
    sig = inspect.signature(gastm::StorageSpecification.__init__)
    params = list(sig.parameters.keys())



def test_gastm::othersyntaxobject_is_not_abstract():
    assert not inspect.isabstract(gastm::OtherSyntaxObject)


def test_gastm::othersyntaxobject_constructor_exists():
    assert callable(gastm::OtherSyntaxObject.__init__)


def test_gastm::othersyntaxobject_constructor_args():
    sig = inspect.signature(gastm::OtherSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_gastm::gastmsemanticobject_is_not_abstract():
    assert not inspect.isabstract(gastm::GASTMSemanticObject)


def test_gastm::gastmsemanticobject_constructor_exists():
    assert callable(gastm::GASTMSemanticObject.__init__)


def test_gastm::gastmsemanticobject_constructor_args():
    sig = inspect.signature(gastm::GASTMSemanticObject.__init__)
    params = list(sig.parameters.keys())



def test_gastm::gastmsourceobject_is_not_abstract():
    assert not inspect.isabstract(gastm::GASTMSourceObject)


def test_gastm::gastmsourceobject_constructor_exists():
    assert callable(gastm::GASTMSourceObject.__init__)


def test_gastm::gastmsourceobject_constructor_args():
    sig = inspect.signature(gastm::GASTMSourceObject.__init__)
    params = list(sig.parameters.keys())



def test_gastm::gastmobject_is_not_abstract():
    assert not inspect.isabstract(gastm::GASTMObject)


def test_gastm::gastmobject_constructor_exists():
    assert callable(gastm::GASTMObject.__init__)


def test_gastm::gastmobject_constructor_args():
    sig = inspect.signature(gastm::GASTMObject.__init__)
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



def test_sastm::rdbindexcolumn_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBIndexColumn)


def test_sastm::rdbindexcolumn_constructor_exists():
    assert callable(sastm::RDBIndexColumn.__init__)


def test_sastm::rdbindexcolumn_constructor_args():
    sig = inspect.signature(sastm::RDBIndexColumn.__init__)
    params = list(sig.parameters.keys())
    assert "AscendingOrDescending" in params, "Missing parameter 'AscendingOrDescending'"

def test_sastm::rdbindexcolumn_has_AscendingOrDescending():
    assert hasattr(sastm::RDBIndexColumn, "AscendingOrDescending")
    descriptor = None
    for klass in sastm::RDBIndexColumn.__mro__:
        if "AscendingOrDescending" in klass.__dict__:
            descriptor = klass.__dict__["AscendingOrDescending"]
            break
    assert isinstance(descriptor, property)



def test_gastm::virtualspecification_is_not_abstract():
    assert not inspect.isabstract(gastm::VirtualSpecification)


def test_gastm::virtualspecification_constructor_exists():
    assert callable(gastm::VirtualSpecification.__init__)


def test_gastm::virtualspecification_constructor_args():
    sig = inspect.signature(gastm::VirtualSpecification.__init__)
    params = list(sig.parameters.keys())



def test_gastm::name_is_not_abstract():
    assert not inspect.isabstract(gastm::Name)


def test_gastm::name_constructor_exists():
    assert callable(gastm::Name.__init__)


def test_gastm::name_constructor_args():
    sig = inspect.signature(gastm::Name.__init__)
    params = list(sig.parameters.keys())
    assert "nameString" in params, "Missing parameter 'nameString'"

def test_gastm::name_has_nameString():
    assert hasattr(gastm::Name, "nameString")
    descriptor = None
    for klass in gastm::Name.__mro__:
        if "nameString" in klass.__dict__:
            descriptor = klass.__dict__["nameString"]
            break
    assert isinstance(descriptor, property)



def test_sastm::rdbindex_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBIndex)


def test_sastm::rdbindex_constructor_exists():
    assert callable(sastm::RDBIndex.__init__)


def test_sastm::rdbindex_constructor_args():
    sig = inspect.signature(sastm::RDBIndex.__init__)
    params = list(sig.parameters.keys())
    assert "NotNull" in params, "Missing parameter 'NotNull'"
    assert "IsUnique" in params, "Missing parameter 'IsUnique'"

def test_sastm::rdbindex_has_NotNull():
    assert hasattr(sastm::RDBIndex, "NotNull")
    descriptor = None
    for klass in sastm::RDBIndex.__mro__:
        if "NotNull" in klass.__dict__:
            descriptor = klass.__dict__["NotNull"]
            break
    assert isinstance(descriptor, property)

def test_sastm::rdbindex_has_IsUnique():
    assert hasattr(sastm::RDBIndex, "IsUnique")
    descriptor = None
    for klass in sastm::RDBIndex.__mro__:
        if "IsUnique" in klass.__dict__:
            descriptor = klass.__dict__["IsUnique"]
            break
    assert isinstance(descriptor, property)



def test_gastm::functionmemberattribute_is_not_abstract():
    assert not inspect.isabstract(gastm::FunctionMemberAttribute)


def test_gastm::functionmemberattribute_constructor_exists():
    assert callable(gastm::FunctionMemberAttribute.__init__)


def test_gastm::functionmemberattribute_constructor_args():
    sig = inspect.signature(gastm::FunctionMemberAttribute.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbtrigger_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBTrigger)


def test_sastm::rdbtrigger_constructor_exists():
    assert callable(sastm::RDBTrigger.__init__)


def test_sastm::rdbtrigger_constructor_args():
    sig = inspect.signature(sastm::RDBTrigger.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbconstraint_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBConstraint)


def test_sastm::rdbconstraint_constructor_exists():
    assert callable(sastm::RDBConstraint.__init__)


def test_sastm::rdbconstraint_constructor_args():
    sig = inspect.signature(sastm::RDBConstraint.__init__)
    params = list(sig.parameters.keys())



def test_gastm::compilationunit_is_not_abstract():
    assert not inspect.isabstract(gastm::CompilationUnit)


def test_gastm::compilationunit_constructor_exists():
    assert callable(gastm::CompilationUnit.__init__)


def test_gastm::compilationunit_constructor_args():
    sig = inspect.signature(gastm::CompilationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"

def test_gastm::compilationunit_has_language():
    assert hasattr(gastm::CompilationUnit, "language")
    descriptor = None
    for klass in gastm::CompilationUnit.__mro__:
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



def test_gastm::gastmsyntaxobject_is_not_abstract():
    assert not inspect.isabstract(gastm::GASTMSyntaxObject)


def test_gastm::gastmsyntaxobject_constructor_exists():
    assert callable(gastm::GASTMSyntaxObject.__init__)


def test_gastm::gastmsyntaxobject_constructor_args():
    sig = inspect.signature(gastm::GASTMSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_scope_is_not_abstract():
    assert not inspect.isabstract(Scope)


def test_scope_constructor_exists():
    assert callable(Scope.__init__)


def test_scope_constructor_args():
    sig = inspect.signature(Scope.__init__)
    params = list(sig.parameters.keys())



def test_gastm::functionscope_is_not_abstract():
    assert not inspect.isabstract(gastm::FunctionScope)


def test_gastm::functionscope_constructor_exists():
    assert callable(gastm::FunctionScope.__init__)


def test_gastm::functionscope_constructor_args():
    sig = inspect.signature(gastm::FunctionScope.__init__)
    params = list(sig.parameters.keys())



def test_gastm::blockscope_is_not_abstract():
    assert not inspect.isabstract(gastm::BlockScope)


def test_gastm::blockscope_constructor_exists():
    assert callable(gastm::BlockScope.__init__)


def test_gastm::blockscope_constructor_args():
    sig = inspect.signature(gastm::BlockScope.__init__)
    params = list(sig.parameters.keys())



def test_gastm::aggregatescope_is_not_abstract():
    assert not inspect.isabstract(gastm::AggregateScope)


def test_gastm::aggregatescope_constructor_exists():
    assert callable(gastm::AggregateScope.__init__)


def test_gastm::aggregatescope_constructor_args():
    sig = inspect.signature(gastm::AggregateScope.__init__)
    params = list(sig.parameters.keys())



def test_gastm::programscope_is_not_abstract():
    assert not inspect.isabstract(gastm::ProgramScope)


def test_gastm::programscope_constructor_exists():
    assert callable(gastm::ProgramScope.__init__)


def test_gastm::programscope_constructor_args():
    sig = inspect.signature(gastm::ProgramScope.__init__)
    params = list(sig.parameters.keys())



def test_definitionobject_is_not_abstract():
    assert not inspect.isabstract(DefinitionObject)


def test_definitionobject_constructor_exists():
    assert callable(DefinitionObject.__init__)


def test_definitionobject_constructor_args():
    sig = inspect.signature(DefinitionObject.__init__)
    params = list(sig.parameters.keys())



def test_globalscope_is_not_abstract():
    assert not inspect.isabstract(GlobalScope)


def test_globalscope_constructor_exists():
    assert callable(GlobalScope.__init__)


def test_globalscope_constructor_args():
    sig = inspect.signature(GlobalScope.__init__)
    params = list(sig.parameters.keys())



def test_gastm::globalscope_is_not_abstract():
    assert not inspect.isabstract(gastm::GlobalScope)


def test_gastm::globalscope_constructor_exists():
    assert callable(gastm::GlobalScope.__init__)


def test_gastm::globalscope_constructor_args():
    sig = inspect.signature(gastm::GlobalScope.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_gastm::specificin_is_not_abstract():
    assert not inspect.isabstract(gastm::SpecificIn)


def test_gastm::specificin_constructor_exists():
    assert callable(gastm::SpecificIn.__init__)


def test_gastm::specificin_constructor_args():
    sig = inspect.signature(gastm::SpecificIn.__init__)
    params = list(sig.parameters.keys())



def test_gastm::specificlike_is_not_abstract():
    assert not inspect.isabstract(gastm::SpecificLike)


def test_gastm::specificlike_constructor_exists():
    assert callable(gastm::SpecificLike.__init__)


def test_gastm::specificlike_constructor_args():
    sig = inspect.signature(gastm::SpecificLike.__init__)
    params = list(sig.parameters.keys())



def test_gastm::notgreater_is_not_abstract():
    assert not inspect.isabstract(gastm::NotGreater)


def test_gastm::notgreater_constructor_exists():
    assert callable(gastm::NotGreater.__init__)


def test_gastm::notgreater_constructor_args():
    sig = inspect.signature(gastm::NotGreater.__init__)
    params = list(sig.parameters.keys())



def test_gastm::assign_is_not_abstract():
    assert not inspect.isabstract(gastm::Assign)


def test_gastm::assign_constructor_exists():
    assert callable(gastm::Assign.__init__)


def test_gastm::assign_constructor_args():
    sig = inspect.signature(gastm::Assign.__init__)
    params = list(sig.parameters.keys())



def test_gastm::divide_is_not_abstract():
    assert not inspect.isabstract(gastm::Divide)


def test_gastm::divide_constructor_exists():
    assert callable(gastm::Divide.__init__)


def test_gastm::divide_constructor_args():
    sig = inspect.signature(gastm::Divide.__init__)
    params = list(sig.parameters.keys())



def test_gastm::bitxor_is_not_abstract():
    assert not inspect.isabstract(gastm::BitXor)


def test_gastm::bitxor_constructor_exists():
    assert callable(gastm::BitXor.__init__)


def test_gastm::bitxor_constructor_args():
    sig = inspect.signature(gastm::BitXor.__init__)
    params = list(sig.parameters.keys())



def test_gastm::exponent_is_not_abstract():
    assert not inspect.isabstract(gastm::Exponent)


def test_gastm::exponent_constructor_exists():
    assert callable(gastm::Exponent.__init__)


def test_gastm::exponent_constructor_args():
    sig = inspect.signature(gastm::Exponent.__init__)
    params = list(sig.parameters.keys())



def test_gastm::less_is_not_abstract():
    assert not inspect.isabstract(gastm::Less)


def test_gastm::less_constructor_exists():
    assert callable(gastm::Less.__init__)


def test_gastm::less_constructor_args():
    sig = inspect.signature(gastm::Less.__init__)
    params = list(sig.parameters.keys())



def test_gastm::or_is_not_abstract():
    assert not inspect.isabstract(gastm::Or)


def test_gastm::or_constructor_exists():
    assert callable(gastm::Or.__init__)


def test_gastm::or_constructor_args():
    sig = inspect.signature(gastm::Or.__init__)
    params = list(sig.parameters.keys())



def test_gastm::equal_is_not_abstract():
    assert not inspect.isabstract(gastm::Equal)


def test_gastm::equal_constructor_exists():
    assert callable(gastm::Equal.__init__)


def test_gastm::equal_constructor_args():
    sig = inspect.signature(gastm::Equal.__init__)
    params = list(sig.parameters.keys())



def test_gastm::bitrightshift_is_not_abstract():
    assert not inspect.isabstract(gastm::BitRightShift)


def test_gastm::bitrightshift_constructor_exists():
    assert callable(gastm::BitRightShift.__init__)


def test_gastm::bitrightshift_constructor_args():
    sig = inspect.signature(gastm::BitRightShift.__init__)
    params = list(sig.parameters.keys())



def test_gastm::subtract_is_not_abstract():
    assert not inspect.isabstract(gastm::Subtract)


def test_gastm::subtract_constructor_exists():
    assert callable(gastm::Subtract.__init__)


def test_gastm::subtract_constructor_args():
    sig = inspect.signature(gastm::Subtract.__init__)
    params = list(sig.parameters.keys())



def test_gastm::add_is_not_abstract():
    assert not inspect.isabstract(gastm::Add)


def test_gastm::add_constructor_exists():
    assert callable(gastm::Add.__init__)


def test_gastm::add_constructor_args():
    sig = inspect.signature(gastm::Add.__init__)
    params = list(sig.parameters.keys())



def test_gastm::greater_is_not_abstract():
    assert not inspect.isabstract(gastm::Greater)


def test_gastm::greater_constructor_exists():
    assert callable(gastm::Greater.__init__)


def test_gastm::greater_constructor_args():
    sig = inspect.signature(gastm::Greater.__init__)
    params = list(sig.parameters.keys())



def test_gastm::specificgreaterequal_is_not_abstract():
    assert not inspect.isabstract(gastm::SpecificGreaterEqual)


def test_gastm::specificgreaterequal_constructor_exists():
    assert callable(gastm::SpecificGreaterEqual.__init__)


def test_gastm::specificgreaterequal_constructor_args():
    sig = inspect.signature(gastm::SpecificGreaterEqual.__init__)
    params = list(sig.parameters.keys())



def test_gastm::multiply_is_not_abstract():
    assert not inspect.isabstract(gastm::Multiply)


def test_gastm::multiply_constructor_exists():
    assert callable(gastm::Multiply.__init__)


def test_gastm::multiply_constructor_args():
    sig = inspect.signature(gastm::Multiply.__init__)
    params = list(sig.parameters.keys())



def test_gastm::specificconcatstring_is_not_abstract():
    assert not inspect.isabstract(gastm::SpecificConcatString)


def test_gastm::specificconcatstring_constructor_exists():
    assert callable(gastm::SpecificConcatString.__init__)


def test_gastm::specificconcatstring_constructor_args():
    sig = inspect.signature(gastm::SpecificConcatString.__init__)
    params = list(sig.parameters.keys())



def test_gastm::bitleftshift_is_not_abstract():
    assert not inspect.isabstract(gastm::BitLeftShift)


def test_gastm::bitleftshift_constructor_exists():
    assert callable(gastm::BitLeftShift.__init__)


def test_gastm::bitleftshift_constructor_args():
    sig = inspect.signature(gastm::BitLeftShift.__init__)
    params = list(sig.parameters.keys())



def test_gastm::specificlessequal_is_not_abstract():
    assert not inspect.isabstract(gastm::SpecificLessEqual)


def test_gastm::specificlessequal_constructor_exists():
    assert callable(gastm::SpecificLessEqual.__init__)


def test_gastm::specificlessequal_constructor_args():
    sig = inspect.signature(gastm::SpecificLessEqual.__init__)
    params = list(sig.parameters.keys())



def test_gastm::bitor_is_not_abstract():
    assert not inspect.isabstract(gastm::BitOr)


def test_gastm::bitor_constructor_exists():
    assert callable(gastm::BitOr.__init__)


def test_gastm::bitor_constructor_args():
    sig = inspect.signature(gastm::BitOr.__init__)
    params = list(sig.parameters.keys())



def test_gastm::notless_is_not_abstract():
    assert not inspect.isabstract(gastm::NotLess)


def test_gastm::notless_constructor_exists():
    assert callable(gastm::NotLess.__init__)


def test_gastm::notless_constructor_args():
    sig = inspect.signature(gastm::NotLess.__init__)
    params = list(sig.parameters.keys())



def test_gastm::bitand_is_not_abstract():
    assert not inspect.isabstract(gastm::BitAnd)


def test_gastm::bitand_constructor_exists():
    assert callable(gastm::BitAnd.__init__)


def test_gastm::bitand_constructor_args():
    sig = inspect.signature(gastm::BitAnd.__init__)
    params = list(sig.parameters.keys())



def test_gastm::and_is_not_abstract():
    assert not inspect.isabstract(gastm::And)


def test_gastm::and_constructor_exists():
    assert callable(gastm::And.__init__)


def test_gastm::and_constructor_args():
    sig = inspect.signature(gastm::And.__init__)
    params = list(sig.parameters.keys())



def test_gastm::notequal_is_not_abstract():
    assert not inspect.isabstract(gastm::NotEqual)


def test_gastm::notequal_constructor_exists():
    assert callable(gastm::NotEqual.__init__)


def test_gastm::notequal_constructor_args():
    sig = inspect.signature(gastm::NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_gastm::modulus_is_not_abstract():
    assert not inspect.isabstract(gastm::Modulus)


def test_gastm::modulus_constructor_exists():
    assert callable(gastm::Modulus.__init__)


def test_gastm::modulus_constructor_args():
    sig = inspect.signature(gastm::Modulus.__init__)
    params = list(sig.parameters.keys())



def test_gastm::operatorassign_is_not_abstract():
    assert not inspect.isabstract(gastm::OperatorAssign)


def test_gastm::operatorassign_constructor_exists():
    assert callable(gastm::OperatorAssign.__init__)


def test_gastm::operatorassign_constructor_args():
    sig = inspect.signature(gastm::OperatorAssign.__init__)
    params = list(sig.parameters.keys())



def test_actualparameter_is_not_abstract():
    assert not inspect.isabstract(ActualParameter)


def test_actualparameter_constructor_exists():
    assert callable(ActualParameter.__init__)


def test_actualparameter_constructor_args():
    sig = inspect.signature(ActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_gastm::missingactualparameter_is_not_abstract():
    assert not inspect.isabstract(gastm::MissingActualParameter)


def test_gastm::missingactualparameter_constructor_exists():
    assert callable(gastm::MissingActualParameter.__init__)


def test_gastm::missingactualparameter_constructor_args():
    sig = inspect.signature(gastm::MissingActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_gastm::actualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(gastm::ActualParameterExpression)


def test_gastm::actualparameterexpression_constructor_exists():
    assert callable(gastm::ActualParameterExpression.__init__)


def test_gastm::actualparameterexpression_constructor_args():
    sig = inspect.signature(gastm::ActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_identifierreference_is_not_abstract():
    assert not inspect.isabstract(IdentifierReference)


def test_identifierreference_constructor_exists():
    assert callable(IdentifierReference.__init__)


def test_identifierreference_constructor_args():
    sig = inspect.signature(IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbtablealias_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBTableAlias)


def test_sastm::rdbtablealias_constructor_exists():
    assert callable(sastm::RDBTableAlias.__init__)


def test_sastm::rdbtablealias_constructor_args():
    sig = inspect.signature(sastm::RDBTableAlias.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbtablereference_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBTableReference)


def test_sastm::rdbtablereference_constructor_exists():
    assert callable(sastm::RDBTableReference.__init__)


def test_sastm::rdbtablereference_constructor_args():
    sig = inspect.signature(sastm::RDBTableReference.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbcolumnreference_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBColumnReference)


def test_sastm::rdbcolumnreference_constructor_exists():
    assert callable(sastm::RDBColumnReference.__init__)


def test_sastm::rdbcolumnreference_constructor_args():
    sig = inspect.signature(sastm::RDBColumnReference.__init__)
    params = list(sig.parameters.keys())



def test_namereference_is_not_abstract():
    assert not inspect.isabstract(NameReference)


def test_namereference_constructor_exists():
    assert callable(NameReference.__init__)


def test_namereference_constructor_args():
    sig = inspect.signature(NameReference.__init__)
    params = list(sig.parameters.keys())



def test_gastm::identifierreference_is_not_abstract():
    assert not inspect.isabstract(gastm::IdentifierReference)


def test_gastm::identifierreference_constructor_exists():
    assert callable(gastm::IdentifierReference.__init__)


def test_gastm::identifierreference_constructor_args():
    sig = inspect.signature(gastm::IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_gastm::typequalifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(gastm::TypeQualifiedIdentifierReference)


def test_gastm::typequalifiedidentifierreference_constructor_exists():
    assert callable(gastm::TypeQualifiedIdentifierReference.__init__)


def test_gastm::typequalifiedidentifierreference_constructor_args():
    sig = inspect.signature(gastm::TypeQualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_gastm::qualifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(gastm::QualifiedIdentifierReference)


def test_gastm::qualifiedidentifierreference_constructor_exists():
    assert callable(gastm::QualifiedIdentifierReference.__init__)


def test_gastm::qualifiedidentifierreference_constructor_args():
    sig = inspect.signature(gastm::QualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_gastm::catchblock_is_not_abstract():
    assert not inspect.isabstract(gastm::CatchBlock)


def test_gastm::catchblock_constructor_exists():
    assert callable(gastm::CatchBlock.__init__)


def test_gastm::catchblock_constructor_args():
    sig = inspect.signature(gastm::CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_catchblock_is_not_abstract():
    assert not inspect.isabstract(CatchBlock)


def test_catchblock_constructor_exists():
    assert callable(CatchBlock.__init__)


def test_catchblock_constructor_args():
    sig = inspect.signature(CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_gastm::typescatchblock_is_not_abstract():
    assert not inspect.isabstract(gastm::TypesCatchBlock)


def test_gastm::typescatchblock_constructor_exists():
    assert callable(gastm::TypesCatchBlock.__init__)


def test_gastm::typescatchblock_constructor_args():
    sig = inspect.signature(gastm::TypesCatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_loopstatement_is_not_abstract():
    assert not inspect.isabstract(LoopStatement)


def test_loopstatement_constructor_exists():
    assert callable(LoopStatement.__init__)


def test_loopstatement_constructor_args():
    sig = inspect.signature(LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::dowhilestatement_is_not_abstract():
    assert not inspect.isabstract(gastm::DoWhileStatement)


def test_gastm::dowhilestatement_constructor_exists():
    assert callable(gastm::DoWhileStatement.__init__)


def test_gastm::dowhilestatement_constructor_args():
    sig = inspect.signature(gastm::DoWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::whilestatement_is_not_abstract():
    assert not inspect.isabstract(gastm::WhileStatement)


def test_gastm::whilestatement_constructor_exists():
    assert callable(gastm::WhileStatement.__init__)


def test_gastm::whilestatement_constructor_args():
    sig = inspect.signature(gastm::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::forstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::ForStatement)


def test_gastm::forstatement_constructor_exists():
    assert callable(gastm::ForStatement.__init__)


def test_gastm::forstatement_constructor_args():
    sig = inspect.signature(gastm::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::variablecatchblock_is_not_abstract():
    assert not inspect.isabstract(gastm::VariableCatchBlock)


def test_gastm::variablecatchblock_constructor_exists():
    assert callable(gastm::VariableCatchBlock.__init__)


def test_gastm::variablecatchblock_constructor_args():
    sig = inspect.signature(gastm::VariableCatchBlock.__init__)
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



def test_gastm::switchcase_is_not_abstract():
    assert not inspect.isabstract(gastm::SwitchCase)


def test_gastm::switchcase_constructor_exists():
    assert callable(gastm::SwitchCase.__init__)


def test_gastm::switchcase_constructor_args():
    sig = inspect.signature(gastm::SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_switchcase_is_not_abstract():
    assert not inspect.isabstract(SwitchCase)


def test_switchcase_constructor_exists():
    assert callable(SwitchCase.__init__)


def test_switchcase_constructor_args():
    sig = inspect.signature(SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_gastm::defaultblock_is_not_abstract():
    assert not inspect.isabstract(gastm::DefaultBlock)


def test_gastm::defaultblock_constructor_exists():
    assert callable(gastm::DefaultBlock.__init__)


def test_gastm::defaultblock_constructor_args():
    sig = inspect.signature(gastm::DefaultBlock.__init__)
    params = list(sig.parameters.keys())



def test_gastm::caseblock_is_not_abstract():
    assert not inspect.isabstract(gastm::CaseBlock)


def test_gastm::caseblock_constructor_exists():
    assert callable(gastm::CaseBlock.__init__)


def test_gastm::caseblock_constructor_args():
    sig = inspect.signature(gastm::CaseBlock.__init__)
    params = list(sig.parameters.keys())



def test_labelaccess_is_not_abstract():
    assert not inspect.isabstract(LabelAccess)


def test_labelaccess_constructor_exists():
    assert callable(LabelAccess.__init__)


def test_labelaccess_constructor_args():
    sig = inspect.signature(LabelAccess.__init__)
    params = list(sig.parameters.keys())



def test_gastm::dimension_is_not_abstract():
    assert not inspect.isabstract(gastm::Dimension)


def test_gastm::dimension_constructor_exists():
    assert callable(gastm::Dimension.__init__)


def test_gastm::dimension_constructor_args():
    sig = inspect.signature(gastm::Dimension.__init__)
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



def test_gastm::pointertype_is_not_abstract():
    assert not inspect.isabstract(gastm::PointerType)


def test_gastm::pointertype_constructor_exists():
    assert callable(gastm::PointerType.__init__)


def test_gastm::pointertype_constructor_args():
    sig = inspect.signature(gastm::PointerType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::collectiontype_is_not_abstract():
    assert not inspect.isabstract(gastm::CollectionType)


def test_gastm::collectiontype_constructor_exists():
    assert callable(gastm::CollectionType.__init__)


def test_gastm::collectiontype_constructor_args():
    sig = inspect.signature(gastm::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::rangetype_is_not_abstract():
    assert not inspect.isabstract(gastm::RangeType)


def test_gastm::rangetype_constructor_exists():
    assert callable(gastm::RangeType.__init__)


def test_gastm::rangetype_constructor_args():
    sig = inspect.signature(gastm::RangeType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::referencetype_is_not_abstract():
    assert not inspect.isabstract(gastm::ReferenceType)


def test_gastm::referencetype_constructor_exists():
    assert callable(gastm::ReferenceType.__init__)


def test_gastm::referencetype_constructor_args():
    sig = inspect.signature(gastm::ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::arraytype_is_not_abstract():
    assert not inspect.isabstract(gastm::ArrayType)


def test_gastm::arraytype_constructor_exists():
    assert callable(gastm::ArrayType.__init__)


def test_gastm::arraytype_constructor_args():
    sig = inspect.signature(gastm::ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_aggregatescope_is_not_abstract():
    assert not inspect.isabstract(AggregateScope)


def test_aggregatescope_constructor_exists():
    assert callable(AggregateScope.__init__)


def test_aggregatescope_constructor_args():
    sig = inspect.signature(AggregateScope.__init__)
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



def test_sastm::rdbraw_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBRaw)


def test_sastm::rdbraw_constructor_exists():
    assert callable(sastm::RDBRaw.__init__)


def test_sastm::rdbraw_constructor_args():
    sig = inspect.signature(sastm::RDBRaw.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbboolean_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBBoolean)


def test_sastm::rdbboolean_constructor_exists():
    assert callable(sastm::RDBBoolean.__init__)


def test_sastm::rdbboolean_constructor_args():
    sig = inspect.signature(sastm::RDBBoolean.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbclob_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBClob)


def test_sastm::rdbclob_constructor_exists():
    assert callable(sastm::RDBClob.__init__)


def test_sastm::rdbclob_constructor_args():
    sig = inspect.signature(sastm::RDBClob.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbrowid_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBRowid)


def test_sastm::rdbrowid_constructor_exists():
    assert callable(sastm::RDBRowid.__init__)


def test_sastm::rdbrowid_constructor_args():
    sig = inspect.signature(sastm::RDBRowid.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbtabletype_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBTableType)


def test_sastm::rdbtabletype_constructor_exists():
    assert callable(sastm::RDBTableType.__init__)


def test_sastm::rdbtabletype_constructor_args():
    sig = inspect.signature(sastm::RDBTableType.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbdatabasetype_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBDataBaseType)


def test_sastm::rdbdatabasetype_constructor_exists():
    assert callable(sastm::RDBDataBaseType.__init__)


def test_sastm::rdbdatabasetype_constructor_args():
    sig = inspect.signature(sastm::RDBDataBaseType.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbtimestamp_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBTimestamp)


def test_sastm::rdbtimestamp_constructor_exists():
    assert callable(sastm::RDBTimestamp.__init__)


def test_sastm::rdbtimestamp_constructor_args():
    sig = inspect.signature(sastm::RDBTimestamp.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbchar_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBChar)


def test_sastm::rdbchar_constructor_exists():
    assert callable(sastm::RDBChar.__init__)


def test_sastm::rdbchar_constructor_args():
    sig = inspect.signature(sastm::RDBChar.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbvarchar_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBVarchar)


def test_sastm::rdbvarchar_constructor_exists():
    assert callable(sastm::RDBVarchar.__init__)


def test_sastm::rdbvarchar_constructor_args():
    sig = inspect.signature(sastm::RDBVarchar.__init__)
    params = list(sig.parameters.keys())



def test_gastm::aggregatetype_is_not_abstract():
    assert not inspect.isabstract(gastm::AggregateType)


def test_gastm::aggregatetype_constructor_exists():
    assert callable(gastm::AggregateType.__init__)


def test_gastm::aggregatetype_constructor_args():
    sig = inspect.signature(gastm::AggregateType.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbnumber_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBNumber)


def test_sastm::rdbnumber_constructor_exists():
    assert callable(sastm::RDBNumber.__init__)


def test_sastm::rdbnumber_constructor_args():
    sig = inspect.signature(sastm::RDBNumber.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdblong_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBLong)


def test_sastm::rdblong_constructor_exists():
    assert callable(sastm::RDBLong.__init__)


def test_sastm::rdblong_constructor_args():
    sig = inspect.signature(sastm::RDBLong.__init__)
    params = list(sig.parameters.keys())



def test_gastm::enumtype_is_not_abstract():
    assert not inspect.isabstract(gastm::EnumType)


def test_gastm::enumtype_constructor_exists():
    assert callable(gastm::EnumType.__init__)


def test_gastm::enumtype_constructor_args():
    sig = inspect.signature(gastm::EnumType.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbstring_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBString)


def test_sastm::rdbstring_constructor_exists():
    assert callable(sastm::RDBString.__init__)


def test_sastm::rdbstring_constructor_args():
    sig = inspect.signature(sastm::RDBString.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbreal_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBReal)


def test_sastm::rdbreal_constructor_exists():
    assert callable(sastm::RDBReal.__init__)


def test_sastm::rdbreal_constructor_args():
    sig = inspect.signature(sastm::RDBReal.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbblob_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBBlob)


def test_sastm::rdbblob_constructor_exists():
    assert callable(sastm::RDBBlob.__init__)


def test_sastm::rdbblob_constructor_args():
    sig = inspect.signature(sastm::RDBBlob.__init__)
    params = list(sig.parameters.keys())



def test_gastm::exceptiontype_is_not_abstract():
    assert not inspect.isabstract(gastm::ExceptionType)


def test_gastm::exceptiontype_constructor_exists():
    assert callable(gastm::ExceptionType.__init__)


def test_gastm::exceptiontype_constructor_args():
    sig = inspect.signature(gastm::ExceptionType.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbdecimal_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBDecimal)


def test_sastm::rdbdecimal_constructor_exists():
    assert callable(sastm::RDBDecimal.__init__)


def test_sastm::rdbdecimal_constructor_args():
    sig = inspect.signature(sastm::RDBDecimal.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbnclob_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBNClob)


def test_sastm::rdbnclob_constructor_exists():
    assert callable(sastm::RDBNClob.__init__)


def test_sastm::rdbnclob_constructor_args():
    sig = inspect.signature(sastm::RDBNClob.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbinteger_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBInteger)


def test_sastm::rdbinteger_constructor_exists():
    assert callable(sastm::RDBInteger.__init__)


def test_sastm::rdbinteger_constructor_args():
    sig = inspect.signature(sastm::RDBInteger.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbint_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBInt)


def test_sastm::rdbint_constructor_exists():
    assert callable(sastm::RDBInt.__init__)


def test_sastm::rdbint_constructor_args():
    sig = inspect.signature(sastm::RDBInt.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbusertype_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBUserType)


def test_sastm::rdbusertype_constructor_exists():
    assert callable(sastm::RDBUserType.__init__)


def test_sastm::rdbusertype_constructor_args():
    sig = inspect.signature(sastm::RDBUserType.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbviewtype_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBViewType)


def test_sastm::rdbviewtype_constructor_exists():
    assert callable(sastm::RDBViewType.__init__)


def test_sastm::rdbviewtype_constructor_args():
    sig = inspect.signature(sastm::RDBViewType.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbbfile_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBBFile)


def test_sastm::rdbbfile_constructor_exists():
    assert callable(sastm::RDBBFile.__init__)


def test_sastm::rdbbfile_constructor_args():
    sig = inspect.signature(sastm::RDBBFile.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbfloat_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBFloat)


def test_sastm::rdbfloat_constructor_exists():
    assert callable(sastm::RDBFloat.__init__)


def test_sastm::rdbfloat_constructor_args():
    sig = inspect.signature(sastm::RDBFloat.__init__)
    params = list(sig.parameters.keys())



def test_gastm::constructedtype_is_not_abstract():
    assert not inspect.isabstract(gastm::ConstructedType)


def test_gastm::constructedtype_constructor_exists():
    assert callable(gastm::ConstructedType.__init__)


def test_gastm::constructedtype_constructor_args():
    sig = inspect.signature(gastm::ConstructedType.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbdate_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBDate)


def test_sastm::rdbdate_constructor_exists():
    assert callable(sastm::RDBDate.__init__)


def test_sastm::rdbdate_constructor_args():
    sig = inspect.signature(sastm::RDBDate.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbcursortype_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBCursorType)


def test_sastm::rdbcursortype_constructor_exists():
    assert callable(sastm::RDBCursorType.__init__)


def test_sastm::rdbcursortype_constructor_args():
    sig = inspect.signature(sastm::RDBCursorType.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbtablespacetype_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBTableSpaceType)


def test_sastm::rdbtablespacetype_constructor_exists():
    assert callable(sastm::RDBTableSpaceType.__init__)


def test_sastm::rdbtablespacetype_constructor_args():
    sig = inspect.signature(sastm::RDBTableSpaceType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::primitivetype_is_not_abstract():
    assert not inspect.isabstract(gastm::PrimitiveType)


def test_gastm::primitivetype_constructor_exists():
    assert callable(gastm::PrimitiveType.__init__)


def test_gastm::primitivetype_constructor_args():
    sig = inspect.signature(gastm::PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "isSigned" in params, "Missing parameter 'isSigned'"

def test_gastm::primitivetype_has_isSigned():
    assert hasattr(gastm::PrimitiveType, "isSigned")
    descriptor = None
    for klass in gastm::PrimitiveType.__mro__:
        if "isSigned" in klass.__dict__:
            descriptor = klass.__dict__["isSigned"]
            break
    assert isinstance(descriptor, property)



def test_gastm::derivesfrom_is_not_abstract():
    assert not inspect.isabstract(gastm::DerivesFrom)


def test_gastm::derivesfrom_constructor_exists():
    assert callable(gastm::DerivesFrom.__init__)


def test_gastm::derivesfrom_constructor_args():
    sig = inspect.signature(gastm::DerivesFrom.__init__)
    params = list(sig.parameters.keys())
    assert "isVirtual" in params, "Missing parameter 'isVirtual'"

def test_gastm::derivesfrom_has_isVirtual():
    assert hasattr(gastm::DerivesFrom, "isVirtual")
    descriptor = None
    for klass in gastm::DerivesFrom.__mro__:
        if "isVirtual" in klass.__dict__:
            descriptor = klass.__dict__["isVirtual"]
            break
    assert isinstance(descriptor, property)



def test_derivesfrom_is_not_abstract():
    assert not inspect.isabstract(DerivesFrom)


def test_derivesfrom_constructor_exists():
    assert callable(DerivesFrom.__init__)


def test_derivesfrom_constructor_args():
    sig = inspect.signature(DerivesFrom.__init__)
    params = list(sig.parameters.keys())



def test_gastm::namedtype_is_not_abstract():
    assert not inspect.isabstract(gastm::NamedType)


def test_gastm::namedtype_constructor_exists():
    assert callable(gastm::NamedType.__init__)


def test_gastm::namedtype_constructor_args():
    sig = inspect.signature(gastm::NamedType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::formalparametertype_is_not_abstract():
    assert not inspect.isabstract(gastm::FormalParameterType)


def test_gastm::formalparametertype_constructor_exists():
    assert callable(gastm::FormalParameterType.__init__)


def test_gastm::formalparametertype_constructor_args():
    sig = inspect.signature(gastm::FormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_formalparametertype_is_not_abstract():
    assert not inspect.isabstract(FormalParameterType)


def test_formalparametertype_constructor_exists():
    assert callable(FormalParameterType.__init__)


def test_formalparametertype_constructor_args():
    sig = inspect.signature(FormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::byvalueformalparametertype_is_not_abstract():
    assert not inspect.isabstract(gastm::ByValueFormalParameterType)


def test_gastm::byvalueformalparametertype_constructor_exists():
    assert callable(gastm::ByValueFormalParameterType.__init__)


def test_gastm::byvalueformalparametertype_constructor_args():
    sig = inspect.signature(gastm::ByValueFormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::byreferenceformalparametertype_is_not_abstract():
    assert not inspect.isabstract(gastm::ByReferenceFormalParameterType)


def test_gastm::byreferenceformalparametertype_constructor_exists():
    assert callable(gastm::ByReferenceFormalParameterType.__init__)


def test_gastm::byreferenceformalparametertype_constructor_args():
    sig = inspect.signature(gastm::ByReferenceFormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_gastm::labeltype_is_not_abstract():
    assert not inspect.isabstract(gastm::LabelType)


def test_gastm::labeltype_constructor_exists():
    assert callable(gastm::LabelType.__init__)


def test_gastm::labeltype_constructor_args():
    sig = inspect.signature(gastm::LabelType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::functiontype_is_not_abstract():
    assert not inspect.isabstract(gastm::FunctionType)


def test_gastm::functiontype_constructor_exists():
    assert callable(gastm::FunctionType.__init__)


def test_gastm::functiontype_constructor_args():
    sig = inspect.signature(gastm::FunctionType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::namespacetype_is_not_abstract():
    assert not inspect.isabstract(gastm::NameSpaceType)


def test_gastm::namespacetype_constructor_exists():
    assert callable(gastm::NameSpaceType.__init__)


def test_gastm::namespacetype_constructor_args():
    sig = inspect.signature(gastm::NameSpaceType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::typereference_is_not_abstract():
    assert not inspect.isabstract(gastm::TypeReference)


def test_gastm::typereference_constructor_exists():
    assert callable(gastm::TypeReference.__init__)


def test_gastm::typereference_constructor_args():
    sig = inspect.signature(gastm::TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_gastm::namespacedefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::NameSpaceDefinition)


def test_gastm::namespacedefinition_constructor_exists():
    assert callable(gastm::NameSpaceDefinition.__init__)


def test_gastm::namespacedefinition_constructor_args():
    sig = inspect.signature(gastm::NameSpaceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_aggregatetype_is_not_abstract():
    assert not inspect.isabstract(AggregateType)


def test_aggregatetype_constructor_exists():
    assert callable(AggregateType.__init__)


def test_aggregatetype_constructor_args():
    sig = inspect.signature(AggregateType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::uniontype_is_not_abstract():
    assert not inspect.isabstract(gastm::UnionType)


def test_gastm::uniontype_constructor_exists():
    assert callable(gastm::UnionType.__init__)


def test_gastm::uniontype_constructor_args():
    sig = inspect.signature(gastm::UnionType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::structuretype_is_not_abstract():
    assert not inspect.isabstract(gastm::StructureType)


def test_gastm::structuretype_constructor_exists():
    assert callable(gastm::StructureType.__init__)


def test_gastm::structuretype_constructor_args():
    sig = inspect.signature(gastm::StructureType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::classtype_is_not_abstract():
    assert not inspect.isabstract(gastm::ClassType)


def test_gastm::classtype_constructor_exists():
    assert callable(gastm::ClassType.__init__)


def test_gastm::classtype_constructor_args():
    sig = inspect.signature(gastm::ClassType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::annotationtype_is_not_abstract():
    assert not inspect.isabstract(gastm::AnnotationType)


def test_gastm::annotationtype_constructor_exists():
    assert callable(gastm::AnnotationType.__init__)


def test_gastm::annotationtype_constructor_args():
    sig = inspect.signature(gastm::AnnotationType.__init__)
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



def test_gastm::aggregatetypedefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::AggregateTypeDefinition)


def test_gastm::aggregatetypedefinition_constructor_exists():
    assert callable(gastm::AggregateTypeDefinition.__init__)


def test_gastm::aggregatetypedefinition_constructor_args():
    sig = inspect.signature(gastm::AggregateTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm::namedtypedefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::NamedTypeDefinition)


def test_gastm::namedtypedefinition_constructor_exists():
    assert callable(gastm::NamedTypeDefinition.__init__)


def test_gastm::namedtypedefinition_constructor_args():
    sig = inspect.signature(gastm::NamedTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm::typedefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::TypeDefinition)


def test_gastm::typedefinition_constructor_exists():
    assert callable(gastm::TypeDefinition.__init__)


def test_gastm::typedefinition_constructor_args():
    sig = inspect.signature(gastm::TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_datadefinition_is_not_abstract():
    assert not inspect.isabstract(DataDefinition)


def test_datadefinition_constructor_exists():
    assert callable(DataDefinition.__init__)


def test_datadefinition_constructor_args():
    sig = inspect.signature(DataDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm::variabledefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::VariableDefinition)


def test_gastm::variabledefinition_constructor_exists():
    assert callable(gastm::VariableDefinition.__init__)


def test_gastm::variabledefinition_constructor_args():
    sig = inspect.signature(gastm::VariableDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm::formalparameterdefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::FormalParameterDefinition)


def test_gastm::formalparameterdefinition_constructor_exists():
    assert callable(gastm::FormalParameterDefinition.__init__)


def test_gastm::formalparameterdefinition_constructor_args():
    sig = inspect.signature(gastm::FormalParameterDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm::bitfielddefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::BitFieldDefinition)


def test_gastm::bitfielddefinition_constructor_exists():
    assert callable(gastm::BitFieldDefinition.__init__)


def test_gastm::bitfielddefinition_constructor_args():
    sig = inspect.signature(gastm::BitFieldDefinition.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::namereference_is_not_abstract():
    assert not inspect.isabstract(gastm::NameReference)


def test_gastm::namereference_constructor_exists():
    assert callable(gastm::NameReference.__init__)


def test_gastm::namereference_constructor_args():
    sig = inspect.signature(gastm::NameReference.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbhostvariableexpression_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBHostVariableExpression)


def test_sastm::rdbhostvariableexpression_constructor_exists():
    assert callable(sastm::RDBHostVariableExpression.__init__)


def test_sastm::rdbhostvariableexpression_constructor_args():
    sig = inspect.signature(sastm::RDBHostVariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(gastm::UnaryExpression)


def test_gastm::unaryexpression_constructor_exists():
    assert callable(gastm::UnaryExpression.__init__)


def test_gastm::unaryexpression_constructor_args():
    sig = inspect.signature(gastm::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(gastm::BinaryExpression)


def test_gastm::binaryexpression_constructor_exists():
    assert callable(gastm::BinaryExpression.__init__)


def test_gastm::binaryexpression_constructor_args():
    sig = inspect.signature(gastm::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::functioncallexpression_is_not_abstract():
    assert not inspect.isabstract(gastm::FunctionCallExpression)


def test_gastm::functioncallexpression_constructor_exists():
    assert callable(gastm::FunctionCallExpression.__init__)


def test_gastm::functioncallexpression_constructor_args():
    sig = inspect.signature(gastm::FunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::arrayaccess_is_not_abstract():
    assert not inspect.isabstract(gastm::ArrayAccess)


def test_gastm::arrayaccess_constructor_exists():
    assert callable(gastm::ArrayAccess.__init__)


def test_gastm::arrayaccess_constructor_args():
    sig = inspect.signature(gastm::ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_gastm::literal_is_not_abstract():
    assert not inspect.isabstract(gastm::Literal)


def test_gastm::literal_constructor_exists():
    assert callable(gastm::Literal.__init__)


def test_gastm::literal_constructor_args():
    sig = inspect.signature(gastm::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_gastm::literal_has_value():
    assert hasattr(gastm::Literal, "value")
    descriptor = None
    for klass in gastm::Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_gastm::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(gastm::ConditionalExpression)


def test_gastm::conditionalexpression_constructor_exists():
    assert callable(gastm::ConditionalExpression.__init__)


def test_gastm::conditionalexpression_constructor_args():
    sig = inspect.signature(gastm::ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::labelaccess_is_not_abstract():
    assert not inspect.isabstract(gastm::LabelAccess)


def test_gastm::labelaccess_constructor_exists():
    assert callable(gastm::LabelAccess.__init__)


def test_gastm::labelaccess_constructor_args():
    sig = inspect.signature(gastm::LabelAccess.__init__)
    params = list(sig.parameters.keys())



def test_gastm::aggregateexpression_is_not_abstract():
    assert not inspect.isabstract(gastm::AggregateExpression)


def test_gastm::aggregateexpression_constructor_exists():
    assert callable(gastm::AggregateExpression.__init__)


def test_gastm::aggregateexpression_constructor_args():
    sig = inspect.signature(gastm::AggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::annotationexpression_is_not_abstract():
    assert not inspect.isabstract(gastm::AnnotationExpression)


def test_gastm::annotationexpression_constructor_exists():
    assert callable(gastm::AnnotationExpression.__init__)


def test_gastm::annotationexpression_constructor_args():
    sig = inspect.signature(gastm::AnnotationExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::rangeexpression_is_not_abstract():
    assert not inspect.isabstract(gastm::RangeExpression)


def test_gastm::rangeexpression_constructor_exists():
    assert callable(gastm::RangeExpression.__init__)


def test_gastm::rangeexpression_constructor_args():
    sig = inspect.signature(gastm::RangeExpression.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbselectexpression_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBSelectExpression)


def test_sastm::rdbselectexpression_constructor_exists():
    assert callable(sastm::RDBSelectExpression.__init__)


def test_sastm::rdbselectexpression_constructor_args():
    sig = inspect.signature(sastm::RDBSelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::newexpression_is_not_abstract():
    assert not inspect.isabstract(gastm::NewExpression)


def test_gastm::newexpression_constructor_exists():
    assert callable(gastm::NewExpression.__init__)


def test_gastm::newexpression_constructor_args():
    sig = inspect.signature(gastm::NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::castexpression_is_not_abstract():
    assert not inspect.isabstract(gastm::CastExpression)


def test_gastm::castexpression_constructor_exists():
    assert callable(gastm::CastExpression.__init__)


def test_gastm::castexpression_constructor_args():
    sig = inspect.signature(gastm::CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastmsyntaxobject_is_not_abstract():
    assert not inspect.isabstract(GASTMSyntaxObject)


def test_gastmsyntaxobject_constructor_exists():
    assert callable(GASTMSyntaxObject.__init__)


def test_gastmsyntaxobject_constructor_args():
    sig = inspect.signature(GASTMSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_gastm::expression_is_not_abstract():
    assert not inspect.isabstract(gastm::Expression)


def test_gastm::expression_constructor_exists():
    assert callable(gastm::Expression.__init__)


def test_gastm::expression_constructor_args():
    sig = inspect.signature(gastm::Expression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::preprocessorelement_is_not_abstract():
    assert not inspect.isabstract(gastm::PreprocessorElement)


def test_gastm::preprocessorelement_constructor_exists():
    assert callable(gastm::PreprocessorElement.__init__)


def test_gastm::preprocessorelement_constructor_args():
    sig = inspect.signature(gastm::PreprocessorElement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::statement_is_not_abstract():
    assert not inspect.isabstract(gastm::Statement)


def test_gastm::statement_constructor_exists():
    assert callable(gastm::Statement.__init__)


def test_gastm::statement_constructor_args():
    sig = inspect.signature(gastm::Statement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::definitionobject_is_not_abstract():
    assert not inspect.isabstract(gastm::DefinitionObject)


def test_gastm::definitionobject_constructor_exists():
    assert callable(gastm::DefinitionObject.__init__)


def test_gastm::definitionobject_constructor_args():
    sig = inspect.signature(gastm::DefinitionObject.__init__)
    params = list(sig.parameters.keys())



def test_gastm::type_is_not_abstract():
    assert not inspect.isabstract(gastm::Type)


def test_gastm::type_constructor_exists():
    assert callable(gastm::Type.__init__)


def test_gastm::type_constructor_args():
    sig = inspect.signature(gastm::Type.__init__)
    params = list(sig.parameters.keys())
    assert "isConst" in params, "Missing parameter 'isConst'"
    assert "isVolatile" in params, "Missing parameter 'isVolatile'"

def test_gastm::type_has_isConst():
    assert hasattr(gastm::Type, "isConst")
    descriptor = None
    for klass in gastm::Type.__mro__:
        if "isConst" in klass.__dict__:
            descriptor = klass.__dict__["isConst"]
            break
    assert isinstance(descriptor, property)

def test_gastm::type_has_isVolatile():
    assert hasattr(gastm::Type, "isVolatile")
    descriptor = None
    for klass in gastm::Type.__mro__:
        if "isVolatile" in klass.__dict__:
            descriptor = klass.__dict__["isVolatile"]
            break
    assert isinstance(descriptor, property)



def test_gastm::comment_is_not_abstract():
    assert not inspect.isabstract(gastm::Comment)


def test_gastm::comment_constructor_exists():
    assert callable(gastm::Comment.__init__)


def test_gastm::comment_constructor_args():
    sig = inspect.signature(gastm::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_gastm::comment_has_text():
    assert hasattr(gastm::Comment, "text")
    descriptor = None
    for klass in gastm::Comment.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_gastm::macrodefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::MacroDefinition)


def test_gastm::macrodefinition_constructor_exists():
    assert callable(gastm::MacroDefinition.__init__)


def test_gastm::macrodefinition_constructor_args():
    sig = inspect.signature(gastm::MacroDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "macroName" in params, "Missing parameter 'macroName'"

def test_gastm::macrodefinition_has_body():
    assert hasattr(gastm::MacroDefinition, "body")
    descriptor = None
    for klass in gastm::MacroDefinition.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_gastm::macrodefinition_has_macroName():
    assert hasattr(gastm::MacroDefinition, "macroName")
    descriptor = None
    for klass in gastm::MacroDefinition.__mro__:
        if "macroName" in klass.__dict__:
            descriptor = klass.__dict__["macroName"]
            break
    assert isinstance(descriptor, property)



def test_macrodefinition_is_not_abstract():
    assert not inspect.isabstract(MacroDefinition)


def test_macrodefinition_constructor_exists():
    assert callable(MacroDefinition.__init__)


def test_macrodefinition_constructor_args():
    sig = inspect.signature(MacroDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm::macrocall_is_not_abstract():
    assert not inspect.isabstract(gastm::MacroCall)


def test_gastm::macrocall_constructor_exists():
    assert callable(gastm::MacroCall.__init__)


def test_gastm::macrocall_constructor_args():
    sig = inspect.signature(gastm::MacroCall.__init__)
    params = list(sig.parameters.keys())



def test_gastm::includeunit_is_not_abstract():
    assert not inspect.isabstract(gastm::IncludeUnit)


def test_gastm::includeunit_constructor_exists():
    assert callable(gastm::IncludeUnit.__init__)


def test_gastm::includeunit_constructor_args():
    sig = inspect.signature(gastm::IncludeUnit.__init__)
    params = list(sig.parameters.keys())



def test_labeltype_is_not_abstract():
    assert not inspect.isabstract(LabelType)


def test_labeltype_constructor_exists():
    assert callable(LabelType.__init__)


def test_labeltype_constructor_args():
    sig = inspect.signature(LabelType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::labeldefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::LabelDefinition)


def test_gastm::labeldefinition_constructor_exists():
    assert callable(gastm::LabelDefinition.__init__)


def test_gastm::labeldefinition_constructor_args():
    sig = inspect.signature(gastm::LabelDefinition.__init__)
    params = list(sig.parameters.keys())



def test_namespacetype_is_not_abstract():
    assert not inspect.isabstract(NameSpaceType)


def test_namespacetype_constructor_exists():
    assert callable(NameSpaceType.__init__)


def test_namespacetype_constructor_args():
    sig = inspect.signature(NameSpaceType.__init__)
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



def test_gastm::formalparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(gastm::FormalParameterDeclaration)


def test_gastm::formalparameterdeclaration_constructor_exists():
    assert callable(gastm::FormalParameterDeclaration.__init__)


def test_gastm::formalparameterdeclaration_constructor_args():
    sig = inspect.signature(gastm::FormalParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_gastm::functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(gastm::FunctionDeclaration)


def test_gastm::functiondeclaration_constructor_exists():
    assert callable(gastm::FunctionDeclaration.__init__)


def test_gastm::functiondeclaration_constructor_args():
    sig = inspect.signature(gastm::FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_gastm::enumliteraldefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::EnumLiteralDefinition)


def test_gastm::enumliteraldefinition_constructor_exists():
    assert callable(gastm::EnumLiteralDefinition.__init__)


def test_gastm::enumliteraldefinition_constructor_args():
    sig = inspect.signature(gastm::EnumLiteralDefinition.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbtabledefinition_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBTableDefinition)


def test_sastm::rdbtabledefinition_constructor_exists():
    assert callable(sastm::RDBTableDefinition.__init__)


def test_sastm::rdbtabledefinition_constructor_args():
    sig = inspect.signature(sastm::RDBTableDefinition.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbcursordefinition_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBCursorDefinition)


def test_sastm::rdbcursordefinition_constructor_exists():
    assert callable(sastm::RDBCursorDefinition.__init__)


def test_sastm::rdbcursordefinition_constructor_args():
    sig = inspect.signature(sastm::RDBCursorDefinition.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbcolumndefinition_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBColumnDefinition)


def test_sastm::rdbcolumndefinition_constructor_exists():
    assert callable(sastm::RDBColumnDefinition.__init__)


def test_sastm::rdbcolumndefinition_constructor_args():
    sig = inspect.signature(sastm::RDBColumnDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "NotNull" in params, "Missing parameter 'NotNull'"

def test_sastm::rdbcolumndefinition_has_NotNull():
    assert hasattr(sastm::RDBColumnDefinition, "NotNull")
    descriptor = None
    for klass in sastm::RDBColumnDefinition.__mro__:
        if "NotNull" in klass.__dict__:
            descriptor = klass.__dict__["NotNull"]
            break
    assert isinstance(descriptor, property)



def test_sastm::rdbuserdefinition_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBUserDefinition)


def test_sastm::rdbuserdefinition_constructor_exists():
    assert callable(sastm::RDBUserDefinition.__init__)


def test_sastm::rdbuserdefinition_constructor_args():
    sig = inspect.signature(sastm::RDBUserDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm::datadefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::DataDefinition)


def test_gastm::datadefinition_constructor_exists():
    assert callable(gastm::DataDefinition.__init__)


def test_gastm::datadefinition_constructor_args():
    sig = inspect.signature(gastm::DataDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "isMutable" in params, "Missing parameter 'isMutable'"

def test_gastm::datadefinition_has_isMutable():
    assert hasattr(gastm::DataDefinition, "isMutable")
    descriptor = None
    for klass in gastm::DataDefinition.__mro__:
        if "isMutable" in klass.__dict__:
            descriptor = klass.__dict__["isMutable"]
            break
    assert isinstance(descriptor, property)



def test_sastm::rdbviewdefinition_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBViewDefinition)


def test_sastm::rdbviewdefinition_constructor_exists():
    assert callable(sastm::RDBViewDefinition.__init__)


def test_sastm::rdbviewdefinition_constructor_args():
    sig = inspect.signature(sastm::RDBViewDefinition.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbtablespacedefinition_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBTableSpaceDefinition)


def test_sastm::rdbtablespacedefinition_constructor_exists():
    assert callable(sastm::RDBTableSpaceDefinition.__init__)


def test_sastm::rdbtablespacedefinition_constructor_args():
    sig = inspect.signature(sastm::RDBTableSpaceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm::specifictriggerdefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::SpecificTriggerDefinition)


def test_gastm::specifictriggerdefinition_constructor_exists():
    assert callable(gastm::SpecificTriggerDefinition.__init__)


def test_gastm::specifictriggerdefinition_constructor_args():
    sig = inspect.signature(gastm::SpecificTriggerDefinition.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbdatabasedefinition_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBDatabaseDefinition)


def test_sastm::rdbdatabasedefinition_constructor_exists():
    assert callable(sastm::RDBDatabaseDefinition.__init__)


def test_sastm::rdbdatabasedefinition_constructor_args():
    sig = inspect.signature(sastm::RDBDatabaseDefinition.__init__)
    params = list(sig.parameters.keys())



def test_typereference_is_not_abstract():
    assert not inspect.isabstract(TypeReference)


def test_typereference_constructor_exists():
    assert callable(TypeReference.__init__)


def test_typereference_constructor_args():
    sig = inspect.signature(TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_gastm::namedtypereference_is_not_abstract():
    assert not inspect.isabstract(gastm::NamedTypeReference)


def test_gastm::namedtypereference_constructor_exists():
    assert callable(gastm::NamedTypeReference.__init__)


def test_gastm::namedtypereference_constructor_args():
    sig = inspect.signature(gastm::NamedTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_gastm::unnamedtypereference_is_not_abstract():
    assert not inspect.isabstract(gastm::UnnamedTypeReference)


def test_gastm::unnamedtypereference_constructor_exists():
    assert callable(gastm::UnnamedTypeReference.__init__)


def test_gastm::unnamedtypereference_constructor_args():
    sig = inspect.signature(gastm::UnnamedTypeReference.__init__)
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



def test_gastm::declaration_is_not_abstract():
    assert not inspect.isabstract(gastm::Declaration)


def test_gastm::declaration_constructor_exists():
    assert callable(gastm::Declaration.__init__)


def test_gastm::declaration_constructor_args():
    sig = inspect.signature(gastm::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_gastm::definition_is_not_abstract():
    assert not inspect.isabstract(gastm::Definition)


def test_gastm::definition_constructor_exists():
    assert callable(gastm::Definition.__init__)


def test_gastm::definition_constructor_args():
    sig = inspect.signature(gastm::Definition.__init__)
    params = list(sig.parameters.keys())



def test_gastm::declarationordefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::DeclarationOrDefinition)


def test_gastm::declarationordefinition_constructor_exists():
    assert callable(gastm::DeclarationOrDefinition.__init__)


def test_gastm::declarationordefinition_constructor_args():
    sig = inspect.signature(gastm::DeclarationOrDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "isRegister" in params, "Missing parameter 'isRegister'"
    assert "linkageSpecifier" in params, "Missing parameter 'linkageSpecifier'"

def test_gastm::declarationordefinition_has_isRegister():
    assert hasattr(gastm::DeclarationOrDefinition, "isRegister")
    descriptor = None
    for klass in gastm::DeclarationOrDefinition.__mro__:
        if "isRegister" in klass.__dict__:
            descriptor = klass.__dict__["isRegister"]
            break
    assert isinstance(descriptor, property)

def test_gastm::declarationordefinition_has_linkageSpecifier():
    assert hasattr(gastm::DeclarationOrDefinition, "linkageSpecifier")
    descriptor = None
    for klass in gastm::DeclarationOrDefinition.__mro__:
        if "linkageSpecifier" in klass.__dict__:
            descriptor = klass.__dict__["linkageSpecifier"]
            break
    assert isinstance(descriptor, property)



def test_gastm::entrydefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::EntryDefinition)


def test_gastm::entrydefinition_constructor_exists():
    assert callable(gastm::EntryDefinition.__init__)


def test_gastm::entrydefinition_constructor_args():
    sig = inspect.signature(gastm::EntryDefinition.__init__)
    params = list(sig.parameters.keys())



def test_virtualspecification_is_not_abstract():
    assert not inspect.isabstract(VirtualSpecification)


def test_virtualspecification_constructor_exists():
    assert callable(VirtualSpecification.__init__)


def test_virtualspecification_constructor_args():
    sig = inspect.signature(VirtualSpecification.__init__)
    params = list(sig.parameters.keys())



def test_gastm::virtual_is_not_abstract():
    assert not inspect.isabstract(gastm::Virtual)


def test_gastm::virtual_constructor_exists():
    assert callable(gastm::Virtual.__init__)


def test_gastm::virtual_constructor_args():
    sig = inspect.signature(gastm::Virtual.__init__)
    params = list(sig.parameters.keys())



def test_gastm::nonvirtual_is_not_abstract():
    assert not inspect.isabstract(gastm::NonVirtual)


def test_gastm::nonvirtual_constructor_exists():
    assert callable(gastm::NonVirtual.__init__)


def test_gastm::nonvirtual_constructor_args():
    sig = inspect.signature(gastm::NonVirtual.__init__)
    params = list(sig.parameters.keys())



def test_gastm::purevirtual_is_not_abstract():
    assert not inspect.isabstract(gastm::PureVirtual)


def test_gastm::purevirtual_constructor_exists():
    assert callable(gastm::PureVirtual.__init__)


def test_gastm::purevirtual_constructor_args():
    sig = inspect.signature(gastm::PureVirtual.__init__)
    params = list(sig.parameters.keys())



def test_gastm::functionmemberattributes_is_not_abstract():
    assert not inspect.isabstract(gastm::FunctionMemberAttributes)


def test_gastm::functionmemberattributes_constructor_exists():
    assert callable(gastm::FunctionMemberAttributes.__init__)


def test_gastm::functionmemberattributes_constructor_args():
    sig = inspect.signature(gastm::FunctionMemberAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "isInline" in params, "Missing parameter 'isInline'"
    assert "isFriend" in params, "Missing parameter 'isFriend'"
    assert "isThisConst" in params, "Missing parameter 'isThisConst'"

def test_gastm::functionmemberattributes_has_isInline():
    assert hasattr(gastm::FunctionMemberAttributes, "isInline")
    descriptor = None
    for klass in gastm::FunctionMemberAttributes.__mro__:
        if "isInline" in klass.__dict__:
            descriptor = klass.__dict__["isInline"]
            break
    assert isinstance(descriptor, property)

def test_gastm::functionmemberattributes_has_isFriend():
    assert hasattr(gastm::FunctionMemberAttributes, "isFriend")
    descriptor = None
    for klass in gastm::FunctionMemberAttributes.__mro__:
        if "isFriend" in klass.__dict__:
            descriptor = klass.__dict__["isFriend"]
            break
    assert isinstance(descriptor, property)

def test_gastm::functionmemberattributes_has_isThisConst():
    assert hasattr(gastm::FunctionMemberAttributes, "isThisConst")
    descriptor = None
    for klass in gastm::FunctionMemberAttributes.__mro__:
        if "isThisConst" in klass.__dict__:
            descriptor = klass.__dict__["isThisConst"]
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



def test_gastm::jumpstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::JumpStatement)


def test_gastm::jumpstatement_constructor_exists():
    assert callable(gastm::JumpStatement.__init__)


def test_gastm::jumpstatement_constructor_args():
    sig = inspect.signature(gastm::JumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbconnectstatement_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBConnectStatement)


def test_sastm::rdbconnectstatement_constructor_exists():
    assert callable(sastm::RDBConnectStatement.__init__)


def test_sastm::rdbconnectstatement_constructor_args():
    sig = inspect.signature(sastm::RDBConnectStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::loopstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::LoopStatement)


def test_gastm::loopstatement_constructor_exists():
    assert callable(gastm::LoopStatement.__init__)


def test_gastm::loopstatement_constructor_args():
    sig = inspect.signature(gastm::LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::deletestatement_is_not_abstract():
    assert not inspect.isabstract(gastm::DeleteStatement)


def test_gastm::deletestatement_constructor_exists():
    assert callable(gastm::DeleteStatement.__init__)


def test_gastm::deletestatement_constructor_args():
    sig = inspect.signature(gastm::DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::labeledstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::LabeledStatement)


def test_gastm::labeledstatement_constructor_exists():
    assert callable(gastm::LabeledStatement.__init__)


def test_gastm::labeledstatement_constructor_args():
    sig = inspect.signature(gastm::LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::ifstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::IfStatement)


def test_gastm::ifstatement_constructor_exists():
    assert callable(gastm::IfStatement.__init__)


def test_gastm::ifstatement_constructor_args():
    sig = inspect.signature(gastm::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::terminatestatement_is_not_abstract():
    assert not inspect.isabstract(gastm::TerminateStatement)


def test_gastm::terminatestatement_constructor_exists():
    assert callable(gastm::TerminateStatement.__init__)


def test_gastm::terminatestatement_constructor_args():
    sig = inspect.signature(gastm::TerminateStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::continuestatement_is_not_abstract():
    assert not inspect.isabstract(gastm::ContinueStatement)


def test_gastm::continuestatement_constructor_exists():
    assert callable(gastm::ContinueStatement.__init__)


def test_gastm::continuestatement_constructor_args():
    sig = inspect.signature(gastm::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::switchstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::SwitchStatement)


def test_gastm::switchstatement_constructor_exists():
    assert callable(gastm::SwitchStatement.__init__)


def test_gastm::switchstatement_constructor_args():
    sig = inspect.signature(gastm::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbcursorstatement_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBCursorStatement)


def test_sastm::rdbcursorstatement_constructor_exists():
    assert callable(sastm::RDBCursorStatement.__init__)


def test_sastm::rdbcursorstatement_constructor_args():
    sig = inspect.signature(sastm::RDBCursorStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::declarationordefinitionstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::DeclarationOrDefinitionStatement)


def test_gastm::declarationordefinitionstatement_constructor_exists():
    assert callable(gastm::DeclarationOrDefinitionStatement.__init__)


def test_gastm::declarationordefinitionstatement_constructor_args():
    sig = inspect.signature(gastm::DeclarationOrDefinitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbselectstatement_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBSelectStatement)


def test_sastm::rdbselectstatement_constructor_exists():
    assert callable(sastm::RDBSelectStatement.__init__)


def test_sastm::rdbselectstatement_constructor_args():
    sig = inspect.signature(sastm::RDBSelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::returnstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::ReturnStatement)


def test_gastm::returnstatement_constructor_exists():
    assert callable(gastm::ReturnStatement.__init__)


def test_gastm::returnstatement_constructor_args():
    sig = inspect.signature(gastm::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbmodifystatement_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBModifyStatement)


def test_sastm::rdbmodifystatement_constructor_exists():
    assert callable(sastm::RDBModifyStatement.__init__)


def test_sastm::rdbmodifystatement_constructor_args():
    sig = inspect.signature(sastm::RDBModifyStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::blockstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::BlockStatement)


def test_gastm::blockstatement_constructor_exists():
    assert callable(gastm::BlockStatement.__init__)


def test_gastm::blockstatement_constructor_args():
    sig = inspect.signature(gastm::BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::trystatement_is_not_abstract():
    assert not inspect.isabstract(gastm::TryStatement)


def test_gastm::trystatement_constructor_exists():
    assert callable(gastm::TryStatement.__init__)


def test_gastm::trystatement_constructor_args():
    sig = inspect.signature(gastm::TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_sastm::rdbinsertstatement_is_not_abstract():
    assert not inspect.isabstract(sastm::RDBInsertStatement)


def test_sastm::rdbinsertstatement_constructor_exists():
    assert callable(sastm::RDBInsertStatement.__init__)


def test_sastm::rdbinsertstatement_constructor_args():
    sig = inspect.signature(sastm::RDBInsertStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::ExpressionStatement)


def test_gastm::expressionstatement_constructor_exists():
    assert callable(gastm::ExpressionStatement.__init__)


def test_gastm::expressionstatement_constructor_args():
    sig = inspect.signature(gastm::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::throwstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::ThrowStatement)


def test_gastm::throwstatement_constructor_exists():
    assert callable(gastm::ThrowStatement.__init__)


def test_gastm::throwstatement_constructor_args():
    sig = inspect.signature(gastm::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::specificselectstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::SpecificSelectStatement)


def test_gastm::specificselectstatement_constructor_exists():
    assert callable(gastm::SpecificSelectStatement.__init__)


def test_gastm::specificselectstatement_constructor_args():
    sig = inspect.signature(gastm::SpecificSelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::breakstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::BreakStatement)


def test_gastm::breakstatement_constructor_exists():
    assert callable(gastm::BreakStatement.__init__)


def test_gastm::breakstatement_constructor_args():
    sig = inspect.signature(gastm::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::emptystatement_is_not_abstract():
    assert not inspect.isabstract(gastm::EmptyStatement)


def test_gastm::emptystatement_constructor_exists():
    assert callable(gastm::EmptyStatement.__init__)


def test_gastm::emptystatement_constructor_args():
    sig = inspect.signature(gastm::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_formalparameterdefinition_is_not_abstract():
    assert not inspect.isabstract(FormalParameterDefinition)


def test_formalparameterdefinition_constructor_exists():
    assert callable(FormalParameterDefinition.__init__)


def test_formalparameterdefinition_constructor_args():
    sig = inspect.signature(FormalParameterDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm::functiondefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::FunctionDefinition)


def test_gastm::functiondefinition_constructor_exists():
    assert callable(gastm::FunctionDefinition.__init__)


def test_gastm::functiondefinition_constructor_args():
    sig = inspect.signature(gastm::FunctionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(gastm::VariableDeclaration)


def test_gastm::variabledeclaration_constructor_exists():
    assert callable(gastm::VariableDeclaration.__init__)


def test_gastm::variabledeclaration_constructor_args():
    sig = inspect.signature(gastm::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isMutable" in params, "Missing parameter 'isMutable'"

def test_gastm::variabledeclaration_has_isMutable():
    assert hasattr(gastm::VariableDeclaration, "isMutable")
    descriptor = None
    for klass in gastm::VariableDeclaration.__mro__:
        if "isMutable" in klass.__dict__:
            descriptor = klass.__dict__["isMutable"]
            break
    assert isinstance(descriptor, property)



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



def test_gastm::scope_is_not_abstract():
    assert not inspect.isabstract(gastm::Scope)


def test_gastm::scope_constructor_exists():
    assert callable(gastm::Scope.__init__)


def test_gastm::scope_constructor_args():
    sig = inspect.signature(gastm::Scope.__init__)
    params = list(sig.parameters.keys())



def test_gastm::project_is_not_abstract():
    assert not inspect.isabstract(gastm::Project)


def test_gastm::project_constructor_exists():
    assert callable(gastm::Project.__init__)


def test_gastm::project_constructor_args():
    sig = inspect.signature(gastm::Project.__init__)
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



def test_gastm::sourcelocation_is_not_abstract():
    assert not inspect.isabstract(gastm::SourceLocation)


def test_gastm::sourcelocation_constructor_exists():
    assert callable(gastm::SourceLocation.__init__)


def test_gastm::sourcelocation_constructor_args():
    sig = inspect.signature(gastm::SourceLocation.__init__)
    params = list(sig.parameters.keys())
    assert "startLine" in params, "Missing parameter 'startLine'"
    assert "endLine" in params, "Missing parameter 'endLine'"
    assert "startColumn" in params, "Missing parameter 'startColumn'"
    assert "endColumn" in params, "Missing parameter 'endColumn'"

def test_gastm::sourcelocation_has_startLine():
    assert hasattr(gastm::SourceLocation, "startLine")
    descriptor = None
    for klass in gastm::SourceLocation.__mro__:
        if "startLine" in klass.__dict__:
            descriptor = klass.__dict__["startLine"]
            break
    assert isinstance(descriptor, property)

def test_gastm::sourcelocation_has_endLine():
    assert hasattr(gastm::SourceLocation, "endLine")
    descriptor = None
    for klass in gastm::SourceLocation.__mro__:
        if "endLine" in klass.__dict__:
            descriptor = klass.__dict__["endLine"]
            break
    assert isinstance(descriptor, property)

def test_gastm::sourcelocation_has_startColumn():
    assert hasattr(gastm::SourceLocation, "startColumn")
    descriptor = None
    for klass in gastm::SourceLocation.__mro__:
        if "startColumn" in klass.__dict__:
            descriptor = klass.__dict__["startColumn"]
            break
    assert isinstance(descriptor, property)

def test_gastm::sourcelocation_has_endColumn():
    assert hasattr(gastm::SourceLocation, "endColumn")
    descriptor = None
    for klass in gastm::SourceLocation.__mro__:
        if "endColumn" in klass.__dict__:
            descriptor = klass.__dict__["endColumn"]
            break
    assert isinstance(descriptor, property)



def test_gastm::sourcefile_is_not_abstract():
    assert not inspect.isabstract(gastm::SourceFile)


def test_gastm::sourcefile_constructor_exists():
    assert callable(gastm::SourceFile.__init__)


def test_gastm::sourcefile_constructor_args():
    sig = inspect.signature(gastm::SourceFile.__init__)
    params = list(sig.parameters.keys())
    assert "pathName" in params, "Missing parameter 'pathName'"

def test_gastm::sourcefile_has_pathName():
    assert hasattr(gastm::SourceFile, "pathName")
    descriptor = None
    for klass in gastm::SourceFile.__mro__:
        if "pathName" in klass.__dict__:
            descriptor = klass.__dict__["pathName"]
            break
    assert isinstance(descriptor, property)



def test_gastm::actualparameter_is_not_abstract():
    assert not inspect.isabstract(gastm::ActualParameter)


def test_gastm::actualparameter_constructor_exists():
    assert callable(gastm::ActualParameter.__init__)


def test_gastm::actualparameter_constructor_args():
    sig = inspect.signature(gastm::ActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_gastm::binaryoperator_is_not_abstract():
    assert not inspect.isabstract(gastm::BinaryOperator)


def test_gastm::binaryoperator_constructor_exists():
    assert callable(gastm::BinaryOperator.__init__)


def test_gastm::binaryoperator_constructor_args():
    sig = inspect.signature(gastm::BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_gastm::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(gastm::UnaryOperator)


def test_gastm::unaryoperator_constructor_exists():
    assert callable(gastm::UnaryOperator.__init__)


def test_gastm::unaryoperator_constructor_args():
    sig = inspect.signature(gastm::UnaryOperator.__init__)
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
sastm::RDBHostVariableReference_strategy = st.builds(
    sastm::RDBHostVariableReference,
)
RDBHostVariableReference_strategy = st.builds(
    RDBHostVariableReference,
)
RDBCursorStatement_strategy = st.builds(
    RDBCursorStatement,
)
sastm::RDBFetchCursorStatement_strategy = st.builds(
    sastm::RDBFetchCursorStatement,
)
sastm::RDBOpenCursorStatement_strategy = st.builds(
    sastm::RDBOpenCursorStatement,
)
RDBModifyStatement_strategy = st.builds(
    RDBModifyStatement,
)
sastm::RDBUpdateStatement_strategy = st.builds(
    sastm::RDBUpdateStatement,
)
AggregateTypeDefinition_strategy = st.builds(
    AggregateTypeDefinition,
)
Project_strategy = st.builds(
    Project,
)
NamedTypeDefinition_strategy = st.builds(
    NamedTypeDefinition,
)
RDBConstraint_strategy = st.builds(
    RDBConstraint,
)
sastm::RDBRefIntegrity_strategy = st.builds(
    sastm::RDBRefIntegrity,
)
sastm::RDBUniqueKey_strategy = st.builds(
    sastm::RDBUniqueKey,
)
sastm::RDBCheckConstraint_strategy = st.builds(
    sastm::RDBCheckConstraint,
    RDBConstraintText=
        safe_text,
    RDBConstraintType=
        safe_text
)
ActualParameterExpression_strategy = st.builds(
    ActualParameterExpression,
)
gastm::ByReferenceActualParameterExpression_strategy = st.builds(
    gastm::ByReferenceActualParameterExpression,
)
gastm::ByValueActualParameterExpression_strategy = st.builds(
    gastm::ByValueActualParameterExpression,
)
IncludeUnit_strategy = st.builds(
    IncludeUnit,
)
NameSpaceDefinition_strategy = st.builds(
    NameSpaceDefinition,
)
sastm::RDBTableSpaceReference_strategy = st.builds(
    sastm::RDBTableSpaceReference,
)
RDBTableSpaceReference_strategy = st.builds(
    RDBTableSpaceReference,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
gastm::AddressOf_strategy = st.builds(
    gastm::AddressOf,
)
gastm::Increment_strategy = st.builds(
    gastm::Increment,
)
gastm::BitNot_strategy = st.builds(
    gastm::BitNot,
)
gastm::Negate_strategy = st.builds(
    gastm::Negate,
)
gastm::Decrement_strategy = st.builds(
    gastm::Decrement,
)
gastm::Deref_strategy = st.builds(
    gastm::Deref,
)
gastm::Not_strategy = st.builds(
    gastm::Not,
)
gastm::UnaryPlus_strategy = st.builds(
    gastm::UnaryPlus,
)
Literal_strategy = st.builds(
    Literal,
)
gastm::CharLiteral_strategy = st.builds(
    gastm::CharLiteral,
)
gastm::RealLiteral_strategy = st.builds(
    gastm::RealLiteral,
)
gastm::StringLiteral_strategy = st.builds(
    gastm::StringLiteral,
)
gastm::BooleanLiteral_strategy = st.builds(
    gastm::BooleanLiteral,
)
gastm::BitLiteral_strategy = st.builds(
    gastm::BitLiteral,
)
gastm::IntegerlLiteral_strategy = st.builds(
    gastm::IntegerlLiteral,
)
QualifiedIdentifierReference_strategy = st.builds(
    QualifiedIdentifierReference,
)
gastm::QualifiedOverData_strategy = st.builds(
    gastm::QualifiedOverData,
)
gastm::QualifiedOverPointer_strategy = st.builds(
    gastm::QualifiedOverPointer,
)
gastm::PostDecrement_strategy = st.builds(
    gastm::PostDecrement,
)
gastm::PostIncrement_strategy = st.builds(
    gastm::PostIncrement,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
gastm::Byte_strategy = st.builds(
    gastm::Byte,
)
gastm::LongInteger_strategy = st.builds(
    gastm::LongInteger,
)
gastm::Integer_strategy = st.builds(
    gastm::Integer,
)
gastm::Boolean_strategy = st.builds(
    gastm::Boolean,
)
gastm::LongDouble_strategy = st.builds(
    gastm::LongDouble,
)
gastm::ShortInteger_strategy = st.builds(
    gastm::ShortInteger,
)
gastm::Float_strategy = st.builds(
    gastm::Float,
)
gastm::WideCharacter_strategy = st.builds(
    gastm::WideCharacter,
)
gastm::Double_strategy = st.builds(
    gastm::Double,
)
gastm::Character_strategy = st.builds(
    gastm::Character,
)
gastm::String_strategy = st.builds(
    gastm::String,
)
gastm::Void_strategy = st.builds(
    gastm::Void,
)
StorageSpecification_strategy = st.builds(
    StorageSpecification,
)
gastm::PerClassMember_strategy = st.builds(
    gastm::PerClassMember,
)
gastm::FunctionPersistent_strategy = st.builds(
    gastm::FunctionPersistent,
)
gastm::FileLocal_strategy = st.builds(
    gastm::FileLocal,
)
gastm::NoDef_strategy = st.builds(
    gastm::NoDef,
)
gastm::External_strategy = st.builds(
    gastm::External,
)
ForStatement_strategy = st.builds(
    ForStatement,
)
gastm::ForCheckAfterStatement_strategy = st.builds(
    gastm::ForCheckAfterStatement,
)
gastm::ForCheckBeforeStatement_strategy = st.builds(
    gastm::ForCheckBeforeStatement,
)
AccessKind_strategy = st.builds(
    AccessKind,
)
gastm::Private_strategy = st.builds(
    gastm::Private,
)
gastm::Protected_strategy = st.builds(
    gastm::Protected,
)
gastm::Public_strategy = st.builds(
    gastm::Public,
)
sastm::RDBCloseCursorStatement_strategy = st.builds(
    sastm::RDBCloseCursorStatement,
)
sastm::RDBDeleteStatement_strategy = st.builds(
    sastm::RDBDeleteStatement,
)
gastm::AccessKind_strategy = st.builds(
    gastm::AccessKind,
)
gastm::DataType_strategy = st.builds(
    gastm::DataType,
)
gastm::StorageSpecification_strategy = st.builds(
    gastm::StorageSpecification,
)
gastm::OtherSyntaxObject_strategy = st.builds(
    gastm::OtherSyntaxObject,
)
gastm::GASTMSemanticObject_strategy = st.builds(
    gastm::GASTMSemanticObject,
)
gastm::GASTMSourceObject_strategy = st.builds(
    gastm::GASTMSourceObject,
)
gastm::GASTMObject_strategy = st.builds(
    gastm::GASTMObject,
)
ProgramScope_strategy = st.builds(
    ProgramScope,
)
OtherSyntaxObject_strategy = st.builds(
    OtherSyntaxObject,
)
sastm::RDBIndexColumn_strategy = st.builds(
    sastm::RDBIndexColumn,
    AscendingOrDescending=
        safe_text
)
gastm::VirtualSpecification_strategy = st.builds(
    gastm::VirtualSpecification,
)
gastm::Name_strategy = st.builds(
    gastm::Name,
    nameString=
        safe_text
)
sastm::RDBIndex_strategy = st.builds(
    sastm::RDBIndex,
    NotNull=
        st.booleans(),
    IsUnique=
        st.booleans()
)
gastm::FunctionMemberAttribute_strategy = st.builds(
    gastm::FunctionMemberAttribute,
)
sastm::RDBTrigger_strategy = st.builds(
    sastm::RDBTrigger,
)
sastm::RDBConstraint_strategy = st.builds(
    sastm::RDBConstraint,
)
gastm::CompilationUnit_strategy = st.builds(
    gastm::CompilationUnit,
    language=
        safe_text
)
AnnotationExpression_strategy = st.builds(
    AnnotationExpression,
)
PreprocessorElement_strategy = st.builds(
    PreprocessorElement,
)
SourceLocation_strategy = st.builds(
    SourceLocation,
)
GASTMObject_strategy = st.builds(
    GASTMObject,
)
gastm::GASTMSyntaxObject_strategy = st.builds(
    gastm::GASTMSyntaxObject,
)
Scope_strategy = st.builds(
    Scope,
)
gastm::FunctionScope_strategy = st.builds(
    gastm::FunctionScope,
)
gastm::BlockScope_strategy = st.builds(
    gastm::BlockScope,
)
gastm::AggregateScope_strategy = st.builds(
    gastm::AggregateScope,
)
gastm::ProgramScope_strategy = st.builds(
    gastm::ProgramScope,
)
DefinitionObject_strategy = st.builds(
    DefinitionObject,
)
GlobalScope_strategy = st.builds(
    GlobalScope,
)
gastm::GlobalScope_strategy = st.builds(
    gastm::GlobalScope,
)
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
gastm::SpecificIn_strategy = st.builds(
    gastm::SpecificIn,
)
gastm::SpecificLike_strategy = st.builds(
    gastm::SpecificLike,
)
gastm::NotGreater_strategy = st.builds(
    gastm::NotGreater,
)
gastm::Assign_strategy = st.builds(
    gastm::Assign,
)
gastm::Divide_strategy = st.builds(
    gastm::Divide,
)
gastm::BitXor_strategy = st.builds(
    gastm::BitXor,
)
gastm::Exponent_strategy = st.builds(
    gastm::Exponent,
)
gastm::Less_strategy = st.builds(
    gastm::Less,
)
gastm::Or_strategy = st.builds(
    gastm::Or,
)
gastm::Equal_strategy = st.builds(
    gastm::Equal,
)
gastm::BitRightShift_strategy = st.builds(
    gastm::BitRightShift,
)
gastm::Subtract_strategy = st.builds(
    gastm::Subtract,
)
gastm::Add_strategy = st.builds(
    gastm::Add,
)
gastm::Greater_strategy = st.builds(
    gastm::Greater,
)
gastm::SpecificGreaterEqual_strategy = st.builds(
    gastm::SpecificGreaterEqual,
)
gastm::Multiply_strategy = st.builds(
    gastm::Multiply,
)
gastm::SpecificConcatString_strategy = st.builds(
    gastm::SpecificConcatString,
)
gastm::BitLeftShift_strategy = st.builds(
    gastm::BitLeftShift,
)
gastm::SpecificLessEqual_strategy = st.builds(
    gastm::SpecificLessEqual,
)
gastm::BitOr_strategy = st.builds(
    gastm::BitOr,
)
gastm::NotLess_strategy = st.builds(
    gastm::NotLess,
)
gastm::BitAnd_strategy = st.builds(
    gastm::BitAnd,
)
gastm::And_strategy = st.builds(
    gastm::And,
)
gastm::NotEqual_strategy = st.builds(
    gastm::NotEqual,
)
gastm::Modulus_strategy = st.builds(
    gastm::Modulus,
)
gastm::OperatorAssign_strategy = st.builds(
    gastm::OperatorAssign,
)
ActualParameter_strategy = st.builds(
    ActualParameter,
)
gastm::MissingActualParameter_strategy = st.builds(
    gastm::MissingActualParameter,
)
gastm::ActualParameterExpression_strategy = st.builds(
    gastm::ActualParameterExpression,
)
IdentifierReference_strategy = st.builds(
    IdentifierReference,
)
sastm::RDBTableAlias_strategy = st.builds(
    sastm::RDBTableAlias,
)
sastm::RDBTableReference_strategy = st.builds(
    sastm::RDBTableReference,
)
sastm::RDBColumnReference_strategy = st.builds(
    sastm::RDBColumnReference,
)
NameReference_strategy = st.builds(
    NameReference,
)
gastm::IdentifierReference_strategy = st.builds(
    gastm::IdentifierReference,
)
gastm::TypeQualifiedIdentifierReference_strategy = st.builds(
    gastm::TypeQualifiedIdentifierReference,
)
gastm::QualifiedIdentifierReference_strategy = st.builds(
    gastm::QualifiedIdentifierReference,
)
gastm::CatchBlock_strategy = st.builds(
    gastm::CatchBlock,
)
CatchBlock_strategy = st.builds(
    CatchBlock,
)
gastm::TypesCatchBlock_strategy = st.builds(
    gastm::TypesCatchBlock,
)
LoopStatement_strategy = st.builds(
    LoopStatement,
)
gastm::DoWhileStatement_strategy = st.builds(
    gastm::DoWhileStatement,
)
gastm::WhileStatement_strategy = st.builds(
    gastm::WhileStatement,
)
gastm::ForStatement_strategy = st.builds(
    gastm::ForStatement,
)
gastm::VariableCatchBlock_strategy = st.builds(
    gastm::VariableCatchBlock,
)
BlockScope_strategy = st.builds(
    BlockScope,
)
LabelDefinition_strategy = st.builds(
    LabelDefinition,
)
gastm::SwitchCase_strategy = st.builds(
    gastm::SwitchCase,
)
SwitchCase_strategy = st.builds(
    SwitchCase,
)
gastm::DefaultBlock_strategy = st.builds(
    gastm::DefaultBlock,
)
gastm::CaseBlock_strategy = st.builds(
    gastm::CaseBlock,
)
LabelAccess_strategy = st.builds(
    LabelAccess,
)
gastm::Dimension_strategy = st.builds(
    gastm::Dimension,
)
Dimension_strategy = st.builds(
    Dimension,
)
ConstructedType_strategy = st.builds(
    ConstructedType,
)
gastm::PointerType_strategy = st.builds(
    gastm::PointerType,
)
gastm::CollectionType_strategy = st.builds(
    gastm::CollectionType,
)
gastm::RangeType_strategy = st.builds(
    gastm::RangeType,
)
gastm::ReferenceType_strategy = st.builds(
    gastm::ReferenceType,
)
gastm::ArrayType_strategy = st.builds(
    gastm::ArrayType,
)
AggregateScope_strategy = st.builds(
    AggregateScope,
)
EnumLiteralDefinition_strategy = st.builds(
    EnumLiteralDefinition,
)
DataType_strategy = st.builds(
    DataType,
)
sastm::RDBRaw_strategy = st.builds(
    sastm::RDBRaw,
)
sastm::RDBBoolean_strategy = st.builds(
    sastm::RDBBoolean,
)
sastm::RDBClob_strategy = st.builds(
    sastm::RDBClob,
)
sastm::RDBRowid_strategy = st.builds(
    sastm::RDBRowid,
)
sastm::RDBTableType_strategy = st.builds(
    sastm::RDBTableType,
)
sastm::RDBDataBaseType_strategy = st.builds(
    sastm::RDBDataBaseType,
)
sastm::RDBTimestamp_strategy = st.builds(
    sastm::RDBTimestamp,
)
sastm::RDBChar_strategy = st.builds(
    sastm::RDBChar,
)
sastm::RDBVarchar_strategy = st.builds(
    sastm::RDBVarchar,
)
gastm::AggregateType_strategy = st.builds(
    gastm::AggregateType,
)
sastm::RDBNumber_strategy = st.builds(
    sastm::RDBNumber,
)
sastm::RDBLong_strategy = st.builds(
    sastm::RDBLong,
)
gastm::EnumType_strategy = st.builds(
    gastm::EnumType,
)
sastm::RDBString_strategy = st.builds(
    sastm::RDBString,
)
sastm::RDBReal_strategy = st.builds(
    sastm::RDBReal,
)
sastm::RDBBlob_strategy = st.builds(
    sastm::RDBBlob,
)
gastm::ExceptionType_strategy = st.builds(
    gastm::ExceptionType,
)
sastm::RDBDecimal_strategy = st.builds(
    sastm::RDBDecimal,
)
sastm::RDBNClob_strategy = st.builds(
    sastm::RDBNClob,
)
sastm::RDBInteger_strategy = st.builds(
    sastm::RDBInteger,
)
sastm::RDBInt_strategy = st.builds(
    sastm::RDBInt,
)
sastm::RDBUserType_strategy = st.builds(
    sastm::RDBUserType,
)
sastm::RDBViewType_strategy = st.builds(
    sastm::RDBViewType,
)
sastm::RDBBFile_strategy = st.builds(
    sastm::RDBBFile,
)
sastm::RDBFloat_strategy = st.builds(
    sastm::RDBFloat,
)
gastm::ConstructedType_strategy = st.builds(
    gastm::ConstructedType,
)
sastm::RDBDate_strategy = st.builds(
    sastm::RDBDate,
)
sastm::RDBCursorType_strategy = st.builds(
    sastm::RDBCursorType,
)
sastm::RDBTableSpaceType_strategy = st.builds(
    sastm::RDBTableSpaceType,
)
gastm::PrimitiveType_strategy = st.builds(
    gastm::PrimitiveType,
    isSigned=
        st.booleans()
)
gastm::DerivesFrom_strategy = st.builds(
    gastm::DerivesFrom,
    isVirtual=
        st.booleans()
)
DerivesFrom_strategy = st.builds(
    DerivesFrom,
)
gastm::NamedType_strategy = st.builds(
    gastm::NamedType,
)
gastm::FormalParameterType_strategy = st.builds(
    gastm::FormalParameterType,
)
FormalParameterType_strategy = st.builds(
    FormalParameterType,
)
gastm::ByValueFormalParameterType_strategy = st.builds(
    gastm::ByValueFormalParameterType,
)
gastm::ByReferenceFormalParameterType_strategy = st.builds(
    gastm::ByReferenceFormalParameterType,
)
Type_strategy = st.builds(
    Type,
)
gastm::LabelType_strategy = st.builds(
    gastm::LabelType,
)
gastm::FunctionType_strategy = st.builds(
    gastm::FunctionType,
)
gastm::NameSpaceType_strategy = st.builds(
    gastm::NameSpaceType,
)
gastm::TypeReference_strategy = st.builds(
    gastm::TypeReference,
)
gastm::NameSpaceDefinition_strategy = st.builds(
    gastm::NameSpaceDefinition,
)
AggregateType_strategy = st.builds(
    AggregateType,
)
gastm::UnionType_strategy = st.builds(
    gastm::UnionType,
)
gastm::StructureType_strategy = st.builds(
    gastm::StructureType,
)
gastm::ClassType_strategy = st.builds(
    gastm::ClassType,
)
gastm::AnnotationType_strategy = st.builds(
    gastm::AnnotationType,
)
NamedType_strategy = st.builds(
    NamedType,
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
gastm::AggregateTypeDefinition_strategy = st.builds(
    gastm::AggregateTypeDefinition,
)
gastm::NamedTypeDefinition_strategy = st.builds(
    gastm::NamedTypeDefinition,
)
gastm::TypeDefinition_strategy = st.builds(
    gastm::TypeDefinition,
)
DataDefinition_strategy = st.builds(
    DataDefinition,
)
gastm::VariableDefinition_strategy = st.builds(
    gastm::VariableDefinition,
)
gastm::FormalParameterDefinition_strategy = st.builds(
    gastm::FormalParameterDefinition,
)
gastm::BitFieldDefinition_strategy = st.builds(
    gastm::BitFieldDefinition,
)
Expression_strategy = st.builds(
    Expression,
)
gastm::NameReference_strategy = st.builds(
    gastm::NameReference,
)
sastm::RDBHostVariableExpression_strategy = st.builds(
    sastm::RDBHostVariableExpression,
)
gastm::UnaryExpression_strategy = st.builds(
    gastm::UnaryExpression,
)
gastm::BinaryExpression_strategy = st.builds(
    gastm::BinaryExpression,
)
gastm::FunctionCallExpression_strategy = st.builds(
    gastm::FunctionCallExpression,
)
gastm::ArrayAccess_strategy = st.builds(
    gastm::ArrayAccess,
)
gastm::Literal_strategy = st.builds(
    gastm::Literal,
    value=
        safe_text
)
gastm::ConditionalExpression_strategy = st.builds(
    gastm::ConditionalExpression,
)
gastm::LabelAccess_strategy = st.builds(
    gastm::LabelAccess,
)
gastm::AggregateExpression_strategy = st.builds(
    gastm::AggregateExpression,
)
gastm::AnnotationExpression_strategy = st.builds(
    gastm::AnnotationExpression,
)
gastm::RangeExpression_strategy = st.builds(
    gastm::RangeExpression,
)
sastm::RDBSelectExpression_strategy = st.builds(
    sastm::RDBSelectExpression,
)
gastm::NewExpression_strategy = st.builds(
    gastm::NewExpression,
)
gastm::CastExpression_strategy = st.builds(
    gastm::CastExpression,
)
GASTMSyntaxObject_strategy = st.builds(
    GASTMSyntaxObject,
)
gastm::Expression_strategy = st.builds(
    gastm::Expression,
)
gastm::PreprocessorElement_strategy = st.builds(
    gastm::PreprocessorElement,
)
gastm::Statement_strategy = st.builds(
    gastm::Statement,
)
gastm::DefinitionObject_strategy = st.builds(
    gastm::DefinitionObject,
)
gastm::Type_strategy = st.builds(
    gastm::Type,
    isConst=
        st.booleans(),
    isVolatile=
        st.booleans()
)
gastm::Comment_strategy = st.builds(
    gastm::Comment,
    text=
        safe_text
)
gastm::MacroDefinition_strategy = st.builds(
    gastm::MacroDefinition,
    body=
        safe_text,
    macroName=
        safe_text
)
MacroDefinition_strategy = st.builds(
    MacroDefinition,
)
gastm::MacroCall_strategy = st.builds(
    gastm::MacroCall,
)
gastm::IncludeUnit_strategy = st.builds(
    gastm::IncludeUnit,
)
LabelType_strategy = st.builds(
    LabelType,
)
gastm::LabelDefinition_strategy = st.builds(
    gastm::LabelDefinition,
)
NameSpaceType_strategy = st.builds(
    NameSpaceType,
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
gastm::FormalParameterDeclaration_strategy = st.builds(
    gastm::FormalParameterDeclaration,
)
gastm::FunctionDeclaration_strategy = st.builds(
    gastm::FunctionDeclaration,
)
Definition_strategy = st.builds(
    Definition,
)
gastm::EnumLiteralDefinition_strategy = st.builds(
    gastm::EnumLiteralDefinition,
)
sastm::RDBTableDefinition_strategy = st.builds(
    sastm::RDBTableDefinition,
)
sastm::RDBCursorDefinition_strategy = st.builds(
    sastm::RDBCursorDefinition,
)
sastm::RDBColumnDefinition_strategy = st.builds(
    sastm::RDBColumnDefinition,
    NotNull=
        st.booleans()
)
sastm::RDBUserDefinition_strategy = st.builds(
    sastm::RDBUserDefinition,
)
gastm::DataDefinition_strategy = st.builds(
    gastm::DataDefinition,
    isMutable=
        st.booleans()
)
sastm::RDBViewDefinition_strategy = st.builds(
    sastm::RDBViewDefinition,
)
sastm::RDBTableSpaceDefinition_strategy = st.builds(
    sastm::RDBTableSpaceDefinition,
)
gastm::SpecificTriggerDefinition_strategy = st.builds(
    gastm::SpecificTriggerDefinition,
)
sastm::RDBDatabaseDefinition_strategy = st.builds(
    sastm::RDBDatabaseDefinition,
)
TypeReference_strategy = st.builds(
    TypeReference,
)
gastm::NamedTypeReference_strategy = st.builds(
    gastm::NamedTypeReference,
)
gastm::UnnamedTypeReference_strategy = st.builds(
    gastm::UnnamedTypeReference,
)
Name_strategy = st.builds(
    Name,
)
DeclarationOrDefinition_strategy = st.builds(
    DeclarationOrDefinition,
)
gastm::Declaration_strategy = st.builds(
    gastm::Declaration,
)
gastm::Definition_strategy = st.builds(
    gastm::Definition,
)
gastm::DeclarationOrDefinition_strategy = st.builds(
    gastm::DeclarationOrDefinition,
    isRegister=
        st.booleans(),
    linkageSpecifier=
        safe_text
)
gastm::EntryDefinition_strategy = st.builds(
    gastm::EntryDefinition,
)
VirtualSpecification_strategy = st.builds(
    VirtualSpecification,
)
gastm::Virtual_strategy = st.builds(
    gastm::Virtual,
)
gastm::NonVirtual_strategy = st.builds(
    gastm::NonVirtual,
)
gastm::PureVirtual_strategy = st.builds(
    gastm::PureVirtual,
)
gastm::FunctionMemberAttributes_strategy = st.builds(
    gastm::FunctionMemberAttributes,
    isInline=
        st.booleans(),
    isFriend=
        st.booleans(),
    isThisConst=
        st.booleans()
)
FunctionScope_strategy = st.builds(
    FunctionScope,
)
Statement_strategy = st.builds(
    Statement,
)
gastm::JumpStatement_strategy = st.builds(
    gastm::JumpStatement,
)
sastm::RDBConnectStatement_strategy = st.builds(
    sastm::RDBConnectStatement,
)
gastm::LoopStatement_strategy = st.builds(
    gastm::LoopStatement,
)
gastm::DeleteStatement_strategy = st.builds(
    gastm::DeleteStatement,
)
gastm::LabeledStatement_strategy = st.builds(
    gastm::LabeledStatement,
)
gastm::IfStatement_strategy = st.builds(
    gastm::IfStatement,
)
gastm::TerminateStatement_strategy = st.builds(
    gastm::TerminateStatement,
)
gastm::ContinueStatement_strategy = st.builds(
    gastm::ContinueStatement,
)
gastm::SwitchStatement_strategy = st.builds(
    gastm::SwitchStatement,
)
sastm::RDBCursorStatement_strategy = st.builds(
    sastm::RDBCursorStatement,
)
gastm::DeclarationOrDefinitionStatement_strategy = st.builds(
    gastm::DeclarationOrDefinitionStatement,
)
sastm::RDBSelectStatement_strategy = st.builds(
    sastm::RDBSelectStatement,
)
gastm::ReturnStatement_strategy = st.builds(
    gastm::ReturnStatement,
)
sastm::RDBModifyStatement_strategy = st.builds(
    sastm::RDBModifyStatement,
)
gastm::BlockStatement_strategy = st.builds(
    gastm::BlockStatement,
)
gastm::TryStatement_strategy = st.builds(
    gastm::TryStatement,
)
sastm::RDBInsertStatement_strategy = st.builds(
    sastm::RDBInsertStatement,
)
gastm::ExpressionStatement_strategy = st.builds(
    gastm::ExpressionStatement,
)
gastm::ThrowStatement_strategy = st.builds(
    gastm::ThrowStatement,
)
gastm::SpecificSelectStatement_strategy = st.builds(
    gastm::SpecificSelectStatement,
)
gastm::BreakStatement_strategy = st.builds(
    gastm::BreakStatement,
)
gastm::EmptyStatement_strategy = st.builds(
    gastm::EmptyStatement,
)
FormalParameterDefinition_strategy = st.builds(
    FormalParameterDefinition,
)
gastm::FunctionDefinition_strategy = st.builds(
    gastm::FunctionDefinition,
)
gastm::VariableDeclaration_strategy = st.builds(
    gastm::VariableDeclaration,
    isMutable=
        st.booleans()
)
CompilationUnit_strategy = st.builds(
    CompilationUnit,
)
GASTMSemanticObject_strategy = st.builds(
    GASTMSemanticObject,
)
gastm::Scope_strategy = st.builds(
    gastm::Scope,
)
gastm::Project_strategy = st.builds(
    gastm::Project,
)
SourceFile_strategy = st.builds(
    SourceFile,
)
GASTMSourceObject_strategy = st.builds(
    GASTMSourceObject,
)
gastm::SourceLocation_strategy = st.builds(
    gastm::SourceLocation,
    startLine=
        st.integers(),
    endLine=
        st.integers(),
    startColumn=
        st.integers(),
    endColumn=
        st.integers()
)
gastm::SourceFile_strategy = st.builds(
    gastm::SourceFile,
    pathName=
        safe_text
)
gastm::ActualParameter_strategy = st.builds(
    gastm::ActualParameter,
)
gastm::BinaryOperator_strategy = st.builds(
    gastm::BinaryOperator,
)
gastm::UnaryOperator_strategy = st.builds(
    gastm::UnaryOperator,
)

@given(instance=sastm::RDBHostVariableReference_strategy)
@settings(max_examples=50)
def test_sastm::rdbhostvariablereference_instantiation(instance):
    assert isinstance(instance, sastm::RDBHostVariableReference)

@given(instance=RDBHostVariableReference_strategy)
@settings(max_examples=50)
def test_rdbhostvariablereference_instantiation(instance):
    assert isinstance(instance, RDBHostVariableReference)

@given(instance=RDBCursorStatement_strategy)
@settings(max_examples=50)
def test_rdbcursorstatement_instantiation(instance):
    assert isinstance(instance, RDBCursorStatement)

@given(instance=sastm::RDBFetchCursorStatement_strategy)
@settings(max_examples=50)
def test_sastm::rdbfetchcursorstatement_instantiation(instance):
    assert isinstance(instance, sastm::RDBFetchCursorStatement)

@given(instance=sastm::RDBOpenCursorStatement_strategy)
@settings(max_examples=50)
def test_sastm::rdbopencursorstatement_instantiation(instance):
    assert isinstance(instance, sastm::RDBOpenCursorStatement)

@given(instance=RDBModifyStatement_strategy)
@settings(max_examples=50)
def test_rdbmodifystatement_instantiation(instance):
    assert isinstance(instance, RDBModifyStatement)

@given(instance=sastm::RDBUpdateStatement_strategy)
@settings(max_examples=50)
def test_sastm::rdbupdatestatement_instantiation(instance):
    assert isinstance(instance, sastm::RDBUpdateStatement)

@given(instance=AggregateTypeDefinition_strategy)
@settings(max_examples=50)
def test_aggregatetypedefinition_instantiation(instance):
    assert isinstance(instance, AggregateTypeDefinition)

@given(instance=Project_strategy)
@settings(max_examples=50)
def test_project_instantiation(instance):
    assert isinstance(instance, Project)

@given(instance=NamedTypeDefinition_strategy)
@settings(max_examples=50)
def test_namedtypedefinition_instantiation(instance):
    assert isinstance(instance, NamedTypeDefinition)

@given(instance=RDBConstraint_strategy)
@settings(max_examples=50)
def test_rdbconstraint_instantiation(instance):
    assert isinstance(instance, RDBConstraint)

@given(instance=sastm::RDBRefIntegrity_strategy)
@settings(max_examples=50)
def test_sastm::rdbrefintegrity_instantiation(instance):
    assert isinstance(instance, sastm::RDBRefIntegrity)

@given(instance=sastm::RDBUniqueKey_strategy)
@settings(max_examples=50)
def test_sastm::rdbuniquekey_instantiation(instance):
    assert isinstance(instance, sastm::RDBUniqueKey)

@given(instance=sastm::RDBCheckConstraint_strategy)
@settings(max_examples=50)
def test_sastm::rdbcheckconstraint_instantiation(instance):
    assert isinstance(instance, sastm::RDBCheckConstraint)

@given(instance=sastm::RDBCheckConstraint_strategy)
def test_sastm::rdbcheckconstraint_RDBConstraintText_type(instance):
    assert isinstance(instance.RDBConstraintText, str)


@given(instance=sastm::RDBCheckConstraint_strategy)
def test_sastm::rdbcheckconstraint_RDBConstraintText_setter(instance):
    original = instance.RDBConstraintText
    instance.RDBConstraintText = original
    assert instance.RDBConstraintText == original

@given(instance=sastm::RDBCheckConstraint_strategy)
def test_sastm::rdbcheckconstraint_RDBConstraintType_type(instance):
    assert isinstance(instance.RDBConstraintType, str)


@given(instance=sastm::RDBCheckConstraint_strategy)
def test_sastm::rdbcheckconstraint_RDBConstraintType_setter(instance):
    original = instance.RDBConstraintType
    instance.RDBConstraintType = original
    assert instance.RDBConstraintType == original

@given(instance=ActualParameterExpression_strategy)
@settings(max_examples=50)
def test_actualparameterexpression_instantiation(instance):
    assert isinstance(instance, ActualParameterExpression)

@given(instance=gastm::ByReferenceActualParameterExpression_strategy)
@settings(max_examples=50)
def test_gastm::byreferenceactualparameterexpression_instantiation(instance):
    assert isinstance(instance, gastm::ByReferenceActualParameterExpression)

@given(instance=gastm::ByValueActualParameterExpression_strategy)
@settings(max_examples=50)
def test_gastm::byvalueactualparameterexpression_instantiation(instance):
    assert isinstance(instance, gastm::ByValueActualParameterExpression)

@given(instance=IncludeUnit_strategy)
@settings(max_examples=50)
def test_includeunit_instantiation(instance):
    assert isinstance(instance, IncludeUnit)

@given(instance=NameSpaceDefinition_strategy)
@settings(max_examples=50)
def test_namespacedefinition_instantiation(instance):
    assert isinstance(instance, NameSpaceDefinition)

@given(instance=sastm::RDBTableSpaceReference_strategy)
@settings(max_examples=50)
def test_sastm::rdbtablespacereference_instantiation(instance):
    assert isinstance(instance, sastm::RDBTableSpaceReference)

@given(instance=RDBTableSpaceReference_strategy)
@settings(max_examples=50)
def test_rdbtablespacereference_instantiation(instance):
    assert isinstance(instance, RDBTableSpaceReference)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=gastm::AddressOf_strategy)
@settings(max_examples=50)
def test_gastm::addressof_instantiation(instance):
    assert isinstance(instance, gastm::AddressOf)

@given(instance=gastm::Increment_strategy)
@settings(max_examples=50)
def test_gastm::increment_instantiation(instance):
    assert isinstance(instance, gastm::Increment)

@given(instance=gastm::BitNot_strategy)
@settings(max_examples=50)
def test_gastm::bitnot_instantiation(instance):
    assert isinstance(instance, gastm::BitNot)

@given(instance=gastm::Negate_strategy)
@settings(max_examples=50)
def test_gastm::negate_instantiation(instance):
    assert isinstance(instance, gastm::Negate)

@given(instance=gastm::Decrement_strategy)
@settings(max_examples=50)
def test_gastm::decrement_instantiation(instance):
    assert isinstance(instance, gastm::Decrement)

@given(instance=gastm::Deref_strategy)
@settings(max_examples=50)
def test_gastm::deref_instantiation(instance):
    assert isinstance(instance, gastm::Deref)

@given(instance=gastm::Not_strategy)
@settings(max_examples=50)
def test_gastm::not_instantiation(instance):
    assert isinstance(instance, gastm::Not)

@given(instance=gastm::UnaryPlus_strategy)
@settings(max_examples=50)
def test_gastm::unaryplus_instantiation(instance):
    assert isinstance(instance, gastm::UnaryPlus)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=gastm::CharLiteral_strategy)
@settings(max_examples=50)
def test_gastm::charliteral_instantiation(instance):
    assert isinstance(instance, gastm::CharLiteral)

@given(instance=gastm::RealLiteral_strategy)
@settings(max_examples=50)
def test_gastm::realliteral_instantiation(instance):
    assert isinstance(instance, gastm::RealLiteral)

@given(instance=gastm::StringLiteral_strategy)
@settings(max_examples=50)
def test_gastm::stringliteral_instantiation(instance):
    assert isinstance(instance, gastm::StringLiteral)

@given(instance=gastm::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_gastm::booleanliteral_instantiation(instance):
    assert isinstance(instance, gastm::BooleanLiteral)

@given(instance=gastm::BitLiteral_strategy)
@settings(max_examples=50)
def test_gastm::bitliteral_instantiation(instance):
    assert isinstance(instance, gastm::BitLiteral)

@given(instance=gastm::IntegerlLiteral_strategy)
@settings(max_examples=50)
def test_gastm::integerlliteral_instantiation(instance):
    assert isinstance(instance, gastm::IntegerlLiteral)

@given(instance=QualifiedIdentifierReference_strategy)
@settings(max_examples=50)
def test_qualifiedidentifierreference_instantiation(instance):
    assert isinstance(instance, QualifiedIdentifierReference)

@given(instance=gastm::QualifiedOverData_strategy)
@settings(max_examples=50)
def test_gastm::qualifiedoverdata_instantiation(instance):
    assert isinstance(instance, gastm::QualifiedOverData)

@given(instance=gastm::QualifiedOverPointer_strategy)
@settings(max_examples=50)
def test_gastm::qualifiedoverpointer_instantiation(instance):
    assert isinstance(instance, gastm::QualifiedOverPointer)

@given(instance=gastm::PostDecrement_strategy)
@settings(max_examples=50)
def test_gastm::postdecrement_instantiation(instance):
    assert isinstance(instance, gastm::PostDecrement)

@given(instance=gastm::PostIncrement_strategy)
@settings(max_examples=50)
def test_gastm::postincrement_instantiation(instance):
    assert isinstance(instance, gastm::PostIncrement)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=gastm::Byte_strategy)
@settings(max_examples=50)
def test_gastm::byte_instantiation(instance):
    assert isinstance(instance, gastm::Byte)

@given(instance=gastm::LongInteger_strategy)
@settings(max_examples=50)
def test_gastm::longinteger_instantiation(instance):
    assert isinstance(instance, gastm::LongInteger)

@given(instance=gastm::Integer_strategy)
@settings(max_examples=50)
def test_gastm::integer_instantiation(instance):
    assert isinstance(instance, gastm::Integer)

@given(instance=gastm::Boolean_strategy)
@settings(max_examples=50)
def test_gastm::boolean_instantiation(instance):
    assert isinstance(instance, gastm::Boolean)

@given(instance=gastm::LongDouble_strategy)
@settings(max_examples=50)
def test_gastm::longdouble_instantiation(instance):
    assert isinstance(instance, gastm::LongDouble)

@given(instance=gastm::ShortInteger_strategy)
@settings(max_examples=50)
def test_gastm::shortinteger_instantiation(instance):
    assert isinstance(instance, gastm::ShortInteger)

@given(instance=gastm::Float_strategy)
@settings(max_examples=50)
def test_gastm::float_instantiation(instance):
    assert isinstance(instance, gastm::Float)

@given(instance=gastm::WideCharacter_strategy)
@settings(max_examples=50)
def test_gastm::widecharacter_instantiation(instance):
    assert isinstance(instance, gastm::WideCharacter)

@given(instance=gastm::Double_strategy)
@settings(max_examples=50)
def test_gastm::double_instantiation(instance):
    assert isinstance(instance, gastm::Double)

@given(instance=gastm::Character_strategy)
@settings(max_examples=50)
def test_gastm::character_instantiation(instance):
    assert isinstance(instance, gastm::Character)

@given(instance=gastm::String_strategy)
@settings(max_examples=50)
def test_gastm::string_instantiation(instance):
    assert isinstance(instance, gastm::String)

@given(instance=gastm::Void_strategy)
@settings(max_examples=50)
def test_gastm::void_instantiation(instance):
    assert isinstance(instance, gastm::Void)

@given(instance=StorageSpecification_strategy)
@settings(max_examples=50)
def test_storagespecification_instantiation(instance):
    assert isinstance(instance, StorageSpecification)

@given(instance=gastm::PerClassMember_strategy)
@settings(max_examples=50)
def test_gastm::perclassmember_instantiation(instance):
    assert isinstance(instance, gastm::PerClassMember)

@given(instance=gastm::FunctionPersistent_strategy)
@settings(max_examples=50)
def test_gastm::functionpersistent_instantiation(instance):
    assert isinstance(instance, gastm::FunctionPersistent)

@given(instance=gastm::FileLocal_strategy)
@settings(max_examples=50)
def test_gastm::filelocal_instantiation(instance):
    assert isinstance(instance, gastm::FileLocal)

@given(instance=gastm::NoDef_strategy)
@settings(max_examples=50)
def test_gastm::nodef_instantiation(instance):
    assert isinstance(instance, gastm::NoDef)

@given(instance=gastm::External_strategy)
@settings(max_examples=50)
def test_gastm::external_instantiation(instance):
    assert isinstance(instance, gastm::External)

@given(instance=ForStatement_strategy)
@settings(max_examples=50)
def test_forstatement_instantiation(instance):
    assert isinstance(instance, ForStatement)

@given(instance=gastm::ForCheckAfterStatement_strategy)
@settings(max_examples=50)
def test_gastm::forcheckafterstatement_instantiation(instance):
    assert isinstance(instance, gastm::ForCheckAfterStatement)

@given(instance=gastm::ForCheckBeforeStatement_strategy)
@settings(max_examples=50)
def test_gastm::forcheckbeforestatement_instantiation(instance):
    assert isinstance(instance, gastm::ForCheckBeforeStatement)

@given(instance=AccessKind_strategy)
@settings(max_examples=50)
def test_accesskind_instantiation(instance):
    assert isinstance(instance, AccessKind)

@given(instance=gastm::Private_strategy)
@settings(max_examples=50)
def test_gastm::private_instantiation(instance):
    assert isinstance(instance, gastm::Private)

@given(instance=gastm::Protected_strategy)
@settings(max_examples=50)
def test_gastm::protected_instantiation(instance):
    assert isinstance(instance, gastm::Protected)

@given(instance=gastm::Public_strategy)
@settings(max_examples=50)
def test_gastm::public_instantiation(instance):
    assert isinstance(instance, gastm::Public)

@given(instance=sastm::RDBCloseCursorStatement_strategy)
@settings(max_examples=50)
def test_sastm::rdbclosecursorstatement_instantiation(instance):
    assert isinstance(instance, sastm::RDBCloseCursorStatement)

@given(instance=sastm::RDBDeleteStatement_strategy)
@settings(max_examples=50)
def test_sastm::rdbdeletestatement_instantiation(instance):
    assert isinstance(instance, sastm::RDBDeleteStatement)

@given(instance=gastm::AccessKind_strategy)
@settings(max_examples=50)
def test_gastm::accesskind_instantiation(instance):
    assert isinstance(instance, gastm::AccessKind)

@given(instance=gastm::DataType_strategy)
@settings(max_examples=50)
def test_gastm::datatype_instantiation(instance):
    assert isinstance(instance, gastm::DataType)

@given(instance=gastm::StorageSpecification_strategy)
@settings(max_examples=50)
def test_gastm::storagespecification_instantiation(instance):
    assert isinstance(instance, gastm::StorageSpecification)

@given(instance=gastm::OtherSyntaxObject_strategy)
@settings(max_examples=50)
def test_gastm::othersyntaxobject_instantiation(instance):
    assert isinstance(instance, gastm::OtherSyntaxObject)

@given(instance=gastm::GASTMSemanticObject_strategy)
@settings(max_examples=50)
def test_gastm::gastmsemanticobject_instantiation(instance):
    assert isinstance(instance, gastm::GASTMSemanticObject)

@given(instance=gastm::GASTMSourceObject_strategy)
@settings(max_examples=50)
def test_gastm::gastmsourceobject_instantiation(instance):
    assert isinstance(instance, gastm::GASTMSourceObject)

@given(instance=gastm::GASTMObject_strategy)
@settings(max_examples=50)
def test_gastm::gastmobject_instantiation(instance):
    assert isinstance(instance, gastm::GASTMObject)

@given(instance=ProgramScope_strategy)
@settings(max_examples=50)
def test_programscope_instantiation(instance):
    assert isinstance(instance, ProgramScope)

@given(instance=OtherSyntaxObject_strategy)
@settings(max_examples=50)
def test_othersyntaxobject_instantiation(instance):
    assert isinstance(instance, OtherSyntaxObject)

@given(instance=sastm::RDBIndexColumn_strategy)
@settings(max_examples=50)
def test_sastm::rdbindexcolumn_instantiation(instance):
    assert isinstance(instance, sastm::RDBIndexColumn)

@given(instance=sastm::RDBIndexColumn_strategy)
def test_sastm::rdbindexcolumn_AscendingOrDescending_type(instance):
    assert isinstance(instance.AscendingOrDescending, str)


@given(instance=sastm::RDBIndexColumn_strategy)
def test_sastm::rdbindexcolumn_AscendingOrDescending_setter(instance):
    original = instance.AscendingOrDescending
    instance.AscendingOrDescending = original
    assert instance.AscendingOrDescending == original

@given(instance=gastm::VirtualSpecification_strategy)
@settings(max_examples=50)
def test_gastm::virtualspecification_instantiation(instance):
    assert isinstance(instance, gastm::VirtualSpecification)

@given(instance=gastm::Name_strategy)
@settings(max_examples=50)
def test_gastm::name_instantiation(instance):
    assert isinstance(instance, gastm::Name)

@given(instance=gastm::Name_strategy)
def test_gastm::name_nameString_type(instance):
    assert isinstance(instance.nameString, str)


@given(instance=gastm::Name_strategy)
def test_gastm::name_nameString_setter(instance):
    original = instance.nameString
    instance.nameString = original
    assert instance.nameString == original

@given(instance=sastm::RDBIndex_strategy)
@settings(max_examples=50)
def test_sastm::rdbindex_instantiation(instance):
    assert isinstance(instance, sastm::RDBIndex)

@given(instance=sastm::RDBIndex_strategy)
def test_sastm::rdbindex_NotNull_type(instance):
    assert isinstance(instance.NotNull, bool)


@given(instance=sastm::RDBIndex_strategy)
def test_sastm::rdbindex_NotNull_setter(instance):
    original = instance.NotNull
    instance.NotNull = original
    assert instance.NotNull == original

@given(instance=sastm::RDBIndex_strategy)
def test_sastm::rdbindex_IsUnique_type(instance):
    assert isinstance(instance.IsUnique, bool)


@given(instance=sastm::RDBIndex_strategy)
def test_sastm::rdbindex_IsUnique_setter(instance):
    original = instance.IsUnique
    instance.IsUnique = original
    assert instance.IsUnique == original

@given(instance=gastm::FunctionMemberAttribute_strategy)
@settings(max_examples=50)
def test_gastm::functionmemberattribute_instantiation(instance):
    assert isinstance(instance, gastm::FunctionMemberAttribute)

@given(instance=sastm::RDBTrigger_strategy)
@settings(max_examples=50)
def test_sastm::rdbtrigger_instantiation(instance):
    assert isinstance(instance, sastm::RDBTrigger)

@given(instance=sastm::RDBConstraint_strategy)
@settings(max_examples=50)
def test_sastm::rdbconstraint_instantiation(instance):
    assert isinstance(instance, sastm::RDBConstraint)

@given(instance=gastm::CompilationUnit_strategy)
@settings(max_examples=50)
def test_gastm::compilationunit_instantiation(instance):
    assert isinstance(instance, gastm::CompilationUnit)

@given(instance=gastm::CompilationUnit_strategy)
def test_gastm::compilationunit_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=gastm::CompilationUnit_strategy)
def test_gastm::compilationunit_language_setter(instance):
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

@given(instance=SourceLocation_strategy)
@settings(max_examples=50)
def test_sourcelocation_instantiation(instance):
    assert isinstance(instance, SourceLocation)

@given(instance=GASTMObject_strategy)
@settings(max_examples=50)
def test_gastmobject_instantiation(instance):
    assert isinstance(instance, GASTMObject)

@given(instance=gastm::GASTMSyntaxObject_strategy)
@settings(max_examples=50)
def test_gastm::gastmsyntaxobject_instantiation(instance):
    assert isinstance(instance, gastm::GASTMSyntaxObject)

@given(instance=Scope_strategy)
@settings(max_examples=50)
def test_scope_instantiation(instance):
    assert isinstance(instance, Scope)

@given(instance=gastm::FunctionScope_strategy)
@settings(max_examples=50)
def test_gastm::functionscope_instantiation(instance):
    assert isinstance(instance, gastm::FunctionScope)

@given(instance=gastm::BlockScope_strategy)
@settings(max_examples=50)
def test_gastm::blockscope_instantiation(instance):
    assert isinstance(instance, gastm::BlockScope)

@given(instance=gastm::AggregateScope_strategy)
@settings(max_examples=50)
def test_gastm::aggregatescope_instantiation(instance):
    assert isinstance(instance, gastm::AggregateScope)

@given(instance=gastm::ProgramScope_strategy)
@settings(max_examples=50)
def test_gastm::programscope_instantiation(instance):
    assert isinstance(instance, gastm::ProgramScope)

@given(instance=DefinitionObject_strategy)
@settings(max_examples=50)
def test_definitionobject_instantiation(instance):
    assert isinstance(instance, DefinitionObject)

@given(instance=GlobalScope_strategy)
@settings(max_examples=50)
def test_globalscope_instantiation(instance):
    assert isinstance(instance, GlobalScope)

@given(instance=gastm::GlobalScope_strategy)
@settings(max_examples=50)
def test_gastm::globalscope_instantiation(instance):
    assert isinstance(instance, gastm::GlobalScope)

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=gastm::SpecificIn_strategy)
@settings(max_examples=50)
def test_gastm::specificin_instantiation(instance):
    assert isinstance(instance, gastm::SpecificIn)

@given(instance=gastm::SpecificLike_strategy)
@settings(max_examples=50)
def test_gastm::specificlike_instantiation(instance):
    assert isinstance(instance, gastm::SpecificLike)

@given(instance=gastm::NotGreater_strategy)
@settings(max_examples=50)
def test_gastm::notgreater_instantiation(instance):
    assert isinstance(instance, gastm::NotGreater)

@given(instance=gastm::Assign_strategy)
@settings(max_examples=50)
def test_gastm::assign_instantiation(instance):
    assert isinstance(instance, gastm::Assign)

@given(instance=gastm::Divide_strategy)
@settings(max_examples=50)
def test_gastm::divide_instantiation(instance):
    assert isinstance(instance, gastm::Divide)

@given(instance=gastm::BitXor_strategy)
@settings(max_examples=50)
def test_gastm::bitxor_instantiation(instance):
    assert isinstance(instance, gastm::BitXor)

@given(instance=gastm::Exponent_strategy)
@settings(max_examples=50)
def test_gastm::exponent_instantiation(instance):
    assert isinstance(instance, gastm::Exponent)

@given(instance=gastm::Less_strategy)
@settings(max_examples=50)
def test_gastm::less_instantiation(instance):
    assert isinstance(instance, gastm::Less)

@given(instance=gastm::Or_strategy)
@settings(max_examples=50)
def test_gastm::or_instantiation(instance):
    assert isinstance(instance, gastm::Or)

@given(instance=gastm::Equal_strategy)
@settings(max_examples=50)
def test_gastm::equal_instantiation(instance):
    assert isinstance(instance, gastm::Equal)

@given(instance=gastm::BitRightShift_strategy)
@settings(max_examples=50)
def test_gastm::bitrightshift_instantiation(instance):
    assert isinstance(instance, gastm::BitRightShift)

@given(instance=gastm::Subtract_strategy)
@settings(max_examples=50)
def test_gastm::subtract_instantiation(instance):
    assert isinstance(instance, gastm::Subtract)

@given(instance=gastm::Add_strategy)
@settings(max_examples=50)
def test_gastm::add_instantiation(instance):
    assert isinstance(instance, gastm::Add)

@given(instance=gastm::Greater_strategy)
@settings(max_examples=50)
def test_gastm::greater_instantiation(instance):
    assert isinstance(instance, gastm::Greater)

@given(instance=gastm::SpecificGreaterEqual_strategy)
@settings(max_examples=50)
def test_gastm::specificgreaterequal_instantiation(instance):
    assert isinstance(instance, gastm::SpecificGreaterEqual)

@given(instance=gastm::Multiply_strategy)
@settings(max_examples=50)
def test_gastm::multiply_instantiation(instance):
    assert isinstance(instance, gastm::Multiply)

@given(instance=gastm::SpecificConcatString_strategy)
@settings(max_examples=50)
def test_gastm::specificconcatstring_instantiation(instance):
    assert isinstance(instance, gastm::SpecificConcatString)

@given(instance=gastm::BitLeftShift_strategy)
@settings(max_examples=50)
def test_gastm::bitleftshift_instantiation(instance):
    assert isinstance(instance, gastm::BitLeftShift)

@given(instance=gastm::SpecificLessEqual_strategy)
@settings(max_examples=50)
def test_gastm::specificlessequal_instantiation(instance):
    assert isinstance(instance, gastm::SpecificLessEqual)

@given(instance=gastm::BitOr_strategy)
@settings(max_examples=50)
def test_gastm::bitor_instantiation(instance):
    assert isinstance(instance, gastm::BitOr)

@given(instance=gastm::NotLess_strategy)
@settings(max_examples=50)
def test_gastm::notless_instantiation(instance):
    assert isinstance(instance, gastm::NotLess)

@given(instance=gastm::BitAnd_strategy)
@settings(max_examples=50)
def test_gastm::bitand_instantiation(instance):
    assert isinstance(instance, gastm::BitAnd)

@given(instance=gastm::And_strategy)
@settings(max_examples=50)
def test_gastm::and_instantiation(instance):
    assert isinstance(instance, gastm::And)

@given(instance=gastm::NotEqual_strategy)
@settings(max_examples=50)
def test_gastm::notequal_instantiation(instance):
    assert isinstance(instance, gastm::NotEqual)

@given(instance=gastm::Modulus_strategy)
@settings(max_examples=50)
def test_gastm::modulus_instantiation(instance):
    assert isinstance(instance, gastm::Modulus)

@given(instance=gastm::OperatorAssign_strategy)
@settings(max_examples=50)
def test_gastm::operatorassign_instantiation(instance):
    assert isinstance(instance, gastm::OperatorAssign)

@given(instance=ActualParameter_strategy)
@settings(max_examples=50)
def test_actualparameter_instantiation(instance):
    assert isinstance(instance, ActualParameter)

@given(instance=gastm::MissingActualParameter_strategy)
@settings(max_examples=50)
def test_gastm::missingactualparameter_instantiation(instance):
    assert isinstance(instance, gastm::MissingActualParameter)

@given(instance=gastm::ActualParameterExpression_strategy)
@settings(max_examples=50)
def test_gastm::actualparameterexpression_instantiation(instance):
    assert isinstance(instance, gastm::ActualParameterExpression)

@given(instance=IdentifierReference_strategy)
@settings(max_examples=50)
def test_identifierreference_instantiation(instance):
    assert isinstance(instance, IdentifierReference)

@given(instance=sastm::RDBTableAlias_strategy)
@settings(max_examples=50)
def test_sastm::rdbtablealias_instantiation(instance):
    assert isinstance(instance, sastm::RDBTableAlias)

@given(instance=sastm::RDBTableReference_strategy)
@settings(max_examples=50)
def test_sastm::rdbtablereference_instantiation(instance):
    assert isinstance(instance, sastm::RDBTableReference)

@given(instance=sastm::RDBColumnReference_strategy)
@settings(max_examples=50)
def test_sastm::rdbcolumnreference_instantiation(instance):
    assert isinstance(instance, sastm::RDBColumnReference)

@given(instance=NameReference_strategy)
@settings(max_examples=50)
def test_namereference_instantiation(instance):
    assert isinstance(instance, NameReference)

@given(instance=gastm::IdentifierReference_strategy)
@settings(max_examples=50)
def test_gastm::identifierreference_instantiation(instance):
    assert isinstance(instance, gastm::IdentifierReference)

@given(instance=gastm::TypeQualifiedIdentifierReference_strategy)
@settings(max_examples=50)
def test_gastm::typequalifiedidentifierreference_instantiation(instance):
    assert isinstance(instance, gastm::TypeQualifiedIdentifierReference)

@given(instance=gastm::QualifiedIdentifierReference_strategy)
@settings(max_examples=50)
def test_gastm::qualifiedidentifierreference_instantiation(instance):
    assert isinstance(instance, gastm::QualifiedIdentifierReference)

@given(instance=gastm::CatchBlock_strategy)
@settings(max_examples=50)
def test_gastm::catchblock_instantiation(instance):
    assert isinstance(instance, gastm::CatchBlock)

@given(instance=CatchBlock_strategy)
@settings(max_examples=50)
def test_catchblock_instantiation(instance):
    assert isinstance(instance, CatchBlock)

@given(instance=gastm::TypesCatchBlock_strategy)
@settings(max_examples=50)
def test_gastm::typescatchblock_instantiation(instance):
    assert isinstance(instance, gastm::TypesCatchBlock)

@given(instance=LoopStatement_strategy)
@settings(max_examples=50)
def test_loopstatement_instantiation(instance):
    assert isinstance(instance, LoopStatement)

@given(instance=gastm::DoWhileStatement_strategy)
@settings(max_examples=50)
def test_gastm::dowhilestatement_instantiation(instance):
    assert isinstance(instance, gastm::DoWhileStatement)

@given(instance=gastm::WhileStatement_strategy)
@settings(max_examples=50)
def test_gastm::whilestatement_instantiation(instance):
    assert isinstance(instance, gastm::WhileStatement)

@given(instance=gastm::ForStatement_strategy)
@settings(max_examples=50)
def test_gastm::forstatement_instantiation(instance):
    assert isinstance(instance, gastm::ForStatement)

@given(instance=gastm::VariableCatchBlock_strategy)
@settings(max_examples=50)
def test_gastm::variablecatchblock_instantiation(instance):
    assert isinstance(instance, gastm::VariableCatchBlock)

@given(instance=BlockScope_strategy)
@settings(max_examples=50)
def test_blockscope_instantiation(instance):
    assert isinstance(instance, BlockScope)

@given(instance=LabelDefinition_strategy)
@settings(max_examples=50)
def test_labeldefinition_instantiation(instance):
    assert isinstance(instance, LabelDefinition)

@given(instance=gastm::SwitchCase_strategy)
@settings(max_examples=50)
def test_gastm::switchcase_instantiation(instance):
    assert isinstance(instance, gastm::SwitchCase)

@given(instance=SwitchCase_strategy)
@settings(max_examples=50)
def test_switchcase_instantiation(instance):
    assert isinstance(instance, SwitchCase)

@given(instance=gastm::DefaultBlock_strategy)
@settings(max_examples=50)
def test_gastm::defaultblock_instantiation(instance):
    assert isinstance(instance, gastm::DefaultBlock)

@given(instance=gastm::CaseBlock_strategy)
@settings(max_examples=50)
def test_gastm::caseblock_instantiation(instance):
    assert isinstance(instance, gastm::CaseBlock)

@given(instance=LabelAccess_strategy)
@settings(max_examples=50)
def test_labelaccess_instantiation(instance):
    assert isinstance(instance, LabelAccess)

@given(instance=gastm::Dimension_strategy)
@settings(max_examples=50)
def test_gastm::dimension_instantiation(instance):
    assert isinstance(instance, gastm::Dimension)

@given(instance=Dimension_strategy)
@settings(max_examples=50)
def test_dimension_instantiation(instance):
    assert isinstance(instance, Dimension)

@given(instance=ConstructedType_strategy)
@settings(max_examples=50)
def test_constructedtype_instantiation(instance):
    assert isinstance(instance, ConstructedType)

@given(instance=gastm::PointerType_strategy)
@settings(max_examples=50)
def test_gastm::pointertype_instantiation(instance):
    assert isinstance(instance, gastm::PointerType)

@given(instance=gastm::CollectionType_strategy)
@settings(max_examples=50)
def test_gastm::collectiontype_instantiation(instance):
    assert isinstance(instance, gastm::CollectionType)

@given(instance=gastm::RangeType_strategy)
@settings(max_examples=50)
def test_gastm::rangetype_instantiation(instance):
    assert isinstance(instance, gastm::RangeType)

@given(instance=gastm::ReferenceType_strategy)
@settings(max_examples=50)
def test_gastm::referencetype_instantiation(instance):
    assert isinstance(instance, gastm::ReferenceType)

@given(instance=gastm::ArrayType_strategy)
@settings(max_examples=50)
def test_gastm::arraytype_instantiation(instance):
    assert isinstance(instance, gastm::ArrayType)

@given(instance=AggregateScope_strategy)
@settings(max_examples=50)
def test_aggregatescope_instantiation(instance):
    assert isinstance(instance, AggregateScope)

@given(instance=EnumLiteralDefinition_strategy)
@settings(max_examples=50)
def test_enumliteraldefinition_instantiation(instance):
    assert isinstance(instance, EnumLiteralDefinition)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=sastm::RDBRaw_strategy)
@settings(max_examples=50)
def test_sastm::rdbraw_instantiation(instance):
    assert isinstance(instance, sastm::RDBRaw)

@given(instance=sastm::RDBBoolean_strategy)
@settings(max_examples=50)
def test_sastm::rdbboolean_instantiation(instance):
    assert isinstance(instance, sastm::RDBBoolean)

@given(instance=sastm::RDBClob_strategy)
@settings(max_examples=50)
def test_sastm::rdbclob_instantiation(instance):
    assert isinstance(instance, sastm::RDBClob)

@given(instance=sastm::RDBRowid_strategy)
@settings(max_examples=50)
def test_sastm::rdbrowid_instantiation(instance):
    assert isinstance(instance, sastm::RDBRowid)

@given(instance=sastm::RDBTableType_strategy)
@settings(max_examples=50)
def test_sastm::rdbtabletype_instantiation(instance):
    assert isinstance(instance, sastm::RDBTableType)

@given(instance=sastm::RDBDataBaseType_strategy)
@settings(max_examples=50)
def test_sastm::rdbdatabasetype_instantiation(instance):
    assert isinstance(instance, sastm::RDBDataBaseType)

@given(instance=sastm::RDBTimestamp_strategy)
@settings(max_examples=50)
def test_sastm::rdbtimestamp_instantiation(instance):
    assert isinstance(instance, sastm::RDBTimestamp)

@given(instance=sastm::RDBChar_strategy)
@settings(max_examples=50)
def test_sastm::rdbchar_instantiation(instance):
    assert isinstance(instance, sastm::RDBChar)

@given(instance=sastm::RDBVarchar_strategy)
@settings(max_examples=50)
def test_sastm::rdbvarchar_instantiation(instance):
    assert isinstance(instance, sastm::RDBVarchar)

@given(instance=gastm::AggregateType_strategy)
@settings(max_examples=50)
def test_gastm::aggregatetype_instantiation(instance):
    assert isinstance(instance, gastm::AggregateType)

@given(instance=sastm::RDBNumber_strategy)
@settings(max_examples=50)
def test_sastm::rdbnumber_instantiation(instance):
    assert isinstance(instance, sastm::RDBNumber)

@given(instance=sastm::RDBLong_strategy)
@settings(max_examples=50)
def test_sastm::rdblong_instantiation(instance):
    assert isinstance(instance, sastm::RDBLong)

@given(instance=gastm::EnumType_strategy)
@settings(max_examples=50)
def test_gastm::enumtype_instantiation(instance):
    assert isinstance(instance, gastm::EnumType)

@given(instance=sastm::RDBString_strategy)
@settings(max_examples=50)
def test_sastm::rdbstring_instantiation(instance):
    assert isinstance(instance, sastm::RDBString)

@given(instance=sastm::RDBReal_strategy)
@settings(max_examples=50)
def test_sastm::rdbreal_instantiation(instance):
    assert isinstance(instance, sastm::RDBReal)

@given(instance=sastm::RDBBlob_strategy)
@settings(max_examples=50)
def test_sastm::rdbblob_instantiation(instance):
    assert isinstance(instance, sastm::RDBBlob)

@given(instance=gastm::ExceptionType_strategy)
@settings(max_examples=50)
def test_gastm::exceptiontype_instantiation(instance):
    assert isinstance(instance, gastm::ExceptionType)

@given(instance=sastm::RDBDecimal_strategy)
@settings(max_examples=50)
def test_sastm::rdbdecimal_instantiation(instance):
    assert isinstance(instance, sastm::RDBDecimal)

@given(instance=sastm::RDBNClob_strategy)
@settings(max_examples=50)
def test_sastm::rdbnclob_instantiation(instance):
    assert isinstance(instance, sastm::RDBNClob)

@given(instance=sastm::RDBInteger_strategy)
@settings(max_examples=50)
def test_sastm::rdbinteger_instantiation(instance):
    assert isinstance(instance, sastm::RDBInteger)

@given(instance=sastm::RDBInt_strategy)
@settings(max_examples=50)
def test_sastm::rdbint_instantiation(instance):
    assert isinstance(instance, sastm::RDBInt)

@given(instance=sastm::RDBUserType_strategy)
@settings(max_examples=50)
def test_sastm::rdbusertype_instantiation(instance):
    assert isinstance(instance, sastm::RDBUserType)

@given(instance=sastm::RDBViewType_strategy)
@settings(max_examples=50)
def test_sastm::rdbviewtype_instantiation(instance):
    assert isinstance(instance, sastm::RDBViewType)

@given(instance=sastm::RDBBFile_strategy)
@settings(max_examples=50)
def test_sastm::rdbbfile_instantiation(instance):
    assert isinstance(instance, sastm::RDBBFile)

@given(instance=sastm::RDBFloat_strategy)
@settings(max_examples=50)
def test_sastm::rdbfloat_instantiation(instance):
    assert isinstance(instance, sastm::RDBFloat)

@given(instance=gastm::ConstructedType_strategy)
@settings(max_examples=50)
def test_gastm::constructedtype_instantiation(instance):
    assert isinstance(instance, gastm::ConstructedType)

@given(instance=sastm::RDBDate_strategy)
@settings(max_examples=50)
def test_sastm::rdbdate_instantiation(instance):
    assert isinstance(instance, sastm::RDBDate)

@given(instance=sastm::RDBCursorType_strategy)
@settings(max_examples=50)
def test_sastm::rdbcursortype_instantiation(instance):
    assert isinstance(instance, sastm::RDBCursorType)

@given(instance=sastm::RDBTableSpaceType_strategy)
@settings(max_examples=50)
def test_sastm::rdbtablespacetype_instantiation(instance):
    assert isinstance(instance, sastm::RDBTableSpaceType)

@given(instance=gastm::PrimitiveType_strategy)
@settings(max_examples=50)
def test_gastm::primitivetype_instantiation(instance):
    assert isinstance(instance, gastm::PrimitiveType)

@given(instance=gastm::PrimitiveType_strategy)
def test_gastm::primitivetype_isSigned_type(instance):
    assert isinstance(instance.isSigned, bool)


@given(instance=gastm::PrimitiveType_strategy)
def test_gastm::primitivetype_isSigned_setter(instance):
    original = instance.isSigned
    instance.isSigned = original
    assert instance.isSigned == original

@given(instance=gastm::DerivesFrom_strategy)
@settings(max_examples=50)
def test_gastm::derivesfrom_instantiation(instance):
    assert isinstance(instance, gastm::DerivesFrom)

@given(instance=gastm::DerivesFrom_strategy)
def test_gastm::derivesfrom_isVirtual_type(instance):
    assert isinstance(instance.isVirtual, bool)


@given(instance=gastm::DerivesFrom_strategy)
def test_gastm::derivesfrom_isVirtual_setter(instance):
    original = instance.isVirtual
    instance.isVirtual = original
    assert instance.isVirtual == original

@given(instance=DerivesFrom_strategy)
@settings(max_examples=50)
def test_derivesfrom_instantiation(instance):
    assert isinstance(instance, DerivesFrom)

@given(instance=gastm::NamedType_strategy)
@settings(max_examples=50)
def test_gastm::namedtype_instantiation(instance):
    assert isinstance(instance, gastm::NamedType)

@given(instance=gastm::FormalParameterType_strategy)
@settings(max_examples=50)
def test_gastm::formalparametertype_instantiation(instance):
    assert isinstance(instance, gastm::FormalParameterType)

@given(instance=FormalParameterType_strategy)
@settings(max_examples=50)
def test_formalparametertype_instantiation(instance):
    assert isinstance(instance, FormalParameterType)

@given(instance=gastm::ByValueFormalParameterType_strategy)
@settings(max_examples=50)
def test_gastm::byvalueformalparametertype_instantiation(instance):
    assert isinstance(instance, gastm::ByValueFormalParameterType)

@given(instance=gastm::ByReferenceFormalParameterType_strategy)
@settings(max_examples=50)
def test_gastm::byreferenceformalparametertype_instantiation(instance):
    assert isinstance(instance, gastm::ByReferenceFormalParameterType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=gastm::LabelType_strategy)
@settings(max_examples=50)
def test_gastm::labeltype_instantiation(instance):
    assert isinstance(instance, gastm::LabelType)

@given(instance=gastm::FunctionType_strategy)
@settings(max_examples=50)
def test_gastm::functiontype_instantiation(instance):
    assert isinstance(instance, gastm::FunctionType)

@given(instance=gastm::NameSpaceType_strategy)
@settings(max_examples=50)
def test_gastm::namespacetype_instantiation(instance):
    assert isinstance(instance, gastm::NameSpaceType)

@given(instance=gastm::TypeReference_strategy)
@settings(max_examples=50)
def test_gastm::typereference_instantiation(instance):
    assert isinstance(instance, gastm::TypeReference)

@given(instance=gastm::NameSpaceDefinition_strategy)
@settings(max_examples=50)
def test_gastm::namespacedefinition_instantiation(instance):
    assert isinstance(instance, gastm::NameSpaceDefinition)

@given(instance=AggregateType_strategy)
@settings(max_examples=50)
def test_aggregatetype_instantiation(instance):
    assert isinstance(instance, AggregateType)

@given(instance=gastm::UnionType_strategy)
@settings(max_examples=50)
def test_gastm::uniontype_instantiation(instance):
    assert isinstance(instance, gastm::UnionType)

@given(instance=gastm::StructureType_strategy)
@settings(max_examples=50)
def test_gastm::structuretype_instantiation(instance):
    assert isinstance(instance, gastm::StructureType)

@given(instance=gastm::ClassType_strategy)
@settings(max_examples=50)
def test_gastm::classtype_instantiation(instance):
    assert isinstance(instance, gastm::ClassType)

@given(instance=gastm::AnnotationType_strategy)
@settings(max_examples=50)
def test_gastm::annotationtype_instantiation(instance):
    assert isinstance(instance, gastm::AnnotationType)

@given(instance=NamedType_strategy)
@settings(max_examples=50)
def test_namedtype_instantiation(instance):
    assert isinstance(instance, NamedType)

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=gastm::AggregateTypeDefinition_strategy)
@settings(max_examples=50)
def test_gastm::aggregatetypedefinition_instantiation(instance):
    assert isinstance(instance, gastm::AggregateTypeDefinition)

@given(instance=gastm::NamedTypeDefinition_strategy)
@settings(max_examples=50)
def test_gastm::namedtypedefinition_instantiation(instance):
    assert isinstance(instance, gastm::NamedTypeDefinition)

@given(instance=gastm::TypeDefinition_strategy)
@settings(max_examples=50)
def test_gastm::typedefinition_instantiation(instance):
    assert isinstance(instance, gastm::TypeDefinition)

@given(instance=DataDefinition_strategy)
@settings(max_examples=50)
def test_datadefinition_instantiation(instance):
    assert isinstance(instance, DataDefinition)

@given(instance=gastm::VariableDefinition_strategy)
@settings(max_examples=50)
def test_gastm::variabledefinition_instantiation(instance):
    assert isinstance(instance, gastm::VariableDefinition)

@given(instance=gastm::FormalParameterDefinition_strategy)
@settings(max_examples=50)
def test_gastm::formalparameterdefinition_instantiation(instance):
    assert isinstance(instance, gastm::FormalParameterDefinition)

@given(instance=gastm::BitFieldDefinition_strategy)
@settings(max_examples=50)
def test_gastm::bitfielddefinition_instantiation(instance):
    assert isinstance(instance, gastm::BitFieldDefinition)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=gastm::NameReference_strategy)
@settings(max_examples=50)
def test_gastm::namereference_instantiation(instance):
    assert isinstance(instance, gastm::NameReference)

@given(instance=sastm::RDBHostVariableExpression_strategy)
@settings(max_examples=50)
def test_sastm::rdbhostvariableexpression_instantiation(instance):
    assert isinstance(instance, sastm::RDBHostVariableExpression)

@given(instance=gastm::UnaryExpression_strategy)
@settings(max_examples=50)
def test_gastm::unaryexpression_instantiation(instance):
    assert isinstance(instance, gastm::UnaryExpression)

@given(instance=gastm::BinaryExpression_strategy)
@settings(max_examples=50)
def test_gastm::binaryexpression_instantiation(instance):
    assert isinstance(instance, gastm::BinaryExpression)

@given(instance=gastm::FunctionCallExpression_strategy)
@settings(max_examples=50)
def test_gastm::functioncallexpression_instantiation(instance):
    assert isinstance(instance, gastm::FunctionCallExpression)

@given(instance=gastm::ArrayAccess_strategy)
@settings(max_examples=50)
def test_gastm::arrayaccess_instantiation(instance):
    assert isinstance(instance, gastm::ArrayAccess)

@given(instance=gastm::Literal_strategy)
@settings(max_examples=50)
def test_gastm::literal_instantiation(instance):
    assert isinstance(instance, gastm::Literal)

@given(instance=gastm::Literal_strategy)
def test_gastm::literal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=gastm::Literal_strategy)
def test_gastm::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gastm::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_gastm::conditionalexpression_instantiation(instance):
    assert isinstance(instance, gastm::ConditionalExpression)

@given(instance=gastm::LabelAccess_strategy)
@settings(max_examples=50)
def test_gastm::labelaccess_instantiation(instance):
    assert isinstance(instance, gastm::LabelAccess)

@given(instance=gastm::AggregateExpression_strategy)
@settings(max_examples=50)
def test_gastm::aggregateexpression_instantiation(instance):
    assert isinstance(instance, gastm::AggregateExpression)

@given(instance=gastm::AnnotationExpression_strategy)
@settings(max_examples=50)
def test_gastm::annotationexpression_instantiation(instance):
    assert isinstance(instance, gastm::AnnotationExpression)

@given(instance=gastm::RangeExpression_strategy)
@settings(max_examples=50)
def test_gastm::rangeexpression_instantiation(instance):
    assert isinstance(instance, gastm::RangeExpression)

@given(instance=sastm::RDBSelectExpression_strategy)
@settings(max_examples=50)
def test_sastm::rdbselectexpression_instantiation(instance):
    assert isinstance(instance, sastm::RDBSelectExpression)

@given(instance=gastm::NewExpression_strategy)
@settings(max_examples=50)
def test_gastm::newexpression_instantiation(instance):
    assert isinstance(instance, gastm::NewExpression)

@given(instance=gastm::CastExpression_strategy)
@settings(max_examples=50)
def test_gastm::castexpression_instantiation(instance):
    assert isinstance(instance, gastm::CastExpression)

@given(instance=GASTMSyntaxObject_strategy)
@settings(max_examples=50)
def test_gastmsyntaxobject_instantiation(instance):
    assert isinstance(instance, GASTMSyntaxObject)

@given(instance=gastm::Expression_strategy)
@settings(max_examples=50)
def test_gastm::expression_instantiation(instance):
    assert isinstance(instance, gastm::Expression)

@given(instance=gastm::PreprocessorElement_strategy)
@settings(max_examples=50)
def test_gastm::preprocessorelement_instantiation(instance):
    assert isinstance(instance, gastm::PreprocessorElement)

@given(instance=gastm::Statement_strategy)
@settings(max_examples=50)
def test_gastm::statement_instantiation(instance):
    assert isinstance(instance, gastm::Statement)

@given(instance=gastm::DefinitionObject_strategy)
@settings(max_examples=50)
def test_gastm::definitionobject_instantiation(instance):
    assert isinstance(instance, gastm::DefinitionObject)

@given(instance=gastm::Type_strategy)
@settings(max_examples=50)
def test_gastm::type_instantiation(instance):
    assert isinstance(instance, gastm::Type)

@given(instance=gastm::Type_strategy)
def test_gastm::type_isConst_type(instance):
    assert isinstance(instance.isConst, bool)


@given(instance=gastm::Type_strategy)
def test_gastm::type_isConst_setter(instance):
    original = instance.isConst
    instance.isConst = original
    assert instance.isConst == original

@given(instance=gastm::Type_strategy)
def test_gastm::type_isVolatile_type(instance):
    assert isinstance(instance.isVolatile, bool)


@given(instance=gastm::Type_strategy)
def test_gastm::type_isVolatile_setter(instance):
    original = instance.isVolatile
    instance.isVolatile = original
    assert instance.isVolatile == original

@given(instance=gastm::Comment_strategy)
@settings(max_examples=50)
def test_gastm::comment_instantiation(instance):
    assert isinstance(instance, gastm::Comment)

@given(instance=gastm::Comment_strategy)
def test_gastm::comment_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=gastm::Comment_strategy)
def test_gastm::comment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=gastm::MacroDefinition_strategy)
@settings(max_examples=50)
def test_gastm::macrodefinition_instantiation(instance):
    assert isinstance(instance, gastm::MacroDefinition)

@given(instance=gastm::MacroDefinition_strategy)
def test_gastm::macrodefinition_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=gastm::MacroDefinition_strategy)
def test_gastm::macrodefinition_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=gastm::MacroDefinition_strategy)
def test_gastm::macrodefinition_macroName_type(instance):
    assert isinstance(instance.macroName, str)


@given(instance=gastm::MacroDefinition_strategy)
def test_gastm::macrodefinition_macroName_setter(instance):
    original = instance.macroName
    instance.macroName = original
    assert instance.macroName == original

@given(instance=MacroDefinition_strategy)
@settings(max_examples=50)
def test_macrodefinition_instantiation(instance):
    assert isinstance(instance, MacroDefinition)

@given(instance=gastm::MacroCall_strategy)
@settings(max_examples=50)
def test_gastm::macrocall_instantiation(instance):
    assert isinstance(instance, gastm::MacroCall)

@given(instance=gastm::IncludeUnit_strategy)
@settings(max_examples=50)
def test_gastm::includeunit_instantiation(instance):
    assert isinstance(instance, gastm::IncludeUnit)

@given(instance=LabelType_strategy)
@settings(max_examples=50)
def test_labeltype_instantiation(instance):
    assert isinstance(instance, LabelType)

@given(instance=gastm::LabelDefinition_strategy)
@settings(max_examples=50)
def test_gastm::labeldefinition_instantiation(instance):
    assert isinstance(instance, gastm::LabelDefinition)

@given(instance=NameSpaceType_strategy)
@settings(max_examples=50)
def test_namespacetype_instantiation(instance):
    assert isinstance(instance, NameSpaceType)

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

@given(instance=gastm::FormalParameterDeclaration_strategy)
@settings(max_examples=50)
def test_gastm::formalparameterdeclaration_instantiation(instance):
    assert isinstance(instance, gastm::FormalParameterDeclaration)

@given(instance=gastm::FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_gastm::functiondeclaration_instantiation(instance):
    assert isinstance(instance, gastm::FunctionDeclaration)

@given(instance=Definition_strategy)
@settings(max_examples=50)
def test_definition_instantiation(instance):
    assert isinstance(instance, Definition)

@given(instance=gastm::EnumLiteralDefinition_strategy)
@settings(max_examples=50)
def test_gastm::enumliteraldefinition_instantiation(instance):
    assert isinstance(instance, gastm::EnumLiteralDefinition)

@given(instance=sastm::RDBTableDefinition_strategy)
@settings(max_examples=50)
def test_sastm::rdbtabledefinition_instantiation(instance):
    assert isinstance(instance, sastm::RDBTableDefinition)

@given(instance=sastm::RDBCursorDefinition_strategy)
@settings(max_examples=50)
def test_sastm::rdbcursordefinition_instantiation(instance):
    assert isinstance(instance, sastm::RDBCursorDefinition)

@given(instance=sastm::RDBColumnDefinition_strategy)
@settings(max_examples=50)
def test_sastm::rdbcolumndefinition_instantiation(instance):
    assert isinstance(instance, sastm::RDBColumnDefinition)

@given(instance=sastm::RDBColumnDefinition_strategy)
def test_sastm::rdbcolumndefinition_NotNull_type(instance):
    assert isinstance(instance.NotNull, bool)


@given(instance=sastm::RDBColumnDefinition_strategy)
def test_sastm::rdbcolumndefinition_NotNull_setter(instance):
    original = instance.NotNull
    instance.NotNull = original
    assert instance.NotNull == original

@given(instance=sastm::RDBUserDefinition_strategy)
@settings(max_examples=50)
def test_sastm::rdbuserdefinition_instantiation(instance):
    assert isinstance(instance, sastm::RDBUserDefinition)

@given(instance=gastm::DataDefinition_strategy)
@settings(max_examples=50)
def test_gastm::datadefinition_instantiation(instance):
    assert isinstance(instance, gastm::DataDefinition)

@given(instance=gastm::DataDefinition_strategy)
def test_gastm::datadefinition_isMutable_type(instance):
    assert isinstance(instance.isMutable, bool)


@given(instance=gastm::DataDefinition_strategy)
def test_gastm::datadefinition_isMutable_setter(instance):
    original = instance.isMutable
    instance.isMutable = original
    assert instance.isMutable == original

@given(instance=sastm::RDBViewDefinition_strategy)
@settings(max_examples=50)
def test_sastm::rdbviewdefinition_instantiation(instance):
    assert isinstance(instance, sastm::RDBViewDefinition)

@given(instance=sastm::RDBTableSpaceDefinition_strategy)
@settings(max_examples=50)
def test_sastm::rdbtablespacedefinition_instantiation(instance):
    assert isinstance(instance, sastm::RDBTableSpaceDefinition)

@given(instance=gastm::SpecificTriggerDefinition_strategy)
@settings(max_examples=50)
def test_gastm::specifictriggerdefinition_instantiation(instance):
    assert isinstance(instance, gastm::SpecificTriggerDefinition)

@given(instance=sastm::RDBDatabaseDefinition_strategy)
@settings(max_examples=50)
def test_sastm::rdbdatabasedefinition_instantiation(instance):
    assert isinstance(instance, sastm::RDBDatabaseDefinition)

@given(instance=TypeReference_strategy)
@settings(max_examples=50)
def test_typereference_instantiation(instance):
    assert isinstance(instance, TypeReference)

@given(instance=gastm::NamedTypeReference_strategy)
@settings(max_examples=50)
def test_gastm::namedtypereference_instantiation(instance):
    assert isinstance(instance, gastm::NamedTypeReference)

@given(instance=gastm::UnnamedTypeReference_strategy)
@settings(max_examples=50)
def test_gastm::unnamedtypereference_instantiation(instance):
    assert isinstance(instance, gastm::UnnamedTypeReference)

@given(instance=Name_strategy)
@settings(max_examples=50)
def test_name_instantiation(instance):
    assert isinstance(instance, Name)

@given(instance=DeclarationOrDefinition_strategy)
@settings(max_examples=50)
def test_declarationordefinition_instantiation(instance):
    assert isinstance(instance, DeclarationOrDefinition)

@given(instance=gastm::Declaration_strategy)
@settings(max_examples=50)
def test_gastm::declaration_instantiation(instance):
    assert isinstance(instance, gastm::Declaration)

@given(instance=gastm::Definition_strategy)
@settings(max_examples=50)
def test_gastm::definition_instantiation(instance):
    assert isinstance(instance, gastm::Definition)

@given(instance=gastm::DeclarationOrDefinition_strategy)
@settings(max_examples=50)
def test_gastm::declarationordefinition_instantiation(instance):
    assert isinstance(instance, gastm::DeclarationOrDefinition)

@given(instance=gastm::DeclarationOrDefinition_strategy)
def test_gastm::declarationordefinition_isRegister_type(instance):
    assert isinstance(instance.isRegister, bool)


@given(instance=gastm::DeclarationOrDefinition_strategy)
def test_gastm::declarationordefinition_isRegister_setter(instance):
    original = instance.isRegister
    instance.isRegister = original
    assert instance.isRegister == original

@given(instance=gastm::DeclarationOrDefinition_strategy)
def test_gastm::declarationordefinition_linkageSpecifier_type(instance):
    assert isinstance(instance.linkageSpecifier, str)


@given(instance=gastm::DeclarationOrDefinition_strategy)
def test_gastm::declarationordefinition_linkageSpecifier_setter(instance):
    original = instance.linkageSpecifier
    instance.linkageSpecifier = original
    assert instance.linkageSpecifier == original

@given(instance=gastm::EntryDefinition_strategy)
@settings(max_examples=50)
def test_gastm::entrydefinition_instantiation(instance):
    assert isinstance(instance, gastm::EntryDefinition)

@given(instance=VirtualSpecification_strategy)
@settings(max_examples=50)
def test_virtualspecification_instantiation(instance):
    assert isinstance(instance, VirtualSpecification)

@given(instance=gastm::Virtual_strategy)
@settings(max_examples=50)
def test_gastm::virtual_instantiation(instance):
    assert isinstance(instance, gastm::Virtual)

@given(instance=gastm::NonVirtual_strategy)
@settings(max_examples=50)
def test_gastm::nonvirtual_instantiation(instance):
    assert isinstance(instance, gastm::NonVirtual)

@given(instance=gastm::PureVirtual_strategy)
@settings(max_examples=50)
def test_gastm::purevirtual_instantiation(instance):
    assert isinstance(instance, gastm::PureVirtual)

@given(instance=gastm::FunctionMemberAttributes_strategy)
@settings(max_examples=50)
def test_gastm::functionmemberattributes_instantiation(instance):
    assert isinstance(instance, gastm::FunctionMemberAttributes)

@given(instance=gastm::FunctionMemberAttributes_strategy)
def test_gastm::functionmemberattributes_isInline_type(instance):
    assert isinstance(instance.isInline, bool)


@given(instance=gastm::FunctionMemberAttributes_strategy)
def test_gastm::functionmemberattributes_isInline_setter(instance):
    original = instance.isInline
    instance.isInline = original
    assert instance.isInline == original

@given(instance=gastm::FunctionMemberAttributes_strategy)
def test_gastm::functionmemberattributes_isFriend_type(instance):
    assert isinstance(instance.isFriend, bool)


@given(instance=gastm::FunctionMemberAttributes_strategy)
def test_gastm::functionmemberattributes_isFriend_setter(instance):
    original = instance.isFriend
    instance.isFriend = original
    assert instance.isFriend == original

@given(instance=gastm::FunctionMemberAttributes_strategy)
def test_gastm::functionmemberattributes_isThisConst_type(instance):
    assert isinstance(instance.isThisConst, bool)


@given(instance=gastm::FunctionMemberAttributes_strategy)
def test_gastm::functionmemberattributes_isThisConst_setter(instance):
    original = instance.isThisConst
    instance.isThisConst = original
    assert instance.isThisConst == original

@given(instance=FunctionScope_strategy)
@settings(max_examples=50)
def test_functionscope_instantiation(instance):
    assert isinstance(instance, FunctionScope)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=gastm::JumpStatement_strategy)
@settings(max_examples=50)
def test_gastm::jumpstatement_instantiation(instance):
    assert isinstance(instance, gastm::JumpStatement)

@given(instance=sastm::RDBConnectStatement_strategy)
@settings(max_examples=50)
def test_sastm::rdbconnectstatement_instantiation(instance):
    assert isinstance(instance, sastm::RDBConnectStatement)

@given(instance=gastm::LoopStatement_strategy)
@settings(max_examples=50)
def test_gastm::loopstatement_instantiation(instance):
    assert isinstance(instance, gastm::LoopStatement)

@given(instance=gastm::DeleteStatement_strategy)
@settings(max_examples=50)
def test_gastm::deletestatement_instantiation(instance):
    assert isinstance(instance, gastm::DeleteStatement)

@given(instance=gastm::LabeledStatement_strategy)
@settings(max_examples=50)
def test_gastm::labeledstatement_instantiation(instance):
    assert isinstance(instance, gastm::LabeledStatement)

@given(instance=gastm::IfStatement_strategy)
@settings(max_examples=50)
def test_gastm::ifstatement_instantiation(instance):
    assert isinstance(instance, gastm::IfStatement)

@given(instance=gastm::TerminateStatement_strategy)
@settings(max_examples=50)
def test_gastm::terminatestatement_instantiation(instance):
    assert isinstance(instance, gastm::TerminateStatement)

@given(instance=gastm::ContinueStatement_strategy)
@settings(max_examples=50)
def test_gastm::continuestatement_instantiation(instance):
    assert isinstance(instance, gastm::ContinueStatement)

@given(instance=gastm::SwitchStatement_strategy)
@settings(max_examples=50)
def test_gastm::switchstatement_instantiation(instance):
    assert isinstance(instance, gastm::SwitchStatement)

@given(instance=sastm::RDBCursorStatement_strategy)
@settings(max_examples=50)
def test_sastm::rdbcursorstatement_instantiation(instance):
    assert isinstance(instance, sastm::RDBCursorStatement)

@given(instance=gastm::DeclarationOrDefinitionStatement_strategy)
@settings(max_examples=50)
def test_gastm::declarationordefinitionstatement_instantiation(instance):
    assert isinstance(instance, gastm::DeclarationOrDefinitionStatement)

@given(instance=sastm::RDBSelectStatement_strategy)
@settings(max_examples=50)
def test_sastm::rdbselectstatement_instantiation(instance):
    assert isinstance(instance, sastm::RDBSelectStatement)

@given(instance=gastm::ReturnStatement_strategy)
@settings(max_examples=50)
def test_gastm::returnstatement_instantiation(instance):
    assert isinstance(instance, gastm::ReturnStatement)

@given(instance=sastm::RDBModifyStatement_strategy)
@settings(max_examples=50)
def test_sastm::rdbmodifystatement_instantiation(instance):
    assert isinstance(instance, sastm::RDBModifyStatement)

@given(instance=gastm::BlockStatement_strategy)
@settings(max_examples=50)
def test_gastm::blockstatement_instantiation(instance):
    assert isinstance(instance, gastm::BlockStatement)

@given(instance=gastm::TryStatement_strategy)
@settings(max_examples=50)
def test_gastm::trystatement_instantiation(instance):
    assert isinstance(instance, gastm::TryStatement)

@given(instance=sastm::RDBInsertStatement_strategy)
@settings(max_examples=50)
def test_sastm::rdbinsertstatement_instantiation(instance):
    assert isinstance(instance, sastm::RDBInsertStatement)

@given(instance=gastm::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_gastm::expressionstatement_instantiation(instance):
    assert isinstance(instance, gastm::ExpressionStatement)

@given(instance=gastm::ThrowStatement_strategy)
@settings(max_examples=50)
def test_gastm::throwstatement_instantiation(instance):
    assert isinstance(instance, gastm::ThrowStatement)

@given(instance=gastm::SpecificSelectStatement_strategy)
@settings(max_examples=50)
def test_gastm::specificselectstatement_instantiation(instance):
    assert isinstance(instance, gastm::SpecificSelectStatement)

@given(instance=gastm::BreakStatement_strategy)
@settings(max_examples=50)
def test_gastm::breakstatement_instantiation(instance):
    assert isinstance(instance, gastm::BreakStatement)

@given(instance=gastm::EmptyStatement_strategy)
@settings(max_examples=50)
def test_gastm::emptystatement_instantiation(instance):
    assert isinstance(instance, gastm::EmptyStatement)

@given(instance=FormalParameterDefinition_strategy)
@settings(max_examples=50)
def test_formalparameterdefinition_instantiation(instance):
    assert isinstance(instance, FormalParameterDefinition)

@given(instance=gastm::FunctionDefinition_strategy)
@settings(max_examples=50)
def test_gastm::functiondefinition_instantiation(instance):
    assert isinstance(instance, gastm::FunctionDefinition)

@given(instance=gastm::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_gastm::variabledeclaration_instantiation(instance):
    assert isinstance(instance, gastm::VariableDeclaration)

@given(instance=gastm::VariableDeclaration_strategy)
def test_gastm::variabledeclaration_isMutable_type(instance):
    assert isinstance(instance.isMutable, bool)


@given(instance=gastm::VariableDeclaration_strategy)
def test_gastm::variabledeclaration_isMutable_setter(instance):
    original = instance.isMutable
    instance.isMutable = original
    assert instance.isMutable == original

@given(instance=CompilationUnit_strategy)
@settings(max_examples=50)
def test_compilationunit_instantiation(instance):
    assert isinstance(instance, CompilationUnit)

@given(instance=GASTMSemanticObject_strategy)
@settings(max_examples=50)
def test_gastmsemanticobject_instantiation(instance):
    assert isinstance(instance, GASTMSemanticObject)

@given(instance=gastm::Scope_strategy)
@settings(max_examples=50)
def test_gastm::scope_instantiation(instance):
    assert isinstance(instance, gastm::Scope)

@given(instance=gastm::Project_strategy)
@settings(max_examples=50)
def test_gastm::project_instantiation(instance):
    assert isinstance(instance, gastm::Project)

@given(instance=SourceFile_strategy)
@settings(max_examples=50)
def test_sourcefile_instantiation(instance):
    assert isinstance(instance, SourceFile)

@given(instance=GASTMSourceObject_strategy)
@settings(max_examples=50)
def test_gastmsourceobject_instantiation(instance):
    assert isinstance(instance, GASTMSourceObject)

@given(instance=gastm::SourceLocation_strategy)
@settings(max_examples=50)
def test_gastm::sourcelocation_instantiation(instance):
    assert isinstance(instance, gastm::SourceLocation)

@given(instance=gastm::SourceLocation_strategy)
def test_gastm::sourcelocation_startLine_type(instance):
    assert isinstance(instance.startLine, int)


@given(instance=gastm::SourceLocation_strategy)
def test_gastm::sourcelocation_startLine_setter(instance):
    original = instance.startLine
    instance.startLine = original
    assert instance.startLine == original

@given(instance=gastm::SourceLocation_strategy)
def test_gastm::sourcelocation_endLine_type(instance):
    assert isinstance(instance.endLine, int)


@given(instance=gastm::SourceLocation_strategy)
def test_gastm::sourcelocation_endLine_setter(instance):
    original = instance.endLine
    instance.endLine = original
    assert instance.endLine == original

@given(instance=gastm::SourceLocation_strategy)
def test_gastm::sourcelocation_startColumn_type(instance):
    assert isinstance(instance.startColumn, int)


@given(instance=gastm::SourceLocation_strategy)
def test_gastm::sourcelocation_startColumn_setter(instance):
    original = instance.startColumn
    instance.startColumn = original
    assert instance.startColumn == original

@given(instance=gastm::SourceLocation_strategy)
def test_gastm::sourcelocation_endColumn_type(instance):
    assert isinstance(instance.endColumn, int)


@given(instance=gastm::SourceLocation_strategy)
def test_gastm::sourcelocation_endColumn_setter(instance):
    original = instance.endColumn
    instance.endColumn = original
    assert instance.endColumn == original

@given(instance=gastm::SourceFile_strategy)
@settings(max_examples=50)
def test_gastm::sourcefile_instantiation(instance):
    assert isinstance(instance, gastm::SourceFile)

@given(instance=gastm::SourceFile_strategy)
def test_gastm::sourcefile_pathName_type(instance):
    assert isinstance(instance.pathName, str)


@given(instance=gastm::SourceFile_strategy)
def test_gastm::sourcefile_pathName_setter(instance):
    original = instance.pathName
    instance.pathName = original
    assert instance.pathName == original

@given(instance=gastm::ActualParameter_strategy)
@settings(max_examples=50)
def test_gastm::actualparameter_instantiation(instance):
    assert isinstance(instance, gastm::ActualParameter)

@given(instance=gastm::BinaryOperator_strategy)
@settings(max_examples=50)
def test_gastm::binaryoperator_instantiation(instance):
    assert isinstance(instance, gastm::BinaryOperator)

@given(instance=gastm::UnaryOperator_strategy)
@settings(max_examples=50)
def test_gastm::unaryoperator_instantiation(instance):
    assert isinstance(instance, gastm::UnaryOperator)
