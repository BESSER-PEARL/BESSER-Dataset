import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ActualParameterExpression,
    gastm::ByReferenceActualParameterExpression,
    gastm::ByValueActualParameterExpression,
    UnaryOperator,
    gastm::AddressOf,
    gastm::Negate,
    gastm::PostIncrement,
    gastm::Not,
    gastm::BitNot,
    gastm::Deref,
    gastm::Decrement,
    gastm::Increment,
    gastm::PostDecrement,
    gastm::UnaryPlus,
    Literal,
    gastm::CharLiteral,
    gastm::BitLiteral,
    gastm::RealLiteral,
    gastm::BooleanLiteral,
    gastm::IntegerlLiteral,
    QualifiedIdentifierReference,
    gastm::QualifiedOverData,
    gastm::QualifiedOverPointer,
    ForStatement,
    gastm::ForCheckAfterStatement,
    gastm::ForCheckBeforeStatement,
    AccessKind,
    gastm::Private,
    gastm::Protected,
    gastm::Public,
    gastm::StringLiteral,
    PrimitiveType,
    gastm::Byte,
    gastm::Character,
    gastm::Double,
    gastm::LongInteger,
    gastm::ShortInteger,
    gastm::String,
    gastm::WideCharacter,
    gastm::LongDouble,
    gastm::Float,
    gastm::Integer,
    gastm::Void,
    StorageSpecification,
    gastm::FunctionPersistent,
    gastm::PerClassMember,
    gastm::NoDef,
    gastm::FileLocal,
    gastm::External,
    gastm::Boolean,
    ActualParameter,
    gastm::MissingActualParameter,
    gastm::ActualParameterExpression,
    BinaryOperator,
    gastm::BitRightShift,
    gastm::Subtract,
    gastm::BitXor,
    gastm::Less,
    gastm::Multiply,
    gastm::Add,
    gastm::BitLeftShift,
    gastm::Assign,
    gastm::Modulus,
    gastm::Greater,
    gastm::BitAnd,
    gastm::NotLess,
    gastm::NotEqual,
    gastm::Divide,
    gastm::Exponent,
    gastm::NotGreater,
    gastm::Equal,
    gastm::And,
    gastm::BitOr,
    gastm::Or,
    gastm::OperatorAssign,
    NameReference,
    gastm::IdentifierReference,
    gastm::QualifiedIdentifierReference,
    gastm::TypeQualifiedIdentifierReference,
    IdentifierReference,
    CatchBlock,
    LoopStatement,
    gastm::DoWhileStatement,
    gastm::WhileStatement,
    gastm::ForStatement,
    gastm::VariableCatchBlock,
    gastm::TypesCatchBlock,
    SwitchCase,
    gastm::CaseBlock,
    gastm::DefaultBlock,
    BlockScope,
    LabelDefinition,
    DerivesFrom,
    LabelAccess,
    ConstructedType,
    gastm::CollectionType,
    gastm::ReferenceType,
    gastm::RangeType,
    gastm::PointerType,
    gastm::ArrayType,
    AggregateScope,
    EnumLiteralDefinition,
    DataType,
    gastm::ConstructedType,
    gastm::EnumType,
    gastm::AggregateType,
    gastm::ExceptionType,
    gastm::PrimitiveType,
    gastm::NamedType,
    gastm::FormalParameterType,
    FormalParameterType,
    gastm::ByReferenceFormalParameterType,
    gastm::ByValueFormalParameterType,
    Type,
    gastm::LabelType,
    gastm::TypeReference,
    gastm::NameSpaceType,
    gastm::FunctionType,
    Dimension,
    NameSpaceType,
    AggregateType,
    gastm::ClassType,
    gastm::UnionType,
    gastm::AnnotationType,
    gastm::StructureType,
    NamedType,
    TypeDefinition,
    gastm::AggregateTypeDefinition,
    gastm::NamedTypeDefinition,
    GASTMSyntaxObject,
    gastm::DefinitionObject,
    gastm::PreprocessorElement,
    gastm::Expression,
    gastm::Statement,
    gastm::Type,
    MacroDefinition,
    LabelType,
    gastm::FunctionMemberAttributes,
    FunctionScope,
    Statement,
    gastm::EmptyStatement,
    gastm::ContinueStatement,
    gastm::ExpressionStatement,
    gastm::ReturnStatement,
    gastm::BlockStatement,
    gastm::DeclarationOrDefinitionStatement,
    gastm::LabeledStatement,
    gastm::DeleteStatement,
    gastm::TryStatement,
    gastm::SwitchStatement,
    gastm::IfStatement,
    gastm::TerminateStatement,
    gastm::BreakStatement,
    gastm::ThrowStatement,
    gastm::LoopStatement,
    gastm::JumpStatement,
    FormalParameterDefinition,
    DataDefinition,
    gastm::FormalParameterDefinition,
    gastm::VariableDefinition,
    gastm::BitFieldDefinition,
    Expression,
    gastm::AggregateExpression,
    gastm::LabelAccess,
    gastm::ArrayAccess,
    gastm::BinaryExpression,
    gastm::CastExpression,
    gastm::FunctionCallExpression,
    gastm::RangeExpression,
    gastm::ConditionalExpression,
    gastm::NewExpression,
    gastm::AnnotationExpression,
    gastm::UnaryExpression,
    gastm::Literal,
    gastm::NameReference,
    VirtualSpecification,
    gastm::Virtual,
    gastm::NonVirtual,
    gastm::PureVirtual,
    FormalParameterDeclaration,
    Declaration,
    gastm::FormalParameterDeclaration,
    gastm::FunctionDeclaration,
    Definition,
    gastm::EnumLiteralDefinition,
    gastm::EntryDefinition,
    gastm::FunctionDefinition,
    gastm::DataDefinition,
    TypeReference,
    gastm::NamedTypeReference,
    gastm::UnnamedTypeReference,
    Name,
    DeclarationOrDefinition,
    gastm::Declaration,
    gastm::Definition,
    gastm::VariableDeclaration,
    FunctionMemberAttributes,
    SourceLocation,
    GASTMObject,
    gastm::GASTMSyntaxObject,
    Scope,
    gastm::BlockScope,
    gastm::ProgramScope,
    gastm::AggregateScope,
    gastm::GlobalScope,
    gastm::FunctionScope,
    DefinitionObject,
    gastm::LabelDefinition,
    gastm::NameSpaceDefinition,
    gastm::TypeDefinition,
    GlobalScope,
    CompilationUnit,
    GASTMSemanticObject,
    gastm::Scope,
    gastm::Project,
    SourceFile,
    gastm::DeclarationOrDefinition,
    ProgramScope,
    OtherSyntaxObject,
    gastm::Name,
    gastm::Dimension,
    gastm::DerivesFrom,
    gastm::VirtualSpecification,
    gastm::SwitchCase,
    gastm::FunctionMemberAttribute,
    gastm::CatchBlock,
    gastm::CompilationUnit,
    AnnotationExpression,
    PreprocessorElement,
    gastm::MacroDefinition,
    gastm::MacroCall,
    gastm::IncludeUnit,
    gastm::Comment,
    GASTMSourceObject,
    gastm::SourceLocation,
    gastm::SourceFile,
    gastm::ActualParameter,
    gastm::BinaryOperator,
    gastm::UnaryOperator,
    gastm::AccessKind,
    gastm::DataType,
    gastm::StorageSpecification,
    gastm::OtherSyntaxObject,
    gastm::GASTMSemanticObject,
    gastm::GASTMSourceObject,
    gastm::GASTMObject,
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



def test_gastm::negate_is_not_abstract():
    assert not inspect.isabstract(gastm::Negate)


def test_gastm::negate_constructor_exists():
    assert callable(gastm::Negate.__init__)


def test_gastm::negate_constructor_args():
    sig = inspect.signature(gastm::Negate.__init__)
    params = list(sig.parameters.keys())



def test_gastm::postincrement_is_not_abstract():
    assert not inspect.isabstract(gastm::PostIncrement)


def test_gastm::postincrement_constructor_exists():
    assert callable(gastm::PostIncrement.__init__)


def test_gastm::postincrement_constructor_args():
    sig = inspect.signature(gastm::PostIncrement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::not_is_not_abstract():
    assert not inspect.isabstract(gastm::Not)


def test_gastm::not_constructor_exists():
    assert callable(gastm::Not.__init__)


def test_gastm::not_constructor_args():
    sig = inspect.signature(gastm::Not.__init__)
    params = list(sig.parameters.keys())



def test_gastm::bitnot_is_not_abstract():
    assert not inspect.isabstract(gastm::BitNot)


def test_gastm::bitnot_constructor_exists():
    assert callable(gastm::BitNot.__init__)


def test_gastm::bitnot_constructor_args():
    sig = inspect.signature(gastm::BitNot.__init__)
    params = list(sig.parameters.keys())



def test_gastm::deref_is_not_abstract():
    assert not inspect.isabstract(gastm::Deref)


def test_gastm::deref_constructor_exists():
    assert callable(gastm::Deref.__init__)


def test_gastm::deref_constructor_args():
    sig = inspect.signature(gastm::Deref.__init__)
    params = list(sig.parameters.keys())



def test_gastm::decrement_is_not_abstract():
    assert not inspect.isabstract(gastm::Decrement)


def test_gastm::decrement_constructor_exists():
    assert callable(gastm::Decrement.__init__)


def test_gastm::decrement_constructor_args():
    sig = inspect.signature(gastm::Decrement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::increment_is_not_abstract():
    assert not inspect.isabstract(gastm::Increment)


def test_gastm::increment_constructor_exists():
    assert callable(gastm::Increment.__init__)


def test_gastm::increment_constructor_args():
    sig = inspect.signature(gastm::Increment.__init__)
    params = list(sig.parameters.keys())



def test_gastm::postdecrement_is_not_abstract():
    assert not inspect.isabstract(gastm::PostDecrement)


def test_gastm::postdecrement_constructor_exists():
    assert callable(gastm::PostDecrement.__init__)


def test_gastm::postdecrement_constructor_args():
    sig = inspect.signature(gastm::PostDecrement.__init__)
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



def test_gastm::bitliteral_is_not_abstract():
    assert not inspect.isabstract(gastm::BitLiteral)


def test_gastm::bitliteral_constructor_exists():
    assert callable(gastm::BitLiteral.__init__)


def test_gastm::bitliteral_constructor_args():
    sig = inspect.signature(gastm::BitLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gastm::realliteral_is_not_abstract():
    assert not inspect.isabstract(gastm::RealLiteral)


def test_gastm::realliteral_constructor_exists():
    assert callable(gastm::RealLiteral.__init__)


def test_gastm::realliteral_constructor_args():
    sig = inspect.signature(gastm::RealLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gastm::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(gastm::BooleanLiteral)


def test_gastm::booleanliteral_constructor_exists():
    assert callable(gastm::BooleanLiteral.__init__)


def test_gastm::booleanliteral_constructor_args():
    sig = inspect.signature(gastm::BooleanLiteral.__init__)
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



def test_gastm::stringliteral_is_not_abstract():
    assert not inspect.isabstract(gastm::StringLiteral)


def test_gastm::stringliteral_constructor_exists():
    assert callable(gastm::StringLiteral.__init__)


def test_gastm::stringliteral_constructor_args():
    sig = inspect.signature(gastm::StringLiteral.__init__)
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



def test_gastm::character_is_not_abstract():
    assert not inspect.isabstract(gastm::Character)


def test_gastm::character_constructor_exists():
    assert callable(gastm::Character.__init__)


def test_gastm::character_constructor_args():
    sig = inspect.signature(gastm::Character.__init__)
    params = list(sig.parameters.keys())



def test_gastm::double_is_not_abstract():
    assert not inspect.isabstract(gastm::Double)


def test_gastm::double_constructor_exists():
    assert callable(gastm::Double.__init__)


def test_gastm::double_constructor_args():
    sig = inspect.signature(gastm::Double.__init__)
    params = list(sig.parameters.keys())



def test_gastm::longinteger_is_not_abstract():
    assert not inspect.isabstract(gastm::LongInteger)


def test_gastm::longinteger_constructor_exists():
    assert callable(gastm::LongInteger.__init__)


def test_gastm::longinteger_constructor_args():
    sig = inspect.signature(gastm::LongInteger.__init__)
    params = list(sig.parameters.keys())



def test_gastm::shortinteger_is_not_abstract():
    assert not inspect.isabstract(gastm::ShortInteger)


def test_gastm::shortinteger_constructor_exists():
    assert callable(gastm::ShortInteger.__init__)


def test_gastm::shortinteger_constructor_args():
    sig = inspect.signature(gastm::ShortInteger.__init__)
    params = list(sig.parameters.keys())



def test_gastm::string_is_not_abstract():
    assert not inspect.isabstract(gastm::String)


def test_gastm::string_constructor_exists():
    assert callable(gastm::String.__init__)


def test_gastm::string_constructor_args():
    sig = inspect.signature(gastm::String.__init__)
    params = list(sig.parameters.keys())



def test_gastm::widecharacter_is_not_abstract():
    assert not inspect.isabstract(gastm::WideCharacter)


def test_gastm::widecharacter_constructor_exists():
    assert callable(gastm::WideCharacter.__init__)


def test_gastm::widecharacter_constructor_args():
    sig = inspect.signature(gastm::WideCharacter.__init__)
    params = list(sig.parameters.keys())



def test_gastm::longdouble_is_not_abstract():
    assert not inspect.isabstract(gastm::LongDouble)


def test_gastm::longdouble_constructor_exists():
    assert callable(gastm::LongDouble.__init__)


def test_gastm::longdouble_constructor_args():
    sig = inspect.signature(gastm::LongDouble.__init__)
    params = list(sig.parameters.keys())



def test_gastm::float_is_not_abstract():
    assert not inspect.isabstract(gastm::Float)


def test_gastm::float_constructor_exists():
    assert callable(gastm::Float.__init__)


def test_gastm::float_constructor_args():
    sig = inspect.signature(gastm::Float.__init__)
    params = list(sig.parameters.keys())



def test_gastm::integer_is_not_abstract():
    assert not inspect.isabstract(gastm::Integer)


def test_gastm::integer_constructor_exists():
    assert callable(gastm::Integer.__init__)


def test_gastm::integer_constructor_args():
    sig = inspect.signature(gastm::Integer.__init__)
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



def test_gastm::functionpersistent_is_not_abstract():
    assert not inspect.isabstract(gastm::FunctionPersistent)


def test_gastm::functionpersistent_constructor_exists():
    assert callable(gastm::FunctionPersistent.__init__)


def test_gastm::functionpersistent_constructor_args():
    sig = inspect.signature(gastm::FunctionPersistent.__init__)
    params = list(sig.parameters.keys())



def test_gastm::perclassmember_is_not_abstract():
    assert not inspect.isabstract(gastm::PerClassMember)


def test_gastm::perclassmember_constructor_exists():
    assert callable(gastm::PerClassMember.__init__)


def test_gastm::perclassmember_constructor_args():
    sig = inspect.signature(gastm::PerClassMember.__init__)
    params = list(sig.parameters.keys())



def test_gastm::nodef_is_not_abstract():
    assert not inspect.isabstract(gastm::NoDef)


def test_gastm::nodef_constructor_exists():
    assert callable(gastm::NoDef.__init__)


def test_gastm::nodef_constructor_args():
    sig = inspect.signature(gastm::NoDef.__init__)
    params = list(sig.parameters.keys())



def test_gastm::filelocal_is_not_abstract():
    assert not inspect.isabstract(gastm::FileLocal)


def test_gastm::filelocal_constructor_exists():
    assert callable(gastm::FileLocal.__init__)


def test_gastm::filelocal_constructor_args():
    sig = inspect.signature(gastm::FileLocal.__init__)
    params = list(sig.parameters.keys())



def test_gastm::external_is_not_abstract():
    assert not inspect.isabstract(gastm::External)


def test_gastm::external_constructor_exists():
    assert callable(gastm::External.__init__)


def test_gastm::external_constructor_args():
    sig = inspect.signature(gastm::External.__init__)
    params = list(sig.parameters.keys())



def test_gastm::boolean_is_not_abstract():
    assert not inspect.isabstract(gastm::Boolean)


def test_gastm::boolean_constructor_exists():
    assert callable(gastm::Boolean.__init__)


def test_gastm::boolean_constructor_args():
    sig = inspect.signature(gastm::Boolean.__init__)
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



def test_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
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



def test_gastm::bitxor_is_not_abstract():
    assert not inspect.isabstract(gastm::BitXor)


def test_gastm::bitxor_constructor_exists():
    assert callable(gastm::BitXor.__init__)


def test_gastm::bitxor_constructor_args():
    sig = inspect.signature(gastm::BitXor.__init__)
    params = list(sig.parameters.keys())



def test_gastm::less_is_not_abstract():
    assert not inspect.isabstract(gastm::Less)


def test_gastm::less_constructor_exists():
    assert callable(gastm::Less.__init__)


def test_gastm::less_constructor_args():
    sig = inspect.signature(gastm::Less.__init__)
    params = list(sig.parameters.keys())



def test_gastm::multiply_is_not_abstract():
    assert not inspect.isabstract(gastm::Multiply)


def test_gastm::multiply_constructor_exists():
    assert callable(gastm::Multiply.__init__)


def test_gastm::multiply_constructor_args():
    sig = inspect.signature(gastm::Multiply.__init__)
    params = list(sig.parameters.keys())



def test_gastm::add_is_not_abstract():
    assert not inspect.isabstract(gastm::Add)


def test_gastm::add_constructor_exists():
    assert callable(gastm::Add.__init__)


def test_gastm::add_constructor_args():
    sig = inspect.signature(gastm::Add.__init__)
    params = list(sig.parameters.keys())



def test_gastm::bitleftshift_is_not_abstract():
    assert not inspect.isabstract(gastm::BitLeftShift)


def test_gastm::bitleftshift_constructor_exists():
    assert callable(gastm::BitLeftShift.__init__)


def test_gastm::bitleftshift_constructor_args():
    sig = inspect.signature(gastm::BitLeftShift.__init__)
    params = list(sig.parameters.keys())



def test_gastm::assign_is_not_abstract():
    assert not inspect.isabstract(gastm::Assign)


def test_gastm::assign_constructor_exists():
    assert callable(gastm::Assign.__init__)


def test_gastm::assign_constructor_args():
    sig = inspect.signature(gastm::Assign.__init__)
    params = list(sig.parameters.keys())



def test_gastm::modulus_is_not_abstract():
    assert not inspect.isabstract(gastm::Modulus)


def test_gastm::modulus_constructor_exists():
    assert callable(gastm::Modulus.__init__)


def test_gastm::modulus_constructor_args():
    sig = inspect.signature(gastm::Modulus.__init__)
    params = list(sig.parameters.keys())



def test_gastm::greater_is_not_abstract():
    assert not inspect.isabstract(gastm::Greater)


def test_gastm::greater_constructor_exists():
    assert callable(gastm::Greater.__init__)


def test_gastm::greater_constructor_args():
    sig = inspect.signature(gastm::Greater.__init__)
    params = list(sig.parameters.keys())



def test_gastm::bitand_is_not_abstract():
    assert not inspect.isabstract(gastm::BitAnd)


def test_gastm::bitand_constructor_exists():
    assert callable(gastm::BitAnd.__init__)


def test_gastm::bitand_constructor_args():
    sig = inspect.signature(gastm::BitAnd.__init__)
    params = list(sig.parameters.keys())



def test_gastm::notless_is_not_abstract():
    assert not inspect.isabstract(gastm::NotLess)


def test_gastm::notless_constructor_exists():
    assert callable(gastm::NotLess.__init__)


def test_gastm::notless_constructor_args():
    sig = inspect.signature(gastm::NotLess.__init__)
    params = list(sig.parameters.keys())



def test_gastm::notequal_is_not_abstract():
    assert not inspect.isabstract(gastm::NotEqual)


def test_gastm::notequal_constructor_exists():
    assert callable(gastm::NotEqual.__init__)


def test_gastm::notequal_constructor_args():
    sig = inspect.signature(gastm::NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_gastm::divide_is_not_abstract():
    assert not inspect.isabstract(gastm::Divide)


def test_gastm::divide_constructor_exists():
    assert callable(gastm::Divide.__init__)


def test_gastm::divide_constructor_args():
    sig = inspect.signature(gastm::Divide.__init__)
    params = list(sig.parameters.keys())



def test_gastm::exponent_is_not_abstract():
    assert not inspect.isabstract(gastm::Exponent)


def test_gastm::exponent_constructor_exists():
    assert callable(gastm::Exponent.__init__)


def test_gastm::exponent_constructor_args():
    sig = inspect.signature(gastm::Exponent.__init__)
    params = list(sig.parameters.keys())



def test_gastm::notgreater_is_not_abstract():
    assert not inspect.isabstract(gastm::NotGreater)


def test_gastm::notgreater_constructor_exists():
    assert callable(gastm::NotGreater.__init__)


def test_gastm::notgreater_constructor_args():
    sig = inspect.signature(gastm::NotGreater.__init__)
    params = list(sig.parameters.keys())



def test_gastm::equal_is_not_abstract():
    assert not inspect.isabstract(gastm::Equal)


def test_gastm::equal_constructor_exists():
    assert callable(gastm::Equal.__init__)


def test_gastm::equal_constructor_args():
    sig = inspect.signature(gastm::Equal.__init__)
    params = list(sig.parameters.keys())



def test_gastm::and_is_not_abstract():
    assert not inspect.isabstract(gastm::And)


def test_gastm::and_constructor_exists():
    assert callable(gastm::And.__init__)


def test_gastm::and_constructor_args():
    sig = inspect.signature(gastm::And.__init__)
    params = list(sig.parameters.keys())



def test_gastm::bitor_is_not_abstract():
    assert not inspect.isabstract(gastm::BitOr)


def test_gastm::bitor_constructor_exists():
    assert callable(gastm::BitOr.__init__)


def test_gastm::bitor_constructor_args():
    sig = inspect.signature(gastm::BitOr.__init__)
    params = list(sig.parameters.keys())



def test_gastm::or_is_not_abstract():
    assert not inspect.isabstract(gastm::Or)


def test_gastm::or_constructor_exists():
    assert callable(gastm::Or.__init__)


def test_gastm::or_constructor_args():
    sig = inspect.signature(gastm::Or.__init__)
    params = list(sig.parameters.keys())



def test_gastm::operatorassign_is_not_abstract():
    assert not inspect.isabstract(gastm::OperatorAssign)


def test_gastm::operatorassign_constructor_exists():
    assert callable(gastm::OperatorAssign.__init__)


def test_gastm::operatorassign_constructor_args():
    sig = inspect.signature(gastm::OperatorAssign.__init__)
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



def test_gastm::qualifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(gastm::QualifiedIdentifierReference)


def test_gastm::qualifiedidentifierreference_constructor_exists():
    assert callable(gastm::QualifiedIdentifierReference.__init__)


def test_gastm::qualifiedidentifierreference_constructor_args():
    sig = inspect.signature(gastm::QualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_gastm::typequalifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(gastm::TypeQualifiedIdentifierReference)


def test_gastm::typequalifiedidentifierreference_constructor_exists():
    assert callable(gastm::TypeQualifiedIdentifierReference.__init__)


def test_gastm::typequalifiedidentifierreference_constructor_args():
    sig = inspect.signature(gastm::TypeQualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_identifierreference_is_not_abstract():
    assert not inspect.isabstract(IdentifierReference)


def test_identifierreference_constructor_exists():
    assert callable(IdentifierReference.__init__)


def test_identifierreference_constructor_args():
    sig = inspect.signature(IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_catchblock_is_not_abstract():
    assert not inspect.isabstract(CatchBlock)


def test_catchblock_constructor_exists():
    assert callable(CatchBlock.__init__)


def test_catchblock_constructor_args():
    sig = inspect.signature(CatchBlock.__init__)
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



def test_gastm::typescatchblock_is_not_abstract():
    assert not inspect.isabstract(gastm::TypesCatchBlock)


def test_gastm::typescatchblock_constructor_exists():
    assert callable(gastm::TypesCatchBlock.__init__)


def test_gastm::typescatchblock_constructor_args():
    sig = inspect.signature(gastm::TypesCatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_switchcase_is_not_abstract():
    assert not inspect.isabstract(SwitchCase)


def test_switchcase_constructor_exists():
    assert callable(SwitchCase.__init__)


def test_switchcase_constructor_args():
    sig = inspect.signature(SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_gastm::caseblock_is_not_abstract():
    assert not inspect.isabstract(gastm::CaseBlock)


def test_gastm::caseblock_constructor_exists():
    assert callable(gastm::CaseBlock.__init__)


def test_gastm::caseblock_constructor_args():
    sig = inspect.signature(gastm::CaseBlock.__init__)
    params = list(sig.parameters.keys())



def test_gastm::defaultblock_is_not_abstract():
    assert not inspect.isabstract(gastm::DefaultBlock)


def test_gastm::defaultblock_constructor_exists():
    assert callable(gastm::DefaultBlock.__init__)


def test_gastm::defaultblock_constructor_args():
    sig = inspect.signature(gastm::DefaultBlock.__init__)
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



def test_derivesfrom_is_not_abstract():
    assert not inspect.isabstract(DerivesFrom)


def test_derivesfrom_constructor_exists():
    assert callable(DerivesFrom.__init__)


def test_derivesfrom_constructor_args():
    sig = inspect.signature(DerivesFrom.__init__)
    params = list(sig.parameters.keys())



def test_labelaccess_is_not_abstract():
    assert not inspect.isabstract(LabelAccess)


def test_labelaccess_constructor_exists():
    assert callable(LabelAccess.__init__)


def test_labelaccess_constructor_args():
    sig = inspect.signature(LabelAccess.__init__)
    params = list(sig.parameters.keys())



def test_constructedtype_is_not_abstract():
    assert not inspect.isabstract(ConstructedType)


def test_constructedtype_constructor_exists():
    assert callable(ConstructedType.__init__)


def test_constructedtype_constructor_args():
    sig = inspect.signature(ConstructedType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::collectiontype_is_not_abstract():
    assert not inspect.isabstract(gastm::CollectionType)


def test_gastm::collectiontype_constructor_exists():
    assert callable(gastm::CollectionType.__init__)


def test_gastm::collectiontype_constructor_args():
    sig = inspect.signature(gastm::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::referencetype_is_not_abstract():
    assert not inspect.isabstract(gastm::ReferenceType)


def test_gastm::referencetype_constructor_exists():
    assert callable(gastm::ReferenceType.__init__)


def test_gastm::referencetype_constructor_args():
    sig = inspect.signature(gastm::ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::rangetype_is_not_abstract():
    assert not inspect.isabstract(gastm::RangeType)


def test_gastm::rangetype_constructor_exists():
    assert callable(gastm::RangeType.__init__)


def test_gastm::rangetype_constructor_args():
    sig = inspect.signature(gastm::RangeType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::pointertype_is_not_abstract():
    assert not inspect.isabstract(gastm::PointerType)


def test_gastm::pointertype_constructor_exists():
    assert callable(gastm::PointerType.__init__)


def test_gastm::pointertype_constructor_args():
    sig = inspect.signature(gastm::PointerType.__init__)
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



def test_gastm::constructedtype_is_not_abstract():
    assert not inspect.isabstract(gastm::ConstructedType)


def test_gastm::constructedtype_constructor_exists():
    assert callable(gastm::ConstructedType.__init__)


def test_gastm::constructedtype_constructor_args():
    sig = inspect.signature(gastm::ConstructedType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::enumtype_is_not_abstract():
    assert not inspect.isabstract(gastm::EnumType)


def test_gastm::enumtype_constructor_exists():
    assert callable(gastm::EnumType.__init__)


def test_gastm::enumtype_constructor_args():
    sig = inspect.signature(gastm::EnumType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::aggregatetype_is_not_abstract():
    assert not inspect.isabstract(gastm::AggregateType)


def test_gastm::aggregatetype_constructor_exists():
    assert callable(gastm::AggregateType.__init__)


def test_gastm::aggregatetype_constructor_args():
    sig = inspect.signature(gastm::AggregateType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::exceptiontype_is_not_abstract():
    assert not inspect.isabstract(gastm::ExceptionType)


def test_gastm::exceptiontype_constructor_exists():
    assert callable(gastm::ExceptionType.__init__)


def test_gastm::exceptiontype_constructor_args():
    sig = inspect.signature(gastm::ExceptionType.__init__)
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



def test_gastm::byreferenceformalparametertype_is_not_abstract():
    assert not inspect.isabstract(gastm::ByReferenceFormalParameterType)


def test_gastm::byreferenceformalparametertype_constructor_exists():
    assert callable(gastm::ByReferenceFormalParameterType.__init__)


def test_gastm::byreferenceformalparametertype_constructor_args():
    sig = inspect.signature(gastm::ByReferenceFormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::byvalueformalparametertype_is_not_abstract():
    assert not inspect.isabstract(gastm::ByValueFormalParameterType)


def test_gastm::byvalueformalparametertype_constructor_exists():
    assert callable(gastm::ByValueFormalParameterType.__init__)


def test_gastm::byvalueformalparametertype_constructor_args():
    sig = inspect.signature(gastm::ByValueFormalParameterType.__init__)
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



def test_gastm::typereference_is_not_abstract():
    assert not inspect.isabstract(gastm::TypeReference)


def test_gastm::typereference_constructor_exists():
    assert callable(gastm::TypeReference.__init__)


def test_gastm::typereference_constructor_args():
    sig = inspect.signature(gastm::TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_gastm::namespacetype_is_not_abstract():
    assert not inspect.isabstract(gastm::NameSpaceType)


def test_gastm::namespacetype_constructor_exists():
    assert callable(gastm::NameSpaceType.__init__)


def test_gastm::namespacetype_constructor_args():
    sig = inspect.signature(gastm::NameSpaceType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::functiontype_is_not_abstract():
    assert not inspect.isabstract(gastm::FunctionType)


def test_gastm::functiontype_constructor_exists():
    assert callable(gastm::FunctionType.__init__)


def test_gastm::functiontype_constructor_args():
    sig = inspect.signature(gastm::FunctionType.__init__)
    params = list(sig.parameters.keys())



def test_dimension_is_not_abstract():
    assert not inspect.isabstract(Dimension)


def test_dimension_constructor_exists():
    assert callable(Dimension.__init__)


def test_dimension_constructor_args():
    sig = inspect.signature(Dimension.__init__)
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



def test_gastm::classtype_is_not_abstract():
    assert not inspect.isabstract(gastm::ClassType)


def test_gastm::classtype_constructor_exists():
    assert callable(gastm::ClassType.__init__)


def test_gastm::classtype_constructor_args():
    sig = inspect.signature(gastm::ClassType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::uniontype_is_not_abstract():
    assert not inspect.isabstract(gastm::UnionType)


def test_gastm::uniontype_constructor_exists():
    assert callable(gastm::UnionType.__init__)


def test_gastm::uniontype_constructor_args():
    sig = inspect.signature(gastm::UnionType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::annotationtype_is_not_abstract():
    assert not inspect.isabstract(gastm::AnnotationType)


def test_gastm::annotationtype_constructor_exists():
    assert callable(gastm::AnnotationType.__init__)


def test_gastm::annotationtype_constructor_args():
    sig = inspect.signature(gastm::AnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_gastm::structuretype_is_not_abstract():
    assert not inspect.isabstract(gastm::StructureType)


def test_gastm::structuretype_constructor_exists():
    assert callable(gastm::StructureType.__init__)


def test_gastm::structuretype_constructor_args():
    sig = inspect.signature(gastm::StructureType.__init__)
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



def test_gastmsyntaxobject_is_not_abstract():
    assert not inspect.isabstract(GASTMSyntaxObject)


def test_gastmsyntaxobject_constructor_exists():
    assert callable(GASTMSyntaxObject.__init__)


def test_gastmsyntaxobject_constructor_args():
    sig = inspect.signature(GASTMSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_gastm::definitionobject_is_not_abstract():
    assert not inspect.isabstract(gastm::DefinitionObject)


def test_gastm::definitionobject_constructor_exists():
    assert callable(gastm::DefinitionObject.__init__)


def test_gastm::definitionobject_constructor_args():
    sig = inspect.signature(gastm::DefinitionObject.__init__)
    params = list(sig.parameters.keys())



def test_gastm::preprocessorelement_is_not_abstract():
    assert not inspect.isabstract(gastm::PreprocessorElement)


def test_gastm::preprocessorelement_constructor_exists():
    assert callable(gastm::PreprocessorElement.__init__)


def test_gastm::preprocessorelement_constructor_args():
    sig = inspect.signature(gastm::PreprocessorElement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::expression_is_not_abstract():
    assert not inspect.isabstract(gastm::Expression)


def test_gastm::expression_constructor_exists():
    assert callable(gastm::Expression.__init__)


def test_gastm::expression_constructor_args():
    sig = inspect.signature(gastm::Expression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::statement_is_not_abstract():
    assert not inspect.isabstract(gastm::Statement)


def test_gastm::statement_constructor_exists():
    assert callable(gastm::Statement.__init__)


def test_gastm::statement_constructor_args():
    sig = inspect.signature(gastm::Statement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::type_is_not_abstract():
    assert not inspect.isabstract(gastm::Type)


def test_gastm::type_constructor_exists():
    assert callable(gastm::Type.__init__)


def test_gastm::type_constructor_args():
    sig = inspect.signature(gastm::Type.__init__)
    params = list(sig.parameters.keys())
    assert "isVolatile" in params, "Missing parameter 'isVolatile'"
    assert "isConst" in params, "Missing parameter 'isConst'"

def test_gastm::type_has_isVolatile():
    assert hasattr(gastm::Type, "isVolatile")
    descriptor = None
    for klass in gastm::Type.__mro__:
        if "isVolatile" in klass.__dict__:
            descriptor = klass.__dict__["isVolatile"]
            break
    assert isinstance(descriptor, property)

def test_gastm::type_has_isConst():
    assert hasattr(gastm::Type, "isConst")
    descriptor = None
    for klass in gastm::Type.__mro__:
        if "isConst" in klass.__dict__:
            descriptor = klass.__dict__["isConst"]
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



def test_gastm::functionmemberattributes_is_not_abstract():
    assert not inspect.isabstract(gastm::FunctionMemberAttributes)


def test_gastm::functionmemberattributes_constructor_exists():
    assert callable(gastm::FunctionMemberAttributes.__init__)


def test_gastm::functionmemberattributes_constructor_args():
    sig = inspect.signature(gastm::FunctionMemberAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "isInline" in params, "Missing parameter 'isInline'"
    assert "isThisConst" in params, "Missing parameter 'isThisConst'"
    assert "isFriend" in params, "Missing parameter 'isFriend'"

def test_gastm::functionmemberattributes_has_isInline():
    assert hasattr(gastm::FunctionMemberAttributes, "isInline")
    descriptor = None
    for klass in gastm::FunctionMemberAttributes.__mro__:
        if "isInline" in klass.__dict__:
            descriptor = klass.__dict__["isInline"]
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

def test_gastm::functionmemberattributes_has_isFriend():
    assert hasattr(gastm::FunctionMemberAttributes, "isFriend")
    descriptor = None
    for klass in gastm::FunctionMemberAttributes.__mro__:
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



def test_gastm::emptystatement_is_not_abstract():
    assert not inspect.isabstract(gastm::EmptyStatement)


def test_gastm::emptystatement_constructor_exists():
    assert callable(gastm::EmptyStatement.__init__)


def test_gastm::emptystatement_constructor_args():
    sig = inspect.signature(gastm::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::continuestatement_is_not_abstract():
    assert not inspect.isabstract(gastm::ContinueStatement)


def test_gastm::continuestatement_constructor_exists():
    assert callable(gastm::ContinueStatement.__init__)


def test_gastm::continuestatement_constructor_args():
    sig = inspect.signature(gastm::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::ExpressionStatement)


def test_gastm::expressionstatement_constructor_exists():
    assert callable(gastm::ExpressionStatement.__init__)


def test_gastm::expressionstatement_constructor_args():
    sig = inspect.signature(gastm::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::returnstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::ReturnStatement)


def test_gastm::returnstatement_constructor_exists():
    assert callable(gastm::ReturnStatement.__init__)


def test_gastm::returnstatement_constructor_args():
    sig = inspect.signature(gastm::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::blockstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::BlockStatement)


def test_gastm::blockstatement_constructor_exists():
    assert callable(gastm::BlockStatement.__init__)


def test_gastm::blockstatement_constructor_args():
    sig = inspect.signature(gastm::BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::declarationordefinitionstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::DeclarationOrDefinitionStatement)


def test_gastm::declarationordefinitionstatement_constructor_exists():
    assert callable(gastm::DeclarationOrDefinitionStatement.__init__)


def test_gastm::declarationordefinitionstatement_constructor_args():
    sig = inspect.signature(gastm::DeclarationOrDefinitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::labeledstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::LabeledStatement)


def test_gastm::labeledstatement_constructor_exists():
    assert callable(gastm::LabeledStatement.__init__)


def test_gastm::labeledstatement_constructor_args():
    sig = inspect.signature(gastm::LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::deletestatement_is_not_abstract():
    assert not inspect.isabstract(gastm::DeleteStatement)


def test_gastm::deletestatement_constructor_exists():
    assert callable(gastm::DeleteStatement.__init__)


def test_gastm::deletestatement_constructor_args():
    sig = inspect.signature(gastm::DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::trystatement_is_not_abstract():
    assert not inspect.isabstract(gastm::TryStatement)


def test_gastm::trystatement_constructor_exists():
    assert callable(gastm::TryStatement.__init__)


def test_gastm::trystatement_constructor_args():
    sig = inspect.signature(gastm::TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::switchstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::SwitchStatement)


def test_gastm::switchstatement_constructor_exists():
    assert callable(gastm::SwitchStatement.__init__)


def test_gastm::switchstatement_constructor_args():
    sig = inspect.signature(gastm::SwitchStatement.__init__)
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



def test_gastm::breakstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::BreakStatement)


def test_gastm::breakstatement_constructor_exists():
    assert callable(gastm::BreakStatement.__init__)


def test_gastm::breakstatement_constructor_args():
    sig = inspect.signature(gastm::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::throwstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::ThrowStatement)


def test_gastm::throwstatement_constructor_exists():
    assert callable(gastm::ThrowStatement.__init__)


def test_gastm::throwstatement_constructor_args():
    sig = inspect.signature(gastm::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::loopstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::LoopStatement)


def test_gastm::loopstatement_constructor_exists():
    assert callable(gastm::LoopStatement.__init__)


def test_gastm::loopstatement_constructor_args():
    sig = inspect.signature(gastm::LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm::jumpstatement_is_not_abstract():
    assert not inspect.isabstract(gastm::JumpStatement)


def test_gastm::jumpstatement_constructor_exists():
    assert callable(gastm::JumpStatement.__init__)


def test_gastm::jumpstatement_constructor_args():
    sig = inspect.signature(gastm::JumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_formalparameterdefinition_is_not_abstract():
    assert not inspect.isabstract(FormalParameterDefinition)


def test_formalparameterdefinition_constructor_exists():
    assert callable(FormalParameterDefinition.__init__)


def test_formalparameterdefinition_constructor_args():
    sig = inspect.signature(FormalParameterDefinition.__init__)
    params = list(sig.parameters.keys())



def test_datadefinition_is_not_abstract():
    assert not inspect.isabstract(DataDefinition)


def test_datadefinition_constructor_exists():
    assert callable(DataDefinition.__init__)


def test_datadefinition_constructor_args():
    sig = inspect.signature(DataDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm::formalparameterdefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::FormalParameterDefinition)


def test_gastm::formalparameterdefinition_constructor_exists():
    assert callable(gastm::FormalParameterDefinition.__init__)


def test_gastm::formalparameterdefinition_constructor_args():
    sig = inspect.signature(gastm::FormalParameterDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm::variabledefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::VariableDefinition)


def test_gastm::variabledefinition_constructor_exists():
    assert callable(gastm::VariableDefinition.__init__)


def test_gastm::variabledefinition_constructor_args():
    sig = inspect.signature(gastm::VariableDefinition.__init__)
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



def test_gastm::aggregateexpression_is_not_abstract():
    assert not inspect.isabstract(gastm::AggregateExpression)


def test_gastm::aggregateexpression_constructor_exists():
    assert callable(gastm::AggregateExpression.__init__)


def test_gastm::aggregateexpression_constructor_args():
    sig = inspect.signature(gastm::AggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::labelaccess_is_not_abstract():
    assert not inspect.isabstract(gastm::LabelAccess)


def test_gastm::labelaccess_constructor_exists():
    assert callable(gastm::LabelAccess.__init__)


def test_gastm::labelaccess_constructor_args():
    sig = inspect.signature(gastm::LabelAccess.__init__)
    params = list(sig.parameters.keys())



def test_gastm::arrayaccess_is_not_abstract():
    assert not inspect.isabstract(gastm::ArrayAccess)


def test_gastm::arrayaccess_constructor_exists():
    assert callable(gastm::ArrayAccess.__init__)


def test_gastm::arrayaccess_constructor_args():
    sig = inspect.signature(gastm::ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_gastm::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(gastm::BinaryExpression)


def test_gastm::binaryexpression_constructor_exists():
    assert callable(gastm::BinaryExpression.__init__)


def test_gastm::binaryexpression_constructor_args():
    sig = inspect.signature(gastm::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::castexpression_is_not_abstract():
    assert not inspect.isabstract(gastm::CastExpression)


def test_gastm::castexpression_constructor_exists():
    assert callable(gastm::CastExpression.__init__)


def test_gastm::castexpression_constructor_args():
    sig = inspect.signature(gastm::CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::functioncallexpression_is_not_abstract():
    assert not inspect.isabstract(gastm::FunctionCallExpression)


def test_gastm::functioncallexpression_constructor_exists():
    assert callable(gastm::FunctionCallExpression.__init__)


def test_gastm::functioncallexpression_constructor_args():
    sig = inspect.signature(gastm::FunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::rangeexpression_is_not_abstract():
    assert not inspect.isabstract(gastm::RangeExpression)


def test_gastm::rangeexpression_constructor_exists():
    assert callable(gastm::RangeExpression.__init__)


def test_gastm::rangeexpression_constructor_args():
    sig = inspect.signature(gastm::RangeExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(gastm::ConditionalExpression)


def test_gastm::conditionalexpression_constructor_exists():
    assert callable(gastm::ConditionalExpression.__init__)


def test_gastm::conditionalexpression_constructor_args():
    sig = inspect.signature(gastm::ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::newexpression_is_not_abstract():
    assert not inspect.isabstract(gastm::NewExpression)


def test_gastm::newexpression_constructor_exists():
    assert callable(gastm::NewExpression.__init__)


def test_gastm::newexpression_constructor_args():
    sig = inspect.signature(gastm::NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::annotationexpression_is_not_abstract():
    assert not inspect.isabstract(gastm::AnnotationExpression)


def test_gastm::annotationexpression_constructor_exists():
    assert callable(gastm::AnnotationExpression.__init__)


def test_gastm::annotationexpression_constructor_args():
    sig = inspect.signature(gastm::AnnotationExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(gastm::UnaryExpression)


def test_gastm::unaryexpression_constructor_exists():
    assert callable(gastm::UnaryExpression.__init__)


def test_gastm::unaryexpression_constructor_args():
    sig = inspect.signature(gastm::UnaryExpression.__init__)
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



def test_gastm::namereference_is_not_abstract():
    assert not inspect.isabstract(gastm::NameReference)


def test_gastm::namereference_constructor_exists():
    assert callable(gastm::NameReference.__init__)


def test_gastm::namereference_constructor_args():
    sig = inspect.signature(gastm::NameReference.__init__)
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



def test_gastm::entrydefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::EntryDefinition)


def test_gastm::entrydefinition_constructor_exists():
    assert callable(gastm::EntryDefinition.__init__)


def test_gastm::entrydefinition_constructor_args():
    sig = inspect.signature(gastm::EntryDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm::functiondefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::FunctionDefinition)


def test_gastm::functiondefinition_constructor_exists():
    assert callable(gastm::FunctionDefinition.__init__)


def test_gastm::functiondefinition_constructor_args():
    sig = inspect.signature(gastm::FunctionDefinition.__init__)
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



def test_functionmemberattributes_is_not_abstract():
    assert not inspect.isabstract(FunctionMemberAttributes)


def test_functionmemberattributes_constructor_exists():
    assert callable(FunctionMemberAttributes.__init__)


def test_functionmemberattributes_constructor_args():
    sig = inspect.signature(FunctionMemberAttributes.__init__)
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



def test_gastm::blockscope_is_not_abstract():
    assert not inspect.isabstract(gastm::BlockScope)


def test_gastm::blockscope_constructor_exists():
    assert callable(gastm::BlockScope.__init__)


def test_gastm::blockscope_constructor_args():
    sig = inspect.signature(gastm::BlockScope.__init__)
    params = list(sig.parameters.keys())



def test_gastm::programscope_is_not_abstract():
    assert not inspect.isabstract(gastm::ProgramScope)


def test_gastm::programscope_constructor_exists():
    assert callable(gastm::ProgramScope.__init__)


def test_gastm::programscope_constructor_args():
    sig = inspect.signature(gastm::ProgramScope.__init__)
    params = list(sig.parameters.keys())



def test_gastm::aggregatescope_is_not_abstract():
    assert not inspect.isabstract(gastm::AggregateScope)


def test_gastm::aggregatescope_constructor_exists():
    assert callable(gastm::AggregateScope.__init__)


def test_gastm::aggregatescope_constructor_args():
    sig = inspect.signature(gastm::AggregateScope.__init__)
    params = list(sig.parameters.keys())



def test_gastm::globalscope_is_not_abstract():
    assert not inspect.isabstract(gastm::GlobalScope)


def test_gastm::globalscope_constructor_exists():
    assert callable(gastm::GlobalScope.__init__)


def test_gastm::globalscope_constructor_args():
    sig = inspect.signature(gastm::GlobalScope.__init__)
    params = list(sig.parameters.keys())



def test_gastm::functionscope_is_not_abstract():
    assert not inspect.isabstract(gastm::FunctionScope)


def test_gastm::functionscope_constructor_exists():
    assert callable(gastm::FunctionScope.__init__)


def test_gastm::functionscope_constructor_args():
    sig = inspect.signature(gastm::FunctionScope.__init__)
    params = list(sig.parameters.keys())



def test_definitionobject_is_not_abstract():
    assert not inspect.isabstract(DefinitionObject)


def test_definitionobject_constructor_exists():
    assert callable(DefinitionObject.__init__)


def test_definitionobject_constructor_args():
    sig = inspect.signature(DefinitionObject.__init__)
    params = list(sig.parameters.keys())



def test_gastm::labeldefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::LabelDefinition)


def test_gastm::labeldefinition_constructor_exists():
    assert callable(gastm::LabelDefinition.__init__)


def test_gastm::labeldefinition_constructor_args():
    sig = inspect.signature(gastm::LabelDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm::namespacedefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::NameSpaceDefinition)


def test_gastm::namespacedefinition_constructor_exists():
    assert callable(gastm::NameSpaceDefinition.__init__)


def test_gastm::namespacedefinition_constructor_args():
    sig = inspect.signature(gastm::NameSpaceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm::typedefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::TypeDefinition)


def test_gastm::typedefinition_constructor_exists():
    assert callable(gastm::TypeDefinition.__init__)


def test_gastm::typedefinition_constructor_args():
    sig = inspect.signature(gastm::TypeDefinition.__init__)
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



def test_gastm::dimension_is_not_abstract():
    assert not inspect.isabstract(gastm::Dimension)


def test_gastm::dimension_constructor_exists():
    assert callable(gastm::Dimension.__init__)


def test_gastm::dimension_constructor_args():
    sig = inspect.signature(gastm::Dimension.__init__)
    params = list(sig.parameters.keys())



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



def test_gastm::virtualspecification_is_not_abstract():
    assert not inspect.isabstract(gastm::VirtualSpecification)


def test_gastm::virtualspecification_constructor_exists():
    assert callable(gastm::VirtualSpecification.__init__)


def test_gastm::virtualspecification_constructor_args():
    sig = inspect.signature(gastm::VirtualSpecification.__init__)
    params = list(sig.parameters.keys())



def test_gastm::switchcase_is_not_abstract():
    assert not inspect.isabstract(gastm::SwitchCase)


def test_gastm::switchcase_constructor_exists():
    assert callable(gastm::SwitchCase.__init__)


def test_gastm::switchcase_constructor_args():
    sig = inspect.signature(gastm::SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_gastm::functionmemberattribute_is_not_abstract():
    assert not inspect.isabstract(gastm::FunctionMemberAttribute)


def test_gastm::functionmemberattribute_constructor_exists():
    assert callable(gastm::FunctionMemberAttribute.__init__)


def test_gastm::functionmemberattribute_constructor_args():
    sig = inspect.signature(gastm::FunctionMemberAttribute.__init__)
    params = list(sig.parameters.keys())



def test_gastm::catchblock_is_not_abstract():
    assert not inspect.isabstract(gastm::CatchBlock)


def test_gastm::catchblock_constructor_exists():
    assert callable(gastm::CatchBlock.__init__)


def test_gastm::catchblock_constructor_args():
    sig = inspect.signature(gastm::CatchBlock.__init__)
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



def test_gastm::macrodefinition_is_not_abstract():
    assert not inspect.isabstract(gastm::MacroDefinition)


def test_gastm::macrodefinition_constructor_exists():
    assert callable(gastm::MacroDefinition.__init__)


def test_gastm::macrodefinition_constructor_args():
    sig = inspect.signature(gastm::MacroDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "macroName" in params, "Missing parameter 'macroName'"
    assert "body" in params, "Missing parameter 'body'"

def test_gastm::macrodefinition_has_macroName():
    assert hasattr(gastm::MacroDefinition, "macroName")
    descriptor = None
    for klass in gastm::MacroDefinition.__mro__:
        if "macroName" in klass.__dict__:
            descriptor = klass.__dict__["macroName"]
            break
    assert isinstance(descriptor, property)

def test_gastm::macrodefinition_has_body():
    assert hasattr(gastm::MacroDefinition, "body")
    descriptor = None
    for klass in gastm::MacroDefinition.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



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
    assert "endLine" in params, "Missing parameter 'endLine'"
    assert "startLine" in params, "Missing parameter 'startLine'"
    assert "endColumn" in params, "Missing parameter 'endColumn'"
    assert "startColumn" in params, "Missing parameter 'startColumn'"

def test_gastm::sourcelocation_has_endLine():
    assert hasattr(gastm::SourceLocation, "endLine")
    descriptor = None
    for klass in gastm::SourceLocation.__mro__:
        if "endLine" in klass.__dict__:
            descriptor = klass.__dict__["endLine"]
            break
    assert isinstance(descriptor, property)

def test_gastm::sourcelocation_has_startLine():
    assert hasattr(gastm::SourceLocation, "startLine")
    descriptor = None
    for klass in gastm::SourceLocation.__mro__:
        if "startLine" in klass.__dict__:
            descriptor = klass.__dict__["startLine"]
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

def test_gastm::sourcelocation_has_startColumn():
    assert hasattr(gastm::SourceLocation, "startColumn")
    descriptor = None
    for klass in gastm::SourceLocation.__mro__:
        if "startColumn" in klass.__dict__:
            descriptor = klass.__dict__["startColumn"]
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
gastm::ByReferenceActualParameterExpression_strategy = st.builds(
    gastm::ByReferenceActualParameterExpression,
)
gastm::ByValueActualParameterExpression_strategy = st.builds(
    gastm::ByValueActualParameterExpression,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
gastm::AddressOf_strategy = st.builds(
    gastm::AddressOf,
)
gastm::Negate_strategy = st.builds(
    gastm::Negate,
)
gastm::PostIncrement_strategy = st.builds(
    gastm::PostIncrement,
)
gastm::Not_strategy = st.builds(
    gastm::Not,
)
gastm::BitNot_strategy = st.builds(
    gastm::BitNot,
)
gastm::Deref_strategy = st.builds(
    gastm::Deref,
)
gastm::Decrement_strategy = st.builds(
    gastm::Decrement,
)
gastm::Increment_strategy = st.builds(
    gastm::Increment,
)
gastm::PostDecrement_strategy = st.builds(
    gastm::PostDecrement,
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
gastm::BitLiteral_strategy = st.builds(
    gastm::BitLiteral,
)
gastm::RealLiteral_strategy = st.builds(
    gastm::RealLiteral,
)
gastm::BooleanLiteral_strategy = st.builds(
    gastm::BooleanLiteral,
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
gastm::StringLiteral_strategy = st.builds(
    gastm::StringLiteral,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
gastm::Byte_strategy = st.builds(
    gastm::Byte,
)
gastm::Character_strategy = st.builds(
    gastm::Character,
)
gastm::Double_strategy = st.builds(
    gastm::Double,
)
gastm::LongInteger_strategy = st.builds(
    gastm::LongInteger,
)
gastm::ShortInteger_strategy = st.builds(
    gastm::ShortInteger,
)
gastm::String_strategy = st.builds(
    gastm::String,
)
gastm::WideCharacter_strategy = st.builds(
    gastm::WideCharacter,
)
gastm::LongDouble_strategy = st.builds(
    gastm::LongDouble,
)
gastm::Float_strategy = st.builds(
    gastm::Float,
)
gastm::Integer_strategy = st.builds(
    gastm::Integer,
)
gastm::Void_strategy = st.builds(
    gastm::Void,
)
StorageSpecification_strategy = st.builds(
    StorageSpecification,
)
gastm::FunctionPersistent_strategy = st.builds(
    gastm::FunctionPersistent,
)
gastm::PerClassMember_strategy = st.builds(
    gastm::PerClassMember,
)
gastm::NoDef_strategy = st.builds(
    gastm::NoDef,
)
gastm::FileLocal_strategy = st.builds(
    gastm::FileLocal,
)
gastm::External_strategy = st.builds(
    gastm::External,
)
gastm::Boolean_strategy = st.builds(
    gastm::Boolean,
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
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
gastm::BitRightShift_strategy = st.builds(
    gastm::BitRightShift,
)
gastm::Subtract_strategy = st.builds(
    gastm::Subtract,
)
gastm::BitXor_strategy = st.builds(
    gastm::BitXor,
)
gastm::Less_strategy = st.builds(
    gastm::Less,
)
gastm::Multiply_strategy = st.builds(
    gastm::Multiply,
)
gastm::Add_strategy = st.builds(
    gastm::Add,
)
gastm::BitLeftShift_strategy = st.builds(
    gastm::BitLeftShift,
)
gastm::Assign_strategy = st.builds(
    gastm::Assign,
)
gastm::Modulus_strategy = st.builds(
    gastm::Modulus,
)
gastm::Greater_strategy = st.builds(
    gastm::Greater,
)
gastm::BitAnd_strategy = st.builds(
    gastm::BitAnd,
)
gastm::NotLess_strategy = st.builds(
    gastm::NotLess,
)
gastm::NotEqual_strategy = st.builds(
    gastm::NotEqual,
)
gastm::Divide_strategy = st.builds(
    gastm::Divide,
)
gastm::Exponent_strategy = st.builds(
    gastm::Exponent,
)
gastm::NotGreater_strategy = st.builds(
    gastm::NotGreater,
)
gastm::Equal_strategy = st.builds(
    gastm::Equal,
)
gastm::And_strategy = st.builds(
    gastm::And,
)
gastm::BitOr_strategy = st.builds(
    gastm::BitOr,
)
gastm::Or_strategy = st.builds(
    gastm::Or,
)
gastm::OperatorAssign_strategy = st.builds(
    gastm::OperatorAssign,
)
NameReference_strategy = st.builds(
    NameReference,
)
gastm::IdentifierReference_strategy = st.builds(
    gastm::IdentifierReference,
)
gastm::QualifiedIdentifierReference_strategy = st.builds(
    gastm::QualifiedIdentifierReference,
)
gastm::TypeQualifiedIdentifierReference_strategy = st.builds(
    gastm::TypeQualifiedIdentifierReference,
)
IdentifierReference_strategy = st.builds(
    IdentifierReference,
)
CatchBlock_strategy = st.builds(
    CatchBlock,
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
gastm::TypesCatchBlock_strategy = st.builds(
    gastm::TypesCatchBlock,
)
SwitchCase_strategy = st.builds(
    SwitchCase,
)
gastm::CaseBlock_strategy = st.builds(
    gastm::CaseBlock,
)
gastm::DefaultBlock_strategy = st.builds(
    gastm::DefaultBlock,
)
BlockScope_strategy = st.builds(
    BlockScope,
)
LabelDefinition_strategy = st.builds(
    LabelDefinition,
)
DerivesFrom_strategy = st.builds(
    DerivesFrom,
)
LabelAccess_strategy = st.builds(
    LabelAccess,
)
ConstructedType_strategy = st.builds(
    ConstructedType,
)
gastm::CollectionType_strategy = st.builds(
    gastm::CollectionType,
)
gastm::ReferenceType_strategy = st.builds(
    gastm::ReferenceType,
)
gastm::RangeType_strategy = st.builds(
    gastm::RangeType,
)
gastm::PointerType_strategy = st.builds(
    gastm::PointerType,
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
gastm::ConstructedType_strategy = st.builds(
    gastm::ConstructedType,
)
gastm::EnumType_strategy = st.builds(
    gastm::EnumType,
)
gastm::AggregateType_strategy = st.builds(
    gastm::AggregateType,
)
gastm::ExceptionType_strategy = st.builds(
    gastm::ExceptionType,
)
gastm::PrimitiveType_strategy = st.builds(
    gastm::PrimitiveType,
    isSigned=
        st.booleans()
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
gastm::ByReferenceFormalParameterType_strategy = st.builds(
    gastm::ByReferenceFormalParameterType,
)
gastm::ByValueFormalParameterType_strategy = st.builds(
    gastm::ByValueFormalParameterType,
)
Type_strategy = st.builds(
    Type,
)
gastm::LabelType_strategy = st.builds(
    gastm::LabelType,
)
gastm::TypeReference_strategy = st.builds(
    gastm::TypeReference,
)
gastm::NameSpaceType_strategy = st.builds(
    gastm::NameSpaceType,
)
gastm::FunctionType_strategy = st.builds(
    gastm::FunctionType,
)
Dimension_strategy = st.builds(
    Dimension,
)
NameSpaceType_strategy = st.builds(
    NameSpaceType,
)
AggregateType_strategy = st.builds(
    AggregateType,
)
gastm::ClassType_strategy = st.builds(
    gastm::ClassType,
)
gastm::UnionType_strategy = st.builds(
    gastm::UnionType,
)
gastm::AnnotationType_strategy = st.builds(
    gastm::AnnotationType,
)
gastm::StructureType_strategy = st.builds(
    gastm::StructureType,
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
GASTMSyntaxObject_strategy = st.builds(
    GASTMSyntaxObject,
)
gastm::DefinitionObject_strategy = st.builds(
    gastm::DefinitionObject,
)
gastm::PreprocessorElement_strategy = st.builds(
    gastm::PreprocessorElement,
)
gastm::Expression_strategy = st.builds(
    gastm::Expression,
)
gastm::Statement_strategy = st.builds(
    gastm::Statement,
)
gastm::Type_strategy = st.builds(
    gastm::Type,
    isVolatile=
        st.booleans(),
    isConst=
        st.booleans()
)
MacroDefinition_strategy = st.builds(
    MacroDefinition,
)
LabelType_strategy = st.builds(
    LabelType,
)
gastm::FunctionMemberAttributes_strategy = st.builds(
    gastm::FunctionMemberAttributes,
    isInline=
        st.booleans(),
    isThisConst=
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
gastm::EmptyStatement_strategy = st.builds(
    gastm::EmptyStatement,
)
gastm::ContinueStatement_strategy = st.builds(
    gastm::ContinueStatement,
)
gastm::ExpressionStatement_strategy = st.builds(
    gastm::ExpressionStatement,
)
gastm::ReturnStatement_strategy = st.builds(
    gastm::ReturnStatement,
)
gastm::BlockStatement_strategy = st.builds(
    gastm::BlockStatement,
)
gastm::DeclarationOrDefinitionStatement_strategy = st.builds(
    gastm::DeclarationOrDefinitionStatement,
)
gastm::LabeledStatement_strategy = st.builds(
    gastm::LabeledStatement,
)
gastm::DeleteStatement_strategy = st.builds(
    gastm::DeleteStatement,
)
gastm::TryStatement_strategy = st.builds(
    gastm::TryStatement,
)
gastm::SwitchStatement_strategy = st.builds(
    gastm::SwitchStatement,
)
gastm::IfStatement_strategy = st.builds(
    gastm::IfStatement,
)
gastm::TerminateStatement_strategy = st.builds(
    gastm::TerminateStatement,
)
gastm::BreakStatement_strategy = st.builds(
    gastm::BreakStatement,
)
gastm::ThrowStatement_strategy = st.builds(
    gastm::ThrowStatement,
)
gastm::LoopStatement_strategy = st.builds(
    gastm::LoopStatement,
)
gastm::JumpStatement_strategy = st.builds(
    gastm::JumpStatement,
)
FormalParameterDefinition_strategy = st.builds(
    FormalParameterDefinition,
)
DataDefinition_strategy = st.builds(
    DataDefinition,
)
gastm::FormalParameterDefinition_strategy = st.builds(
    gastm::FormalParameterDefinition,
)
gastm::VariableDefinition_strategy = st.builds(
    gastm::VariableDefinition,
)
gastm::BitFieldDefinition_strategy = st.builds(
    gastm::BitFieldDefinition,
)
Expression_strategy = st.builds(
    Expression,
)
gastm::AggregateExpression_strategy = st.builds(
    gastm::AggregateExpression,
)
gastm::LabelAccess_strategy = st.builds(
    gastm::LabelAccess,
)
gastm::ArrayAccess_strategy = st.builds(
    gastm::ArrayAccess,
)
gastm::BinaryExpression_strategy = st.builds(
    gastm::BinaryExpression,
)
gastm::CastExpression_strategy = st.builds(
    gastm::CastExpression,
)
gastm::FunctionCallExpression_strategy = st.builds(
    gastm::FunctionCallExpression,
)
gastm::RangeExpression_strategy = st.builds(
    gastm::RangeExpression,
)
gastm::ConditionalExpression_strategy = st.builds(
    gastm::ConditionalExpression,
)
gastm::NewExpression_strategy = st.builds(
    gastm::NewExpression,
)
gastm::AnnotationExpression_strategy = st.builds(
    gastm::AnnotationExpression,
)
gastm::UnaryExpression_strategy = st.builds(
    gastm::UnaryExpression,
)
gastm::Literal_strategy = st.builds(
    gastm::Literal,
    value=
        safe_text
)
gastm::NameReference_strategy = st.builds(
    gastm::NameReference,
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
gastm::EntryDefinition_strategy = st.builds(
    gastm::EntryDefinition,
)
gastm::FunctionDefinition_strategy = st.builds(
    gastm::FunctionDefinition,
)
gastm::DataDefinition_strategy = st.builds(
    gastm::DataDefinition,
    isMutable=
        st.booleans()
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
gastm::VariableDeclaration_strategy = st.builds(
    gastm::VariableDeclaration,
    isMutable=
        st.booleans()
)
FunctionMemberAttributes_strategy = st.builds(
    FunctionMemberAttributes,
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
gastm::BlockScope_strategy = st.builds(
    gastm::BlockScope,
)
gastm::ProgramScope_strategy = st.builds(
    gastm::ProgramScope,
)
gastm::AggregateScope_strategy = st.builds(
    gastm::AggregateScope,
)
gastm::GlobalScope_strategy = st.builds(
    gastm::GlobalScope,
)
gastm::FunctionScope_strategy = st.builds(
    gastm::FunctionScope,
)
DefinitionObject_strategy = st.builds(
    DefinitionObject,
)
gastm::LabelDefinition_strategy = st.builds(
    gastm::LabelDefinition,
)
gastm::NameSpaceDefinition_strategy = st.builds(
    gastm::NameSpaceDefinition,
)
gastm::TypeDefinition_strategy = st.builds(
    gastm::TypeDefinition,
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
gastm::Scope_strategy = st.builds(
    gastm::Scope,
)
gastm::Project_strategy = st.builds(
    gastm::Project,
)
SourceFile_strategy = st.builds(
    SourceFile,
)
gastm::DeclarationOrDefinition_strategy = st.builds(
    gastm::DeclarationOrDefinition,
    isRegister=
        st.booleans(),
    linkageSpecifier=
        safe_text
)
ProgramScope_strategy = st.builds(
    ProgramScope,
)
OtherSyntaxObject_strategy = st.builds(
    OtherSyntaxObject,
)
gastm::Name_strategy = st.builds(
    gastm::Name,
    nameString=
        safe_text
)
gastm::Dimension_strategy = st.builds(
    gastm::Dimension,
)
gastm::DerivesFrom_strategy = st.builds(
    gastm::DerivesFrom,
    isVirtual=
        st.booleans()
)
gastm::VirtualSpecification_strategy = st.builds(
    gastm::VirtualSpecification,
)
gastm::SwitchCase_strategy = st.builds(
    gastm::SwitchCase,
)
gastm::FunctionMemberAttribute_strategy = st.builds(
    gastm::FunctionMemberAttribute,
)
gastm::CatchBlock_strategy = st.builds(
    gastm::CatchBlock,
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
gastm::MacroDefinition_strategy = st.builds(
    gastm::MacroDefinition,
    macroName=
        safe_text,
    body=
        safe_text
)
gastm::MacroCall_strategy = st.builds(
    gastm::MacroCall,
)
gastm::IncludeUnit_strategy = st.builds(
    gastm::IncludeUnit,
)
gastm::Comment_strategy = st.builds(
    gastm::Comment,
    text=
        safe_text
)
GASTMSourceObject_strategy = st.builds(
    GASTMSourceObject,
)
gastm::SourceLocation_strategy = st.builds(
    gastm::SourceLocation,
    endLine=
        st.integers(),
    startLine=
        st.integers(),
    endColumn=
        st.integers(),
    startColumn=
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

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=gastm::AddressOf_strategy)
@settings(max_examples=50)
def test_gastm::addressof_instantiation(instance):
    assert isinstance(instance, gastm::AddressOf)

@given(instance=gastm::Negate_strategy)
@settings(max_examples=50)
def test_gastm::negate_instantiation(instance):
    assert isinstance(instance, gastm::Negate)

@given(instance=gastm::PostIncrement_strategy)
@settings(max_examples=50)
def test_gastm::postincrement_instantiation(instance):
    assert isinstance(instance, gastm::PostIncrement)

@given(instance=gastm::Not_strategy)
@settings(max_examples=50)
def test_gastm::not_instantiation(instance):
    assert isinstance(instance, gastm::Not)

@given(instance=gastm::BitNot_strategy)
@settings(max_examples=50)
def test_gastm::bitnot_instantiation(instance):
    assert isinstance(instance, gastm::BitNot)

@given(instance=gastm::Deref_strategy)
@settings(max_examples=50)
def test_gastm::deref_instantiation(instance):
    assert isinstance(instance, gastm::Deref)

@given(instance=gastm::Decrement_strategy)
@settings(max_examples=50)
def test_gastm::decrement_instantiation(instance):
    assert isinstance(instance, gastm::Decrement)

@given(instance=gastm::Increment_strategy)
@settings(max_examples=50)
def test_gastm::increment_instantiation(instance):
    assert isinstance(instance, gastm::Increment)

@given(instance=gastm::PostDecrement_strategy)
@settings(max_examples=50)
def test_gastm::postdecrement_instantiation(instance):
    assert isinstance(instance, gastm::PostDecrement)

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

@given(instance=gastm::BitLiteral_strategy)
@settings(max_examples=50)
def test_gastm::bitliteral_instantiation(instance):
    assert isinstance(instance, gastm::BitLiteral)

@given(instance=gastm::RealLiteral_strategy)
@settings(max_examples=50)
def test_gastm::realliteral_instantiation(instance):
    assert isinstance(instance, gastm::RealLiteral)

@given(instance=gastm::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_gastm::booleanliteral_instantiation(instance):
    assert isinstance(instance, gastm::BooleanLiteral)

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

@given(instance=gastm::StringLiteral_strategy)
@settings(max_examples=50)
def test_gastm::stringliteral_instantiation(instance):
    assert isinstance(instance, gastm::StringLiteral)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=gastm::Byte_strategy)
@settings(max_examples=50)
def test_gastm::byte_instantiation(instance):
    assert isinstance(instance, gastm::Byte)

@given(instance=gastm::Character_strategy)
@settings(max_examples=50)
def test_gastm::character_instantiation(instance):
    assert isinstance(instance, gastm::Character)

@given(instance=gastm::Double_strategy)
@settings(max_examples=50)
def test_gastm::double_instantiation(instance):
    assert isinstance(instance, gastm::Double)

@given(instance=gastm::LongInteger_strategy)
@settings(max_examples=50)
def test_gastm::longinteger_instantiation(instance):
    assert isinstance(instance, gastm::LongInteger)

@given(instance=gastm::ShortInteger_strategy)
@settings(max_examples=50)
def test_gastm::shortinteger_instantiation(instance):
    assert isinstance(instance, gastm::ShortInteger)

@given(instance=gastm::String_strategy)
@settings(max_examples=50)
def test_gastm::string_instantiation(instance):
    assert isinstance(instance, gastm::String)

@given(instance=gastm::WideCharacter_strategy)
@settings(max_examples=50)
def test_gastm::widecharacter_instantiation(instance):
    assert isinstance(instance, gastm::WideCharacter)

@given(instance=gastm::LongDouble_strategy)
@settings(max_examples=50)
def test_gastm::longdouble_instantiation(instance):
    assert isinstance(instance, gastm::LongDouble)

@given(instance=gastm::Float_strategy)
@settings(max_examples=50)
def test_gastm::float_instantiation(instance):
    assert isinstance(instance, gastm::Float)

@given(instance=gastm::Integer_strategy)
@settings(max_examples=50)
def test_gastm::integer_instantiation(instance):
    assert isinstance(instance, gastm::Integer)

@given(instance=gastm::Void_strategy)
@settings(max_examples=50)
def test_gastm::void_instantiation(instance):
    assert isinstance(instance, gastm::Void)

@given(instance=StorageSpecification_strategy)
@settings(max_examples=50)
def test_storagespecification_instantiation(instance):
    assert isinstance(instance, StorageSpecification)

@given(instance=gastm::FunctionPersistent_strategy)
@settings(max_examples=50)
def test_gastm::functionpersistent_instantiation(instance):
    assert isinstance(instance, gastm::FunctionPersistent)

@given(instance=gastm::PerClassMember_strategy)
@settings(max_examples=50)
def test_gastm::perclassmember_instantiation(instance):
    assert isinstance(instance, gastm::PerClassMember)

@given(instance=gastm::NoDef_strategy)
@settings(max_examples=50)
def test_gastm::nodef_instantiation(instance):
    assert isinstance(instance, gastm::NoDef)

@given(instance=gastm::FileLocal_strategy)
@settings(max_examples=50)
def test_gastm::filelocal_instantiation(instance):
    assert isinstance(instance, gastm::FileLocal)

@given(instance=gastm::External_strategy)
@settings(max_examples=50)
def test_gastm::external_instantiation(instance):
    assert isinstance(instance, gastm::External)

@given(instance=gastm::Boolean_strategy)
@settings(max_examples=50)
def test_gastm::boolean_instantiation(instance):
    assert isinstance(instance, gastm::Boolean)

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

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=gastm::BitRightShift_strategy)
@settings(max_examples=50)
def test_gastm::bitrightshift_instantiation(instance):
    assert isinstance(instance, gastm::BitRightShift)

@given(instance=gastm::Subtract_strategy)
@settings(max_examples=50)
def test_gastm::subtract_instantiation(instance):
    assert isinstance(instance, gastm::Subtract)

@given(instance=gastm::BitXor_strategy)
@settings(max_examples=50)
def test_gastm::bitxor_instantiation(instance):
    assert isinstance(instance, gastm::BitXor)

@given(instance=gastm::Less_strategy)
@settings(max_examples=50)
def test_gastm::less_instantiation(instance):
    assert isinstance(instance, gastm::Less)

@given(instance=gastm::Multiply_strategy)
@settings(max_examples=50)
def test_gastm::multiply_instantiation(instance):
    assert isinstance(instance, gastm::Multiply)

@given(instance=gastm::Add_strategy)
@settings(max_examples=50)
def test_gastm::add_instantiation(instance):
    assert isinstance(instance, gastm::Add)

@given(instance=gastm::BitLeftShift_strategy)
@settings(max_examples=50)
def test_gastm::bitleftshift_instantiation(instance):
    assert isinstance(instance, gastm::BitLeftShift)

@given(instance=gastm::Assign_strategy)
@settings(max_examples=50)
def test_gastm::assign_instantiation(instance):
    assert isinstance(instance, gastm::Assign)

@given(instance=gastm::Modulus_strategy)
@settings(max_examples=50)
def test_gastm::modulus_instantiation(instance):
    assert isinstance(instance, gastm::Modulus)

@given(instance=gastm::Greater_strategy)
@settings(max_examples=50)
def test_gastm::greater_instantiation(instance):
    assert isinstance(instance, gastm::Greater)

@given(instance=gastm::BitAnd_strategy)
@settings(max_examples=50)
def test_gastm::bitand_instantiation(instance):
    assert isinstance(instance, gastm::BitAnd)

@given(instance=gastm::NotLess_strategy)
@settings(max_examples=50)
def test_gastm::notless_instantiation(instance):
    assert isinstance(instance, gastm::NotLess)

@given(instance=gastm::NotEqual_strategy)
@settings(max_examples=50)
def test_gastm::notequal_instantiation(instance):
    assert isinstance(instance, gastm::NotEqual)

@given(instance=gastm::Divide_strategy)
@settings(max_examples=50)
def test_gastm::divide_instantiation(instance):
    assert isinstance(instance, gastm::Divide)

@given(instance=gastm::Exponent_strategy)
@settings(max_examples=50)
def test_gastm::exponent_instantiation(instance):
    assert isinstance(instance, gastm::Exponent)

@given(instance=gastm::NotGreater_strategy)
@settings(max_examples=50)
def test_gastm::notgreater_instantiation(instance):
    assert isinstance(instance, gastm::NotGreater)

@given(instance=gastm::Equal_strategy)
@settings(max_examples=50)
def test_gastm::equal_instantiation(instance):
    assert isinstance(instance, gastm::Equal)

@given(instance=gastm::And_strategy)
@settings(max_examples=50)
def test_gastm::and_instantiation(instance):
    assert isinstance(instance, gastm::And)

@given(instance=gastm::BitOr_strategy)
@settings(max_examples=50)
def test_gastm::bitor_instantiation(instance):
    assert isinstance(instance, gastm::BitOr)

@given(instance=gastm::Or_strategy)
@settings(max_examples=50)
def test_gastm::or_instantiation(instance):
    assert isinstance(instance, gastm::Or)

@given(instance=gastm::OperatorAssign_strategy)
@settings(max_examples=50)
def test_gastm::operatorassign_instantiation(instance):
    assert isinstance(instance, gastm::OperatorAssign)

@given(instance=NameReference_strategy)
@settings(max_examples=50)
def test_namereference_instantiation(instance):
    assert isinstance(instance, NameReference)

@given(instance=gastm::IdentifierReference_strategy)
@settings(max_examples=50)
def test_gastm::identifierreference_instantiation(instance):
    assert isinstance(instance, gastm::IdentifierReference)

@given(instance=gastm::QualifiedIdentifierReference_strategy)
@settings(max_examples=50)
def test_gastm::qualifiedidentifierreference_instantiation(instance):
    assert isinstance(instance, gastm::QualifiedIdentifierReference)

@given(instance=gastm::TypeQualifiedIdentifierReference_strategy)
@settings(max_examples=50)
def test_gastm::typequalifiedidentifierreference_instantiation(instance):
    assert isinstance(instance, gastm::TypeQualifiedIdentifierReference)

@given(instance=IdentifierReference_strategy)
@settings(max_examples=50)
def test_identifierreference_instantiation(instance):
    assert isinstance(instance, IdentifierReference)

@given(instance=CatchBlock_strategy)
@settings(max_examples=50)
def test_catchblock_instantiation(instance):
    assert isinstance(instance, CatchBlock)

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

@given(instance=gastm::TypesCatchBlock_strategy)
@settings(max_examples=50)
def test_gastm::typescatchblock_instantiation(instance):
    assert isinstance(instance, gastm::TypesCatchBlock)

@given(instance=SwitchCase_strategy)
@settings(max_examples=50)
def test_switchcase_instantiation(instance):
    assert isinstance(instance, SwitchCase)

@given(instance=gastm::CaseBlock_strategy)
@settings(max_examples=50)
def test_gastm::caseblock_instantiation(instance):
    assert isinstance(instance, gastm::CaseBlock)

@given(instance=gastm::DefaultBlock_strategy)
@settings(max_examples=50)
def test_gastm::defaultblock_instantiation(instance):
    assert isinstance(instance, gastm::DefaultBlock)

@given(instance=BlockScope_strategy)
@settings(max_examples=50)
def test_blockscope_instantiation(instance):
    assert isinstance(instance, BlockScope)

@given(instance=LabelDefinition_strategy)
@settings(max_examples=50)
def test_labeldefinition_instantiation(instance):
    assert isinstance(instance, LabelDefinition)

@given(instance=DerivesFrom_strategy)
@settings(max_examples=50)
def test_derivesfrom_instantiation(instance):
    assert isinstance(instance, DerivesFrom)

@given(instance=LabelAccess_strategy)
@settings(max_examples=50)
def test_labelaccess_instantiation(instance):
    assert isinstance(instance, LabelAccess)

@given(instance=ConstructedType_strategy)
@settings(max_examples=50)
def test_constructedtype_instantiation(instance):
    assert isinstance(instance, ConstructedType)

@given(instance=gastm::CollectionType_strategy)
@settings(max_examples=50)
def test_gastm::collectiontype_instantiation(instance):
    assert isinstance(instance, gastm::CollectionType)

@given(instance=gastm::ReferenceType_strategy)
@settings(max_examples=50)
def test_gastm::referencetype_instantiation(instance):
    assert isinstance(instance, gastm::ReferenceType)

@given(instance=gastm::RangeType_strategy)
@settings(max_examples=50)
def test_gastm::rangetype_instantiation(instance):
    assert isinstance(instance, gastm::RangeType)

@given(instance=gastm::PointerType_strategy)
@settings(max_examples=50)
def test_gastm::pointertype_instantiation(instance):
    assert isinstance(instance, gastm::PointerType)

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

@given(instance=gastm::ConstructedType_strategy)
@settings(max_examples=50)
def test_gastm::constructedtype_instantiation(instance):
    assert isinstance(instance, gastm::ConstructedType)

@given(instance=gastm::EnumType_strategy)
@settings(max_examples=50)
def test_gastm::enumtype_instantiation(instance):
    assert isinstance(instance, gastm::EnumType)

@given(instance=gastm::AggregateType_strategy)
@settings(max_examples=50)
def test_gastm::aggregatetype_instantiation(instance):
    assert isinstance(instance, gastm::AggregateType)

@given(instance=gastm::ExceptionType_strategy)
@settings(max_examples=50)
def test_gastm::exceptiontype_instantiation(instance):
    assert isinstance(instance, gastm::ExceptionType)

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

@given(instance=gastm::ByReferenceFormalParameterType_strategy)
@settings(max_examples=50)
def test_gastm::byreferenceformalparametertype_instantiation(instance):
    assert isinstance(instance, gastm::ByReferenceFormalParameterType)

@given(instance=gastm::ByValueFormalParameterType_strategy)
@settings(max_examples=50)
def test_gastm::byvalueformalparametertype_instantiation(instance):
    assert isinstance(instance, gastm::ByValueFormalParameterType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=gastm::LabelType_strategy)
@settings(max_examples=50)
def test_gastm::labeltype_instantiation(instance):
    assert isinstance(instance, gastm::LabelType)

@given(instance=gastm::TypeReference_strategy)
@settings(max_examples=50)
def test_gastm::typereference_instantiation(instance):
    assert isinstance(instance, gastm::TypeReference)

@given(instance=gastm::NameSpaceType_strategy)
@settings(max_examples=50)
def test_gastm::namespacetype_instantiation(instance):
    assert isinstance(instance, gastm::NameSpaceType)

@given(instance=gastm::FunctionType_strategy)
@settings(max_examples=50)
def test_gastm::functiontype_instantiation(instance):
    assert isinstance(instance, gastm::FunctionType)

@given(instance=Dimension_strategy)
@settings(max_examples=50)
def test_dimension_instantiation(instance):
    assert isinstance(instance, Dimension)

@given(instance=NameSpaceType_strategy)
@settings(max_examples=50)
def test_namespacetype_instantiation(instance):
    assert isinstance(instance, NameSpaceType)

@given(instance=AggregateType_strategy)
@settings(max_examples=50)
def test_aggregatetype_instantiation(instance):
    assert isinstance(instance, AggregateType)

@given(instance=gastm::ClassType_strategy)
@settings(max_examples=50)
def test_gastm::classtype_instantiation(instance):
    assert isinstance(instance, gastm::ClassType)

@given(instance=gastm::UnionType_strategy)
@settings(max_examples=50)
def test_gastm::uniontype_instantiation(instance):
    assert isinstance(instance, gastm::UnionType)

@given(instance=gastm::AnnotationType_strategy)
@settings(max_examples=50)
def test_gastm::annotationtype_instantiation(instance):
    assert isinstance(instance, gastm::AnnotationType)

@given(instance=gastm::StructureType_strategy)
@settings(max_examples=50)
def test_gastm::structuretype_instantiation(instance):
    assert isinstance(instance, gastm::StructureType)

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

@given(instance=GASTMSyntaxObject_strategy)
@settings(max_examples=50)
def test_gastmsyntaxobject_instantiation(instance):
    assert isinstance(instance, GASTMSyntaxObject)

@given(instance=gastm::DefinitionObject_strategy)
@settings(max_examples=50)
def test_gastm::definitionobject_instantiation(instance):
    assert isinstance(instance, gastm::DefinitionObject)

@given(instance=gastm::PreprocessorElement_strategy)
@settings(max_examples=50)
def test_gastm::preprocessorelement_instantiation(instance):
    assert isinstance(instance, gastm::PreprocessorElement)

@given(instance=gastm::Expression_strategy)
@settings(max_examples=50)
def test_gastm::expression_instantiation(instance):
    assert isinstance(instance, gastm::Expression)

@given(instance=gastm::Statement_strategy)
@settings(max_examples=50)
def test_gastm::statement_instantiation(instance):
    assert isinstance(instance, gastm::Statement)

@given(instance=gastm::Type_strategy)
@settings(max_examples=50)
def test_gastm::type_instantiation(instance):
    assert isinstance(instance, gastm::Type)

@given(instance=gastm::Type_strategy)
def test_gastm::type_isVolatile_type(instance):
    assert isinstance(instance.isVolatile, bool)


@given(instance=gastm::Type_strategy)
def test_gastm::type_isVolatile_setter(instance):
    original = instance.isVolatile
    instance.isVolatile = original
    assert instance.isVolatile == original

@given(instance=gastm::Type_strategy)
def test_gastm::type_isConst_type(instance):
    assert isinstance(instance.isConst, bool)


@given(instance=gastm::Type_strategy)
def test_gastm::type_isConst_setter(instance):
    original = instance.isConst
    instance.isConst = original
    assert instance.isConst == original

@given(instance=MacroDefinition_strategy)
@settings(max_examples=50)
def test_macrodefinition_instantiation(instance):
    assert isinstance(instance, MacroDefinition)

@given(instance=LabelType_strategy)
@settings(max_examples=50)
def test_labeltype_instantiation(instance):
    assert isinstance(instance, LabelType)

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
def test_gastm::functionmemberattributes_isThisConst_type(instance):
    assert isinstance(instance.isThisConst, bool)


@given(instance=gastm::FunctionMemberAttributes_strategy)
def test_gastm::functionmemberattributes_isThisConst_setter(instance):
    original = instance.isThisConst
    instance.isThisConst = original
    assert instance.isThisConst == original

@given(instance=gastm::FunctionMemberAttributes_strategy)
def test_gastm::functionmemberattributes_isFriend_type(instance):
    assert isinstance(instance.isFriend, bool)


@given(instance=gastm::FunctionMemberAttributes_strategy)
def test_gastm::functionmemberattributes_isFriend_setter(instance):
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

@given(instance=gastm::EmptyStatement_strategy)
@settings(max_examples=50)
def test_gastm::emptystatement_instantiation(instance):
    assert isinstance(instance, gastm::EmptyStatement)

@given(instance=gastm::ContinueStatement_strategy)
@settings(max_examples=50)
def test_gastm::continuestatement_instantiation(instance):
    assert isinstance(instance, gastm::ContinueStatement)

@given(instance=gastm::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_gastm::expressionstatement_instantiation(instance):
    assert isinstance(instance, gastm::ExpressionStatement)

@given(instance=gastm::ReturnStatement_strategy)
@settings(max_examples=50)
def test_gastm::returnstatement_instantiation(instance):
    assert isinstance(instance, gastm::ReturnStatement)

@given(instance=gastm::BlockStatement_strategy)
@settings(max_examples=50)
def test_gastm::blockstatement_instantiation(instance):
    assert isinstance(instance, gastm::BlockStatement)

@given(instance=gastm::DeclarationOrDefinitionStatement_strategy)
@settings(max_examples=50)
def test_gastm::declarationordefinitionstatement_instantiation(instance):
    assert isinstance(instance, gastm::DeclarationOrDefinitionStatement)

@given(instance=gastm::LabeledStatement_strategy)
@settings(max_examples=50)
def test_gastm::labeledstatement_instantiation(instance):
    assert isinstance(instance, gastm::LabeledStatement)

@given(instance=gastm::DeleteStatement_strategy)
@settings(max_examples=50)
def test_gastm::deletestatement_instantiation(instance):
    assert isinstance(instance, gastm::DeleteStatement)

@given(instance=gastm::TryStatement_strategy)
@settings(max_examples=50)
def test_gastm::trystatement_instantiation(instance):
    assert isinstance(instance, gastm::TryStatement)

@given(instance=gastm::SwitchStatement_strategy)
@settings(max_examples=50)
def test_gastm::switchstatement_instantiation(instance):
    assert isinstance(instance, gastm::SwitchStatement)

@given(instance=gastm::IfStatement_strategy)
@settings(max_examples=50)
def test_gastm::ifstatement_instantiation(instance):
    assert isinstance(instance, gastm::IfStatement)

@given(instance=gastm::TerminateStatement_strategy)
@settings(max_examples=50)
def test_gastm::terminatestatement_instantiation(instance):
    assert isinstance(instance, gastm::TerminateStatement)

@given(instance=gastm::BreakStatement_strategy)
@settings(max_examples=50)
def test_gastm::breakstatement_instantiation(instance):
    assert isinstance(instance, gastm::BreakStatement)

@given(instance=gastm::ThrowStatement_strategy)
@settings(max_examples=50)
def test_gastm::throwstatement_instantiation(instance):
    assert isinstance(instance, gastm::ThrowStatement)

@given(instance=gastm::LoopStatement_strategy)
@settings(max_examples=50)
def test_gastm::loopstatement_instantiation(instance):
    assert isinstance(instance, gastm::LoopStatement)

@given(instance=gastm::JumpStatement_strategy)
@settings(max_examples=50)
def test_gastm::jumpstatement_instantiation(instance):
    assert isinstance(instance, gastm::JumpStatement)

@given(instance=FormalParameterDefinition_strategy)
@settings(max_examples=50)
def test_formalparameterdefinition_instantiation(instance):
    assert isinstance(instance, FormalParameterDefinition)

@given(instance=DataDefinition_strategy)
@settings(max_examples=50)
def test_datadefinition_instantiation(instance):
    assert isinstance(instance, DataDefinition)

@given(instance=gastm::FormalParameterDefinition_strategy)
@settings(max_examples=50)
def test_gastm::formalparameterdefinition_instantiation(instance):
    assert isinstance(instance, gastm::FormalParameterDefinition)

@given(instance=gastm::VariableDefinition_strategy)
@settings(max_examples=50)
def test_gastm::variabledefinition_instantiation(instance):
    assert isinstance(instance, gastm::VariableDefinition)

@given(instance=gastm::BitFieldDefinition_strategy)
@settings(max_examples=50)
def test_gastm::bitfielddefinition_instantiation(instance):
    assert isinstance(instance, gastm::BitFieldDefinition)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=gastm::AggregateExpression_strategy)
@settings(max_examples=50)
def test_gastm::aggregateexpression_instantiation(instance):
    assert isinstance(instance, gastm::AggregateExpression)

@given(instance=gastm::LabelAccess_strategy)
@settings(max_examples=50)
def test_gastm::labelaccess_instantiation(instance):
    assert isinstance(instance, gastm::LabelAccess)

@given(instance=gastm::ArrayAccess_strategy)
@settings(max_examples=50)
def test_gastm::arrayaccess_instantiation(instance):
    assert isinstance(instance, gastm::ArrayAccess)

@given(instance=gastm::BinaryExpression_strategy)
@settings(max_examples=50)
def test_gastm::binaryexpression_instantiation(instance):
    assert isinstance(instance, gastm::BinaryExpression)

@given(instance=gastm::CastExpression_strategy)
@settings(max_examples=50)
def test_gastm::castexpression_instantiation(instance):
    assert isinstance(instance, gastm::CastExpression)

@given(instance=gastm::FunctionCallExpression_strategy)
@settings(max_examples=50)
def test_gastm::functioncallexpression_instantiation(instance):
    assert isinstance(instance, gastm::FunctionCallExpression)

@given(instance=gastm::RangeExpression_strategy)
@settings(max_examples=50)
def test_gastm::rangeexpression_instantiation(instance):
    assert isinstance(instance, gastm::RangeExpression)

@given(instance=gastm::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_gastm::conditionalexpression_instantiation(instance):
    assert isinstance(instance, gastm::ConditionalExpression)

@given(instance=gastm::NewExpression_strategy)
@settings(max_examples=50)
def test_gastm::newexpression_instantiation(instance):
    assert isinstance(instance, gastm::NewExpression)

@given(instance=gastm::AnnotationExpression_strategy)
@settings(max_examples=50)
def test_gastm::annotationexpression_instantiation(instance):
    assert isinstance(instance, gastm::AnnotationExpression)

@given(instance=gastm::UnaryExpression_strategy)
@settings(max_examples=50)
def test_gastm::unaryexpression_instantiation(instance):
    assert isinstance(instance, gastm::UnaryExpression)

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

@given(instance=gastm::NameReference_strategy)
@settings(max_examples=50)
def test_gastm::namereference_instantiation(instance):
    assert isinstance(instance, gastm::NameReference)

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

@given(instance=gastm::EntryDefinition_strategy)
@settings(max_examples=50)
def test_gastm::entrydefinition_instantiation(instance):
    assert isinstance(instance, gastm::EntryDefinition)

@given(instance=gastm::FunctionDefinition_strategy)
@settings(max_examples=50)
def test_gastm::functiondefinition_instantiation(instance):
    assert isinstance(instance, gastm::FunctionDefinition)

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

@given(instance=FunctionMemberAttributes_strategy)
@settings(max_examples=50)
def test_functionmemberattributes_instantiation(instance):
    assert isinstance(instance, FunctionMemberAttributes)

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

@given(instance=gastm::BlockScope_strategy)
@settings(max_examples=50)
def test_gastm::blockscope_instantiation(instance):
    assert isinstance(instance, gastm::BlockScope)

@given(instance=gastm::ProgramScope_strategy)
@settings(max_examples=50)
def test_gastm::programscope_instantiation(instance):
    assert isinstance(instance, gastm::ProgramScope)

@given(instance=gastm::AggregateScope_strategy)
@settings(max_examples=50)
def test_gastm::aggregatescope_instantiation(instance):
    assert isinstance(instance, gastm::AggregateScope)

@given(instance=gastm::GlobalScope_strategy)
@settings(max_examples=50)
def test_gastm::globalscope_instantiation(instance):
    assert isinstance(instance, gastm::GlobalScope)

@given(instance=gastm::FunctionScope_strategy)
@settings(max_examples=50)
def test_gastm::functionscope_instantiation(instance):
    assert isinstance(instance, gastm::FunctionScope)

@given(instance=DefinitionObject_strategy)
@settings(max_examples=50)
def test_definitionobject_instantiation(instance):
    assert isinstance(instance, DefinitionObject)

@given(instance=gastm::LabelDefinition_strategy)
@settings(max_examples=50)
def test_gastm::labeldefinition_instantiation(instance):
    assert isinstance(instance, gastm::LabelDefinition)

@given(instance=gastm::NameSpaceDefinition_strategy)
@settings(max_examples=50)
def test_gastm::namespacedefinition_instantiation(instance):
    assert isinstance(instance, gastm::NameSpaceDefinition)

@given(instance=gastm::TypeDefinition_strategy)
@settings(max_examples=50)
def test_gastm::typedefinition_instantiation(instance):
    assert isinstance(instance, gastm::TypeDefinition)

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

@given(instance=ProgramScope_strategy)
@settings(max_examples=50)
def test_programscope_instantiation(instance):
    assert isinstance(instance, ProgramScope)

@given(instance=OtherSyntaxObject_strategy)
@settings(max_examples=50)
def test_othersyntaxobject_instantiation(instance):
    assert isinstance(instance, OtherSyntaxObject)

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

@given(instance=gastm::Dimension_strategy)
@settings(max_examples=50)
def test_gastm::dimension_instantiation(instance):
    assert isinstance(instance, gastm::Dimension)

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

@given(instance=gastm::VirtualSpecification_strategy)
@settings(max_examples=50)
def test_gastm::virtualspecification_instantiation(instance):
    assert isinstance(instance, gastm::VirtualSpecification)

@given(instance=gastm::SwitchCase_strategy)
@settings(max_examples=50)
def test_gastm::switchcase_instantiation(instance):
    assert isinstance(instance, gastm::SwitchCase)

@given(instance=gastm::FunctionMemberAttribute_strategy)
@settings(max_examples=50)
def test_gastm::functionmemberattribute_instantiation(instance):
    assert isinstance(instance, gastm::FunctionMemberAttribute)

@given(instance=gastm::CatchBlock_strategy)
@settings(max_examples=50)
def test_gastm::catchblock_instantiation(instance):
    assert isinstance(instance, gastm::CatchBlock)

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

@given(instance=gastm::MacroDefinition_strategy)
@settings(max_examples=50)
def test_gastm::macrodefinition_instantiation(instance):
    assert isinstance(instance, gastm::MacroDefinition)

@given(instance=gastm::MacroDefinition_strategy)
def test_gastm::macrodefinition_macroName_type(instance):
    assert isinstance(instance.macroName, str)


@given(instance=gastm::MacroDefinition_strategy)
def test_gastm::macrodefinition_macroName_setter(instance):
    original = instance.macroName
    instance.macroName = original
    assert instance.macroName == original

@given(instance=gastm::MacroDefinition_strategy)
def test_gastm::macrodefinition_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=gastm::MacroDefinition_strategy)
def test_gastm::macrodefinition_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=gastm::MacroCall_strategy)
@settings(max_examples=50)
def test_gastm::macrocall_instantiation(instance):
    assert isinstance(instance, gastm::MacroCall)

@given(instance=gastm::IncludeUnit_strategy)
@settings(max_examples=50)
def test_gastm::includeunit_instantiation(instance):
    assert isinstance(instance, gastm::IncludeUnit)

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

@given(instance=GASTMSourceObject_strategy)
@settings(max_examples=50)
def test_gastmsourceobject_instantiation(instance):
    assert isinstance(instance, GASTMSourceObject)

@given(instance=gastm::SourceLocation_strategy)
@settings(max_examples=50)
def test_gastm::sourcelocation_instantiation(instance):
    assert isinstance(instance, gastm::SourceLocation)

@given(instance=gastm::SourceLocation_strategy)
def test_gastm::sourcelocation_endLine_type(instance):
    assert isinstance(instance.endLine, int)


@given(instance=gastm::SourceLocation_strategy)
def test_gastm::sourcelocation_endLine_setter(instance):
    original = instance.endLine
    instance.endLine = original
    assert instance.endLine == original

@given(instance=gastm::SourceLocation_strategy)
def test_gastm::sourcelocation_startLine_type(instance):
    assert isinstance(instance.startLine, int)


@given(instance=gastm::SourceLocation_strategy)
def test_gastm::sourcelocation_startLine_setter(instance):
    original = instance.startLine
    instance.startLine = original
    assert instance.startLine == original

@given(instance=gastm::SourceLocation_strategy)
def test_gastm::sourcelocation_endColumn_type(instance):
    assert isinstance(instance.endColumn, int)


@given(instance=gastm::SourceLocation_strategy)
def test_gastm::sourcelocation_endColumn_setter(instance):
    original = instance.endColumn
    instance.endColumn = original
    assert instance.endColumn == original

@given(instance=gastm::SourceLocation_strategy)
def test_gastm::sourcelocation_startColumn_type(instance):
    assert isinstance(instance.startColumn, int)


@given(instance=gastm::SourceLocation_strategy)
def test_gastm::sourcelocation_startColumn_setter(instance):
    original = instance.startColumn
    instance.startColumn = original
    assert instance.startColumn == original

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
