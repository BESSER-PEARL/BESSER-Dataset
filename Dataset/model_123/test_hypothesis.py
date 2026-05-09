import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ClassType,
    astm::SpecificClassType,
    ActualParameterExpression,
    astm::ByReferenceActualParameterExpression,
    astm::ByValueActualParameterExpression,
    UnaryOperator,
    astm::Not,
    astm::Deref,
    astm::BitNot,
    astm::Decrement,
    astm::Increment,
    astm::AddressOf,
    astm::PostIncrement,
    astm::Negate,
    astm::PostDecrement,
    astm::UnaryPlus,
    Literal,
    astm::CharLiteral,
    astm::StringLiteral,
    astm::BitLiteral,
    astm::RealLiteral,
    astm::BooleanLiteral,
    astm::IntegerlLiteral,
    QualifiedIdentifierReference,
    astm::QualifiedOverData,
    astm::QualifiedOverPointer,
    ForStatement,
    astm::ForCheckAfterStatement,
    astm::ForCheckBeforeStatement,
    AccessKind,
    astm::Private,
    astm::Protected,
    astm::Public,
    FormalParameterType,
    astm::ByReferenceFormalParameterType,
    astm::ByValueFormalParameterType,
    PrimitiveType,
    astm::String,
    astm::Double,
    astm::Byte,
    astm::WideCharacter,
    astm::Integer,
    astm::Float,
    astm::LongInteger,
    astm::Boolean,
    astm::ShortInteger,
    astm::LongDouble,
    astm::Character,
    astm::Void,
    VirtualSpecification,
    astm::NonVirtual,
    astm::PureVirtual,
    astm::Virtual,
    StorageSpecification,
    astm::NoDef,
    astm::PerClassMember,
    astm::FunctionPersistent,
    astm::FileLocal,
    astm::External,
    Scope,
    ActualParameter,
    astm::MissingActualParameter,
    astm::ActualParameterExpression,
    BinaryOperator,
    astm::Exponent,
    astm::Assign,
    astm::BitAnd,
    astm::Add,
    astm::NotGreater,
    astm::Or,
    astm::And,
    astm::BitRightShift,
    astm::NotLess,
    astm::Modulus,
    astm::Multiply,
    astm::Equal,
    astm::Subtract,
    astm::Less,
    astm::NotEqual,
    astm::Greater,
    astm::BitLeftShift,
    astm::BitOr,
    astm::BitXor,
    astm::OperatorAssign,
    NameReference,
    astm::IdentifierReference,
    astm::TypeQualifiedIdentifierReference,
    astm::QualifiedIdentifierReference,
    Expression,
    astm::UnaryExpression,
    astm::BinaryExpression,
    astm::NewExpression,
    astm::ArrayAccess,
    astm::FunctionCallExpression,
    astm::Literal,
    astm::AggregateExpression,
    astm::CastExpression,
    astm::RangeExpression,
    astm::ConditionalExpression,
    astm::NameReference,
    CatchBlock,
    astm::VariableCatchBlock,
    astm::TypesCatchBlock,
    LoopStatement,
    astm::DoWhileStatement,
    astm::WhileStatement,
    SwitchCase,
    astm::DefaultBlock,
    astm::CaseBlock,
    astm::BlockScope,
    astm::ForStatement,
    astm::LabelAccess,
    Statement,
    astm::SwitchStatement,
    astm::TryStatement,
    astm::ThrowStatement,
    astm::EmptyStatement,
    astm::ExpressionStatement,
    astm::ReturnStatement,
    astm::BreakStatement,
    astm::DeclarationOrDefinitionStatement,
    astm::BlockStatement,
    astm::IfStatement,
    astm::ContinueStatement,
    astm::JumpStatement,
    astm::LabeledStatement,
    astm::TerminateStatement,
    astm::LoopStatement,
    astm::DeleteStatement,
    TypeReference,
    astm::NamedTypeReference,
    astm::UnnamedTypeReference,
    AggregateType,
    astm::StructureType,
    astm::AnnotationType,
    astm::UnionType,
    astm::ClassType,
    Type,
    astm::FunctionType,
    ConstructedType,
    astm::PointerType,
    astm::CollectionType,
    astm::ReferenceType,
    astm::RangeType,
    astm::ArrayType,
    astm::AggregateScope,
    DataType,
    astm::FormalParameterType,
    astm::ExceptionType,
    astm::ConstructedType,
    astm::EnumType,
    astm::PrimitiveType,
    GASTMSyntaxObject,
    astm::Type,
    PreprocessorElement,
    astm::MacroDefinition,
    astm::MacroCall,
    astm::Comment,
    astm::IncludeUnit,
    astm::LabelType,
    astm::NameSpaceType,
    astm::AggregateType,
    astm::NamedType,
    TypeDefinition,
    astm::AggregateTypeDefinition,
    astm::NamedTypeDefinition,
    DataDefinition,
    astm::VariableDefinition,
    astm::BitFieldDefinition,
    astm::Expression,
    astm::FunctionScope,
    astm::Statement,
    astm::FormalParameterDefinition,
    Definition,
    astm::EntryDefinition,
    astm::DataDefinition,
    astm::EnumLiteralDefinition,
    astm::FunctionDefinition,
    astm::FunctionMemberAttributes,
    Declaration,
    astm::FormalParameterDeclaration,
    astm::VariableDeclaration,
    astm::FunctionDeclaration,
    astm::TypeReference,
    DeclarationOrDefinition,
    astm::Declaration,
    astm::Definition,
    DefinitionObject,
    astm::NameSpaceDefinition,
    astm::LabelDefinition,
    astm::TypeDefinition,
    astm::DeclarationOrDefinition,
    astm::ProgramScope,
    OtherSyntaxObject,
    astm::SwitchCase,
    astm::FunctionMemberAttribute,
    astm::Name,
    astm::VirtualSpecification,
    astm::Dimension,
    astm::DerivesFrom,
    astm::CatchBlock,
    astm::AnnotationExpression,
    astm::PreprocessorElement,
    GASTMObject,
    astm::GASTMSyntaxObject,
    astm::DefinitionObject,
    astm::GlobalScope,
    astm::CompilationUnit,
    GASTMSemanticObject,
    astm::Scope,
    astm::Project,
    GASTMSourceObject,
    astm::SourceLocation,
    astm::SourceFile,
    astm::ActualParameter,
    astm::BinaryOperator,
    astm::UnaryOperator,
    astm::AccessKind,
    astm::DataType,
    astm::StorageSpecification,
    astm::OtherSyntaxObject,
    astm::GASTMSemanticObject,
    astm::GASTMSourceObject,
    astm::GASTMObject,
    astm::Divide,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classtype_is_not_abstract():
    assert not inspect.isabstract(ClassType)


def test_classtype_constructor_exists():
    assert callable(ClassType.__init__)


def test_classtype_constructor_args():
    sig = inspect.signature(ClassType.__init__)
    params = list(sig.parameters.keys())



def test_astm::specificclasstype_is_not_abstract():
    assert not inspect.isabstract(astm::SpecificClassType)


def test_astm::specificclasstype_constructor_exists():
    assert callable(astm::SpecificClassType.__init__)


def test_astm::specificclasstype_constructor_args():
    sig = inspect.signature(astm::SpecificClassType.__init__)
    params = list(sig.parameters.keys())
    assert "imports" in params, "Missing parameter 'imports'"
    assert "package" in params, "Missing parameter 'package'"

def test_astm::specificclasstype_has_imports():
    assert hasattr(astm::SpecificClassType, "imports")
    descriptor = None
    for klass in astm::SpecificClassType.__mro__:
        if "imports" in klass.__dict__:
            descriptor = klass.__dict__["imports"]
            break
    assert isinstance(descriptor, property)

def test_astm::specificclasstype_has_package():
    assert hasattr(astm::SpecificClassType, "package")
    descriptor = None
    for klass in astm::SpecificClassType.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)



def test_actualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(ActualParameterExpression)


def test_actualparameterexpression_constructor_exists():
    assert callable(ActualParameterExpression.__init__)


def test_actualparameterexpression_constructor_args():
    sig = inspect.signature(ActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::byreferenceactualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(astm::ByReferenceActualParameterExpression)


def test_astm::byreferenceactualparameterexpression_constructor_exists():
    assert callable(astm::ByReferenceActualParameterExpression.__init__)


def test_astm::byreferenceactualparameterexpression_constructor_args():
    sig = inspect.signature(astm::ByReferenceActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::byvalueactualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(astm::ByValueActualParameterExpression)


def test_astm::byvalueactualparameterexpression_constructor_exists():
    assert callable(astm::ByValueActualParameterExpression.__init__)


def test_astm::byvalueactualparameterexpression_constructor_args():
    sig = inspect.signature(astm::ByValueActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_astm::not_is_not_abstract():
    assert not inspect.isabstract(astm::Not)


def test_astm::not_constructor_exists():
    assert callable(astm::Not.__init__)


def test_astm::not_constructor_args():
    sig = inspect.signature(astm::Not.__init__)
    params = list(sig.parameters.keys())



def test_astm::deref_is_not_abstract():
    assert not inspect.isabstract(astm::Deref)


def test_astm::deref_constructor_exists():
    assert callable(astm::Deref.__init__)


def test_astm::deref_constructor_args():
    sig = inspect.signature(astm::Deref.__init__)
    params = list(sig.parameters.keys())



def test_astm::bitnot_is_not_abstract():
    assert not inspect.isabstract(astm::BitNot)


def test_astm::bitnot_constructor_exists():
    assert callable(astm::BitNot.__init__)


def test_astm::bitnot_constructor_args():
    sig = inspect.signature(astm::BitNot.__init__)
    params = list(sig.parameters.keys())



def test_astm::decrement_is_not_abstract():
    assert not inspect.isabstract(astm::Decrement)


def test_astm::decrement_constructor_exists():
    assert callable(astm::Decrement.__init__)


def test_astm::decrement_constructor_args():
    sig = inspect.signature(astm::Decrement.__init__)
    params = list(sig.parameters.keys())



def test_astm::increment_is_not_abstract():
    assert not inspect.isabstract(astm::Increment)


def test_astm::increment_constructor_exists():
    assert callable(astm::Increment.__init__)


def test_astm::increment_constructor_args():
    sig = inspect.signature(astm::Increment.__init__)
    params = list(sig.parameters.keys())



def test_astm::addressof_is_not_abstract():
    assert not inspect.isabstract(astm::AddressOf)


def test_astm::addressof_constructor_exists():
    assert callable(astm::AddressOf.__init__)


def test_astm::addressof_constructor_args():
    sig = inspect.signature(astm::AddressOf.__init__)
    params = list(sig.parameters.keys())



def test_astm::postincrement_is_not_abstract():
    assert not inspect.isabstract(astm::PostIncrement)


def test_astm::postincrement_constructor_exists():
    assert callable(astm::PostIncrement.__init__)


def test_astm::postincrement_constructor_args():
    sig = inspect.signature(astm::PostIncrement.__init__)
    params = list(sig.parameters.keys())



def test_astm::negate_is_not_abstract():
    assert not inspect.isabstract(astm::Negate)


def test_astm::negate_constructor_exists():
    assert callable(astm::Negate.__init__)


def test_astm::negate_constructor_args():
    sig = inspect.signature(astm::Negate.__init__)
    params = list(sig.parameters.keys())



def test_astm::postdecrement_is_not_abstract():
    assert not inspect.isabstract(astm::PostDecrement)


def test_astm::postdecrement_constructor_exists():
    assert callable(astm::PostDecrement.__init__)


def test_astm::postdecrement_constructor_args():
    sig = inspect.signature(astm::PostDecrement.__init__)
    params = list(sig.parameters.keys())



def test_astm::unaryplus_is_not_abstract():
    assert not inspect.isabstract(astm::UnaryPlus)


def test_astm::unaryplus_constructor_exists():
    assert callable(astm::UnaryPlus.__init__)


def test_astm::unaryplus_constructor_args():
    sig = inspect.signature(astm::UnaryPlus.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_astm::charliteral_is_not_abstract():
    assert not inspect.isabstract(astm::CharLiteral)


def test_astm::charliteral_constructor_exists():
    assert callable(astm::CharLiteral.__init__)


def test_astm::charliteral_constructor_args():
    sig = inspect.signature(astm::CharLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm::stringliteral_is_not_abstract():
    assert not inspect.isabstract(astm::StringLiteral)


def test_astm::stringliteral_constructor_exists():
    assert callable(astm::StringLiteral.__init__)


def test_astm::stringliteral_constructor_args():
    sig = inspect.signature(astm::StringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm::bitliteral_is_not_abstract():
    assert not inspect.isabstract(astm::BitLiteral)


def test_astm::bitliteral_constructor_exists():
    assert callable(astm::BitLiteral.__init__)


def test_astm::bitliteral_constructor_args():
    sig = inspect.signature(astm::BitLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm::realliteral_is_not_abstract():
    assert not inspect.isabstract(astm::RealLiteral)


def test_astm::realliteral_constructor_exists():
    assert callable(astm::RealLiteral.__init__)


def test_astm::realliteral_constructor_args():
    sig = inspect.signature(astm::RealLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(astm::BooleanLiteral)


def test_astm::booleanliteral_constructor_exists():
    assert callable(astm::BooleanLiteral.__init__)


def test_astm::booleanliteral_constructor_args():
    sig = inspect.signature(astm::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm::integerlliteral_is_not_abstract():
    assert not inspect.isabstract(astm::IntegerlLiteral)


def test_astm::integerlliteral_constructor_exists():
    assert callable(astm::IntegerlLiteral.__init__)


def test_astm::integerlliteral_constructor_args():
    sig = inspect.signature(astm::IntegerlLiteral.__init__)
    params = list(sig.parameters.keys())



def test_qualifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(QualifiedIdentifierReference)


def test_qualifiedidentifierreference_constructor_exists():
    assert callable(QualifiedIdentifierReference.__init__)


def test_qualifiedidentifierreference_constructor_args():
    sig = inspect.signature(QualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_astm::qualifiedoverdata_is_not_abstract():
    assert not inspect.isabstract(astm::QualifiedOverData)


def test_astm::qualifiedoverdata_constructor_exists():
    assert callable(astm::QualifiedOverData.__init__)


def test_astm::qualifiedoverdata_constructor_args():
    sig = inspect.signature(astm::QualifiedOverData.__init__)
    params = list(sig.parameters.keys())



def test_astm::qualifiedoverpointer_is_not_abstract():
    assert not inspect.isabstract(astm::QualifiedOverPointer)


def test_astm::qualifiedoverpointer_constructor_exists():
    assert callable(astm::QualifiedOverPointer.__init__)


def test_astm::qualifiedoverpointer_constructor_args():
    sig = inspect.signature(astm::QualifiedOverPointer.__init__)
    params = list(sig.parameters.keys())



def test_forstatement_is_not_abstract():
    assert not inspect.isabstract(ForStatement)


def test_forstatement_constructor_exists():
    assert callable(ForStatement.__init__)


def test_forstatement_constructor_args():
    sig = inspect.signature(ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::forcheckafterstatement_is_not_abstract():
    assert not inspect.isabstract(astm::ForCheckAfterStatement)


def test_astm::forcheckafterstatement_constructor_exists():
    assert callable(astm::ForCheckAfterStatement.__init__)


def test_astm::forcheckafterstatement_constructor_args():
    sig = inspect.signature(astm::ForCheckAfterStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::forcheckbeforestatement_is_not_abstract():
    assert not inspect.isabstract(astm::ForCheckBeforeStatement)


def test_astm::forcheckbeforestatement_constructor_exists():
    assert callable(astm::ForCheckBeforeStatement.__init__)


def test_astm::forcheckbeforestatement_constructor_args():
    sig = inspect.signature(astm::ForCheckBeforeStatement.__init__)
    params = list(sig.parameters.keys())



def test_accesskind_is_not_abstract():
    assert not inspect.isabstract(AccessKind)


def test_accesskind_constructor_exists():
    assert callable(AccessKind.__init__)


def test_accesskind_constructor_args():
    sig = inspect.signature(AccessKind.__init__)
    params = list(sig.parameters.keys())



def test_astm::private_is_not_abstract():
    assert not inspect.isabstract(astm::Private)


def test_astm::private_constructor_exists():
    assert callable(astm::Private.__init__)


def test_astm::private_constructor_args():
    sig = inspect.signature(astm::Private.__init__)
    params = list(sig.parameters.keys())



def test_astm::protected_is_not_abstract():
    assert not inspect.isabstract(astm::Protected)


def test_astm::protected_constructor_exists():
    assert callable(astm::Protected.__init__)


def test_astm::protected_constructor_args():
    sig = inspect.signature(astm::Protected.__init__)
    params = list(sig.parameters.keys())



def test_astm::public_is_not_abstract():
    assert not inspect.isabstract(astm::Public)


def test_astm::public_constructor_exists():
    assert callable(astm::Public.__init__)


def test_astm::public_constructor_args():
    sig = inspect.signature(astm::Public.__init__)
    params = list(sig.parameters.keys())



def test_formalparametertype_is_not_abstract():
    assert not inspect.isabstract(FormalParameterType)


def test_formalparametertype_constructor_exists():
    assert callable(FormalParameterType.__init__)


def test_formalparametertype_constructor_args():
    sig = inspect.signature(FormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_astm::byreferenceformalparametertype_is_not_abstract():
    assert not inspect.isabstract(astm::ByReferenceFormalParameterType)


def test_astm::byreferenceformalparametertype_constructor_exists():
    assert callable(astm::ByReferenceFormalParameterType.__init__)


def test_astm::byreferenceformalparametertype_constructor_args():
    sig = inspect.signature(astm::ByReferenceFormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_astm::byvalueformalparametertype_is_not_abstract():
    assert not inspect.isabstract(astm::ByValueFormalParameterType)


def test_astm::byvalueformalparametertype_constructor_exists():
    assert callable(astm::ByValueFormalParameterType.__init__)


def test_astm::byvalueformalparametertype_constructor_args():
    sig = inspect.signature(astm::ByValueFormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_astm::string_is_not_abstract():
    assert not inspect.isabstract(astm::String)


def test_astm::string_constructor_exists():
    assert callable(astm::String.__init__)


def test_astm::string_constructor_args():
    sig = inspect.signature(astm::String.__init__)
    params = list(sig.parameters.keys())



def test_astm::double_is_not_abstract():
    assert not inspect.isabstract(astm::Double)


def test_astm::double_constructor_exists():
    assert callable(astm::Double.__init__)


def test_astm::double_constructor_args():
    sig = inspect.signature(astm::Double.__init__)
    params = list(sig.parameters.keys())



def test_astm::byte_is_not_abstract():
    assert not inspect.isabstract(astm::Byte)


def test_astm::byte_constructor_exists():
    assert callable(astm::Byte.__init__)


def test_astm::byte_constructor_args():
    sig = inspect.signature(astm::Byte.__init__)
    params = list(sig.parameters.keys())



def test_astm::widecharacter_is_not_abstract():
    assert not inspect.isabstract(astm::WideCharacter)


def test_astm::widecharacter_constructor_exists():
    assert callable(astm::WideCharacter.__init__)


def test_astm::widecharacter_constructor_args():
    sig = inspect.signature(astm::WideCharacter.__init__)
    params = list(sig.parameters.keys())



def test_astm::integer_is_not_abstract():
    assert not inspect.isabstract(astm::Integer)


def test_astm::integer_constructor_exists():
    assert callable(astm::Integer.__init__)


def test_astm::integer_constructor_args():
    sig = inspect.signature(astm::Integer.__init__)
    params = list(sig.parameters.keys())



def test_astm::float_is_not_abstract():
    assert not inspect.isabstract(astm::Float)


def test_astm::float_constructor_exists():
    assert callable(astm::Float.__init__)


def test_astm::float_constructor_args():
    sig = inspect.signature(astm::Float.__init__)
    params = list(sig.parameters.keys())



def test_astm::longinteger_is_not_abstract():
    assert not inspect.isabstract(astm::LongInteger)


def test_astm::longinteger_constructor_exists():
    assert callable(astm::LongInteger.__init__)


def test_astm::longinteger_constructor_args():
    sig = inspect.signature(astm::LongInteger.__init__)
    params = list(sig.parameters.keys())



def test_astm::boolean_is_not_abstract():
    assert not inspect.isabstract(astm::Boolean)


def test_astm::boolean_constructor_exists():
    assert callable(astm::Boolean.__init__)


def test_astm::boolean_constructor_args():
    sig = inspect.signature(astm::Boolean.__init__)
    params = list(sig.parameters.keys())



def test_astm::shortinteger_is_not_abstract():
    assert not inspect.isabstract(astm::ShortInteger)


def test_astm::shortinteger_constructor_exists():
    assert callable(astm::ShortInteger.__init__)


def test_astm::shortinteger_constructor_args():
    sig = inspect.signature(astm::ShortInteger.__init__)
    params = list(sig.parameters.keys())



def test_astm::longdouble_is_not_abstract():
    assert not inspect.isabstract(astm::LongDouble)


def test_astm::longdouble_constructor_exists():
    assert callable(astm::LongDouble.__init__)


def test_astm::longdouble_constructor_args():
    sig = inspect.signature(astm::LongDouble.__init__)
    params = list(sig.parameters.keys())



def test_astm::character_is_not_abstract():
    assert not inspect.isabstract(astm::Character)


def test_astm::character_constructor_exists():
    assert callable(astm::Character.__init__)


def test_astm::character_constructor_args():
    sig = inspect.signature(astm::Character.__init__)
    params = list(sig.parameters.keys())



def test_astm::void_is_not_abstract():
    assert not inspect.isabstract(astm::Void)


def test_astm::void_constructor_exists():
    assert callable(astm::Void.__init__)


def test_astm::void_constructor_args():
    sig = inspect.signature(astm::Void.__init__)
    params = list(sig.parameters.keys())



def test_virtualspecification_is_not_abstract():
    assert not inspect.isabstract(VirtualSpecification)


def test_virtualspecification_constructor_exists():
    assert callable(VirtualSpecification.__init__)


def test_virtualspecification_constructor_args():
    sig = inspect.signature(VirtualSpecification.__init__)
    params = list(sig.parameters.keys())



def test_astm::nonvirtual_is_not_abstract():
    assert not inspect.isabstract(astm::NonVirtual)


def test_astm::nonvirtual_constructor_exists():
    assert callable(astm::NonVirtual.__init__)


def test_astm::nonvirtual_constructor_args():
    sig = inspect.signature(astm::NonVirtual.__init__)
    params = list(sig.parameters.keys())



def test_astm::purevirtual_is_not_abstract():
    assert not inspect.isabstract(astm::PureVirtual)


def test_astm::purevirtual_constructor_exists():
    assert callable(astm::PureVirtual.__init__)


def test_astm::purevirtual_constructor_args():
    sig = inspect.signature(astm::PureVirtual.__init__)
    params = list(sig.parameters.keys())



def test_astm::virtual_is_not_abstract():
    assert not inspect.isabstract(astm::Virtual)


def test_astm::virtual_constructor_exists():
    assert callable(astm::Virtual.__init__)


def test_astm::virtual_constructor_args():
    sig = inspect.signature(astm::Virtual.__init__)
    params = list(sig.parameters.keys())



def test_storagespecification_is_not_abstract():
    assert not inspect.isabstract(StorageSpecification)


def test_storagespecification_constructor_exists():
    assert callable(StorageSpecification.__init__)


def test_storagespecification_constructor_args():
    sig = inspect.signature(StorageSpecification.__init__)
    params = list(sig.parameters.keys())



def test_astm::nodef_is_not_abstract():
    assert not inspect.isabstract(astm::NoDef)


def test_astm::nodef_constructor_exists():
    assert callable(astm::NoDef.__init__)


def test_astm::nodef_constructor_args():
    sig = inspect.signature(astm::NoDef.__init__)
    params = list(sig.parameters.keys())



def test_astm::perclassmember_is_not_abstract():
    assert not inspect.isabstract(astm::PerClassMember)


def test_astm::perclassmember_constructor_exists():
    assert callable(astm::PerClassMember.__init__)


def test_astm::perclassmember_constructor_args():
    sig = inspect.signature(astm::PerClassMember.__init__)
    params = list(sig.parameters.keys())



def test_astm::functionpersistent_is_not_abstract():
    assert not inspect.isabstract(astm::FunctionPersistent)


def test_astm::functionpersistent_constructor_exists():
    assert callable(astm::FunctionPersistent.__init__)


def test_astm::functionpersistent_constructor_args():
    sig = inspect.signature(astm::FunctionPersistent.__init__)
    params = list(sig.parameters.keys())



def test_astm::filelocal_is_not_abstract():
    assert not inspect.isabstract(astm::FileLocal)


def test_astm::filelocal_constructor_exists():
    assert callable(astm::FileLocal.__init__)


def test_astm::filelocal_constructor_args():
    sig = inspect.signature(astm::FileLocal.__init__)
    params = list(sig.parameters.keys())



def test_astm::external_is_not_abstract():
    assert not inspect.isabstract(astm::External)


def test_astm::external_constructor_exists():
    assert callable(astm::External.__init__)


def test_astm::external_constructor_args():
    sig = inspect.signature(astm::External.__init__)
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



def test_astm::missingactualparameter_is_not_abstract():
    assert not inspect.isabstract(astm::MissingActualParameter)


def test_astm::missingactualparameter_constructor_exists():
    assert callable(astm::MissingActualParameter.__init__)


def test_astm::missingactualparameter_constructor_args():
    sig = inspect.signature(astm::MissingActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_astm::actualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(astm::ActualParameterExpression)


def test_astm::actualparameterexpression_constructor_exists():
    assert callable(astm::ActualParameterExpression.__init__)


def test_astm::actualparameterexpression_constructor_args():
    sig = inspect.signature(astm::ActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_astm::exponent_is_not_abstract():
    assert not inspect.isabstract(astm::Exponent)


def test_astm::exponent_constructor_exists():
    assert callable(astm::Exponent.__init__)


def test_astm::exponent_constructor_args():
    sig = inspect.signature(astm::Exponent.__init__)
    params = list(sig.parameters.keys())



def test_astm::assign_is_not_abstract():
    assert not inspect.isabstract(astm::Assign)


def test_astm::assign_constructor_exists():
    assert callable(astm::Assign.__init__)


def test_astm::assign_constructor_args():
    sig = inspect.signature(astm::Assign.__init__)
    params = list(sig.parameters.keys())



def test_astm::bitand_is_not_abstract():
    assert not inspect.isabstract(astm::BitAnd)


def test_astm::bitand_constructor_exists():
    assert callable(astm::BitAnd.__init__)


def test_astm::bitand_constructor_args():
    sig = inspect.signature(astm::BitAnd.__init__)
    params = list(sig.parameters.keys())



def test_astm::add_is_not_abstract():
    assert not inspect.isabstract(astm::Add)


def test_astm::add_constructor_exists():
    assert callable(astm::Add.__init__)


def test_astm::add_constructor_args():
    sig = inspect.signature(astm::Add.__init__)
    params = list(sig.parameters.keys())



def test_astm::notgreater_is_not_abstract():
    assert not inspect.isabstract(astm::NotGreater)


def test_astm::notgreater_constructor_exists():
    assert callable(astm::NotGreater.__init__)


def test_astm::notgreater_constructor_args():
    sig = inspect.signature(astm::NotGreater.__init__)
    params = list(sig.parameters.keys())



def test_astm::or_is_not_abstract():
    assert not inspect.isabstract(astm::Or)


def test_astm::or_constructor_exists():
    assert callable(astm::Or.__init__)


def test_astm::or_constructor_args():
    sig = inspect.signature(astm::Or.__init__)
    params = list(sig.parameters.keys())



def test_astm::and_is_not_abstract():
    assert not inspect.isabstract(astm::And)


def test_astm::and_constructor_exists():
    assert callable(astm::And.__init__)


def test_astm::and_constructor_args():
    sig = inspect.signature(astm::And.__init__)
    params = list(sig.parameters.keys())



def test_astm::bitrightshift_is_not_abstract():
    assert not inspect.isabstract(astm::BitRightShift)


def test_astm::bitrightshift_constructor_exists():
    assert callable(astm::BitRightShift.__init__)


def test_astm::bitrightshift_constructor_args():
    sig = inspect.signature(astm::BitRightShift.__init__)
    params = list(sig.parameters.keys())



def test_astm::notless_is_not_abstract():
    assert not inspect.isabstract(astm::NotLess)


def test_astm::notless_constructor_exists():
    assert callable(astm::NotLess.__init__)


def test_astm::notless_constructor_args():
    sig = inspect.signature(astm::NotLess.__init__)
    params = list(sig.parameters.keys())



def test_astm::modulus_is_not_abstract():
    assert not inspect.isabstract(astm::Modulus)


def test_astm::modulus_constructor_exists():
    assert callable(astm::Modulus.__init__)


def test_astm::modulus_constructor_args():
    sig = inspect.signature(astm::Modulus.__init__)
    params = list(sig.parameters.keys())



def test_astm::multiply_is_not_abstract():
    assert not inspect.isabstract(astm::Multiply)


def test_astm::multiply_constructor_exists():
    assert callable(astm::Multiply.__init__)


def test_astm::multiply_constructor_args():
    sig = inspect.signature(astm::Multiply.__init__)
    params = list(sig.parameters.keys())



def test_astm::equal_is_not_abstract():
    assert not inspect.isabstract(astm::Equal)


def test_astm::equal_constructor_exists():
    assert callable(astm::Equal.__init__)


def test_astm::equal_constructor_args():
    sig = inspect.signature(astm::Equal.__init__)
    params = list(sig.parameters.keys())



def test_astm::subtract_is_not_abstract():
    assert not inspect.isabstract(astm::Subtract)


def test_astm::subtract_constructor_exists():
    assert callable(astm::Subtract.__init__)


def test_astm::subtract_constructor_args():
    sig = inspect.signature(astm::Subtract.__init__)
    params = list(sig.parameters.keys())



def test_astm::less_is_not_abstract():
    assert not inspect.isabstract(astm::Less)


def test_astm::less_constructor_exists():
    assert callable(astm::Less.__init__)


def test_astm::less_constructor_args():
    sig = inspect.signature(astm::Less.__init__)
    params = list(sig.parameters.keys())



def test_astm::notequal_is_not_abstract():
    assert not inspect.isabstract(astm::NotEqual)


def test_astm::notequal_constructor_exists():
    assert callable(astm::NotEqual.__init__)


def test_astm::notequal_constructor_args():
    sig = inspect.signature(astm::NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_astm::greater_is_not_abstract():
    assert not inspect.isabstract(astm::Greater)


def test_astm::greater_constructor_exists():
    assert callable(astm::Greater.__init__)


def test_astm::greater_constructor_args():
    sig = inspect.signature(astm::Greater.__init__)
    params = list(sig.parameters.keys())



def test_astm::bitleftshift_is_not_abstract():
    assert not inspect.isabstract(astm::BitLeftShift)


def test_astm::bitleftshift_constructor_exists():
    assert callable(astm::BitLeftShift.__init__)


def test_astm::bitleftshift_constructor_args():
    sig = inspect.signature(astm::BitLeftShift.__init__)
    params = list(sig.parameters.keys())



def test_astm::bitor_is_not_abstract():
    assert not inspect.isabstract(astm::BitOr)


def test_astm::bitor_constructor_exists():
    assert callable(astm::BitOr.__init__)


def test_astm::bitor_constructor_args():
    sig = inspect.signature(astm::BitOr.__init__)
    params = list(sig.parameters.keys())



def test_astm::bitxor_is_not_abstract():
    assert not inspect.isabstract(astm::BitXor)


def test_astm::bitxor_constructor_exists():
    assert callable(astm::BitXor.__init__)


def test_astm::bitxor_constructor_args():
    sig = inspect.signature(astm::BitXor.__init__)
    params = list(sig.parameters.keys())



def test_astm::operatorassign_is_not_abstract():
    assert not inspect.isabstract(astm::OperatorAssign)


def test_astm::operatorassign_constructor_exists():
    assert callable(astm::OperatorAssign.__init__)


def test_astm::operatorassign_constructor_args():
    sig = inspect.signature(astm::OperatorAssign.__init__)
    params = list(sig.parameters.keys())



def test_namereference_is_not_abstract():
    assert not inspect.isabstract(NameReference)


def test_namereference_constructor_exists():
    assert callable(NameReference.__init__)


def test_namereference_constructor_args():
    sig = inspect.signature(NameReference.__init__)
    params = list(sig.parameters.keys())



def test_astm::identifierreference_is_not_abstract():
    assert not inspect.isabstract(astm::IdentifierReference)


def test_astm::identifierreference_constructor_exists():
    assert callable(astm::IdentifierReference.__init__)


def test_astm::identifierreference_constructor_args():
    sig = inspect.signature(astm::IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_astm::typequalifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(astm::TypeQualifiedIdentifierReference)


def test_astm::typequalifiedidentifierreference_constructor_exists():
    assert callable(astm::TypeQualifiedIdentifierReference.__init__)


def test_astm::typequalifiedidentifierreference_constructor_args():
    sig = inspect.signature(astm::TypeQualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_astm::qualifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(astm::QualifiedIdentifierReference)


def test_astm::qualifiedidentifierreference_constructor_exists():
    assert callable(astm::QualifiedIdentifierReference.__init__)


def test_astm::qualifiedidentifierreference_constructor_args():
    sig = inspect.signature(astm::QualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_astm::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(astm::UnaryExpression)


def test_astm::unaryexpression_constructor_exists():
    assert callable(astm::UnaryExpression.__init__)


def test_astm::unaryexpression_constructor_args():
    sig = inspect.signature(astm::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(astm::BinaryExpression)


def test_astm::binaryexpression_constructor_exists():
    assert callable(astm::BinaryExpression.__init__)


def test_astm::binaryexpression_constructor_args():
    sig = inspect.signature(astm::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::newexpression_is_not_abstract():
    assert not inspect.isabstract(astm::NewExpression)


def test_astm::newexpression_constructor_exists():
    assert callable(astm::NewExpression.__init__)


def test_astm::newexpression_constructor_args():
    sig = inspect.signature(astm::NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::arrayaccess_is_not_abstract():
    assert not inspect.isabstract(astm::ArrayAccess)


def test_astm::arrayaccess_constructor_exists():
    assert callable(astm::ArrayAccess.__init__)


def test_astm::arrayaccess_constructor_args():
    sig = inspect.signature(astm::ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_astm::functioncallexpression_is_not_abstract():
    assert not inspect.isabstract(astm::FunctionCallExpression)


def test_astm::functioncallexpression_constructor_exists():
    assert callable(astm::FunctionCallExpression.__init__)


def test_astm::functioncallexpression_constructor_args():
    sig = inspect.signature(astm::FunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::literal_is_not_abstract():
    assert not inspect.isabstract(astm::Literal)


def test_astm::literal_constructor_exists():
    assert callable(astm::Literal.__init__)


def test_astm::literal_constructor_args():
    sig = inspect.signature(astm::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_astm::literal_has_value():
    assert hasattr(astm::Literal, "value")
    descriptor = None
    for klass in astm::Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_astm::aggregateexpression_is_not_abstract():
    assert not inspect.isabstract(astm::AggregateExpression)


def test_astm::aggregateexpression_constructor_exists():
    assert callable(astm::AggregateExpression.__init__)


def test_astm::aggregateexpression_constructor_args():
    sig = inspect.signature(astm::AggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::castexpression_is_not_abstract():
    assert not inspect.isabstract(astm::CastExpression)


def test_astm::castexpression_constructor_exists():
    assert callable(astm::CastExpression.__init__)


def test_astm::castexpression_constructor_args():
    sig = inspect.signature(astm::CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::rangeexpression_is_not_abstract():
    assert not inspect.isabstract(astm::RangeExpression)


def test_astm::rangeexpression_constructor_exists():
    assert callable(astm::RangeExpression.__init__)


def test_astm::rangeexpression_constructor_args():
    sig = inspect.signature(astm::RangeExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(astm::ConditionalExpression)


def test_astm::conditionalexpression_constructor_exists():
    assert callable(astm::ConditionalExpression.__init__)


def test_astm::conditionalexpression_constructor_args():
    sig = inspect.signature(astm::ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::namereference_is_not_abstract():
    assert not inspect.isabstract(astm::NameReference)


def test_astm::namereference_constructor_exists():
    assert callable(astm::NameReference.__init__)


def test_astm::namereference_constructor_args():
    sig = inspect.signature(astm::NameReference.__init__)
    params = list(sig.parameters.keys())



def test_catchblock_is_not_abstract():
    assert not inspect.isabstract(CatchBlock)


def test_catchblock_constructor_exists():
    assert callable(CatchBlock.__init__)


def test_catchblock_constructor_args():
    sig = inspect.signature(CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_astm::variablecatchblock_is_not_abstract():
    assert not inspect.isabstract(astm::VariableCatchBlock)


def test_astm::variablecatchblock_constructor_exists():
    assert callable(astm::VariableCatchBlock.__init__)


def test_astm::variablecatchblock_constructor_args():
    sig = inspect.signature(astm::VariableCatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_astm::typescatchblock_is_not_abstract():
    assert not inspect.isabstract(astm::TypesCatchBlock)


def test_astm::typescatchblock_constructor_exists():
    assert callable(astm::TypesCatchBlock.__init__)


def test_astm::typescatchblock_constructor_args():
    sig = inspect.signature(astm::TypesCatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_loopstatement_is_not_abstract():
    assert not inspect.isabstract(LoopStatement)


def test_loopstatement_constructor_exists():
    assert callable(LoopStatement.__init__)


def test_loopstatement_constructor_args():
    sig = inspect.signature(LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::dowhilestatement_is_not_abstract():
    assert not inspect.isabstract(astm::DoWhileStatement)


def test_astm::dowhilestatement_constructor_exists():
    assert callable(astm::DoWhileStatement.__init__)


def test_astm::dowhilestatement_constructor_args():
    sig = inspect.signature(astm::DoWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::whilestatement_is_not_abstract():
    assert not inspect.isabstract(astm::WhileStatement)


def test_astm::whilestatement_constructor_exists():
    assert callable(astm::WhileStatement.__init__)


def test_astm::whilestatement_constructor_args():
    sig = inspect.signature(astm::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_switchcase_is_not_abstract():
    assert not inspect.isabstract(SwitchCase)


def test_switchcase_constructor_exists():
    assert callable(SwitchCase.__init__)


def test_switchcase_constructor_args():
    sig = inspect.signature(SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_astm::defaultblock_is_not_abstract():
    assert not inspect.isabstract(astm::DefaultBlock)


def test_astm::defaultblock_constructor_exists():
    assert callable(astm::DefaultBlock.__init__)


def test_astm::defaultblock_constructor_args():
    sig = inspect.signature(astm::DefaultBlock.__init__)
    params = list(sig.parameters.keys())



def test_astm::caseblock_is_not_abstract():
    assert not inspect.isabstract(astm::CaseBlock)


def test_astm::caseblock_constructor_exists():
    assert callable(astm::CaseBlock.__init__)


def test_astm::caseblock_constructor_args():
    sig = inspect.signature(astm::CaseBlock.__init__)
    params = list(sig.parameters.keys())



def test_astm::blockscope_is_not_abstract():
    assert not inspect.isabstract(astm::BlockScope)


def test_astm::blockscope_constructor_exists():
    assert callable(astm::BlockScope.__init__)


def test_astm::blockscope_constructor_args():
    sig = inspect.signature(astm::BlockScope.__init__)
    params = list(sig.parameters.keys())



def test_astm::forstatement_is_not_abstract():
    assert not inspect.isabstract(astm::ForStatement)


def test_astm::forstatement_constructor_exists():
    assert callable(astm::ForStatement.__init__)


def test_astm::forstatement_constructor_args():
    sig = inspect.signature(astm::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::labelaccess_is_not_abstract():
    assert not inspect.isabstract(astm::LabelAccess)


def test_astm::labelaccess_constructor_exists():
    assert callable(astm::LabelAccess.__init__)


def test_astm::labelaccess_constructor_args():
    sig = inspect.signature(astm::LabelAccess.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_astm::switchstatement_is_not_abstract():
    assert not inspect.isabstract(astm::SwitchStatement)


def test_astm::switchstatement_constructor_exists():
    assert callable(astm::SwitchStatement.__init__)


def test_astm::switchstatement_constructor_args():
    sig = inspect.signature(astm::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::trystatement_is_not_abstract():
    assert not inspect.isabstract(astm::TryStatement)


def test_astm::trystatement_constructor_exists():
    assert callable(astm::TryStatement.__init__)


def test_astm::trystatement_constructor_args():
    sig = inspect.signature(astm::TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::throwstatement_is_not_abstract():
    assert not inspect.isabstract(astm::ThrowStatement)


def test_astm::throwstatement_constructor_exists():
    assert callable(astm::ThrowStatement.__init__)


def test_astm::throwstatement_constructor_args():
    sig = inspect.signature(astm::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::emptystatement_is_not_abstract():
    assert not inspect.isabstract(astm::EmptyStatement)


def test_astm::emptystatement_constructor_exists():
    assert callable(astm::EmptyStatement.__init__)


def test_astm::emptystatement_constructor_args():
    sig = inspect.signature(astm::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(astm::ExpressionStatement)


def test_astm::expressionstatement_constructor_exists():
    assert callable(astm::ExpressionStatement.__init__)


def test_astm::expressionstatement_constructor_args():
    sig = inspect.signature(astm::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::returnstatement_is_not_abstract():
    assert not inspect.isabstract(astm::ReturnStatement)


def test_astm::returnstatement_constructor_exists():
    assert callable(astm::ReturnStatement.__init__)


def test_astm::returnstatement_constructor_args():
    sig = inspect.signature(astm::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::breakstatement_is_not_abstract():
    assert not inspect.isabstract(astm::BreakStatement)


def test_astm::breakstatement_constructor_exists():
    assert callable(astm::BreakStatement.__init__)


def test_astm::breakstatement_constructor_args():
    sig = inspect.signature(astm::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::declarationordefinitionstatement_is_not_abstract():
    assert not inspect.isabstract(astm::DeclarationOrDefinitionStatement)


def test_astm::declarationordefinitionstatement_constructor_exists():
    assert callable(astm::DeclarationOrDefinitionStatement.__init__)


def test_astm::declarationordefinitionstatement_constructor_args():
    sig = inspect.signature(astm::DeclarationOrDefinitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::blockstatement_is_not_abstract():
    assert not inspect.isabstract(astm::BlockStatement)


def test_astm::blockstatement_constructor_exists():
    assert callable(astm::BlockStatement.__init__)


def test_astm::blockstatement_constructor_args():
    sig = inspect.signature(astm::BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::ifstatement_is_not_abstract():
    assert not inspect.isabstract(astm::IfStatement)


def test_astm::ifstatement_constructor_exists():
    assert callable(astm::IfStatement.__init__)


def test_astm::ifstatement_constructor_args():
    sig = inspect.signature(astm::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::continuestatement_is_not_abstract():
    assert not inspect.isabstract(astm::ContinueStatement)


def test_astm::continuestatement_constructor_exists():
    assert callable(astm::ContinueStatement.__init__)


def test_astm::continuestatement_constructor_args():
    sig = inspect.signature(astm::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::jumpstatement_is_not_abstract():
    assert not inspect.isabstract(astm::JumpStatement)


def test_astm::jumpstatement_constructor_exists():
    assert callable(astm::JumpStatement.__init__)


def test_astm::jumpstatement_constructor_args():
    sig = inspect.signature(astm::JumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::labeledstatement_is_not_abstract():
    assert not inspect.isabstract(astm::LabeledStatement)


def test_astm::labeledstatement_constructor_exists():
    assert callable(astm::LabeledStatement.__init__)


def test_astm::labeledstatement_constructor_args():
    sig = inspect.signature(astm::LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::terminatestatement_is_not_abstract():
    assert not inspect.isabstract(astm::TerminateStatement)


def test_astm::terminatestatement_constructor_exists():
    assert callable(astm::TerminateStatement.__init__)


def test_astm::terminatestatement_constructor_args():
    sig = inspect.signature(astm::TerminateStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::loopstatement_is_not_abstract():
    assert not inspect.isabstract(astm::LoopStatement)


def test_astm::loopstatement_constructor_exists():
    assert callable(astm::LoopStatement.__init__)


def test_astm::loopstatement_constructor_args():
    sig = inspect.signature(astm::LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::deletestatement_is_not_abstract():
    assert not inspect.isabstract(astm::DeleteStatement)


def test_astm::deletestatement_constructor_exists():
    assert callable(astm::DeleteStatement.__init__)


def test_astm::deletestatement_constructor_args():
    sig = inspect.signature(astm::DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_typereference_is_not_abstract():
    assert not inspect.isabstract(TypeReference)


def test_typereference_constructor_exists():
    assert callable(TypeReference.__init__)


def test_typereference_constructor_args():
    sig = inspect.signature(TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_astm::namedtypereference_is_not_abstract():
    assert not inspect.isabstract(astm::NamedTypeReference)


def test_astm::namedtypereference_constructor_exists():
    assert callable(astm::NamedTypeReference.__init__)


def test_astm::namedtypereference_constructor_args():
    sig = inspect.signature(astm::NamedTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_astm::unnamedtypereference_is_not_abstract():
    assert not inspect.isabstract(astm::UnnamedTypeReference)


def test_astm::unnamedtypereference_constructor_exists():
    assert callable(astm::UnnamedTypeReference.__init__)


def test_astm::unnamedtypereference_constructor_args():
    sig = inspect.signature(astm::UnnamedTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_aggregatetype_is_not_abstract():
    assert not inspect.isabstract(AggregateType)


def test_aggregatetype_constructor_exists():
    assert callable(AggregateType.__init__)


def test_aggregatetype_constructor_args():
    sig = inspect.signature(AggregateType.__init__)
    params = list(sig.parameters.keys())



def test_astm::structuretype_is_not_abstract():
    assert not inspect.isabstract(astm::StructureType)


def test_astm::structuretype_constructor_exists():
    assert callable(astm::StructureType.__init__)


def test_astm::structuretype_constructor_args():
    sig = inspect.signature(astm::StructureType.__init__)
    params = list(sig.parameters.keys())



def test_astm::annotationtype_is_not_abstract():
    assert not inspect.isabstract(astm::AnnotationType)


def test_astm::annotationtype_constructor_exists():
    assert callable(astm::AnnotationType.__init__)


def test_astm::annotationtype_constructor_args():
    sig = inspect.signature(astm::AnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_astm::uniontype_is_not_abstract():
    assert not inspect.isabstract(astm::UnionType)


def test_astm::uniontype_constructor_exists():
    assert callable(astm::UnionType.__init__)


def test_astm::uniontype_constructor_args():
    sig = inspect.signature(astm::UnionType.__init__)
    params = list(sig.parameters.keys())



def test_astm::classtype_is_not_abstract():
    assert not inspect.isabstract(astm::ClassType)


def test_astm::classtype_constructor_exists():
    assert callable(astm::ClassType.__init__)


def test_astm::classtype_constructor_args():
    sig = inspect.signature(astm::ClassType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_astm::functiontype_is_not_abstract():
    assert not inspect.isabstract(astm::FunctionType)


def test_astm::functiontype_constructor_exists():
    assert callable(astm::FunctionType.__init__)


def test_astm::functiontype_constructor_args():
    sig = inspect.signature(astm::FunctionType.__init__)
    params = list(sig.parameters.keys())



def test_constructedtype_is_not_abstract():
    assert not inspect.isabstract(ConstructedType)


def test_constructedtype_constructor_exists():
    assert callable(ConstructedType.__init__)


def test_constructedtype_constructor_args():
    sig = inspect.signature(ConstructedType.__init__)
    params = list(sig.parameters.keys())



def test_astm::pointertype_is_not_abstract():
    assert not inspect.isabstract(astm::PointerType)


def test_astm::pointertype_constructor_exists():
    assert callable(astm::PointerType.__init__)


def test_astm::pointertype_constructor_args():
    sig = inspect.signature(astm::PointerType.__init__)
    params = list(sig.parameters.keys())



def test_astm::collectiontype_is_not_abstract():
    assert not inspect.isabstract(astm::CollectionType)


def test_astm::collectiontype_constructor_exists():
    assert callable(astm::CollectionType.__init__)


def test_astm::collectiontype_constructor_args():
    sig = inspect.signature(astm::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_astm::referencetype_is_not_abstract():
    assert not inspect.isabstract(astm::ReferenceType)


def test_astm::referencetype_constructor_exists():
    assert callable(astm::ReferenceType.__init__)


def test_astm::referencetype_constructor_args():
    sig = inspect.signature(astm::ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_astm::rangetype_is_not_abstract():
    assert not inspect.isabstract(astm::RangeType)


def test_astm::rangetype_constructor_exists():
    assert callable(astm::RangeType.__init__)


def test_astm::rangetype_constructor_args():
    sig = inspect.signature(astm::RangeType.__init__)
    params = list(sig.parameters.keys())



def test_astm::arraytype_is_not_abstract():
    assert not inspect.isabstract(astm::ArrayType)


def test_astm::arraytype_constructor_exists():
    assert callable(astm::ArrayType.__init__)


def test_astm::arraytype_constructor_args():
    sig = inspect.signature(astm::ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_astm::aggregatescope_is_not_abstract():
    assert not inspect.isabstract(astm::AggregateScope)


def test_astm::aggregatescope_constructor_exists():
    assert callable(astm::AggregateScope.__init__)


def test_astm::aggregatescope_constructor_args():
    sig = inspect.signature(astm::AggregateScope.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_astm::formalparametertype_is_not_abstract():
    assert not inspect.isabstract(astm::FormalParameterType)


def test_astm::formalparametertype_constructor_exists():
    assert callable(astm::FormalParameterType.__init__)


def test_astm::formalparametertype_constructor_args():
    sig = inspect.signature(astm::FormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_astm::exceptiontype_is_not_abstract():
    assert not inspect.isabstract(astm::ExceptionType)


def test_astm::exceptiontype_constructor_exists():
    assert callable(astm::ExceptionType.__init__)


def test_astm::exceptiontype_constructor_args():
    sig = inspect.signature(astm::ExceptionType.__init__)
    params = list(sig.parameters.keys())



def test_astm::constructedtype_is_not_abstract():
    assert not inspect.isabstract(astm::ConstructedType)


def test_astm::constructedtype_constructor_exists():
    assert callable(astm::ConstructedType.__init__)


def test_astm::constructedtype_constructor_args():
    sig = inspect.signature(astm::ConstructedType.__init__)
    params = list(sig.parameters.keys())



def test_astm::enumtype_is_not_abstract():
    assert not inspect.isabstract(astm::EnumType)


def test_astm::enumtype_constructor_exists():
    assert callable(astm::EnumType.__init__)


def test_astm::enumtype_constructor_args():
    sig = inspect.signature(astm::EnumType.__init__)
    params = list(sig.parameters.keys())



def test_astm::primitivetype_is_not_abstract():
    assert not inspect.isabstract(astm::PrimitiveType)


def test_astm::primitivetype_constructor_exists():
    assert callable(astm::PrimitiveType.__init__)


def test_astm::primitivetype_constructor_args():
    sig = inspect.signature(astm::PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "isSigned" in params, "Missing parameter 'isSigned'"

def test_astm::primitivetype_has_isSigned():
    assert hasattr(astm::PrimitiveType, "isSigned")
    descriptor = None
    for klass in astm::PrimitiveType.__mro__:
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



def test_astm::type_is_not_abstract():
    assert not inspect.isabstract(astm::Type)


def test_astm::type_constructor_exists():
    assert callable(astm::Type.__init__)


def test_astm::type_constructor_args():
    sig = inspect.signature(astm::Type.__init__)
    params = list(sig.parameters.keys())
    assert "isConst" in params, "Missing parameter 'isConst'"
    assert "isVolatile" in params, "Missing parameter 'isVolatile'"

def test_astm::type_has_isConst():
    assert hasattr(astm::Type, "isConst")
    descriptor = None
    for klass in astm::Type.__mro__:
        if "isConst" in klass.__dict__:
            descriptor = klass.__dict__["isConst"]
            break
    assert isinstance(descriptor, property)

def test_astm::type_has_isVolatile():
    assert hasattr(astm::Type, "isVolatile")
    descriptor = None
    for klass in astm::Type.__mro__:
        if "isVolatile" in klass.__dict__:
            descriptor = klass.__dict__["isVolatile"]
            break
    assert isinstance(descriptor, property)



def test_preprocessorelement_is_not_abstract():
    assert not inspect.isabstract(PreprocessorElement)


def test_preprocessorelement_constructor_exists():
    assert callable(PreprocessorElement.__init__)


def test_preprocessorelement_constructor_args():
    sig = inspect.signature(PreprocessorElement.__init__)
    params = list(sig.parameters.keys())



def test_astm::macrodefinition_is_not_abstract():
    assert not inspect.isabstract(astm::MacroDefinition)


def test_astm::macrodefinition_constructor_exists():
    assert callable(astm::MacroDefinition.__init__)


def test_astm::macrodefinition_constructor_args():
    sig = inspect.signature(astm::MacroDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "macroName" in params, "Missing parameter 'macroName'"
    assert "body" in params, "Missing parameter 'body'"

def test_astm::macrodefinition_has_macroName():
    assert hasattr(astm::MacroDefinition, "macroName")
    descriptor = None
    for klass in astm::MacroDefinition.__mro__:
        if "macroName" in klass.__dict__:
            descriptor = klass.__dict__["macroName"]
            break
    assert isinstance(descriptor, property)

def test_astm::macrodefinition_has_body():
    assert hasattr(astm::MacroDefinition, "body")
    descriptor = None
    for klass in astm::MacroDefinition.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_astm::macrocall_is_not_abstract():
    assert not inspect.isabstract(astm::MacroCall)


def test_astm::macrocall_constructor_exists():
    assert callable(astm::MacroCall.__init__)


def test_astm::macrocall_constructor_args():
    sig = inspect.signature(astm::MacroCall.__init__)
    params = list(sig.parameters.keys())



def test_astm::comment_is_not_abstract():
    assert not inspect.isabstract(astm::Comment)


def test_astm::comment_constructor_exists():
    assert callable(astm::Comment.__init__)


def test_astm::comment_constructor_args():
    sig = inspect.signature(astm::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_astm::comment_has_text():
    assert hasattr(astm::Comment, "text")
    descriptor = None
    for klass in astm::Comment.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_astm::includeunit_is_not_abstract():
    assert not inspect.isabstract(astm::IncludeUnit)


def test_astm::includeunit_constructor_exists():
    assert callable(astm::IncludeUnit.__init__)


def test_astm::includeunit_constructor_args():
    sig = inspect.signature(astm::IncludeUnit.__init__)
    params = list(sig.parameters.keys())



def test_astm::labeltype_is_not_abstract():
    assert not inspect.isabstract(astm::LabelType)


def test_astm::labeltype_constructor_exists():
    assert callable(astm::LabelType.__init__)


def test_astm::labeltype_constructor_args():
    sig = inspect.signature(astm::LabelType.__init__)
    params = list(sig.parameters.keys())



def test_astm::namespacetype_is_not_abstract():
    assert not inspect.isabstract(astm::NameSpaceType)


def test_astm::namespacetype_constructor_exists():
    assert callable(astm::NameSpaceType.__init__)


def test_astm::namespacetype_constructor_args():
    sig = inspect.signature(astm::NameSpaceType.__init__)
    params = list(sig.parameters.keys())



def test_astm::aggregatetype_is_not_abstract():
    assert not inspect.isabstract(astm::AggregateType)


def test_astm::aggregatetype_constructor_exists():
    assert callable(astm::AggregateType.__init__)


def test_astm::aggregatetype_constructor_args():
    sig = inspect.signature(astm::AggregateType.__init__)
    params = list(sig.parameters.keys())



def test_astm::namedtype_is_not_abstract():
    assert not inspect.isabstract(astm::NamedType)


def test_astm::namedtype_constructor_exists():
    assert callable(astm::NamedType.__init__)


def test_astm::namedtype_constructor_args():
    sig = inspect.signature(astm::NamedType.__init__)
    params = list(sig.parameters.keys())



def test_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm::aggregatetypedefinition_is_not_abstract():
    assert not inspect.isabstract(astm::AggregateTypeDefinition)


def test_astm::aggregatetypedefinition_constructor_exists():
    assert callable(astm::AggregateTypeDefinition.__init__)


def test_astm::aggregatetypedefinition_constructor_args():
    sig = inspect.signature(astm::AggregateTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm::namedtypedefinition_is_not_abstract():
    assert not inspect.isabstract(astm::NamedTypeDefinition)


def test_astm::namedtypedefinition_constructor_exists():
    assert callable(astm::NamedTypeDefinition.__init__)


def test_astm::namedtypedefinition_constructor_args():
    sig = inspect.signature(astm::NamedTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_datadefinition_is_not_abstract():
    assert not inspect.isabstract(DataDefinition)


def test_datadefinition_constructor_exists():
    assert callable(DataDefinition.__init__)


def test_datadefinition_constructor_args():
    sig = inspect.signature(DataDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm::variabledefinition_is_not_abstract():
    assert not inspect.isabstract(astm::VariableDefinition)


def test_astm::variabledefinition_constructor_exists():
    assert callable(astm::VariableDefinition.__init__)


def test_astm::variabledefinition_constructor_args():
    sig = inspect.signature(astm::VariableDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm::bitfielddefinition_is_not_abstract():
    assert not inspect.isabstract(astm::BitFieldDefinition)


def test_astm::bitfielddefinition_constructor_exists():
    assert callable(astm::BitFieldDefinition.__init__)


def test_astm::bitfielddefinition_constructor_args():
    sig = inspect.signature(astm::BitFieldDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm::expression_is_not_abstract():
    assert not inspect.isabstract(astm::Expression)


def test_astm::expression_constructor_exists():
    assert callable(astm::Expression.__init__)


def test_astm::expression_constructor_args():
    sig = inspect.signature(astm::Expression.__init__)
    params = list(sig.parameters.keys())



def test_astm::functionscope_is_not_abstract():
    assert not inspect.isabstract(astm::FunctionScope)


def test_astm::functionscope_constructor_exists():
    assert callable(astm::FunctionScope.__init__)


def test_astm::functionscope_constructor_args():
    sig = inspect.signature(astm::FunctionScope.__init__)
    params = list(sig.parameters.keys())



def test_astm::statement_is_not_abstract():
    assert not inspect.isabstract(astm::Statement)


def test_astm::statement_constructor_exists():
    assert callable(astm::Statement.__init__)


def test_astm::statement_constructor_args():
    sig = inspect.signature(astm::Statement.__init__)
    params = list(sig.parameters.keys())



def test_astm::formalparameterdefinition_is_not_abstract():
    assert not inspect.isabstract(astm::FormalParameterDefinition)


def test_astm::formalparameterdefinition_constructor_exists():
    assert callable(astm::FormalParameterDefinition.__init__)


def test_astm::formalparameterdefinition_constructor_args():
    sig = inspect.signature(astm::FormalParameterDefinition.__init__)
    params = list(sig.parameters.keys())



def test_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_astm::entrydefinition_is_not_abstract():
    assert not inspect.isabstract(astm::EntryDefinition)


def test_astm::entrydefinition_constructor_exists():
    assert callable(astm::EntryDefinition.__init__)


def test_astm::entrydefinition_constructor_args():
    sig = inspect.signature(astm::EntryDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm::datadefinition_is_not_abstract():
    assert not inspect.isabstract(astm::DataDefinition)


def test_astm::datadefinition_constructor_exists():
    assert callable(astm::DataDefinition.__init__)


def test_astm::datadefinition_constructor_args():
    sig = inspect.signature(astm::DataDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "isMutable" in params, "Missing parameter 'isMutable'"

def test_astm::datadefinition_has_isMutable():
    assert hasattr(astm::DataDefinition, "isMutable")
    descriptor = None
    for klass in astm::DataDefinition.__mro__:
        if "isMutable" in klass.__dict__:
            descriptor = klass.__dict__["isMutable"]
            break
    assert isinstance(descriptor, property)



def test_astm::enumliteraldefinition_is_not_abstract():
    assert not inspect.isabstract(astm::EnumLiteralDefinition)


def test_astm::enumliteraldefinition_constructor_exists():
    assert callable(astm::EnumLiteralDefinition.__init__)


def test_astm::enumliteraldefinition_constructor_args():
    sig = inspect.signature(astm::EnumLiteralDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm::functiondefinition_is_not_abstract():
    assert not inspect.isabstract(astm::FunctionDefinition)


def test_astm::functiondefinition_constructor_exists():
    assert callable(astm::FunctionDefinition.__init__)


def test_astm::functiondefinition_constructor_args():
    sig = inspect.signature(astm::FunctionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm::functionmemberattributes_is_not_abstract():
    assert not inspect.isabstract(astm::FunctionMemberAttributes)


def test_astm::functionmemberattributes_constructor_exists():
    assert callable(astm::FunctionMemberAttributes.__init__)


def test_astm::functionmemberattributes_constructor_args():
    sig = inspect.signature(astm::FunctionMemberAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "isThisConst" in params, "Missing parameter 'isThisConst'"
    assert "isInline" in params, "Missing parameter 'isInline'"
    assert "isFriend" in params, "Missing parameter 'isFriend'"

def test_astm::functionmemberattributes_has_isThisConst():
    assert hasattr(astm::FunctionMemberAttributes, "isThisConst")
    descriptor = None
    for klass in astm::FunctionMemberAttributes.__mro__:
        if "isThisConst" in klass.__dict__:
            descriptor = klass.__dict__["isThisConst"]
            break
    assert isinstance(descriptor, property)

def test_astm::functionmemberattributes_has_isInline():
    assert hasattr(astm::FunctionMemberAttributes, "isInline")
    descriptor = None
    for klass in astm::FunctionMemberAttributes.__mro__:
        if "isInline" in klass.__dict__:
            descriptor = klass.__dict__["isInline"]
            break
    assert isinstance(descriptor, property)

def test_astm::functionmemberattributes_has_isFriend():
    assert hasattr(astm::FunctionMemberAttributes, "isFriend")
    descriptor = None
    for klass in astm::FunctionMemberAttributes.__mro__:
        if "isFriend" in klass.__dict__:
            descriptor = klass.__dict__["isFriend"]
            break
    assert isinstance(descriptor, property)



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_astm::formalparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(astm::FormalParameterDeclaration)


def test_astm::formalparameterdeclaration_constructor_exists():
    assert callable(astm::FormalParameterDeclaration.__init__)


def test_astm::formalparameterdeclaration_constructor_args():
    sig = inspect.signature(astm::FormalParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_astm::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(astm::VariableDeclaration)


def test_astm::variabledeclaration_constructor_exists():
    assert callable(astm::VariableDeclaration.__init__)


def test_astm::variabledeclaration_constructor_args():
    sig = inspect.signature(astm::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isMutable" in params, "Missing parameter 'isMutable'"

def test_astm::variabledeclaration_has_isMutable():
    assert hasattr(astm::VariableDeclaration, "isMutable")
    descriptor = None
    for klass in astm::VariableDeclaration.__mro__:
        if "isMutable" in klass.__dict__:
            descriptor = klass.__dict__["isMutable"]
            break
    assert isinstance(descriptor, property)



def test_astm::functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(astm::FunctionDeclaration)


def test_astm::functiondeclaration_constructor_exists():
    assert callable(astm::FunctionDeclaration.__init__)


def test_astm::functiondeclaration_constructor_args():
    sig = inspect.signature(astm::FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_astm::typereference_is_not_abstract():
    assert not inspect.isabstract(astm::TypeReference)


def test_astm::typereference_constructor_exists():
    assert callable(astm::TypeReference.__init__)


def test_astm::typereference_constructor_args():
    sig = inspect.signature(astm::TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_declarationordefinition_is_not_abstract():
    assert not inspect.isabstract(DeclarationOrDefinition)


def test_declarationordefinition_constructor_exists():
    assert callable(DeclarationOrDefinition.__init__)


def test_declarationordefinition_constructor_args():
    sig = inspect.signature(DeclarationOrDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm::declaration_is_not_abstract():
    assert not inspect.isabstract(astm::Declaration)


def test_astm::declaration_constructor_exists():
    assert callable(astm::Declaration.__init__)


def test_astm::declaration_constructor_args():
    sig = inspect.signature(astm::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_astm::definition_is_not_abstract():
    assert not inspect.isabstract(astm::Definition)


def test_astm::definition_constructor_exists():
    assert callable(astm::Definition.__init__)


def test_astm::definition_constructor_args():
    sig = inspect.signature(astm::Definition.__init__)
    params = list(sig.parameters.keys())



def test_definitionobject_is_not_abstract():
    assert not inspect.isabstract(DefinitionObject)


def test_definitionobject_constructor_exists():
    assert callable(DefinitionObject.__init__)


def test_definitionobject_constructor_args():
    sig = inspect.signature(DefinitionObject.__init__)
    params = list(sig.parameters.keys())



def test_astm::namespacedefinition_is_not_abstract():
    assert not inspect.isabstract(astm::NameSpaceDefinition)


def test_astm::namespacedefinition_constructor_exists():
    assert callable(astm::NameSpaceDefinition.__init__)


def test_astm::namespacedefinition_constructor_args():
    sig = inspect.signature(astm::NameSpaceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm::labeldefinition_is_not_abstract():
    assert not inspect.isabstract(astm::LabelDefinition)


def test_astm::labeldefinition_constructor_exists():
    assert callable(astm::LabelDefinition.__init__)


def test_astm::labeldefinition_constructor_args():
    sig = inspect.signature(astm::LabelDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm::typedefinition_is_not_abstract():
    assert not inspect.isabstract(astm::TypeDefinition)


def test_astm::typedefinition_constructor_exists():
    assert callable(astm::TypeDefinition.__init__)


def test_astm::typedefinition_constructor_args():
    sig = inspect.signature(astm::TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm::declarationordefinition_is_not_abstract():
    assert not inspect.isabstract(astm::DeclarationOrDefinition)


def test_astm::declarationordefinition_constructor_exists():
    assert callable(astm::DeclarationOrDefinition.__init__)


def test_astm::declarationordefinition_constructor_args():
    sig = inspect.signature(astm::DeclarationOrDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "isRegister" in params, "Missing parameter 'isRegister'"
    assert "linkageSpecifier" in params, "Missing parameter 'linkageSpecifier'"

def test_astm::declarationordefinition_has_isRegister():
    assert hasattr(astm::DeclarationOrDefinition, "isRegister")
    descriptor = None
    for klass in astm::DeclarationOrDefinition.__mro__:
        if "isRegister" in klass.__dict__:
            descriptor = klass.__dict__["isRegister"]
            break
    assert isinstance(descriptor, property)

def test_astm::declarationordefinition_has_linkageSpecifier():
    assert hasattr(astm::DeclarationOrDefinition, "linkageSpecifier")
    descriptor = None
    for klass in astm::DeclarationOrDefinition.__mro__:
        if "linkageSpecifier" in klass.__dict__:
            descriptor = klass.__dict__["linkageSpecifier"]
            break
    assert isinstance(descriptor, property)



def test_astm::programscope_is_not_abstract():
    assert not inspect.isabstract(astm::ProgramScope)


def test_astm::programscope_constructor_exists():
    assert callable(astm::ProgramScope.__init__)


def test_astm::programscope_constructor_args():
    sig = inspect.signature(astm::ProgramScope.__init__)
    params = list(sig.parameters.keys())



def test_othersyntaxobject_is_not_abstract():
    assert not inspect.isabstract(OtherSyntaxObject)


def test_othersyntaxobject_constructor_exists():
    assert callable(OtherSyntaxObject.__init__)


def test_othersyntaxobject_constructor_args():
    sig = inspect.signature(OtherSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_astm::switchcase_is_not_abstract():
    assert not inspect.isabstract(astm::SwitchCase)


def test_astm::switchcase_constructor_exists():
    assert callable(astm::SwitchCase.__init__)


def test_astm::switchcase_constructor_args():
    sig = inspect.signature(astm::SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_astm::functionmemberattribute_is_not_abstract():
    assert not inspect.isabstract(astm::FunctionMemberAttribute)


def test_astm::functionmemberattribute_constructor_exists():
    assert callable(astm::FunctionMemberAttribute.__init__)


def test_astm::functionmemberattribute_constructor_args():
    sig = inspect.signature(astm::FunctionMemberAttribute.__init__)
    params = list(sig.parameters.keys())



def test_astm::name_is_not_abstract():
    assert not inspect.isabstract(astm::Name)


def test_astm::name_constructor_exists():
    assert callable(astm::Name.__init__)


def test_astm::name_constructor_args():
    sig = inspect.signature(astm::Name.__init__)
    params = list(sig.parameters.keys())
    assert "nameString" in params, "Missing parameter 'nameString'"

def test_astm::name_has_nameString():
    assert hasattr(astm::Name, "nameString")
    descriptor = None
    for klass in astm::Name.__mro__:
        if "nameString" in klass.__dict__:
            descriptor = klass.__dict__["nameString"]
            break
    assert isinstance(descriptor, property)



def test_astm::virtualspecification_is_not_abstract():
    assert not inspect.isabstract(astm::VirtualSpecification)


def test_astm::virtualspecification_constructor_exists():
    assert callable(astm::VirtualSpecification.__init__)


def test_astm::virtualspecification_constructor_args():
    sig = inspect.signature(astm::VirtualSpecification.__init__)
    params = list(sig.parameters.keys())



def test_astm::dimension_is_not_abstract():
    assert not inspect.isabstract(astm::Dimension)


def test_astm::dimension_constructor_exists():
    assert callable(astm::Dimension.__init__)


def test_astm::dimension_constructor_args():
    sig = inspect.signature(astm::Dimension.__init__)
    params = list(sig.parameters.keys())



def test_astm::derivesfrom_is_not_abstract():
    assert not inspect.isabstract(astm::DerivesFrom)


def test_astm::derivesfrom_constructor_exists():
    assert callable(astm::DerivesFrom.__init__)


def test_astm::derivesfrom_constructor_args():
    sig = inspect.signature(astm::DerivesFrom.__init__)
    params = list(sig.parameters.keys())
    assert "isVirtual" in params, "Missing parameter 'isVirtual'"

def test_astm::derivesfrom_has_isVirtual():
    assert hasattr(astm::DerivesFrom, "isVirtual")
    descriptor = None
    for klass in astm::DerivesFrom.__mro__:
        if "isVirtual" in klass.__dict__:
            descriptor = klass.__dict__["isVirtual"]
            break
    assert isinstance(descriptor, property)



def test_astm::catchblock_is_not_abstract():
    assert not inspect.isabstract(astm::CatchBlock)


def test_astm::catchblock_constructor_exists():
    assert callable(astm::CatchBlock.__init__)


def test_astm::catchblock_constructor_args():
    sig = inspect.signature(astm::CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_astm::annotationexpression_is_not_abstract():
    assert not inspect.isabstract(astm::AnnotationExpression)


def test_astm::annotationexpression_constructor_exists():
    assert callable(astm::AnnotationExpression.__init__)


def test_astm::annotationexpression_constructor_args():
    sig = inspect.signature(astm::AnnotationExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::preprocessorelement_is_not_abstract():
    assert not inspect.isabstract(astm::PreprocessorElement)


def test_astm::preprocessorelement_constructor_exists():
    assert callable(astm::PreprocessorElement.__init__)


def test_astm::preprocessorelement_constructor_args():
    sig = inspect.signature(astm::PreprocessorElement.__init__)
    params = list(sig.parameters.keys())



def test_gastmobject_is_not_abstract():
    assert not inspect.isabstract(GASTMObject)


def test_gastmobject_constructor_exists():
    assert callable(GASTMObject.__init__)


def test_gastmobject_constructor_args():
    sig = inspect.signature(GASTMObject.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastmsyntaxobject_is_not_abstract():
    assert not inspect.isabstract(astm::GASTMSyntaxObject)


def test_astm::gastmsyntaxobject_constructor_exists():
    assert callable(astm::GASTMSyntaxObject.__init__)


def test_astm::gastmsyntaxobject_constructor_args():
    sig = inspect.signature(astm::GASTMSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_astm::definitionobject_is_not_abstract():
    assert not inspect.isabstract(astm::DefinitionObject)


def test_astm::definitionobject_constructor_exists():
    assert callable(astm::DefinitionObject.__init__)


def test_astm::definitionobject_constructor_args():
    sig = inspect.signature(astm::DefinitionObject.__init__)
    params = list(sig.parameters.keys())



def test_astm::globalscope_is_not_abstract():
    assert not inspect.isabstract(astm::GlobalScope)


def test_astm::globalscope_constructor_exists():
    assert callable(astm::GlobalScope.__init__)


def test_astm::globalscope_constructor_args():
    sig = inspect.signature(astm::GlobalScope.__init__)
    params = list(sig.parameters.keys())



def test_astm::compilationunit_is_not_abstract():
    assert not inspect.isabstract(astm::CompilationUnit)


def test_astm::compilationunit_constructor_exists():
    assert callable(astm::CompilationUnit.__init__)


def test_astm::compilationunit_constructor_args():
    sig = inspect.signature(astm::CompilationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"

def test_astm::compilationunit_has_language():
    assert hasattr(astm::CompilationUnit, "language")
    descriptor = None
    for klass in astm::CompilationUnit.__mro__:
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



def test_astm::scope_is_not_abstract():
    assert not inspect.isabstract(astm::Scope)


def test_astm::scope_constructor_exists():
    assert callable(astm::Scope.__init__)


def test_astm::scope_constructor_args():
    sig = inspect.signature(astm::Scope.__init__)
    params = list(sig.parameters.keys())



def test_astm::project_is_not_abstract():
    assert not inspect.isabstract(astm::Project)


def test_astm::project_constructor_exists():
    assert callable(astm::Project.__init__)


def test_astm::project_constructor_args():
    sig = inspect.signature(astm::Project.__init__)
    params = list(sig.parameters.keys())



def test_gastmsourceobject_is_not_abstract():
    assert not inspect.isabstract(GASTMSourceObject)


def test_gastmsourceobject_constructor_exists():
    assert callable(GASTMSourceObject.__init__)


def test_gastmsourceobject_constructor_args():
    sig = inspect.signature(GASTMSourceObject.__init__)
    params = list(sig.parameters.keys())



def test_astm::sourcelocation_is_not_abstract():
    assert not inspect.isabstract(astm::SourceLocation)


def test_astm::sourcelocation_constructor_exists():
    assert callable(astm::SourceLocation.__init__)


def test_astm::sourcelocation_constructor_args():
    sig = inspect.signature(astm::SourceLocation.__init__)
    params = list(sig.parameters.keys())
    assert "startLine" in params, "Missing parameter 'startLine'"
    assert "endColumn" in params, "Missing parameter 'endColumn'"
    assert "endLine" in params, "Missing parameter 'endLine'"
    assert "startColumn" in params, "Missing parameter 'startColumn'"

def test_astm::sourcelocation_has_startLine():
    assert hasattr(astm::SourceLocation, "startLine")
    descriptor = None
    for klass in astm::SourceLocation.__mro__:
        if "startLine" in klass.__dict__:
            descriptor = klass.__dict__["startLine"]
            break
    assert isinstance(descriptor, property)

def test_astm::sourcelocation_has_endColumn():
    assert hasattr(astm::SourceLocation, "endColumn")
    descriptor = None
    for klass in astm::SourceLocation.__mro__:
        if "endColumn" in klass.__dict__:
            descriptor = klass.__dict__["endColumn"]
            break
    assert isinstance(descriptor, property)

def test_astm::sourcelocation_has_endLine():
    assert hasattr(astm::SourceLocation, "endLine")
    descriptor = None
    for klass in astm::SourceLocation.__mro__:
        if "endLine" in klass.__dict__:
            descriptor = klass.__dict__["endLine"]
            break
    assert isinstance(descriptor, property)

def test_astm::sourcelocation_has_startColumn():
    assert hasattr(astm::SourceLocation, "startColumn")
    descriptor = None
    for klass in astm::SourceLocation.__mro__:
        if "startColumn" in klass.__dict__:
            descriptor = klass.__dict__["startColumn"]
            break
    assert isinstance(descriptor, property)



def test_astm::sourcefile_is_not_abstract():
    assert not inspect.isabstract(astm::SourceFile)


def test_astm::sourcefile_constructor_exists():
    assert callable(astm::SourceFile.__init__)


def test_astm::sourcefile_constructor_args():
    sig = inspect.signature(astm::SourceFile.__init__)
    params = list(sig.parameters.keys())
    assert "pathName" in params, "Missing parameter 'pathName'"

def test_astm::sourcefile_has_pathName():
    assert hasattr(astm::SourceFile, "pathName")
    descriptor = None
    for klass in astm::SourceFile.__mro__:
        if "pathName" in klass.__dict__:
            descriptor = klass.__dict__["pathName"]
            break
    assert isinstance(descriptor, property)



def test_astm::actualparameter_is_not_abstract():
    assert not inspect.isabstract(astm::ActualParameter)


def test_astm::actualparameter_constructor_exists():
    assert callable(astm::ActualParameter.__init__)


def test_astm::actualparameter_constructor_args():
    sig = inspect.signature(astm::ActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_astm::binaryoperator_is_not_abstract():
    assert not inspect.isabstract(astm::BinaryOperator)


def test_astm::binaryoperator_constructor_exists():
    assert callable(astm::BinaryOperator.__init__)


def test_astm::binaryoperator_constructor_args():
    sig = inspect.signature(astm::BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_astm::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(astm::UnaryOperator)


def test_astm::unaryoperator_constructor_exists():
    assert callable(astm::UnaryOperator.__init__)


def test_astm::unaryoperator_constructor_args():
    sig = inspect.signature(astm::UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_astm::accesskind_is_not_abstract():
    assert not inspect.isabstract(astm::AccessKind)


def test_astm::accesskind_constructor_exists():
    assert callable(astm::AccessKind.__init__)


def test_astm::accesskind_constructor_args():
    sig = inspect.signature(astm::AccessKind.__init__)
    params = list(sig.parameters.keys())



def test_astm::datatype_is_not_abstract():
    assert not inspect.isabstract(astm::DataType)


def test_astm::datatype_constructor_exists():
    assert callable(astm::DataType.__init__)


def test_astm::datatype_constructor_args():
    sig = inspect.signature(astm::DataType.__init__)
    params = list(sig.parameters.keys())



def test_astm::storagespecification_is_not_abstract():
    assert not inspect.isabstract(astm::StorageSpecification)


def test_astm::storagespecification_constructor_exists():
    assert callable(astm::StorageSpecification.__init__)


def test_astm::storagespecification_constructor_args():
    sig = inspect.signature(astm::StorageSpecification.__init__)
    params = list(sig.parameters.keys())



def test_astm::othersyntaxobject_is_not_abstract():
    assert not inspect.isabstract(astm::OtherSyntaxObject)


def test_astm::othersyntaxobject_constructor_exists():
    assert callable(astm::OtherSyntaxObject.__init__)


def test_astm::othersyntaxobject_constructor_args():
    sig = inspect.signature(astm::OtherSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastmsemanticobject_is_not_abstract():
    assert not inspect.isabstract(astm::GASTMSemanticObject)


def test_astm::gastmsemanticobject_constructor_exists():
    assert callable(astm::GASTMSemanticObject.__init__)


def test_astm::gastmsemanticobject_constructor_args():
    sig = inspect.signature(astm::GASTMSemanticObject.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastmsourceobject_is_not_abstract():
    assert not inspect.isabstract(astm::GASTMSourceObject)


def test_astm::gastmsourceobject_constructor_exists():
    assert callable(astm::GASTMSourceObject.__init__)


def test_astm::gastmsourceobject_constructor_args():
    sig = inspect.signature(astm::GASTMSourceObject.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastmobject_is_not_abstract():
    assert not inspect.isabstract(astm::GASTMObject)


def test_astm::gastmobject_constructor_exists():
    assert callable(astm::GASTMObject.__init__)


def test_astm::gastmobject_constructor_args():
    sig = inspect.signature(astm::GASTMObject.__init__)
    params = list(sig.parameters.keys())



def test_astm::divide_is_not_abstract():
    assert not inspect.isabstract(astm::Divide)


def test_astm::divide_constructor_exists():
    assert callable(astm::Divide.__init__)


def test_astm::divide_constructor_args():
    sig = inspect.signature(astm::Divide.__init__)
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
ClassType_strategy = st.builds(
    ClassType,
)
astm::SpecificClassType_strategy = st.builds(
    astm::SpecificClassType,
    imports=
        safe_text,
    package=
        safe_text
)
ActualParameterExpression_strategy = st.builds(
    ActualParameterExpression,
)
astm::ByReferenceActualParameterExpression_strategy = st.builds(
    astm::ByReferenceActualParameterExpression,
)
astm::ByValueActualParameterExpression_strategy = st.builds(
    astm::ByValueActualParameterExpression,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
astm::Not_strategy = st.builds(
    astm::Not,
)
astm::Deref_strategy = st.builds(
    astm::Deref,
)
astm::BitNot_strategy = st.builds(
    astm::BitNot,
)
astm::Decrement_strategy = st.builds(
    astm::Decrement,
)
astm::Increment_strategy = st.builds(
    astm::Increment,
)
astm::AddressOf_strategy = st.builds(
    astm::AddressOf,
)
astm::PostIncrement_strategy = st.builds(
    astm::PostIncrement,
)
astm::Negate_strategy = st.builds(
    astm::Negate,
)
astm::PostDecrement_strategy = st.builds(
    astm::PostDecrement,
)
astm::UnaryPlus_strategy = st.builds(
    astm::UnaryPlus,
)
Literal_strategy = st.builds(
    Literal,
)
astm::CharLiteral_strategy = st.builds(
    astm::CharLiteral,
)
astm::StringLiteral_strategy = st.builds(
    astm::StringLiteral,
)
astm::BitLiteral_strategy = st.builds(
    astm::BitLiteral,
)
astm::RealLiteral_strategy = st.builds(
    astm::RealLiteral,
)
astm::BooleanLiteral_strategy = st.builds(
    astm::BooleanLiteral,
)
astm::IntegerlLiteral_strategy = st.builds(
    astm::IntegerlLiteral,
)
QualifiedIdentifierReference_strategy = st.builds(
    QualifiedIdentifierReference,
)
astm::QualifiedOverData_strategy = st.builds(
    astm::QualifiedOverData,
)
astm::QualifiedOverPointer_strategy = st.builds(
    astm::QualifiedOverPointer,
)
ForStatement_strategy = st.builds(
    ForStatement,
)
astm::ForCheckAfterStatement_strategy = st.builds(
    astm::ForCheckAfterStatement,
)
astm::ForCheckBeforeStatement_strategy = st.builds(
    astm::ForCheckBeforeStatement,
)
AccessKind_strategy = st.builds(
    AccessKind,
)
astm::Private_strategy = st.builds(
    astm::Private,
)
astm::Protected_strategy = st.builds(
    astm::Protected,
)
astm::Public_strategy = st.builds(
    astm::Public,
)
FormalParameterType_strategy = st.builds(
    FormalParameterType,
)
astm::ByReferenceFormalParameterType_strategy = st.builds(
    astm::ByReferenceFormalParameterType,
)
astm::ByValueFormalParameterType_strategy = st.builds(
    astm::ByValueFormalParameterType,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
astm::String_strategy = st.builds(
    astm::String,
)
astm::Double_strategy = st.builds(
    astm::Double,
)
astm::Byte_strategy = st.builds(
    astm::Byte,
)
astm::WideCharacter_strategy = st.builds(
    astm::WideCharacter,
)
astm::Integer_strategy = st.builds(
    astm::Integer,
)
astm::Float_strategy = st.builds(
    astm::Float,
)
astm::LongInteger_strategy = st.builds(
    astm::LongInteger,
)
astm::Boolean_strategy = st.builds(
    astm::Boolean,
)
astm::ShortInteger_strategy = st.builds(
    astm::ShortInteger,
)
astm::LongDouble_strategy = st.builds(
    astm::LongDouble,
)
astm::Character_strategy = st.builds(
    astm::Character,
)
astm::Void_strategy = st.builds(
    astm::Void,
)
VirtualSpecification_strategy = st.builds(
    VirtualSpecification,
)
astm::NonVirtual_strategy = st.builds(
    astm::NonVirtual,
)
astm::PureVirtual_strategy = st.builds(
    astm::PureVirtual,
)
astm::Virtual_strategy = st.builds(
    astm::Virtual,
)
StorageSpecification_strategy = st.builds(
    StorageSpecification,
)
astm::NoDef_strategy = st.builds(
    astm::NoDef,
)
astm::PerClassMember_strategy = st.builds(
    astm::PerClassMember,
)
astm::FunctionPersistent_strategy = st.builds(
    astm::FunctionPersistent,
)
astm::FileLocal_strategy = st.builds(
    astm::FileLocal,
)
astm::External_strategy = st.builds(
    astm::External,
)
Scope_strategy = st.builds(
    Scope,
)
ActualParameter_strategy = st.builds(
    ActualParameter,
)
astm::MissingActualParameter_strategy = st.builds(
    astm::MissingActualParameter,
)
astm::ActualParameterExpression_strategy = st.builds(
    astm::ActualParameterExpression,
)
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
astm::Exponent_strategy = st.builds(
    astm::Exponent,
)
astm::Assign_strategy = st.builds(
    astm::Assign,
)
astm::BitAnd_strategy = st.builds(
    astm::BitAnd,
)
astm::Add_strategy = st.builds(
    astm::Add,
)
astm::NotGreater_strategy = st.builds(
    astm::NotGreater,
)
astm::Or_strategy = st.builds(
    astm::Or,
)
astm::And_strategy = st.builds(
    astm::And,
)
astm::BitRightShift_strategy = st.builds(
    astm::BitRightShift,
)
astm::NotLess_strategy = st.builds(
    astm::NotLess,
)
astm::Modulus_strategy = st.builds(
    astm::Modulus,
)
astm::Multiply_strategy = st.builds(
    astm::Multiply,
)
astm::Equal_strategy = st.builds(
    astm::Equal,
)
astm::Subtract_strategy = st.builds(
    astm::Subtract,
)
astm::Less_strategy = st.builds(
    astm::Less,
)
astm::NotEqual_strategy = st.builds(
    astm::NotEqual,
)
astm::Greater_strategy = st.builds(
    astm::Greater,
)
astm::BitLeftShift_strategy = st.builds(
    astm::BitLeftShift,
)
astm::BitOr_strategy = st.builds(
    astm::BitOr,
)
astm::BitXor_strategy = st.builds(
    astm::BitXor,
)
astm::OperatorAssign_strategy = st.builds(
    astm::OperatorAssign,
)
NameReference_strategy = st.builds(
    NameReference,
)
astm::IdentifierReference_strategy = st.builds(
    astm::IdentifierReference,
)
astm::TypeQualifiedIdentifierReference_strategy = st.builds(
    astm::TypeQualifiedIdentifierReference,
)
astm::QualifiedIdentifierReference_strategy = st.builds(
    astm::QualifiedIdentifierReference,
)
Expression_strategy = st.builds(
    Expression,
)
astm::UnaryExpression_strategy = st.builds(
    astm::UnaryExpression,
)
astm::BinaryExpression_strategy = st.builds(
    astm::BinaryExpression,
)
astm::NewExpression_strategy = st.builds(
    astm::NewExpression,
)
astm::ArrayAccess_strategy = st.builds(
    astm::ArrayAccess,
)
astm::FunctionCallExpression_strategy = st.builds(
    astm::FunctionCallExpression,
)
astm::Literal_strategy = st.builds(
    astm::Literal,
    value=
        safe_text
)
astm::AggregateExpression_strategy = st.builds(
    astm::AggregateExpression,
)
astm::CastExpression_strategy = st.builds(
    astm::CastExpression,
)
astm::RangeExpression_strategy = st.builds(
    astm::RangeExpression,
)
astm::ConditionalExpression_strategy = st.builds(
    astm::ConditionalExpression,
)
astm::NameReference_strategy = st.builds(
    astm::NameReference,
)
CatchBlock_strategy = st.builds(
    CatchBlock,
)
astm::VariableCatchBlock_strategy = st.builds(
    astm::VariableCatchBlock,
)
astm::TypesCatchBlock_strategy = st.builds(
    astm::TypesCatchBlock,
)
LoopStatement_strategy = st.builds(
    LoopStatement,
)
astm::DoWhileStatement_strategy = st.builds(
    astm::DoWhileStatement,
)
astm::WhileStatement_strategy = st.builds(
    astm::WhileStatement,
)
SwitchCase_strategy = st.builds(
    SwitchCase,
)
astm::DefaultBlock_strategy = st.builds(
    astm::DefaultBlock,
)
astm::CaseBlock_strategy = st.builds(
    astm::CaseBlock,
)
astm::BlockScope_strategy = st.builds(
    astm::BlockScope,
)
astm::ForStatement_strategy = st.builds(
    astm::ForStatement,
)
astm::LabelAccess_strategy = st.builds(
    astm::LabelAccess,
)
Statement_strategy = st.builds(
    Statement,
)
astm::SwitchStatement_strategy = st.builds(
    astm::SwitchStatement,
)
astm::TryStatement_strategy = st.builds(
    astm::TryStatement,
)
astm::ThrowStatement_strategy = st.builds(
    astm::ThrowStatement,
)
astm::EmptyStatement_strategy = st.builds(
    astm::EmptyStatement,
)
astm::ExpressionStatement_strategy = st.builds(
    astm::ExpressionStatement,
)
astm::ReturnStatement_strategy = st.builds(
    astm::ReturnStatement,
)
astm::BreakStatement_strategy = st.builds(
    astm::BreakStatement,
)
astm::DeclarationOrDefinitionStatement_strategy = st.builds(
    astm::DeclarationOrDefinitionStatement,
)
astm::BlockStatement_strategy = st.builds(
    astm::BlockStatement,
)
astm::IfStatement_strategy = st.builds(
    astm::IfStatement,
)
astm::ContinueStatement_strategy = st.builds(
    astm::ContinueStatement,
)
astm::JumpStatement_strategy = st.builds(
    astm::JumpStatement,
)
astm::LabeledStatement_strategy = st.builds(
    astm::LabeledStatement,
)
astm::TerminateStatement_strategy = st.builds(
    astm::TerminateStatement,
)
astm::LoopStatement_strategy = st.builds(
    astm::LoopStatement,
)
astm::DeleteStatement_strategy = st.builds(
    astm::DeleteStatement,
)
TypeReference_strategy = st.builds(
    TypeReference,
)
astm::NamedTypeReference_strategy = st.builds(
    astm::NamedTypeReference,
)
astm::UnnamedTypeReference_strategy = st.builds(
    astm::UnnamedTypeReference,
)
AggregateType_strategy = st.builds(
    AggregateType,
)
astm::StructureType_strategy = st.builds(
    astm::StructureType,
)
astm::AnnotationType_strategy = st.builds(
    astm::AnnotationType,
)
astm::UnionType_strategy = st.builds(
    astm::UnionType,
)
astm::ClassType_strategy = st.builds(
    astm::ClassType,
)
Type_strategy = st.builds(
    Type,
)
astm::FunctionType_strategy = st.builds(
    astm::FunctionType,
)
ConstructedType_strategy = st.builds(
    ConstructedType,
)
astm::PointerType_strategy = st.builds(
    astm::PointerType,
)
astm::CollectionType_strategy = st.builds(
    astm::CollectionType,
)
astm::ReferenceType_strategy = st.builds(
    astm::ReferenceType,
)
astm::RangeType_strategy = st.builds(
    astm::RangeType,
)
astm::ArrayType_strategy = st.builds(
    astm::ArrayType,
)
astm::AggregateScope_strategy = st.builds(
    astm::AggregateScope,
)
DataType_strategy = st.builds(
    DataType,
)
astm::FormalParameterType_strategy = st.builds(
    astm::FormalParameterType,
)
astm::ExceptionType_strategy = st.builds(
    astm::ExceptionType,
)
astm::ConstructedType_strategy = st.builds(
    astm::ConstructedType,
)
astm::EnumType_strategy = st.builds(
    astm::EnumType,
)
astm::PrimitiveType_strategy = st.builds(
    astm::PrimitiveType,
    isSigned=
        st.booleans()
)
GASTMSyntaxObject_strategy = st.builds(
    GASTMSyntaxObject,
)
astm::Type_strategy = st.builds(
    astm::Type,
    isConst=
        st.booleans(),
    isVolatile=
        st.booleans()
)
PreprocessorElement_strategy = st.builds(
    PreprocessorElement,
)
astm::MacroDefinition_strategy = st.builds(
    astm::MacroDefinition,
    macroName=
        safe_text,
    body=
        safe_text
)
astm::MacroCall_strategy = st.builds(
    astm::MacroCall,
)
astm::Comment_strategy = st.builds(
    astm::Comment,
    text=
        safe_text
)
astm::IncludeUnit_strategy = st.builds(
    astm::IncludeUnit,
)
astm::LabelType_strategy = st.builds(
    astm::LabelType,
)
astm::NameSpaceType_strategy = st.builds(
    astm::NameSpaceType,
)
astm::AggregateType_strategy = st.builds(
    astm::AggregateType,
)
astm::NamedType_strategy = st.builds(
    astm::NamedType,
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
astm::AggregateTypeDefinition_strategy = st.builds(
    astm::AggregateTypeDefinition,
)
astm::NamedTypeDefinition_strategy = st.builds(
    astm::NamedTypeDefinition,
)
DataDefinition_strategy = st.builds(
    DataDefinition,
)
astm::VariableDefinition_strategy = st.builds(
    astm::VariableDefinition,
)
astm::BitFieldDefinition_strategy = st.builds(
    astm::BitFieldDefinition,
)
astm::Expression_strategy = st.builds(
    astm::Expression,
)
astm::FunctionScope_strategy = st.builds(
    astm::FunctionScope,
)
astm::Statement_strategy = st.builds(
    astm::Statement,
)
astm::FormalParameterDefinition_strategy = st.builds(
    astm::FormalParameterDefinition,
)
Definition_strategy = st.builds(
    Definition,
)
astm::EntryDefinition_strategy = st.builds(
    astm::EntryDefinition,
)
astm::DataDefinition_strategy = st.builds(
    astm::DataDefinition,
    isMutable=
        st.booleans()
)
astm::EnumLiteralDefinition_strategy = st.builds(
    astm::EnumLiteralDefinition,
)
astm::FunctionDefinition_strategy = st.builds(
    astm::FunctionDefinition,
)
astm::FunctionMemberAttributes_strategy = st.builds(
    astm::FunctionMemberAttributes,
    isThisConst=
        st.booleans(),
    isInline=
        st.booleans(),
    isFriend=
        st.booleans()
)
Declaration_strategy = st.builds(
    Declaration,
)
astm::FormalParameterDeclaration_strategy = st.builds(
    astm::FormalParameterDeclaration,
)
astm::VariableDeclaration_strategy = st.builds(
    astm::VariableDeclaration,
    isMutable=
        st.booleans()
)
astm::FunctionDeclaration_strategy = st.builds(
    astm::FunctionDeclaration,
)
astm::TypeReference_strategy = st.builds(
    astm::TypeReference,
)
DeclarationOrDefinition_strategy = st.builds(
    DeclarationOrDefinition,
)
astm::Declaration_strategy = st.builds(
    astm::Declaration,
)
astm::Definition_strategy = st.builds(
    astm::Definition,
)
DefinitionObject_strategy = st.builds(
    DefinitionObject,
)
astm::NameSpaceDefinition_strategy = st.builds(
    astm::NameSpaceDefinition,
)
astm::LabelDefinition_strategy = st.builds(
    astm::LabelDefinition,
)
astm::TypeDefinition_strategy = st.builds(
    astm::TypeDefinition,
)
astm::DeclarationOrDefinition_strategy = st.builds(
    astm::DeclarationOrDefinition,
    isRegister=
        st.booleans(),
    linkageSpecifier=
        safe_text
)
astm::ProgramScope_strategy = st.builds(
    astm::ProgramScope,
)
OtherSyntaxObject_strategy = st.builds(
    OtherSyntaxObject,
)
astm::SwitchCase_strategy = st.builds(
    astm::SwitchCase,
)
astm::FunctionMemberAttribute_strategy = st.builds(
    astm::FunctionMemberAttribute,
)
astm::Name_strategy = st.builds(
    astm::Name,
    nameString=
        safe_text
)
astm::VirtualSpecification_strategy = st.builds(
    astm::VirtualSpecification,
)
astm::Dimension_strategy = st.builds(
    astm::Dimension,
)
astm::DerivesFrom_strategy = st.builds(
    astm::DerivesFrom,
    isVirtual=
        st.booleans()
)
astm::CatchBlock_strategy = st.builds(
    astm::CatchBlock,
)
astm::AnnotationExpression_strategy = st.builds(
    astm::AnnotationExpression,
)
astm::PreprocessorElement_strategy = st.builds(
    astm::PreprocessorElement,
)
GASTMObject_strategy = st.builds(
    GASTMObject,
)
astm::GASTMSyntaxObject_strategy = st.builds(
    astm::GASTMSyntaxObject,
)
astm::DefinitionObject_strategy = st.builds(
    astm::DefinitionObject,
)
astm::GlobalScope_strategy = st.builds(
    astm::GlobalScope,
)
astm::CompilationUnit_strategy = st.builds(
    astm::CompilationUnit,
    language=
        safe_text
)
GASTMSemanticObject_strategy = st.builds(
    GASTMSemanticObject,
)
astm::Scope_strategy = st.builds(
    astm::Scope,
)
astm::Project_strategy = st.builds(
    astm::Project,
)
GASTMSourceObject_strategy = st.builds(
    GASTMSourceObject,
)
astm::SourceLocation_strategy = st.builds(
    astm::SourceLocation,
    startLine=
        st.integers(),
    endColumn=
        st.integers(),
    endLine=
        st.integers(),
    startColumn=
        st.integers()
)
astm::SourceFile_strategy = st.builds(
    astm::SourceFile,
    pathName=
        safe_text
)
astm::ActualParameter_strategy = st.builds(
    astm::ActualParameter,
)
astm::BinaryOperator_strategy = st.builds(
    astm::BinaryOperator,
)
astm::UnaryOperator_strategy = st.builds(
    astm::UnaryOperator,
)
astm::AccessKind_strategy = st.builds(
    astm::AccessKind,
)
astm::DataType_strategy = st.builds(
    astm::DataType,
)
astm::StorageSpecification_strategy = st.builds(
    astm::StorageSpecification,
)
astm::OtherSyntaxObject_strategy = st.builds(
    astm::OtherSyntaxObject,
)
astm::GASTMSemanticObject_strategy = st.builds(
    astm::GASTMSemanticObject,
)
astm::GASTMSourceObject_strategy = st.builds(
    astm::GASTMSourceObject,
)
astm::GASTMObject_strategy = st.builds(
    astm::GASTMObject,
)
astm::Divide_strategy = st.builds(
    astm::Divide,
)

@given(instance=ClassType_strategy)
@settings(max_examples=50)
def test_classtype_instantiation(instance):
    assert isinstance(instance, ClassType)

@given(instance=astm::SpecificClassType_strategy)
@settings(max_examples=50)
def test_astm::specificclasstype_instantiation(instance):
    assert isinstance(instance, astm::SpecificClassType)

@given(instance=astm::SpecificClassType_strategy)
def test_astm::specificclasstype_imports_type(instance):
    assert isinstance(instance.imports, str)


@given(instance=astm::SpecificClassType_strategy)
def test_astm::specificclasstype_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original

@given(instance=astm::SpecificClassType_strategy)
def test_astm::specificclasstype_package_type(instance):
    assert isinstance(instance.package, str)


@given(instance=astm::SpecificClassType_strategy)
def test_astm::specificclasstype_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original

@given(instance=ActualParameterExpression_strategy)
@settings(max_examples=50)
def test_actualparameterexpression_instantiation(instance):
    assert isinstance(instance, ActualParameterExpression)

@given(instance=astm::ByReferenceActualParameterExpression_strategy)
@settings(max_examples=50)
def test_astm::byreferenceactualparameterexpression_instantiation(instance):
    assert isinstance(instance, astm::ByReferenceActualParameterExpression)

@given(instance=astm::ByValueActualParameterExpression_strategy)
@settings(max_examples=50)
def test_astm::byvalueactualparameterexpression_instantiation(instance):
    assert isinstance(instance, astm::ByValueActualParameterExpression)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=astm::Not_strategy)
@settings(max_examples=50)
def test_astm::not_instantiation(instance):
    assert isinstance(instance, astm::Not)

@given(instance=astm::Deref_strategy)
@settings(max_examples=50)
def test_astm::deref_instantiation(instance):
    assert isinstance(instance, astm::Deref)

@given(instance=astm::BitNot_strategy)
@settings(max_examples=50)
def test_astm::bitnot_instantiation(instance):
    assert isinstance(instance, astm::BitNot)

@given(instance=astm::Decrement_strategy)
@settings(max_examples=50)
def test_astm::decrement_instantiation(instance):
    assert isinstance(instance, astm::Decrement)

@given(instance=astm::Increment_strategy)
@settings(max_examples=50)
def test_astm::increment_instantiation(instance):
    assert isinstance(instance, astm::Increment)

@given(instance=astm::AddressOf_strategy)
@settings(max_examples=50)
def test_astm::addressof_instantiation(instance):
    assert isinstance(instance, astm::AddressOf)

@given(instance=astm::PostIncrement_strategy)
@settings(max_examples=50)
def test_astm::postincrement_instantiation(instance):
    assert isinstance(instance, astm::PostIncrement)

@given(instance=astm::Negate_strategy)
@settings(max_examples=50)
def test_astm::negate_instantiation(instance):
    assert isinstance(instance, astm::Negate)

@given(instance=astm::PostDecrement_strategy)
@settings(max_examples=50)
def test_astm::postdecrement_instantiation(instance):
    assert isinstance(instance, astm::PostDecrement)

@given(instance=astm::UnaryPlus_strategy)
@settings(max_examples=50)
def test_astm::unaryplus_instantiation(instance):
    assert isinstance(instance, astm::UnaryPlus)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=astm::CharLiteral_strategy)
@settings(max_examples=50)
def test_astm::charliteral_instantiation(instance):
    assert isinstance(instance, astm::CharLiteral)

@given(instance=astm::StringLiteral_strategy)
@settings(max_examples=50)
def test_astm::stringliteral_instantiation(instance):
    assert isinstance(instance, astm::StringLiteral)

@given(instance=astm::BitLiteral_strategy)
@settings(max_examples=50)
def test_astm::bitliteral_instantiation(instance):
    assert isinstance(instance, astm::BitLiteral)

@given(instance=astm::RealLiteral_strategy)
@settings(max_examples=50)
def test_astm::realliteral_instantiation(instance):
    assert isinstance(instance, astm::RealLiteral)

@given(instance=astm::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_astm::booleanliteral_instantiation(instance):
    assert isinstance(instance, astm::BooleanLiteral)

@given(instance=astm::IntegerlLiteral_strategy)
@settings(max_examples=50)
def test_astm::integerlliteral_instantiation(instance):
    assert isinstance(instance, astm::IntegerlLiteral)

@given(instance=QualifiedIdentifierReference_strategy)
@settings(max_examples=50)
def test_qualifiedidentifierreference_instantiation(instance):
    assert isinstance(instance, QualifiedIdentifierReference)

@given(instance=astm::QualifiedOverData_strategy)
@settings(max_examples=50)
def test_astm::qualifiedoverdata_instantiation(instance):
    assert isinstance(instance, astm::QualifiedOverData)

@given(instance=astm::QualifiedOverPointer_strategy)
@settings(max_examples=50)
def test_astm::qualifiedoverpointer_instantiation(instance):
    assert isinstance(instance, astm::QualifiedOverPointer)

@given(instance=ForStatement_strategy)
@settings(max_examples=50)
def test_forstatement_instantiation(instance):
    assert isinstance(instance, ForStatement)

@given(instance=astm::ForCheckAfterStatement_strategy)
@settings(max_examples=50)
def test_astm::forcheckafterstatement_instantiation(instance):
    assert isinstance(instance, astm::ForCheckAfterStatement)

@given(instance=astm::ForCheckBeforeStatement_strategy)
@settings(max_examples=50)
def test_astm::forcheckbeforestatement_instantiation(instance):
    assert isinstance(instance, astm::ForCheckBeforeStatement)

@given(instance=AccessKind_strategy)
@settings(max_examples=50)
def test_accesskind_instantiation(instance):
    assert isinstance(instance, AccessKind)

@given(instance=astm::Private_strategy)
@settings(max_examples=50)
def test_astm::private_instantiation(instance):
    assert isinstance(instance, astm::Private)

@given(instance=astm::Protected_strategy)
@settings(max_examples=50)
def test_astm::protected_instantiation(instance):
    assert isinstance(instance, astm::Protected)

@given(instance=astm::Public_strategy)
@settings(max_examples=50)
def test_astm::public_instantiation(instance):
    assert isinstance(instance, astm::Public)

@given(instance=FormalParameterType_strategy)
@settings(max_examples=50)
def test_formalparametertype_instantiation(instance):
    assert isinstance(instance, FormalParameterType)

@given(instance=astm::ByReferenceFormalParameterType_strategy)
@settings(max_examples=50)
def test_astm::byreferenceformalparametertype_instantiation(instance):
    assert isinstance(instance, astm::ByReferenceFormalParameterType)

@given(instance=astm::ByValueFormalParameterType_strategy)
@settings(max_examples=50)
def test_astm::byvalueformalparametertype_instantiation(instance):
    assert isinstance(instance, astm::ByValueFormalParameterType)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=astm::String_strategy)
@settings(max_examples=50)
def test_astm::string_instantiation(instance):
    assert isinstance(instance, astm::String)

@given(instance=astm::Double_strategy)
@settings(max_examples=50)
def test_astm::double_instantiation(instance):
    assert isinstance(instance, astm::Double)

@given(instance=astm::Byte_strategy)
@settings(max_examples=50)
def test_astm::byte_instantiation(instance):
    assert isinstance(instance, astm::Byte)

@given(instance=astm::WideCharacter_strategy)
@settings(max_examples=50)
def test_astm::widecharacter_instantiation(instance):
    assert isinstance(instance, astm::WideCharacter)

@given(instance=astm::Integer_strategy)
@settings(max_examples=50)
def test_astm::integer_instantiation(instance):
    assert isinstance(instance, astm::Integer)

@given(instance=astm::Float_strategy)
@settings(max_examples=50)
def test_astm::float_instantiation(instance):
    assert isinstance(instance, astm::Float)

@given(instance=astm::LongInteger_strategy)
@settings(max_examples=50)
def test_astm::longinteger_instantiation(instance):
    assert isinstance(instance, astm::LongInteger)

@given(instance=astm::Boolean_strategy)
@settings(max_examples=50)
def test_astm::boolean_instantiation(instance):
    assert isinstance(instance, astm::Boolean)

@given(instance=astm::ShortInteger_strategy)
@settings(max_examples=50)
def test_astm::shortinteger_instantiation(instance):
    assert isinstance(instance, astm::ShortInteger)

@given(instance=astm::LongDouble_strategy)
@settings(max_examples=50)
def test_astm::longdouble_instantiation(instance):
    assert isinstance(instance, astm::LongDouble)

@given(instance=astm::Character_strategy)
@settings(max_examples=50)
def test_astm::character_instantiation(instance):
    assert isinstance(instance, astm::Character)

@given(instance=astm::Void_strategy)
@settings(max_examples=50)
def test_astm::void_instantiation(instance):
    assert isinstance(instance, astm::Void)

@given(instance=VirtualSpecification_strategy)
@settings(max_examples=50)
def test_virtualspecification_instantiation(instance):
    assert isinstance(instance, VirtualSpecification)

@given(instance=astm::NonVirtual_strategy)
@settings(max_examples=50)
def test_astm::nonvirtual_instantiation(instance):
    assert isinstance(instance, astm::NonVirtual)

@given(instance=astm::PureVirtual_strategy)
@settings(max_examples=50)
def test_astm::purevirtual_instantiation(instance):
    assert isinstance(instance, astm::PureVirtual)

@given(instance=astm::Virtual_strategy)
@settings(max_examples=50)
def test_astm::virtual_instantiation(instance):
    assert isinstance(instance, astm::Virtual)

@given(instance=StorageSpecification_strategy)
@settings(max_examples=50)
def test_storagespecification_instantiation(instance):
    assert isinstance(instance, StorageSpecification)

@given(instance=astm::NoDef_strategy)
@settings(max_examples=50)
def test_astm::nodef_instantiation(instance):
    assert isinstance(instance, astm::NoDef)

@given(instance=astm::PerClassMember_strategy)
@settings(max_examples=50)
def test_astm::perclassmember_instantiation(instance):
    assert isinstance(instance, astm::PerClassMember)

@given(instance=astm::FunctionPersistent_strategy)
@settings(max_examples=50)
def test_astm::functionpersistent_instantiation(instance):
    assert isinstance(instance, astm::FunctionPersistent)

@given(instance=astm::FileLocal_strategy)
@settings(max_examples=50)
def test_astm::filelocal_instantiation(instance):
    assert isinstance(instance, astm::FileLocal)

@given(instance=astm::External_strategy)
@settings(max_examples=50)
def test_astm::external_instantiation(instance):
    assert isinstance(instance, astm::External)

@given(instance=Scope_strategy)
@settings(max_examples=50)
def test_scope_instantiation(instance):
    assert isinstance(instance, Scope)

@given(instance=ActualParameter_strategy)
@settings(max_examples=50)
def test_actualparameter_instantiation(instance):
    assert isinstance(instance, ActualParameter)

@given(instance=astm::MissingActualParameter_strategy)
@settings(max_examples=50)
def test_astm::missingactualparameter_instantiation(instance):
    assert isinstance(instance, astm::MissingActualParameter)

@given(instance=astm::ActualParameterExpression_strategy)
@settings(max_examples=50)
def test_astm::actualparameterexpression_instantiation(instance):
    assert isinstance(instance, astm::ActualParameterExpression)

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=astm::Exponent_strategy)
@settings(max_examples=50)
def test_astm::exponent_instantiation(instance):
    assert isinstance(instance, astm::Exponent)

@given(instance=astm::Assign_strategy)
@settings(max_examples=50)
def test_astm::assign_instantiation(instance):
    assert isinstance(instance, astm::Assign)

@given(instance=astm::BitAnd_strategy)
@settings(max_examples=50)
def test_astm::bitand_instantiation(instance):
    assert isinstance(instance, astm::BitAnd)

@given(instance=astm::Add_strategy)
@settings(max_examples=50)
def test_astm::add_instantiation(instance):
    assert isinstance(instance, astm::Add)

@given(instance=astm::NotGreater_strategy)
@settings(max_examples=50)
def test_astm::notgreater_instantiation(instance):
    assert isinstance(instance, astm::NotGreater)

@given(instance=astm::Or_strategy)
@settings(max_examples=50)
def test_astm::or_instantiation(instance):
    assert isinstance(instance, astm::Or)

@given(instance=astm::And_strategy)
@settings(max_examples=50)
def test_astm::and_instantiation(instance):
    assert isinstance(instance, astm::And)

@given(instance=astm::BitRightShift_strategy)
@settings(max_examples=50)
def test_astm::bitrightshift_instantiation(instance):
    assert isinstance(instance, astm::BitRightShift)

@given(instance=astm::NotLess_strategy)
@settings(max_examples=50)
def test_astm::notless_instantiation(instance):
    assert isinstance(instance, astm::NotLess)

@given(instance=astm::Modulus_strategy)
@settings(max_examples=50)
def test_astm::modulus_instantiation(instance):
    assert isinstance(instance, astm::Modulus)

@given(instance=astm::Multiply_strategy)
@settings(max_examples=50)
def test_astm::multiply_instantiation(instance):
    assert isinstance(instance, astm::Multiply)

@given(instance=astm::Equal_strategy)
@settings(max_examples=50)
def test_astm::equal_instantiation(instance):
    assert isinstance(instance, astm::Equal)

@given(instance=astm::Subtract_strategy)
@settings(max_examples=50)
def test_astm::subtract_instantiation(instance):
    assert isinstance(instance, astm::Subtract)

@given(instance=astm::Less_strategy)
@settings(max_examples=50)
def test_astm::less_instantiation(instance):
    assert isinstance(instance, astm::Less)

@given(instance=astm::NotEqual_strategy)
@settings(max_examples=50)
def test_astm::notequal_instantiation(instance):
    assert isinstance(instance, astm::NotEqual)

@given(instance=astm::Greater_strategy)
@settings(max_examples=50)
def test_astm::greater_instantiation(instance):
    assert isinstance(instance, astm::Greater)

@given(instance=astm::BitLeftShift_strategy)
@settings(max_examples=50)
def test_astm::bitleftshift_instantiation(instance):
    assert isinstance(instance, astm::BitLeftShift)

@given(instance=astm::BitOr_strategy)
@settings(max_examples=50)
def test_astm::bitor_instantiation(instance):
    assert isinstance(instance, astm::BitOr)

@given(instance=astm::BitXor_strategy)
@settings(max_examples=50)
def test_astm::bitxor_instantiation(instance):
    assert isinstance(instance, astm::BitXor)

@given(instance=astm::OperatorAssign_strategy)
@settings(max_examples=50)
def test_astm::operatorassign_instantiation(instance):
    assert isinstance(instance, astm::OperatorAssign)

@given(instance=NameReference_strategy)
@settings(max_examples=50)
def test_namereference_instantiation(instance):
    assert isinstance(instance, NameReference)

@given(instance=astm::IdentifierReference_strategy)
@settings(max_examples=50)
def test_astm::identifierreference_instantiation(instance):
    assert isinstance(instance, astm::IdentifierReference)

@given(instance=astm::TypeQualifiedIdentifierReference_strategy)
@settings(max_examples=50)
def test_astm::typequalifiedidentifierreference_instantiation(instance):
    assert isinstance(instance, astm::TypeQualifiedIdentifierReference)

@given(instance=astm::QualifiedIdentifierReference_strategy)
@settings(max_examples=50)
def test_astm::qualifiedidentifierreference_instantiation(instance):
    assert isinstance(instance, astm::QualifiedIdentifierReference)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=astm::UnaryExpression_strategy)
@settings(max_examples=50)
def test_astm::unaryexpression_instantiation(instance):
    assert isinstance(instance, astm::UnaryExpression)

@given(instance=astm::BinaryExpression_strategy)
@settings(max_examples=50)
def test_astm::binaryexpression_instantiation(instance):
    assert isinstance(instance, astm::BinaryExpression)

@given(instance=astm::NewExpression_strategy)
@settings(max_examples=50)
def test_astm::newexpression_instantiation(instance):
    assert isinstance(instance, astm::NewExpression)

@given(instance=astm::ArrayAccess_strategy)
@settings(max_examples=50)
def test_astm::arrayaccess_instantiation(instance):
    assert isinstance(instance, astm::ArrayAccess)

@given(instance=astm::FunctionCallExpression_strategy)
@settings(max_examples=50)
def test_astm::functioncallexpression_instantiation(instance):
    assert isinstance(instance, astm::FunctionCallExpression)

@given(instance=astm::Literal_strategy)
@settings(max_examples=50)
def test_astm::literal_instantiation(instance):
    assert isinstance(instance, astm::Literal)

@given(instance=astm::Literal_strategy)
def test_astm::literal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=astm::Literal_strategy)
def test_astm::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=astm::AggregateExpression_strategy)
@settings(max_examples=50)
def test_astm::aggregateexpression_instantiation(instance):
    assert isinstance(instance, astm::AggregateExpression)

@given(instance=astm::CastExpression_strategy)
@settings(max_examples=50)
def test_astm::castexpression_instantiation(instance):
    assert isinstance(instance, astm::CastExpression)

@given(instance=astm::RangeExpression_strategy)
@settings(max_examples=50)
def test_astm::rangeexpression_instantiation(instance):
    assert isinstance(instance, astm::RangeExpression)

@given(instance=astm::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_astm::conditionalexpression_instantiation(instance):
    assert isinstance(instance, astm::ConditionalExpression)

@given(instance=astm::NameReference_strategy)
@settings(max_examples=50)
def test_astm::namereference_instantiation(instance):
    assert isinstance(instance, astm::NameReference)

@given(instance=CatchBlock_strategy)
@settings(max_examples=50)
def test_catchblock_instantiation(instance):
    assert isinstance(instance, CatchBlock)

@given(instance=astm::VariableCatchBlock_strategy)
@settings(max_examples=50)
def test_astm::variablecatchblock_instantiation(instance):
    assert isinstance(instance, astm::VariableCatchBlock)

@given(instance=astm::TypesCatchBlock_strategy)
@settings(max_examples=50)
def test_astm::typescatchblock_instantiation(instance):
    assert isinstance(instance, astm::TypesCatchBlock)

@given(instance=LoopStatement_strategy)
@settings(max_examples=50)
def test_loopstatement_instantiation(instance):
    assert isinstance(instance, LoopStatement)

@given(instance=astm::DoWhileStatement_strategy)
@settings(max_examples=50)
def test_astm::dowhilestatement_instantiation(instance):
    assert isinstance(instance, astm::DoWhileStatement)

@given(instance=astm::WhileStatement_strategy)
@settings(max_examples=50)
def test_astm::whilestatement_instantiation(instance):
    assert isinstance(instance, astm::WhileStatement)

@given(instance=SwitchCase_strategy)
@settings(max_examples=50)
def test_switchcase_instantiation(instance):
    assert isinstance(instance, SwitchCase)

@given(instance=astm::DefaultBlock_strategy)
@settings(max_examples=50)
def test_astm::defaultblock_instantiation(instance):
    assert isinstance(instance, astm::DefaultBlock)

@given(instance=astm::CaseBlock_strategy)
@settings(max_examples=50)
def test_astm::caseblock_instantiation(instance):
    assert isinstance(instance, astm::CaseBlock)

@given(instance=astm::BlockScope_strategy)
@settings(max_examples=50)
def test_astm::blockscope_instantiation(instance):
    assert isinstance(instance, astm::BlockScope)

@given(instance=astm::ForStatement_strategy)
@settings(max_examples=50)
def test_astm::forstatement_instantiation(instance):
    assert isinstance(instance, astm::ForStatement)

@given(instance=astm::LabelAccess_strategy)
@settings(max_examples=50)
def test_astm::labelaccess_instantiation(instance):
    assert isinstance(instance, astm::LabelAccess)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=astm::SwitchStatement_strategy)
@settings(max_examples=50)
def test_astm::switchstatement_instantiation(instance):
    assert isinstance(instance, astm::SwitchStatement)

@given(instance=astm::TryStatement_strategy)
@settings(max_examples=50)
def test_astm::trystatement_instantiation(instance):
    assert isinstance(instance, astm::TryStatement)

@given(instance=astm::ThrowStatement_strategy)
@settings(max_examples=50)
def test_astm::throwstatement_instantiation(instance):
    assert isinstance(instance, astm::ThrowStatement)

@given(instance=astm::EmptyStatement_strategy)
@settings(max_examples=50)
def test_astm::emptystatement_instantiation(instance):
    assert isinstance(instance, astm::EmptyStatement)

@given(instance=astm::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_astm::expressionstatement_instantiation(instance):
    assert isinstance(instance, astm::ExpressionStatement)

@given(instance=astm::ReturnStatement_strategy)
@settings(max_examples=50)
def test_astm::returnstatement_instantiation(instance):
    assert isinstance(instance, astm::ReturnStatement)

@given(instance=astm::BreakStatement_strategy)
@settings(max_examples=50)
def test_astm::breakstatement_instantiation(instance):
    assert isinstance(instance, astm::BreakStatement)

@given(instance=astm::DeclarationOrDefinitionStatement_strategy)
@settings(max_examples=50)
def test_astm::declarationordefinitionstatement_instantiation(instance):
    assert isinstance(instance, astm::DeclarationOrDefinitionStatement)

@given(instance=astm::BlockStatement_strategy)
@settings(max_examples=50)
def test_astm::blockstatement_instantiation(instance):
    assert isinstance(instance, astm::BlockStatement)

@given(instance=astm::IfStatement_strategy)
@settings(max_examples=50)
def test_astm::ifstatement_instantiation(instance):
    assert isinstance(instance, astm::IfStatement)

@given(instance=astm::ContinueStatement_strategy)
@settings(max_examples=50)
def test_astm::continuestatement_instantiation(instance):
    assert isinstance(instance, astm::ContinueStatement)

@given(instance=astm::JumpStatement_strategy)
@settings(max_examples=50)
def test_astm::jumpstatement_instantiation(instance):
    assert isinstance(instance, astm::JumpStatement)

@given(instance=astm::LabeledStatement_strategy)
@settings(max_examples=50)
def test_astm::labeledstatement_instantiation(instance):
    assert isinstance(instance, astm::LabeledStatement)

@given(instance=astm::TerminateStatement_strategy)
@settings(max_examples=50)
def test_astm::terminatestatement_instantiation(instance):
    assert isinstance(instance, astm::TerminateStatement)

@given(instance=astm::LoopStatement_strategy)
@settings(max_examples=50)
def test_astm::loopstatement_instantiation(instance):
    assert isinstance(instance, astm::LoopStatement)

@given(instance=astm::DeleteStatement_strategy)
@settings(max_examples=50)
def test_astm::deletestatement_instantiation(instance):
    assert isinstance(instance, astm::DeleteStatement)

@given(instance=TypeReference_strategy)
@settings(max_examples=50)
def test_typereference_instantiation(instance):
    assert isinstance(instance, TypeReference)

@given(instance=astm::NamedTypeReference_strategy)
@settings(max_examples=50)
def test_astm::namedtypereference_instantiation(instance):
    assert isinstance(instance, astm::NamedTypeReference)

@given(instance=astm::UnnamedTypeReference_strategy)
@settings(max_examples=50)
def test_astm::unnamedtypereference_instantiation(instance):
    assert isinstance(instance, astm::UnnamedTypeReference)

@given(instance=AggregateType_strategy)
@settings(max_examples=50)
def test_aggregatetype_instantiation(instance):
    assert isinstance(instance, AggregateType)

@given(instance=astm::StructureType_strategy)
@settings(max_examples=50)
def test_astm::structuretype_instantiation(instance):
    assert isinstance(instance, astm::StructureType)

@given(instance=astm::AnnotationType_strategy)
@settings(max_examples=50)
def test_astm::annotationtype_instantiation(instance):
    assert isinstance(instance, astm::AnnotationType)

@given(instance=astm::UnionType_strategy)
@settings(max_examples=50)
def test_astm::uniontype_instantiation(instance):
    assert isinstance(instance, astm::UnionType)

@given(instance=astm::ClassType_strategy)
@settings(max_examples=50)
def test_astm::classtype_instantiation(instance):
    assert isinstance(instance, astm::ClassType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=astm::FunctionType_strategy)
@settings(max_examples=50)
def test_astm::functiontype_instantiation(instance):
    assert isinstance(instance, astm::FunctionType)

@given(instance=ConstructedType_strategy)
@settings(max_examples=50)
def test_constructedtype_instantiation(instance):
    assert isinstance(instance, ConstructedType)

@given(instance=astm::PointerType_strategy)
@settings(max_examples=50)
def test_astm::pointertype_instantiation(instance):
    assert isinstance(instance, astm::PointerType)

@given(instance=astm::CollectionType_strategy)
@settings(max_examples=50)
def test_astm::collectiontype_instantiation(instance):
    assert isinstance(instance, astm::CollectionType)

@given(instance=astm::ReferenceType_strategy)
@settings(max_examples=50)
def test_astm::referencetype_instantiation(instance):
    assert isinstance(instance, astm::ReferenceType)

@given(instance=astm::RangeType_strategy)
@settings(max_examples=50)
def test_astm::rangetype_instantiation(instance):
    assert isinstance(instance, astm::RangeType)

@given(instance=astm::ArrayType_strategy)
@settings(max_examples=50)
def test_astm::arraytype_instantiation(instance):
    assert isinstance(instance, astm::ArrayType)

@given(instance=astm::AggregateScope_strategy)
@settings(max_examples=50)
def test_astm::aggregatescope_instantiation(instance):
    assert isinstance(instance, astm::AggregateScope)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=astm::FormalParameterType_strategy)
@settings(max_examples=50)
def test_astm::formalparametertype_instantiation(instance):
    assert isinstance(instance, astm::FormalParameterType)

@given(instance=astm::ExceptionType_strategy)
@settings(max_examples=50)
def test_astm::exceptiontype_instantiation(instance):
    assert isinstance(instance, astm::ExceptionType)

@given(instance=astm::ConstructedType_strategy)
@settings(max_examples=50)
def test_astm::constructedtype_instantiation(instance):
    assert isinstance(instance, astm::ConstructedType)

@given(instance=astm::EnumType_strategy)
@settings(max_examples=50)
def test_astm::enumtype_instantiation(instance):
    assert isinstance(instance, astm::EnumType)

@given(instance=astm::PrimitiveType_strategy)
@settings(max_examples=50)
def test_astm::primitivetype_instantiation(instance):
    assert isinstance(instance, astm::PrimitiveType)

@given(instance=astm::PrimitiveType_strategy)
def test_astm::primitivetype_isSigned_type(instance):
    assert isinstance(instance.isSigned, bool)


@given(instance=astm::PrimitiveType_strategy)
def test_astm::primitivetype_isSigned_setter(instance):
    original = instance.isSigned
    instance.isSigned = original
    assert instance.isSigned == original

@given(instance=GASTMSyntaxObject_strategy)
@settings(max_examples=50)
def test_gastmsyntaxobject_instantiation(instance):
    assert isinstance(instance, GASTMSyntaxObject)

@given(instance=astm::Type_strategy)
@settings(max_examples=50)
def test_astm::type_instantiation(instance):
    assert isinstance(instance, astm::Type)

@given(instance=astm::Type_strategy)
def test_astm::type_isConst_type(instance):
    assert isinstance(instance.isConst, bool)


@given(instance=astm::Type_strategy)
def test_astm::type_isConst_setter(instance):
    original = instance.isConst
    instance.isConst = original
    assert instance.isConst == original

@given(instance=astm::Type_strategy)
def test_astm::type_isVolatile_type(instance):
    assert isinstance(instance.isVolatile, bool)


@given(instance=astm::Type_strategy)
def test_astm::type_isVolatile_setter(instance):
    original = instance.isVolatile
    instance.isVolatile = original
    assert instance.isVolatile == original

@given(instance=PreprocessorElement_strategy)
@settings(max_examples=50)
def test_preprocessorelement_instantiation(instance):
    assert isinstance(instance, PreprocessorElement)

@given(instance=astm::MacroDefinition_strategy)
@settings(max_examples=50)
def test_astm::macrodefinition_instantiation(instance):
    assert isinstance(instance, astm::MacroDefinition)

@given(instance=astm::MacroDefinition_strategy)
def test_astm::macrodefinition_macroName_type(instance):
    assert isinstance(instance.macroName, str)


@given(instance=astm::MacroDefinition_strategy)
def test_astm::macrodefinition_macroName_setter(instance):
    original = instance.macroName
    instance.macroName = original
    assert instance.macroName == original

@given(instance=astm::MacroDefinition_strategy)
def test_astm::macrodefinition_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=astm::MacroDefinition_strategy)
def test_astm::macrodefinition_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=astm::MacroCall_strategy)
@settings(max_examples=50)
def test_astm::macrocall_instantiation(instance):
    assert isinstance(instance, astm::MacroCall)

@given(instance=astm::Comment_strategy)
@settings(max_examples=50)
def test_astm::comment_instantiation(instance):
    assert isinstance(instance, astm::Comment)

@given(instance=astm::Comment_strategy)
def test_astm::comment_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=astm::Comment_strategy)
def test_astm::comment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=astm::IncludeUnit_strategy)
@settings(max_examples=50)
def test_astm::includeunit_instantiation(instance):
    assert isinstance(instance, astm::IncludeUnit)

@given(instance=astm::LabelType_strategy)
@settings(max_examples=50)
def test_astm::labeltype_instantiation(instance):
    assert isinstance(instance, astm::LabelType)

@given(instance=astm::NameSpaceType_strategy)
@settings(max_examples=50)
def test_astm::namespacetype_instantiation(instance):
    assert isinstance(instance, astm::NameSpaceType)

@given(instance=astm::AggregateType_strategy)
@settings(max_examples=50)
def test_astm::aggregatetype_instantiation(instance):
    assert isinstance(instance, astm::AggregateType)

@given(instance=astm::NamedType_strategy)
@settings(max_examples=50)
def test_astm::namedtype_instantiation(instance):
    assert isinstance(instance, astm::NamedType)

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=astm::AggregateTypeDefinition_strategy)
@settings(max_examples=50)
def test_astm::aggregatetypedefinition_instantiation(instance):
    assert isinstance(instance, astm::AggregateTypeDefinition)

@given(instance=astm::NamedTypeDefinition_strategy)
@settings(max_examples=50)
def test_astm::namedtypedefinition_instantiation(instance):
    assert isinstance(instance, astm::NamedTypeDefinition)

@given(instance=DataDefinition_strategy)
@settings(max_examples=50)
def test_datadefinition_instantiation(instance):
    assert isinstance(instance, DataDefinition)

@given(instance=astm::VariableDefinition_strategy)
@settings(max_examples=50)
def test_astm::variabledefinition_instantiation(instance):
    assert isinstance(instance, astm::VariableDefinition)

@given(instance=astm::BitFieldDefinition_strategy)
@settings(max_examples=50)
def test_astm::bitfielddefinition_instantiation(instance):
    assert isinstance(instance, astm::BitFieldDefinition)

@given(instance=astm::Expression_strategy)
@settings(max_examples=50)
def test_astm::expression_instantiation(instance):
    assert isinstance(instance, astm::Expression)

@given(instance=astm::FunctionScope_strategy)
@settings(max_examples=50)
def test_astm::functionscope_instantiation(instance):
    assert isinstance(instance, astm::FunctionScope)

@given(instance=astm::Statement_strategy)
@settings(max_examples=50)
def test_astm::statement_instantiation(instance):
    assert isinstance(instance, astm::Statement)

@given(instance=astm::FormalParameterDefinition_strategy)
@settings(max_examples=50)
def test_astm::formalparameterdefinition_instantiation(instance):
    assert isinstance(instance, astm::FormalParameterDefinition)

@given(instance=Definition_strategy)
@settings(max_examples=50)
def test_definition_instantiation(instance):
    assert isinstance(instance, Definition)

@given(instance=astm::EntryDefinition_strategy)
@settings(max_examples=50)
def test_astm::entrydefinition_instantiation(instance):
    assert isinstance(instance, astm::EntryDefinition)

@given(instance=astm::DataDefinition_strategy)
@settings(max_examples=50)
def test_astm::datadefinition_instantiation(instance):
    assert isinstance(instance, astm::DataDefinition)

@given(instance=astm::DataDefinition_strategy)
def test_astm::datadefinition_isMutable_type(instance):
    assert isinstance(instance.isMutable, bool)


@given(instance=astm::DataDefinition_strategy)
def test_astm::datadefinition_isMutable_setter(instance):
    original = instance.isMutable
    instance.isMutable = original
    assert instance.isMutable == original

@given(instance=astm::EnumLiteralDefinition_strategy)
@settings(max_examples=50)
def test_astm::enumliteraldefinition_instantiation(instance):
    assert isinstance(instance, astm::EnumLiteralDefinition)

@given(instance=astm::FunctionDefinition_strategy)
@settings(max_examples=50)
def test_astm::functiondefinition_instantiation(instance):
    assert isinstance(instance, astm::FunctionDefinition)

@given(instance=astm::FunctionMemberAttributes_strategy)
@settings(max_examples=50)
def test_astm::functionmemberattributes_instantiation(instance):
    assert isinstance(instance, astm::FunctionMemberAttributes)

@given(instance=astm::FunctionMemberAttributes_strategy)
def test_astm::functionmemberattributes_isThisConst_type(instance):
    assert isinstance(instance.isThisConst, bool)


@given(instance=astm::FunctionMemberAttributes_strategy)
def test_astm::functionmemberattributes_isThisConst_setter(instance):
    original = instance.isThisConst
    instance.isThisConst = original
    assert instance.isThisConst == original

@given(instance=astm::FunctionMemberAttributes_strategy)
def test_astm::functionmemberattributes_isInline_type(instance):
    assert isinstance(instance.isInline, bool)


@given(instance=astm::FunctionMemberAttributes_strategy)
def test_astm::functionmemberattributes_isInline_setter(instance):
    original = instance.isInline
    instance.isInline = original
    assert instance.isInline == original

@given(instance=astm::FunctionMemberAttributes_strategy)
def test_astm::functionmemberattributes_isFriend_type(instance):
    assert isinstance(instance.isFriend, bool)


@given(instance=astm::FunctionMemberAttributes_strategy)
def test_astm::functionmemberattributes_isFriend_setter(instance):
    original = instance.isFriend
    instance.isFriend = original
    assert instance.isFriend == original

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=astm::FormalParameterDeclaration_strategy)
@settings(max_examples=50)
def test_astm::formalparameterdeclaration_instantiation(instance):
    assert isinstance(instance, astm::FormalParameterDeclaration)

@given(instance=astm::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_astm::variabledeclaration_instantiation(instance):
    assert isinstance(instance, astm::VariableDeclaration)

@given(instance=astm::VariableDeclaration_strategy)
def test_astm::variabledeclaration_isMutable_type(instance):
    assert isinstance(instance.isMutable, bool)


@given(instance=astm::VariableDeclaration_strategy)
def test_astm::variabledeclaration_isMutable_setter(instance):
    original = instance.isMutable
    instance.isMutable = original
    assert instance.isMutable == original

@given(instance=astm::FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_astm::functiondeclaration_instantiation(instance):
    assert isinstance(instance, astm::FunctionDeclaration)

@given(instance=astm::TypeReference_strategy)
@settings(max_examples=50)
def test_astm::typereference_instantiation(instance):
    assert isinstance(instance, astm::TypeReference)

@given(instance=DeclarationOrDefinition_strategy)
@settings(max_examples=50)
def test_declarationordefinition_instantiation(instance):
    assert isinstance(instance, DeclarationOrDefinition)

@given(instance=astm::Declaration_strategy)
@settings(max_examples=50)
def test_astm::declaration_instantiation(instance):
    assert isinstance(instance, astm::Declaration)

@given(instance=astm::Definition_strategy)
@settings(max_examples=50)
def test_astm::definition_instantiation(instance):
    assert isinstance(instance, astm::Definition)

@given(instance=DefinitionObject_strategy)
@settings(max_examples=50)
def test_definitionobject_instantiation(instance):
    assert isinstance(instance, DefinitionObject)

@given(instance=astm::NameSpaceDefinition_strategy)
@settings(max_examples=50)
def test_astm::namespacedefinition_instantiation(instance):
    assert isinstance(instance, astm::NameSpaceDefinition)

@given(instance=astm::LabelDefinition_strategy)
@settings(max_examples=50)
def test_astm::labeldefinition_instantiation(instance):
    assert isinstance(instance, astm::LabelDefinition)

@given(instance=astm::TypeDefinition_strategy)
@settings(max_examples=50)
def test_astm::typedefinition_instantiation(instance):
    assert isinstance(instance, astm::TypeDefinition)

@given(instance=astm::DeclarationOrDefinition_strategy)
@settings(max_examples=50)
def test_astm::declarationordefinition_instantiation(instance):
    assert isinstance(instance, astm::DeclarationOrDefinition)

@given(instance=astm::DeclarationOrDefinition_strategy)
def test_astm::declarationordefinition_isRegister_type(instance):
    assert isinstance(instance.isRegister, bool)


@given(instance=astm::DeclarationOrDefinition_strategy)
def test_astm::declarationordefinition_isRegister_setter(instance):
    original = instance.isRegister
    instance.isRegister = original
    assert instance.isRegister == original

@given(instance=astm::DeclarationOrDefinition_strategy)
def test_astm::declarationordefinition_linkageSpecifier_type(instance):
    assert isinstance(instance.linkageSpecifier, str)


@given(instance=astm::DeclarationOrDefinition_strategy)
def test_astm::declarationordefinition_linkageSpecifier_setter(instance):
    original = instance.linkageSpecifier
    instance.linkageSpecifier = original
    assert instance.linkageSpecifier == original

@given(instance=astm::ProgramScope_strategy)
@settings(max_examples=50)
def test_astm::programscope_instantiation(instance):
    assert isinstance(instance, astm::ProgramScope)

@given(instance=OtherSyntaxObject_strategy)
@settings(max_examples=50)
def test_othersyntaxobject_instantiation(instance):
    assert isinstance(instance, OtherSyntaxObject)

@given(instance=astm::SwitchCase_strategy)
@settings(max_examples=50)
def test_astm::switchcase_instantiation(instance):
    assert isinstance(instance, astm::SwitchCase)

@given(instance=astm::FunctionMemberAttribute_strategy)
@settings(max_examples=50)
def test_astm::functionmemberattribute_instantiation(instance):
    assert isinstance(instance, astm::FunctionMemberAttribute)

@given(instance=astm::Name_strategy)
@settings(max_examples=50)
def test_astm::name_instantiation(instance):
    assert isinstance(instance, astm::Name)

@given(instance=astm::Name_strategy)
def test_astm::name_nameString_type(instance):
    assert isinstance(instance.nameString, str)


@given(instance=astm::Name_strategy)
def test_astm::name_nameString_setter(instance):
    original = instance.nameString
    instance.nameString = original
    assert instance.nameString == original

@given(instance=astm::VirtualSpecification_strategy)
@settings(max_examples=50)
def test_astm::virtualspecification_instantiation(instance):
    assert isinstance(instance, astm::VirtualSpecification)

@given(instance=astm::Dimension_strategy)
@settings(max_examples=50)
def test_astm::dimension_instantiation(instance):
    assert isinstance(instance, astm::Dimension)

@given(instance=astm::DerivesFrom_strategy)
@settings(max_examples=50)
def test_astm::derivesfrom_instantiation(instance):
    assert isinstance(instance, astm::DerivesFrom)

@given(instance=astm::DerivesFrom_strategy)
def test_astm::derivesfrom_isVirtual_type(instance):
    assert isinstance(instance.isVirtual, bool)


@given(instance=astm::DerivesFrom_strategy)
def test_astm::derivesfrom_isVirtual_setter(instance):
    original = instance.isVirtual
    instance.isVirtual = original
    assert instance.isVirtual == original

@given(instance=astm::CatchBlock_strategy)
@settings(max_examples=50)
def test_astm::catchblock_instantiation(instance):
    assert isinstance(instance, astm::CatchBlock)

@given(instance=astm::AnnotationExpression_strategy)
@settings(max_examples=50)
def test_astm::annotationexpression_instantiation(instance):
    assert isinstance(instance, astm::AnnotationExpression)

@given(instance=astm::PreprocessorElement_strategy)
@settings(max_examples=50)
def test_astm::preprocessorelement_instantiation(instance):
    assert isinstance(instance, astm::PreprocessorElement)

@given(instance=GASTMObject_strategy)
@settings(max_examples=50)
def test_gastmobject_instantiation(instance):
    assert isinstance(instance, GASTMObject)

@given(instance=astm::GASTMSyntaxObject_strategy)
@settings(max_examples=50)
def test_astm::gastmsyntaxobject_instantiation(instance):
    assert isinstance(instance, astm::GASTMSyntaxObject)

@given(instance=astm::DefinitionObject_strategy)
@settings(max_examples=50)
def test_astm::definitionobject_instantiation(instance):
    assert isinstance(instance, astm::DefinitionObject)

@given(instance=astm::GlobalScope_strategy)
@settings(max_examples=50)
def test_astm::globalscope_instantiation(instance):
    assert isinstance(instance, astm::GlobalScope)

@given(instance=astm::CompilationUnit_strategy)
@settings(max_examples=50)
def test_astm::compilationunit_instantiation(instance):
    assert isinstance(instance, astm::CompilationUnit)

@given(instance=astm::CompilationUnit_strategy)
def test_astm::compilationunit_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=astm::CompilationUnit_strategy)
def test_astm::compilationunit_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=GASTMSemanticObject_strategy)
@settings(max_examples=50)
def test_gastmsemanticobject_instantiation(instance):
    assert isinstance(instance, GASTMSemanticObject)

@given(instance=astm::Scope_strategy)
@settings(max_examples=50)
def test_astm::scope_instantiation(instance):
    assert isinstance(instance, astm::Scope)

@given(instance=astm::Project_strategy)
@settings(max_examples=50)
def test_astm::project_instantiation(instance):
    assert isinstance(instance, astm::Project)

@given(instance=GASTMSourceObject_strategy)
@settings(max_examples=50)
def test_gastmsourceobject_instantiation(instance):
    assert isinstance(instance, GASTMSourceObject)

@given(instance=astm::SourceLocation_strategy)
@settings(max_examples=50)
def test_astm::sourcelocation_instantiation(instance):
    assert isinstance(instance, astm::SourceLocation)

@given(instance=astm::SourceLocation_strategy)
def test_astm::sourcelocation_startLine_type(instance):
    assert isinstance(instance.startLine, int)


@given(instance=astm::SourceLocation_strategy)
def test_astm::sourcelocation_startLine_setter(instance):
    original = instance.startLine
    instance.startLine = original
    assert instance.startLine == original

@given(instance=astm::SourceLocation_strategy)
def test_astm::sourcelocation_endColumn_type(instance):
    assert isinstance(instance.endColumn, int)


@given(instance=astm::SourceLocation_strategy)
def test_astm::sourcelocation_endColumn_setter(instance):
    original = instance.endColumn
    instance.endColumn = original
    assert instance.endColumn == original

@given(instance=astm::SourceLocation_strategy)
def test_astm::sourcelocation_endLine_type(instance):
    assert isinstance(instance.endLine, int)


@given(instance=astm::SourceLocation_strategy)
def test_astm::sourcelocation_endLine_setter(instance):
    original = instance.endLine
    instance.endLine = original
    assert instance.endLine == original

@given(instance=astm::SourceLocation_strategy)
def test_astm::sourcelocation_startColumn_type(instance):
    assert isinstance(instance.startColumn, int)


@given(instance=astm::SourceLocation_strategy)
def test_astm::sourcelocation_startColumn_setter(instance):
    original = instance.startColumn
    instance.startColumn = original
    assert instance.startColumn == original

@given(instance=astm::SourceFile_strategy)
@settings(max_examples=50)
def test_astm::sourcefile_instantiation(instance):
    assert isinstance(instance, astm::SourceFile)

@given(instance=astm::SourceFile_strategy)
def test_astm::sourcefile_pathName_type(instance):
    assert isinstance(instance.pathName, str)


@given(instance=astm::SourceFile_strategy)
def test_astm::sourcefile_pathName_setter(instance):
    original = instance.pathName
    instance.pathName = original
    assert instance.pathName == original

@given(instance=astm::ActualParameter_strategy)
@settings(max_examples=50)
def test_astm::actualparameter_instantiation(instance):
    assert isinstance(instance, astm::ActualParameter)

@given(instance=astm::BinaryOperator_strategy)
@settings(max_examples=50)
def test_astm::binaryoperator_instantiation(instance):
    assert isinstance(instance, astm::BinaryOperator)

@given(instance=astm::UnaryOperator_strategy)
@settings(max_examples=50)
def test_astm::unaryoperator_instantiation(instance):
    assert isinstance(instance, astm::UnaryOperator)

@given(instance=astm::AccessKind_strategy)
@settings(max_examples=50)
def test_astm::accesskind_instantiation(instance):
    assert isinstance(instance, astm::AccessKind)

@given(instance=astm::DataType_strategy)
@settings(max_examples=50)
def test_astm::datatype_instantiation(instance):
    assert isinstance(instance, astm::DataType)

@given(instance=astm::StorageSpecification_strategy)
@settings(max_examples=50)
def test_astm::storagespecification_instantiation(instance):
    assert isinstance(instance, astm::StorageSpecification)

@given(instance=astm::OtherSyntaxObject_strategy)
@settings(max_examples=50)
def test_astm::othersyntaxobject_instantiation(instance):
    assert isinstance(instance, astm::OtherSyntaxObject)

@given(instance=astm::GASTMSemanticObject_strategy)
@settings(max_examples=50)
def test_astm::gastmsemanticobject_instantiation(instance):
    assert isinstance(instance, astm::GASTMSemanticObject)

@given(instance=astm::GASTMSourceObject_strategy)
@settings(max_examples=50)
def test_astm::gastmsourceobject_instantiation(instance):
    assert isinstance(instance, astm::GASTMSourceObject)

@given(instance=astm::GASTMObject_strategy)
@settings(max_examples=50)
def test_astm::gastmobject_instantiation(instance):
    assert isinstance(instance, astm::GASTMObject)

@given(instance=astm::Divide_strategy)
@settings(max_examples=50)
def test_astm::divide_instantiation(instance):
    assert isinstance(instance, astm::Divide)
