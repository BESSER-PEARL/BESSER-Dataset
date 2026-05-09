import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    StorageSpecification,
    astm::gastm::PerClassMember,
    astm::gastm::FileLocal,
    astm::gastm::FunctionPersistent,
    astm::gastm::NoDef,
    astm::gastm::External,
    ActualParameter,
    astm::gastm::ActualParameterExpression,
    BinaryOperator,
    astm::gastm::OperatorAssign,
    IdentifierReference,
    NameReference,
    astm::gastm::TypeQualifiedIdentifierReference,
    astm::gastm::IdentifierReference,
    astm::gastm::QualifiedIdentifierReference,
    SwitchCase,
    astm::gastm::CaseBlock,
    CatchBlock,
    astm::gastm::TypesCatchBlock,
    astm::gastm::VariableCatchBlock,
    LoopStatement,
    astm::gastm::ForStatement,
    BlockScope,
    LabelDefinition,
    LabelAccess,
    Dimension,
    ConstructedType,
    astm::gastm::ArrayType,
    AggregateScope,
    DelphiInterfaceSection,
    FunctionCallExpression,
    astm::sastm::DelphiFunctionCallExpression,
    BlockStatement,
    astm::sastm::DelphiWithStatement,
    astm::sastm::DelphiBlockStatement,
    NamedTypeReference,
    DelphiImplementationSection,
    astm::gastm::Multiply,
    astm::gastm::Subtract,
    astm::gastm::Add,
    astm::gastm::SpecificConcatString,
    astm::gastm::SpecificLike,
    astm::gastm::SpecificIn,
    astm::gastm::SpecificGreaterEqual,
    astm::gastm::SpecificLessEqual,
    ActualParameterExpression,
    astm::gastm::ByReferenceActualParameterExpression,
    astm::gastm::ByValueActualParameterExpression,
    astm::gastm::MissingActualParameter,
    astm::gastm::Assign,
    astm::gastm::BitRightShift,
    astm::gastm::BitLeftShift,
    astm::gastm::BitXor,
    astm::gastm::BitOr,
    astm::gastm::BitAnd,
    astm::gastm::NotLess,
    astm::gastm::Less,
    astm::gastm::NotGreater,
    astm::gastm::Greater,
    astm::gastm::NotEqual,
    astm::gastm::Equal,
    astm::gastm::Or,
    astm::gastm::And,
    astm::gastm::Exponent,
    astm::gastm::Modulus,
    astm::gastm::Divide,
    astm::gastm::PointerType,
    astm::gastm::CollectionType,
    UnaryOperator,
    astm::gastm::Decrement,
    astm::gastm::Increment,
    astm::gastm::Not,
    astm::gastm::BitNot,
    astm::gastm::PostDecrement,
    astm::gastm::Deref,
    astm::gastm::AddressOf,
    astm::gastm::Negate,
    astm::gastm::PostIncrement,
    astm::gastm::UnaryPlus,
    Literal,
    astm::gastm::StringLiteral,
    astm::gastm::RealLiteral,
    astm::gastm::CharLiteral,
    astm::gastm::BitLiteral,
    astm::gastm::BooleanLiteral,
    astm::gastm::IntegerLiteral,
    QualifiedIdentifierReference,
    astm::gastm::QualifiedOverData,
    astm::gastm::QualifiedOverPointer,
    ForStatement,
    astm::gastm::ForCheckAfterStatement,
    astm::gastm::ForCheckBeforeStatement,
    astm::gastm::DoWhileStatement,
    astm::gastm::WhileStatement,
    astm::gastm::DefaultBlock,
    AccessKind,
    astm::gastm::Private,
    astm::gastm::Protected,
    astm::gastm::Public,
    astm::gastm::RangeType,
    astm::gastm::ReferenceType,
    PrimitiveType,
    astm::gastm::LongInteger,
    astm::gastm::Double,
    astm::gastm::ShortInteger,
    astm::gastm::Character,
    astm::gastm::Float,
    astm::gastm::Integer,
    astm::gastm::LongDouble,
    astm::gastm::WideCharacter,
    astm::gastm::Boolean,
    astm::gastm::String,
    astm::gastm::Byte,
    astm::gastm::Void,
    DerivesFrom,
    FormalParameterType,
    astm::gastm::ByReferenceFormalParameterType,
    astm::gastm::ByValueFormalParameterType,
    EnumLiteralDefinition,
    DataType,
    astm::gastm::FormalParameterType,
    astm::gastm::AggregateType,
    astm::gastm::ConstructedType,
    astm::gastm::EnumType,
    astm::gastm::ExceptionType,
    astm::gastm::NamedType,
    astm::gastm::PrimitiveType,
    MacroDefinition,
    DataDefinition,
    astm::gastm::FormalParameterDefinition,
    astm::gastm::VariableDefinition,
    astm::gastm::BitFieldDefinition,
    Expression,
    astm::gastm::RangeExpression,
    astm::gastm::BinaryExpression,
    astm::gastm::ArrayAccess,
    astm::gastm::AnnotationExpression,
    astm::gastm::NewExpression,
    astm::gastm::UnaryExpression,
    astm::gastm::AggregateExpression,
    astm::gastm::NameReference,
    astm::gastm::Literal,
    astm::gastm::FunctionCallExpression,
    astm::gastm::LabelAccess,
    astm::gastm::CastExpression,
    astm::gastm::ConditionalExpression,
    LabelType,
    NameSpaceType,
    AggregateType,
    astm::gastm::ClassType,
    astm::gastm::UnionType,
    astm::gastm::StructureType,
    astm::gastm::AnnotationType,
    NamedType,
    TypeDefinition,
    astm::gastm::AggregateTypeDefinition,
    astm::gastm::NamedTypeDefinition,
    Definition,
    astm::gastm::EntryDefinition,
    astm::gastm::SpecificTriggerDefinition,
    astm::gastm::EnumLiteralDefinition,
    astm::gastm::DataDefinition,
    TypeReference,
    astm::gastm::UnnamedTypeReference,
    astm::gastm::NamedTypeReference,
    Name,
    DeclarationOrDefinition,
    astm::gastm::Declaration,
    astm::gastm::Definition,
    VirtualSpecification,
    astm::gastm::PureVirtual,
    astm::gastm::Virtual,
    astm::gastm::NonVirtual,
    astm::gastm::FunctionMemberAttributes,
    FunctionScope,
    Statement,
    astm::gastm::ContinueStatement,
    astm::gastm::TerminateStatement,
    astm::gastm::ThrowStatement,
    astm::gastm::ReturnStatement,
    astm::gastm::SpecificSelectStatement,
    astm::gastm::EmptyStatement,
    astm::gastm::BreakStatement,
    astm::gastm::LabeledStatement,
    astm::gastm::LoopStatement,
    astm::gastm::JumpStatement,
    astm::gastm::DeleteStatement,
    astm::gastm::ExpressionStatement,
    astm::gastm::TryStatement,
    astm::gastm::DeclarationOrDefinitionStatement,
    astm::gastm::SwitchStatement,
    astm::gastm::IfStatement,
    astm::gastm::BlockStatement,
    FormalParameterDefinition,
    astm::gastm::FunctionDefinition,
    FunctionMemberAttributes,
    FormalParameterDeclaration,
    Declaration,
    astm::gastm::FunctionDeclaration,
    astm::gastm::VariableDeclaration,
    astm::gastm::FormalParameterDeclaration,
    SourceFile,
    GASTMSourceObject,
    astm::gastm::SourceLocation,
    astm::gastm::SourceFile,
    astm::gastm::ActualParameter,
    astm::gastm::BinaryOperator,
    astm::gastm::UnaryOperator,
    astm::gastm::AccessKind,
    Type,
    astm::gastm::FunctionType,
    astm::gastm::NameSpaceType,
    astm::gastm::TypeReference,
    astm::gastm::LabelType,
    astm::gastm::DataType,
    astm::gastm::StorageSpecification,
    GASTMSyntaxObject,
    astm::gastm::DefinitionObject,
    astm::gastm::Type,
    astm::gastm::PreprocessorElement,
    astm::gastm::Expression,
    astm::gastm::Statement,
    astm::gastm::OtherSyntaxObject,
    astm::gastm::GASTMSemanticObject,
    astm::gastm::GASTMSourceObject,
    astm::gastm::GASTMObject,
    ProgramScope,
    OtherSyntaxObject,
    astm::gastm::DerivesFrom,
    astm::gastm::SwitchCase,
    astm::gastm::CatchBlock,
    astm::gastm::Name,
    astm::gastm::Dimension,
    astm::gastm::FunctionMemberAttribute,
    astm::gastm::VirtualSpecification,
    astm::gastm::CompilationUnit,
    AnnotationExpression,
    PreprocessorElement,
    astm::gastm::MacroDefinition,
    astm::gastm::MacroCall,
    astm::gastm::IncludeUnit,
    astm::gastm::Comment,
    SourceLocation,
    GASTMObject,
    astm::gastm::GASTMSyntaxObject,
    Scope,
    astm::gastm::FunctionScope,
    astm::gastm::AggregateScope,
    astm::gastm::GlobalScope,
    astm::gastm::BlockScope,
    astm::gastm::ProgramScope,
    DefinitionObject,
    astm::gastm::DeclarationOrDefinition,
    astm::gastm::TypeDefinition,
    astm::gastm::NameSpaceDefinition,
    astm::gastm::LabelDefinition,
    GlobalScope,
    CompilationUnit,
    astm::sastm::DelphiInterfaceSection,
    astm::sastm::DelphiUnit,
    astm::sastm::DelphiImplementationSection,
    GASTMSemanticObject,
    astm::gastm::Scope,
    astm::gastm::Project,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_storagespecification_is_not_abstract():
    assert not inspect.isabstract(StorageSpecification)


def test_storagespecification_constructor_exists():
    assert callable(StorageSpecification.__init__)


def test_storagespecification_constructor_args():
    sig = inspect.signature(StorageSpecification.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::perclassmember_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::PerClassMember)


def test_astm::gastm::perclassmember_constructor_exists():
    assert callable(astm::gastm::PerClassMember.__init__)


def test_astm::gastm::perclassmember_constructor_args():
    sig = inspect.signature(astm::gastm::PerClassMember.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::filelocal_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::FileLocal)


def test_astm::gastm::filelocal_constructor_exists():
    assert callable(astm::gastm::FileLocal.__init__)


def test_astm::gastm::filelocal_constructor_args():
    sig = inspect.signature(astm::gastm::FileLocal.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::functionpersistent_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::FunctionPersistent)


def test_astm::gastm::functionpersistent_constructor_exists():
    assert callable(astm::gastm::FunctionPersistent.__init__)


def test_astm::gastm::functionpersistent_constructor_args():
    sig = inspect.signature(astm::gastm::FunctionPersistent.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::nodef_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::NoDef)


def test_astm::gastm::nodef_constructor_exists():
    assert callable(astm::gastm::NoDef.__init__)


def test_astm::gastm::nodef_constructor_args():
    sig = inspect.signature(astm::gastm::NoDef.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::external_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::External)


def test_astm::gastm::external_constructor_exists():
    assert callable(astm::gastm::External.__init__)


def test_astm::gastm::external_constructor_args():
    sig = inspect.signature(astm::gastm::External.__init__)
    params = list(sig.parameters.keys())



def test_actualparameter_is_not_abstract():
    assert not inspect.isabstract(ActualParameter)


def test_actualparameter_constructor_exists():
    assert callable(ActualParameter.__init__)


def test_actualparameter_constructor_args():
    sig = inspect.signature(ActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::actualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ActualParameterExpression)


def test_astm::gastm::actualparameterexpression_constructor_exists():
    assert callable(astm::gastm::ActualParameterExpression.__init__)


def test_astm::gastm::actualparameterexpression_constructor_args():
    sig = inspect.signature(astm::gastm::ActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::operatorassign_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::OperatorAssign)


def test_astm::gastm::operatorassign_constructor_exists():
    assert callable(astm::gastm::OperatorAssign.__init__)


def test_astm::gastm::operatorassign_constructor_args():
    sig = inspect.signature(astm::gastm::OperatorAssign.__init__)
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



def test_astm::gastm::typequalifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::TypeQualifiedIdentifierReference)


def test_astm::gastm::typequalifiedidentifierreference_constructor_exists():
    assert callable(astm::gastm::TypeQualifiedIdentifierReference.__init__)


def test_astm::gastm::typequalifiedidentifierreference_constructor_args():
    sig = inspect.signature(astm::gastm::TypeQualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::identifierreference_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::IdentifierReference)


def test_astm::gastm::identifierreference_constructor_exists():
    assert callable(astm::gastm::IdentifierReference.__init__)


def test_astm::gastm::identifierreference_constructor_args():
    sig = inspect.signature(astm::gastm::IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::qualifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::QualifiedIdentifierReference)


def test_astm::gastm::qualifiedidentifierreference_constructor_exists():
    assert callable(astm::gastm::QualifiedIdentifierReference.__init__)


def test_astm::gastm::qualifiedidentifierreference_constructor_args():
    sig = inspect.signature(astm::gastm::QualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_switchcase_is_not_abstract():
    assert not inspect.isabstract(SwitchCase)


def test_switchcase_constructor_exists():
    assert callable(SwitchCase.__init__)


def test_switchcase_constructor_args():
    sig = inspect.signature(SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::caseblock_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::CaseBlock)


def test_astm::gastm::caseblock_constructor_exists():
    assert callable(astm::gastm::CaseBlock.__init__)


def test_astm::gastm::caseblock_constructor_args():
    sig = inspect.signature(astm::gastm::CaseBlock.__init__)
    params = list(sig.parameters.keys())



def test_catchblock_is_not_abstract():
    assert not inspect.isabstract(CatchBlock)


def test_catchblock_constructor_exists():
    assert callable(CatchBlock.__init__)


def test_catchblock_constructor_args():
    sig = inspect.signature(CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::typescatchblock_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::TypesCatchBlock)


def test_astm::gastm::typescatchblock_constructor_exists():
    assert callable(astm::gastm::TypesCatchBlock.__init__)


def test_astm::gastm::typescatchblock_constructor_args():
    sig = inspect.signature(astm::gastm::TypesCatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::variablecatchblock_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::VariableCatchBlock)


def test_astm::gastm::variablecatchblock_constructor_exists():
    assert callable(astm::gastm::VariableCatchBlock.__init__)


def test_astm::gastm::variablecatchblock_constructor_args():
    sig = inspect.signature(astm::gastm::VariableCatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_loopstatement_is_not_abstract():
    assert not inspect.isabstract(LoopStatement)


def test_loopstatement_constructor_exists():
    assert callable(LoopStatement.__init__)


def test_loopstatement_constructor_args():
    sig = inspect.signature(LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::forstatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ForStatement)


def test_astm::gastm::forstatement_constructor_exists():
    assert callable(astm::gastm::ForStatement.__init__)


def test_astm::gastm::forstatement_constructor_args():
    sig = inspect.signature(astm::gastm::ForStatement.__init__)
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



def test_astm::gastm::arraytype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ArrayType)


def test_astm::gastm::arraytype_constructor_exists():
    assert callable(astm::gastm::ArrayType.__init__)


def test_astm::gastm::arraytype_constructor_args():
    sig = inspect.signature(astm::gastm::ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_aggregatescope_is_not_abstract():
    assert not inspect.isabstract(AggregateScope)


def test_aggregatescope_constructor_exists():
    assert callable(AggregateScope.__init__)


def test_aggregatescope_constructor_args():
    sig = inspect.signature(AggregateScope.__init__)
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



def test_astm::sastm::delphifunctioncallexpression_is_not_abstract():
    assert not inspect.isabstract(astm::sastm::DelphiFunctionCallExpression)


def test_astm::sastm::delphifunctioncallexpression_constructor_exists():
    assert callable(astm::sastm::DelphiFunctionCallExpression.__init__)


def test_astm::sastm::delphifunctioncallexpression_constructor_args():
    sig = inspect.signature(astm::sastm::DelphiFunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_blockstatement_is_not_abstract():
    assert not inspect.isabstract(BlockStatement)


def test_blockstatement_constructor_exists():
    assert callable(BlockStatement.__init__)


def test_blockstatement_constructor_args():
    sig = inspect.signature(BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::sastm::delphiwithstatement_is_not_abstract():
    assert not inspect.isabstract(astm::sastm::DelphiWithStatement)


def test_astm::sastm::delphiwithstatement_constructor_exists():
    assert callable(astm::sastm::DelphiWithStatement.__init__)


def test_astm::sastm::delphiwithstatement_constructor_args():
    sig = inspect.signature(astm::sastm::DelphiWithStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::sastm::delphiblockstatement_is_not_abstract():
    assert not inspect.isabstract(astm::sastm::DelphiBlockStatement)


def test_astm::sastm::delphiblockstatement_constructor_exists():
    assert callable(astm::sastm::DelphiBlockStatement.__init__)


def test_astm::sastm::delphiblockstatement_constructor_args():
    sig = inspect.signature(astm::sastm::DelphiBlockStatement.__init__)
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



def test_astm::gastm::multiply_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Multiply)


def test_astm::gastm::multiply_constructor_exists():
    assert callable(astm::gastm::Multiply.__init__)


def test_astm::gastm::multiply_constructor_args():
    sig = inspect.signature(astm::gastm::Multiply.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::subtract_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Subtract)


def test_astm::gastm::subtract_constructor_exists():
    assert callable(astm::gastm::Subtract.__init__)


def test_astm::gastm::subtract_constructor_args():
    sig = inspect.signature(astm::gastm::Subtract.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::add_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Add)


def test_astm::gastm::add_constructor_exists():
    assert callable(astm::gastm::Add.__init__)


def test_astm::gastm::add_constructor_args():
    sig = inspect.signature(astm::gastm::Add.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::specificconcatstring_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::SpecificConcatString)


def test_astm::gastm::specificconcatstring_constructor_exists():
    assert callable(astm::gastm::SpecificConcatString.__init__)


def test_astm::gastm::specificconcatstring_constructor_args():
    sig = inspect.signature(astm::gastm::SpecificConcatString.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::specificlike_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::SpecificLike)


def test_astm::gastm::specificlike_constructor_exists():
    assert callable(astm::gastm::SpecificLike.__init__)


def test_astm::gastm::specificlike_constructor_args():
    sig = inspect.signature(astm::gastm::SpecificLike.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::specificin_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::SpecificIn)


def test_astm::gastm::specificin_constructor_exists():
    assert callable(astm::gastm::SpecificIn.__init__)


def test_astm::gastm::specificin_constructor_args():
    sig = inspect.signature(astm::gastm::SpecificIn.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::specificgreaterequal_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::SpecificGreaterEqual)


def test_astm::gastm::specificgreaterequal_constructor_exists():
    assert callable(astm::gastm::SpecificGreaterEqual.__init__)


def test_astm::gastm::specificgreaterequal_constructor_args():
    sig = inspect.signature(astm::gastm::SpecificGreaterEqual.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::specificlessequal_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::SpecificLessEqual)


def test_astm::gastm::specificlessequal_constructor_exists():
    assert callable(astm::gastm::SpecificLessEqual.__init__)


def test_astm::gastm::specificlessequal_constructor_args():
    sig = inspect.signature(astm::gastm::SpecificLessEqual.__init__)
    params = list(sig.parameters.keys())



def test_actualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(ActualParameterExpression)


def test_actualparameterexpression_constructor_exists():
    assert callable(ActualParameterExpression.__init__)


def test_actualparameterexpression_constructor_args():
    sig = inspect.signature(ActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::byreferenceactualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ByReferenceActualParameterExpression)


def test_astm::gastm::byreferenceactualparameterexpression_constructor_exists():
    assert callable(astm::gastm::ByReferenceActualParameterExpression.__init__)


def test_astm::gastm::byreferenceactualparameterexpression_constructor_args():
    sig = inspect.signature(astm::gastm::ByReferenceActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::byvalueactualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ByValueActualParameterExpression)


def test_astm::gastm::byvalueactualparameterexpression_constructor_exists():
    assert callable(astm::gastm::ByValueActualParameterExpression.__init__)


def test_astm::gastm::byvalueactualparameterexpression_constructor_args():
    sig = inspect.signature(astm::gastm::ByValueActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::missingactualparameter_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::MissingActualParameter)


def test_astm::gastm::missingactualparameter_constructor_exists():
    assert callable(astm::gastm::MissingActualParameter.__init__)


def test_astm::gastm::missingactualparameter_constructor_args():
    sig = inspect.signature(astm::gastm::MissingActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::assign_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Assign)


def test_astm::gastm::assign_constructor_exists():
    assert callable(astm::gastm::Assign.__init__)


def test_astm::gastm::assign_constructor_args():
    sig = inspect.signature(astm::gastm::Assign.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::bitrightshift_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::BitRightShift)


def test_astm::gastm::bitrightshift_constructor_exists():
    assert callable(astm::gastm::BitRightShift.__init__)


def test_astm::gastm::bitrightshift_constructor_args():
    sig = inspect.signature(astm::gastm::BitRightShift.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::bitleftshift_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::BitLeftShift)


def test_astm::gastm::bitleftshift_constructor_exists():
    assert callable(astm::gastm::BitLeftShift.__init__)


def test_astm::gastm::bitleftshift_constructor_args():
    sig = inspect.signature(astm::gastm::BitLeftShift.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::bitxor_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::BitXor)


def test_astm::gastm::bitxor_constructor_exists():
    assert callable(astm::gastm::BitXor.__init__)


def test_astm::gastm::bitxor_constructor_args():
    sig = inspect.signature(astm::gastm::BitXor.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::bitor_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::BitOr)


def test_astm::gastm::bitor_constructor_exists():
    assert callable(astm::gastm::BitOr.__init__)


def test_astm::gastm::bitor_constructor_args():
    sig = inspect.signature(astm::gastm::BitOr.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::bitand_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::BitAnd)


def test_astm::gastm::bitand_constructor_exists():
    assert callable(astm::gastm::BitAnd.__init__)


def test_astm::gastm::bitand_constructor_args():
    sig = inspect.signature(astm::gastm::BitAnd.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::notless_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::NotLess)


def test_astm::gastm::notless_constructor_exists():
    assert callable(astm::gastm::NotLess.__init__)


def test_astm::gastm::notless_constructor_args():
    sig = inspect.signature(astm::gastm::NotLess.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::less_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Less)


def test_astm::gastm::less_constructor_exists():
    assert callable(astm::gastm::Less.__init__)


def test_astm::gastm::less_constructor_args():
    sig = inspect.signature(astm::gastm::Less.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::notgreater_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::NotGreater)


def test_astm::gastm::notgreater_constructor_exists():
    assert callable(astm::gastm::NotGreater.__init__)


def test_astm::gastm::notgreater_constructor_args():
    sig = inspect.signature(astm::gastm::NotGreater.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::greater_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Greater)


def test_astm::gastm::greater_constructor_exists():
    assert callable(astm::gastm::Greater.__init__)


def test_astm::gastm::greater_constructor_args():
    sig = inspect.signature(astm::gastm::Greater.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::notequal_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::NotEqual)


def test_astm::gastm::notequal_constructor_exists():
    assert callable(astm::gastm::NotEqual.__init__)


def test_astm::gastm::notequal_constructor_args():
    sig = inspect.signature(astm::gastm::NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::equal_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Equal)


def test_astm::gastm::equal_constructor_exists():
    assert callable(astm::gastm::Equal.__init__)


def test_astm::gastm::equal_constructor_args():
    sig = inspect.signature(astm::gastm::Equal.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::or_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Or)


def test_astm::gastm::or_constructor_exists():
    assert callable(astm::gastm::Or.__init__)


def test_astm::gastm::or_constructor_args():
    sig = inspect.signature(astm::gastm::Or.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::and_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::And)


def test_astm::gastm::and_constructor_exists():
    assert callable(astm::gastm::And.__init__)


def test_astm::gastm::and_constructor_args():
    sig = inspect.signature(astm::gastm::And.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::exponent_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Exponent)


def test_astm::gastm::exponent_constructor_exists():
    assert callable(astm::gastm::Exponent.__init__)


def test_astm::gastm::exponent_constructor_args():
    sig = inspect.signature(astm::gastm::Exponent.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::modulus_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Modulus)


def test_astm::gastm::modulus_constructor_exists():
    assert callable(astm::gastm::Modulus.__init__)


def test_astm::gastm::modulus_constructor_args():
    sig = inspect.signature(astm::gastm::Modulus.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::divide_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Divide)


def test_astm::gastm::divide_constructor_exists():
    assert callable(astm::gastm::Divide.__init__)


def test_astm::gastm::divide_constructor_args():
    sig = inspect.signature(astm::gastm::Divide.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::pointertype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::PointerType)


def test_astm::gastm::pointertype_constructor_exists():
    assert callable(astm::gastm::PointerType.__init__)


def test_astm::gastm::pointertype_constructor_args():
    sig = inspect.signature(astm::gastm::PointerType.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::collectiontype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::CollectionType)


def test_astm::gastm::collectiontype_constructor_exists():
    assert callable(astm::gastm::CollectionType.__init__)


def test_astm::gastm::collectiontype_constructor_args():
    sig = inspect.signature(astm::gastm::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::decrement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Decrement)


def test_astm::gastm::decrement_constructor_exists():
    assert callable(astm::gastm::Decrement.__init__)


def test_astm::gastm::decrement_constructor_args():
    sig = inspect.signature(astm::gastm::Decrement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::increment_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Increment)


def test_astm::gastm::increment_constructor_exists():
    assert callable(astm::gastm::Increment.__init__)


def test_astm::gastm::increment_constructor_args():
    sig = inspect.signature(astm::gastm::Increment.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::not_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Not)


def test_astm::gastm::not_constructor_exists():
    assert callable(astm::gastm::Not.__init__)


def test_astm::gastm::not_constructor_args():
    sig = inspect.signature(astm::gastm::Not.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::bitnot_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::BitNot)


def test_astm::gastm::bitnot_constructor_exists():
    assert callable(astm::gastm::BitNot.__init__)


def test_astm::gastm::bitnot_constructor_args():
    sig = inspect.signature(astm::gastm::BitNot.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::postdecrement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::PostDecrement)


def test_astm::gastm::postdecrement_constructor_exists():
    assert callable(astm::gastm::PostDecrement.__init__)


def test_astm::gastm::postdecrement_constructor_args():
    sig = inspect.signature(astm::gastm::PostDecrement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::deref_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Deref)


def test_astm::gastm::deref_constructor_exists():
    assert callable(astm::gastm::Deref.__init__)


def test_astm::gastm::deref_constructor_args():
    sig = inspect.signature(astm::gastm::Deref.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::addressof_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::AddressOf)


def test_astm::gastm::addressof_constructor_exists():
    assert callable(astm::gastm::AddressOf.__init__)


def test_astm::gastm::addressof_constructor_args():
    sig = inspect.signature(astm::gastm::AddressOf.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::negate_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Negate)


def test_astm::gastm::negate_constructor_exists():
    assert callable(astm::gastm::Negate.__init__)


def test_astm::gastm::negate_constructor_args():
    sig = inspect.signature(astm::gastm::Negate.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::postincrement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::PostIncrement)


def test_astm::gastm::postincrement_constructor_exists():
    assert callable(astm::gastm::PostIncrement.__init__)


def test_astm::gastm::postincrement_constructor_args():
    sig = inspect.signature(astm::gastm::PostIncrement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::unaryplus_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::UnaryPlus)


def test_astm::gastm::unaryplus_constructor_exists():
    assert callable(astm::gastm::UnaryPlus.__init__)


def test_astm::gastm::unaryplus_constructor_args():
    sig = inspect.signature(astm::gastm::UnaryPlus.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::stringliteral_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::StringLiteral)


def test_astm::gastm::stringliteral_constructor_exists():
    assert callable(astm::gastm::StringLiteral.__init__)


def test_astm::gastm::stringliteral_constructor_args():
    sig = inspect.signature(astm::gastm::StringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::realliteral_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::RealLiteral)


def test_astm::gastm::realliteral_constructor_exists():
    assert callable(astm::gastm::RealLiteral.__init__)


def test_astm::gastm::realliteral_constructor_args():
    sig = inspect.signature(astm::gastm::RealLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::charliteral_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::CharLiteral)


def test_astm::gastm::charliteral_constructor_exists():
    assert callable(astm::gastm::CharLiteral.__init__)


def test_astm::gastm::charliteral_constructor_args():
    sig = inspect.signature(astm::gastm::CharLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::bitliteral_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::BitLiteral)


def test_astm::gastm::bitliteral_constructor_exists():
    assert callable(astm::gastm::BitLiteral.__init__)


def test_astm::gastm::bitliteral_constructor_args():
    sig = inspect.signature(astm::gastm::BitLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::BooleanLiteral)


def test_astm::gastm::booleanliteral_constructor_exists():
    assert callable(astm::gastm::BooleanLiteral.__init__)


def test_astm::gastm::booleanliteral_constructor_args():
    sig = inspect.signature(astm::gastm::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::integerliteral_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::IntegerLiteral)


def test_astm::gastm::integerliteral_constructor_exists():
    assert callable(astm::gastm::IntegerLiteral.__init__)


def test_astm::gastm::integerliteral_constructor_args():
    sig = inspect.signature(astm::gastm::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())



def test_qualifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(QualifiedIdentifierReference)


def test_qualifiedidentifierreference_constructor_exists():
    assert callable(QualifiedIdentifierReference.__init__)


def test_qualifiedidentifierreference_constructor_args():
    sig = inspect.signature(QualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::qualifiedoverdata_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::QualifiedOverData)


def test_astm::gastm::qualifiedoverdata_constructor_exists():
    assert callable(astm::gastm::QualifiedOverData.__init__)


def test_astm::gastm::qualifiedoverdata_constructor_args():
    sig = inspect.signature(astm::gastm::QualifiedOverData.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::qualifiedoverpointer_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::QualifiedOverPointer)


def test_astm::gastm::qualifiedoverpointer_constructor_exists():
    assert callable(astm::gastm::QualifiedOverPointer.__init__)


def test_astm::gastm::qualifiedoverpointer_constructor_args():
    sig = inspect.signature(astm::gastm::QualifiedOverPointer.__init__)
    params = list(sig.parameters.keys())



def test_forstatement_is_not_abstract():
    assert not inspect.isabstract(ForStatement)


def test_forstatement_constructor_exists():
    assert callable(ForStatement.__init__)


def test_forstatement_constructor_args():
    sig = inspect.signature(ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::forcheckafterstatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ForCheckAfterStatement)


def test_astm::gastm::forcheckafterstatement_constructor_exists():
    assert callable(astm::gastm::ForCheckAfterStatement.__init__)


def test_astm::gastm::forcheckafterstatement_constructor_args():
    sig = inspect.signature(astm::gastm::ForCheckAfterStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::forcheckbeforestatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ForCheckBeforeStatement)


def test_astm::gastm::forcheckbeforestatement_constructor_exists():
    assert callable(astm::gastm::ForCheckBeforeStatement.__init__)


def test_astm::gastm::forcheckbeforestatement_constructor_args():
    sig = inspect.signature(astm::gastm::ForCheckBeforeStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::dowhilestatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::DoWhileStatement)


def test_astm::gastm::dowhilestatement_constructor_exists():
    assert callable(astm::gastm::DoWhileStatement.__init__)


def test_astm::gastm::dowhilestatement_constructor_args():
    sig = inspect.signature(astm::gastm::DoWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::whilestatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::WhileStatement)


def test_astm::gastm::whilestatement_constructor_exists():
    assert callable(astm::gastm::WhileStatement.__init__)


def test_astm::gastm::whilestatement_constructor_args():
    sig = inspect.signature(astm::gastm::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::defaultblock_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::DefaultBlock)


def test_astm::gastm::defaultblock_constructor_exists():
    assert callable(astm::gastm::DefaultBlock.__init__)


def test_astm::gastm::defaultblock_constructor_args():
    sig = inspect.signature(astm::gastm::DefaultBlock.__init__)
    params = list(sig.parameters.keys())



def test_accesskind_is_not_abstract():
    assert not inspect.isabstract(AccessKind)


def test_accesskind_constructor_exists():
    assert callable(AccessKind.__init__)


def test_accesskind_constructor_args():
    sig = inspect.signature(AccessKind.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::private_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Private)


def test_astm::gastm::private_constructor_exists():
    assert callable(astm::gastm::Private.__init__)


def test_astm::gastm::private_constructor_args():
    sig = inspect.signature(astm::gastm::Private.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::protected_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Protected)


def test_astm::gastm::protected_constructor_exists():
    assert callable(astm::gastm::Protected.__init__)


def test_astm::gastm::protected_constructor_args():
    sig = inspect.signature(astm::gastm::Protected.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::public_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Public)


def test_astm::gastm::public_constructor_exists():
    assert callable(astm::gastm::Public.__init__)


def test_astm::gastm::public_constructor_args():
    sig = inspect.signature(astm::gastm::Public.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::rangetype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::RangeType)


def test_astm::gastm::rangetype_constructor_exists():
    assert callable(astm::gastm::RangeType.__init__)


def test_astm::gastm::rangetype_constructor_args():
    sig = inspect.signature(astm::gastm::RangeType.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::referencetype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ReferenceType)


def test_astm::gastm::referencetype_constructor_exists():
    assert callable(astm::gastm::ReferenceType.__init__)


def test_astm::gastm::referencetype_constructor_args():
    sig = inspect.signature(astm::gastm::ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::longinteger_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::LongInteger)


def test_astm::gastm::longinteger_constructor_exists():
    assert callable(astm::gastm::LongInteger.__init__)


def test_astm::gastm::longinteger_constructor_args():
    sig = inspect.signature(astm::gastm::LongInteger.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::double_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Double)


def test_astm::gastm::double_constructor_exists():
    assert callable(astm::gastm::Double.__init__)


def test_astm::gastm::double_constructor_args():
    sig = inspect.signature(astm::gastm::Double.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::shortinteger_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ShortInteger)


def test_astm::gastm::shortinteger_constructor_exists():
    assert callable(astm::gastm::ShortInteger.__init__)


def test_astm::gastm::shortinteger_constructor_args():
    sig = inspect.signature(astm::gastm::ShortInteger.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::character_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Character)


def test_astm::gastm::character_constructor_exists():
    assert callable(astm::gastm::Character.__init__)


def test_astm::gastm::character_constructor_args():
    sig = inspect.signature(astm::gastm::Character.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::float_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Float)


def test_astm::gastm::float_constructor_exists():
    assert callable(astm::gastm::Float.__init__)


def test_astm::gastm::float_constructor_args():
    sig = inspect.signature(astm::gastm::Float.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::integer_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Integer)


def test_astm::gastm::integer_constructor_exists():
    assert callable(astm::gastm::Integer.__init__)


def test_astm::gastm::integer_constructor_args():
    sig = inspect.signature(astm::gastm::Integer.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::longdouble_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::LongDouble)


def test_astm::gastm::longdouble_constructor_exists():
    assert callable(astm::gastm::LongDouble.__init__)


def test_astm::gastm::longdouble_constructor_args():
    sig = inspect.signature(astm::gastm::LongDouble.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::widecharacter_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::WideCharacter)


def test_astm::gastm::widecharacter_constructor_exists():
    assert callable(astm::gastm::WideCharacter.__init__)


def test_astm::gastm::widecharacter_constructor_args():
    sig = inspect.signature(astm::gastm::WideCharacter.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::boolean_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Boolean)


def test_astm::gastm::boolean_constructor_exists():
    assert callable(astm::gastm::Boolean.__init__)


def test_astm::gastm::boolean_constructor_args():
    sig = inspect.signature(astm::gastm::Boolean.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::string_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::String)


def test_astm::gastm::string_constructor_exists():
    assert callable(astm::gastm::String.__init__)


def test_astm::gastm::string_constructor_args():
    sig = inspect.signature(astm::gastm::String.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::byte_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Byte)


def test_astm::gastm::byte_constructor_exists():
    assert callable(astm::gastm::Byte.__init__)


def test_astm::gastm::byte_constructor_args():
    sig = inspect.signature(astm::gastm::Byte.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::void_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Void)


def test_astm::gastm::void_constructor_exists():
    assert callable(astm::gastm::Void.__init__)


def test_astm::gastm::void_constructor_args():
    sig = inspect.signature(astm::gastm::Void.__init__)
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



def test_astm::gastm::byreferenceformalparametertype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ByReferenceFormalParameterType)


def test_astm::gastm::byreferenceformalparametertype_constructor_exists():
    assert callable(astm::gastm::ByReferenceFormalParameterType.__init__)


def test_astm::gastm::byreferenceformalparametertype_constructor_args():
    sig = inspect.signature(astm::gastm::ByReferenceFormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::byvalueformalparametertype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ByValueFormalParameterType)


def test_astm::gastm::byvalueformalparametertype_constructor_exists():
    assert callable(astm::gastm::ByValueFormalParameterType.__init__)


def test_astm::gastm::byvalueformalparametertype_constructor_args():
    sig = inspect.signature(astm::gastm::ByValueFormalParameterType.__init__)
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



def test_astm::gastm::formalparametertype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::FormalParameterType)


def test_astm::gastm::formalparametertype_constructor_exists():
    assert callable(astm::gastm::FormalParameterType.__init__)


def test_astm::gastm::formalparametertype_constructor_args():
    sig = inspect.signature(astm::gastm::FormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::aggregatetype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::AggregateType)


def test_astm::gastm::aggregatetype_constructor_exists():
    assert callable(astm::gastm::AggregateType.__init__)


def test_astm::gastm::aggregatetype_constructor_args():
    sig = inspect.signature(astm::gastm::AggregateType.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::constructedtype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ConstructedType)


def test_astm::gastm::constructedtype_constructor_exists():
    assert callable(astm::gastm::ConstructedType.__init__)


def test_astm::gastm::constructedtype_constructor_args():
    sig = inspect.signature(astm::gastm::ConstructedType.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::enumtype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::EnumType)


def test_astm::gastm::enumtype_constructor_exists():
    assert callable(astm::gastm::EnumType.__init__)


def test_astm::gastm::enumtype_constructor_args():
    sig = inspect.signature(astm::gastm::EnumType.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::exceptiontype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ExceptionType)


def test_astm::gastm::exceptiontype_constructor_exists():
    assert callable(astm::gastm::ExceptionType.__init__)


def test_astm::gastm::exceptiontype_constructor_args():
    sig = inspect.signature(astm::gastm::ExceptionType.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::namedtype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::NamedType)


def test_astm::gastm::namedtype_constructor_exists():
    assert callable(astm::gastm::NamedType.__init__)


def test_astm::gastm::namedtype_constructor_args():
    sig = inspect.signature(astm::gastm::NamedType.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::primitivetype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::PrimitiveType)


def test_astm::gastm::primitivetype_constructor_exists():
    assert callable(astm::gastm::PrimitiveType.__init__)


def test_astm::gastm::primitivetype_constructor_args():
    sig = inspect.signature(astm::gastm::PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "isSigned" in params, "Missing parameter 'isSigned'"

def test_astm::gastm::primitivetype_has_isSigned():
    assert hasattr(astm::gastm::PrimitiveType, "isSigned")
    descriptor = None
    for klass in astm::gastm::PrimitiveType.__mro__:
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



def test_astm::gastm::formalparameterdefinition_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::FormalParameterDefinition)


def test_astm::gastm::formalparameterdefinition_constructor_exists():
    assert callable(astm::gastm::FormalParameterDefinition.__init__)


def test_astm::gastm::formalparameterdefinition_constructor_args():
    sig = inspect.signature(astm::gastm::FormalParameterDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::variabledefinition_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::VariableDefinition)


def test_astm::gastm::variabledefinition_constructor_exists():
    assert callable(astm::gastm::VariableDefinition.__init__)


def test_astm::gastm::variabledefinition_constructor_args():
    sig = inspect.signature(astm::gastm::VariableDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::bitfielddefinition_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::BitFieldDefinition)


def test_astm::gastm::bitfielddefinition_constructor_exists():
    assert callable(astm::gastm::BitFieldDefinition.__init__)


def test_astm::gastm::bitfielddefinition_constructor_args():
    sig = inspect.signature(astm::gastm::BitFieldDefinition.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::rangeexpression_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::RangeExpression)


def test_astm::gastm::rangeexpression_constructor_exists():
    assert callable(astm::gastm::RangeExpression.__init__)


def test_astm::gastm::rangeexpression_constructor_args():
    sig = inspect.signature(astm::gastm::RangeExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::BinaryExpression)


def test_astm::gastm::binaryexpression_constructor_exists():
    assert callable(astm::gastm::BinaryExpression.__init__)


def test_astm::gastm::binaryexpression_constructor_args():
    sig = inspect.signature(astm::gastm::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::arrayaccess_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ArrayAccess)


def test_astm::gastm::arrayaccess_constructor_exists():
    assert callable(astm::gastm::ArrayAccess.__init__)


def test_astm::gastm::arrayaccess_constructor_args():
    sig = inspect.signature(astm::gastm::ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::annotationexpression_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::AnnotationExpression)


def test_astm::gastm::annotationexpression_constructor_exists():
    assert callable(astm::gastm::AnnotationExpression.__init__)


def test_astm::gastm::annotationexpression_constructor_args():
    sig = inspect.signature(astm::gastm::AnnotationExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::newexpression_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::NewExpression)


def test_astm::gastm::newexpression_constructor_exists():
    assert callable(astm::gastm::NewExpression.__init__)


def test_astm::gastm::newexpression_constructor_args():
    sig = inspect.signature(astm::gastm::NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::UnaryExpression)


def test_astm::gastm::unaryexpression_constructor_exists():
    assert callable(astm::gastm::UnaryExpression.__init__)


def test_astm::gastm::unaryexpression_constructor_args():
    sig = inspect.signature(astm::gastm::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::aggregateexpression_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::AggregateExpression)


def test_astm::gastm::aggregateexpression_constructor_exists():
    assert callable(astm::gastm::AggregateExpression.__init__)


def test_astm::gastm::aggregateexpression_constructor_args():
    sig = inspect.signature(astm::gastm::AggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::namereference_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::NameReference)


def test_astm::gastm::namereference_constructor_exists():
    assert callable(astm::gastm::NameReference.__init__)


def test_astm::gastm::namereference_constructor_args():
    sig = inspect.signature(astm::gastm::NameReference.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::literal_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Literal)


def test_astm::gastm::literal_constructor_exists():
    assert callable(astm::gastm::Literal.__init__)


def test_astm::gastm::literal_constructor_args():
    sig = inspect.signature(astm::gastm::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_astm::gastm::literal_has_value():
    assert hasattr(astm::gastm::Literal, "value")
    descriptor = None
    for klass in astm::gastm::Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_astm::gastm::functioncallexpression_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::FunctionCallExpression)


def test_astm::gastm::functioncallexpression_constructor_exists():
    assert callable(astm::gastm::FunctionCallExpression.__init__)


def test_astm::gastm::functioncallexpression_constructor_args():
    sig = inspect.signature(astm::gastm::FunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::labelaccess_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::LabelAccess)


def test_astm::gastm::labelaccess_constructor_exists():
    assert callable(astm::gastm::LabelAccess.__init__)


def test_astm::gastm::labelaccess_constructor_args():
    sig = inspect.signature(astm::gastm::LabelAccess.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::castexpression_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::CastExpression)


def test_astm::gastm::castexpression_constructor_exists():
    assert callable(astm::gastm::CastExpression.__init__)


def test_astm::gastm::castexpression_constructor_args():
    sig = inspect.signature(astm::gastm::CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ConditionalExpression)


def test_astm::gastm::conditionalexpression_constructor_exists():
    assert callable(astm::gastm::ConditionalExpression.__init__)


def test_astm::gastm::conditionalexpression_constructor_args():
    sig = inspect.signature(astm::gastm::ConditionalExpression.__init__)
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



def test_astm::gastm::classtype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ClassType)


def test_astm::gastm::classtype_constructor_exists():
    assert callable(astm::gastm::ClassType.__init__)


def test_astm::gastm::classtype_constructor_args():
    sig = inspect.signature(astm::gastm::ClassType.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::uniontype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::UnionType)


def test_astm::gastm::uniontype_constructor_exists():
    assert callable(astm::gastm::UnionType.__init__)


def test_astm::gastm::uniontype_constructor_args():
    sig = inspect.signature(astm::gastm::UnionType.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::structuretype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::StructureType)


def test_astm::gastm::structuretype_constructor_exists():
    assert callable(astm::gastm::StructureType.__init__)


def test_astm::gastm::structuretype_constructor_args():
    sig = inspect.signature(astm::gastm::StructureType.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::annotationtype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::AnnotationType)


def test_astm::gastm::annotationtype_constructor_exists():
    assert callable(astm::gastm::AnnotationType.__init__)


def test_astm::gastm::annotationtype_constructor_args():
    sig = inspect.signature(astm::gastm::AnnotationType.__init__)
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



def test_astm::gastm::aggregatetypedefinition_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::AggregateTypeDefinition)


def test_astm::gastm::aggregatetypedefinition_constructor_exists():
    assert callable(astm::gastm::AggregateTypeDefinition.__init__)


def test_astm::gastm::aggregatetypedefinition_constructor_args():
    sig = inspect.signature(astm::gastm::AggregateTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::namedtypedefinition_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::NamedTypeDefinition)


def test_astm::gastm::namedtypedefinition_constructor_exists():
    assert callable(astm::gastm::NamedTypeDefinition.__init__)


def test_astm::gastm::namedtypedefinition_constructor_args():
    sig = inspect.signature(astm::gastm::NamedTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::entrydefinition_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::EntryDefinition)


def test_astm::gastm::entrydefinition_constructor_exists():
    assert callable(astm::gastm::EntryDefinition.__init__)


def test_astm::gastm::entrydefinition_constructor_args():
    sig = inspect.signature(astm::gastm::EntryDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::specifictriggerdefinition_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::SpecificTriggerDefinition)


def test_astm::gastm::specifictriggerdefinition_constructor_exists():
    assert callable(astm::gastm::SpecificTriggerDefinition.__init__)


def test_astm::gastm::specifictriggerdefinition_constructor_args():
    sig = inspect.signature(astm::gastm::SpecificTriggerDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::enumliteraldefinition_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::EnumLiteralDefinition)


def test_astm::gastm::enumliteraldefinition_constructor_exists():
    assert callable(astm::gastm::EnumLiteralDefinition.__init__)


def test_astm::gastm::enumliteraldefinition_constructor_args():
    sig = inspect.signature(astm::gastm::EnumLiteralDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::datadefinition_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::DataDefinition)


def test_astm::gastm::datadefinition_constructor_exists():
    assert callable(astm::gastm::DataDefinition.__init__)


def test_astm::gastm::datadefinition_constructor_args():
    sig = inspect.signature(astm::gastm::DataDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "isMutable" in params, "Missing parameter 'isMutable'"

def test_astm::gastm::datadefinition_has_isMutable():
    assert hasattr(astm::gastm::DataDefinition, "isMutable")
    descriptor = None
    for klass in astm::gastm::DataDefinition.__mro__:
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



def test_astm::gastm::unnamedtypereference_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::UnnamedTypeReference)


def test_astm::gastm::unnamedtypereference_constructor_exists():
    assert callable(astm::gastm::UnnamedTypeReference.__init__)


def test_astm::gastm::unnamedtypereference_constructor_args():
    sig = inspect.signature(astm::gastm::UnnamedTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::namedtypereference_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::NamedTypeReference)


def test_astm::gastm::namedtypereference_constructor_exists():
    assert callable(astm::gastm::NamedTypeReference.__init__)


def test_astm::gastm::namedtypereference_constructor_args():
    sig = inspect.signature(astm::gastm::NamedTypeReference.__init__)
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



def test_astm::gastm::declaration_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Declaration)


def test_astm::gastm::declaration_constructor_exists():
    assert callable(astm::gastm::Declaration.__init__)


def test_astm::gastm::declaration_constructor_args():
    sig = inspect.signature(astm::gastm::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::definition_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Definition)


def test_astm::gastm::definition_constructor_exists():
    assert callable(astm::gastm::Definition.__init__)


def test_astm::gastm::definition_constructor_args():
    sig = inspect.signature(astm::gastm::Definition.__init__)
    params = list(sig.parameters.keys())



def test_virtualspecification_is_not_abstract():
    assert not inspect.isabstract(VirtualSpecification)


def test_virtualspecification_constructor_exists():
    assert callable(VirtualSpecification.__init__)


def test_virtualspecification_constructor_args():
    sig = inspect.signature(VirtualSpecification.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::purevirtual_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::PureVirtual)


def test_astm::gastm::purevirtual_constructor_exists():
    assert callable(astm::gastm::PureVirtual.__init__)


def test_astm::gastm::purevirtual_constructor_args():
    sig = inspect.signature(astm::gastm::PureVirtual.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::virtual_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Virtual)


def test_astm::gastm::virtual_constructor_exists():
    assert callable(astm::gastm::Virtual.__init__)


def test_astm::gastm::virtual_constructor_args():
    sig = inspect.signature(astm::gastm::Virtual.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::nonvirtual_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::NonVirtual)


def test_astm::gastm::nonvirtual_constructor_exists():
    assert callable(astm::gastm::NonVirtual.__init__)


def test_astm::gastm::nonvirtual_constructor_args():
    sig = inspect.signature(astm::gastm::NonVirtual.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::functionmemberattributes_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::FunctionMemberAttributes)


def test_astm::gastm::functionmemberattributes_constructor_exists():
    assert callable(astm::gastm::FunctionMemberAttributes.__init__)


def test_astm::gastm::functionmemberattributes_constructor_args():
    sig = inspect.signature(astm::gastm::FunctionMemberAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "isThisConst" in params, "Missing parameter 'isThisConst'"
    assert "isFriend" in params, "Missing parameter 'isFriend'"
    assert "isInline" in params, "Missing parameter 'isInline'"

def test_astm::gastm::functionmemberattributes_has_isThisConst():
    assert hasattr(astm::gastm::FunctionMemberAttributes, "isThisConst")
    descriptor = None
    for klass in astm::gastm::FunctionMemberAttributes.__mro__:
        if "isThisConst" in klass.__dict__:
            descriptor = klass.__dict__["isThisConst"]
            break
    assert isinstance(descriptor, property)

def test_astm::gastm::functionmemberattributes_has_isFriend():
    assert hasattr(astm::gastm::FunctionMemberAttributes, "isFriend")
    descriptor = None
    for klass in astm::gastm::FunctionMemberAttributes.__mro__:
        if "isFriend" in klass.__dict__:
            descriptor = klass.__dict__["isFriend"]
            break
    assert isinstance(descriptor, property)

def test_astm::gastm::functionmemberattributes_has_isInline():
    assert hasattr(astm::gastm::FunctionMemberAttributes, "isInline")
    descriptor = None
    for klass in astm::gastm::FunctionMemberAttributes.__mro__:
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



def test_astm::gastm::continuestatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ContinueStatement)


def test_astm::gastm::continuestatement_constructor_exists():
    assert callable(astm::gastm::ContinueStatement.__init__)


def test_astm::gastm::continuestatement_constructor_args():
    sig = inspect.signature(astm::gastm::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::terminatestatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::TerminateStatement)


def test_astm::gastm::terminatestatement_constructor_exists():
    assert callable(astm::gastm::TerminateStatement.__init__)


def test_astm::gastm::terminatestatement_constructor_args():
    sig = inspect.signature(astm::gastm::TerminateStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::throwstatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ThrowStatement)


def test_astm::gastm::throwstatement_constructor_exists():
    assert callable(astm::gastm::ThrowStatement.__init__)


def test_astm::gastm::throwstatement_constructor_args():
    sig = inspect.signature(astm::gastm::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::returnstatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ReturnStatement)


def test_astm::gastm::returnstatement_constructor_exists():
    assert callable(astm::gastm::ReturnStatement.__init__)


def test_astm::gastm::returnstatement_constructor_args():
    sig = inspect.signature(astm::gastm::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::specificselectstatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::SpecificSelectStatement)


def test_astm::gastm::specificselectstatement_constructor_exists():
    assert callable(astm::gastm::SpecificSelectStatement.__init__)


def test_astm::gastm::specificselectstatement_constructor_args():
    sig = inspect.signature(astm::gastm::SpecificSelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::emptystatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::EmptyStatement)


def test_astm::gastm::emptystatement_constructor_exists():
    assert callable(astm::gastm::EmptyStatement.__init__)


def test_astm::gastm::emptystatement_constructor_args():
    sig = inspect.signature(astm::gastm::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::breakstatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::BreakStatement)


def test_astm::gastm::breakstatement_constructor_exists():
    assert callable(astm::gastm::BreakStatement.__init__)


def test_astm::gastm::breakstatement_constructor_args():
    sig = inspect.signature(astm::gastm::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::labeledstatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::LabeledStatement)


def test_astm::gastm::labeledstatement_constructor_exists():
    assert callable(astm::gastm::LabeledStatement.__init__)


def test_astm::gastm::labeledstatement_constructor_args():
    sig = inspect.signature(astm::gastm::LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::loopstatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::LoopStatement)


def test_astm::gastm::loopstatement_constructor_exists():
    assert callable(astm::gastm::LoopStatement.__init__)


def test_astm::gastm::loopstatement_constructor_args():
    sig = inspect.signature(astm::gastm::LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::jumpstatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::JumpStatement)


def test_astm::gastm::jumpstatement_constructor_exists():
    assert callable(astm::gastm::JumpStatement.__init__)


def test_astm::gastm::jumpstatement_constructor_args():
    sig = inspect.signature(astm::gastm::JumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::deletestatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::DeleteStatement)


def test_astm::gastm::deletestatement_constructor_exists():
    assert callable(astm::gastm::DeleteStatement.__init__)


def test_astm::gastm::deletestatement_constructor_args():
    sig = inspect.signature(astm::gastm::DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ExpressionStatement)


def test_astm::gastm::expressionstatement_constructor_exists():
    assert callable(astm::gastm::ExpressionStatement.__init__)


def test_astm::gastm::expressionstatement_constructor_args():
    sig = inspect.signature(astm::gastm::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::trystatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::TryStatement)


def test_astm::gastm::trystatement_constructor_exists():
    assert callable(astm::gastm::TryStatement.__init__)


def test_astm::gastm::trystatement_constructor_args():
    sig = inspect.signature(astm::gastm::TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::declarationordefinitionstatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::DeclarationOrDefinitionStatement)


def test_astm::gastm::declarationordefinitionstatement_constructor_exists():
    assert callable(astm::gastm::DeclarationOrDefinitionStatement.__init__)


def test_astm::gastm::declarationordefinitionstatement_constructor_args():
    sig = inspect.signature(astm::gastm::DeclarationOrDefinitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::switchstatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::SwitchStatement)


def test_astm::gastm::switchstatement_constructor_exists():
    assert callable(astm::gastm::SwitchStatement.__init__)


def test_astm::gastm::switchstatement_constructor_args():
    sig = inspect.signature(astm::gastm::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::ifstatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::IfStatement)


def test_astm::gastm::ifstatement_constructor_exists():
    assert callable(astm::gastm::IfStatement.__init__)


def test_astm::gastm::ifstatement_constructor_args():
    sig = inspect.signature(astm::gastm::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::blockstatement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::BlockStatement)


def test_astm::gastm::blockstatement_constructor_exists():
    assert callable(astm::gastm::BlockStatement.__init__)


def test_astm::gastm::blockstatement_constructor_args():
    sig = inspect.signature(astm::gastm::BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_formalparameterdefinition_is_not_abstract():
    assert not inspect.isabstract(FormalParameterDefinition)


def test_formalparameterdefinition_constructor_exists():
    assert callable(FormalParameterDefinition.__init__)


def test_formalparameterdefinition_constructor_args():
    sig = inspect.signature(FormalParameterDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::functiondefinition_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::FunctionDefinition)


def test_astm::gastm::functiondefinition_constructor_exists():
    assert callable(astm::gastm::FunctionDefinition.__init__)


def test_astm::gastm::functiondefinition_constructor_args():
    sig = inspect.signature(astm::gastm::FunctionDefinition.__init__)
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



def test_astm::gastm::functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::FunctionDeclaration)


def test_astm::gastm::functiondeclaration_constructor_exists():
    assert callable(astm::gastm::FunctionDeclaration.__init__)


def test_astm::gastm::functiondeclaration_constructor_args():
    sig = inspect.signature(astm::gastm::FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::VariableDeclaration)


def test_astm::gastm::variabledeclaration_constructor_exists():
    assert callable(astm::gastm::VariableDeclaration.__init__)


def test_astm::gastm::variabledeclaration_constructor_args():
    sig = inspect.signature(astm::gastm::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isMutable" in params, "Missing parameter 'isMutable'"

def test_astm::gastm::variabledeclaration_has_isMutable():
    assert hasattr(astm::gastm::VariableDeclaration, "isMutable")
    descriptor = None
    for klass in astm::gastm::VariableDeclaration.__mro__:
        if "isMutable" in klass.__dict__:
            descriptor = klass.__dict__["isMutable"]
            break
    assert isinstance(descriptor, property)



def test_astm::gastm::formalparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::FormalParameterDeclaration)


def test_astm::gastm::formalparameterdeclaration_constructor_exists():
    assert callable(astm::gastm::FormalParameterDeclaration.__init__)


def test_astm::gastm::formalparameterdeclaration_constructor_args():
    sig = inspect.signature(astm::gastm::FormalParameterDeclaration.__init__)
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



def test_astm::gastm::sourcelocation_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::SourceLocation)


def test_astm::gastm::sourcelocation_constructor_exists():
    assert callable(astm::gastm::SourceLocation.__init__)


def test_astm::gastm::sourcelocation_constructor_args():
    sig = inspect.signature(astm::gastm::SourceLocation.__init__)
    params = list(sig.parameters.keys())
    assert "startColumn" in params, "Missing parameter 'startColumn'"
    assert "endColumn" in params, "Missing parameter 'endColumn'"
    assert "startLine" in params, "Missing parameter 'startLine'"
    assert "endLine" in params, "Missing parameter 'endLine'"

def test_astm::gastm::sourcelocation_has_startColumn():
    assert hasattr(astm::gastm::SourceLocation, "startColumn")
    descriptor = None
    for klass in astm::gastm::SourceLocation.__mro__:
        if "startColumn" in klass.__dict__:
            descriptor = klass.__dict__["startColumn"]
            break
    assert isinstance(descriptor, property)

def test_astm::gastm::sourcelocation_has_endColumn():
    assert hasattr(astm::gastm::SourceLocation, "endColumn")
    descriptor = None
    for klass in astm::gastm::SourceLocation.__mro__:
        if "endColumn" in klass.__dict__:
            descriptor = klass.__dict__["endColumn"]
            break
    assert isinstance(descriptor, property)

def test_astm::gastm::sourcelocation_has_startLine():
    assert hasattr(astm::gastm::SourceLocation, "startLine")
    descriptor = None
    for klass in astm::gastm::SourceLocation.__mro__:
        if "startLine" in klass.__dict__:
            descriptor = klass.__dict__["startLine"]
            break
    assert isinstance(descriptor, property)

def test_astm::gastm::sourcelocation_has_endLine():
    assert hasattr(astm::gastm::SourceLocation, "endLine")
    descriptor = None
    for klass in astm::gastm::SourceLocation.__mro__:
        if "endLine" in klass.__dict__:
            descriptor = klass.__dict__["endLine"]
            break
    assert isinstance(descriptor, property)



def test_astm::gastm::sourcefile_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::SourceFile)


def test_astm::gastm::sourcefile_constructor_exists():
    assert callable(astm::gastm::SourceFile.__init__)


def test_astm::gastm::sourcefile_constructor_args():
    sig = inspect.signature(astm::gastm::SourceFile.__init__)
    params = list(sig.parameters.keys())
    assert "pathName" in params, "Missing parameter 'pathName'"

def test_astm::gastm::sourcefile_has_pathName():
    assert hasattr(astm::gastm::SourceFile, "pathName")
    descriptor = None
    for klass in astm::gastm::SourceFile.__mro__:
        if "pathName" in klass.__dict__:
            descriptor = klass.__dict__["pathName"]
            break
    assert isinstance(descriptor, property)



def test_astm::gastm::actualparameter_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ActualParameter)


def test_astm::gastm::actualparameter_constructor_exists():
    assert callable(astm::gastm::ActualParameter.__init__)


def test_astm::gastm::actualparameter_constructor_args():
    sig = inspect.signature(astm::gastm::ActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::binaryoperator_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::BinaryOperator)


def test_astm::gastm::binaryoperator_constructor_exists():
    assert callable(astm::gastm::BinaryOperator.__init__)


def test_astm::gastm::binaryoperator_constructor_args():
    sig = inspect.signature(astm::gastm::BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::UnaryOperator)


def test_astm::gastm::unaryoperator_constructor_exists():
    assert callable(astm::gastm::UnaryOperator.__init__)


def test_astm::gastm::unaryoperator_constructor_args():
    sig = inspect.signature(astm::gastm::UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::accesskind_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::AccessKind)


def test_astm::gastm::accesskind_constructor_exists():
    assert callable(astm::gastm::AccessKind.__init__)


def test_astm::gastm::accesskind_constructor_args():
    sig = inspect.signature(astm::gastm::AccessKind.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::functiontype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::FunctionType)


def test_astm::gastm::functiontype_constructor_exists():
    assert callable(astm::gastm::FunctionType.__init__)


def test_astm::gastm::functiontype_constructor_args():
    sig = inspect.signature(astm::gastm::FunctionType.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::namespacetype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::NameSpaceType)


def test_astm::gastm::namespacetype_constructor_exists():
    assert callable(astm::gastm::NameSpaceType.__init__)


def test_astm::gastm::namespacetype_constructor_args():
    sig = inspect.signature(astm::gastm::NameSpaceType.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::typereference_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::TypeReference)


def test_astm::gastm::typereference_constructor_exists():
    assert callable(astm::gastm::TypeReference.__init__)


def test_astm::gastm::typereference_constructor_args():
    sig = inspect.signature(astm::gastm::TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::labeltype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::LabelType)


def test_astm::gastm::labeltype_constructor_exists():
    assert callable(astm::gastm::LabelType.__init__)


def test_astm::gastm::labeltype_constructor_args():
    sig = inspect.signature(astm::gastm::LabelType.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::datatype_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::DataType)


def test_astm::gastm::datatype_constructor_exists():
    assert callable(astm::gastm::DataType.__init__)


def test_astm::gastm::datatype_constructor_args():
    sig = inspect.signature(astm::gastm::DataType.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::storagespecification_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::StorageSpecification)


def test_astm::gastm::storagespecification_constructor_exists():
    assert callable(astm::gastm::StorageSpecification.__init__)


def test_astm::gastm::storagespecification_constructor_args():
    sig = inspect.signature(astm::gastm::StorageSpecification.__init__)
    params = list(sig.parameters.keys())



def test_gastmsyntaxobject_is_not_abstract():
    assert not inspect.isabstract(GASTMSyntaxObject)


def test_gastmsyntaxobject_constructor_exists():
    assert callable(GASTMSyntaxObject.__init__)


def test_gastmsyntaxobject_constructor_args():
    sig = inspect.signature(GASTMSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::definitionobject_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::DefinitionObject)


def test_astm::gastm::definitionobject_constructor_exists():
    assert callable(astm::gastm::DefinitionObject.__init__)


def test_astm::gastm::definitionobject_constructor_args():
    sig = inspect.signature(astm::gastm::DefinitionObject.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::type_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Type)


def test_astm::gastm::type_constructor_exists():
    assert callable(astm::gastm::Type.__init__)


def test_astm::gastm::type_constructor_args():
    sig = inspect.signature(astm::gastm::Type.__init__)
    params = list(sig.parameters.keys())
    assert "isConst" in params, "Missing parameter 'isConst'"
    assert "isVolatile" in params, "Missing parameter 'isVolatile'"

def test_astm::gastm::type_has_isConst():
    assert hasattr(astm::gastm::Type, "isConst")
    descriptor = None
    for klass in astm::gastm::Type.__mro__:
        if "isConst" in klass.__dict__:
            descriptor = klass.__dict__["isConst"]
            break
    assert isinstance(descriptor, property)

def test_astm::gastm::type_has_isVolatile():
    assert hasattr(astm::gastm::Type, "isVolatile")
    descriptor = None
    for klass in astm::gastm::Type.__mro__:
        if "isVolatile" in klass.__dict__:
            descriptor = klass.__dict__["isVolatile"]
            break
    assert isinstance(descriptor, property)



def test_astm::gastm::preprocessorelement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::PreprocessorElement)


def test_astm::gastm::preprocessorelement_constructor_exists():
    assert callable(astm::gastm::PreprocessorElement.__init__)


def test_astm::gastm::preprocessorelement_constructor_args():
    sig = inspect.signature(astm::gastm::PreprocessorElement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::expression_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Expression)


def test_astm::gastm::expression_constructor_exists():
    assert callable(astm::gastm::Expression.__init__)


def test_astm::gastm::expression_constructor_args():
    sig = inspect.signature(astm::gastm::Expression.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::statement_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Statement)


def test_astm::gastm::statement_constructor_exists():
    assert callable(astm::gastm::Statement.__init__)


def test_astm::gastm::statement_constructor_args():
    sig = inspect.signature(astm::gastm::Statement.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::othersyntaxobject_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::OtherSyntaxObject)


def test_astm::gastm::othersyntaxobject_constructor_exists():
    assert callable(astm::gastm::OtherSyntaxObject.__init__)


def test_astm::gastm::othersyntaxobject_constructor_args():
    sig = inspect.signature(astm::gastm::OtherSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::gastmsemanticobject_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::GASTMSemanticObject)


def test_astm::gastm::gastmsemanticobject_constructor_exists():
    assert callable(astm::gastm::GASTMSemanticObject.__init__)


def test_astm::gastm::gastmsemanticobject_constructor_args():
    sig = inspect.signature(astm::gastm::GASTMSemanticObject.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::gastmsourceobject_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::GASTMSourceObject)


def test_astm::gastm::gastmsourceobject_constructor_exists():
    assert callable(astm::gastm::GASTMSourceObject.__init__)


def test_astm::gastm::gastmsourceobject_constructor_args():
    sig = inspect.signature(astm::gastm::GASTMSourceObject.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::gastmobject_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::GASTMObject)


def test_astm::gastm::gastmobject_constructor_exists():
    assert callable(astm::gastm::GASTMObject.__init__)


def test_astm::gastm::gastmobject_constructor_args():
    sig = inspect.signature(astm::gastm::GASTMObject.__init__)
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



def test_astm::gastm::derivesfrom_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::DerivesFrom)


def test_astm::gastm::derivesfrom_constructor_exists():
    assert callable(astm::gastm::DerivesFrom.__init__)


def test_astm::gastm::derivesfrom_constructor_args():
    sig = inspect.signature(astm::gastm::DerivesFrom.__init__)
    params = list(sig.parameters.keys())
    assert "isVirtual" in params, "Missing parameter 'isVirtual'"

def test_astm::gastm::derivesfrom_has_isVirtual():
    assert hasattr(astm::gastm::DerivesFrom, "isVirtual")
    descriptor = None
    for klass in astm::gastm::DerivesFrom.__mro__:
        if "isVirtual" in klass.__dict__:
            descriptor = klass.__dict__["isVirtual"]
            break
    assert isinstance(descriptor, property)



def test_astm::gastm::switchcase_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::SwitchCase)


def test_astm::gastm::switchcase_constructor_exists():
    assert callable(astm::gastm::SwitchCase.__init__)


def test_astm::gastm::switchcase_constructor_args():
    sig = inspect.signature(astm::gastm::SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::catchblock_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::CatchBlock)


def test_astm::gastm::catchblock_constructor_exists():
    assert callable(astm::gastm::CatchBlock.__init__)


def test_astm::gastm::catchblock_constructor_args():
    sig = inspect.signature(astm::gastm::CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::name_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Name)


def test_astm::gastm::name_constructor_exists():
    assert callable(astm::gastm::Name.__init__)


def test_astm::gastm::name_constructor_args():
    sig = inspect.signature(astm::gastm::Name.__init__)
    params = list(sig.parameters.keys())
    assert "nameString" in params, "Missing parameter 'nameString'"

def test_astm::gastm::name_has_nameString():
    assert hasattr(astm::gastm::Name, "nameString")
    descriptor = None
    for klass in astm::gastm::Name.__mro__:
        if "nameString" in klass.__dict__:
            descriptor = klass.__dict__["nameString"]
            break
    assert isinstance(descriptor, property)



def test_astm::gastm::dimension_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Dimension)


def test_astm::gastm::dimension_constructor_exists():
    assert callable(astm::gastm::Dimension.__init__)


def test_astm::gastm::dimension_constructor_args():
    sig = inspect.signature(astm::gastm::Dimension.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::functionmemberattribute_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::FunctionMemberAttribute)


def test_astm::gastm::functionmemberattribute_constructor_exists():
    assert callable(astm::gastm::FunctionMemberAttribute.__init__)


def test_astm::gastm::functionmemberattribute_constructor_args():
    sig = inspect.signature(astm::gastm::FunctionMemberAttribute.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::virtualspecification_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::VirtualSpecification)


def test_astm::gastm::virtualspecification_constructor_exists():
    assert callable(astm::gastm::VirtualSpecification.__init__)


def test_astm::gastm::virtualspecification_constructor_args():
    sig = inspect.signature(astm::gastm::VirtualSpecification.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::compilationunit_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::CompilationUnit)


def test_astm::gastm::compilationunit_constructor_exists():
    assert callable(astm::gastm::CompilationUnit.__init__)


def test_astm::gastm::compilationunit_constructor_args():
    sig = inspect.signature(astm::gastm::CompilationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"

def test_astm::gastm::compilationunit_has_language():
    assert hasattr(astm::gastm::CompilationUnit, "language")
    descriptor = None
    for klass in astm::gastm::CompilationUnit.__mro__:
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



def test_astm::gastm::macrodefinition_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::MacroDefinition)


def test_astm::gastm::macrodefinition_constructor_exists():
    assert callable(astm::gastm::MacroDefinition.__init__)


def test_astm::gastm::macrodefinition_constructor_args():
    sig = inspect.signature(astm::gastm::MacroDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "macroName" in params, "Missing parameter 'macroName'"

def test_astm::gastm::macrodefinition_has_body():
    assert hasattr(astm::gastm::MacroDefinition, "body")
    descriptor = None
    for klass in astm::gastm::MacroDefinition.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_astm::gastm::macrodefinition_has_macroName():
    assert hasattr(astm::gastm::MacroDefinition, "macroName")
    descriptor = None
    for klass in astm::gastm::MacroDefinition.__mro__:
        if "macroName" in klass.__dict__:
            descriptor = klass.__dict__["macroName"]
            break
    assert isinstance(descriptor, property)



def test_astm::gastm::macrocall_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::MacroCall)


def test_astm::gastm::macrocall_constructor_exists():
    assert callable(astm::gastm::MacroCall.__init__)


def test_astm::gastm::macrocall_constructor_args():
    sig = inspect.signature(astm::gastm::MacroCall.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::includeunit_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::IncludeUnit)


def test_astm::gastm::includeunit_constructor_exists():
    assert callable(astm::gastm::IncludeUnit.__init__)


def test_astm::gastm::includeunit_constructor_args():
    sig = inspect.signature(astm::gastm::IncludeUnit.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::comment_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Comment)


def test_astm::gastm::comment_constructor_exists():
    assert callable(astm::gastm::Comment.__init__)


def test_astm::gastm::comment_constructor_args():
    sig = inspect.signature(astm::gastm::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_astm::gastm::comment_has_text():
    assert hasattr(astm::gastm::Comment, "text")
    descriptor = None
    for klass in astm::gastm::Comment.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
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



def test_astm::gastm::gastmsyntaxobject_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::GASTMSyntaxObject)


def test_astm::gastm::gastmsyntaxobject_constructor_exists():
    assert callable(astm::gastm::GASTMSyntaxObject.__init__)


def test_astm::gastm::gastmsyntaxobject_constructor_args():
    sig = inspect.signature(astm::gastm::GASTMSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_scope_is_not_abstract():
    assert not inspect.isabstract(Scope)


def test_scope_constructor_exists():
    assert callable(Scope.__init__)


def test_scope_constructor_args():
    sig = inspect.signature(Scope.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::functionscope_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::FunctionScope)


def test_astm::gastm::functionscope_constructor_exists():
    assert callable(astm::gastm::FunctionScope.__init__)


def test_astm::gastm::functionscope_constructor_args():
    sig = inspect.signature(astm::gastm::FunctionScope.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::aggregatescope_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::AggregateScope)


def test_astm::gastm::aggregatescope_constructor_exists():
    assert callable(astm::gastm::AggregateScope.__init__)


def test_astm::gastm::aggregatescope_constructor_args():
    sig = inspect.signature(astm::gastm::AggregateScope.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::globalscope_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::GlobalScope)


def test_astm::gastm::globalscope_constructor_exists():
    assert callable(astm::gastm::GlobalScope.__init__)


def test_astm::gastm::globalscope_constructor_args():
    sig = inspect.signature(astm::gastm::GlobalScope.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::blockscope_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::BlockScope)


def test_astm::gastm::blockscope_constructor_exists():
    assert callable(astm::gastm::BlockScope.__init__)


def test_astm::gastm::blockscope_constructor_args():
    sig = inspect.signature(astm::gastm::BlockScope.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::programscope_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::ProgramScope)


def test_astm::gastm::programscope_constructor_exists():
    assert callable(astm::gastm::ProgramScope.__init__)


def test_astm::gastm::programscope_constructor_args():
    sig = inspect.signature(astm::gastm::ProgramScope.__init__)
    params = list(sig.parameters.keys())



def test_definitionobject_is_not_abstract():
    assert not inspect.isabstract(DefinitionObject)


def test_definitionobject_constructor_exists():
    assert callable(DefinitionObject.__init__)


def test_definitionobject_constructor_args():
    sig = inspect.signature(DefinitionObject.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::declarationordefinition_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::DeclarationOrDefinition)


def test_astm::gastm::declarationordefinition_constructor_exists():
    assert callable(astm::gastm::DeclarationOrDefinition.__init__)


def test_astm::gastm::declarationordefinition_constructor_args():
    sig = inspect.signature(astm::gastm::DeclarationOrDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "isRegister" in params, "Missing parameter 'isRegister'"
    assert "linkageSpecifier" in params, "Missing parameter 'linkageSpecifier'"

def test_astm::gastm::declarationordefinition_has_isRegister():
    assert hasattr(astm::gastm::DeclarationOrDefinition, "isRegister")
    descriptor = None
    for klass in astm::gastm::DeclarationOrDefinition.__mro__:
        if "isRegister" in klass.__dict__:
            descriptor = klass.__dict__["isRegister"]
            break
    assert isinstance(descriptor, property)

def test_astm::gastm::declarationordefinition_has_linkageSpecifier():
    assert hasattr(astm::gastm::DeclarationOrDefinition, "linkageSpecifier")
    descriptor = None
    for klass in astm::gastm::DeclarationOrDefinition.__mro__:
        if "linkageSpecifier" in klass.__dict__:
            descriptor = klass.__dict__["linkageSpecifier"]
            break
    assert isinstance(descriptor, property)



def test_astm::gastm::typedefinition_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::TypeDefinition)


def test_astm::gastm::typedefinition_constructor_exists():
    assert callable(astm::gastm::TypeDefinition.__init__)


def test_astm::gastm::typedefinition_constructor_args():
    sig = inspect.signature(astm::gastm::TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::namespacedefinition_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::NameSpaceDefinition)


def test_astm::gastm::namespacedefinition_constructor_exists():
    assert callable(astm::gastm::NameSpaceDefinition.__init__)


def test_astm::gastm::namespacedefinition_constructor_args():
    sig = inspect.signature(astm::gastm::NameSpaceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::labeldefinition_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::LabelDefinition)


def test_astm::gastm::labeldefinition_constructor_exists():
    assert callable(astm::gastm::LabelDefinition.__init__)


def test_astm::gastm::labeldefinition_constructor_args():
    sig = inspect.signature(astm::gastm::LabelDefinition.__init__)
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



def test_astm::sastm::delphiinterfacesection_is_not_abstract():
    assert not inspect.isabstract(astm::sastm::DelphiInterfaceSection)


def test_astm::sastm::delphiinterfacesection_constructor_exists():
    assert callable(astm::sastm::DelphiInterfaceSection.__init__)


def test_astm::sastm::delphiinterfacesection_constructor_args():
    sig = inspect.signature(astm::sastm::DelphiInterfaceSection.__init__)
    params = list(sig.parameters.keys())



def test_astm::sastm::delphiunit_is_not_abstract():
    assert not inspect.isabstract(astm::sastm::DelphiUnit)


def test_astm::sastm::delphiunit_constructor_exists():
    assert callable(astm::sastm::DelphiUnit.__init__)


def test_astm::sastm::delphiunit_constructor_args():
    sig = inspect.signature(astm::sastm::DelphiUnit.__init__)
    params = list(sig.parameters.keys())



def test_astm::sastm::delphiimplementationsection_is_not_abstract():
    assert not inspect.isabstract(astm::sastm::DelphiImplementationSection)


def test_astm::sastm::delphiimplementationsection_constructor_exists():
    assert callable(astm::sastm::DelphiImplementationSection.__init__)


def test_astm::sastm::delphiimplementationsection_constructor_args():
    sig = inspect.signature(astm::sastm::DelphiImplementationSection.__init__)
    params = list(sig.parameters.keys())



def test_gastmsemanticobject_is_not_abstract():
    assert not inspect.isabstract(GASTMSemanticObject)


def test_gastmsemanticobject_constructor_exists():
    assert callable(GASTMSemanticObject.__init__)


def test_gastmsemanticobject_constructor_args():
    sig = inspect.signature(GASTMSemanticObject.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::scope_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Scope)


def test_astm::gastm::scope_constructor_exists():
    assert callable(astm::gastm::Scope.__init__)


def test_astm::gastm::scope_constructor_args():
    sig = inspect.signature(astm::gastm::Scope.__init__)
    params = list(sig.parameters.keys())



def test_astm::gastm::project_is_not_abstract():
    assert not inspect.isabstract(astm::gastm::Project)


def test_astm::gastm::project_constructor_exists():
    assert callable(astm::gastm::Project.__init__)


def test_astm::gastm::project_constructor_args():
    sig = inspect.signature(astm::gastm::Project.__init__)
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
StorageSpecification_strategy = st.builds(
    StorageSpecification,
)
astm::gastm::PerClassMember_strategy = st.builds(
    astm::gastm::PerClassMember,
)
astm::gastm::FileLocal_strategy = st.builds(
    astm::gastm::FileLocal,
)
astm::gastm::FunctionPersistent_strategy = st.builds(
    astm::gastm::FunctionPersistent,
)
astm::gastm::NoDef_strategy = st.builds(
    astm::gastm::NoDef,
)
astm::gastm::External_strategy = st.builds(
    astm::gastm::External,
)
ActualParameter_strategy = st.builds(
    ActualParameter,
)
astm::gastm::ActualParameterExpression_strategy = st.builds(
    astm::gastm::ActualParameterExpression,
)
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
astm::gastm::OperatorAssign_strategy = st.builds(
    astm::gastm::OperatorAssign,
)
IdentifierReference_strategy = st.builds(
    IdentifierReference,
)
NameReference_strategy = st.builds(
    NameReference,
)
astm::gastm::TypeQualifiedIdentifierReference_strategy = st.builds(
    astm::gastm::TypeQualifiedIdentifierReference,
)
astm::gastm::IdentifierReference_strategy = st.builds(
    astm::gastm::IdentifierReference,
)
astm::gastm::QualifiedIdentifierReference_strategy = st.builds(
    astm::gastm::QualifiedIdentifierReference,
)
SwitchCase_strategy = st.builds(
    SwitchCase,
)
astm::gastm::CaseBlock_strategy = st.builds(
    astm::gastm::CaseBlock,
)
CatchBlock_strategy = st.builds(
    CatchBlock,
)
astm::gastm::TypesCatchBlock_strategy = st.builds(
    astm::gastm::TypesCatchBlock,
)
astm::gastm::VariableCatchBlock_strategy = st.builds(
    astm::gastm::VariableCatchBlock,
)
LoopStatement_strategy = st.builds(
    LoopStatement,
)
astm::gastm::ForStatement_strategy = st.builds(
    astm::gastm::ForStatement,
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
astm::gastm::ArrayType_strategy = st.builds(
    astm::gastm::ArrayType,
)
AggregateScope_strategy = st.builds(
    AggregateScope,
)
DelphiInterfaceSection_strategy = st.builds(
    DelphiInterfaceSection,
)
FunctionCallExpression_strategy = st.builds(
    FunctionCallExpression,
)
astm::sastm::DelphiFunctionCallExpression_strategy = st.builds(
    astm::sastm::DelphiFunctionCallExpression,
)
BlockStatement_strategy = st.builds(
    BlockStatement,
)
astm::sastm::DelphiWithStatement_strategy = st.builds(
    astm::sastm::DelphiWithStatement,
)
astm::sastm::DelphiBlockStatement_strategy = st.builds(
    astm::sastm::DelphiBlockStatement,
)
NamedTypeReference_strategy = st.builds(
    NamedTypeReference,
)
DelphiImplementationSection_strategy = st.builds(
    DelphiImplementationSection,
)
astm::gastm::Multiply_strategy = st.builds(
    astm::gastm::Multiply,
)
astm::gastm::Subtract_strategy = st.builds(
    astm::gastm::Subtract,
)
astm::gastm::Add_strategy = st.builds(
    astm::gastm::Add,
)
astm::gastm::SpecificConcatString_strategy = st.builds(
    astm::gastm::SpecificConcatString,
)
astm::gastm::SpecificLike_strategy = st.builds(
    astm::gastm::SpecificLike,
)
astm::gastm::SpecificIn_strategy = st.builds(
    astm::gastm::SpecificIn,
)
astm::gastm::SpecificGreaterEqual_strategy = st.builds(
    astm::gastm::SpecificGreaterEqual,
)
astm::gastm::SpecificLessEqual_strategy = st.builds(
    astm::gastm::SpecificLessEqual,
)
ActualParameterExpression_strategy = st.builds(
    ActualParameterExpression,
)
astm::gastm::ByReferenceActualParameterExpression_strategy = st.builds(
    astm::gastm::ByReferenceActualParameterExpression,
)
astm::gastm::ByValueActualParameterExpression_strategy = st.builds(
    astm::gastm::ByValueActualParameterExpression,
)
astm::gastm::MissingActualParameter_strategy = st.builds(
    astm::gastm::MissingActualParameter,
)
astm::gastm::Assign_strategy = st.builds(
    astm::gastm::Assign,
)
astm::gastm::BitRightShift_strategy = st.builds(
    astm::gastm::BitRightShift,
)
astm::gastm::BitLeftShift_strategy = st.builds(
    astm::gastm::BitLeftShift,
)
astm::gastm::BitXor_strategy = st.builds(
    astm::gastm::BitXor,
)
astm::gastm::BitOr_strategy = st.builds(
    astm::gastm::BitOr,
)
astm::gastm::BitAnd_strategy = st.builds(
    astm::gastm::BitAnd,
)
astm::gastm::NotLess_strategy = st.builds(
    astm::gastm::NotLess,
)
astm::gastm::Less_strategy = st.builds(
    astm::gastm::Less,
)
astm::gastm::NotGreater_strategy = st.builds(
    astm::gastm::NotGreater,
)
astm::gastm::Greater_strategy = st.builds(
    astm::gastm::Greater,
)
astm::gastm::NotEqual_strategy = st.builds(
    astm::gastm::NotEqual,
)
astm::gastm::Equal_strategy = st.builds(
    astm::gastm::Equal,
)
astm::gastm::Or_strategy = st.builds(
    astm::gastm::Or,
)
astm::gastm::And_strategy = st.builds(
    astm::gastm::And,
)
astm::gastm::Exponent_strategy = st.builds(
    astm::gastm::Exponent,
)
astm::gastm::Modulus_strategy = st.builds(
    astm::gastm::Modulus,
)
astm::gastm::Divide_strategy = st.builds(
    astm::gastm::Divide,
)
astm::gastm::PointerType_strategy = st.builds(
    astm::gastm::PointerType,
)
astm::gastm::CollectionType_strategy = st.builds(
    astm::gastm::CollectionType,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
astm::gastm::Decrement_strategy = st.builds(
    astm::gastm::Decrement,
)
astm::gastm::Increment_strategy = st.builds(
    astm::gastm::Increment,
)
astm::gastm::Not_strategy = st.builds(
    astm::gastm::Not,
)
astm::gastm::BitNot_strategy = st.builds(
    astm::gastm::BitNot,
)
astm::gastm::PostDecrement_strategy = st.builds(
    astm::gastm::PostDecrement,
)
astm::gastm::Deref_strategy = st.builds(
    astm::gastm::Deref,
)
astm::gastm::AddressOf_strategy = st.builds(
    astm::gastm::AddressOf,
)
astm::gastm::Negate_strategy = st.builds(
    astm::gastm::Negate,
)
astm::gastm::PostIncrement_strategy = st.builds(
    astm::gastm::PostIncrement,
)
astm::gastm::UnaryPlus_strategy = st.builds(
    astm::gastm::UnaryPlus,
)
Literal_strategy = st.builds(
    Literal,
)
astm::gastm::StringLiteral_strategy = st.builds(
    astm::gastm::StringLiteral,
)
astm::gastm::RealLiteral_strategy = st.builds(
    astm::gastm::RealLiteral,
)
astm::gastm::CharLiteral_strategy = st.builds(
    astm::gastm::CharLiteral,
)
astm::gastm::BitLiteral_strategy = st.builds(
    astm::gastm::BitLiteral,
)
astm::gastm::BooleanLiteral_strategy = st.builds(
    astm::gastm::BooleanLiteral,
)
astm::gastm::IntegerLiteral_strategy = st.builds(
    astm::gastm::IntegerLiteral,
)
QualifiedIdentifierReference_strategy = st.builds(
    QualifiedIdentifierReference,
)
astm::gastm::QualifiedOverData_strategy = st.builds(
    astm::gastm::QualifiedOverData,
)
astm::gastm::QualifiedOverPointer_strategy = st.builds(
    astm::gastm::QualifiedOverPointer,
)
ForStatement_strategy = st.builds(
    ForStatement,
)
astm::gastm::ForCheckAfterStatement_strategy = st.builds(
    astm::gastm::ForCheckAfterStatement,
)
astm::gastm::ForCheckBeforeStatement_strategy = st.builds(
    astm::gastm::ForCheckBeforeStatement,
)
astm::gastm::DoWhileStatement_strategy = st.builds(
    astm::gastm::DoWhileStatement,
)
astm::gastm::WhileStatement_strategy = st.builds(
    astm::gastm::WhileStatement,
)
astm::gastm::DefaultBlock_strategy = st.builds(
    astm::gastm::DefaultBlock,
)
AccessKind_strategy = st.builds(
    AccessKind,
)
astm::gastm::Private_strategy = st.builds(
    astm::gastm::Private,
)
astm::gastm::Protected_strategy = st.builds(
    astm::gastm::Protected,
)
astm::gastm::Public_strategy = st.builds(
    astm::gastm::Public,
)
astm::gastm::RangeType_strategy = st.builds(
    astm::gastm::RangeType,
)
astm::gastm::ReferenceType_strategy = st.builds(
    astm::gastm::ReferenceType,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
astm::gastm::LongInteger_strategy = st.builds(
    astm::gastm::LongInteger,
)
astm::gastm::Double_strategy = st.builds(
    astm::gastm::Double,
)
astm::gastm::ShortInteger_strategy = st.builds(
    astm::gastm::ShortInteger,
)
astm::gastm::Character_strategy = st.builds(
    astm::gastm::Character,
)
astm::gastm::Float_strategy = st.builds(
    astm::gastm::Float,
)
astm::gastm::Integer_strategy = st.builds(
    astm::gastm::Integer,
)
astm::gastm::LongDouble_strategy = st.builds(
    astm::gastm::LongDouble,
)
astm::gastm::WideCharacter_strategy = st.builds(
    astm::gastm::WideCharacter,
)
astm::gastm::Boolean_strategy = st.builds(
    astm::gastm::Boolean,
)
astm::gastm::String_strategy = st.builds(
    astm::gastm::String,
)
astm::gastm::Byte_strategy = st.builds(
    astm::gastm::Byte,
)
astm::gastm::Void_strategy = st.builds(
    astm::gastm::Void,
)
DerivesFrom_strategy = st.builds(
    DerivesFrom,
)
FormalParameterType_strategy = st.builds(
    FormalParameterType,
)
astm::gastm::ByReferenceFormalParameterType_strategy = st.builds(
    astm::gastm::ByReferenceFormalParameterType,
)
astm::gastm::ByValueFormalParameterType_strategy = st.builds(
    astm::gastm::ByValueFormalParameterType,
)
EnumLiteralDefinition_strategy = st.builds(
    EnumLiteralDefinition,
)
DataType_strategy = st.builds(
    DataType,
)
astm::gastm::FormalParameterType_strategy = st.builds(
    astm::gastm::FormalParameterType,
)
astm::gastm::AggregateType_strategy = st.builds(
    astm::gastm::AggregateType,
)
astm::gastm::ConstructedType_strategy = st.builds(
    astm::gastm::ConstructedType,
)
astm::gastm::EnumType_strategy = st.builds(
    astm::gastm::EnumType,
)
astm::gastm::ExceptionType_strategy = st.builds(
    astm::gastm::ExceptionType,
)
astm::gastm::NamedType_strategy = st.builds(
    astm::gastm::NamedType,
)
astm::gastm::PrimitiveType_strategy = st.builds(
    astm::gastm::PrimitiveType,
    isSigned=
        st.booleans()
)
MacroDefinition_strategy = st.builds(
    MacroDefinition,
)
DataDefinition_strategy = st.builds(
    DataDefinition,
)
astm::gastm::FormalParameterDefinition_strategy = st.builds(
    astm::gastm::FormalParameterDefinition,
)
astm::gastm::VariableDefinition_strategy = st.builds(
    astm::gastm::VariableDefinition,
)
astm::gastm::BitFieldDefinition_strategy = st.builds(
    astm::gastm::BitFieldDefinition,
)
Expression_strategy = st.builds(
    Expression,
)
astm::gastm::RangeExpression_strategy = st.builds(
    astm::gastm::RangeExpression,
)
astm::gastm::BinaryExpression_strategy = st.builds(
    astm::gastm::BinaryExpression,
)
astm::gastm::ArrayAccess_strategy = st.builds(
    astm::gastm::ArrayAccess,
)
astm::gastm::AnnotationExpression_strategy = st.builds(
    astm::gastm::AnnotationExpression,
)
astm::gastm::NewExpression_strategy = st.builds(
    astm::gastm::NewExpression,
)
astm::gastm::UnaryExpression_strategy = st.builds(
    astm::gastm::UnaryExpression,
)
astm::gastm::AggregateExpression_strategy = st.builds(
    astm::gastm::AggregateExpression,
)
astm::gastm::NameReference_strategy = st.builds(
    astm::gastm::NameReference,
)
astm::gastm::Literal_strategy = st.builds(
    astm::gastm::Literal,
    value=
        safe_text
)
astm::gastm::FunctionCallExpression_strategy = st.builds(
    astm::gastm::FunctionCallExpression,
)
astm::gastm::LabelAccess_strategy = st.builds(
    astm::gastm::LabelAccess,
)
astm::gastm::CastExpression_strategy = st.builds(
    astm::gastm::CastExpression,
)
astm::gastm::ConditionalExpression_strategy = st.builds(
    astm::gastm::ConditionalExpression,
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
astm::gastm::ClassType_strategy = st.builds(
    astm::gastm::ClassType,
)
astm::gastm::UnionType_strategy = st.builds(
    astm::gastm::UnionType,
)
astm::gastm::StructureType_strategy = st.builds(
    astm::gastm::StructureType,
)
astm::gastm::AnnotationType_strategy = st.builds(
    astm::gastm::AnnotationType,
)
NamedType_strategy = st.builds(
    NamedType,
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
astm::gastm::AggregateTypeDefinition_strategy = st.builds(
    astm::gastm::AggregateTypeDefinition,
)
astm::gastm::NamedTypeDefinition_strategy = st.builds(
    astm::gastm::NamedTypeDefinition,
)
Definition_strategy = st.builds(
    Definition,
)
astm::gastm::EntryDefinition_strategy = st.builds(
    astm::gastm::EntryDefinition,
)
astm::gastm::SpecificTriggerDefinition_strategy = st.builds(
    astm::gastm::SpecificTriggerDefinition,
)
astm::gastm::EnumLiteralDefinition_strategy = st.builds(
    astm::gastm::EnumLiteralDefinition,
)
astm::gastm::DataDefinition_strategy = st.builds(
    astm::gastm::DataDefinition,
    isMutable=
        st.booleans()
)
TypeReference_strategy = st.builds(
    TypeReference,
)
astm::gastm::UnnamedTypeReference_strategy = st.builds(
    astm::gastm::UnnamedTypeReference,
)
astm::gastm::NamedTypeReference_strategy = st.builds(
    astm::gastm::NamedTypeReference,
)
Name_strategy = st.builds(
    Name,
)
DeclarationOrDefinition_strategy = st.builds(
    DeclarationOrDefinition,
)
astm::gastm::Declaration_strategy = st.builds(
    astm::gastm::Declaration,
)
astm::gastm::Definition_strategy = st.builds(
    astm::gastm::Definition,
)
VirtualSpecification_strategy = st.builds(
    VirtualSpecification,
)
astm::gastm::PureVirtual_strategy = st.builds(
    astm::gastm::PureVirtual,
)
astm::gastm::Virtual_strategy = st.builds(
    astm::gastm::Virtual,
)
astm::gastm::NonVirtual_strategy = st.builds(
    astm::gastm::NonVirtual,
)
astm::gastm::FunctionMemberAttributes_strategy = st.builds(
    astm::gastm::FunctionMemberAttributes,
    isThisConst=
        st.booleans(),
    isFriend=
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
astm::gastm::ContinueStatement_strategy = st.builds(
    astm::gastm::ContinueStatement,
)
astm::gastm::TerminateStatement_strategy = st.builds(
    astm::gastm::TerminateStatement,
)
astm::gastm::ThrowStatement_strategy = st.builds(
    astm::gastm::ThrowStatement,
)
astm::gastm::ReturnStatement_strategy = st.builds(
    astm::gastm::ReturnStatement,
)
astm::gastm::SpecificSelectStatement_strategy = st.builds(
    astm::gastm::SpecificSelectStatement,
)
astm::gastm::EmptyStatement_strategy = st.builds(
    astm::gastm::EmptyStatement,
)
astm::gastm::BreakStatement_strategy = st.builds(
    astm::gastm::BreakStatement,
)
astm::gastm::LabeledStatement_strategy = st.builds(
    astm::gastm::LabeledStatement,
)
astm::gastm::LoopStatement_strategy = st.builds(
    astm::gastm::LoopStatement,
)
astm::gastm::JumpStatement_strategy = st.builds(
    astm::gastm::JumpStatement,
)
astm::gastm::DeleteStatement_strategy = st.builds(
    astm::gastm::DeleteStatement,
)
astm::gastm::ExpressionStatement_strategy = st.builds(
    astm::gastm::ExpressionStatement,
)
astm::gastm::TryStatement_strategy = st.builds(
    astm::gastm::TryStatement,
)
astm::gastm::DeclarationOrDefinitionStatement_strategy = st.builds(
    astm::gastm::DeclarationOrDefinitionStatement,
)
astm::gastm::SwitchStatement_strategy = st.builds(
    astm::gastm::SwitchStatement,
)
astm::gastm::IfStatement_strategy = st.builds(
    astm::gastm::IfStatement,
)
astm::gastm::BlockStatement_strategy = st.builds(
    astm::gastm::BlockStatement,
)
FormalParameterDefinition_strategy = st.builds(
    FormalParameterDefinition,
)
astm::gastm::FunctionDefinition_strategy = st.builds(
    astm::gastm::FunctionDefinition,
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
astm::gastm::FunctionDeclaration_strategy = st.builds(
    astm::gastm::FunctionDeclaration,
)
astm::gastm::VariableDeclaration_strategy = st.builds(
    astm::gastm::VariableDeclaration,
    isMutable=
        st.booleans()
)
astm::gastm::FormalParameterDeclaration_strategy = st.builds(
    astm::gastm::FormalParameterDeclaration,
)
SourceFile_strategy = st.builds(
    SourceFile,
)
GASTMSourceObject_strategy = st.builds(
    GASTMSourceObject,
)
astm::gastm::SourceLocation_strategy = st.builds(
    astm::gastm::SourceLocation,
    startColumn=
        st.integers(),
    endColumn=
        st.integers(),
    startLine=
        st.integers(),
    endLine=
        st.integers()
)
astm::gastm::SourceFile_strategy = st.builds(
    astm::gastm::SourceFile,
    pathName=
        safe_text
)
astm::gastm::ActualParameter_strategy = st.builds(
    astm::gastm::ActualParameter,
)
astm::gastm::BinaryOperator_strategy = st.builds(
    astm::gastm::BinaryOperator,
)
astm::gastm::UnaryOperator_strategy = st.builds(
    astm::gastm::UnaryOperator,
)
astm::gastm::AccessKind_strategy = st.builds(
    astm::gastm::AccessKind,
)
Type_strategy = st.builds(
    Type,
)
astm::gastm::FunctionType_strategy = st.builds(
    astm::gastm::FunctionType,
)
astm::gastm::NameSpaceType_strategy = st.builds(
    astm::gastm::NameSpaceType,
)
astm::gastm::TypeReference_strategy = st.builds(
    astm::gastm::TypeReference,
)
astm::gastm::LabelType_strategy = st.builds(
    astm::gastm::LabelType,
)
astm::gastm::DataType_strategy = st.builds(
    astm::gastm::DataType,
)
astm::gastm::StorageSpecification_strategy = st.builds(
    astm::gastm::StorageSpecification,
)
GASTMSyntaxObject_strategy = st.builds(
    GASTMSyntaxObject,
)
astm::gastm::DefinitionObject_strategy = st.builds(
    astm::gastm::DefinitionObject,
)
astm::gastm::Type_strategy = st.builds(
    astm::gastm::Type,
    isConst=
        st.booleans(),
    isVolatile=
        st.booleans()
)
astm::gastm::PreprocessorElement_strategy = st.builds(
    astm::gastm::PreprocessorElement,
)
astm::gastm::Expression_strategy = st.builds(
    astm::gastm::Expression,
)
astm::gastm::Statement_strategy = st.builds(
    astm::gastm::Statement,
)
astm::gastm::OtherSyntaxObject_strategy = st.builds(
    astm::gastm::OtherSyntaxObject,
)
astm::gastm::GASTMSemanticObject_strategy = st.builds(
    astm::gastm::GASTMSemanticObject,
)
astm::gastm::GASTMSourceObject_strategy = st.builds(
    astm::gastm::GASTMSourceObject,
)
astm::gastm::GASTMObject_strategy = st.builds(
    astm::gastm::GASTMObject,
)
ProgramScope_strategy = st.builds(
    ProgramScope,
)
OtherSyntaxObject_strategy = st.builds(
    OtherSyntaxObject,
)
astm::gastm::DerivesFrom_strategy = st.builds(
    astm::gastm::DerivesFrom,
    isVirtual=
        st.booleans()
)
astm::gastm::SwitchCase_strategy = st.builds(
    astm::gastm::SwitchCase,
)
astm::gastm::CatchBlock_strategy = st.builds(
    astm::gastm::CatchBlock,
)
astm::gastm::Name_strategy = st.builds(
    astm::gastm::Name,
    nameString=
        safe_text
)
astm::gastm::Dimension_strategy = st.builds(
    astm::gastm::Dimension,
)
astm::gastm::FunctionMemberAttribute_strategy = st.builds(
    astm::gastm::FunctionMemberAttribute,
)
astm::gastm::VirtualSpecification_strategy = st.builds(
    astm::gastm::VirtualSpecification,
)
astm::gastm::CompilationUnit_strategy = st.builds(
    astm::gastm::CompilationUnit,
    language=
        safe_text
)
AnnotationExpression_strategy = st.builds(
    AnnotationExpression,
)
PreprocessorElement_strategy = st.builds(
    PreprocessorElement,
)
astm::gastm::MacroDefinition_strategy = st.builds(
    astm::gastm::MacroDefinition,
    body=
        safe_text,
    macroName=
        safe_text
)
astm::gastm::MacroCall_strategy = st.builds(
    astm::gastm::MacroCall,
)
astm::gastm::IncludeUnit_strategy = st.builds(
    astm::gastm::IncludeUnit,
)
astm::gastm::Comment_strategy = st.builds(
    astm::gastm::Comment,
    text=
        safe_text
)
SourceLocation_strategy = st.builds(
    SourceLocation,
)
GASTMObject_strategy = st.builds(
    GASTMObject,
)
astm::gastm::GASTMSyntaxObject_strategy = st.builds(
    astm::gastm::GASTMSyntaxObject,
)
Scope_strategy = st.builds(
    Scope,
)
astm::gastm::FunctionScope_strategy = st.builds(
    astm::gastm::FunctionScope,
)
astm::gastm::AggregateScope_strategy = st.builds(
    astm::gastm::AggregateScope,
)
astm::gastm::GlobalScope_strategy = st.builds(
    astm::gastm::GlobalScope,
)
astm::gastm::BlockScope_strategy = st.builds(
    astm::gastm::BlockScope,
)
astm::gastm::ProgramScope_strategy = st.builds(
    astm::gastm::ProgramScope,
)
DefinitionObject_strategy = st.builds(
    DefinitionObject,
)
astm::gastm::DeclarationOrDefinition_strategy = st.builds(
    astm::gastm::DeclarationOrDefinition,
    isRegister=
        st.booleans(),
    linkageSpecifier=
        safe_text
)
astm::gastm::TypeDefinition_strategy = st.builds(
    astm::gastm::TypeDefinition,
)
astm::gastm::NameSpaceDefinition_strategy = st.builds(
    astm::gastm::NameSpaceDefinition,
)
astm::gastm::LabelDefinition_strategy = st.builds(
    astm::gastm::LabelDefinition,
)
GlobalScope_strategy = st.builds(
    GlobalScope,
)
CompilationUnit_strategy = st.builds(
    CompilationUnit,
)
astm::sastm::DelphiInterfaceSection_strategy = st.builds(
    astm::sastm::DelphiInterfaceSection,
)
astm::sastm::DelphiUnit_strategy = st.builds(
    astm::sastm::DelphiUnit,
)
astm::sastm::DelphiImplementationSection_strategy = st.builds(
    astm::sastm::DelphiImplementationSection,
)
GASTMSemanticObject_strategy = st.builds(
    GASTMSemanticObject,
)
astm::gastm::Scope_strategy = st.builds(
    astm::gastm::Scope,
)
astm::gastm::Project_strategy = st.builds(
    astm::gastm::Project,
)

@given(instance=StorageSpecification_strategy)
@settings(max_examples=50)
def test_storagespecification_instantiation(instance):
    assert isinstance(instance, StorageSpecification)

@given(instance=astm::gastm::PerClassMember_strategy)
@settings(max_examples=50)
def test_astm::gastm::perclassmember_instantiation(instance):
    assert isinstance(instance, astm::gastm::PerClassMember)

@given(instance=astm::gastm::FileLocal_strategy)
@settings(max_examples=50)
def test_astm::gastm::filelocal_instantiation(instance):
    assert isinstance(instance, astm::gastm::FileLocal)

@given(instance=astm::gastm::FunctionPersistent_strategy)
@settings(max_examples=50)
def test_astm::gastm::functionpersistent_instantiation(instance):
    assert isinstance(instance, astm::gastm::FunctionPersistent)

@given(instance=astm::gastm::NoDef_strategy)
@settings(max_examples=50)
def test_astm::gastm::nodef_instantiation(instance):
    assert isinstance(instance, astm::gastm::NoDef)

@given(instance=astm::gastm::External_strategy)
@settings(max_examples=50)
def test_astm::gastm::external_instantiation(instance):
    assert isinstance(instance, astm::gastm::External)

@given(instance=ActualParameter_strategy)
@settings(max_examples=50)
def test_actualparameter_instantiation(instance):
    assert isinstance(instance, ActualParameter)

@given(instance=astm::gastm::ActualParameterExpression_strategy)
@settings(max_examples=50)
def test_astm::gastm::actualparameterexpression_instantiation(instance):
    assert isinstance(instance, astm::gastm::ActualParameterExpression)

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=astm::gastm::OperatorAssign_strategy)
@settings(max_examples=50)
def test_astm::gastm::operatorassign_instantiation(instance):
    assert isinstance(instance, astm::gastm::OperatorAssign)

@given(instance=IdentifierReference_strategy)
@settings(max_examples=50)
def test_identifierreference_instantiation(instance):
    assert isinstance(instance, IdentifierReference)

@given(instance=NameReference_strategy)
@settings(max_examples=50)
def test_namereference_instantiation(instance):
    assert isinstance(instance, NameReference)

@given(instance=astm::gastm::TypeQualifiedIdentifierReference_strategy)
@settings(max_examples=50)
def test_astm::gastm::typequalifiedidentifierreference_instantiation(instance):
    assert isinstance(instance, astm::gastm::TypeQualifiedIdentifierReference)

@given(instance=astm::gastm::IdentifierReference_strategy)
@settings(max_examples=50)
def test_astm::gastm::identifierreference_instantiation(instance):
    assert isinstance(instance, astm::gastm::IdentifierReference)

@given(instance=astm::gastm::QualifiedIdentifierReference_strategy)
@settings(max_examples=50)
def test_astm::gastm::qualifiedidentifierreference_instantiation(instance):
    assert isinstance(instance, astm::gastm::QualifiedIdentifierReference)

@given(instance=SwitchCase_strategy)
@settings(max_examples=50)
def test_switchcase_instantiation(instance):
    assert isinstance(instance, SwitchCase)

@given(instance=astm::gastm::CaseBlock_strategy)
@settings(max_examples=50)
def test_astm::gastm::caseblock_instantiation(instance):
    assert isinstance(instance, astm::gastm::CaseBlock)

@given(instance=CatchBlock_strategy)
@settings(max_examples=50)
def test_catchblock_instantiation(instance):
    assert isinstance(instance, CatchBlock)

@given(instance=astm::gastm::TypesCatchBlock_strategy)
@settings(max_examples=50)
def test_astm::gastm::typescatchblock_instantiation(instance):
    assert isinstance(instance, astm::gastm::TypesCatchBlock)

@given(instance=astm::gastm::VariableCatchBlock_strategy)
@settings(max_examples=50)
def test_astm::gastm::variablecatchblock_instantiation(instance):
    assert isinstance(instance, astm::gastm::VariableCatchBlock)

@given(instance=LoopStatement_strategy)
@settings(max_examples=50)
def test_loopstatement_instantiation(instance):
    assert isinstance(instance, LoopStatement)

@given(instance=astm::gastm::ForStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::forstatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::ForStatement)

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

@given(instance=astm::gastm::ArrayType_strategy)
@settings(max_examples=50)
def test_astm::gastm::arraytype_instantiation(instance):
    assert isinstance(instance, astm::gastm::ArrayType)

@given(instance=AggregateScope_strategy)
@settings(max_examples=50)
def test_aggregatescope_instantiation(instance):
    assert isinstance(instance, AggregateScope)

@given(instance=DelphiInterfaceSection_strategy)
@settings(max_examples=50)
def test_delphiinterfacesection_instantiation(instance):
    assert isinstance(instance, DelphiInterfaceSection)

@given(instance=FunctionCallExpression_strategy)
@settings(max_examples=50)
def test_functioncallexpression_instantiation(instance):
    assert isinstance(instance, FunctionCallExpression)

@given(instance=astm::sastm::DelphiFunctionCallExpression_strategy)
@settings(max_examples=50)
def test_astm::sastm::delphifunctioncallexpression_instantiation(instance):
    assert isinstance(instance, astm::sastm::DelphiFunctionCallExpression)

@given(instance=BlockStatement_strategy)
@settings(max_examples=50)
def test_blockstatement_instantiation(instance):
    assert isinstance(instance, BlockStatement)

@given(instance=astm::sastm::DelphiWithStatement_strategy)
@settings(max_examples=50)
def test_astm::sastm::delphiwithstatement_instantiation(instance):
    assert isinstance(instance, astm::sastm::DelphiWithStatement)

@given(instance=astm::sastm::DelphiBlockStatement_strategy)
@settings(max_examples=50)
def test_astm::sastm::delphiblockstatement_instantiation(instance):
    assert isinstance(instance, astm::sastm::DelphiBlockStatement)

@given(instance=NamedTypeReference_strategy)
@settings(max_examples=50)
def test_namedtypereference_instantiation(instance):
    assert isinstance(instance, NamedTypeReference)

@given(instance=DelphiImplementationSection_strategy)
@settings(max_examples=50)
def test_delphiimplementationsection_instantiation(instance):
    assert isinstance(instance, DelphiImplementationSection)

@given(instance=astm::gastm::Multiply_strategy)
@settings(max_examples=50)
def test_astm::gastm::multiply_instantiation(instance):
    assert isinstance(instance, astm::gastm::Multiply)

@given(instance=astm::gastm::Subtract_strategy)
@settings(max_examples=50)
def test_astm::gastm::subtract_instantiation(instance):
    assert isinstance(instance, astm::gastm::Subtract)

@given(instance=astm::gastm::Add_strategy)
@settings(max_examples=50)
def test_astm::gastm::add_instantiation(instance):
    assert isinstance(instance, astm::gastm::Add)

@given(instance=astm::gastm::SpecificConcatString_strategy)
@settings(max_examples=50)
def test_astm::gastm::specificconcatstring_instantiation(instance):
    assert isinstance(instance, astm::gastm::SpecificConcatString)

@given(instance=astm::gastm::SpecificLike_strategy)
@settings(max_examples=50)
def test_astm::gastm::specificlike_instantiation(instance):
    assert isinstance(instance, astm::gastm::SpecificLike)

@given(instance=astm::gastm::SpecificIn_strategy)
@settings(max_examples=50)
def test_astm::gastm::specificin_instantiation(instance):
    assert isinstance(instance, astm::gastm::SpecificIn)

@given(instance=astm::gastm::SpecificGreaterEqual_strategy)
@settings(max_examples=50)
def test_astm::gastm::specificgreaterequal_instantiation(instance):
    assert isinstance(instance, astm::gastm::SpecificGreaterEqual)

@given(instance=astm::gastm::SpecificLessEqual_strategy)
@settings(max_examples=50)
def test_astm::gastm::specificlessequal_instantiation(instance):
    assert isinstance(instance, astm::gastm::SpecificLessEqual)

@given(instance=ActualParameterExpression_strategy)
@settings(max_examples=50)
def test_actualparameterexpression_instantiation(instance):
    assert isinstance(instance, ActualParameterExpression)

@given(instance=astm::gastm::ByReferenceActualParameterExpression_strategy)
@settings(max_examples=50)
def test_astm::gastm::byreferenceactualparameterexpression_instantiation(instance):
    assert isinstance(instance, astm::gastm::ByReferenceActualParameterExpression)

@given(instance=astm::gastm::ByValueActualParameterExpression_strategy)
@settings(max_examples=50)
def test_astm::gastm::byvalueactualparameterexpression_instantiation(instance):
    assert isinstance(instance, astm::gastm::ByValueActualParameterExpression)

@given(instance=astm::gastm::MissingActualParameter_strategy)
@settings(max_examples=50)
def test_astm::gastm::missingactualparameter_instantiation(instance):
    assert isinstance(instance, astm::gastm::MissingActualParameter)

@given(instance=astm::gastm::Assign_strategy)
@settings(max_examples=50)
def test_astm::gastm::assign_instantiation(instance):
    assert isinstance(instance, astm::gastm::Assign)

@given(instance=astm::gastm::BitRightShift_strategy)
@settings(max_examples=50)
def test_astm::gastm::bitrightshift_instantiation(instance):
    assert isinstance(instance, astm::gastm::BitRightShift)

@given(instance=astm::gastm::BitLeftShift_strategy)
@settings(max_examples=50)
def test_astm::gastm::bitleftshift_instantiation(instance):
    assert isinstance(instance, astm::gastm::BitLeftShift)

@given(instance=astm::gastm::BitXor_strategy)
@settings(max_examples=50)
def test_astm::gastm::bitxor_instantiation(instance):
    assert isinstance(instance, astm::gastm::BitXor)

@given(instance=astm::gastm::BitOr_strategy)
@settings(max_examples=50)
def test_astm::gastm::bitor_instantiation(instance):
    assert isinstance(instance, astm::gastm::BitOr)

@given(instance=astm::gastm::BitAnd_strategy)
@settings(max_examples=50)
def test_astm::gastm::bitand_instantiation(instance):
    assert isinstance(instance, astm::gastm::BitAnd)

@given(instance=astm::gastm::NotLess_strategy)
@settings(max_examples=50)
def test_astm::gastm::notless_instantiation(instance):
    assert isinstance(instance, astm::gastm::NotLess)

@given(instance=astm::gastm::Less_strategy)
@settings(max_examples=50)
def test_astm::gastm::less_instantiation(instance):
    assert isinstance(instance, astm::gastm::Less)

@given(instance=astm::gastm::NotGreater_strategy)
@settings(max_examples=50)
def test_astm::gastm::notgreater_instantiation(instance):
    assert isinstance(instance, astm::gastm::NotGreater)

@given(instance=astm::gastm::Greater_strategy)
@settings(max_examples=50)
def test_astm::gastm::greater_instantiation(instance):
    assert isinstance(instance, astm::gastm::Greater)

@given(instance=astm::gastm::NotEqual_strategy)
@settings(max_examples=50)
def test_astm::gastm::notequal_instantiation(instance):
    assert isinstance(instance, astm::gastm::NotEqual)

@given(instance=astm::gastm::Equal_strategy)
@settings(max_examples=50)
def test_astm::gastm::equal_instantiation(instance):
    assert isinstance(instance, astm::gastm::Equal)

@given(instance=astm::gastm::Or_strategy)
@settings(max_examples=50)
def test_astm::gastm::or_instantiation(instance):
    assert isinstance(instance, astm::gastm::Or)

@given(instance=astm::gastm::And_strategy)
@settings(max_examples=50)
def test_astm::gastm::and_instantiation(instance):
    assert isinstance(instance, astm::gastm::And)

@given(instance=astm::gastm::Exponent_strategy)
@settings(max_examples=50)
def test_astm::gastm::exponent_instantiation(instance):
    assert isinstance(instance, astm::gastm::Exponent)

@given(instance=astm::gastm::Modulus_strategy)
@settings(max_examples=50)
def test_astm::gastm::modulus_instantiation(instance):
    assert isinstance(instance, astm::gastm::Modulus)

@given(instance=astm::gastm::Divide_strategy)
@settings(max_examples=50)
def test_astm::gastm::divide_instantiation(instance):
    assert isinstance(instance, astm::gastm::Divide)

@given(instance=astm::gastm::PointerType_strategy)
@settings(max_examples=50)
def test_astm::gastm::pointertype_instantiation(instance):
    assert isinstance(instance, astm::gastm::PointerType)

@given(instance=astm::gastm::CollectionType_strategy)
@settings(max_examples=50)
def test_astm::gastm::collectiontype_instantiation(instance):
    assert isinstance(instance, astm::gastm::CollectionType)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=astm::gastm::Decrement_strategy)
@settings(max_examples=50)
def test_astm::gastm::decrement_instantiation(instance):
    assert isinstance(instance, astm::gastm::Decrement)

@given(instance=astm::gastm::Increment_strategy)
@settings(max_examples=50)
def test_astm::gastm::increment_instantiation(instance):
    assert isinstance(instance, astm::gastm::Increment)

@given(instance=astm::gastm::Not_strategy)
@settings(max_examples=50)
def test_astm::gastm::not_instantiation(instance):
    assert isinstance(instance, astm::gastm::Not)

@given(instance=astm::gastm::BitNot_strategy)
@settings(max_examples=50)
def test_astm::gastm::bitnot_instantiation(instance):
    assert isinstance(instance, astm::gastm::BitNot)

@given(instance=astm::gastm::PostDecrement_strategy)
@settings(max_examples=50)
def test_astm::gastm::postdecrement_instantiation(instance):
    assert isinstance(instance, astm::gastm::PostDecrement)

@given(instance=astm::gastm::Deref_strategy)
@settings(max_examples=50)
def test_astm::gastm::deref_instantiation(instance):
    assert isinstance(instance, astm::gastm::Deref)

@given(instance=astm::gastm::AddressOf_strategy)
@settings(max_examples=50)
def test_astm::gastm::addressof_instantiation(instance):
    assert isinstance(instance, astm::gastm::AddressOf)

@given(instance=astm::gastm::Negate_strategy)
@settings(max_examples=50)
def test_astm::gastm::negate_instantiation(instance):
    assert isinstance(instance, astm::gastm::Negate)

@given(instance=astm::gastm::PostIncrement_strategy)
@settings(max_examples=50)
def test_astm::gastm::postincrement_instantiation(instance):
    assert isinstance(instance, astm::gastm::PostIncrement)

@given(instance=astm::gastm::UnaryPlus_strategy)
@settings(max_examples=50)
def test_astm::gastm::unaryplus_instantiation(instance):
    assert isinstance(instance, astm::gastm::UnaryPlus)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=astm::gastm::StringLiteral_strategy)
@settings(max_examples=50)
def test_astm::gastm::stringliteral_instantiation(instance):
    assert isinstance(instance, astm::gastm::StringLiteral)

@given(instance=astm::gastm::RealLiteral_strategy)
@settings(max_examples=50)
def test_astm::gastm::realliteral_instantiation(instance):
    assert isinstance(instance, astm::gastm::RealLiteral)

@given(instance=astm::gastm::CharLiteral_strategy)
@settings(max_examples=50)
def test_astm::gastm::charliteral_instantiation(instance):
    assert isinstance(instance, astm::gastm::CharLiteral)

@given(instance=astm::gastm::BitLiteral_strategy)
@settings(max_examples=50)
def test_astm::gastm::bitliteral_instantiation(instance):
    assert isinstance(instance, astm::gastm::BitLiteral)

@given(instance=astm::gastm::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_astm::gastm::booleanliteral_instantiation(instance):
    assert isinstance(instance, astm::gastm::BooleanLiteral)

@given(instance=astm::gastm::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_astm::gastm::integerliteral_instantiation(instance):
    assert isinstance(instance, astm::gastm::IntegerLiteral)

@given(instance=QualifiedIdentifierReference_strategy)
@settings(max_examples=50)
def test_qualifiedidentifierreference_instantiation(instance):
    assert isinstance(instance, QualifiedIdentifierReference)

@given(instance=astm::gastm::QualifiedOverData_strategy)
@settings(max_examples=50)
def test_astm::gastm::qualifiedoverdata_instantiation(instance):
    assert isinstance(instance, astm::gastm::QualifiedOverData)

@given(instance=astm::gastm::QualifiedOverPointer_strategy)
@settings(max_examples=50)
def test_astm::gastm::qualifiedoverpointer_instantiation(instance):
    assert isinstance(instance, astm::gastm::QualifiedOverPointer)

@given(instance=ForStatement_strategy)
@settings(max_examples=50)
def test_forstatement_instantiation(instance):
    assert isinstance(instance, ForStatement)

@given(instance=astm::gastm::ForCheckAfterStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::forcheckafterstatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::ForCheckAfterStatement)

@given(instance=astm::gastm::ForCheckBeforeStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::forcheckbeforestatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::ForCheckBeforeStatement)

@given(instance=astm::gastm::DoWhileStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::dowhilestatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::DoWhileStatement)

@given(instance=astm::gastm::WhileStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::whilestatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::WhileStatement)

@given(instance=astm::gastm::DefaultBlock_strategy)
@settings(max_examples=50)
def test_astm::gastm::defaultblock_instantiation(instance):
    assert isinstance(instance, astm::gastm::DefaultBlock)

@given(instance=AccessKind_strategy)
@settings(max_examples=50)
def test_accesskind_instantiation(instance):
    assert isinstance(instance, AccessKind)

@given(instance=astm::gastm::Private_strategy)
@settings(max_examples=50)
def test_astm::gastm::private_instantiation(instance):
    assert isinstance(instance, astm::gastm::Private)

@given(instance=astm::gastm::Protected_strategy)
@settings(max_examples=50)
def test_astm::gastm::protected_instantiation(instance):
    assert isinstance(instance, astm::gastm::Protected)

@given(instance=astm::gastm::Public_strategy)
@settings(max_examples=50)
def test_astm::gastm::public_instantiation(instance):
    assert isinstance(instance, astm::gastm::Public)

@given(instance=astm::gastm::RangeType_strategy)
@settings(max_examples=50)
def test_astm::gastm::rangetype_instantiation(instance):
    assert isinstance(instance, astm::gastm::RangeType)

@given(instance=astm::gastm::ReferenceType_strategy)
@settings(max_examples=50)
def test_astm::gastm::referencetype_instantiation(instance):
    assert isinstance(instance, astm::gastm::ReferenceType)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=astm::gastm::LongInteger_strategy)
@settings(max_examples=50)
def test_astm::gastm::longinteger_instantiation(instance):
    assert isinstance(instance, astm::gastm::LongInteger)

@given(instance=astm::gastm::Double_strategy)
@settings(max_examples=50)
def test_astm::gastm::double_instantiation(instance):
    assert isinstance(instance, astm::gastm::Double)

@given(instance=astm::gastm::ShortInteger_strategy)
@settings(max_examples=50)
def test_astm::gastm::shortinteger_instantiation(instance):
    assert isinstance(instance, astm::gastm::ShortInteger)

@given(instance=astm::gastm::Character_strategy)
@settings(max_examples=50)
def test_astm::gastm::character_instantiation(instance):
    assert isinstance(instance, astm::gastm::Character)

@given(instance=astm::gastm::Float_strategy)
@settings(max_examples=50)
def test_astm::gastm::float_instantiation(instance):
    assert isinstance(instance, astm::gastm::Float)

@given(instance=astm::gastm::Integer_strategy)
@settings(max_examples=50)
def test_astm::gastm::integer_instantiation(instance):
    assert isinstance(instance, astm::gastm::Integer)

@given(instance=astm::gastm::LongDouble_strategy)
@settings(max_examples=50)
def test_astm::gastm::longdouble_instantiation(instance):
    assert isinstance(instance, astm::gastm::LongDouble)

@given(instance=astm::gastm::WideCharacter_strategy)
@settings(max_examples=50)
def test_astm::gastm::widecharacter_instantiation(instance):
    assert isinstance(instance, astm::gastm::WideCharacter)

@given(instance=astm::gastm::Boolean_strategy)
@settings(max_examples=50)
def test_astm::gastm::boolean_instantiation(instance):
    assert isinstance(instance, astm::gastm::Boolean)

@given(instance=astm::gastm::String_strategy)
@settings(max_examples=50)
def test_astm::gastm::string_instantiation(instance):
    assert isinstance(instance, astm::gastm::String)

@given(instance=astm::gastm::Byte_strategy)
@settings(max_examples=50)
def test_astm::gastm::byte_instantiation(instance):
    assert isinstance(instance, astm::gastm::Byte)

@given(instance=astm::gastm::Void_strategy)
@settings(max_examples=50)
def test_astm::gastm::void_instantiation(instance):
    assert isinstance(instance, astm::gastm::Void)

@given(instance=DerivesFrom_strategy)
@settings(max_examples=50)
def test_derivesfrom_instantiation(instance):
    assert isinstance(instance, DerivesFrom)

@given(instance=FormalParameterType_strategy)
@settings(max_examples=50)
def test_formalparametertype_instantiation(instance):
    assert isinstance(instance, FormalParameterType)

@given(instance=astm::gastm::ByReferenceFormalParameterType_strategy)
@settings(max_examples=50)
def test_astm::gastm::byreferenceformalparametertype_instantiation(instance):
    assert isinstance(instance, astm::gastm::ByReferenceFormalParameterType)

@given(instance=astm::gastm::ByValueFormalParameterType_strategy)
@settings(max_examples=50)
def test_astm::gastm::byvalueformalparametertype_instantiation(instance):
    assert isinstance(instance, astm::gastm::ByValueFormalParameterType)

@given(instance=EnumLiteralDefinition_strategy)
@settings(max_examples=50)
def test_enumliteraldefinition_instantiation(instance):
    assert isinstance(instance, EnumLiteralDefinition)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=astm::gastm::FormalParameterType_strategy)
@settings(max_examples=50)
def test_astm::gastm::formalparametertype_instantiation(instance):
    assert isinstance(instance, astm::gastm::FormalParameterType)

@given(instance=astm::gastm::AggregateType_strategy)
@settings(max_examples=50)
def test_astm::gastm::aggregatetype_instantiation(instance):
    assert isinstance(instance, astm::gastm::AggregateType)

@given(instance=astm::gastm::ConstructedType_strategy)
@settings(max_examples=50)
def test_astm::gastm::constructedtype_instantiation(instance):
    assert isinstance(instance, astm::gastm::ConstructedType)

@given(instance=astm::gastm::EnumType_strategy)
@settings(max_examples=50)
def test_astm::gastm::enumtype_instantiation(instance):
    assert isinstance(instance, astm::gastm::EnumType)

@given(instance=astm::gastm::ExceptionType_strategy)
@settings(max_examples=50)
def test_astm::gastm::exceptiontype_instantiation(instance):
    assert isinstance(instance, astm::gastm::ExceptionType)

@given(instance=astm::gastm::NamedType_strategy)
@settings(max_examples=50)
def test_astm::gastm::namedtype_instantiation(instance):
    assert isinstance(instance, astm::gastm::NamedType)

@given(instance=astm::gastm::PrimitiveType_strategy)
@settings(max_examples=50)
def test_astm::gastm::primitivetype_instantiation(instance):
    assert isinstance(instance, astm::gastm::PrimitiveType)

@given(instance=astm::gastm::PrimitiveType_strategy)
def test_astm::gastm::primitivetype_isSigned_type(instance):
    assert isinstance(instance.isSigned, bool)


@given(instance=astm::gastm::PrimitiveType_strategy)
def test_astm::gastm::primitivetype_isSigned_setter(instance):
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

@given(instance=astm::gastm::FormalParameterDefinition_strategy)
@settings(max_examples=50)
def test_astm::gastm::formalparameterdefinition_instantiation(instance):
    assert isinstance(instance, astm::gastm::FormalParameterDefinition)

@given(instance=astm::gastm::VariableDefinition_strategy)
@settings(max_examples=50)
def test_astm::gastm::variabledefinition_instantiation(instance):
    assert isinstance(instance, astm::gastm::VariableDefinition)

@given(instance=astm::gastm::BitFieldDefinition_strategy)
@settings(max_examples=50)
def test_astm::gastm::bitfielddefinition_instantiation(instance):
    assert isinstance(instance, astm::gastm::BitFieldDefinition)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=astm::gastm::RangeExpression_strategy)
@settings(max_examples=50)
def test_astm::gastm::rangeexpression_instantiation(instance):
    assert isinstance(instance, astm::gastm::RangeExpression)

@given(instance=astm::gastm::BinaryExpression_strategy)
@settings(max_examples=50)
def test_astm::gastm::binaryexpression_instantiation(instance):
    assert isinstance(instance, astm::gastm::BinaryExpression)

@given(instance=astm::gastm::ArrayAccess_strategy)
@settings(max_examples=50)
def test_astm::gastm::arrayaccess_instantiation(instance):
    assert isinstance(instance, astm::gastm::ArrayAccess)

@given(instance=astm::gastm::AnnotationExpression_strategy)
@settings(max_examples=50)
def test_astm::gastm::annotationexpression_instantiation(instance):
    assert isinstance(instance, astm::gastm::AnnotationExpression)

@given(instance=astm::gastm::NewExpression_strategy)
@settings(max_examples=50)
def test_astm::gastm::newexpression_instantiation(instance):
    assert isinstance(instance, astm::gastm::NewExpression)

@given(instance=astm::gastm::UnaryExpression_strategy)
@settings(max_examples=50)
def test_astm::gastm::unaryexpression_instantiation(instance):
    assert isinstance(instance, astm::gastm::UnaryExpression)

@given(instance=astm::gastm::AggregateExpression_strategy)
@settings(max_examples=50)
def test_astm::gastm::aggregateexpression_instantiation(instance):
    assert isinstance(instance, astm::gastm::AggregateExpression)

@given(instance=astm::gastm::NameReference_strategy)
@settings(max_examples=50)
def test_astm::gastm::namereference_instantiation(instance):
    assert isinstance(instance, astm::gastm::NameReference)

@given(instance=astm::gastm::Literal_strategy)
@settings(max_examples=50)
def test_astm::gastm::literal_instantiation(instance):
    assert isinstance(instance, astm::gastm::Literal)

@given(instance=astm::gastm::Literal_strategy)
def test_astm::gastm::literal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=astm::gastm::Literal_strategy)
def test_astm::gastm::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=astm::gastm::FunctionCallExpression_strategy)
@settings(max_examples=50)
def test_astm::gastm::functioncallexpression_instantiation(instance):
    assert isinstance(instance, astm::gastm::FunctionCallExpression)

@given(instance=astm::gastm::LabelAccess_strategy)
@settings(max_examples=50)
def test_astm::gastm::labelaccess_instantiation(instance):
    assert isinstance(instance, astm::gastm::LabelAccess)

@given(instance=astm::gastm::CastExpression_strategy)
@settings(max_examples=50)
def test_astm::gastm::castexpression_instantiation(instance):
    assert isinstance(instance, astm::gastm::CastExpression)

@given(instance=astm::gastm::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_astm::gastm::conditionalexpression_instantiation(instance):
    assert isinstance(instance, astm::gastm::ConditionalExpression)

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

@given(instance=astm::gastm::ClassType_strategy)
@settings(max_examples=50)
def test_astm::gastm::classtype_instantiation(instance):
    assert isinstance(instance, astm::gastm::ClassType)

@given(instance=astm::gastm::UnionType_strategy)
@settings(max_examples=50)
def test_astm::gastm::uniontype_instantiation(instance):
    assert isinstance(instance, astm::gastm::UnionType)

@given(instance=astm::gastm::StructureType_strategy)
@settings(max_examples=50)
def test_astm::gastm::structuretype_instantiation(instance):
    assert isinstance(instance, astm::gastm::StructureType)

@given(instance=astm::gastm::AnnotationType_strategy)
@settings(max_examples=50)
def test_astm::gastm::annotationtype_instantiation(instance):
    assert isinstance(instance, astm::gastm::AnnotationType)

@given(instance=NamedType_strategy)
@settings(max_examples=50)
def test_namedtype_instantiation(instance):
    assert isinstance(instance, NamedType)

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=astm::gastm::AggregateTypeDefinition_strategy)
@settings(max_examples=50)
def test_astm::gastm::aggregatetypedefinition_instantiation(instance):
    assert isinstance(instance, astm::gastm::AggregateTypeDefinition)

@given(instance=astm::gastm::NamedTypeDefinition_strategy)
@settings(max_examples=50)
def test_astm::gastm::namedtypedefinition_instantiation(instance):
    assert isinstance(instance, astm::gastm::NamedTypeDefinition)

@given(instance=Definition_strategy)
@settings(max_examples=50)
def test_definition_instantiation(instance):
    assert isinstance(instance, Definition)

@given(instance=astm::gastm::EntryDefinition_strategy)
@settings(max_examples=50)
def test_astm::gastm::entrydefinition_instantiation(instance):
    assert isinstance(instance, astm::gastm::EntryDefinition)

@given(instance=astm::gastm::SpecificTriggerDefinition_strategy)
@settings(max_examples=50)
def test_astm::gastm::specifictriggerdefinition_instantiation(instance):
    assert isinstance(instance, astm::gastm::SpecificTriggerDefinition)

@given(instance=astm::gastm::EnumLiteralDefinition_strategy)
@settings(max_examples=50)
def test_astm::gastm::enumliteraldefinition_instantiation(instance):
    assert isinstance(instance, astm::gastm::EnumLiteralDefinition)

@given(instance=astm::gastm::DataDefinition_strategy)
@settings(max_examples=50)
def test_astm::gastm::datadefinition_instantiation(instance):
    assert isinstance(instance, astm::gastm::DataDefinition)

@given(instance=astm::gastm::DataDefinition_strategy)
def test_astm::gastm::datadefinition_isMutable_type(instance):
    assert isinstance(instance.isMutable, bool)


@given(instance=astm::gastm::DataDefinition_strategy)
def test_astm::gastm::datadefinition_isMutable_setter(instance):
    original = instance.isMutable
    instance.isMutable = original
    assert instance.isMutable == original

@given(instance=TypeReference_strategy)
@settings(max_examples=50)
def test_typereference_instantiation(instance):
    assert isinstance(instance, TypeReference)

@given(instance=astm::gastm::UnnamedTypeReference_strategy)
@settings(max_examples=50)
def test_astm::gastm::unnamedtypereference_instantiation(instance):
    assert isinstance(instance, astm::gastm::UnnamedTypeReference)

@given(instance=astm::gastm::NamedTypeReference_strategy)
@settings(max_examples=50)
def test_astm::gastm::namedtypereference_instantiation(instance):
    assert isinstance(instance, astm::gastm::NamedTypeReference)

@given(instance=Name_strategy)
@settings(max_examples=50)
def test_name_instantiation(instance):
    assert isinstance(instance, Name)

@given(instance=DeclarationOrDefinition_strategy)
@settings(max_examples=50)
def test_declarationordefinition_instantiation(instance):
    assert isinstance(instance, DeclarationOrDefinition)

@given(instance=astm::gastm::Declaration_strategy)
@settings(max_examples=50)
def test_astm::gastm::declaration_instantiation(instance):
    assert isinstance(instance, astm::gastm::Declaration)

@given(instance=astm::gastm::Definition_strategy)
@settings(max_examples=50)
def test_astm::gastm::definition_instantiation(instance):
    assert isinstance(instance, astm::gastm::Definition)

@given(instance=VirtualSpecification_strategy)
@settings(max_examples=50)
def test_virtualspecification_instantiation(instance):
    assert isinstance(instance, VirtualSpecification)

@given(instance=astm::gastm::PureVirtual_strategy)
@settings(max_examples=50)
def test_astm::gastm::purevirtual_instantiation(instance):
    assert isinstance(instance, astm::gastm::PureVirtual)

@given(instance=astm::gastm::Virtual_strategy)
@settings(max_examples=50)
def test_astm::gastm::virtual_instantiation(instance):
    assert isinstance(instance, astm::gastm::Virtual)

@given(instance=astm::gastm::NonVirtual_strategy)
@settings(max_examples=50)
def test_astm::gastm::nonvirtual_instantiation(instance):
    assert isinstance(instance, astm::gastm::NonVirtual)

@given(instance=astm::gastm::FunctionMemberAttributes_strategy)
@settings(max_examples=50)
def test_astm::gastm::functionmemberattributes_instantiation(instance):
    assert isinstance(instance, astm::gastm::FunctionMemberAttributes)

@given(instance=astm::gastm::FunctionMemberAttributes_strategy)
def test_astm::gastm::functionmemberattributes_isThisConst_type(instance):
    assert isinstance(instance.isThisConst, bool)


@given(instance=astm::gastm::FunctionMemberAttributes_strategy)
def test_astm::gastm::functionmemberattributes_isThisConst_setter(instance):
    original = instance.isThisConst
    instance.isThisConst = original
    assert instance.isThisConst == original

@given(instance=astm::gastm::FunctionMemberAttributes_strategy)
def test_astm::gastm::functionmemberattributes_isFriend_type(instance):
    assert isinstance(instance.isFriend, bool)


@given(instance=astm::gastm::FunctionMemberAttributes_strategy)
def test_astm::gastm::functionmemberattributes_isFriend_setter(instance):
    original = instance.isFriend
    instance.isFriend = original
    assert instance.isFriend == original

@given(instance=astm::gastm::FunctionMemberAttributes_strategy)
def test_astm::gastm::functionmemberattributes_isInline_type(instance):
    assert isinstance(instance.isInline, bool)


@given(instance=astm::gastm::FunctionMemberAttributes_strategy)
def test_astm::gastm::functionmemberattributes_isInline_setter(instance):
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

@given(instance=astm::gastm::ContinueStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::continuestatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::ContinueStatement)

@given(instance=astm::gastm::TerminateStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::terminatestatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::TerminateStatement)

@given(instance=astm::gastm::ThrowStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::throwstatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::ThrowStatement)

@given(instance=astm::gastm::ReturnStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::returnstatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::ReturnStatement)

@given(instance=astm::gastm::SpecificSelectStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::specificselectstatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::SpecificSelectStatement)

@given(instance=astm::gastm::EmptyStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::emptystatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::EmptyStatement)

@given(instance=astm::gastm::BreakStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::breakstatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::BreakStatement)

@given(instance=astm::gastm::LabeledStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::labeledstatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::LabeledStatement)

@given(instance=astm::gastm::LoopStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::loopstatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::LoopStatement)

@given(instance=astm::gastm::JumpStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::jumpstatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::JumpStatement)

@given(instance=astm::gastm::DeleteStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::deletestatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::DeleteStatement)

@given(instance=astm::gastm::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::expressionstatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::ExpressionStatement)

@given(instance=astm::gastm::TryStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::trystatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::TryStatement)

@given(instance=astm::gastm::DeclarationOrDefinitionStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::declarationordefinitionstatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::DeclarationOrDefinitionStatement)

@given(instance=astm::gastm::SwitchStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::switchstatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::SwitchStatement)

@given(instance=astm::gastm::IfStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::ifstatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::IfStatement)

@given(instance=astm::gastm::BlockStatement_strategy)
@settings(max_examples=50)
def test_astm::gastm::blockstatement_instantiation(instance):
    assert isinstance(instance, astm::gastm::BlockStatement)

@given(instance=FormalParameterDefinition_strategy)
@settings(max_examples=50)
def test_formalparameterdefinition_instantiation(instance):
    assert isinstance(instance, FormalParameterDefinition)

@given(instance=astm::gastm::FunctionDefinition_strategy)
@settings(max_examples=50)
def test_astm::gastm::functiondefinition_instantiation(instance):
    assert isinstance(instance, astm::gastm::FunctionDefinition)

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

@given(instance=astm::gastm::FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_astm::gastm::functiondeclaration_instantiation(instance):
    assert isinstance(instance, astm::gastm::FunctionDeclaration)

@given(instance=astm::gastm::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_astm::gastm::variabledeclaration_instantiation(instance):
    assert isinstance(instance, astm::gastm::VariableDeclaration)

@given(instance=astm::gastm::VariableDeclaration_strategy)
def test_astm::gastm::variabledeclaration_isMutable_type(instance):
    assert isinstance(instance.isMutable, bool)


@given(instance=astm::gastm::VariableDeclaration_strategy)
def test_astm::gastm::variabledeclaration_isMutable_setter(instance):
    original = instance.isMutable
    instance.isMutable = original
    assert instance.isMutable == original

@given(instance=astm::gastm::FormalParameterDeclaration_strategy)
@settings(max_examples=50)
def test_astm::gastm::formalparameterdeclaration_instantiation(instance):
    assert isinstance(instance, astm::gastm::FormalParameterDeclaration)

@given(instance=SourceFile_strategy)
@settings(max_examples=50)
def test_sourcefile_instantiation(instance):
    assert isinstance(instance, SourceFile)

@given(instance=GASTMSourceObject_strategy)
@settings(max_examples=50)
def test_gastmsourceobject_instantiation(instance):
    assert isinstance(instance, GASTMSourceObject)

@given(instance=astm::gastm::SourceLocation_strategy)
@settings(max_examples=50)
def test_astm::gastm::sourcelocation_instantiation(instance):
    assert isinstance(instance, astm::gastm::SourceLocation)

@given(instance=astm::gastm::SourceLocation_strategy)
def test_astm::gastm::sourcelocation_startColumn_type(instance):
    assert isinstance(instance.startColumn, int)


@given(instance=astm::gastm::SourceLocation_strategy)
def test_astm::gastm::sourcelocation_startColumn_setter(instance):
    original = instance.startColumn
    instance.startColumn = original
    assert instance.startColumn == original

@given(instance=astm::gastm::SourceLocation_strategy)
def test_astm::gastm::sourcelocation_endColumn_type(instance):
    assert isinstance(instance.endColumn, int)


@given(instance=astm::gastm::SourceLocation_strategy)
def test_astm::gastm::sourcelocation_endColumn_setter(instance):
    original = instance.endColumn
    instance.endColumn = original
    assert instance.endColumn == original

@given(instance=astm::gastm::SourceLocation_strategy)
def test_astm::gastm::sourcelocation_startLine_type(instance):
    assert isinstance(instance.startLine, int)


@given(instance=astm::gastm::SourceLocation_strategy)
def test_astm::gastm::sourcelocation_startLine_setter(instance):
    original = instance.startLine
    instance.startLine = original
    assert instance.startLine == original

@given(instance=astm::gastm::SourceLocation_strategy)
def test_astm::gastm::sourcelocation_endLine_type(instance):
    assert isinstance(instance.endLine, int)


@given(instance=astm::gastm::SourceLocation_strategy)
def test_astm::gastm::sourcelocation_endLine_setter(instance):
    original = instance.endLine
    instance.endLine = original
    assert instance.endLine == original

@given(instance=astm::gastm::SourceFile_strategy)
@settings(max_examples=50)
def test_astm::gastm::sourcefile_instantiation(instance):
    assert isinstance(instance, astm::gastm::SourceFile)

@given(instance=astm::gastm::SourceFile_strategy)
def test_astm::gastm::sourcefile_pathName_type(instance):
    assert isinstance(instance.pathName, str)


@given(instance=astm::gastm::SourceFile_strategy)
def test_astm::gastm::sourcefile_pathName_setter(instance):
    original = instance.pathName
    instance.pathName = original
    assert instance.pathName == original

@given(instance=astm::gastm::ActualParameter_strategy)
@settings(max_examples=50)
def test_astm::gastm::actualparameter_instantiation(instance):
    assert isinstance(instance, astm::gastm::ActualParameter)

@given(instance=astm::gastm::BinaryOperator_strategy)
@settings(max_examples=50)
def test_astm::gastm::binaryoperator_instantiation(instance):
    assert isinstance(instance, astm::gastm::BinaryOperator)

@given(instance=astm::gastm::UnaryOperator_strategy)
@settings(max_examples=50)
def test_astm::gastm::unaryoperator_instantiation(instance):
    assert isinstance(instance, astm::gastm::UnaryOperator)

@given(instance=astm::gastm::AccessKind_strategy)
@settings(max_examples=50)
def test_astm::gastm::accesskind_instantiation(instance):
    assert isinstance(instance, astm::gastm::AccessKind)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=astm::gastm::FunctionType_strategy)
@settings(max_examples=50)
def test_astm::gastm::functiontype_instantiation(instance):
    assert isinstance(instance, astm::gastm::FunctionType)

@given(instance=astm::gastm::NameSpaceType_strategy)
@settings(max_examples=50)
def test_astm::gastm::namespacetype_instantiation(instance):
    assert isinstance(instance, astm::gastm::NameSpaceType)

@given(instance=astm::gastm::TypeReference_strategy)
@settings(max_examples=50)
def test_astm::gastm::typereference_instantiation(instance):
    assert isinstance(instance, astm::gastm::TypeReference)

@given(instance=astm::gastm::LabelType_strategy)
@settings(max_examples=50)
def test_astm::gastm::labeltype_instantiation(instance):
    assert isinstance(instance, astm::gastm::LabelType)

@given(instance=astm::gastm::DataType_strategy)
@settings(max_examples=50)
def test_astm::gastm::datatype_instantiation(instance):
    assert isinstance(instance, astm::gastm::DataType)

@given(instance=astm::gastm::StorageSpecification_strategy)
@settings(max_examples=50)
def test_astm::gastm::storagespecification_instantiation(instance):
    assert isinstance(instance, astm::gastm::StorageSpecification)

@given(instance=GASTMSyntaxObject_strategy)
@settings(max_examples=50)
def test_gastmsyntaxobject_instantiation(instance):
    assert isinstance(instance, GASTMSyntaxObject)

@given(instance=astm::gastm::DefinitionObject_strategy)
@settings(max_examples=50)
def test_astm::gastm::definitionobject_instantiation(instance):
    assert isinstance(instance, astm::gastm::DefinitionObject)

@given(instance=astm::gastm::Type_strategy)
@settings(max_examples=50)
def test_astm::gastm::type_instantiation(instance):
    assert isinstance(instance, astm::gastm::Type)

@given(instance=astm::gastm::Type_strategy)
def test_astm::gastm::type_isConst_type(instance):
    assert isinstance(instance.isConst, bool)


@given(instance=astm::gastm::Type_strategy)
def test_astm::gastm::type_isConst_setter(instance):
    original = instance.isConst
    instance.isConst = original
    assert instance.isConst == original

@given(instance=astm::gastm::Type_strategy)
def test_astm::gastm::type_isVolatile_type(instance):
    assert isinstance(instance.isVolatile, bool)


@given(instance=astm::gastm::Type_strategy)
def test_astm::gastm::type_isVolatile_setter(instance):
    original = instance.isVolatile
    instance.isVolatile = original
    assert instance.isVolatile == original

@given(instance=astm::gastm::PreprocessorElement_strategy)
@settings(max_examples=50)
def test_astm::gastm::preprocessorelement_instantiation(instance):
    assert isinstance(instance, astm::gastm::PreprocessorElement)

@given(instance=astm::gastm::Expression_strategy)
@settings(max_examples=50)
def test_astm::gastm::expression_instantiation(instance):
    assert isinstance(instance, astm::gastm::Expression)

@given(instance=astm::gastm::Statement_strategy)
@settings(max_examples=50)
def test_astm::gastm::statement_instantiation(instance):
    assert isinstance(instance, astm::gastm::Statement)

@given(instance=astm::gastm::OtherSyntaxObject_strategy)
@settings(max_examples=50)
def test_astm::gastm::othersyntaxobject_instantiation(instance):
    assert isinstance(instance, astm::gastm::OtherSyntaxObject)

@given(instance=astm::gastm::GASTMSemanticObject_strategy)
@settings(max_examples=50)
def test_astm::gastm::gastmsemanticobject_instantiation(instance):
    assert isinstance(instance, astm::gastm::GASTMSemanticObject)

@given(instance=astm::gastm::GASTMSourceObject_strategy)
@settings(max_examples=50)
def test_astm::gastm::gastmsourceobject_instantiation(instance):
    assert isinstance(instance, astm::gastm::GASTMSourceObject)

@given(instance=astm::gastm::GASTMObject_strategy)
@settings(max_examples=50)
def test_astm::gastm::gastmobject_instantiation(instance):
    assert isinstance(instance, astm::gastm::GASTMObject)

@given(instance=ProgramScope_strategy)
@settings(max_examples=50)
def test_programscope_instantiation(instance):
    assert isinstance(instance, ProgramScope)

@given(instance=OtherSyntaxObject_strategy)
@settings(max_examples=50)
def test_othersyntaxobject_instantiation(instance):
    assert isinstance(instance, OtherSyntaxObject)

@given(instance=astm::gastm::DerivesFrom_strategy)
@settings(max_examples=50)
def test_astm::gastm::derivesfrom_instantiation(instance):
    assert isinstance(instance, astm::gastm::DerivesFrom)

@given(instance=astm::gastm::DerivesFrom_strategy)
def test_astm::gastm::derivesfrom_isVirtual_type(instance):
    assert isinstance(instance.isVirtual, bool)


@given(instance=astm::gastm::DerivesFrom_strategy)
def test_astm::gastm::derivesfrom_isVirtual_setter(instance):
    original = instance.isVirtual
    instance.isVirtual = original
    assert instance.isVirtual == original

@given(instance=astm::gastm::SwitchCase_strategy)
@settings(max_examples=50)
def test_astm::gastm::switchcase_instantiation(instance):
    assert isinstance(instance, astm::gastm::SwitchCase)

@given(instance=astm::gastm::CatchBlock_strategy)
@settings(max_examples=50)
def test_astm::gastm::catchblock_instantiation(instance):
    assert isinstance(instance, astm::gastm::CatchBlock)

@given(instance=astm::gastm::Name_strategy)
@settings(max_examples=50)
def test_astm::gastm::name_instantiation(instance):
    assert isinstance(instance, astm::gastm::Name)

@given(instance=astm::gastm::Name_strategy)
def test_astm::gastm::name_nameString_type(instance):
    assert isinstance(instance.nameString, str)


@given(instance=astm::gastm::Name_strategy)
def test_astm::gastm::name_nameString_setter(instance):
    original = instance.nameString
    instance.nameString = original
    assert instance.nameString == original

@given(instance=astm::gastm::Dimension_strategy)
@settings(max_examples=50)
def test_astm::gastm::dimension_instantiation(instance):
    assert isinstance(instance, astm::gastm::Dimension)

@given(instance=astm::gastm::FunctionMemberAttribute_strategy)
@settings(max_examples=50)
def test_astm::gastm::functionmemberattribute_instantiation(instance):
    assert isinstance(instance, astm::gastm::FunctionMemberAttribute)

@given(instance=astm::gastm::VirtualSpecification_strategy)
@settings(max_examples=50)
def test_astm::gastm::virtualspecification_instantiation(instance):
    assert isinstance(instance, astm::gastm::VirtualSpecification)

@given(instance=astm::gastm::CompilationUnit_strategy)
@settings(max_examples=50)
def test_astm::gastm::compilationunit_instantiation(instance):
    assert isinstance(instance, astm::gastm::CompilationUnit)

@given(instance=astm::gastm::CompilationUnit_strategy)
def test_astm::gastm::compilationunit_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=astm::gastm::CompilationUnit_strategy)
def test_astm::gastm::compilationunit_language_setter(instance):
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

@given(instance=astm::gastm::MacroDefinition_strategy)
@settings(max_examples=50)
def test_astm::gastm::macrodefinition_instantiation(instance):
    assert isinstance(instance, astm::gastm::MacroDefinition)

@given(instance=astm::gastm::MacroDefinition_strategy)
def test_astm::gastm::macrodefinition_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=astm::gastm::MacroDefinition_strategy)
def test_astm::gastm::macrodefinition_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=astm::gastm::MacroDefinition_strategy)
def test_astm::gastm::macrodefinition_macroName_type(instance):
    assert isinstance(instance.macroName, str)


@given(instance=astm::gastm::MacroDefinition_strategy)
def test_astm::gastm::macrodefinition_macroName_setter(instance):
    original = instance.macroName
    instance.macroName = original
    assert instance.macroName == original

@given(instance=astm::gastm::MacroCall_strategy)
@settings(max_examples=50)
def test_astm::gastm::macrocall_instantiation(instance):
    assert isinstance(instance, astm::gastm::MacroCall)

@given(instance=astm::gastm::IncludeUnit_strategy)
@settings(max_examples=50)
def test_astm::gastm::includeunit_instantiation(instance):
    assert isinstance(instance, astm::gastm::IncludeUnit)

@given(instance=astm::gastm::Comment_strategy)
@settings(max_examples=50)
def test_astm::gastm::comment_instantiation(instance):
    assert isinstance(instance, astm::gastm::Comment)

@given(instance=astm::gastm::Comment_strategy)
def test_astm::gastm::comment_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=astm::gastm::Comment_strategy)
def test_astm::gastm::comment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=SourceLocation_strategy)
@settings(max_examples=50)
def test_sourcelocation_instantiation(instance):
    assert isinstance(instance, SourceLocation)

@given(instance=GASTMObject_strategy)
@settings(max_examples=50)
def test_gastmobject_instantiation(instance):
    assert isinstance(instance, GASTMObject)

@given(instance=astm::gastm::GASTMSyntaxObject_strategy)
@settings(max_examples=50)
def test_astm::gastm::gastmsyntaxobject_instantiation(instance):
    assert isinstance(instance, astm::gastm::GASTMSyntaxObject)

@given(instance=Scope_strategy)
@settings(max_examples=50)
def test_scope_instantiation(instance):
    assert isinstance(instance, Scope)

@given(instance=astm::gastm::FunctionScope_strategy)
@settings(max_examples=50)
def test_astm::gastm::functionscope_instantiation(instance):
    assert isinstance(instance, astm::gastm::FunctionScope)

@given(instance=astm::gastm::AggregateScope_strategy)
@settings(max_examples=50)
def test_astm::gastm::aggregatescope_instantiation(instance):
    assert isinstance(instance, astm::gastm::AggregateScope)

@given(instance=astm::gastm::GlobalScope_strategy)
@settings(max_examples=50)
def test_astm::gastm::globalscope_instantiation(instance):
    assert isinstance(instance, astm::gastm::GlobalScope)

@given(instance=astm::gastm::BlockScope_strategy)
@settings(max_examples=50)
def test_astm::gastm::blockscope_instantiation(instance):
    assert isinstance(instance, astm::gastm::BlockScope)

@given(instance=astm::gastm::ProgramScope_strategy)
@settings(max_examples=50)
def test_astm::gastm::programscope_instantiation(instance):
    assert isinstance(instance, astm::gastm::ProgramScope)

@given(instance=DefinitionObject_strategy)
@settings(max_examples=50)
def test_definitionobject_instantiation(instance):
    assert isinstance(instance, DefinitionObject)

@given(instance=astm::gastm::DeclarationOrDefinition_strategy)
@settings(max_examples=50)
def test_astm::gastm::declarationordefinition_instantiation(instance):
    assert isinstance(instance, astm::gastm::DeclarationOrDefinition)

@given(instance=astm::gastm::DeclarationOrDefinition_strategy)
def test_astm::gastm::declarationordefinition_isRegister_type(instance):
    assert isinstance(instance.isRegister, bool)


@given(instance=astm::gastm::DeclarationOrDefinition_strategy)
def test_astm::gastm::declarationordefinition_isRegister_setter(instance):
    original = instance.isRegister
    instance.isRegister = original
    assert instance.isRegister == original

@given(instance=astm::gastm::DeclarationOrDefinition_strategy)
def test_astm::gastm::declarationordefinition_linkageSpecifier_type(instance):
    assert isinstance(instance.linkageSpecifier, str)


@given(instance=astm::gastm::DeclarationOrDefinition_strategy)
def test_astm::gastm::declarationordefinition_linkageSpecifier_setter(instance):
    original = instance.linkageSpecifier
    instance.linkageSpecifier = original
    assert instance.linkageSpecifier == original

@given(instance=astm::gastm::TypeDefinition_strategy)
@settings(max_examples=50)
def test_astm::gastm::typedefinition_instantiation(instance):
    assert isinstance(instance, astm::gastm::TypeDefinition)

@given(instance=astm::gastm::NameSpaceDefinition_strategy)
@settings(max_examples=50)
def test_astm::gastm::namespacedefinition_instantiation(instance):
    assert isinstance(instance, astm::gastm::NameSpaceDefinition)

@given(instance=astm::gastm::LabelDefinition_strategy)
@settings(max_examples=50)
def test_astm::gastm::labeldefinition_instantiation(instance):
    assert isinstance(instance, astm::gastm::LabelDefinition)

@given(instance=GlobalScope_strategy)
@settings(max_examples=50)
def test_globalscope_instantiation(instance):
    assert isinstance(instance, GlobalScope)

@given(instance=CompilationUnit_strategy)
@settings(max_examples=50)
def test_compilationunit_instantiation(instance):
    assert isinstance(instance, CompilationUnit)

@given(instance=astm::sastm::DelphiInterfaceSection_strategy)
@settings(max_examples=50)
def test_astm::sastm::delphiinterfacesection_instantiation(instance):
    assert isinstance(instance, astm::sastm::DelphiInterfaceSection)

@given(instance=astm::sastm::DelphiUnit_strategy)
@settings(max_examples=50)
def test_astm::sastm::delphiunit_instantiation(instance):
    assert isinstance(instance, astm::sastm::DelphiUnit)

@given(instance=astm::sastm::DelphiImplementationSection_strategy)
@settings(max_examples=50)
def test_astm::sastm::delphiimplementationsection_instantiation(instance):
    assert isinstance(instance, astm::sastm::DelphiImplementationSection)

@given(instance=GASTMSemanticObject_strategy)
@settings(max_examples=50)
def test_gastmsemanticobject_instantiation(instance):
    assert isinstance(instance, GASTMSemanticObject)

@given(instance=astm::gastm::Scope_strategy)
@settings(max_examples=50)
def test_astm::gastm::scope_instantiation(instance):
    assert isinstance(instance, astm::gastm::Scope)

@given(instance=astm::gastm::Project_strategy)
@settings(max_examples=50)
def test_astm::gastm::project_instantiation(instance):
    assert isinstance(instance, astm::gastm::Project)
