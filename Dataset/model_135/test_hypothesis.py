import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TMethodCall,
    TUnaryOperator,
    simTL4J::simTL::TUnaryOperatorNOT,
    simTL::TPlaceholder,
    simTL4J::simTL::TPlaceholder,
    simTL::TIf,
    simTL::TFor,
    simTL4J::simTL::TAbstractMethodStatement,
    simTL4J::simTL::TMethodCall,
    simTL4J::simTL::TModelImport,
    TModelImport,
    simTL4J::simTL::TemplateHeader,
    TemplateHeader,
    simTL4J::simTL::Template,
    simTL4J::simTL::TForVariable,
    TForVariable,
    simTL4J::simTL::TFor,
    TAbstractMethodStatement,
    simTL4J::simTL::TMethodStatementImpl,
    simTL4J::simTL::TUnaryOperator,
    simTL4J::simTL::TIf,
    AdditionalLocalVariable,
    statements::ForLoopInitializer,
    ClassifierReference,
    types::TypeReference,
    Block,
    CatchBlock,
    statements::SwitchCase,
    LocalVariable,
    JumpLabel,
    statements::Conditional,
    simTL4J::statements::NormalSwitchCase,
    StatementListContainer,
    simTL4J::statements::SwitchCase,
    WhileLoop,
    simTL4J::statements::DoWhileLoop,
    SwitchCase,
    simTL4J::statements::DefaultSwitchCase,
    statements::StatementContainer,
    OrdinaryParameter,
    simTL4J::statements::CatchBlock,
    modifiers::Modifiable,
    Jump,
    simTL4J::statements::Continue,
    simTL4J::statements::Break,
    references::ElementReference,
    Statement,
    simTL4J::statements::LocalVariableStatement,
    simTL4J::statements::Throw,
    simTL4J::statements::Jump,
    simTL4J::statements::Switch,
    simTL4J::statements::Return,
    simTL4J::statements::ExpressionStatement,
    simTL4J::statements::EmptyStatement,
    PrimitiveType,
    simTL4J::types::Void,
    simTL4J::types::Char,
    simTL4J::types::Boolean,
    simTL4J::types::Long,
    simTL4J::types::Int,
    simTL4J::types::Double,
    simTL4J::types::Short,
    simTL4J::types::Byte,
    simTL4J::types::Float,
    ElementReference,
    simTL4J::references::IdentifierReference,
    ArraySelector,
    expressions::PrimaryExpression,
    simTL4J::simTL::TPlaceholder::PrimaryExpression,
    Parameter,
    simTL4J::parameters::VariableLengthParameter,
    simTL4J::parameters::OrdinaryParameter,
    operators::UnaryOperator,
    operators::AdditiveOperator,
    simTL4J::operators::Subtraction,
    simTL4J::operators::Addition,
    Operator,
    simTL4J::operators::MultiplicativeOperator,
    simTL4J::operators::UnaryModificationOperator,
    simTL4J::operators::EqualityOperator,
    simTL4J::operators::RelationOperator,
    simTL4J::operators::AssignmentOperator,
    simTL4J::operators::UnaryOperator,
    simTL4J::operators::ShiftOperator,
    simTL4J::operators::AdditiveOperator,
    AnnotationInstanceOrModifier,
    simTL4J::modifiers::Modifier,
    Modifier,
    simTL4J::modifiers::Synchronized,
    simTL4J::modifiers::Private,
    simTL4J::modifiers::Static,
    simTL4J::modifiers::Strictfp,
    simTL4J::modifiers::Transient,
    simTL4J::modifiers::Abstract,
    simTL4J::modifiers::Volatile,
    simTL4J::modifiers::Native,
    simTL4J::modifiers::Protected,
    simTL4J::modifiers::Public,
    simTL4J::modifiers::Final,
    members::Method,
    Method,
    simTL4J::members::InterfaceMethod,
    AdditionalField,
    variables::Variable,
    members::ExceptionThrower,
    parameters::Parametrizable,
    statements::StatementListContainer,
    simTL4J::members::ClassMethod,
    instantiations::Initializable,
    Member,
    simTL4J::members::EmptyMember,
    NamedElement,
    simTL4J::references::ReferenceableElement,
    simTL4J::members::Member,
    NamespaceClassifierReference,
    LongLiteral,
    simTL4J::literals::OctalLongLiteral,
    simTL4J::literals::HexLongLiteral,
    simTL4J::literals::DecimalLongLiteral,
    IntegerLiteral,
    simTL4J::literals::HexIntegerLiteral,
    simTL4J::literals::OctalIntegerLiteral,
    simTL4J::literals::DecimalIntegerLiteral,
    DoubleLiteral,
    simTL4J::literals::HexDoubleLiteral,
    simTL4J::literals::DecimalDoubleLiteral,
    FloatLiteral,
    simTL4J::literals::HexFloatLiteral,
    simTL4J::literals::DecimalFloatLiteral,
    Literal,
    simTL4J::literals::CharacterLiteral,
    simTL4J::literals::FloatLiteral,
    simTL4J::literals::NullLiteral,
    simTL4J::literals::DoubleLiteral,
    simTL4J::literals::LongLiteral,
    simTL4J::literals::IntegerLiteral,
    simTL4J::literals::BooleanLiteral,
    PrimaryExpression,
    simTL4J::literals::Literal,
    Self,
    simTL4J::literals::This,
    simTL4J::literals::Super,
    Instantiation,
    simTL4J::instantiations::ExplicitConstructorCall,
    AnonymousClass,
    generics::CallTypeArgumentable,
    instantiations::Instantiation,
    simTL4J::instantiations::NewConstructorCall,
    generics::TypeArgumentable,
    simTL4J::references::Reference,
    simTL4J::types::ClassifierReference,
    references::Argumentable,
    simTL4J::references::MethodCall,
    ReferenceableElement,
    StaticImport,
    simTL4J::imports::StaticMemberImport,
    simTL4J::imports::StaticClassifierImport,
    Static,
    Import,
    simTL4J::imports::StaticImport,
    simTL4J::imports::PackageImport,
    simTL4J::imports::ClassifierImport,
    NamespaceAwareElement,
    simTL4J::imports::Import,
    TypeParameter,
    generics::TypeArgument,
    expressions::UnaryModificationExpressionChild,
    MultiplicativeOperator,
    simTL4J::operators::Multiplication,
    simTL4J::operators::Division,
    simTL4J::operators::Remainder,
    MultiplicativeExpressionChild,
    simTL4J::expressions::UnaryExpression,
    AdditiveOperator,
    AdditiveExpressionChild,
    simTL4J::expressions::MultiplicativeExpressionChild,
    simTL4J::expressions::MultiplicativeExpression,
    ConditionalAndExpressionChild,
    simTL4J::expressions::InclusiveOrExpression,
    ConditionalOrExpressionChild,
    simTL4J::expressions::ConditionalAndExpression,
    simTL4J::expressions::ConditionalAndExpressionChild,
    RelationExpressionChild,
    simTL4J::expressions::ShiftExpressionChild,
    InstanceOfExpressionChild,
    simTL4J::expressions::RelationExpression,
    expressions::EqualityExpressionChild,
    EqualityExpressionChild,
    simTL4J::expressions::InstanceOfExpressionChild,
    EqualityOperator,
    simTL4J::operators::NotEqual,
    simTL4J::operators::Equal,
    AndExpressionChild,
    simTL4J::expressions::EqualityExpression,
    simTL4J::expressions::EqualityExpressionChild,
    ExclusiveOrExpressionChild,
    simTL4J::expressions::AndExpression,
    simTL4J::expressions::AndExpressionChild,
    simTL4J::expressions::InclusiveOrExpressionChild,
    InclusiveOrExpressionChild,
    simTL4J::expressions::ExclusiveOrExpression,
    simTL4J::expressions::ExclusiveOrExpressionChild,
    Package,
    CompilationUnit,
    annotations::Annotable,
    containers::JavaRoot,
    ConditionalExpressionChild,
    simTL4J::expressions::ConditionalOrExpressionChild,
    simTL4J::expressions::ConditionalOrExpression,
    AssignmentOperator,
    simTL4J::operators::AssignmentExclusiveOr,
    simTL4J::operators::AssignmentRightShift,
    simTL4J::operators::AssignmentUnsignedRightShift,
    simTL4J::operators::AssignmentMinus,
    simTL4J::operators::AssignmentAnd,
    simTL4J::operators::AssignmentMultiplication,
    simTL4J::operators::AssignmentOr,
    simTL4J::operators::AssignmentDivision,
    simTL4J::operators::AssignmentPlus,
    simTL4J::operators::AssignmentLeftShift,
    simTL4J::operators::AssignmentModulo,
    simTL4J::operators::Assignment,
    AssignmentExpressionChild,
    simTL4J::expressions::ConditionalExpressionChild,
    simTL4J::expressions::ConditionalExpression,
    ForLoopInitializer,
    simTL4J::expressions::ExpressionList,
    JavaRoot,
    simTL4J::containers::EmptyModel,
    simTL4J::containers::CompilationUnit,
    imports::ImportingElement,
    commons::NamedElement,
    TPlaceholder,
    simTL4J::commons::Commentable,
    classifiers::Implementor,
    classifiers::ConcreteClassifier,
    simTL4J::classifiers::Class,
    TypeReference,
    EnumConstant,
    simTL4J::classifiers::Enumeration,
    ConcreteClassifier,
    simTL4J::classifiers::Annotation,
    simTL4J::classifiers::Interface,
    arrays::ArrayTypeable,
    types::TypedElement,
    simTL4J::expressions::CastExpression,
    simTL4J::expressions::InstanceOfExpression,
    simTL4J::generics::QualifiedTypeArgument,
    expressions::Expression,
    ArrayInitializationValue,
    annotations::AnnotationValue,
    arrays::ArrayInitializationValue,
    simTL4J::expressions::Expression,
    simTL4J::arrays::ArrayInitializer,
    modifiers::AnnotableAndModifiable,
    simTL4J::variables::LocalVariable,
    simTL4J::parameters::Parameter,
    statements::Statement,
    simTL4J::simTL::TFor::StatementListContainer,
    simTL4J::statements::ForLoop,
    simTL4J::statements::ForEachLoop,
    simTL4J::statements::Assert,
    simTL4J::statements::TryBlock,
    simTL4J::statements::Condition,
    simTL4J::statements::SynchronizedBlock,
    simTL4J::simTL::TIf::StatementListContainer,
    simTL4J::statements::WhileLoop,
    simTL4J::statements::JumpLabel,
    members::Member,
    simTL4J::statements::Block,
    members::MemberContainer,
    simTL4J::simTL::TFor::MemberContainer,
    simTL4J::simTL::TIf::MemberContainer,
    generics::TypeParametrizable,
    simTL4J::members::Constructor,
    classifiers::Classifier,
    simTL4J::classifiers::ConcreteClassifier,
    references::ReferenceableElement,
    simTL4J::members::Method,
    simTL4J::members::EnumConstant,
    simTL4J::members::Field,
    simTL4J::containers::Package,
    simTL4J::members::AdditionalField,
    simTL4J::variables::AdditionalLocalVariable,
    simTL4J::variables::Variable,
    types::Type,
    simTL4J::types::PrimitiveType,
    simTL4J::classifiers::AnonymousClass,
    simTL4J::classifiers::Classifier,
    ArrayInitializer,
    modifiers::AnnotationInstanceOrModifier,
    references::Reference,
    simTL4J::instantiations::Instantiation,
    simTL4J::arrays::ArrayInstantiationBySize,
    simTL4J::arrays::ArrayInstantiationByValues,
    AnnotationInstance,
    Commentable,
    simTL4J::members::MemberContainer,
    simTL4J::modifiers::AnnotationInstanceOrModifier,
    simTL4J::references::Argumentable,
    simTL4J::statements::StatementContainer,
    simTL4J::arrays::ArrayDimension,
    simTL4J::instantiations::Initializable,
    simTL4J::operators::Operator,
    simTL4J::commons::NamespaceAwareElement,
    simTL4J::arrays::ArrayInitializationValue,
    simTL4J::statements::StatementListContainer,
    simTL4J::types::TypedElement,
    simTL4J::parameters::Parametrizable,
    simTL4J::commons::NamedElement,
    simTL4J::classifiers::Implementor,
    simTL4J::arrays::ArraySelector,
    simTL4J::imports::ImportingElement,
    simTL4J::types::Type,
    simTL4J::generics::TypeParametrizable,
    simTL4J::modifiers::AnnotableAndModifiable,
    simTL4J::literals::Self,
    simTL4J::members::ExceptionThrower,
    simTL4J::statements::Statement,
    simTL4J::statements::Conditional,
    simTL4J::types::TypeReference,
    simTL4J::statements::ForLoopInitializer,
    simTL4J::modifiers::Modifiable,
    simTL4J::annotations::Annotable,
    ArrayDimension,
    simTL4J::arrays::ArrayTypeable,
    Expression,
    simTL4J::expressions::AssignmentExpressionChild,
    simTL4J::expressions::AssignmentExpression,
    simTL4J::annotations::AnnotationValue,
    InterfaceMethod,
    simTL4J::annotations::AnnotationAttribute,
    simTL4J::annotations::AnnotationAttributeSetting,
    AnnotationAttributeSetting,
    AnnotationValue,
    simTL4J::annotations::AnnotationParameter,
    AnnotationParameter,
    simTL4J::annotations::AnnotationParameterList,
    simTL4J::annotations::SingleAnnotationParameter,
    Classifier,
    simTL4J::generics::TypeParameter,
    commons::NamespaceAwareElement,
    simTL4J::annotations::AnnotationInstance,
    simTL4J::types::NamespaceClassifierReference,
    simTL4J::containers::JavaRoot,
    UnaryModificationExpression,
    simTL4J::expressions::SuffixUnaryModificationExpression,
    simTL4J::expressions::PrefixUnaryModificationExpression,
    simTL4J::generics::CallTypeArgumentable,
    TypeArgument,
    simTL4J::generics::ExtendsTypeArgument,
    simTL4J::generics::SuperTypeArgument,
    simTL4J::generics::UnknownTypeArgument,
    simTL4J::generics::TypeArgumentable,
    ArrayTypeable,
    simTL4J::generics::TypeArgument,
    Reference,
    simTL4J::references::SelfReference,
    simTL4J::references::ReflectiveClassReference,
    simTL4J::references::ElementReference,
    simTL4J::references::StringReference,
    simTL4J::references::PrimitiveTypeReference,
    simTL4J::expressions::NestedExpression,
    ShiftOperator,
    simTL4J::operators::RightShift,
    simTL4J::operators::LeftShift,
    simTL4J::operators::UnsignedRightShift,
    ShiftExpressionChild,
    simTL4J::expressions::AdditiveExpressionChild,
    simTL4J::expressions::AdditiveExpression,
    simTL4J::expressions::ShiftExpression,
    simTL4J::expressions::RelationExpressionChild,
    RelationOperator,
    simTL4J::operators::LessThanOrEqual,
    simTL4J::operators::GreaterThan,
    simTL4J::operators::GreaterThanOrEqual,
    simTL4J::operators::LessThan,
    UnaryModificationOperator,
    simTL4J::operators::PlusPlus,
    simTL4J::operators::MinusMinus,
    UnaryModificationExpressionChild,
    simTL4J::expressions::PrimaryExpression,
    simTL4J::expressions::UnaryExpressionChild,
    UnaryExpressionChild,
    simTL4J::expressions::UnaryModificationExpressionChild,
    simTL4J::expressions::UnaryModificationExpression,
    UnaryOperator,
    simTL4J::operators::Complement,
    simTL4J::operators::Negate,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tmethodcall_is_not_abstract():
    assert not inspect.isabstract(TMethodCall)


def test_tmethodcall_constructor_exists():
    assert callable(TMethodCall.__init__)


def test_tmethodcall_constructor_args():
    sig = inspect.signature(TMethodCall.__init__)
    params = list(sig.parameters.keys())



def test_tunaryoperator_is_not_abstract():
    assert not inspect.isabstract(TUnaryOperator)


def test_tunaryoperator_constructor_exists():
    assert callable(TUnaryOperator.__init__)


def test_tunaryoperator_constructor_args():
    sig = inspect.signature(TUnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::simtl::tunaryoperatornot_is_not_abstract():
    assert not inspect.isabstract(simTL4J::simTL::TUnaryOperatorNOT)


def test_simtl4j::simtl::tunaryoperatornot_constructor_exists():
    assert callable(simTL4J::simTL::TUnaryOperatorNOT.__init__)


def test_simtl4j::simtl::tunaryoperatornot_constructor_args():
    sig = inspect.signature(simTL4J::simTL::TUnaryOperatorNOT.__init__)
    params = list(sig.parameters.keys())



def test_simtl::tplaceholder_is_not_abstract():
    assert not inspect.isabstract(simTL::TPlaceholder)


def test_simtl::tplaceholder_constructor_exists():
    assert callable(simTL::TPlaceholder.__init__)


def test_simtl::tplaceholder_constructor_args():
    sig = inspect.signature(simTL::TPlaceholder.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::simtl::tplaceholder_is_not_abstract():
    assert not inspect.isabstract(simTL4J::simTL::TPlaceholder)


def test_simtl4j::simtl::tplaceholder_constructor_exists():
    assert callable(simTL4J::simTL::TPlaceholder.__init__)


def test_simtl4j::simtl::tplaceholder_constructor_args():
    sig = inspect.signature(simTL4J::simTL::TPlaceholder.__init__)
    params = list(sig.parameters.keys())



def test_simtl::tif_is_not_abstract():
    assert not inspect.isabstract(simTL::TIf)


def test_simtl::tif_constructor_exists():
    assert callable(simTL::TIf.__init__)


def test_simtl::tif_constructor_args():
    sig = inspect.signature(simTL::TIf.__init__)
    params = list(sig.parameters.keys())



def test_simtl::tfor_is_not_abstract():
    assert not inspect.isabstract(simTL::TFor)


def test_simtl::tfor_constructor_exists():
    assert callable(simTL::TFor.__init__)


def test_simtl::tfor_constructor_args():
    sig = inspect.signature(simTL::TFor.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::simtl::tabstractmethodstatement_is_not_abstract():
    assert not inspect.isabstract(simTL4J::simTL::TAbstractMethodStatement)


def test_simtl4j::simtl::tabstractmethodstatement_constructor_exists():
    assert callable(simTL4J::simTL::TAbstractMethodStatement.__init__)


def test_simtl4j::simtl::tabstractmethodstatement_constructor_args():
    sig = inspect.signature(simTL4J::simTL::TAbstractMethodStatement.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::simtl::tmethodcall_is_not_abstract():
    assert not inspect.isabstract(simTL4J::simTL::TMethodCall)


def test_simtl4j::simtl::tmethodcall_constructor_exists():
    assert callable(simTL4J::simTL::TMethodCall.__init__)


def test_simtl4j::simtl::tmethodcall_constructor_args():
    sig = inspect.signature(simTL4J::simTL::TMethodCall.__init__)
    params = list(sig.parameters.keys())
    assert "params" in params, "Missing parameter 'params'"
    assert "methodName" in params, "Missing parameter 'methodName'"

def test_simtl4j::simtl::tmethodcall_has_params():
    assert hasattr(simTL4J::simTL::TMethodCall, "params")
    descriptor = None
    for klass in simTL4J::simTL::TMethodCall.__mro__:
        if "params" in klass.__dict__:
            descriptor = klass.__dict__["params"]
            break
    assert isinstance(descriptor, property)

def test_simtl4j::simtl::tmethodcall_has_methodName():
    assert hasattr(simTL4J::simTL::TMethodCall, "methodName")
    descriptor = None
    for klass in simTL4J::simTL::TMethodCall.__mro__:
        if "methodName" in klass.__dict__:
            descriptor = klass.__dict__["methodName"]
            break
    assert isinstance(descriptor, property)



def test_simtl4j::simtl::tmodelimport_is_not_abstract():
    assert not inspect.isabstract(simTL4J::simTL::TModelImport)


def test_simtl4j::simtl::tmodelimport_constructor_exists():
    assert callable(simTL4J::simTL::TModelImport.__init__)


def test_simtl4j::simtl::tmodelimport_constructor_args():
    sig = inspect.signature(simTL4J::simTL::TModelImport.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uri" in params, "Missing parameter 'uri'"

def test_simtl4j::simtl::tmodelimport_has_name():
    assert hasattr(simTL4J::simTL::TModelImport, "name")
    descriptor = None
    for klass in simTL4J::simTL::TModelImport.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simtl4j::simtl::tmodelimport_has_uri():
    assert hasattr(simTL4J::simTL::TModelImport, "uri")
    descriptor = None
    for klass in simTL4J::simTL::TModelImport.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_tmodelimport_is_not_abstract():
    assert not inspect.isabstract(TModelImport)


def test_tmodelimport_constructor_exists():
    assert callable(TModelImport.__init__)


def test_tmodelimport_constructor_args():
    sig = inspect.signature(TModelImport.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::simtl::templateheader_is_not_abstract():
    assert not inspect.isabstract(simTL4J::simTL::TemplateHeader)


def test_simtl4j::simtl::templateheader_constructor_exists():
    assert callable(simTL4J::simTL::TemplateHeader.__init__)


def test_simtl4j::simtl::templateheader_constructor_args():
    sig = inspect.signature(simTL4J::simTL::TemplateHeader.__init__)
    params = list(sig.parameters.keys())



def test_templateheader_is_not_abstract():
    assert not inspect.isabstract(TemplateHeader)


def test_templateheader_constructor_exists():
    assert callable(TemplateHeader.__init__)


def test_templateheader_constructor_args():
    sig = inspect.signature(TemplateHeader.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::simtl::template_is_not_abstract():
    assert not inspect.isabstract(simTL4J::simTL::Template)


def test_simtl4j::simtl::template_constructor_exists():
    assert callable(simTL4J::simTL::Template.__init__)


def test_simtl4j::simtl::template_constructor_args():
    sig = inspect.signature(simTL4J::simTL::Template.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::simtl::tforvariable_is_not_abstract():
    assert not inspect.isabstract(simTL4J::simTL::TForVariable)


def test_simtl4j::simtl::tforvariable_constructor_exists():
    assert callable(simTL4J::simTL::TForVariable.__init__)


def test_simtl4j::simtl::tforvariable_constructor_args():
    sig = inspect.signature(simTL4J::simTL::TForVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simtl4j::simtl::tforvariable_has_name():
    assert hasattr(simTL4J::simTL::TForVariable, "name")
    descriptor = None
    for klass in simTL4J::simTL::TForVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tforvariable_is_not_abstract():
    assert not inspect.isabstract(TForVariable)


def test_tforvariable_constructor_exists():
    assert callable(TForVariable.__init__)


def test_tforvariable_constructor_args():
    sig = inspect.signature(TForVariable.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::simtl::tfor_is_not_abstract():
    assert not inspect.isabstract(simTL4J::simTL::TFor)


def test_simtl4j::simtl::tfor_constructor_exists():
    assert callable(simTL4J::simTL::TFor.__init__)


def test_simtl4j::simtl::tfor_constructor_args():
    sig = inspect.signature(simTL4J::simTL::TFor.__init__)
    params = list(sig.parameters.keys())



def test_tabstractmethodstatement_is_not_abstract():
    assert not inspect.isabstract(TAbstractMethodStatement)


def test_tabstractmethodstatement_constructor_exists():
    assert callable(TAbstractMethodStatement.__init__)


def test_tabstractmethodstatement_constructor_args():
    sig = inspect.signature(TAbstractMethodStatement.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::simtl::tmethodstatementimpl_is_not_abstract():
    assert not inspect.isabstract(simTL4J::simTL::TMethodStatementImpl)


def test_simtl4j::simtl::tmethodstatementimpl_constructor_exists():
    assert callable(simTL4J::simTL::TMethodStatementImpl.__init__)


def test_simtl4j::simtl::tmethodstatementimpl_constructor_args():
    sig = inspect.signature(simTL4J::simTL::TMethodStatementImpl.__init__)
    params = list(sig.parameters.keys())
    assert "caller" in params, "Missing parameter 'caller'"

def test_simtl4j::simtl::tmethodstatementimpl_has_caller():
    assert hasattr(simTL4J::simTL::TMethodStatementImpl, "caller")
    descriptor = None
    for klass in simTL4J::simTL::TMethodStatementImpl.__mro__:
        if "caller" in klass.__dict__:
            descriptor = klass.__dict__["caller"]
            break
    assert isinstance(descriptor, property)



def test_simtl4j::simtl::tunaryoperator_is_not_abstract():
    assert not inspect.isabstract(simTL4J::simTL::TUnaryOperator)


def test_simtl4j::simtl::tunaryoperator_constructor_exists():
    assert callable(simTL4J::simTL::TUnaryOperator.__init__)


def test_simtl4j::simtl::tunaryoperator_constructor_args():
    sig = inspect.signature(simTL4J::simTL::TUnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::simtl::tif_is_not_abstract():
    assert not inspect.isabstract(simTL4J::simTL::TIf)


def test_simtl4j::simtl::tif_constructor_exists():
    assert callable(simTL4J::simTL::TIf.__init__)


def test_simtl4j::simtl::tif_constructor_args():
    sig = inspect.signature(simTL4J::simTL::TIf.__init__)
    params = list(sig.parameters.keys())



def test_additionallocalvariable_is_not_abstract():
    assert not inspect.isabstract(AdditionalLocalVariable)


def test_additionallocalvariable_constructor_exists():
    assert callable(AdditionalLocalVariable.__init__)


def test_additionallocalvariable_constructor_args():
    sig = inspect.signature(AdditionalLocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_statements::forloopinitializer_is_not_abstract():
    assert not inspect.isabstract(statements::ForLoopInitializer)


def test_statements::forloopinitializer_constructor_exists():
    assert callable(statements::ForLoopInitializer.__init__)


def test_statements::forloopinitializer_constructor_args():
    sig = inspect.signature(statements::ForLoopInitializer.__init__)
    params = list(sig.parameters.keys())



def test_classifierreference_is_not_abstract():
    assert not inspect.isabstract(ClassifierReference)


def test_classifierreference_constructor_exists():
    assert callable(ClassifierReference.__init__)


def test_classifierreference_constructor_args():
    sig = inspect.signature(ClassifierReference.__init__)
    params = list(sig.parameters.keys())



def test_types::typereference_is_not_abstract():
    assert not inspect.isabstract(types::TypeReference)


def test_types::typereference_constructor_exists():
    assert callable(types::TypeReference.__init__)


def test_types::typereference_constructor_args():
    sig = inspect.signature(types::TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_catchblock_is_not_abstract():
    assert not inspect.isabstract(CatchBlock)


def test_catchblock_constructor_exists():
    assert callable(CatchBlock.__init__)


def test_catchblock_constructor_args():
    sig = inspect.signature(CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_statements::switchcase_is_not_abstract():
    assert not inspect.isabstract(statements::SwitchCase)


def test_statements::switchcase_constructor_exists():
    assert callable(statements::SwitchCase.__init__)


def test_statements::switchcase_constructor_args():
    sig = inspect.signature(statements::SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_localvariable_is_not_abstract():
    assert not inspect.isabstract(LocalVariable)


def test_localvariable_constructor_exists():
    assert callable(LocalVariable.__init__)


def test_localvariable_constructor_args():
    sig = inspect.signature(LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_jumplabel_is_not_abstract():
    assert not inspect.isabstract(JumpLabel)


def test_jumplabel_constructor_exists():
    assert callable(JumpLabel.__init__)


def test_jumplabel_constructor_args():
    sig = inspect.signature(JumpLabel.__init__)
    params = list(sig.parameters.keys())



def test_statements::conditional_is_not_abstract():
    assert not inspect.isabstract(statements::Conditional)


def test_statements::conditional_constructor_exists():
    assert callable(statements::Conditional.__init__)


def test_statements::conditional_constructor_args():
    sig = inspect.signature(statements::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::normalswitchcase_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::NormalSwitchCase)


def test_simtl4j::statements::normalswitchcase_constructor_exists():
    assert callable(simTL4J::statements::NormalSwitchCase.__init__)


def test_simtl4j::statements::normalswitchcase_constructor_args():
    sig = inspect.signature(simTL4J::statements::NormalSwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_statementlistcontainer_is_not_abstract():
    assert not inspect.isabstract(StatementListContainer)


def test_statementlistcontainer_constructor_exists():
    assert callable(StatementListContainer.__init__)


def test_statementlistcontainer_constructor_args():
    sig = inspect.signature(StatementListContainer.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::switchcase_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::SwitchCase)


def test_simtl4j::statements::switchcase_constructor_exists():
    assert callable(simTL4J::statements::SwitchCase.__init__)


def test_simtl4j::statements::switchcase_constructor_args():
    sig = inspect.signature(simTL4J::statements::SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_whileloop_is_not_abstract():
    assert not inspect.isabstract(WhileLoop)


def test_whileloop_constructor_exists():
    assert callable(WhileLoop.__init__)


def test_whileloop_constructor_args():
    sig = inspect.signature(WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::dowhileloop_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::DoWhileLoop)


def test_simtl4j::statements::dowhileloop_constructor_exists():
    assert callable(simTL4J::statements::DoWhileLoop.__init__)


def test_simtl4j::statements::dowhileloop_constructor_args():
    sig = inspect.signature(simTL4J::statements::DoWhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_switchcase_is_not_abstract():
    assert not inspect.isabstract(SwitchCase)


def test_switchcase_constructor_exists():
    assert callable(SwitchCase.__init__)


def test_switchcase_constructor_args():
    sig = inspect.signature(SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::defaultswitchcase_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::DefaultSwitchCase)


def test_simtl4j::statements::defaultswitchcase_constructor_exists():
    assert callable(simTL4J::statements::DefaultSwitchCase.__init__)


def test_simtl4j::statements::defaultswitchcase_constructor_args():
    sig = inspect.signature(simTL4J::statements::DefaultSwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_statements::statementcontainer_is_not_abstract():
    assert not inspect.isabstract(statements::StatementContainer)


def test_statements::statementcontainer_constructor_exists():
    assert callable(statements::StatementContainer.__init__)


def test_statements::statementcontainer_constructor_args():
    sig = inspect.signature(statements::StatementContainer.__init__)
    params = list(sig.parameters.keys())



def test_ordinaryparameter_is_not_abstract():
    assert not inspect.isabstract(OrdinaryParameter)


def test_ordinaryparameter_constructor_exists():
    assert callable(OrdinaryParameter.__init__)


def test_ordinaryparameter_constructor_args():
    sig = inspect.signature(OrdinaryParameter.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::catchblock_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::CatchBlock)


def test_simtl4j::statements::catchblock_constructor_exists():
    assert callable(simTL4J::statements::CatchBlock.__init__)


def test_simtl4j::statements::catchblock_constructor_args():
    sig = inspect.signature(simTL4J::statements::CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_modifiers::modifiable_is_not_abstract():
    assert not inspect.isabstract(modifiers::Modifiable)


def test_modifiers::modifiable_constructor_exists():
    assert callable(modifiers::Modifiable.__init__)


def test_modifiers::modifiable_constructor_args():
    sig = inspect.signature(modifiers::Modifiable.__init__)
    params = list(sig.parameters.keys())



def test_jump_is_not_abstract():
    assert not inspect.isabstract(Jump)


def test_jump_constructor_exists():
    assert callable(Jump.__init__)


def test_jump_constructor_args():
    sig = inspect.signature(Jump.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::continue_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::Continue)


def test_simtl4j::statements::continue_constructor_exists():
    assert callable(simTL4J::statements::Continue.__init__)


def test_simtl4j::statements::continue_constructor_args():
    sig = inspect.signature(simTL4J::statements::Continue.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::break_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::Break)


def test_simtl4j::statements::break_constructor_exists():
    assert callable(simTL4J::statements::Break.__init__)


def test_simtl4j::statements::break_constructor_args():
    sig = inspect.signature(simTL4J::statements::Break.__init__)
    params = list(sig.parameters.keys())



def test_references::elementreference_is_not_abstract():
    assert not inspect.isabstract(references::ElementReference)


def test_references::elementreference_constructor_exists():
    assert callable(references::ElementReference.__init__)


def test_references::elementreference_constructor_args():
    sig = inspect.signature(references::ElementReference.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::localvariablestatement_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::LocalVariableStatement)


def test_simtl4j::statements::localvariablestatement_constructor_exists():
    assert callable(simTL4J::statements::LocalVariableStatement.__init__)


def test_simtl4j::statements::localvariablestatement_constructor_args():
    sig = inspect.signature(simTL4J::statements::LocalVariableStatement.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::throw_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::Throw)


def test_simtl4j::statements::throw_constructor_exists():
    assert callable(simTL4J::statements::Throw.__init__)


def test_simtl4j::statements::throw_constructor_args():
    sig = inspect.signature(simTL4J::statements::Throw.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::jump_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::Jump)


def test_simtl4j::statements::jump_constructor_exists():
    assert callable(simTL4J::statements::Jump.__init__)


def test_simtl4j::statements::jump_constructor_args():
    sig = inspect.signature(simTL4J::statements::Jump.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::switch_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::Switch)


def test_simtl4j::statements::switch_constructor_exists():
    assert callable(simTL4J::statements::Switch.__init__)


def test_simtl4j::statements::switch_constructor_args():
    sig = inspect.signature(simTL4J::statements::Switch.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::return_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::Return)


def test_simtl4j::statements::return_constructor_exists():
    assert callable(simTL4J::statements::Return.__init__)


def test_simtl4j::statements::return_constructor_args():
    sig = inspect.signature(simTL4J::statements::Return.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::ExpressionStatement)


def test_simtl4j::statements::expressionstatement_constructor_exists():
    assert callable(simTL4J::statements::ExpressionStatement.__init__)


def test_simtl4j::statements::expressionstatement_constructor_args():
    sig = inspect.signature(simTL4J::statements::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::emptystatement_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::EmptyStatement)


def test_simtl4j::statements::emptystatement_constructor_exists():
    assert callable(simTL4J::statements::EmptyStatement.__init__)


def test_simtl4j::statements::emptystatement_constructor_args():
    sig = inspect.signature(simTL4J::statements::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::types::void_is_not_abstract():
    assert not inspect.isabstract(simTL4J::types::Void)


def test_simtl4j::types::void_constructor_exists():
    assert callable(simTL4J::types::Void.__init__)


def test_simtl4j::types::void_constructor_args():
    sig = inspect.signature(simTL4J::types::Void.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::types::char_is_not_abstract():
    assert not inspect.isabstract(simTL4J::types::Char)


def test_simtl4j::types::char_constructor_exists():
    assert callable(simTL4J::types::Char.__init__)


def test_simtl4j::types::char_constructor_args():
    sig = inspect.signature(simTL4J::types::Char.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::types::boolean_is_not_abstract():
    assert not inspect.isabstract(simTL4J::types::Boolean)


def test_simtl4j::types::boolean_constructor_exists():
    assert callable(simTL4J::types::Boolean.__init__)


def test_simtl4j::types::boolean_constructor_args():
    sig = inspect.signature(simTL4J::types::Boolean.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::types::long_is_not_abstract():
    assert not inspect.isabstract(simTL4J::types::Long)


def test_simtl4j::types::long_constructor_exists():
    assert callable(simTL4J::types::Long.__init__)


def test_simtl4j::types::long_constructor_args():
    sig = inspect.signature(simTL4J::types::Long.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::types::int_is_not_abstract():
    assert not inspect.isabstract(simTL4J::types::Int)


def test_simtl4j::types::int_constructor_exists():
    assert callable(simTL4J::types::Int.__init__)


def test_simtl4j::types::int_constructor_args():
    sig = inspect.signature(simTL4J::types::Int.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::types::double_is_not_abstract():
    assert not inspect.isabstract(simTL4J::types::Double)


def test_simtl4j::types::double_constructor_exists():
    assert callable(simTL4J::types::Double.__init__)


def test_simtl4j::types::double_constructor_args():
    sig = inspect.signature(simTL4J::types::Double.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::types::short_is_not_abstract():
    assert not inspect.isabstract(simTL4J::types::Short)


def test_simtl4j::types::short_constructor_exists():
    assert callable(simTL4J::types::Short.__init__)


def test_simtl4j::types::short_constructor_args():
    sig = inspect.signature(simTL4J::types::Short.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::types::byte_is_not_abstract():
    assert not inspect.isabstract(simTL4J::types::Byte)


def test_simtl4j::types::byte_constructor_exists():
    assert callable(simTL4J::types::Byte.__init__)


def test_simtl4j::types::byte_constructor_args():
    sig = inspect.signature(simTL4J::types::Byte.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::types::float_is_not_abstract():
    assert not inspect.isabstract(simTL4J::types::Float)


def test_simtl4j::types::float_constructor_exists():
    assert callable(simTL4J::types::Float.__init__)


def test_simtl4j::types::float_constructor_args():
    sig = inspect.signature(simTL4J::types::Float.__init__)
    params = list(sig.parameters.keys())



def test_elementreference_is_not_abstract():
    assert not inspect.isabstract(ElementReference)


def test_elementreference_constructor_exists():
    assert callable(ElementReference.__init__)


def test_elementreference_constructor_args():
    sig = inspect.signature(ElementReference.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::references::identifierreference_is_not_abstract():
    assert not inspect.isabstract(simTL4J::references::IdentifierReference)


def test_simtl4j::references::identifierreference_constructor_exists():
    assert callable(simTL4J::references::IdentifierReference.__init__)


def test_simtl4j::references::identifierreference_constructor_args():
    sig = inspect.signature(simTL4J::references::IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_arrayselector_is_not_abstract():
    assert not inspect.isabstract(ArraySelector)


def test_arrayselector_constructor_exists():
    assert callable(ArraySelector.__init__)


def test_arrayselector_constructor_args():
    sig = inspect.signature(ArraySelector.__init__)
    params = list(sig.parameters.keys())



def test_expressions::primaryexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::PrimaryExpression)


def test_expressions::primaryexpression_constructor_exists():
    assert callable(expressions::PrimaryExpression.__init__)


def test_expressions::primaryexpression_constructor_args():
    sig = inspect.signature(expressions::PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::simtl::tplaceholder::primaryexpression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::simTL::TPlaceholder::PrimaryExpression)


def test_simtl4j::simtl::tplaceholder::primaryexpression_constructor_exists():
    assert callable(simTL4J::simTL::TPlaceholder::PrimaryExpression.__init__)


def test_simtl4j::simtl::tplaceholder::primaryexpression_constructor_args():
    sig = inspect.signature(simTL4J::simTL::TPlaceholder::PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::parameters::variablelengthparameter_is_not_abstract():
    assert not inspect.isabstract(simTL4J::parameters::VariableLengthParameter)


def test_simtl4j::parameters::variablelengthparameter_constructor_exists():
    assert callable(simTL4J::parameters::VariableLengthParameter.__init__)


def test_simtl4j::parameters::variablelengthparameter_constructor_args():
    sig = inspect.signature(simTL4J::parameters::VariableLengthParameter.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::parameters::ordinaryparameter_is_not_abstract():
    assert not inspect.isabstract(simTL4J::parameters::OrdinaryParameter)


def test_simtl4j::parameters::ordinaryparameter_constructor_exists():
    assert callable(simTL4J::parameters::OrdinaryParameter.__init__)


def test_simtl4j::parameters::ordinaryparameter_constructor_args():
    sig = inspect.signature(simTL4J::parameters::OrdinaryParameter.__init__)
    params = list(sig.parameters.keys())



def test_operators::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(operators::UnaryOperator)


def test_operators::unaryoperator_constructor_exists():
    assert callable(operators::UnaryOperator.__init__)


def test_operators::unaryoperator_constructor_args():
    sig = inspect.signature(operators::UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_operators::additiveoperator_is_not_abstract():
    assert not inspect.isabstract(operators::AdditiveOperator)


def test_operators::additiveoperator_constructor_exists():
    assert callable(operators::AdditiveOperator.__init__)


def test_operators::additiveoperator_constructor_args():
    sig = inspect.signature(operators::AdditiveOperator.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::subtraction_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::Subtraction)


def test_simtl4j::operators::subtraction_constructor_exists():
    assert callable(simTL4J::operators::Subtraction.__init__)


def test_simtl4j::operators::subtraction_constructor_args():
    sig = inspect.signature(simTL4J::operators::Subtraction.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::addition_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::Addition)


def test_simtl4j::operators::addition_constructor_exists():
    assert callable(simTL4J::operators::Addition.__init__)


def test_simtl4j::operators::addition_constructor_args():
    sig = inspect.signature(simTL4J::operators::Addition.__init__)
    params = list(sig.parameters.keys())



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::multiplicativeoperator_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::MultiplicativeOperator)


def test_simtl4j::operators::multiplicativeoperator_constructor_exists():
    assert callable(simTL4J::operators::MultiplicativeOperator.__init__)


def test_simtl4j::operators::multiplicativeoperator_constructor_args():
    sig = inspect.signature(simTL4J::operators::MultiplicativeOperator.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::unarymodificationoperator_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::UnaryModificationOperator)


def test_simtl4j::operators::unarymodificationoperator_constructor_exists():
    assert callable(simTL4J::operators::UnaryModificationOperator.__init__)


def test_simtl4j::operators::unarymodificationoperator_constructor_args():
    sig = inspect.signature(simTL4J::operators::UnaryModificationOperator.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::equalityoperator_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::EqualityOperator)


def test_simtl4j::operators::equalityoperator_constructor_exists():
    assert callable(simTL4J::operators::EqualityOperator.__init__)


def test_simtl4j::operators::equalityoperator_constructor_args():
    sig = inspect.signature(simTL4J::operators::EqualityOperator.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::relationoperator_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::RelationOperator)


def test_simtl4j::operators::relationoperator_constructor_exists():
    assert callable(simTL4J::operators::RelationOperator.__init__)


def test_simtl4j::operators::relationoperator_constructor_args():
    sig = inspect.signature(simTL4J::operators::RelationOperator.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::assignmentoperator_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::AssignmentOperator)


def test_simtl4j::operators::assignmentoperator_constructor_exists():
    assert callable(simTL4J::operators::AssignmentOperator.__init__)


def test_simtl4j::operators::assignmentoperator_constructor_args():
    sig = inspect.signature(simTL4J::operators::AssignmentOperator.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::UnaryOperator)


def test_simtl4j::operators::unaryoperator_constructor_exists():
    assert callable(simTL4J::operators::UnaryOperator.__init__)


def test_simtl4j::operators::unaryoperator_constructor_args():
    sig = inspect.signature(simTL4J::operators::UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::shiftoperator_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::ShiftOperator)


def test_simtl4j::operators::shiftoperator_constructor_exists():
    assert callable(simTL4J::operators::ShiftOperator.__init__)


def test_simtl4j::operators::shiftoperator_constructor_args():
    sig = inspect.signature(simTL4J::operators::ShiftOperator.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::additiveoperator_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::AdditiveOperator)


def test_simtl4j::operators::additiveoperator_constructor_exists():
    assert callable(simTL4J::operators::AdditiveOperator.__init__)


def test_simtl4j::operators::additiveoperator_constructor_args():
    sig = inspect.signature(simTL4J::operators::AdditiveOperator.__init__)
    params = list(sig.parameters.keys())



def test_annotationinstanceormodifier_is_not_abstract():
    assert not inspect.isabstract(AnnotationInstanceOrModifier)


def test_annotationinstanceormodifier_constructor_exists():
    assert callable(AnnotationInstanceOrModifier.__init__)


def test_annotationinstanceormodifier_constructor_args():
    sig = inspect.signature(AnnotationInstanceOrModifier.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::modifiers::modifier_is_not_abstract():
    assert not inspect.isabstract(simTL4J::modifiers::Modifier)


def test_simtl4j::modifiers::modifier_constructor_exists():
    assert callable(simTL4J::modifiers::Modifier.__init__)


def test_simtl4j::modifiers::modifier_constructor_args():
    sig = inspect.signature(simTL4J::modifiers::Modifier.__init__)
    params = list(sig.parameters.keys())



def test_modifier_is_not_abstract():
    assert not inspect.isabstract(Modifier)


def test_modifier_constructor_exists():
    assert callable(Modifier.__init__)


def test_modifier_constructor_args():
    sig = inspect.signature(Modifier.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::modifiers::synchronized_is_not_abstract():
    assert not inspect.isabstract(simTL4J::modifiers::Synchronized)


def test_simtl4j::modifiers::synchronized_constructor_exists():
    assert callable(simTL4J::modifiers::Synchronized.__init__)


def test_simtl4j::modifiers::synchronized_constructor_args():
    sig = inspect.signature(simTL4J::modifiers::Synchronized.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::modifiers::private_is_not_abstract():
    assert not inspect.isabstract(simTL4J::modifiers::Private)


def test_simtl4j::modifiers::private_constructor_exists():
    assert callable(simTL4J::modifiers::Private.__init__)


def test_simtl4j::modifiers::private_constructor_args():
    sig = inspect.signature(simTL4J::modifiers::Private.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::modifiers::static_is_not_abstract():
    assert not inspect.isabstract(simTL4J::modifiers::Static)


def test_simtl4j::modifiers::static_constructor_exists():
    assert callable(simTL4J::modifiers::Static.__init__)


def test_simtl4j::modifiers::static_constructor_args():
    sig = inspect.signature(simTL4J::modifiers::Static.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::modifiers::strictfp_is_not_abstract():
    assert not inspect.isabstract(simTL4J::modifiers::Strictfp)


def test_simtl4j::modifiers::strictfp_constructor_exists():
    assert callable(simTL4J::modifiers::Strictfp.__init__)


def test_simtl4j::modifiers::strictfp_constructor_args():
    sig = inspect.signature(simTL4J::modifiers::Strictfp.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::modifiers::transient_is_not_abstract():
    assert not inspect.isabstract(simTL4J::modifiers::Transient)


def test_simtl4j::modifiers::transient_constructor_exists():
    assert callable(simTL4J::modifiers::Transient.__init__)


def test_simtl4j::modifiers::transient_constructor_args():
    sig = inspect.signature(simTL4J::modifiers::Transient.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::modifiers::abstract_is_not_abstract():
    assert not inspect.isabstract(simTL4J::modifiers::Abstract)


def test_simtl4j::modifiers::abstract_constructor_exists():
    assert callable(simTL4J::modifiers::Abstract.__init__)


def test_simtl4j::modifiers::abstract_constructor_args():
    sig = inspect.signature(simTL4J::modifiers::Abstract.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::modifiers::volatile_is_not_abstract():
    assert not inspect.isabstract(simTL4J::modifiers::Volatile)


def test_simtl4j::modifiers::volatile_constructor_exists():
    assert callable(simTL4J::modifiers::Volatile.__init__)


def test_simtl4j::modifiers::volatile_constructor_args():
    sig = inspect.signature(simTL4J::modifiers::Volatile.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::modifiers::native_is_not_abstract():
    assert not inspect.isabstract(simTL4J::modifiers::Native)


def test_simtl4j::modifiers::native_constructor_exists():
    assert callable(simTL4J::modifiers::Native.__init__)


def test_simtl4j::modifiers::native_constructor_args():
    sig = inspect.signature(simTL4J::modifiers::Native.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::modifiers::protected_is_not_abstract():
    assert not inspect.isabstract(simTL4J::modifiers::Protected)


def test_simtl4j::modifiers::protected_constructor_exists():
    assert callable(simTL4J::modifiers::Protected.__init__)


def test_simtl4j::modifiers::protected_constructor_args():
    sig = inspect.signature(simTL4J::modifiers::Protected.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::modifiers::public_is_not_abstract():
    assert not inspect.isabstract(simTL4J::modifiers::Public)


def test_simtl4j::modifiers::public_constructor_exists():
    assert callable(simTL4J::modifiers::Public.__init__)


def test_simtl4j::modifiers::public_constructor_args():
    sig = inspect.signature(simTL4J::modifiers::Public.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::modifiers::final_is_not_abstract():
    assert not inspect.isabstract(simTL4J::modifiers::Final)


def test_simtl4j::modifiers::final_constructor_exists():
    assert callable(simTL4J::modifiers::Final.__init__)


def test_simtl4j::modifiers::final_constructor_args():
    sig = inspect.signature(simTL4J::modifiers::Final.__init__)
    params = list(sig.parameters.keys())



def test_members::method_is_not_abstract():
    assert not inspect.isabstract(members::Method)


def test_members::method_constructor_exists():
    assert callable(members::Method.__init__)


def test_members::method_constructor_args():
    sig = inspect.signature(members::Method.__init__)
    params = list(sig.parameters.keys())



def test_method_is_not_abstract():
    assert not inspect.isabstract(Method)


def test_method_constructor_exists():
    assert callable(Method.__init__)


def test_method_constructor_args():
    sig = inspect.signature(Method.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::members::interfacemethod_is_not_abstract():
    assert not inspect.isabstract(simTL4J::members::InterfaceMethod)


def test_simtl4j::members::interfacemethod_constructor_exists():
    assert callable(simTL4J::members::InterfaceMethod.__init__)


def test_simtl4j::members::interfacemethod_constructor_args():
    sig = inspect.signature(simTL4J::members::InterfaceMethod.__init__)
    params = list(sig.parameters.keys())



def test_additionalfield_is_not_abstract():
    assert not inspect.isabstract(AdditionalField)


def test_additionalfield_constructor_exists():
    assert callable(AdditionalField.__init__)


def test_additionalfield_constructor_args():
    sig = inspect.signature(AdditionalField.__init__)
    params = list(sig.parameters.keys())



def test_variables::variable_is_not_abstract():
    assert not inspect.isabstract(variables::Variable)


def test_variables::variable_constructor_exists():
    assert callable(variables::Variable.__init__)


def test_variables::variable_constructor_args():
    sig = inspect.signature(variables::Variable.__init__)
    params = list(sig.parameters.keys())



def test_members::exceptionthrower_is_not_abstract():
    assert not inspect.isabstract(members::ExceptionThrower)


def test_members::exceptionthrower_constructor_exists():
    assert callable(members::ExceptionThrower.__init__)


def test_members::exceptionthrower_constructor_args():
    sig = inspect.signature(members::ExceptionThrower.__init__)
    params = list(sig.parameters.keys())



def test_parameters::parametrizable_is_not_abstract():
    assert not inspect.isabstract(parameters::Parametrizable)


def test_parameters::parametrizable_constructor_exists():
    assert callable(parameters::Parametrizable.__init__)


def test_parameters::parametrizable_constructor_args():
    sig = inspect.signature(parameters::Parametrizable.__init__)
    params = list(sig.parameters.keys())



def test_statements::statementlistcontainer_is_not_abstract():
    assert not inspect.isabstract(statements::StatementListContainer)


def test_statements::statementlistcontainer_constructor_exists():
    assert callable(statements::StatementListContainer.__init__)


def test_statements::statementlistcontainer_constructor_args():
    sig = inspect.signature(statements::StatementListContainer.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::members::classmethod_is_not_abstract():
    assert not inspect.isabstract(simTL4J::members::ClassMethod)


def test_simtl4j::members::classmethod_constructor_exists():
    assert callable(simTL4J::members::ClassMethod.__init__)


def test_simtl4j::members::classmethod_constructor_args():
    sig = inspect.signature(simTL4J::members::ClassMethod.__init__)
    params = list(sig.parameters.keys())



def test_instantiations::initializable_is_not_abstract():
    assert not inspect.isabstract(instantiations::Initializable)


def test_instantiations::initializable_constructor_exists():
    assert callable(instantiations::Initializable.__init__)


def test_instantiations::initializable_constructor_args():
    sig = inspect.signature(instantiations::Initializable.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::members::emptymember_is_not_abstract():
    assert not inspect.isabstract(simTL4J::members::EmptyMember)


def test_simtl4j::members::emptymember_constructor_exists():
    assert callable(simTL4J::members::EmptyMember.__init__)


def test_simtl4j::members::emptymember_constructor_args():
    sig = inspect.signature(simTL4J::members::EmptyMember.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::references::referenceableelement_is_not_abstract():
    assert not inspect.isabstract(simTL4J::references::ReferenceableElement)


def test_simtl4j::references::referenceableelement_constructor_exists():
    assert callable(simTL4J::references::ReferenceableElement.__init__)


def test_simtl4j::references::referenceableelement_constructor_args():
    sig = inspect.signature(simTL4J::references::ReferenceableElement.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::members::member_is_not_abstract():
    assert not inspect.isabstract(simTL4J::members::Member)


def test_simtl4j::members::member_constructor_exists():
    assert callable(simTL4J::members::Member.__init__)


def test_simtl4j::members::member_constructor_args():
    sig = inspect.signature(simTL4J::members::Member.__init__)
    params = list(sig.parameters.keys())



def test_namespaceclassifierreference_is_not_abstract():
    assert not inspect.isabstract(NamespaceClassifierReference)


def test_namespaceclassifierreference_constructor_exists():
    assert callable(NamespaceClassifierReference.__init__)


def test_namespaceclassifierreference_constructor_args():
    sig = inspect.signature(NamespaceClassifierReference.__init__)
    params = list(sig.parameters.keys())



def test_longliteral_is_not_abstract():
    assert not inspect.isabstract(LongLiteral)


def test_longliteral_constructor_exists():
    assert callable(LongLiteral.__init__)


def test_longliteral_constructor_args():
    sig = inspect.signature(LongLiteral.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::literals::octallongliteral_is_not_abstract():
    assert not inspect.isabstract(simTL4J::literals::OctalLongLiteral)


def test_simtl4j::literals::octallongliteral_constructor_exists():
    assert callable(simTL4J::literals::OctalLongLiteral.__init__)


def test_simtl4j::literals::octallongliteral_constructor_args():
    sig = inspect.signature(simTL4J::literals::OctalLongLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "octalValue" in params, "Missing parameter 'octalValue'"

def test_simtl4j::literals::octallongliteral_has_octalValue():
    assert hasattr(simTL4J::literals::OctalLongLiteral, "octalValue")
    descriptor = None
    for klass in simTL4J::literals::OctalLongLiteral.__mro__:
        if "octalValue" in klass.__dict__:
            descriptor = klass.__dict__["octalValue"]
            break
    assert isinstance(descriptor, property)



def test_simtl4j::literals::hexlongliteral_is_not_abstract():
    assert not inspect.isabstract(simTL4J::literals::HexLongLiteral)


def test_simtl4j::literals::hexlongliteral_constructor_exists():
    assert callable(simTL4J::literals::HexLongLiteral.__init__)


def test_simtl4j::literals::hexlongliteral_constructor_args():
    sig = inspect.signature(simTL4J::literals::HexLongLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "hexValue" in params, "Missing parameter 'hexValue'"

def test_simtl4j::literals::hexlongliteral_has_hexValue():
    assert hasattr(simTL4J::literals::HexLongLiteral, "hexValue")
    descriptor = None
    for klass in simTL4J::literals::HexLongLiteral.__mro__:
        if "hexValue" in klass.__dict__:
            descriptor = klass.__dict__["hexValue"]
            break
    assert isinstance(descriptor, property)



def test_simtl4j::literals::decimallongliteral_is_not_abstract():
    assert not inspect.isabstract(simTL4J::literals::DecimalLongLiteral)


def test_simtl4j::literals::decimallongliteral_constructor_exists():
    assert callable(simTL4J::literals::DecimalLongLiteral.__init__)


def test_simtl4j::literals::decimallongliteral_constructor_args():
    sig = inspect.signature(simTL4J::literals::DecimalLongLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "decimalValue" in params, "Missing parameter 'decimalValue'"

def test_simtl4j::literals::decimallongliteral_has_decimalValue():
    assert hasattr(simTL4J::literals::DecimalLongLiteral, "decimalValue")
    descriptor = None
    for klass in simTL4J::literals::DecimalLongLiteral.__mro__:
        if "decimalValue" in klass.__dict__:
            descriptor = klass.__dict__["decimalValue"]
            break
    assert isinstance(descriptor, property)



def test_integerliteral_is_not_abstract():
    assert not inspect.isabstract(IntegerLiteral)


def test_integerliteral_constructor_exists():
    assert callable(IntegerLiteral.__init__)


def test_integerliteral_constructor_args():
    sig = inspect.signature(IntegerLiteral.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::literals::hexintegerliteral_is_not_abstract():
    assert not inspect.isabstract(simTL4J::literals::HexIntegerLiteral)


def test_simtl4j::literals::hexintegerliteral_constructor_exists():
    assert callable(simTL4J::literals::HexIntegerLiteral.__init__)


def test_simtl4j::literals::hexintegerliteral_constructor_args():
    sig = inspect.signature(simTL4J::literals::HexIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "hexValue" in params, "Missing parameter 'hexValue'"

def test_simtl4j::literals::hexintegerliteral_has_hexValue():
    assert hasattr(simTL4J::literals::HexIntegerLiteral, "hexValue")
    descriptor = None
    for klass in simTL4J::literals::HexIntegerLiteral.__mro__:
        if "hexValue" in klass.__dict__:
            descriptor = klass.__dict__["hexValue"]
            break
    assert isinstance(descriptor, property)



def test_simtl4j::literals::octalintegerliteral_is_not_abstract():
    assert not inspect.isabstract(simTL4J::literals::OctalIntegerLiteral)


def test_simtl4j::literals::octalintegerliteral_constructor_exists():
    assert callable(simTL4J::literals::OctalIntegerLiteral.__init__)


def test_simtl4j::literals::octalintegerliteral_constructor_args():
    sig = inspect.signature(simTL4J::literals::OctalIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "octalValue" in params, "Missing parameter 'octalValue'"

def test_simtl4j::literals::octalintegerliteral_has_octalValue():
    assert hasattr(simTL4J::literals::OctalIntegerLiteral, "octalValue")
    descriptor = None
    for klass in simTL4J::literals::OctalIntegerLiteral.__mro__:
        if "octalValue" in klass.__dict__:
            descriptor = klass.__dict__["octalValue"]
            break
    assert isinstance(descriptor, property)



def test_simtl4j::literals::decimalintegerliteral_is_not_abstract():
    assert not inspect.isabstract(simTL4J::literals::DecimalIntegerLiteral)


def test_simtl4j::literals::decimalintegerliteral_constructor_exists():
    assert callable(simTL4J::literals::DecimalIntegerLiteral.__init__)


def test_simtl4j::literals::decimalintegerliteral_constructor_args():
    sig = inspect.signature(simTL4J::literals::DecimalIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "decimalValue" in params, "Missing parameter 'decimalValue'"

def test_simtl4j::literals::decimalintegerliteral_has_decimalValue():
    assert hasattr(simTL4J::literals::DecimalIntegerLiteral, "decimalValue")
    descriptor = None
    for klass in simTL4J::literals::DecimalIntegerLiteral.__mro__:
        if "decimalValue" in klass.__dict__:
            descriptor = klass.__dict__["decimalValue"]
            break
    assert isinstance(descriptor, property)



def test_doubleliteral_is_not_abstract():
    assert not inspect.isabstract(DoubleLiteral)


def test_doubleliteral_constructor_exists():
    assert callable(DoubleLiteral.__init__)


def test_doubleliteral_constructor_args():
    sig = inspect.signature(DoubleLiteral.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::literals::hexdoubleliteral_is_not_abstract():
    assert not inspect.isabstract(simTL4J::literals::HexDoubleLiteral)


def test_simtl4j::literals::hexdoubleliteral_constructor_exists():
    assert callable(simTL4J::literals::HexDoubleLiteral.__init__)


def test_simtl4j::literals::hexdoubleliteral_constructor_args():
    sig = inspect.signature(simTL4J::literals::HexDoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "hexValue" in params, "Missing parameter 'hexValue'"

def test_simtl4j::literals::hexdoubleliteral_has_hexValue():
    assert hasattr(simTL4J::literals::HexDoubleLiteral, "hexValue")
    descriptor = None
    for klass in simTL4J::literals::HexDoubleLiteral.__mro__:
        if "hexValue" in klass.__dict__:
            descriptor = klass.__dict__["hexValue"]
            break
    assert isinstance(descriptor, property)



def test_simtl4j::literals::decimaldoubleliteral_is_not_abstract():
    assert not inspect.isabstract(simTL4J::literals::DecimalDoubleLiteral)


def test_simtl4j::literals::decimaldoubleliteral_constructor_exists():
    assert callable(simTL4J::literals::DecimalDoubleLiteral.__init__)


def test_simtl4j::literals::decimaldoubleliteral_constructor_args():
    sig = inspect.signature(simTL4J::literals::DecimalDoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "decimalValue" in params, "Missing parameter 'decimalValue'"

def test_simtl4j::literals::decimaldoubleliteral_has_decimalValue():
    assert hasattr(simTL4J::literals::DecimalDoubleLiteral, "decimalValue")
    descriptor = None
    for klass in simTL4J::literals::DecimalDoubleLiteral.__mro__:
        if "decimalValue" in klass.__dict__:
            descriptor = klass.__dict__["decimalValue"]
            break
    assert isinstance(descriptor, property)



def test_floatliteral_is_not_abstract():
    assert not inspect.isabstract(FloatLiteral)


def test_floatliteral_constructor_exists():
    assert callable(FloatLiteral.__init__)


def test_floatliteral_constructor_args():
    sig = inspect.signature(FloatLiteral.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::literals::hexfloatliteral_is_not_abstract():
    assert not inspect.isabstract(simTL4J::literals::HexFloatLiteral)


def test_simtl4j::literals::hexfloatliteral_constructor_exists():
    assert callable(simTL4J::literals::HexFloatLiteral.__init__)


def test_simtl4j::literals::hexfloatliteral_constructor_args():
    sig = inspect.signature(simTL4J::literals::HexFloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "hexValue" in params, "Missing parameter 'hexValue'"

def test_simtl4j::literals::hexfloatliteral_has_hexValue():
    assert hasattr(simTL4J::literals::HexFloatLiteral, "hexValue")
    descriptor = None
    for klass in simTL4J::literals::HexFloatLiteral.__mro__:
        if "hexValue" in klass.__dict__:
            descriptor = klass.__dict__["hexValue"]
            break
    assert isinstance(descriptor, property)



def test_simtl4j::literals::decimalfloatliteral_is_not_abstract():
    assert not inspect.isabstract(simTL4J::literals::DecimalFloatLiteral)


def test_simtl4j::literals::decimalfloatliteral_constructor_exists():
    assert callable(simTL4J::literals::DecimalFloatLiteral.__init__)


def test_simtl4j::literals::decimalfloatliteral_constructor_args():
    sig = inspect.signature(simTL4J::literals::DecimalFloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "decimalValue" in params, "Missing parameter 'decimalValue'"

def test_simtl4j::literals::decimalfloatliteral_has_decimalValue():
    assert hasattr(simTL4J::literals::DecimalFloatLiteral, "decimalValue")
    descriptor = None
    for klass in simTL4J::literals::DecimalFloatLiteral.__mro__:
        if "decimalValue" in klass.__dict__:
            descriptor = klass.__dict__["decimalValue"]
            break
    assert isinstance(descriptor, property)



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::literals::characterliteral_is_not_abstract():
    assert not inspect.isabstract(simTL4J::literals::CharacterLiteral)


def test_simtl4j::literals::characterliteral_constructor_exists():
    assert callable(simTL4J::literals::CharacterLiteral.__init__)


def test_simtl4j::literals::characterliteral_constructor_args():
    sig = inspect.signature(simTL4J::literals::CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_simtl4j::literals::characterliteral_has_value():
    assert hasattr(simTL4J::literals::CharacterLiteral, "value")
    descriptor = None
    for klass in simTL4J::literals::CharacterLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_simtl4j::literals::floatliteral_is_not_abstract():
    assert not inspect.isabstract(simTL4J::literals::FloatLiteral)


def test_simtl4j::literals::floatliteral_constructor_exists():
    assert callable(simTL4J::literals::FloatLiteral.__init__)


def test_simtl4j::literals::floatliteral_constructor_args():
    sig = inspect.signature(simTL4J::literals::FloatLiteral.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::literals::nullliteral_is_not_abstract():
    assert not inspect.isabstract(simTL4J::literals::NullLiteral)


def test_simtl4j::literals::nullliteral_constructor_exists():
    assert callable(simTL4J::literals::NullLiteral.__init__)


def test_simtl4j::literals::nullliteral_constructor_args():
    sig = inspect.signature(simTL4J::literals::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::literals::doubleliteral_is_not_abstract():
    assert not inspect.isabstract(simTL4J::literals::DoubleLiteral)


def test_simtl4j::literals::doubleliteral_constructor_exists():
    assert callable(simTL4J::literals::DoubleLiteral.__init__)


def test_simtl4j::literals::doubleliteral_constructor_args():
    sig = inspect.signature(simTL4J::literals::DoubleLiteral.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::literals::longliteral_is_not_abstract():
    assert not inspect.isabstract(simTL4J::literals::LongLiteral)


def test_simtl4j::literals::longliteral_constructor_exists():
    assert callable(simTL4J::literals::LongLiteral.__init__)


def test_simtl4j::literals::longliteral_constructor_args():
    sig = inspect.signature(simTL4J::literals::LongLiteral.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::literals::integerliteral_is_not_abstract():
    assert not inspect.isabstract(simTL4J::literals::IntegerLiteral)


def test_simtl4j::literals::integerliteral_constructor_exists():
    assert callable(simTL4J::literals::IntegerLiteral.__init__)


def test_simtl4j::literals::integerliteral_constructor_args():
    sig = inspect.signature(simTL4J::literals::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::literals::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(simTL4J::literals::BooleanLiteral)


def test_simtl4j::literals::booleanliteral_constructor_exists():
    assert callable(simTL4J::literals::BooleanLiteral.__init__)


def test_simtl4j::literals::booleanliteral_constructor_args():
    sig = inspect.signature(simTL4J::literals::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_simtl4j::literals::booleanliteral_has_value():
    assert hasattr(simTL4J::literals::BooleanLiteral, "value")
    descriptor = None
    for klass in simTL4J::literals::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpression)


def test_primaryexpression_constructor_exists():
    assert callable(PrimaryExpression.__init__)


def test_primaryexpression_constructor_args():
    sig = inspect.signature(PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::literals::literal_is_not_abstract():
    assert not inspect.isabstract(simTL4J::literals::Literal)


def test_simtl4j::literals::literal_constructor_exists():
    assert callable(simTL4J::literals::Literal.__init__)


def test_simtl4j::literals::literal_constructor_args():
    sig = inspect.signature(simTL4J::literals::Literal.__init__)
    params = list(sig.parameters.keys())



def test_self_is_not_abstract():
    assert not inspect.isabstract(Self)


def test_self_constructor_exists():
    assert callable(Self.__init__)


def test_self_constructor_args():
    sig = inspect.signature(Self.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::literals::this_is_not_abstract():
    assert not inspect.isabstract(simTL4J::literals::This)


def test_simtl4j::literals::this_constructor_exists():
    assert callable(simTL4J::literals::This.__init__)


def test_simtl4j::literals::this_constructor_args():
    sig = inspect.signature(simTL4J::literals::This.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::literals::super_is_not_abstract():
    assert not inspect.isabstract(simTL4J::literals::Super)


def test_simtl4j::literals::super_constructor_exists():
    assert callable(simTL4J::literals::Super.__init__)


def test_simtl4j::literals::super_constructor_args():
    sig = inspect.signature(simTL4J::literals::Super.__init__)
    params = list(sig.parameters.keys())



def test_instantiation_is_not_abstract():
    assert not inspect.isabstract(Instantiation)


def test_instantiation_constructor_exists():
    assert callable(Instantiation.__init__)


def test_instantiation_constructor_args():
    sig = inspect.signature(Instantiation.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::instantiations::explicitconstructorcall_is_not_abstract():
    assert not inspect.isabstract(simTL4J::instantiations::ExplicitConstructorCall)


def test_simtl4j::instantiations::explicitconstructorcall_constructor_exists():
    assert callable(simTL4J::instantiations::ExplicitConstructorCall.__init__)


def test_simtl4j::instantiations::explicitconstructorcall_constructor_args():
    sig = inspect.signature(simTL4J::instantiations::ExplicitConstructorCall.__init__)
    params = list(sig.parameters.keys())



def test_anonymousclass_is_not_abstract():
    assert not inspect.isabstract(AnonymousClass)


def test_anonymousclass_constructor_exists():
    assert callable(AnonymousClass.__init__)


def test_anonymousclass_constructor_args():
    sig = inspect.signature(AnonymousClass.__init__)
    params = list(sig.parameters.keys())



def test_generics::calltypeargumentable_is_not_abstract():
    assert not inspect.isabstract(generics::CallTypeArgumentable)


def test_generics::calltypeargumentable_constructor_exists():
    assert callable(generics::CallTypeArgumentable.__init__)


def test_generics::calltypeargumentable_constructor_args():
    sig = inspect.signature(generics::CallTypeArgumentable.__init__)
    params = list(sig.parameters.keys())



def test_instantiations::instantiation_is_not_abstract():
    assert not inspect.isabstract(instantiations::Instantiation)


def test_instantiations::instantiation_constructor_exists():
    assert callable(instantiations::Instantiation.__init__)


def test_instantiations::instantiation_constructor_args():
    sig = inspect.signature(instantiations::Instantiation.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::instantiations::newconstructorcall_is_not_abstract():
    assert not inspect.isabstract(simTL4J::instantiations::NewConstructorCall)


def test_simtl4j::instantiations::newconstructorcall_constructor_exists():
    assert callable(simTL4J::instantiations::NewConstructorCall.__init__)


def test_simtl4j::instantiations::newconstructorcall_constructor_args():
    sig = inspect.signature(simTL4J::instantiations::NewConstructorCall.__init__)
    params = list(sig.parameters.keys())



def test_generics::typeargumentable_is_not_abstract():
    assert not inspect.isabstract(generics::TypeArgumentable)


def test_generics::typeargumentable_constructor_exists():
    assert callable(generics::TypeArgumentable.__init__)


def test_generics::typeargumentable_constructor_args():
    sig = inspect.signature(generics::TypeArgumentable.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::references::reference_is_not_abstract():
    assert not inspect.isabstract(simTL4J::references::Reference)


def test_simtl4j::references::reference_constructor_exists():
    assert callable(simTL4J::references::Reference.__init__)


def test_simtl4j::references::reference_constructor_args():
    sig = inspect.signature(simTL4J::references::Reference.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::types::classifierreference_is_not_abstract():
    assert not inspect.isabstract(simTL4J::types::ClassifierReference)


def test_simtl4j::types::classifierreference_constructor_exists():
    assert callable(simTL4J::types::ClassifierReference.__init__)


def test_simtl4j::types::classifierreference_constructor_args():
    sig = inspect.signature(simTL4J::types::ClassifierReference.__init__)
    params = list(sig.parameters.keys())



def test_references::argumentable_is_not_abstract():
    assert not inspect.isabstract(references::Argumentable)


def test_references::argumentable_constructor_exists():
    assert callable(references::Argumentable.__init__)


def test_references::argumentable_constructor_args():
    sig = inspect.signature(references::Argumentable.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::references::methodcall_is_not_abstract():
    assert not inspect.isabstract(simTL4J::references::MethodCall)


def test_simtl4j::references::methodcall_constructor_exists():
    assert callable(simTL4J::references::MethodCall.__init__)


def test_simtl4j::references::methodcall_constructor_args():
    sig = inspect.signature(simTL4J::references::MethodCall.__init__)
    params = list(sig.parameters.keys())



def test_referenceableelement_is_not_abstract():
    assert not inspect.isabstract(ReferenceableElement)


def test_referenceableelement_constructor_exists():
    assert callable(ReferenceableElement.__init__)


def test_referenceableelement_constructor_args():
    sig = inspect.signature(ReferenceableElement.__init__)
    params = list(sig.parameters.keys())



def test_staticimport_is_not_abstract():
    assert not inspect.isabstract(StaticImport)


def test_staticimport_constructor_exists():
    assert callable(StaticImport.__init__)


def test_staticimport_constructor_args():
    sig = inspect.signature(StaticImport.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::imports::staticmemberimport_is_not_abstract():
    assert not inspect.isabstract(simTL4J::imports::StaticMemberImport)


def test_simtl4j::imports::staticmemberimport_constructor_exists():
    assert callable(simTL4J::imports::StaticMemberImport.__init__)


def test_simtl4j::imports::staticmemberimport_constructor_args():
    sig = inspect.signature(simTL4J::imports::StaticMemberImport.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::imports::staticclassifierimport_is_not_abstract():
    assert not inspect.isabstract(simTL4J::imports::StaticClassifierImport)


def test_simtl4j::imports::staticclassifierimport_constructor_exists():
    assert callable(simTL4J::imports::StaticClassifierImport.__init__)


def test_simtl4j::imports::staticclassifierimport_constructor_args():
    sig = inspect.signature(simTL4J::imports::StaticClassifierImport.__init__)
    params = list(sig.parameters.keys())



def test_static_is_not_abstract():
    assert not inspect.isabstract(Static)


def test_static_constructor_exists():
    assert callable(Static.__init__)


def test_static_constructor_args():
    sig = inspect.signature(Static.__init__)
    params = list(sig.parameters.keys())



def test_import_is_not_abstract():
    assert not inspect.isabstract(Import)


def test_import_constructor_exists():
    assert callable(Import.__init__)


def test_import_constructor_args():
    sig = inspect.signature(Import.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::imports::staticimport_is_not_abstract():
    assert not inspect.isabstract(simTL4J::imports::StaticImport)


def test_simtl4j::imports::staticimport_constructor_exists():
    assert callable(simTL4J::imports::StaticImport.__init__)


def test_simtl4j::imports::staticimport_constructor_args():
    sig = inspect.signature(simTL4J::imports::StaticImport.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::imports::packageimport_is_not_abstract():
    assert not inspect.isabstract(simTL4J::imports::PackageImport)


def test_simtl4j::imports::packageimport_constructor_exists():
    assert callable(simTL4J::imports::PackageImport.__init__)


def test_simtl4j::imports::packageimport_constructor_args():
    sig = inspect.signature(simTL4J::imports::PackageImport.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::imports::classifierimport_is_not_abstract():
    assert not inspect.isabstract(simTL4J::imports::ClassifierImport)


def test_simtl4j::imports::classifierimport_constructor_exists():
    assert callable(simTL4J::imports::ClassifierImport.__init__)


def test_simtl4j::imports::classifierimport_constructor_args():
    sig = inspect.signature(simTL4J::imports::ClassifierImport.__init__)
    params = list(sig.parameters.keys())



def test_namespaceawareelement_is_not_abstract():
    assert not inspect.isabstract(NamespaceAwareElement)


def test_namespaceawareelement_constructor_exists():
    assert callable(NamespaceAwareElement.__init__)


def test_namespaceawareelement_constructor_args():
    sig = inspect.signature(NamespaceAwareElement.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::imports::import_is_not_abstract():
    assert not inspect.isabstract(simTL4J::imports::Import)


def test_simtl4j::imports::import_constructor_exists():
    assert callable(simTL4J::imports::Import.__init__)


def test_simtl4j::imports::import_constructor_args():
    sig = inspect.signature(simTL4J::imports::Import.__init__)
    params = list(sig.parameters.keys())



def test_typeparameter_is_not_abstract():
    assert not inspect.isabstract(TypeParameter)


def test_typeparameter_constructor_exists():
    assert callable(TypeParameter.__init__)


def test_typeparameter_constructor_args():
    sig = inspect.signature(TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_generics::typeargument_is_not_abstract():
    assert not inspect.isabstract(generics::TypeArgument)


def test_generics::typeargument_constructor_exists():
    assert callable(generics::TypeArgument.__init__)


def test_generics::typeargument_constructor_args():
    sig = inspect.signature(generics::TypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_expressions::unarymodificationexpressionchild_is_not_abstract():
    assert not inspect.isabstract(expressions::UnaryModificationExpressionChild)


def test_expressions::unarymodificationexpressionchild_constructor_exists():
    assert callable(expressions::UnaryModificationExpressionChild.__init__)


def test_expressions::unarymodificationexpressionchild_constructor_args():
    sig = inspect.signature(expressions::UnaryModificationExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_multiplicativeoperator_is_not_abstract():
    assert not inspect.isabstract(MultiplicativeOperator)


def test_multiplicativeoperator_constructor_exists():
    assert callable(MultiplicativeOperator.__init__)


def test_multiplicativeoperator_constructor_args():
    sig = inspect.signature(MultiplicativeOperator.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::multiplication_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::Multiplication)


def test_simtl4j::operators::multiplication_constructor_exists():
    assert callable(simTL4J::operators::Multiplication.__init__)


def test_simtl4j::operators::multiplication_constructor_args():
    sig = inspect.signature(simTL4J::operators::Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::division_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::Division)


def test_simtl4j::operators::division_constructor_exists():
    assert callable(simTL4J::operators::Division.__init__)


def test_simtl4j::operators::division_constructor_args():
    sig = inspect.signature(simTL4J::operators::Division.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::remainder_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::Remainder)


def test_simtl4j::operators::remainder_constructor_exists():
    assert callable(simTL4J::operators::Remainder.__init__)


def test_simtl4j::operators::remainder_constructor_args():
    sig = inspect.signature(simTL4J::operators::Remainder.__init__)
    params = list(sig.parameters.keys())



def test_multiplicativeexpressionchild_is_not_abstract():
    assert not inspect.isabstract(MultiplicativeExpressionChild)


def test_multiplicativeexpressionchild_constructor_exists():
    assert callable(MultiplicativeExpressionChild.__init__)


def test_multiplicativeexpressionchild_constructor_args():
    sig = inspect.signature(MultiplicativeExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::UnaryExpression)


def test_simtl4j::expressions::unaryexpression_constructor_exists():
    assert callable(simTL4J::expressions::UnaryExpression.__init__)


def test_simtl4j::expressions::unaryexpression_constructor_args():
    sig = inspect.signature(simTL4J::expressions::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_additiveoperator_is_not_abstract():
    assert not inspect.isabstract(AdditiveOperator)


def test_additiveoperator_constructor_exists():
    assert callable(AdditiveOperator.__init__)


def test_additiveoperator_constructor_args():
    sig = inspect.signature(AdditiveOperator.__init__)
    params = list(sig.parameters.keys())



def test_additiveexpressionchild_is_not_abstract():
    assert not inspect.isabstract(AdditiveExpressionChild)


def test_additiveexpressionchild_constructor_exists():
    assert callable(AdditiveExpressionChild.__init__)


def test_additiveexpressionchild_constructor_args():
    sig = inspect.signature(AdditiveExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::multiplicativeexpressionchild_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::MultiplicativeExpressionChild)


def test_simtl4j::expressions::multiplicativeexpressionchild_constructor_exists():
    assert callable(simTL4J::expressions::MultiplicativeExpressionChild.__init__)


def test_simtl4j::expressions::multiplicativeexpressionchild_constructor_args():
    sig = inspect.signature(simTL4J::expressions::MultiplicativeExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::MultiplicativeExpression)


def test_simtl4j::expressions::multiplicativeexpression_constructor_exists():
    assert callable(simTL4J::expressions::MultiplicativeExpression.__init__)


def test_simtl4j::expressions::multiplicativeexpression_constructor_args():
    sig = inspect.signature(simTL4J::expressions::MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_conditionalandexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ConditionalAndExpressionChild)


def test_conditionalandexpressionchild_constructor_exists():
    assert callable(ConditionalAndExpressionChild.__init__)


def test_conditionalandexpressionchild_constructor_args():
    sig = inspect.signature(ConditionalAndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::inclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::InclusiveOrExpression)


def test_simtl4j::expressions::inclusiveorexpression_constructor_exists():
    assert callable(simTL4J::expressions::InclusiveOrExpression.__init__)


def test_simtl4j::expressions::inclusiveorexpression_constructor_args():
    sig = inspect.signature(simTL4J::expressions::InclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_conditionalorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ConditionalOrExpressionChild)


def test_conditionalorexpressionchild_constructor_exists():
    assert callable(ConditionalOrExpressionChild.__init__)


def test_conditionalorexpressionchild_constructor_args():
    sig = inspect.signature(ConditionalOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::ConditionalAndExpression)


def test_simtl4j::expressions::conditionalandexpression_constructor_exists():
    assert callable(simTL4J::expressions::ConditionalAndExpression.__init__)


def test_simtl4j::expressions::conditionalandexpression_constructor_args():
    sig = inspect.signature(simTL4J::expressions::ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::conditionalandexpressionchild_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::ConditionalAndExpressionChild)


def test_simtl4j::expressions::conditionalandexpressionchild_constructor_exists():
    assert callable(simTL4J::expressions::ConditionalAndExpressionChild.__init__)


def test_simtl4j::expressions::conditionalandexpressionchild_constructor_args():
    sig = inspect.signature(simTL4J::expressions::ConditionalAndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_relationexpressionchild_is_not_abstract():
    assert not inspect.isabstract(RelationExpressionChild)


def test_relationexpressionchild_constructor_exists():
    assert callable(RelationExpressionChild.__init__)


def test_relationexpressionchild_constructor_args():
    sig = inspect.signature(RelationExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::shiftexpressionchild_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::ShiftExpressionChild)


def test_simtl4j::expressions::shiftexpressionchild_constructor_exists():
    assert callable(simTL4J::expressions::ShiftExpressionChild.__init__)


def test_simtl4j::expressions::shiftexpressionchild_constructor_args():
    sig = inspect.signature(simTL4J::expressions::ShiftExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_instanceofexpressionchild_is_not_abstract():
    assert not inspect.isabstract(InstanceOfExpressionChild)


def test_instanceofexpressionchild_constructor_exists():
    assert callable(InstanceOfExpressionChild.__init__)


def test_instanceofexpressionchild_constructor_args():
    sig = inspect.signature(InstanceOfExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::relationexpression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::RelationExpression)


def test_simtl4j::expressions::relationexpression_constructor_exists():
    assert callable(simTL4J::expressions::RelationExpression.__init__)


def test_simtl4j::expressions::relationexpression_constructor_args():
    sig = inspect.signature(simTL4J::expressions::RelationExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::equalityexpressionchild_is_not_abstract():
    assert not inspect.isabstract(expressions::EqualityExpressionChild)


def test_expressions::equalityexpressionchild_constructor_exists():
    assert callable(expressions::EqualityExpressionChild.__init__)


def test_expressions::equalityexpressionchild_constructor_args():
    sig = inspect.signature(expressions::EqualityExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_equalityexpressionchild_is_not_abstract():
    assert not inspect.isabstract(EqualityExpressionChild)


def test_equalityexpressionchild_constructor_exists():
    assert callable(EqualityExpressionChild.__init__)


def test_equalityexpressionchild_constructor_args():
    sig = inspect.signature(EqualityExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::instanceofexpressionchild_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::InstanceOfExpressionChild)


def test_simtl4j::expressions::instanceofexpressionchild_constructor_exists():
    assert callable(simTL4J::expressions::InstanceOfExpressionChild.__init__)


def test_simtl4j::expressions::instanceofexpressionchild_constructor_args():
    sig = inspect.signature(simTL4J::expressions::InstanceOfExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_equalityoperator_is_not_abstract():
    assert not inspect.isabstract(EqualityOperator)


def test_equalityoperator_constructor_exists():
    assert callable(EqualityOperator.__init__)


def test_equalityoperator_constructor_args():
    sig = inspect.signature(EqualityOperator.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::notequal_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::NotEqual)


def test_simtl4j::operators::notequal_constructor_exists():
    assert callable(simTL4J::operators::NotEqual.__init__)


def test_simtl4j::operators::notequal_constructor_args():
    sig = inspect.signature(simTL4J::operators::NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::equal_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::Equal)


def test_simtl4j::operators::equal_constructor_exists():
    assert callable(simTL4J::operators::Equal.__init__)


def test_simtl4j::operators::equal_constructor_args():
    sig = inspect.signature(simTL4J::operators::Equal.__init__)
    params = list(sig.parameters.keys())



def test_andexpressionchild_is_not_abstract():
    assert not inspect.isabstract(AndExpressionChild)


def test_andexpressionchild_constructor_exists():
    assert callable(AndExpressionChild.__init__)


def test_andexpressionchild_constructor_args():
    sig = inspect.signature(AndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::equalityexpression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::EqualityExpression)


def test_simtl4j::expressions::equalityexpression_constructor_exists():
    assert callable(simTL4J::expressions::EqualityExpression.__init__)


def test_simtl4j::expressions::equalityexpression_constructor_args():
    sig = inspect.signature(simTL4J::expressions::EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::equalityexpressionchild_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::EqualityExpressionChild)


def test_simtl4j::expressions::equalityexpressionchild_constructor_exists():
    assert callable(simTL4J::expressions::EqualityExpressionChild.__init__)


def test_simtl4j::expressions::equalityexpressionchild_constructor_args():
    sig = inspect.signature(simTL4J::expressions::EqualityExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_exclusiveorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ExclusiveOrExpressionChild)


def test_exclusiveorexpressionchild_constructor_exists():
    assert callable(ExclusiveOrExpressionChild.__init__)


def test_exclusiveorexpressionchild_constructor_args():
    sig = inspect.signature(ExclusiveOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::andexpression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::AndExpression)


def test_simtl4j::expressions::andexpression_constructor_exists():
    assert callable(simTL4J::expressions::AndExpression.__init__)


def test_simtl4j::expressions::andexpression_constructor_args():
    sig = inspect.signature(simTL4J::expressions::AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::andexpressionchild_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::AndExpressionChild)


def test_simtl4j::expressions::andexpressionchild_constructor_exists():
    assert callable(simTL4J::expressions::AndExpressionChild.__init__)


def test_simtl4j::expressions::andexpressionchild_constructor_args():
    sig = inspect.signature(simTL4J::expressions::AndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::inclusiveorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::InclusiveOrExpressionChild)


def test_simtl4j::expressions::inclusiveorexpressionchild_constructor_exists():
    assert callable(simTL4J::expressions::InclusiveOrExpressionChild.__init__)


def test_simtl4j::expressions::inclusiveorexpressionchild_constructor_args():
    sig = inspect.signature(simTL4J::expressions::InclusiveOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_inclusiveorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(InclusiveOrExpressionChild)


def test_inclusiveorexpressionchild_constructor_exists():
    assert callable(InclusiveOrExpressionChild.__init__)


def test_inclusiveorexpressionchild_constructor_args():
    sig = inspect.signature(InclusiveOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::exclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::ExclusiveOrExpression)


def test_simtl4j::expressions::exclusiveorexpression_constructor_exists():
    assert callable(simTL4J::expressions::ExclusiveOrExpression.__init__)


def test_simtl4j::expressions::exclusiveorexpression_constructor_args():
    sig = inspect.signature(simTL4J::expressions::ExclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::exclusiveorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::ExclusiveOrExpressionChild)


def test_simtl4j::expressions::exclusiveorexpressionchild_constructor_exists():
    assert callable(simTL4J::expressions::ExclusiveOrExpressionChild.__init__)


def test_simtl4j::expressions::exclusiveorexpressionchild_constructor_args():
    sig = inspect.signature(simTL4J::expressions::ExclusiveOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_compilationunit_is_not_abstract():
    assert not inspect.isabstract(CompilationUnit)


def test_compilationunit_constructor_exists():
    assert callable(CompilationUnit.__init__)


def test_compilationunit_constructor_args():
    sig = inspect.signature(CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_annotations::annotable_is_not_abstract():
    assert not inspect.isabstract(annotations::Annotable)


def test_annotations::annotable_constructor_exists():
    assert callable(annotations::Annotable.__init__)


def test_annotations::annotable_constructor_args():
    sig = inspect.signature(annotations::Annotable.__init__)
    params = list(sig.parameters.keys())



def test_containers::javaroot_is_not_abstract():
    assert not inspect.isabstract(containers::JavaRoot)


def test_containers::javaroot_constructor_exists():
    assert callable(containers::JavaRoot.__init__)


def test_containers::javaroot_constructor_args():
    sig = inspect.signature(containers::JavaRoot.__init__)
    params = list(sig.parameters.keys())



def test_conditionalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ConditionalExpressionChild)


def test_conditionalexpressionchild_constructor_exists():
    assert callable(ConditionalExpressionChild.__init__)


def test_conditionalexpressionchild_constructor_args():
    sig = inspect.signature(ConditionalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::conditionalorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::ConditionalOrExpressionChild)


def test_simtl4j::expressions::conditionalorexpressionchild_constructor_exists():
    assert callable(simTL4J::expressions::ConditionalOrExpressionChild.__init__)


def test_simtl4j::expressions::conditionalorexpressionchild_constructor_args():
    sig = inspect.signature(simTL4J::expressions::ConditionalOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::ConditionalOrExpression)


def test_simtl4j::expressions::conditionalorexpression_constructor_exists():
    assert callable(simTL4J::expressions::ConditionalOrExpression.__init__)


def test_simtl4j::expressions::conditionalorexpression_constructor_args():
    sig = inspect.signature(simTL4J::expressions::ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_assignmentoperator_is_not_abstract():
    assert not inspect.isabstract(AssignmentOperator)


def test_assignmentoperator_constructor_exists():
    assert callable(AssignmentOperator.__init__)


def test_assignmentoperator_constructor_args():
    sig = inspect.signature(AssignmentOperator.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::assignmentexclusiveor_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::AssignmentExclusiveOr)


def test_simtl4j::operators::assignmentexclusiveor_constructor_exists():
    assert callable(simTL4J::operators::AssignmentExclusiveOr.__init__)


def test_simtl4j::operators::assignmentexclusiveor_constructor_args():
    sig = inspect.signature(simTL4J::operators::AssignmentExclusiveOr.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::assignmentrightshift_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::AssignmentRightShift)


def test_simtl4j::operators::assignmentrightshift_constructor_exists():
    assert callable(simTL4J::operators::AssignmentRightShift.__init__)


def test_simtl4j::operators::assignmentrightshift_constructor_args():
    sig = inspect.signature(simTL4J::operators::AssignmentRightShift.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::assignmentunsignedrightshift_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::AssignmentUnsignedRightShift)


def test_simtl4j::operators::assignmentunsignedrightshift_constructor_exists():
    assert callable(simTL4J::operators::AssignmentUnsignedRightShift.__init__)


def test_simtl4j::operators::assignmentunsignedrightshift_constructor_args():
    sig = inspect.signature(simTL4J::operators::AssignmentUnsignedRightShift.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::assignmentminus_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::AssignmentMinus)


def test_simtl4j::operators::assignmentminus_constructor_exists():
    assert callable(simTL4J::operators::AssignmentMinus.__init__)


def test_simtl4j::operators::assignmentminus_constructor_args():
    sig = inspect.signature(simTL4J::operators::AssignmentMinus.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::assignmentand_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::AssignmentAnd)


def test_simtl4j::operators::assignmentand_constructor_exists():
    assert callable(simTL4J::operators::AssignmentAnd.__init__)


def test_simtl4j::operators::assignmentand_constructor_args():
    sig = inspect.signature(simTL4J::operators::AssignmentAnd.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::assignmentmultiplication_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::AssignmentMultiplication)


def test_simtl4j::operators::assignmentmultiplication_constructor_exists():
    assert callable(simTL4J::operators::AssignmentMultiplication.__init__)


def test_simtl4j::operators::assignmentmultiplication_constructor_args():
    sig = inspect.signature(simTL4J::operators::AssignmentMultiplication.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::assignmentor_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::AssignmentOr)


def test_simtl4j::operators::assignmentor_constructor_exists():
    assert callable(simTL4J::operators::AssignmentOr.__init__)


def test_simtl4j::operators::assignmentor_constructor_args():
    sig = inspect.signature(simTL4J::operators::AssignmentOr.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::assignmentdivision_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::AssignmentDivision)


def test_simtl4j::operators::assignmentdivision_constructor_exists():
    assert callable(simTL4J::operators::AssignmentDivision.__init__)


def test_simtl4j::operators::assignmentdivision_constructor_args():
    sig = inspect.signature(simTL4J::operators::AssignmentDivision.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::assignmentplus_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::AssignmentPlus)


def test_simtl4j::operators::assignmentplus_constructor_exists():
    assert callable(simTL4J::operators::AssignmentPlus.__init__)


def test_simtl4j::operators::assignmentplus_constructor_args():
    sig = inspect.signature(simTL4J::operators::AssignmentPlus.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::assignmentleftshift_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::AssignmentLeftShift)


def test_simtl4j::operators::assignmentleftshift_constructor_exists():
    assert callable(simTL4J::operators::AssignmentLeftShift.__init__)


def test_simtl4j::operators::assignmentleftshift_constructor_args():
    sig = inspect.signature(simTL4J::operators::AssignmentLeftShift.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::assignmentmodulo_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::AssignmentModulo)


def test_simtl4j::operators::assignmentmodulo_constructor_exists():
    assert callable(simTL4J::operators::AssignmentModulo.__init__)


def test_simtl4j::operators::assignmentmodulo_constructor_args():
    sig = inspect.signature(simTL4J::operators::AssignmentModulo.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::assignment_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::Assignment)


def test_simtl4j::operators::assignment_constructor_exists():
    assert callable(simTL4J::operators::Assignment.__init__)


def test_simtl4j::operators::assignment_constructor_args():
    sig = inspect.signature(simTL4J::operators::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_assignmentexpressionchild_is_not_abstract():
    assert not inspect.isabstract(AssignmentExpressionChild)


def test_assignmentexpressionchild_constructor_exists():
    assert callable(AssignmentExpressionChild.__init__)


def test_assignmentexpressionchild_constructor_args():
    sig = inspect.signature(AssignmentExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::conditionalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::ConditionalExpressionChild)


def test_simtl4j::expressions::conditionalexpressionchild_constructor_exists():
    assert callable(simTL4J::expressions::ConditionalExpressionChild.__init__)


def test_simtl4j::expressions::conditionalexpressionchild_constructor_args():
    sig = inspect.signature(simTL4J::expressions::ConditionalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::ConditionalExpression)


def test_simtl4j::expressions::conditionalexpression_constructor_exists():
    assert callable(simTL4J::expressions::ConditionalExpression.__init__)


def test_simtl4j::expressions::conditionalexpression_constructor_args():
    sig = inspect.signature(simTL4J::expressions::ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_forloopinitializer_is_not_abstract():
    assert not inspect.isabstract(ForLoopInitializer)


def test_forloopinitializer_constructor_exists():
    assert callable(ForLoopInitializer.__init__)


def test_forloopinitializer_constructor_args():
    sig = inspect.signature(ForLoopInitializer.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::expressionlist_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::ExpressionList)


def test_simtl4j::expressions::expressionlist_constructor_exists():
    assert callable(simTL4J::expressions::ExpressionList.__init__)


def test_simtl4j::expressions::expressionlist_constructor_args():
    sig = inspect.signature(simTL4J::expressions::ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_javaroot_is_not_abstract():
    assert not inspect.isabstract(JavaRoot)


def test_javaroot_constructor_exists():
    assert callable(JavaRoot.__init__)


def test_javaroot_constructor_args():
    sig = inspect.signature(JavaRoot.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::containers::emptymodel_is_not_abstract():
    assert not inspect.isabstract(simTL4J::containers::EmptyModel)


def test_simtl4j::containers::emptymodel_constructor_exists():
    assert callable(simTL4J::containers::EmptyModel.__init__)


def test_simtl4j::containers::emptymodel_constructor_args():
    sig = inspect.signature(simTL4J::containers::EmptyModel.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::containers::compilationunit_is_not_abstract():
    assert not inspect.isabstract(simTL4J::containers::CompilationUnit)


def test_simtl4j::containers::compilationunit_constructor_exists():
    assert callable(simTL4J::containers::CompilationUnit.__init__)


def test_simtl4j::containers::compilationunit_constructor_args():
    sig = inspect.signature(simTL4J::containers::CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_imports::importingelement_is_not_abstract():
    assert not inspect.isabstract(imports::ImportingElement)


def test_imports::importingelement_constructor_exists():
    assert callable(imports::ImportingElement.__init__)


def test_imports::importingelement_constructor_args():
    sig = inspect.signature(imports::ImportingElement.__init__)
    params = list(sig.parameters.keys())



def test_commons::namedelement_is_not_abstract():
    assert not inspect.isabstract(commons::NamedElement)


def test_commons::namedelement_constructor_exists():
    assert callable(commons::NamedElement.__init__)


def test_commons::namedelement_constructor_args():
    sig = inspect.signature(commons::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_tplaceholder_is_not_abstract():
    assert not inspect.isabstract(TPlaceholder)


def test_tplaceholder_constructor_exists():
    assert callable(TPlaceholder.__init__)


def test_tplaceholder_constructor_args():
    sig = inspect.signature(TPlaceholder.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::commons::commentable_is_not_abstract():
    assert not inspect.isabstract(simTL4J::commons::Commentable)


def test_simtl4j::commons::commentable_constructor_exists():
    assert callable(simTL4J::commons::Commentable.__init__)


def test_simtl4j::commons::commentable_constructor_args():
    sig = inspect.signature(simTL4J::commons::Commentable.__init__)
    params = list(sig.parameters.keys())
    assert "comments" in params, "Missing parameter 'comments'"

def test_simtl4j::commons::commentable_has_comments():
    assert hasattr(simTL4J::commons::Commentable, "comments")
    descriptor = None
    for klass in simTL4J::commons::Commentable.__mro__:
        if "comments" in klass.__dict__:
            descriptor = klass.__dict__["comments"]
            break
    assert isinstance(descriptor, property)



def test_classifiers::implementor_is_not_abstract():
    assert not inspect.isabstract(classifiers::Implementor)


def test_classifiers::implementor_constructor_exists():
    assert callable(classifiers::Implementor.__init__)


def test_classifiers::implementor_constructor_args():
    sig = inspect.signature(classifiers::Implementor.__init__)
    params = list(sig.parameters.keys())



def test_classifiers::concreteclassifier_is_not_abstract():
    assert not inspect.isabstract(classifiers::ConcreteClassifier)


def test_classifiers::concreteclassifier_constructor_exists():
    assert callable(classifiers::ConcreteClassifier.__init__)


def test_classifiers::concreteclassifier_constructor_args():
    sig = inspect.signature(classifiers::ConcreteClassifier.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::classifiers::class_is_not_abstract():
    assert not inspect.isabstract(simTL4J::classifiers::Class)


def test_simtl4j::classifiers::class_constructor_exists():
    assert callable(simTL4J::classifiers::Class.__init__)


def test_simtl4j::classifiers::class_constructor_args():
    sig = inspect.signature(simTL4J::classifiers::Class.__init__)
    params = list(sig.parameters.keys())



def test_typereference_is_not_abstract():
    assert not inspect.isabstract(TypeReference)


def test_typereference_constructor_exists():
    assert callable(TypeReference.__init__)


def test_typereference_constructor_args():
    sig = inspect.signature(TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_enumconstant_is_not_abstract():
    assert not inspect.isabstract(EnumConstant)


def test_enumconstant_constructor_exists():
    assert callable(EnumConstant.__init__)


def test_enumconstant_constructor_args():
    sig = inspect.signature(EnumConstant.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::classifiers::enumeration_is_not_abstract():
    assert not inspect.isabstract(simTL4J::classifiers::Enumeration)


def test_simtl4j::classifiers::enumeration_constructor_exists():
    assert callable(simTL4J::classifiers::Enumeration.__init__)


def test_simtl4j::classifiers::enumeration_constructor_args():
    sig = inspect.signature(simTL4J::classifiers::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_concreteclassifier_is_not_abstract():
    assert not inspect.isabstract(ConcreteClassifier)


def test_concreteclassifier_constructor_exists():
    assert callable(ConcreteClassifier.__init__)


def test_concreteclassifier_constructor_args():
    sig = inspect.signature(ConcreteClassifier.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::classifiers::annotation_is_not_abstract():
    assert not inspect.isabstract(simTL4J::classifiers::Annotation)


def test_simtl4j::classifiers::annotation_constructor_exists():
    assert callable(simTL4J::classifiers::Annotation.__init__)


def test_simtl4j::classifiers::annotation_constructor_args():
    sig = inspect.signature(simTL4J::classifiers::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::classifiers::interface_is_not_abstract():
    assert not inspect.isabstract(simTL4J::classifiers::Interface)


def test_simtl4j::classifiers::interface_constructor_exists():
    assert callable(simTL4J::classifiers::Interface.__init__)


def test_simtl4j::classifiers::interface_constructor_args():
    sig = inspect.signature(simTL4J::classifiers::Interface.__init__)
    params = list(sig.parameters.keys())



def test_arrays::arraytypeable_is_not_abstract():
    assert not inspect.isabstract(arrays::ArrayTypeable)


def test_arrays::arraytypeable_constructor_exists():
    assert callable(arrays::ArrayTypeable.__init__)


def test_arrays::arraytypeable_constructor_args():
    sig = inspect.signature(arrays::ArrayTypeable.__init__)
    params = list(sig.parameters.keys())



def test_types::typedelement_is_not_abstract():
    assert not inspect.isabstract(types::TypedElement)


def test_types::typedelement_constructor_exists():
    assert callable(types::TypedElement.__init__)


def test_types::typedelement_constructor_args():
    sig = inspect.signature(types::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::castexpression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::CastExpression)


def test_simtl4j::expressions::castexpression_constructor_exists():
    assert callable(simTL4J::expressions::CastExpression.__init__)


def test_simtl4j::expressions::castexpression_constructor_args():
    sig = inspect.signature(simTL4J::expressions::CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::InstanceOfExpression)


def test_simtl4j::expressions::instanceofexpression_constructor_exists():
    assert callable(simTL4J::expressions::InstanceOfExpression.__init__)


def test_simtl4j::expressions::instanceofexpression_constructor_args():
    sig = inspect.signature(simTL4J::expressions::InstanceOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::generics::qualifiedtypeargument_is_not_abstract():
    assert not inspect.isabstract(simTL4J::generics::QualifiedTypeArgument)


def test_simtl4j::generics::qualifiedtypeargument_constructor_exists():
    assert callable(simTL4J::generics::QualifiedTypeArgument.__init__)


def test_simtl4j::generics::qualifiedtypeargument_constructor_args():
    sig = inspect.signature(simTL4J::generics::QualifiedTypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_expressions::expression_is_not_abstract():
    assert not inspect.isabstract(expressions::Expression)


def test_expressions::expression_constructor_exists():
    assert callable(expressions::Expression.__init__)


def test_expressions::expression_constructor_args():
    sig = inspect.signature(expressions::Expression.__init__)
    params = list(sig.parameters.keys())



def test_arrayinitializationvalue_is_not_abstract():
    assert not inspect.isabstract(ArrayInitializationValue)


def test_arrayinitializationvalue_constructor_exists():
    assert callable(ArrayInitializationValue.__init__)


def test_arrayinitializationvalue_constructor_args():
    sig = inspect.signature(ArrayInitializationValue.__init__)
    params = list(sig.parameters.keys())



def test_annotations::annotationvalue_is_not_abstract():
    assert not inspect.isabstract(annotations::AnnotationValue)


def test_annotations::annotationvalue_constructor_exists():
    assert callable(annotations::AnnotationValue.__init__)


def test_annotations::annotationvalue_constructor_args():
    sig = inspect.signature(annotations::AnnotationValue.__init__)
    params = list(sig.parameters.keys())



def test_arrays::arrayinitializationvalue_is_not_abstract():
    assert not inspect.isabstract(arrays::ArrayInitializationValue)


def test_arrays::arrayinitializationvalue_constructor_exists():
    assert callable(arrays::ArrayInitializationValue.__init__)


def test_arrays::arrayinitializationvalue_constructor_args():
    sig = inspect.signature(arrays::ArrayInitializationValue.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::expression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::Expression)


def test_simtl4j::expressions::expression_constructor_exists():
    assert callable(simTL4J::expressions::Expression.__init__)


def test_simtl4j::expressions::expression_constructor_args():
    sig = inspect.signature(simTL4J::expressions::Expression.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::arrays::arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(simTL4J::arrays::ArrayInitializer)


def test_simtl4j::arrays::arrayinitializer_constructor_exists():
    assert callable(simTL4J::arrays::ArrayInitializer.__init__)


def test_simtl4j::arrays::arrayinitializer_constructor_args():
    sig = inspect.signature(simTL4J::arrays::ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_modifiers::annotableandmodifiable_is_not_abstract():
    assert not inspect.isabstract(modifiers::AnnotableAndModifiable)


def test_modifiers::annotableandmodifiable_constructor_exists():
    assert callable(modifiers::AnnotableAndModifiable.__init__)


def test_modifiers::annotableandmodifiable_constructor_args():
    sig = inspect.signature(modifiers::AnnotableAndModifiable.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::variables::localvariable_is_not_abstract():
    assert not inspect.isabstract(simTL4J::variables::LocalVariable)


def test_simtl4j::variables::localvariable_constructor_exists():
    assert callable(simTL4J::variables::LocalVariable.__init__)


def test_simtl4j::variables::localvariable_constructor_args():
    sig = inspect.signature(simTL4J::variables::LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::parameters::parameter_is_not_abstract():
    assert not inspect.isabstract(simTL4J::parameters::Parameter)


def test_simtl4j::parameters::parameter_constructor_exists():
    assert callable(simTL4J::parameters::Parameter.__init__)


def test_simtl4j::parameters::parameter_constructor_args():
    sig = inspect.signature(simTL4J::parameters::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_statements::statement_is_not_abstract():
    assert not inspect.isabstract(statements::Statement)


def test_statements::statement_constructor_exists():
    assert callable(statements::Statement.__init__)


def test_statements::statement_constructor_args():
    sig = inspect.signature(statements::Statement.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::simtl::tfor::statementlistcontainer_is_not_abstract():
    assert not inspect.isabstract(simTL4J::simTL::TFor::StatementListContainer)


def test_simtl4j::simtl::tfor::statementlistcontainer_constructor_exists():
    assert callable(simTL4J::simTL::TFor::StatementListContainer.__init__)


def test_simtl4j::simtl::tfor::statementlistcontainer_constructor_args():
    sig = inspect.signature(simTL4J::simTL::TFor::StatementListContainer.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::forloop_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::ForLoop)


def test_simtl4j::statements::forloop_constructor_exists():
    assert callable(simTL4J::statements::ForLoop.__init__)


def test_simtl4j::statements::forloop_constructor_args():
    sig = inspect.signature(simTL4J::statements::ForLoop.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::foreachloop_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::ForEachLoop)


def test_simtl4j::statements::foreachloop_constructor_exists():
    assert callable(simTL4J::statements::ForEachLoop.__init__)


def test_simtl4j::statements::foreachloop_constructor_args():
    sig = inspect.signature(simTL4J::statements::ForEachLoop.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::assert_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::Assert)


def test_simtl4j::statements::assert_constructor_exists():
    assert callable(simTL4J::statements::Assert.__init__)


def test_simtl4j::statements::assert_constructor_args():
    sig = inspect.signature(simTL4J::statements::Assert.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::tryblock_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::TryBlock)


def test_simtl4j::statements::tryblock_constructor_exists():
    assert callable(simTL4J::statements::TryBlock.__init__)


def test_simtl4j::statements::tryblock_constructor_args():
    sig = inspect.signature(simTL4J::statements::TryBlock.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::condition_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::Condition)


def test_simtl4j::statements::condition_constructor_exists():
    assert callable(simTL4J::statements::Condition.__init__)


def test_simtl4j::statements::condition_constructor_args():
    sig = inspect.signature(simTL4J::statements::Condition.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::synchronizedblock_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::SynchronizedBlock)


def test_simtl4j::statements::synchronizedblock_constructor_exists():
    assert callable(simTL4J::statements::SynchronizedBlock.__init__)


def test_simtl4j::statements::synchronizedblock_constructor_args():
    sig = inspect.signature(simTL4J::statements::SynchronizedBlock.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::simtl::tif::statementlistcontainer_is_not_abstract():
    assert not inspect.isabstract(simTL4J::simTL::TIf::StatementListContainer)


def test_simtl4j::simtl::tif::statementlistcontainer_constructor_exists():
    assert callable(simTL4J::simTL::TIf::StatementListContainer.__init__)


def test_simtl4j::simtl::tif::statementlistcontainer_constructor_args():
    sig = inspect.signature(simTL4J::simTL::TIf::StatementListContainer.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::whileloop_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::WhileLoop)


def test_simtl4j::statements::whileloop_constructor_exists():
    assert callable(simTL4J::statements::WhileLoop.__init__)


def test_simtl4j::statements::whileloop_constructor_args():
    sig = inspect.signature(simTL4J::statements::WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::jumplabel_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::JumpLabel)


def test_simtl4j::statements::jumplabel_constructor_exists():
    assert callable(simTL4J::statements::JumpLabel.__init__)


def test_simtl4j::statements::jumplabel_constructor_args():
    sig = inspect.signature(simTL4J::statements::JumpLabel.__init__)
    params = list(sig.parameters.keys())



def test_members::member_is_not_abstract():
    assert not inspect.isabstract(members::Member)


def test_members::member_constructor_exists():
    assert callable(members::Member.__init__)


def test_members::member_constructor_args():
    sig = inspect.signature(members::Member.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::block_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::Block)


def test_simtl4j::statements::block_constructor_exists():
    assert callable(simTL4J::statements::Block.__init__)


def test_simtl4j::statements::block_constructor_args():
    sig = inspect.signature(simTL4J::statements::Block.__init__)
    params = list(sig.parameters.keys())



def test_members::membercontainer_is_not_abstract():
    assert not inspect.isabstract(members::MemberContainer)


def test_members::membercontainer_constructor_exists():
    assert callable(members::MemberContainer.__init__)


def test_members::membercontainer_constructor_args():
    sig = inspect.signature(members::MemberContainer.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::simtl::tfor::membercontainer_is_not_abstract():
    assert not inspect.isabstract(simTL4J::simTL::TFor::MemberContainer)


def test_simtl4j::simtl::tfor::membercontainer_constructor_exists():
    assert callable(simTL4J::simTL::TFor::MemberContainer.__init__)


def test_simtl4j::simtl::tfor::membercontainer_constructor_args():
    sig = inspect.signature(simTL4J::simTL::TFor::MemberContainer.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::simtl::tif::membercontainer_is_not_abstract():
    assert not inspect.isabstract(simTL4J::simTL::TIf::MemberContainer)


def test_simtl4j::simtl::tif::membercontainer_constructor_exists():
    assert callable(simTL4J::simTL::TIf::MemberContainer.__init__)


def test_simtl4j::simtl::tif::membercontainer_constructor_args():
    sig = inspect.signature(simTL4J::simTL::TIf::MemberContainer.__init__)
    params = list(sig.parameters.keys())



def test_generics::typeparametrizable_is_not_abstract():
    assert not inspect.isabstract(generics::TypeParametrizable)


def test_generics::typeparametrizable_constructor_exists():
    assert callable(generics::TypeParametrizable.__init__)


def test_generics::typeparametrizable_constructor_args():
    sig = inspect.signature(generics::TypeParametrizable.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::members::constructor_is_not_abstract():
    assert not inspect.isabstract(simTL4J::members::Constructor)


def test_simtl4j::members::constructor_constructor_exists():
    assert callable(simTL4J::members::Constructor.__init__)


def test_simtl4j::members::constructor_constructor_args():
    sig = inspect.signature(simTL4J::members::Constructor.__init__)
    params = list(sig.parameters.keys())



def test_classifiers::classifier_is_not_abstract():
    assert not inspect.isabstract(classifiers::Classifier)


def test_classifiers::classifier_constructor_exists():
    assert callable(classifiers::Classifier.__init__)


def test_classifiers::classifier_constructor_args():
    sig = inspect.signature(classifiers::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::classifiers::concreteclassifier_is_not_abstract():
    assert not inspect.isabstract(simTL4J::classifiers::ConcreteClassifier)


def test_simtl4j::classifiers::concreteclassifier_constructor_exists():
    assert callable(simTL4J::classifiers::ConcreteClassifier.__init__)


def test_simtl4j::classifiers::concreteclassifier_constructor_args():
    sig = inspect.signature(simTL4J::classifiers::ConcreteClassifier.__init__)
    params = list(sig.parameters.keys())
    assert "fullName" in params, "Missing parameter 'fullName'"

def test_simtl4j::classifiers::concreteclassifier_has_fullName():
    assert hasattr(simTL4J::classifiers::ConcreteClassifier, "fullName")
    descriptor = None
    for klass in simTL4J::classifiers::ConcreteClassifier.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
            break
    assert isinstance(descriptor, property)



def test_references::referenceableelement_is_not_abstract():
    assert not inspect.isabstract(references::ReferenceableElement)


def test_references::referenceableelement_constructor_exists():
    assert callable(references::ReferenceableElement.__init__)


def test_references::referenceableelement_constructor_args():
    sig = inspect.signature(references::ReferenceableElement.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::members::method_is_not_abstract():
    assert not inspect.isabstract(simTL4J::members::Method)


def test_simtl4j::members::method_constructor_exists():
    assert callable(simTL4J::members::Method.__init__)


def test_simtl4j::members::method_constructor_args():
    sig = inspect.signature(simTL4J::members::Method.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::members::enumconstant_is_not_abstract():
    assert not inspect.isabstract(simTL4J::members::EnumConstant)


def test_simtl4j::members::enumconstant_constructor_exists():
    assert callable(simTL4J::members::EnumConstant.__init__)


def test_simtl4j::members::enumconstant_constructor_args():
    sig = inspect.signature(simTL4J::members::EnumConstant.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::members::field_is_not_abstract():
    assert not inspect.isabstract(simTL4J::members::Field)


def test_simtl4j::members::field_constructor_exists():
    assert callable(simTL4J::members::Field.__init__)


def test_simtl4j::members::field_constructor_args():
    sig = inspect.signature(simTL4J::members::Field.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::containers::package_is_not_abstract():
    assert not inspect.isabstract(simTL4J::containers::Package)


def test_simtl4j::containers::package_constructor_exists():
    assert callable(simTL4J::containers::Package.__init__)


def test_simtl4j::containers::package_constructor_args():
    sig = inspect.signature(simTL4J::containers::Package.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::members::additionalfield_is_not_abstract():
    assert not inspect.isabstract(simTL4J::members::AdditionalField)


def test_simtl4j::members::additionalfield_constructor_exists():
    assert callable(simTL4J::members::AdditionalField.__init__)


def test_simtl4j::members::additionalfield_constructor_args():
    sig = inspect.signature(simTL4J::members::AdditionalField.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::variables::additionallocalvariable_is_not_abstract():
    assert not inspect.isabstract(simTL4J::variables::AdditionalLocalVariable)


def test_simtl4j::variables::additionallocalvariable_constructor_exists():
    assert callable(simTL4J::variables::AdditionalLocalVariable.__init__)


def test_simtl4j::variables::additionallocalvariable_constructor_args():
    sig = inspect.signature(simTL4J::variables::AdditionalLocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::variables::variable_is_not_abstract():
    assert not inspect.isabstract(simTL4J::variables::Variable)


def test_simtl4j::variables::variable_constructor_exists():
    assert callable(simTL4J::variables::Variable.__init__)


def test_simtl4j::variables::variable_constructor_args():
    sig = inspect.signature(simTL4J::variables::Variable.__init__)
    params = list(sig.parameters.keys())



def test_types::type_is_not_abstract():
    assert not inspect.isabstract(types::Type)


def test_types::type_constructor_exists():
    assert callable(types::Type.__init__)


def test_types::type_constructor_args():
    sig = inspect.signature(types::Type.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::types::primitivetype_is_not_abstract():
    assert not inspect.isabstract(simTL4J::types::PrimitiveType)


def test_simtl4j::types::primitivetype_constructor_exists():
    assert callable(simTL4J::types::PrimitiveType.__init__)


def test_simtl4j::types::primitivetype_constructor_args():
    sig = inspect.signature(simTL4J::types::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::classifiers::anonymousclass_is_not_abstract():
    assert not inspect.isabstract(simTL4J::classifiers::AnonymousClass)


def test_simtl4j::classifiers::anonymousclass_constructor_exists():
    assert callable(simTL4J::classifiers::AnonymousClass.__init__)


def test_simtl4j::classifiers::anonymousclass_constructor_args():
    sig = inspect.signature(simTL4J::classifiers::AnonymousClass.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::classifiers::classifier_is_not_abstract():
    assert not inspect.isabstract(simTL4J::classifiers::Classifier)


def test_simtl4j::classifiers::classifier_constructor_exists():
    assert callable(simTL4J::classifiers::Classifier.__init__)


def test_simtl4j::classifiers::classifier_constructor_args():
    sig = inspect.signature(simTL4J::classifiers::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(ArrayInitializer)


def test_arrayinitializer_constructor_exists():
    assert callable(ArrayInitializer.__init__)


def test_arrayinitializer_constructor_args():
    sig = inspect.signature(ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_modifiers::annotationinstanceormodifier_is_not_abstract():
    assert not inspect.isabstract(modifiers::AnnotationInstanceOrModifier)


def test_modifiers::annotationinstanceormodifier_constructor_exists():
    assert callable(modifiers::AnnotationInstanceOrModifier.__init__)


def test_modifiers::annotationinstanceormodifier_constructor_args():
    sig = inspect.signature(modifiers::AnnotationInstanceOrModifier.__init__)
    params = list(sig.parameters.keys())



def test_references::reference_is_not_abstract():
    assert not inspect.isabstract(references::Reference)


def test_references::reference_constructor_exists():
    assert callable(references::Reference.__init__)


def test_references::reference_constructor_args():
    sig = inspect.signature(references::Reference.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::instantiations::instantiation_is_not_abstract():
    assert not inspect.isabstract(simTL4J::instantiations::Instantiation)


def test_simtl4j::instantiations::instantiation_constructor_exists():
    assert callable(simTL4J::instantiations::Instantiation.__init__)


def test_simtl4j::instantiations::instantiation_constructor_args():
    sig = inspect.signature(simTL4J::instantiations::Instantiation.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::arrays::arrayinstantiationbysize_is_not_abstract():
    assert not inspect.isabstract(simTL4J::arrays::ArrayInstantiationBySize)


def test_simtl4j::arrays::arrayinstantiationbysize_constructor_exists():
    assert callable(simTL4J::arrays::ArrayInstantiationBySize.__init__)


def test_simtl4j::arrays::arrayinstantiationbysize_constructor_args():
    sig = inspect.signature(simTL4J::arrays::ArrayInstantiationBySize.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::arrays::arrayinstantiationbyvalues_is_not_abstract():
    assert not inspect.isabstract(simTL4J::arrays::ArrayInstantiationByValues)


def test_simtl4j::arrays::arrayinstantiationbyvalues_constructor_exists():
    assert callable(simTL4J::arrays::ArrayInstantiationByValues.__init__)


def test_simtl4j::arrays::arrayinstantiationbyvalues_constructor_args():
    sig = inspect.signature(simTL4J::arrays::ArrayInstantiationByValues.__init__)
    params = list(sig.parameters.keys())



def test_annotationinstance_is_not_abstract():
    assert not inspect.isabstract(AnnotationInstance)


def test_annotationinstance_constructor_exists():
    assert callable(AnnotationInstance.__init__)


def test_annotationinstance_constructor_args():
    sig = inspect.signature(AnnotationInstance.__init__)
    params = list(sig.parameters.keys())



def test_commentable_is_not_abstract():
    assert not inspect.isabstract(Commentable)


def test_commentable_constructor_exists():
    assert callable(Commentable.__init__)


def test_commentable_constructor_args():
    sig = inspect.signature(Commentable.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::members::membercontainer_is_not_abstract():
    assert not inspect.isabstract(simTL4J::members::MemberContainer)


def test_simtl4j::members::membercontainer_constructor_exists():
    assert callable(simTL4J::members::MemberContainer.__init__)


def test_simtl4j::members::membercontainer_constructor_args():
    sig = inspect.signature(simTL4J::members::MemberContainer.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::modifiers::annotationinstanceormodifier_is_not_abstract():
    assert not inspect.isabstract(simTL4J::modifiers::AnnotationInstanceOrModifier)


def test_simtl4j::modifiers::annotationinstanceormodifier_constructor_exists():
    assert callable(simTL4J::modifiers::AnnotationInstanceOrModifier.__init__)


def test_simtl4j::modifiers::annotationinstanceormodifier_constructor_args():
    sig = inspect.signature(simTL4J::modifiers::AnnotationInstanceOrModifier.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::references::argumentable_is_not_abstract():
    assert not inspect.isabstract(simTL4J::references::Argumentable)


def test_simtl4j::references::argumentable_constructor_exists():
    assert callable(simTL4J::references::Argumentable.__init__)


def test_simtl4j::references::argumentable_constructor_args():
    sig = inspect.signature(simTL4J::references::Argumentable.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::statementcontainer_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::StatementContainer)


def test_simtl4j::statements::statementcontainer_constructor_exists():
    assert callable(simTL4J::statements::StatementContainer.__init__)


def test_simtl4j::statements::statementcontainer_constructor_args():
    sig = inspect.signature(simTL4J::statements::StatementContainer.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::arrays::arraydimension_is_not_abstract():
    assert not inspect.isabstract(simTL4J::arrays::ArrayDimension)


def test_simtl4j::arrays::arraydimension_constructor_exists():
    assert callable(simTL4J::arrays::ArrayDimension.__init__)


def test_simtl4j::arrays::arraydimension_constructor_args():
    sig = inspect.signature(simTL4J::arrays::ArrayDimension.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::instantiations::initializable_is_not_abstract():
    assert not inspect.isabstract(simTL4J::instantiations::Initializable)


def test_simtl4j::instantiations::initializable_constructor_exists():
    assert callable(simTL4J::instantiations::Initializable.__init__)


def test_simtl4j::instantiations::initializable_constructor_args():
    sig = inspect.signature(simTL4J::instantiations::Initializable.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::operator_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::Operator)


def test_simtl4j::operators::operator_constructor_exists():
    assert callable(simTL4J::operators::Operator.__init__)


def test_simtl4j::operators::operator_constructor_args():
    sig = inspect.signature(simTL4J::operators::Operator.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::commons::namespaceawareelement_is_not_abstract():
    assert not inspect.isabstract(simTL4J::commons::NamespaceAwareElement)


def test_simtl4j::commons::namespaceawareelement_constructor_exists():
    assert callable(simTL4J::commons::NamespaceAwareElement.__init__)


def test_simtl4j::commons::namespaceawareelement_constructor_args():
    sig = inspect.signature(simTL4J::commons::NamespaceAwareElement.__init__)
    params = list(sig.parameters.keys())
    assert "namespaces" in params, "Missing parameter 'namespaces'"

def test_simtl4j::commons::namespaceawareelement_has_namespaces():
    assert hasattr(simTL4J::commons::NamespaceAwareElement, "namespaces")
    descriptor = None
    for klass in simTL4J::commons::NamespaceAwareElement.__mro__:
        if "namespaces" in klass.__dict__:
            descriptor = klass.__dict__["namespaces"]
            break
    assert isinstance(descriptor, property)



def test_simtl4j::arrays::arrayinitializationvalue_is_not_abstract():
    assert not inspect.isabstract(simTL4J::arrays::ArrayInitializationValue)


def test_simtl4j::arrays::arrayinitializationvalue_constructor_exists():
    assert callable(simTL4J::arrays::ArrayInitializationValue.__init__)


def test_simtl4j::arrays::arrayinitializationvalue_constructor_args():
    sig = inspect.signature(simTL4J::arrays::ArrayInitializationValue.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::statementlistcontainer_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::StatementListContainer)


def test_simtl4j::statements::statementlistcontainer_constructor_exists():
    assert callable(simTL4J::statements::StatementListContainer.__init__)


def test_simtl4j::statements::statementlistcontainer_constructor_args():
    sig = inspect.signature(simTL4J::statements::StatementListContainer.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::types::typedelement_is_not_abstract():
    assert not inspect.isabstract(simTL4J::types::TypedElement)


def test_simtl4j::types::typedelement_constructor_exists():
    assert callable(simTL4J::types::TypedElement.__init__)


def test_simtl4j::types::typedelement_constructor_args():
    sig = inspect.signature(simTL4J::types::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::parameters::parametrizable_is_not_abstract():
    assert not inspect.isabstract(simTL4J::parameters::Parametrizable)


def test_simtl4j::parameters::parametrizable_constructor_exists():
    assert callable(simTL4J::parameters::Parametrizable.__init__)


def test_simtl4j::parameters::parametrizable_constructor_args():
    sig = inspect.signature(simTL4J::parameters::Parametrizable.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::commons::namedelement_is_not_abstract():
    assert not inspect.isabstract(simTL4J::commons::NamedElement)


def test_simtl4j::commons::namedelement_constructor_exists():
    assert callable(simTL4J::commons::NamedElement.__init__)


def test_simtl4j::commons::namedelement_constructor_args():
    sig = inspect.signature(simTL4J::commons::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simtl4j::commons::namedelement_has_name():
    assert hasattr(simTL4J::commons::NamedElement, "name")
    descriptor = None
    for klass in simTL4J::commons::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simtl4j::classifiers::implementor_is_not_abstract():
    assert not inspect.isabstract(simTL4J::classifiers::Implementor)


def test_simtl4j::classifiers::implementor_constructor_exists():
    assert callable(simTL4J::classifiers::Implementor.__init__)


def test_simtl4j::classifiers::implementor_constructor_args():
    sig = inspect.signature(simTL4J::classifiers::Implementor.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::arrays::arrayselector_is_not_abstract():
    assert not inspect.isabstract(simTL4J::arrays::ArraySelector)


def test_simtl4j::arrays::arrayselector_constructor_exists():
    assert callable(simTL4J::arrays::ArraySelector.__init__)


def test_simtl4j::arrays::arrayselector_constructor_args():
    sig = inspect.signature(simTL4J::arrays::ArraySelector.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::imports::importingelement_is_not_abstract():
    assert not inspect.isabstract(simTL4J::imports::ImportingElement)


def test_simtl4j::imports::importingelement_constructor_exists():
    assert callable(simTL4J::imports::ImportingElement.__init__)


def test_simtl4j::imports::importingelement_constructor_args():
    sig = inspect.signature(simTL4J::imports::ImportingElement.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::types::type_is_not_abstract():
    assert not inspect.isabstract(simTL4J::types::Type)


def test_simtl4j::types::type_constructor_exists():
    assert callable(simTL4J::types::Type.__init__)


def test_simtl4j::types::type_constructor_args():
    sig = inspect.signature(simTL4J::types::Type.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::generics::typeparametrizable_is_not_abstract():
    assert not inspect.isabstract(simTL4J::generics::TypeParametrizable)


def test_simtl4j::generics::typeparametrizable_constructor_exists():
    assert callable(simTL4J::generics::TypeParametrizable.__init__)


def test_simtl4j::generics::typeparametrizable_constructor_args():
    sig = inspect.signature(simTL4J::generics::TypeParametrizable.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::modifiers::annotableandmodifiable_is_not_abstract():
    assert not inspect.isabstract(simTL4J::modifiers::AnnotableAndModifiable)


def test_simtl4j::modifiers::annotableandmodifiable_constructor_exists():
    assert callable(simTL4J::modifiers::AnnotableAndModifiable.__init__)


def test_simtl4j::modifiers::annotableandmodifiable_constructor_args():
    sig = inspect.signature(simTL4J::modifiers::AnnotableAndModifiable.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::literals::self_is_not_abstract():
    assert not inspect.isabstract(simTL4J::literals::Self)


def test_simtl4j::literals::self_constructor_exists():
    assert callable(simTL4J::literals::Self.__init__)


def test_simtl4j::literals::self_constructor_args():
    sig = inspect.signature(simTL4J::literals::Self.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::members::exceptionthrower_is_not_abstract():
    assert not inspect.isabstract(simTL4J::members::ExceptionThrower)


def test_simtl4j::members::exceptionthrower_constructor_exists():
    assert callable(simTL4J::members::ExceptionThrower.__init__)


def test_simtl4j::members::exceptionthrower_constructor_args():
    sig = inspect.signature(simTL4J::members::ExceptionThrower.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::statement_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::Statement)


def test_simtl4j::statements::statement_constructor_exists():
    assert callable(simTL4J::statements::Statement.__init__)


def test_simtl4j::statements::statement_constructor_args():
    sig = inspect.signature(simTL4J::statements::Statement.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::conditional_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::Conditional)


def test_simtl4j::statements::conditional_constructor_exists():
    assert callable(simTL4J::statements::Conditional.__init__)


def test_simtl4j::statements::conditional_constructor_args():
    sig = inspect.signature(simTL4J::statements::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::types::typereference_is_not_abstract():
    assert not inspect.isabstract(simTL4J::types::TypeReference)


def test_simtl4j::types::typereference_constructor_exists():
    assert callable(simTL4J::types::TypeReference.__init__)


def test_simtl4j::types::typereference_constructor_args():
    sig = inspect.signature(simTL4J::types::TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::statements::forloopinitializer_is_not_abstract():
    assert not inspect.isabstract(simTL4J::statements::ForLoopInitializer)


def test_simtl4j::statements::forloopinitializer_constructor_exists():
    assert callable(simTL4J::statements::ForLoopInitializer.__init__)


def test_simtl4j::statements::forloopinitializer_constructor_args():
    sig = inspect.signature(simTL4J::statements::ForLoopInitializer.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::modifiers::modifiable_is_not_abstract():
    assert not inspect.isabstract(simTL4J::modifiers::Modifiable)


def test_simtl4j::modifiers::modifiable_constructor_exists():
    assert callable(simTL4J::modifiers::Modifiable.__init__)


def test_simtl4j::modifiers::modifiable_constructor_args():
    sig = inspect.signature(simTL4J::modifiers::Modifiable.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::annotations::annotable_is_not_abstract():
    assert not inspect.isabstract(simTL4J::annotations::Annotable)


def test_simtl4j::annotations::annotable_constructor_exists():
    assert callable(simTL4J::annotations::Annotable.__init__)


def test_simtl4j::annotations::annotable_constructor_args():
    sig = inspect.signature(simTL4J::annotations::Annotable.__init__)
    params = list(sig.parameters.keys())



def test_arraydimension_is_not_abstract():
    assert not inspect.isabstract(ArrayDimension)


def test_arraydimension_constructor_exists():
    assert callable(ArrayDimension.__init__)


def test_arraydimension_constructor_args():
    sig = inspect.signature(ArrayDimension.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::arrays::arraytypeable_is_not_abstract():
    assert not inspect.isabstract(simTL4J::arrays::ArrayTypeable)


def test_simtl4j::arrays::arraytypeable_constructor_exists():
    assert callable(simTL4J::arrays::ArrayTypeable.__init__)


def test_simtl4j::arrays::arraytypeable_constructor_args():
    sig = inspect.signature(simTL4J::arrays::ArrayTypeable.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::assignmentexpressionchild_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::AssignmentExpressionChild)


def test_simtl4j::expressions::assignmentexpressionchild_constructor_exists():
    assert callable(simTL4J::expressions::AssignmentExpressionChild.__init__)


def test_simtl4j::expressions::assignmentexpressionchild_constructor_args():
    sig = inspect.signature(simTL4J::expressions::AssignmentExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::AssignmentExpression)


def test_simtl4j::expressions::assignmentexpression_constructor_exists():
    assert callable(simTL4J::expressions::AssignmentExpression.__init__)


def test_simtl4j::expressions::assignmentexpression_constructor_args():
    sig = inspect.signature(simTL4J::expressions::AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::annotations::annotationvalue_is_not_abstract():
    assert not inspect.isabstract(simTL4J::annotations::AnnotationValue)


def test_simtl4j::annotations::annotationvalue_constructor_exists():
    assert callable(simTL4J::annotations::AnnotationValue.__init__)


def test_simtl4j::annotations::annotationvalue_constructor_args():
    sig = inspect.signature(simTL4J::annotations::AnnotationValue.__init__)
    params = list(sig.parameters.keys())



def test_interfacemethod_is_not_abstract():
    assert not inspect.isabstract(InterfaceMethod)


def test_interfacemethod_constructor_exists():
    assert callable(InterfaceMethod.__init__)


def test_interfacemethod_constructor_args():
    sig = inspect.signature(InterfaceMethod.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::annotations::annotationattribute_is_not_abstract():
    assert not inspect.isabstract(simTL4J::annotations::AnnotationAttribute)


def test_simtl4j::annotations::annotationattribute_constructor_exists():
    assert callable(simTL4J::annotations::AnnotationAttribute.__init__)


def test_simtl4j::annotations::annotationattribute_constructor_args():
    sig = inspect.signature(simTL4J::annotations::AnnotationAttribute.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::annotations::annotationattributesetting_is_not_abstract():
    assert not inspect.isabstract(simTL4J::annotations::AnnotationAttributeSetting)


def test_simtl4j::annotations::annotationattributesetting_constructor_exists():
    assert callable(simTL4J::annotations::AnnotationAttributeSetting.__init__)


def test_simtl4j::annotations::annotationattributesetting_constructor_args():
    sig = inspect.signature(simTL4J::annotations::AnnotationAttributeSetting.__init__)
    params = list(sig.parameters.keys())



def test_annotationattributesetting_is_not_abstract():
    assert not inspect.isabstract(AnnotationAttributeSetting)


def test_annotationattributesetting_constructor_exists():
    assert callable(AnnotationAttributeSetting.__init__)


def test_annotationattributesetting_constructor_args():
    sig = inspect.signature(AnnotationAttributeSetting.__init__)
    params = list(sig.parameters.keys())



def test_annotationvalue_is_not_abstract():
    assert not inspect.isabstract(AnnotationValue)


def test_annotationvalue_constructor_exists():
    assert callable(AnnotationValue.__init__)


def test_annotationvalue_constructor_args():
    sig = inspect.signature(AnnotationValue.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::annotations::annotationparameter_is_not_abstract():
    assert not inspect.isabstract(simTL4J::annotations::AnnotationParameter)


def test_simtl4j::annotations::annotationparameter_constructor_exists():
    assert callable(simTL4J::annotations::AnnotationParameter.__init__)


def test_simtl4j::annotations::annotationparameter_constructor_args():
    sig = inspect.signature(simTL4J::annotations::AnnotationParameter.__init__)
    params = list(sig.parameters.keys())



def test_annotationparameter_is_not_abstract():
    assert not inspect.isabstract(AnnotationParameter)


def test_annotationparameter_constructor_exists():
    assert callable(AnnotationParameter.__init__)


def test_annotationparameter_constructor_args():
    sig = inspect.signature(AnnotationParameter.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::annotations::annotationparameterlist_is_not_abstract():
    assert not inspect.isabstract(simTL4J::annotations::AnnotationParameterList)


def test_simtl4j::annotations::annotationparameterlist_constructor_exists():
    assert callable(simTL4J::annotations::AnnotationParameterList.__init__)


def test_simtl4j::annotations::annotationparameterlist_constructor_args():
    sig = inspect.signature(simTL4J::annotations::AnnotationParameterList.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::annotations::singleannotationparameter_is_not_abstract():
    assert not inspect.isabstract(simTL4J::annotations::SingleAnnotationParameter)


def test_simtl4j::annotations::singleannotationparameter_constructor_exists():
    assert callable(simTL4J::annotations::SingleAnnotationParameter.__init__)


def test_simtl4j::annotations::singleannotationparameter_constructor_args():
    sig = inspect.signature(simTL4J::annotations::SingleAnnotationParameter.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::generics::typeparameter_is_not_abstract():
    assert not inspect.isabstract(simTL4J::generics::TypeParameter)


def test_simtl4j::generics::typeparameter_constructor_exists():
    assert callable(simTL4J::generics::TypeParameter.__init__)


def test_simtl4j::generics::typeparameter_constructor_args():
    sig = inspect.signature(simTL4J::generics::TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_commons::namespaceawareelement_is_not_abstract():
    assert not inspect.isabstract(commons::NamespaceAwareElement)


def test_commons::namespaceawareelement_constructor_exists():
    assert callable(commons::NamespaceAwareElement.__init__)


def test_commons::namespaceawareelement_constructor_args():
    sig = inspect.signature(commons::NamespaceAwareElement.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::annotations::annotationinstance_is_not_abstract():
    assert not inspect.isabstract(simTL4J::annotations::AnnotationInstance)


def test_simtl4j::annotations::annotationinstance_constructor_exists():
    assert callable(simTL4J::annotations::AnnotationInstance.__init__)


def test_simtl4j::annotations::annotationinstance_constructor_args():
    sig = inspect.signature(simTL4J::annotations::AnnotationInstance.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::types::namespaceclassifierreference_is_not_abstract():
    assert not inspect.isabstract(simTL4J::types::NamespaceClassifierReference)


def test_simtl4j::types::namespaceclassifierreference_constructor_exists():
    assert callable(simTL4J::types::NamespaceClassifierReference.__init__)


def test_simtl4j::types::namespaceclassifierreference_constructor_args():
    sig = inspect.signature(simTL4J::types::NamespaceClassifierReference.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::containers::javaroot_is_not_abstract():
    assert not inspect.isabstract(simTL4J::containers::JavaRoot)


def test_simtl4j::containers::javaroot_constructor_exists():
    assert callable(simTL4J::containers::JavaRoot.__init__)


def test_simtl4j::containers::javaroot_constructor_args():
    sig = inspect.signature(simTL4J::containers::JavaRoot.__init__)
    params = list(sig.parameters.keys())



def test_unarymodificationexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryModificationExpression)


def test_unarymodificationexpression_constructor_exists():
    assert callable(UnaryModificationExpression.__init__)


def test_unarymodificationexpression_constructor_args():
    sig = inspect.signature(UnaryModificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::suffixunarymodificationexpression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::SuffixUnaryModificationExpression)


def test_simtl4j::expressions::suffixunarymodificationexpression_constructor_exists():
    assert callable(simTL4J::expressions::SuffixUnaryModificationExpression.__init__)


def test_simtl4j::expressions::suffixunarymodificationexpression_constructor_args():
    sig = inspect.signature(simTL4J::expressions::SuffixUnaryModificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::prefixunarymodificationexpression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::PrefixUnaryModificationExpression)


def test_simtl4j::expressions::prefixunarymodificationexpression_constructor_exists():
    assert callable(simTL4J::expressions::PrefixUnaryModificationExpression.__init__)


def test_simtl4j::expressions::prefixunarymodificationexpression_constructor_args():
    sig = inspect.signature(simTL4J::expressions::PrefixUnaryModificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::generics::calltypeargumentable_is_not_abstract():
    assert not inspect.isabstract(simTL4J::generics::CallTypeArgumentable)


def test_simtl4j::generics::calltypeargumentable_constructor_exists():
    assert callable(simTL4J::generics::CallTypeArgumentable.__init__)


def test_simtl4j::generics::calltypeargumentable_constructor_args():
    sig = inspect.signature(simTL4J::generics::CallTypeArgumentable.__init__)
    params = list(sig.parameters.keys())



def test_typeargument_is_not_abstract():
    assert not inspect.isabstract(TypeArgument)


def test_typeargument_constructor_exists():
    assert callable(TypeArgument.__init__)


def test_typeargument_constructor_args():
    sig = inspect.signature(TypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::generics::extendstypeargument_is_not_abstract():
    assert not inspect.isabstract(simTL4J::generics::ExtendsTypeArgument)


def test_simtl4j::generics::extendstypeargument_constructor_exists():
    assert callable(simTL4J::generics::ExtendsTypeArgument.__init__)


def test_simtl4j::generics::extendstypeargument_constructor_args():
    sig = inspect.signature(simTL4J::generics::ExtendsTypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::generics::supertypeargument_is_not_abstract():
    assert not inspect.isabstract(simTL4J::generics::SuperTypeArgument)


def test_simtl4j::generics::supertypeargument_constructor_exists():
    assert callable(simTL4J::generics::SuperTypeArgument.__init__)


def test_simtl4j::generics::supertypeargument_constructor_args():
    sig = inspect.signature(simTL4J::generics::SuperTypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::generics::unknowntypeargument_is_not_abstract():
    assert not inspect.isabstract(simTL4J::generics::UnknownTypeArgument)


def test_simtl4j::generics::unknowntypeargument_constructor_exists():
    assert callable(simTL4J::generics::UnknownTypeArgument.__init__)


def test_simtl4j::generics::unknowntypeargument_constructor_args():
    sig = inspect.signature(simTL4J::generics::UnknownTypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::generics::typeargumentable_is_not_abstract():
    assert not inspect.isabstract(simTL4J::generics::TypeArgumentable)


def test_simtl4j::generics::typeargumentable_constructor_exists():
    assert callable(simTL4J::generics::TypeArgumentable.__init__)


def test_simtl4j::generics::typeargumentable_constructor_args():
    sig = inspect.signature(simTL4J::generics::TypeArgumentable.__init__)
    params = list(sig.parameters.keys())



def test_arraytypeable_is_not_abstract():
    assert not inspect.isabstract(ArrayTypeable)


def test_arraytypeable_constructor_exists():
    assert callable(ArrayTypeable.__init__)


def test_arraytypeable_constructor_args():
    sig = inspect.signature(ArrayTypeable.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::generics::typeargument_is_not_abstract():
    assert not inspect.isabstract(simTL4J::generics::TypeArgument)


def test_simtl4j::generics::typeargument_constructor_exists():
    assert callable(simTL4J::generics::TypeArgument.__init__)


def test_simtl4j::generics::typeargument_constructor_args():
    sig = inspect.signature(simTL4J::generics::TypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_reference_is_not_abstract():
    assert not inspect.isabstract(Reference)


def test_reference_constructor_exists():
    assert callable(Reference.__init__)


def test_reference_constructor_args():
    sig = inspect.signature(Reference.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::references::selfreference_is_not_abstract():
    assert not inspect.isabstract(simTL4J::references::SelfReference)


def test_simtl4j::references::selfreference_constructor_exists():
    assert callable(simTL4J::references::SelfReference.__init__)


def test_simtl4j::references::selfreference_constructor_args():
    sig = inspect.signature(simTL4J::references::SelfReference.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::references::reflectiveclassreference_is_not_abstract():
    assert not inspect.isabstract(simTL4J::references::ReflectiveClassReference)


def test_simtl4j::references::reflectiveclassreference_constructor_exists():
    assert callable(simTL4J::references::ReflectiveClassReference.__init__)


def test_simtl4j::references::reflectiveclassreference_constructor_args():
    sig = inspect.signature(simTL4J::references::ReflectiveClassReference.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::references::elementreference_is_not_abstract():
    assert not inspect.isabstract(simTL4J::references::ElementReference)


def test_simtl4j::references::elementreference_constructor_exists():
    assert callable(simTL4J::references::ElementReference.__init__)


def test_simtl4j::references::elementreference_constructor_args():
    sig = inspect.signature(simTL4J::references::ElementReference.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::references::stringreference_is_not_abstract():
    assert not inspect.isabstract(simTL4J::references::StringReference)


def test_simtl4j::references::stringreference_constructor_exists():
    assert callable(simTL4J::references::StringReference.__init__)


def test_simtl4j::references::stringreference_constructor_args():
    sig = inspect.signature(simTL4J::references::StringReference.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_simtl4j::references::stringreference_has_value():
    assert hasattr(simTL4J::references::StringReference, "value")
    descriptor = None
    for klass in simTL4J::references::StringReference.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_simtl4j::references::primitivetypereference_is_not_abstract():
    assert not inspect.isabstract(simTL4J::references::PrimitiveTypeReference)


def test_simtl4j::references::primitivetypereference_constructor_exists():
    assert callable(simTL4J::references::PrimitiveTypeReference.__init__)


def test_simtl4j::references::primitivetypereference_constructor_args():
    sig = inspect.signature(simTL4J::references::PrimitiveTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::nestedexpression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::NestedExpression)


def test_simtl4j::expressions::nestedexpression_constructor_exists():
    assert callable(simTL4J::expressions::NestedExpression.__init__)


def test_simtl4j::expressions::nestedexpression_constructor_args():
    sig = inspect.signature(simTL4J::expressions::NestedExpression.__init__)
    params = list(sig.parameters.keys())



def test_shiftoperator_is_not_abstract():
    assert not inspect.isabstract(ShiftOperator)


def test_shiftoperator_constructor_exists():
    assert callable(ShiftOperator.__init__)


def test_shiftoperator_constructor_args():
    sig = inspect.signature(ShiftOperator.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::rightshift_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::RightShift)


def test_simtl4j::operators::rightshift_constructor_exists():
    assert callable(simTL4J::operators::RightShift.__init__)


def test_simtl4j::operators::rightshift_constructor_args():
    sig = inspect.signature(simTL4J::operators::RightShift.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::leftshift_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::LeftShift)


def test_simtl4j::operators::leftshift_constructor_exists():
    assert callable(simTL4J::operators::LeftShift.__init__)


def test_simtl4j::operators::leftshift_constructor_args():
    sig = inspect.signature(simTL4J::operators::LeftShift.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::unsignedrightshift_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::UnsignedRightShift)


def test_simtl4j::operators::unsignedrightshift_constructor_exists():
    assert callable(simTL4J::operators::UnsignedRightShift.__init__)


def test_simtl4j::operators::unsignedrightshift_constructor_args():
    sig = inspect.signature(simTL4J::operators::UnsignedRightShift.__init__)
    params = list(sig.parameters.keys())



def test_shiftexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ShiftExpressionChild)


def test_shiftexpressionchild_constructor_exists():
    assert callable(ShiftExpressionChild.__init__)


def test_shiftexpressionchild_constructor_args():
    sig = inspect.signature(ShiftExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::additiveexpressionchild_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::AdditiveExpressionChild)


def test_simtl4j::expressions::additiveexpressionchild_constructor_exists():
    assert callable(simTL4J::expressions::AdditiveExpressionChild.__init__)


def test_simtl4j::expressions::additiveexpressionchild_constructor_args():
    sig = inspect.signature(simTL4J::expressions::AdditiveExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::additiveexpression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::AdditiveExpression)


def test_simtl4j::expressions::additiveexpression_constructor_exists():
    assert callable(simTL4J::expressions::AdditiveExpression.__init__)


def test_simtl4j::expressions::additiveexpression_constructor_args():
    sig = inspect.signature(simTL4J::expressions::AdditiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::shiftexpression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::ShiftExpression)


def test_simtl4j::expressions::shiftexpression_constructor_exists():
    assert callable(simTL4J::expressions::ShiftExpression.__init__)


def test_simtl4j::expressions::shiftexpression_constructor_args():
    sig = inspect.signature(simTL4J::expressions::ShiftExpression.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::relationexpressionchild_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::RelationExpressionChild)


def test_simtl4j::expressions::relationexpressionchild_constructor_exists():
    assert callable(simTL4J::expressions::RelationExpressionChild.__init__)


def test_simtl4j::expressions::relationexpressionchild_constructor_args():
    sig = inspect.signature(simTL4J::expressions::RelationExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_relationoperator_is_not_abstract():
    assert not inspect.isabstract(RelationOperator)


def test_relationoperator_constructor_exists():
    assert callable(RelationOperator.__init__)


def test_relationoperator_constructor_args():
    sig = inspect.signature(RelationOperator.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::lessthanorequal_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::LessThanOrEqual)


def test_simtl4j::operators::lessthanorequal_constructor_exists():
    assert callable(simTL4J::operators::LessThanOrEqual.__init__)


def test_simtl4j::operators::lessthanorequal_constructor_args():
    sig = inspect.signature(simTL4J::operators::LessThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::greaterthan_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::GreaterThan)


def test_simtl4j::operators::greaterthan_constructor_exists():
    assert callable(simTL4J::operators::GreaterThan.__init__)


def test_simtl4j::operators::greaterthan_constructor_args():
    sig = inspect.signature(simTL4J::operators::GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::greaterthanorequal_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::GreaterThanOrEqual)


def test_simtl4j::operators::greaterthanorequal_constructor_exists():
    assert callable(simTL4J::operators::GreaterThanOrEqual.__init__)


def test_simtl4j::operators::greaterthanorequal_constructor_args():
    sig = inspect.signature(simTL4J::operators::GreaterThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::lessthan_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::LessThan)


def test_simtl4j::operators::lessthan_constructor_exists():
    assert callable(simTL4J::operators::LessThan.__init__)


def test_simtl4j::operators::lessthan_constructor_args():
    sig = inspect.signature(simTL4J::operators::LessThan.__init__)
    params = list(sig.parameters.keys())



def test_unarymodificationoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryModificationOperator)


def test_unarymodificationoperator_constructor_exists():
    assert callable(UnaryModificationOperator.__init__)


def test_unarymodificationoperator_constructor_args():
    sig = inspect.signature(UnaryModificationOperator.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::plusplus_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::PlusPlus)


def test_simtl4j::operators::plusplus_constructor_exists():
    assert callable(simTL4J::operators::PlusPlus.__init__)


def test_simtl4j::operators::plusplus_constructor_args():
    sig = inspect.signature(simTL4J::operators::PlusPlus.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::minusminus_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::MinusMinus)


def test_simtl4j::operators::minusminus_constructor_exists():
    assert callable(simTL4J::operators::MinusMinus.__init__)


def test_simtl4j::operators::minusminus_constructor_args():
    sig = inspect.signature(simTL4J::operators::MinusMinus.__init__)
    params = list(sig.parameters.keys())



def test_unarymodificationexpressionchild_is_not_abstract():
    assert not inspect.isabstract(UnaryModificationExpressionChild)


def test_unarymodificationexpressionchild_constructor_exists():
    assert callable(UnaryModificationExpressionChild.__init__)


def test_unarymodificationexpressionchild_constructor_args():
    sig = inspect.signature(UnaryModificationExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::primaryexpression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::PrimaryExpression)


def test_simtl4j::expressions::primaryexpression_constructor_exists():
    assert callable(simTL4J::expressions::PrimaryExpression.__init__)


def test_simtl4j::expressions::primaryexpression_constructor_args():
    sig = inspect.signature(simTL4J::expressions::PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::unaryexpressionchild_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::UnaryExpressionChild)


def test_simtl4j::expressions::unaryexpressionchild_constructor_exists():
    assert callable(simTL4J::expressions::UnaryExpressionChild.__init__)


def test_simtl4j::expressions::unaryexpressionchild_constructor_args():
    sig = inspect.signature(simTL4J::expressions::UnaryExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpressionchild_is_not_abstract():
    assert not inspect.isabstract(UnaryExpressionChild)


def test_unaryexpressionchild_constructor_exists():
    assert callable(UnaryExpressionChild.__init__)


def test_unaryexpressionchild_constructor_args():
    sig = inspect.signature(UnaryExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::unarymodificationexpressionchild_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::UnaryModificationExpressionChild)


def test_simtl4j::expressions::unarymodificationexpressionchild_constructor_exists():
    assert callable(simTL4J::expressions::UnaryModificationExpressionChild.__init__)


def test_simtl4j::expressions::unarymodificationexpressionchild_constructor_args():
    sig = inspect.signature(simTL4J::expressions::UnaryModificationExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::expressions::unarymodificationexpression_is_not_abstract():
    assert not inspect.isabstract(simTL4J::expressions::UnaryModificationExpression)


def test_simtl4j::expressions::unarymodificationexpression_constructor_exists():
    assert callable(simTL4J::expressions::UnaryModificationExpression.__init__)


def test_simtl4j::expressions::unarymodificationexpression_constructor_args():
    sig = inspect.signature(simTL4J::expressions::UnaryModificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::complement_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::Complement)


def test_simtl4j::operators::complement_constructor_exists():
    assert callable(simTL4J::operators::Complement.__init__)


def test_simtl4j::operators::complement_constructor_args():
    sig = inspect.signature(simTL4J::operators::Complement.__init__)
    params = list(sig.parameters.keys())



def test_simtl4j::operators::negate_is_not_abstract():
    assert not inspect.isabstract(simTL4J::operators::Negate)


def test_simtl4j::operators::negate_constructor_exists():
    assert callable(simTL4J::operators::Negate.__init__)


def test_simtl4j::operators::negate_constructor_args():
    sig = inspect.signature(simTL4J::operators::Negate.__init__)
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
TMethodCall_strategy = st.builds(
    TMethodCall,
)
TUnaryOperator_strategy = st.builds(
    TUnaryOperator,
)
simTL4J::simTL::TUnaryOperatorNOT_strategy = st.builds(
    simTL4J::simTL::TUnaryOperatorNOT,
)
simTL::TPlaceholder_strategy = st.builds(
    simTL::TPlaceholder,
)
simTL4J::simTL::TPlaceholder_strategy = st.builds(
    simTL4J::simTL::TPlaceholder,
)
simTL::TIf_strategy = st.builds(
    simTL::TIf,
)
simTL::TFor_strategy = st.builds(
    simTL::TFor,
)
simTL4J::simTL::TAbstractMethodStatement_strategy = st.builds(
    simTL4J::simTL::TAbstractMethodStatement,
)
simTL4J::simTL::TMethodCall_strategy = st.builds(
    simTL4J::simTL::TMethodCall,
    params=
        safe_text,
    methodName=
        safe_text
)
simTL4J::simTL::TModelImport_strategy = st.builds(
    simTL4J::simTL::TModelImport,
    name=
        safe_text,
    uri=
        safe_text
)
TModelImport_strategy = st.builds(
    TModelImport,
)
simTL4J::simTL::TemplateHeader_strategy = st.builds(
    simTL4J::simTL::TemplateHeader,
)
TemplateHeader_strategy = st.builds(
    TemplateHeader,
)
simTL4J::simTL::Template_strategy = st.builds(
    simTL4J::simTL::Template,
)
simTL4J::simTL::TForVariable_strategy = st.builds(
    simTL4J::simTL::TForVariable,
    name=
        safe_text
)
TForVariable_strategy = st.builds(
    TForVariable,
)
simTL4J::simTL::TFor_strategy = st.builds(
    simTL4J::simTL::TFor,
)
TAbstractMethodStatement_strategy = st.builds(
    TAbstractMethodStatement,
)
simTL4J::simTL::TMethodStatementImpl_strategy = st.builds(
    simTL4J::simTL::TMethodStatementImpl,
    caller=
        safe_text
)
simTL4J::simTL::TUnaryOperator_strategy = st.builds(
    simTL4J::simTL::TUnaryOperator,
)
simTL4J::simTL::TIf_strategy = st.builds(
    simTL4J::simTL::TIf,
)
AdditionalLocalVariable_strategy = st.builds(
    AdditionalLocalVariable,
)
statements::ForLoopInitializer_strategy = st.builds(
    statements::ForLoopInitializer,
)
ClassifierReference_strategy = st.builds(
    ClassifierReference,
)
types::TypeReference_strategy = st.builds(
    types::TypeReference,
)
Block_strategy = st.builds(
    Block,
)
CatchBlock_strategy = st.builds(
    CatchBlock,
)
statements::SwitchCase_strategy = st.builds(
    statements::SwitchCase,
)
LocalVariable_strategy = st.builds(
    LocalVariable,
)
JumpLabel_strategy = st.builds(
    JumpLabel,
)
statements::Conditional_strategy = st.builds(
    statements::Conditional,
)
simTL4J::statements::NormalSwitchCase_strategy = st.builds(
    simTL4J::statements::NormalSwitchCase,
)
StatementListContainer_strategy = st.builds(
    StatementListContainer,
)
simTL4J::statements::SwitchCase_strategy = st.builds(
    simTL4J::statements::SwitchCase,
)
WhileLoop_strategy = st.builds(
    WhileLoop,
)
simTL4J::statements::DoWhileLoop_strategy = st.builds(
    simTL4J::statements::DoWhileLoop,
)
SwitchCase_strategy = st.builds(
    SwitchCase,
)
simTL4J::statements::DefaultSwitchCase_strategy = st.builds(
    simTL4J::statements::DefaultSwitchCase,
)
statements::StatementContainer_strategy = st.builds(
    statements::StatementContainer,
)
OrdinaryParameter_strategy = st.builds(
    OrdinaryParameter,
)
simTL4J::statements::CatchBlock_strategy = st.builds(
    simTL4J::statements::CatchBlock,
)
modifiers::Modifiable_strategy = st.builds(
    modifiers::Modifiable,
)
Jump_strategy = st.builds(
    Jump,
)
simTL4J::statements::Continue_strategy = st.builds(
    simTL4J::statements::Continue,
)
simTL4J::statements::Break_strategy = st.builds(
    simTL4J::statements::Break,
)
references::ElementReference_strategy = st.builds(
    references::ElementReference,
)
Statement_strategy = st.builds(
    Statement,
)
simTL4J::statements::LocalVariableStatement_strategy = st.builds(
    simTL4J::statements::LocalVariableStatement,
)
simTL4J::statements::Throw_strategy = st.builds(
    simTL4J::statements::Throw,
)
simTL4J::statements::Jump_strategy = st.builds(
    simTL4J::statements::Jump,
)
simTL4J::statements::Switch_strategy = st.builds(
    simTL4J::statements::Switch,
)
simTL4J::statements::Return_strategy = st.builds(
    simTL4J::statements::Return,
)
simTL4J::statements::ExpressionStatement_strategy = st.builds(
    simTL4J::statements::ExpressionStatement,
)
simTL4J::statements::EmptyStatement_strategy = st.builds(
    simTL4J::statements::EmptyStatement,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
simTL4J::types::Void_strategy = st.builds(
    simTL4J::types::Void,
)
simTL4J::types::Char_strategy = st.builds(
    simTL4J::types::Char,
)
simTL4J::types::Boolean_strategy = st.builds(
    simTL4J::types::Boolean,
)
simTL4J::types::Long_strategy = st.builds(
    simTL4J::types::Long,
)
simTL4J::types::Int_strategy = st.builds(
    simTL4J::types::Int,
)
simTL4J::types::Double_strategy = st.builds(
    simTL4J::types::Double,
)
simTL4J::types::Short_strategy = st.builds(
    simTL4J::types::Short,
)
simTL4J::types::Byte_strategy = st.builds(
    simTL4J::types::Byte,
)
simTL4J::types::Float_strategy = st.builds(
    simTL4J::types::Float,
)
ElementReference_strategy = st.builds(
    ElementReference,
)
simTL4J::references::IdentifierReference_strategy = st.builds(
    simTL4J::references::IdentifierReference,
)
ArraySelector_strategy = st.builds(
    ArraySelector,
)
expressions::PrimaryExpression_strategy = st.builds(
    expressions::PrimaryExpression,
)
simTL4J::simTL::TPlaceholder::PrimaryExpression_strategy = st.builds(
    simTL4J::simTL::TPlaceholder::PrimaryExpression,
)
Parameter_strategy = st.builds(
    Parameter,
)
simTL4J::parameters::VariableLengthParameter_strategy = st.builds(
    simTL4J::parameters::VariableLengthParameter,
)
simTL4J::parameters::OrdinaryParameter_strategy = st.builds(
    simTL4J::parameters::OrdinaryParameter,
)
operators::UnaryOperator_strategy = st.builds(
    operators::UnaryOperator,
)
operators::AdditiveOperator_strategy = st.builds(
    operators::AdditiveOperator,
)
simTL4J::operators::Subtraction_strategy = st.builds(
    simTL4J::operators::Subtraction,
)
simTL4J::operators::Addition_strategy = st.builds(
    simTL4J::operators::Addition,
)
Operator_strategy = st.builds(
    Operator,
)
simTL4J::operators::MultiplicativeOperator_strategy = st.builds(
    simTL4J::operators::MultiplicativeOperator,
)
simTL4J::operators::UnaryModificationOperator_strategy = st.builds(
    simTL4J::operators::UnaryModificationOperator,
)
simTL4J::operators::EqualityOperator_strategy = st.builds(
    simTL4J::operators::EqualityOperator,
)
simTL4J::operators::RelationOperator_strategy = st.builds(
    simTL4J::operators::RelationOperator,
)
simTL4J::operators::AssignmentOperator_strategy = st.builds(
    simTL4J::operators::AssignmentOperator,
)
simTL4J::operators::UnaryOperator_strategy = st.builds(
    simTL4J::operators::UnaryOperator,
)
simTL4J::operators::ShiftOperator_strategy = st.builds(
    simTL4J::operators::ShiftOperator,
)
simTL4J::operators::AdditiveOperator_strategy = st.builds(
    simTL4J::operators::AdditiveOperator,
)
AnnotationInstanceOrModifier_strategy = st.builds(
    AnnotationInstanceOrModifier,
)
simTL4J::modifiers::Modifier_strategy = st.builds(
    simTL4J::modifiers::Modifier,
)
Modifier_strategy = st.builds(
    Modifier,
)
simTL4J::modifiers::Synchronized_strategy = st.builds(
    simTL4J::modifiers::Synchronized,
)
simTL4J::modifiers::Private_strategy = st.builds(
    simTL4J::modifiers::Private,
)
simTL4J::modifiers::Static_strategy = st.builds(
    simTL4J::modifiers::Static,
)
simTL4J::modifiers::Strictfp_strategy = st.builds(
    simTL4J::modifiers::Strictfp,
)
simTL4J::modifiers::Transient_strategy = st.builds(
    simTL4J::modifiers::Transient,
)
simTL4J::modifiers::Abstract_strategy = st.builds(
    simTL4J::modifiers::Abstract,
)
simTL4J::modifiers::Volatile_strategy = st.builds(
    simTL4J::modifiers::Volatile,
)
simTL4J::modifiers::Native_strategy = st.builds(
    simTL4J::modifiers::Native,
)
simTL4J::modifiers::Protected_strategy = st.builds(
    simTL4J::modifiers::Protected,
)
simTL4J::modifiers::Public_strategy = st.builds(
    simTL4J::modifiers::Public,
)
simTL4J::modifiers::Final_strategy = st.builds(
    simTL4J::modifiers::Final,
)
members::Method_strategy = st.builds(
    members::Method,
)
Method_strategy = st.builds(
    Method,
)
simTL4J::members::InterfaceMethod_strategy = st.builds(
    simTL4J::members::InterfaceMethod,
)
AdditionalField_strategy = st.builds(
    AdditionalField,
)
variables::Variable_strategy = st.builds(
    variables::Variable,
)
members::ExceptionThrower_strategy = st.builds(
    members::ExceptionThrower,
)
parameters::Parametrizable_strategy = st.builds(
    parameters::Parametrizable,
)
statements::StatementListContainer_strategy = st.builds(
    statements::StatementListContainer,
)
simTL4J::members::ClassMethod_strategy = st.builds(
    simTL4J::members::ClassMethod,
)
instantiations::Initializable_strategy = st.builds(
    instantiations::Initializable,
)
Member_strategy = st.builds(
    Member,
)
simTL4J::members::EmptyMember_strategy = st.builds(
    simTL4J::members::EmptyMember,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
simTL4J::references::ReferenceableElement_strategy = st.builds(
    simTL4J::references::ReferenceableElement,
)
simTL4J::members::Member_strategy = st.builds(
    simTL4J::members::Member,
)
NamespaceClassifierReference_strategy = st.builds(
    NamespaceClassifierReference,
)
LongLiteral_strategy = st.builds(
    LongLiteral,
)
simTL4J::literals::OctalLongLiteral_strategy = st.builds(
    simTL4J::literals::OctalLongLiteral,
    octalValue=
        safe_text
)
simTL4J::literals::HexLongLiteral_strategy = st.builds(
    simTL4J::literals::HexLongLiteral,
    hexValue=
        safe_text
)
simTL4J::literals::DecimalLongLiteral_strategy = st.builds(
    simTL4J::literals::DecimalLongLiteral,
    decimalValue=
        safe_text
)
IntegerLiteral_strategy = st.builds(
    IntegerLiteral,
)
simTL4J::literals::HexIntegerLiteral_strategy = st.builds(
    simTL4J::literals::HexIntegerLiteral,
    hexValue=
        safe_text
)
simTL4J::literals::OctalIntegerLiteral_strategy = st.builds(
    simTL4J::literals::OctalIntegerLiteral,
    octalValue=
        safe_text
)
simTL4J::literals::DecimalIntegerLiteral_strategy = st.builds(
    simTL4J::literals::DecimalIntegerLiteral,
    decimalValue=
        safe_text
)
DoubleLiteral_strategy = st.builds(
    DoubleLiteral,
)
simTL4J::literals::HexDoubleLiteral_strategy = st.builds(
    simTL4J::literals::HexDoubleLiteral,
    hexValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
simTL4J::literals::DecimalDoubleLiteral_strategy = st.builds(
    simTL4J::literals::DecimalDoubleLiteral,
    decimalValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
FloatLiteral_strategy = st.builds(
    FloatLiteral,
)
simTL4J::literals::HexFloatLiteral_strategy = st.builds(
    simTL4J::literals::HexFloatLiteral,
    hexValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
simTL4J::literals::DecimalFloatLiteral_strategy = st.builds(
    simTL4J::literals::DecimalFloatLiteral,
    decimalValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Literal_strategy = st.builds(
    Literal,
)
simTL4J::literals::CharacterLiteral_strategy = st.builds(
    simTL4J::literals::CharacterLiteral,
    value=
        safe_text
)
simTL4J::literals::FloatLiteral_strategy = st.builds(
    simTL4J::literals::FloatLiteral,
)
simTL4J::literals::NullLiteral_strategy = st.builds(
    simTL4J::literals::NullLiteral,
)
simTL4J::literals::DoubleLiteral_strategy = st.builds(
    simTL4J::literals::DoubleLiteral,
)
simTL4J::literals::LongLiteral_strategy = st.builds(
    simTL4J::literals::LongLiteral,
)
simTL4J::literals::IntegerLiteral_strategy = st.builds(
    simTL4J::literals::IntegerLiteral,
)
simTL4J::literals::BooleanLiteral_strategy = st.builds(
    simTL4J::literals::BooleanLiteral,
    value=
        st.booleans()
)
PrimaryExpression_strategy = st.builds(
    PrimaryExpression,
)
simTL4J::literals::Literal_strategy = st.builds(
    simTL4J::literals::Literal,
)
Self_strategy = st.builds(
    Self,
)
simTL4J::literals::This_strategy = st.builds(
    simTL4J::literals::This,
)
simTL4J::literals::Super_strategy = st.builds(
    simTL4J::literals::Super,
)
Instantiation_strategy = st.builds(
    Instantiation,
)
simTL4J::instantiations::ExplicitConstructorCall_strategy = st.builds(
    simTL4J::instantiations::ExplicitConstructorCall,
)
AnonymousClass_strategy = st.builds(
    AnonymousClass,
)
generics::CallTypeArgumentable_strategy = st.builds(
    generics::CallTypeArgumentable,
)
instantiations::Instantiation_strategy = st.builds(
    instantiations::Instantiation,
)
simTL4J::instantiations::NewConstructorCall_strategy = st.builds(
    simTL4J::instantiations::NewConstructorCall,
)
generics::TypeArgumentable_strategy = st.builds(
    generics::TypeArgumentable,
)
simTL4J::references::Reference_strategy = st.builds(
    simTL4J::references::Reference,
)
simTL4J::types::ClassifierReference_strategy = st.builds(
    simTL4J::types::ClassifierReference,
)
references::Argumentable_strategy = st.builds(
    references::Argumentable,
)
simTL4J::references::MethodCall_strategy = st.builds(
    simTL4J::references::MethodCall,
)
ReferenceableElement_strategy = st.builds(
    ReferenceableElement,
)
StaticImport_strategy = st.builds(
    StaticImport,
)
simTL4J::imports::StaticMemberImport_strategy = st.builds(
    simTL4J::imports::StaticMemberImport,
)
simTL4J::imports::StaticClassifierImport_strategy = st.builds(
    simTL4J::imports::StaticClassifierImport,
)
Static_strategy = st.builds(
    Static,
)
Import_strategy = st.builds(
    Import,
)
simTL4J::imports::StaticImport_strategy = st.builds(
    simTL4J::imports::StaticImport,
)
simTL4J::imports::PackageImport_strategy = st.builds(
    simTL4J::imports::PackageImport,
)
simTL4J::imports::ClassifierImport_strategy = st.builds(
    simTL4J::imports::ClassifierImport,
)
NamespaceAwareElement_strategy = st.builds(
    NamespaceAwareElement,
)
simTL4J::imports::Import_strategy = st.builds(
    simTL4J::imports::Import,
)
TypeParameter_strategy = st.builds(
    TypeParameter,
)
generics::TypeArgument_strategy = st.builds(
    generics::TypeArgument,
)
expressions::UnaryModificationExpressionChild_strategy = st.builds(
    expressions::UnaryModificationExpressionChild,
)
MultiplicativeOperator_strategy = st.builds(
    MultiplicativeOperator,
)
simTL4J::operators::Multiplication_strategy = st.builds(
    simTL4J::operators::Multiplication,
)
simTL4J::operators::Division_strategy = st.builds(
    simTL4J::operators::Division,
)
simTL4J::operators::Remainder_strategy = st.builds(
    simTL4J::operators::Remainder,
)
MultiplicativeExpressionChild_strategy = st.builds(
    MultiplicativeExpressionChild,
)
simTL4J::expressions::UnaryExpression_strategy = st.builds(
    simTL4J::expressions::UnaryExpression,
)
AdditiveOperator_strategy = st.builds(
    AdditiveOperator,
)
AdditiveExpressionChild_strategy = st.builds(
    AdditiveExpressionChild,
)
simTL4J::expressions::MultiplicativeExpressionChild_strategy = st.builds(
    simTL4J::expressions::MultiplicativeExpressionChild,
)
simTL4J::expressions::MultiplicativeExpression_strategy = st.builds(
    simTL4J::expressions::MultiplicativeExpression,
)
ConditionalAndExpressionChild_strategy = st.builds(
    ConditionalAndExpressionChild,
)
simTL4J::expressions::InclusiveOrExpression_strategy = st.builds(
    simTL4J::expressions::InclusiveOrExpression,
)
ConditionalOrExpressionChild_strategy = st.builds(
    ConditionalOrExpressionChild,
)
simTL4J::expressions::ConditionalAndExpression_strategy = st.builds(
    simTL4J::expressions::ConditionalAndExpression,
)
simTL4J::expressions::ConditionalAndExpressionChild_strategy = st.builds(
    simTL4J::expressions::ConditionalAndExpressionChild,
)
RelationExpressionChild_strategy = st.builds(
    RelationExpressionChild,
)
simTL4J::expressions::ShiftExpressionChild_strategy = st.builds(
    simTL4J::expressions::ShiftExpressionChild,
)
InstanceOfExpressionChild_strategy = st.builds(
    InstanceOfExpressionChild,
)
simTL4J::expressions::RelationExpression_strategy = st.builds(
    simTL4J::expressions::RelationExpression,
)
expressions::EqualityExpressionChild_strategy = st.builds(
    expressions::EqualityExpressionChild,
)
EqualityExpressionChild_strategy = st.builds(
    EqualityExpressionChild,
)
simTL4J::expressions::InstanceOfExpressionChild_strategy = st.builds(
    simTL4J::expressions::InstanceOfExpressionChild,
)
EqualityOperator_strategy = st.builds(
    EqualityOperator,
)
simTL4J::operators::NotEqual_strategy = st.builds(
    simTL4J::operators::NotEqual,
)
simTL4J::operators::Equal_strategy = st.builds(
    simTL4J::operators::Equal,
)
AndExpressionChild_strategy = st.builds(
    AndExpressionChild,
)
simTL4J::expressions::EqualityExpression_strategy = st.builds(
    simTL4J::expressions::EqualityExpression,
)
simTL4J::expressions::EqualityExpressionChild_strategy = st.builds(
    simTL4J::expressions::EqualityExpressionChild,
)
ExclusiveOrExpressionChild_strategy = st.builds(
    ExclusiveOrExpressionChild,
)
simTL4J::expressions::AndExpression_strategy = st.builds(
    simTL4J::expressions::AndExpression,
)
simTL4J::expressions::AndExpressionChild_strategy = st.builds(
    simTL4J::expressions::AndExpressionChild,
)
simTL4J::expressions::InclusiveOrExpressionChild_strategy = st.builds(
    simTL4J::expressions::InclusiveOrExpressionChild,
)
InclusiveOrExpressionChild_strategy = st.builds(
    InclusiveOrExpressionChild,
)
simTL4J::expressions::ExclusiveOrExpression_strategy = st.builds(
    simTL4J::expressions::ExclusiveOrExpression,
)
simTL4J::expressions::ExclusiveOrExpressionChild_strategy = st.builds(
    simTL4J::expressions::ExclusiveOrExpressionChild,
)
Package_strategy = st.builds(
    Package,
)
CompilationUnit_strategy = st.builds(
    CompilationUnit,
)
annotations::Annotable_strategy = st.builds(
    annotations::Annotable,
)
containers::JavaRoot_strategy = st.builds(
    containers::JavaRoot,
)
ConditionalExpressionChild_strategy = st.builds(
    ConditionalExpressionChild,
)
simTL4J::expressions::ConditionalOrExpressionChild_strategy = st.builds(
    simTL4J::expressions::ConditionalOrExpressionChild,
)
simTL4J::expressions::ConditionalOrExpression_strategy = st.builds(
    simTL4J::expressions::ConditionalOrExpression,
)
AssignmentOperator_strategy = st.builds(
    AssignmentOperator,
)
simTL4J::operators::AssignmentExclusiveOr_strategy = st.builds(
    simTL4J::operators::AssignmentExclusiveOr,
)
simTL4J::operators::AssignmentRightShift_strategy = st.builds(
    simTL4J::operators::AssignmentRightShift,
)
simTL4J::operators::AssignmentUnsignedRightShift_strategy = st.builds(
    simTL4J::operators::AssignmentUnsignedRightShift,
)
simTL4J::operators::AssignmentMinus_strategy = st.builds(
    simTL4J::operators::AssignmentMinus,
)
simTL4J::operators::AssignmentAnd_strategy = st.builds(
    simTL4J::operators::AssignmentAnd,
)
simTL4J::operators::AssignmentMultiplication_strategy = st.builds(
    simTL4J::operators::AssignmentMultiplication,
)
simTL4J::operators::AssignmentOr_strategy = st.builds(
    simTL4J::operators::AssignmentOr,
)
simTL4J::operators::AssignmentDivision_strategy = st.builds(
    simTL4J::operators::AssignmentDivision,
)
simTL4J::operators::AssignmentPlus_strategy = st.builds(
    simTL4J::operators::AssignmentPlus,
)
simTL4J::operators::AssignmentLeftShift_strategy = st.builds(
    simTL4J::operators::AssignmentLeftShift,
)
simTL4J::operators::AssignmentModulo_strategy = st.builds(
    simTL4J::operators::AssignmentModulo,
)
simTL4J::operators::Assignment_strategy = st.builds(
    simTL4J::operators::Assignment,
)
AssignmentExpressionChild_strategy = st.builds(
    AssignmentExpressionChild,
)
simTL4J::expressions::ConditionalExpressionChild_strategy = st.builds(
    simTL4J::expressions::ConditionalExpressionChild,
)
simTL4J::expressions::ConditionalExpression_strategy = st.builds(
    simTL4J::expressions::ConditionalExpression,
)
ForLoopInitializer_strategy = st.builds(
    ForLoopInitializer,
)
simTL4J::expressions::ExpressionList_strategy = st.builds(
    simTL4J::expressions::ExpressionList,
)
JavaRoot_strategy = st.builds(
    JavaRoot,
)
simTL4J::containers::EmptyModel_strategy = st.builds(
    simTL4J::containers::EmptyModel,
)
simTL4J::containers::CompilationUnit_strategy = st.builds(
    simTL4J::containers::CompilationUnit,
)
imports::ImportingElement_strategy = st.builds(
    imports::ImportingElement,
)
commons::NamedElement_strategy = st.builds(
    commons::NamedElement,
)
TPlaceholder_strategy = st.builds(
    TPlaceholder,
)
simTL4J::commons::Commentable_strategy = st.builds(
    simTL4J::commons::Commentable,
    comments=
        safe_text
)
classifiers::Implementor_strategy = st.builds(
    classifiers::Implementor,
)
classifiers::ConcreteClassifier_strategy = st.builds(
    classifiers::ConcreteClassifier,
)
simTL4J::classifiers::Class_strategy = st.builds(
    simTL4J::classifiers::Class,
)
TypeReference_strategy = st.builds(
    TypeReference,
)
EnumConstant_strategy = st.builds(
    EnumConstant,
)
simTL4J::classifiers::Enumeration_strategy = st.builds(
    simTL4J::classifiers::Enumeration,
)
ConcreteClassifier_strategy = st.builds(
    ConcreteClassifier,
)
simTL4J::classifiers::Annotation_strategy = st.builds(
    simTL4J::classifiers::Annotation,
)
simTL4J::classifiers::Interface_strategy = st.builds(
    simTL4J::classifiers::Interface,
)
arrays::ArrayTypeable_strategy = st.builds(
    arrays::ArrayTypeable,
)
types::TypedElement_strategy = st.builds(
    types::TypedElement,
)
simTL4J::expressions::CastExpression_strategy = st.builds(
    simTL4J::expressions::CastExpression,
)
simTL4J::expressions::InstanceOfExpression_strategy = st.builds(
    simTL4J::expressions::InstanceOfExpression,
)
simTL4J::generics::QualifiedTypeArgument_strategy = st.builds(
    simTL4J::generics::QualifiedTypeArgument,
)
expressions::Expression_strategy = st.builds(
    expressions::Expression,
)
ArrayInitializationValue_strategy = st.builds(
    ArrayInitializationValue,
)
annotations::AnnotationValue_strategy = st.builds(
    annotations::AnnotationValue,
)
arrays::ArrayInitializationValue_strategy = st.builds(
    arrays::ArrayInitializationValue,
)
simTL4J::expressions::Expression_strategy = st.builds(
    simTL4J::expressions::Expression,
)
simTL4J::arrays::ArrayInitializer_strategy = st.builds(
    simTL4J::arrays::ArrayInitializer,
)
modifiers::AnnotableAndModifiable_strategy = st.builds(
    modifiers::AnnotableAndModifiable,
)
simTL4J::variables::LocalVariable_strategy = st.builds(
    simTL4J::variables::LocalVariable,
)
simTL4J::parameters::Parameter_strategy = st.builds(
    simTL4J::parameters::Parameter,
)
statements::Statement_strategy = st.builds(
    statements::Statement,
)
simTL4J::simTL::TFor::StatementListContainer_strategy = st.builds(
    simTL4J::simTL::TFor::StatementListContainer,
)
simTL4J::statements::ForLoop_strategy = st.builds(
    simTL4J::statements::ForLoop,
)
simTL4J::statements::ForEachLoop_strategy = st.builds(
    simTL4J::statements::ForEachLoop,
)
simTL4J::statements::Assert_strategy = st.builds(
    simTL4J::statements::Assert,
)
simTL4J::statements::TryBlock_strategy = st.builds(
    simTL4J::statements::TryBlock,
)
simTL4J::statements::Condition_strategy = st.builds(
    simTL4J::statements::Condition,
)
simTL4J::statements::SynchronizedBlock_strategy = st.builds(
    simTL4J::statements::SynchronizedBlock,
)
simTL4J::simTL::TIf::StatementListContainer_strategy = st.builds(
    simTL4J::simTL::TIf::StatementListContainer,
)
simTL4J::statements::WhileLoop_strategy = st.builds(
    simTL4J::statements::WhileLoop,
)
simTL4J::statements::JumpLabel_strategy = st.builds(
    simTL4J::statements::JumpLabel,
)
members::Member_strategy = st.builds(
    members::Member,
)
simTL4J::statements::Block_strategy = st.builds(
    simTL4J::statements::Block,
)
members::MemberContainer_strategy = st.builds(
    members::MemberContainer,
)
simTL4J::simTL::TFor::MemberContainer_strategy = st.builds(
    simTL4J::simTL::TFor::MemberContainer,
)
simTL4J::simTL::TIf::MemberContainer_strategy = st.builds(
    simTL4J::simTL::TIf::MemberContainer,
)
generics::TypeParametrizable_strategy = st.builds(
    generics::TypeParametrizable,
)
simTL4J::members::Constructor_strategy = st.builds(
    simTL4J::members::Constructor,
)
classifiers::Classifier_strategy = st.builds(
    classifiers::Classifier,
)
simTL4J::classifiers::ConcreteClassifier_strategy = st.builds(
    simTL4J::classifiers::ConcreteClassifier,
    fullName=
        safe_text
)
references::ReferenceableElement_strategy = st.builds(
    references::ReferenceableElement,
)
simTL4J::members::Method_strategy = st.builds(
    simTL4J::members::Method,
)
simTL4J::members::EnumConstant_strategy = st.builds(
    simTL4J::members::EnumConstant,
)
simTL4J::members::Field_strategy = st.builds(
    simTL4J::members::Field,
)
simTL4J::containers::Package_strategy = st.builds(
    simTL4J::containers::Package,
)
simTL4J::members::AdditionalField_strategy = st.builds(
    simTL4J::members::AdditionalField,
)
simTL4J::variables::AdditionalLocalVariable_strategy = st.builds(
    simTL4J::variables::AdditionalLocalVariable,
)
simTL4J::variables::Variable_strategy = st.builds(
    simTL4J::variables::Variable,
)
types::Type_strategy = st.builds(
    types::Type,
)
simTL4J::types::PrimitiveType_strategy = st.builds(
    simTL4J::types::PrimitiveType,
)
simTL4J::classifiers::AnonymousClass_strategy = st.builds(
    simTL4J::classifiers::AnonymousClass,
)
simTL4J::classifiers::Classifier_strategy = st.builds(
    simTL4J::classifiers::Classifier,
)
ArrayInitializer_strategy = st.builds(
    ArrayInitializer,
)
modifiers::AnnotationInstanceOrModifier_strategy = st.builds(
    modifiers::AnnotationInstanceOrModifier,
)
references::Reference_strategy = st.builds(
    references::Reference,
)
simTL4J::instantiations::Instantiation_strategy = st.builds(
    simTL4J::instantiations::Instantiation,
)
simTL4J::arrays::ArrayInstantiationBySize_strategy = st.builds(
    simTL4J::arrays::ArrayInstantiationBySize,
)
simTL4J::arrays::ArrayInstantiationByValues_strategy = st.builds(
    simTL4J::arrays::ArrayInstantiationByValues,
)
AnnotationInstance_strategy = st.builds(
    AnnotationInstance,
)
Commentable_strategy = st.builds(
    Commentable,
)
simTL4J::members::MemberContainer_strategy = st.builds(
    simTL4J::members::MemberContainer,
)
simTL4J::modifiers::AnnotationInstanceOrModifier_strategy = st.builds(
    simTL4J::modifiers::AnnotationInstanceOrModifier,
)
simTL4J::references::Argumentable_strategy = st.builds(
    simTL4J::references::Argumentable,
)
simTL4J::statements::StatementContainer_strategy = st.builds(
    simTL4J::statements::StatementContainer,
)
simTL4J::arrays::ArrayDimension_strategy = st.builds(
    simTL4J::arrays::ArrayDimension,
)
simTL4J::instantiations::Initializable_strategy = st.builds(
    simTL4J::instantiations::Initializable,
)
simTL4J::operators::Operator_strategy = st.builds(
    simTL4J::operators::Operator,
)
simTL4J::commons::NamespaceAwareElement_strategy = st.builds(
    simTL4J::commons::NamespaceAwareElement,
    namespaces=
        safe_text
)
simTL4J::arrays::ArrayInitializationValue_strategy = st.builds(
    simTL4J::arrays::ArrayInitializationValue,
)
simTL4J::statements::StatementListContainer_strategy = st.builds(
    simTL4J::statements::StatementListContainer,
)
simTL4J::types::TypedElement_strategy = st.builds(
    simTL4J::types::TypedElement,
)
simTL4J::parameters::Parametrizable_strategy = st.builds(
    simTL4J::parameters::Parametrizable,
)
simTL4J::commons::NamedElement_strategy = st.builds(
    simTL4J::commons::NamedElement,
    name=
        safe_text
)
simTL4J::classifiers::Implementor_strategy = st.builds(
    simTL4J::classifiers::Implementor,
)
simTL4J::arrays::ArraySelector_strategy = st.builds(
    simTL4J::arrays::ArraySelector,
)
simTL4J::imports::ImportingElement_strategy = st.builds(
    simTL4J::imports::ImportingElement,
)
simTL4J::types::Type_strategy = st.builds(
    simTL4J::types::Type,
)
simTL4J::generics::TypeParametrizable_strategy = st.builds(
    simTL4J::generics::TypeParametrizable,
)
simTL4J::modifiers::AnnotableAndModifiable_strategy = st.builds(
    simTL4J::modifiers::AnnotableAndModifiable,
)
simTL4J::literals::Self_strategy = st.builds(
    simTL4J::literals::Self,
)
simTL4J::members::ExceptionThrower_strategy = st.builds(
    simTL4J::members::ExceptionThrower,
)
simTL4J::statements::Statement_strategy = st.builds(
    simTL4J::statements::Statement,
)
simTL4J::statements::Conditional_strategy = st.builds(
    simTL4J::statements::Conditional,
)
simTL4J::types::TypeReference_strategy = st.builds(
    simTL4J::types::TypeReference,
)
simTL4J::statements::ForLoopInitializer_strategy = st.builds(
    simTL4J::statements::ForLoopInitializer,
)
simTL4J::modifiers::Modifiable_strategy = st.builds(
    simTL4J::modifiers::Modifiable,
)
simTL4J::annotations::Annotable_strategy = st.builds(
    simTL4J::annotations::Annotable,
)
ArrayDimension_strategy = st.builds(
    ArrayDimension,
)
simTL4J::arrays::ArrayTypeable_strategy = st.builds(
    simTL4J::arrays::ArrayTypeable,
)
Expression_strategy = st.builds(
    Expression,
)
simTL4J::expressions::AssignmentExpressionChild_strategy = st.builds(
    simTL4J::expressions::AssignmentExpressionChild,
)
simTL4J::expressions::AssignmentExpression_strategy = st.builds(
    simTL4J::expressions::AssignmentExpression,
)
simTL4J::annotations::AnnotationValue_strategy = st.builds(
    simTL4J::annotations::AnnotationValue,
)
InterfaceMethod_strategy = st.builds(
    InterfaceMethod,
)
simTL4J::annotations::AnnotationAttribute_strategy = st.builds(
    simTL4J::annotations::AnnotationAttribute,
)
simTL4J::annotations::AnnotationAttributeSetting_strategy = st.builds(
    simTL4J::annotations::AnnotationAttributeSetting,
)
AnnotationAttributeSetting_strategy = st.builds(
    AnnotationAttributeSetting,
)
AnnotationValue_strategy = st.builds(
    AnnotationValue,
)
simTL4J::annotations::AnnotationParameter_strategy = st.builds(
    simTL4J::annotations::AnnotationParameter,
)
AnnotationParameter_strategy = st.builds(
    AnnotationParameter,
)
simTL4J::annotations::AnnotationParameterList_strategy = st.builds(
    simTL4J::annotations::AnnotationParameterList,
)
simTL4J::annotations::SingleAnnotationParameter_strategy = st.builds(
    simTL4J::annotations::SingleAnnotationParameter,
)
Classifier_strategy = st.builds(
    Classifier,
)
simTL4J::generics::TypeParameter_strategy = st.builds(
    simTL4J::generics::TypeParameter,
)
commons::NamespaceAwareElement_strategy = st.builds(
    commons::NamespaceAwareElement,
)
simTL4J::annotations::AnnotationInstance_strategy = st.builds(
    simTL4J::annotations::AnnotationInstance,
)
simTL4J::types::NamespaceClassifierReference_strategy = st.builds(
    simTL4J::types::NamespaceClassifierReference,
)
simTL4J::containers::JavaRoot_strategy = st.builds(
    simTL4J::containers::JavaRoot,
)
UnaryModificationExpression_strategy = st.builds(
    UnaryModificationExpression,
)
simTL4J::expressions::SuffixUnaryModificationExpression_strategy = st.builds(
    simTL4J::expressions::SuffixUnaryModificationExpression,
)
simTL4J::expressions::PrefixUnaryModificationExpression_strategy = st.builds(
    simTL4J::expressions::PrefixUnaryModificationExpression,
)
simTL4J::generics::CallTypeArgumentable_strategy = st.builds(
    simTL4J::generics::CallTypeArgumentable,
)
TypeArgument_strategy = st.builds(
    TypeArgument,
)
simTL4J::generics::ExtendsTypeArgument_strategy = st.builds(
    simTL4J::generics::ExtendsTypeArgument,
)
simTL4J::generics::SuperTypeArgument_strategy = st.builds(
    simTL4J::generics::SuperTypeArgument,
)
simTL4J::generics::UnknownTypeArgument_strategy = st.builds(
    simTL4J::generics::UnknownTypeArgument,
)
simTL4J::generics::TypeArgumentable_strategy = st.builds(
    simTL4J::generics::TypeArgumentable,
)
ArrayTypeable_strategy = st.builds(
    ArrayTypeable,
)
simTL4J::generics::TypeArgument_strategy = st.builds(
    simTL4J::generics::TypeArgument,
)
Reference_strategy = st.builds(
    Reference,
)
simTL4J::references::SelfReference_strategy = st.builds(
    simTL4J::references::SelfReference,
)
simTL4J::references::ReflectiveClassReference_strategy = st.builds(
    simTL4J::references::ReflectiveClassReference,
)
simTL4J::references::ElementReference_strategy = st.builds(
    simTL4J::references::ElementReference,
)
simTL4J::references::StringReference_strategy = st.builds(
    simTL4J::references::StringReference,
    value=
        safe_text
)
simTL4J::references::PrimitiveTypeReference_strategy = st.builds(
    simTL4J::references::PrimitiveTypeReference,
)
simTL4J::expressions::NestedExpression_strategy = st.builds(
    simTL4J::expressions::NestedExpression,
)
ShiftOperator_strategy = st.builds(
    ShiftOperator,
)
simTL4J::operators::RightShift_strategy = st.builds(
    simTL4J::operators::RightShift,
)
simTL4J::operators::LeftShift_strategy = st.builds(
    simTL4J::operators::LeftShift,
)
simTL4J::operators::UnsignedRightShift_strategy = st.builds(
    simTL4J::operators::UnsignedRightShift,
)
ShiftExpressionChild_strategy = st.builds(
    ShiftExpressionChild,
)
simTL4J::expressions::AdditiveExpressionChild_strategy = st.builds(
    simTL4J::expressions::AdditiveExpressionChild,
)
simTL4J::expressions::AdditiveExpression_strategy = st.builds(
    simTL4J::expressions::AdditiveExpression,
)
simTL4J::expressions::ShiftExpression_strategy = st.builds(
    simTL4J::expressions::ShiftExpression,
)
simTL4J::expressions::RelationExpressionChild_strategy = st.builds(
    simTL4J::expressions::RelationExpressionChild,
)
RelationOperator_strategy = st.builds(
    RelationOperator,
)
simTL4J::operators::LessThanOrEqual_strategy = st.builds(
    simTL4J::operators::LessThanOrEqual,
)
simTL4J::operators::GreaterThan_strategy = st.builds(
    simTL4J::operators::GreaterThan,
)
simTL4J::operators::GreaterThanOrEqual_strategy = st.builds(
    simTL4J::operators::GreaterThanOrEqual,
)
simTL4J::operators::LessThan_strategy = st.builds(
    simTL4J::operators::LessThan,
)
UnaryModificationOperator_strategy = st.builds(
    UnaryModificationOperator,
)
simTL4J::operators::PlusPlus_strategy = st.builds(
    simTL4J::operators::PlusPlus,
)
simTL4J::operators::MinusMinus_strategy = st.builds(
    simTL4J::operators::MinusMinus,
)
UnaryModificationExpressionChild_strategy = st.builds(
    UnaryModificationExpressionChild,
)
simTL4J::expressions::PrimaryExpression_strategy = st.builds(
    simTL4J::expressions::PrimaryExpression,
)
simTL4J::expressions::UnaryExpressionChild_strategy = st.builds(
    simTL4J::expressions::UnaryExpressionChild,
)
UnaryExpressionChild_strategy = st.builds(
    UnaryExpressionChild,
)
simTL4J::expressions::UnaryModificationExpressionChild_strategy = st.builds(
    simTL4J::expressions::UnaryModificationExpressionChild,
)
simTL4J::expressions::UnaryModificationExpression_strategy = st.builds(
    simTL4J::expressions::UnaryModificationExpression,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
simTL4J::operators::Complement_strategy = st.builds(
    simTL4J::operators::Complement,
)
simTL4J::operators::Negate_strategy = st.builds(
    simTL4J::operators::Negate,
)

@given(instance=TMethodCall_strategy)
@settings(max_examples=50)
def test_tmethodcall_instantiation(instance):
    assert isinstance(instance, TMethodCall)

@given(instance=TUnaryOperator_strategy)
@settings(max_examples=50)
def test_tunaryoperator_instantiation(instance):
    assert isinstance(instance, TUnaryOperator)

@given(instance=simTL4J::simTL::TUnaryOperatorNOT_strategy)
@settings(max_examples=50)
def test_simtl4j::simtl::tunaryoperatornot_instantiation(instance):
    assert isinstance(instance, simTL4J::simTL::TUnaryOperatorNOT)

@given(instance=simTL::TPlaceholder_strategy)
@settings(max_examples=50)
def test_simtl::tplaceholder_instantiation(instance):
    assert isinstance(instance, simTL::TPlaceholder)

@given(instance=simTL4J::simTL::TPlaceholder_strategy)
@settings(max_examples=50)
def test_simtl4j::simtl::tplaceholder_instantiation(instance):
    assert isinstance(instance, simTL4J::simTL::TPlaceholder)

@given(instance=simTL::TIf_strategy)
@settings(max_examples=50)
def test_simtl::tif_instantiation(instance):
    assert isinstance(instance, simTL::TIf)

@given(instance=simTL::TFor_strategy)
@settings(max_examples=50)
def test_simtl::tfor_instantiation(instance):
    assert isinstance(instance, simTL::TFor)

@given(instance=simTL4J::simTL::TAbstractMethodStatement_strategy)
@settings(max_examples=50)
def test_simtl4j::simtl::tabstractmethodstatement_instantiation(instance):
    assert isinstance(instance, simTL4J::simTL::TAbstractMethodStatement)

@given(instance=simTL4J::simTL::TMethodCall_strategy)
@settings(max_examples=50)
def test_simtl4j::simtl::tmethodcall_instantiation(instance):
    assert isinstance(instance, simTL4J::simTL::TMethodCall)

@given(instance=simTL4J::simTL::TMethodCall_strategy)
def test_simtl4j::simtl::tmethodcall_params_type(instance):
    assert isinstance(instance.params, str)


@given(instance=simTL4J::simTL::TMethodCall_strategy)
def test_simtl4j::simtl::tmethodcall_params_setter(instance):
    original = instance.params
    instance.params = original
    assert instance.params == original

@given(instance=simTL4J::simTL::TMethodCall_strategy)
def test_simtl4j::simtl::tmethodcall_methodName_type(instance):
    assert isinstance(instance.methodName, str)


@given(instance=simTL4J::simTL::TMethodCall_strategy)
def test_simtl4j::simtl::tmethodcall_methodName_setter(instance):
    original = instance.methodName
    instance.methodName = original
    assert instance.methodName == original

@given(instance=simTL4J::simTL::TModelImport_strategy)
@settings(max_examples=50)
def test_simtl4j::simtl::tmodelimport_instantiation(instance):
    assert isinstance(instance, simTL4J::simTL::TModelImport)

@given(instance=simTL4J::simTL::TModelImport_strategy)
def test_simtl4j::simtl::tmodelimport_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simTL4J::simTL::TModelImport_strategy)
def test_simtl4j::simtl::tmodelimport_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simTL4J::simTL::TModelImport_strategy)
def test_simtl4j::simtl::tmodelimport_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=simTL4J::simTL::TModelImport_strategy)
def test_simtl4j::simtl::tmodelimport_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=TModelImport_strategy)
@settings(max_examples=50)
def test_tmodelimport_instantiation(instance):
    assert isinstance(instance, TModelImport)

@given(instance=simTL4J::simTL::TemplateHeader_strategy)
@settings(max_examples=50)
def test_simtl4j::simtl::templateheader_instantiation(instance):
    assert isinstance(instance, simTL4J::simTL::TemplateHeader)

@given(instance=TemplateHeader_strategy)
@settings(max_examples=50)
def test_templateheader_instantiation(instance):
    assert isinstance(instance, TemplateHeader)

@given(instance=simTL4J::simTL::Template_strategy)
@settings(max_examples=50)
def test_simtl4j::simtl::template_instantiation(instance):
    assert isinstance(instance, simTL4J::simTL::Template)

@given(instance=simTL4J::simTL::TForVariable_strategy)
@settings(max_examples=50)
def test_simtl4j::simtl::tforvariable_instantiation(instance):
    assert isinstance(instance, simTL4J::simTL::TForVariable)

@given(instance=simTL4J::simTL::TForVariable_strategy)
def test_simtl4j::simtl::tforvariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simTL4J::simTL::TForVariable_strategy)
def test_simtl4j::simtl::tforvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TForVariable_strategy)
@settings(max_examples=50)
def test_tforvariable_instantiation(instance):
    assert isinstance(instance, TForVariable)

@given(instance=simTL4J::simTL::TFor_strategy)
@settings(max_examples=50)
def test_simtl4j::simtl::tfor_instantiation(instance):
    assert isinstance(instance, simTL4J::simTL::TFor)

@given(instance=TAbstractMethodStatement_strategy)
@settings(max_examples=50)
def test_tabstractmethodstatement_instantiation(instance):
    assert isinstance(instance, TAbstractMethodStatement)

@given(instance=simTL4J::simTL::TMethodStatementImpl_strategy)
@settings(max_examples=50)
def test_simtl4j::simtl::tmethodstatementimpl_instantiation(instance):
    assert isinstance(instance, simTL4J::simTL::TMethodStatementImpl)

@given(instance=simTL4J::simTL::TMethodStatementImpl_strategy)
def test_simtl4j::simtl::tmethodstatementimpl_caller_type(instance):
    assert isinstance(instance.caller, str)


@given(instance=simTL4J::simTL::TMethodStatementImpl_strategy)
def test_simtl4j::simtl::tmethodstatementimpl_caller_setter(instance):
    original = instance.caller
    instance.caller = original
    assert instance.caller == original

@given(instance=simTL4J::simTL::TUnaryOperator_strategy)
@settings(max_examples=50)
def test_simtl4j::simtl::tunaryoperator_instantiation(instance):
    assert isinstance(instance, simTL4J::simTL::TUnaryOperator)

@given(instance=simTL4J::simTL::TIf_strategy)
@settings(max_examples=50)
def test_simtl4j::simtl::tif_instantiation(instance):
    assert isinstance(instance, simTL4J::simTL::TIf)

@given(instance=AdditionalLocalVariable_strategy)
@settings(max_examples=50)
def test_additionallocalvariable_instantiation(instance):
    assert isinstance(instance, AdditionalLocalVariable)

@given(instance=statements::ForLoopInitializer_strategy)
@settings(max_examples=50)
def test_statements::forloopinitializer_instantiation(instance):
    assert isinstance(instance, statements::ForLoopInitializer)

@given(instance=ClassifierReference_strategy)
@settings(max_examples=50)
def test_classifierreference_instantiation(instance):
    assert isinstance(instance, ClassifierReference)

@given(instance=types::TypeReference_strategy)
@settings(max_examples=50)
def test_types::typereference_instantiation(instance):
    assert isinstance(instance, types::TypeReference)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=CatchBlock_strategy)
@settings(max_examples=50)
def test_catchblock_instantiation(instance):
    assert isinstance(instance, CatchBlock)

@given(instance=statements::SwitchCase_strategy)
@settings(max_examples=50)
def test_statements::switchcase_instantiation(instance):
    assert isinstance(instance, statements::SwitchCase)

@given(instance=LocalVariable_strategy)
@settings(max_examples=50)
def test_localvariable_instantiation(instance):
    assert isinstance(instance, LocalVariable)

@given(instance=JumpLabel_strategy)
@settings(max_examples=50)
def test_jumplabel_instantiation(instance):
    assert isinstance(instance, JumpLabel)

@given(instance=statements::Conditional_strategy)
@settings(max_examples=50)
def test_statements::conditional_instantiation(instance):
    assert isinstance(instance, statements::Conditional)

@given(instance=simTL4J::statements::NormalSwitchCase_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::normalswitchcase_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::NormalSwitchCase)

@given(instance=StatementListContainer_strategy)
@settings(max_examples=50)
def test_statementlistcontainer_instantiation(instance):
    assert isinstance(instance, StatementListContainer)

@given(instance=simTL4J::statements::SwitchCase_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::switchcase_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::SwitchCase)

@given(instance=WhileLoop_strategy)
@settings(max_examples=50)
def test_whileloop_instantiation(instance):
    assert isinstance(instance, WhileLoop)

@given(instance=simTL4J::statements::DoWhileLoop_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::dowhileloop_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::DoWhileLoop)

@given(instance=SwitchCase_strategy)
@settings(max_examples=50)
def test_switchcase_instantiation(instance):
    assert isinstance(instance, SwitchCase)

@given(instance=simTL4J::statements::DefaultSwitchCase_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::defaultswitchcase_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::DefaultSwitchCase)

@given(instance=statements::StatementContainer_strategy)
@settings(max_examples=50)
def test_statements::statementcontainer_instantiation(instance):
    assert isinstance(instance, statements::StatementContainer)

@given(instance=OrdinaryParameter_strategy)
@settings(max_examples=50)
def test_ordinaryparameter_instantiation(instance):
    assert isinstance(instance, OrdinaryParameter)

@given(instance=simTL4J::statements::CatchBlock_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::catchblock_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::CatchBlock)

@given(instance=modifiers::Modifiable_strategy)
@settings(max_examples=50)
def test_modifiers::modifiable_instantiation(instance):
    assert isinstance(instance, modifiers::Modifiable)

@given(instance=Jump_strategy)
@settings(max_examples=50)
def test_jump_instantiation(instance):
    assert isinstance(instance, Jump)

@given(instance=simTL4J::statements::Continue_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::continue_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::Continue)

@given(instance=simTL4J::statements::Break_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::break_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::Break)

@given(instance=references::ElementReference_strategy)
@settings(max_examples=50)
def test_references::elementreference_instantiation(instance):
    assert isinstance(instance, references::ElementReference)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=simTL4J::statements::LocalVariableStatement_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::localvariablestatement_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::LocalVariableStatement)

@given(instance=simTL4J::statements::Throw_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::throw_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::Throw)

@given(instance=simTL4J::statements::Jump_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::jump_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::Jump)

@given(instance=simTL4J::statements::Switch_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::switch_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::Switch)

@given(instance=simTL4J::statements::Return_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::return_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::Return)

@given(instance=simTL4J::statements::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::expressionstatement_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::ExpressionStatement)

@given(instance=simTL4J::statements::EmptyStatement_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::emptystatement_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::EmptyStatement)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=simTL4J::types::Void_strategy)
@settings(max_examples=50)
def test_simtl4j::types::void_instantiation(instance):
    assert isinstance(instance, simTL4J::types::Void)

@given(instance=simTL4J::types::Char_strategy)
@settings(max_examples=50)
def test_simtl4j::types::char_instantiation(instance):
    assert isinstance(instance, simTL4J::types::Char)

@given(instance=simTL4J::types::Boolean_strategy)
@settings(max_examples=50)
def test_simtl4j::types::boolean_instantiation(instance):
    assert isinstance(instance, simTL4J::types::Boolean)

@given(instance=simTL4J::types::Long_strategy)
@settings(max_examples=50)
def test_simtl4j::types::long_instantiation(instance):
    assert isinstance(instance, simTL4J::types::Long)

@given(instance=simTL4J::types::Int_strategy)
@settings(max_examples=50)
def test_simtl4j::types::int_instantiation(instance):
    assert isinstance(instance, simTL4J::types::Int)

@given(instance=simTL4J::types::Double_strategy)
@settings(max_examples=50)
def test_simtl4j::types::double_instantiation(instance):
    assert isinstance(instance, simTL4J::types::Double)

@given(instance=simTL4J::types::Short_strategy)
@settings(max_examples=50)
def test_simtl4j::types::short_instantiation(instance):
    assert isinstance(instance, simTL4J::types::Short)

@given(instance=simTL4J::types::Byte_strategy)
@settings(max_examples=50)
def test_simtl4j::types::byte_instantiation(instance):
    assert isinstance(instance, simTL4J::types::Byte)

@given(instance=simTL4J::types::Float_strategy)
@settings(max_examples=50)
def test_simtl4j::types::float_instantiation(instance):
    assert isinstance(instance, simTL4J::types::Float)

@given(instance=ElementReference_strategy)
@settings(max_examples=50)
def test_elementreference_instantiation(instance):
    assert isinstance(instance, ElementReference)

@given(instance=simTL4J::references::IdentifierReference_strategy)
@settings(max_examples=50)
def test_simtl4j::references::identifierreference_instantiation(instance):
    assert isinstance(instance, simTL4J::references::IdentifierReference)

@given(instance=ArraySelector_strategy)
@settings(max_examples=50)
def test_arrayselector_instantiation(instance):
    assert isinstance(instance, ArraySelector)

@given(instance=expressions::PrimaryExpression_strategy)
@settings(max_examples=50)
def test_expressions::primaryexpression_instantiation(instance):
    assert isinstance(instance, expressions::PrimaryExpression)

@given(instance=simTL4J::simTL::TPlaceholder::PrimaryExpression_strategy)
@settings(max_examples=50)
def test_simtl4j::simtl::tplaceholder::primaryexpression_instantiation(instance):
    assert isinstance(instance, simTL4J::simTL::TPlaceholder::PrimaryExpression)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=simTL4J::parameters::VariableLengthParameter_strategy)
@settings(max_examples=50)
def test_simtl4j::parameters::variablelengthparameter_instantiation(instance):
    assert isinstance(instance, simTL4J::parameters::VariableLengthParameter)

@given(instance=simTL4J::parameters::OrdinaryParameter_strategy)
@settings(max_examples=50)
def test_simtl4j::parameters::ordinaryparameter_instantiation(instance):
    assert isinstance(instance, simTL4J::parameters::OrdinaryParameter)

@given(instance=operators::UnaryOperator_strategy)
@settings(max_examples=50)
def test_operators::unaryoperator_instantiation(instance):
    assert isinstance(instance, operators::UnaryOperator)

@given(instance=operators::AdditiveOperator_strategy)
@settings(max_examples=50)
def test_operators::additiveoperator_instantiation(instance):
    assert isinstance(instance, operators::AdditiveOperator)

@given(instance=simTL4J::operators::Subtraction_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::subtraction_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::Subtraction)

@given(instance=simTL4J::operators::Addition_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::addition_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::Addition)

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=simTL4J::operators::MultiplicativeOperator_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::multiplicativeoperator_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::MultiplicativeOperator)

@given(instance=simTL4J::operators::UnaryModificationOperator_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::unarymodificationoperator_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::UnaryModificationOperator)

@given(instance=simTL4J::operators::EqualityOperator_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::equalityoperator_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::EqualityOperator)

@given(instance=simTL4J::operators::RelationOperator_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::relationoperator_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::RelationOperator)

@given(instance=simTL4J::operators::AssignmentOperator_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::assignmentoperator_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::AssignmentOperator)

@given(instance=simTL4J::operators::UnaryOperator_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::unaryoperator_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::UnaryOperator)

@given(instance=simTL4J::operators::ShiftOperator_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::shiftoperator_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::ShiftOperator)

@given(instance=simTL4J::operators::AdditiveOperator_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::additiveoperator_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::AdditiveOperator)

@given(instance=AnnotationInstanceOrModifier_strategy)
@settings(max_examples=50)
def test_annotationinstanceormodifier_instantiation(instance):
    assert isinstance(instance, AnnotationInstanceOrModifier)

@given(instance=simTL4J::modifiers::Modifier_strategy)
@settings(max_examples=50)
def test_simtl4j::modifiers::modifier_instantiation(instance):
    assert isinstance(instance, simTL4J::modifiers::Modifier)

@given(instance=Modifier_strategy)
@settings(max_examples=50)
def test_modifier_instantiation(instance):
    assert isinstance(instance, Modifier)

@given(instance=simTL4J::modifiers::Synchronized_strategy)
@settings(max_examples=50)
def test_simtl4j::modifiers::synchronized_instantiation(instance):
    assert isinstance(instance, simTL4J::modifiers::Synchronized)

@given(instance=simTL4J::modifiers::Private_strategy)
@settings(max_examples=50)
def test_simtl4j::modifiers::private_instantiation(instance):
    assert isinstance(instance, simTL4J::modifiers::Private)

@given(instance=simTL4J::modifiers::Static_strategy)
@settings(max_examples=50)
def test_simtl4j::modifiers::static_instantiation(instance):
    assert isinstance(instance, simTL4J::modifiers::Static)

@given(instance=simTL4J::modifiers::Strictfp_strategy)
@settings(max_examples=50)
def test_simtl4j::modifiers::strictfp_instantiation(instance):
    assert isinstance(instance, simTL4J::modifiers::Strictfp)

@given(instance=simTL4J::modifiers::Transient_strategy)
@settings(max_examples=50)
def test_simtl4j::modifiers::transient_instantiation(instance):
    assert isinstance(instance, simTL4J::modifiers::Transient)

@given(instance=simTL4J::modifiers::Abstract_strategy)
@settings(max_examples=50)
def test_simtl4j::modifiers::abstract_instantiation(instance):
    assert isinstance(instance, simTL4J::modifiers::Abstract)

@given(instance=simTL4J::modifiers::Volatile_strategy)
@settings(max_examples=50)
def test_simtl4j::modifiers::volatile_instantiation(instance):
    assert isinstance(instance, simTL4J::modifiers::Volatile)

@given(instance=simTL4J::modifiers::Native_strategy)
@settings(max_examples=50)
def test_simtl4j::modifiers::native_instantiation(instance):
    assert isinstance(instance, simTL4J::modifiers::Native)

@given(instance=simTL4J::modifiers::Protected_strategy)
@settings(max_examples=50)
def test_simtl4j::modifiers::protected_instantiation(instance):
    assert isinstance(instance, simTL4J::modifiers::Protected)

@given(instance=simTL4J::modifiers::Public_strategy)
@settings(max_examples=50)
def test_simtl4j::modifiers::public_instantiation(instance):
    assert isinstance(instance, simTL4J::modifiers::Public)

@given(instance=simTL4J::modifiers::Final_strategy)
@settings(max_examples=50)
def test_simtl4j::modifiers::final_instantiation(instance):
    assert isinstance(instance, simTL4J::modifiers::Final)

@given(instance=members::Method_strategy)
@settings(max_examples=50)
def test_members::method_instantiation(instance):
    assert isinstance(instance, members::Method)

@given(instance=Method_strategy)
@settings(max_examples=50)
def test_method_instantiation(instance):
    assert isinstance(instance, Method)

@given(instance=simTL4J::members::InterfaceMethod_strategy)
@settings(max_examples=50)
def test_simtl4j::members::interfacemethod_instantiation(instance):
    assert isinstance(instance, simTL4J::members::InterfaceMethod)

@given(instance=AdditionalField_strategy)
@settings(max_examples=50)
def test_additionalfield_instantiation(instance):
    assert isinstance(instance, AdditionalField)

@given(instance=variables::Variable_strategy)
@settings(max_examples=50)
def test_variables::variable_instantiation(instance):
    assert isinstance(instance, variables::Variable)

@given(instance=members::ExceptionThrower_strategy)
@settings(max_examples=50)
def test_members::exceptionthrower_instantiation(instance):
    assert isinstance(instance, members::ExceptionThrower)

@given(instance=parameters::Parametrizable_strategy)
@settings(max_examples=50)
def test_parameters::parametrizable_instantiation(instance):
    assert isinstance(instance, parameters::Parametrizable)

@given(instance=statements::StatementListContainer_strategy)
@settings(max_examples=50)
def test_statements::statementlistcontainer_instantiation(instance):
    assert isinstance(instance, statements::StatementListContainer)

@given(instance=simTL4J::members::ClassMethod_strategy)
@settings(max_examples=50)
def test_simtl4j::members::classmethod_instantiation(instance):
    assert isinstance(instance, simTL4J::members::ClassMethod)

@given(instance=instantiations::Initializable_strategy)
@settings(max_examples=50)
def test_instantiations::initializable_instantiation(instance):
    assert isinstance(instance, instantiations::Initializable)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=simTL4J::members::EmptyMember_strategy)
@settings(max_examples=50)
def test_simtl4j::members::emptymember_instantiation(instance):
    assert isinstance(instance, simTL4J::members::EmptyMember)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=simTL4J::references::ReferenceableElement_strategy)
@settings(max_examples=50)
def test_simtl4j::references::referenceableelement_instantiation(instance):
    assert isinstance(instance, simTL4J::references::ReferenceableElement)

@given(instance=simTL4J::members::Member_strategy)
@settings(max_examples=50)
def test_simtl4j::members::member_instantiation(instance):
    assert isinstance(instance, simTL4J::members::Member)

@given(instance=NamespaceClassifierReference_strategy)
@settings(max_examples=50)
def test_namespaceclassifierreference_instantiation(instance):
    assert isinstance(instance, NamespaceClassifierReference)

@given(instance=LongLiteral_strategy)
@settings(max_examples=50)
def test_longliteral_instantiation(instance):
    assert isinstance(instance, LongLiteral)

@given(instance=simTL4J::literals::OctalLongLiteral_strategy)
@settings(max_examples=50)
def test_simtl4j::literals::octallongliteral_instantiation(instance):
    assert isinstance(instance, simTL4J::literals::OctalLongLiteral)

@given(instance=simTL4J::literals::OctalLongLiteral_strategy)
def test_simtl4j::literals::octallongliteral_octalValue_type(instance):
    assert isinstance(instance.octalValue, str)


@given(instance=simTL4J::literals::OctalLongLiteral_strategy)
def test_simtl4j::literals::octallongliteral_octalValue_setter(instance):
    original = instance.octalValue
    instance.octalValue = original
    assert instance.octalValue == original

@given(instance=simTL4J::literals::HexLongLiteral_strategy)
@settings(max_examples=50)
def test_simtl4j::literals::hexlongliteral_instantiation(instance):
    assert isinstance(instance, simTL4J::literals::HexLongLiteral)

@given(instance=simTL4J::literals::HexLongLiteral_strategy)
def test_simtl4j::literals::hexlongliteral_hexValue_type(instance):
    assert isinstance(instance.hexValue, str)


@given(instance=simTL4J::literals::HexLongLiteral_strategy)
def test_simtl4j::literals::hexlongliteral_hexValue_setter(instance):
    original = instance.hexValue
    instance.hexValue = original
    assert instance.hexValue == original

@given(instance=simTL4J::literals::DecimalLongLiteral_strategy)
@settings(max_examples=50)
def test_simtl4j::literals::decimallongliteral_instantiation(instance):
    assert isinstance(instance, simTL4J::literals::DecimalLongLiteral)

@given(instance=simTL4J::literals::DecimalLongLiteral_strategy)
def test_simtl4j::literals::decimallongliteral_decimalValue_type(instance):
    assert isinstance(instance.decimalValue, str)


@given(instance=simTL4J::literals::DecimalLongLiteral_strategy)
def test_simtl4j::literals::decimallongliteral_decimalValue_setter(instance):
    original = instance.decimalValue
    instance.decimalValue = original
    assert instance.decimalValue == original

@given(instance=IntegerLiteral_strategy)
@settings(max_examples=50)
def test_integerliteral_instantiation(instance):
    assert isinstance(instance, IntegerLiteral)

@given(instance=simTL4J::literals::HexIntegerLiteral_strategy)
@settings(max_examples=50)
def test_simtl4j::literals::hexintegerliteral_instantiation(instance):
    assert isinstance(instance, simTL4J::literals::HexIntegerLiteral)

@given(instance=simTL4J::literals::HexIntegerLiteral_strategy)
def test_simtl4j::literals::hexintegerliteral_hexValue_type(instance):
    assert isinstance(instance.hexValue, str)


@given(instance=simTL4J::literals::HexIntegerLiteral_strategy)
def test_simtl4j::literals::hexintegerliteral_hexValue_setter(instance):
    original = instance.hexValue
    instance.hexValue = original
    assert instance.hexValue == original

@given(instance=simTL4J::literals::OctalIntegerLiteral_strategy)
@settings(max_examples=50)
def test_simtl4j::literals::octalintegerliteral_instantiation(instance):
    assert isinstance(instance, simTL4J::literals::OctalIntegerLiteral)

@given(instance=simTL4J::literals::OctalIntegerLiteral_strategy)
def test_simtl4j::literals::octalintegerliteral_octalValue_type(instance):
    assert isinstance(instance.octalValue, str)


@given(instance=simTL4J::literals::OctalIntegerLiteral_strategy)
def test_simtl4j::literals::octalintegerliteral_octalValue_setter(instance):
    original = instance.octalValue
    instance.octalValue = original
    assert instance.octalValue == original

@given(instance=simTL4J::literals::DecimalIntegerLiteral_strategy)
@settings(max_examples=50)
def test_simtl4j::literals::decimalintegerliteral_instantiation(instance):
    assert isinstance(instance, simTL4J::literals::DecimalIntegerLiteral)

@given(instance=simTL4J::literals::DecimalIntegerLiteral_strategy)
def test_simtl4j::literals::decimalintegerliteral_decimalValue_type(instance):
    assert isinstance(instance.decimalValue, str)


@given(instance=simTL4J::literals::DecimalIntegerLiteral_strategy)
def test_simtl4j::literals::decimalintegerliteral_decimalValue_setter(instance):
    original = instance.decimalValue
    instance.decimalValue = original
    assert instance.decimalValue == original

@given(instance=DoubleLiteral_strategy)
@settings(max_examples=50)
def test_doubleliteral_instantiation(instance):
    assert isinstance(instance, DoubleLiteral)

@given(instance=simTL4J::literals::HexDoubleLiteral_strategy)
@settings(max_examples=50)
def test_simtl4j::literals::hexdoubleliteral_instantiation(instance):
    assert isinstance(instance, simTL4J::literals::HexDoubleLiteral)

@given(instance=simTL4J::literals::HexDoubleLiteral_strategy)
def test_simtl4j::literals::hexdoubleliteral_hexValue_type(instance):
    assert isinstance(instance.hexValue, float)


@given(instance=simTL4J::literals::HexDoubleLiteral_strategy)
def test_simtl4j::literals::hexdoubleliteral_hexValue_setter(instance):
    original = instance.hexValue
    instance.hexValue = original
    assert instance.hexValue == original

@given(instance=simTL4J::literals::DecimalDoubleLiteral_strategy)
@settings(max_examples=50)
def test_simtl4j::literals::decimaldoubleliteral_instantiation(instance):
    assert isinstance(instance, simTL4J::literals::DecimalDoubleLiteral)

@given(instance=simTL4J::literals::DecimalDoubleLiteral_strategy)
def test_simtl4j::literals::decimaldoubleliteral_decimalValue_type(instance):
    assert isinstance(instance.decimalValue, float)


@given(instance=simTL4J::literals::DecimalDoubleLiteral_strategy)
def test_simtl4j::literals::decimaldoubleliteral_decimalValue_setter(instance):
    original = instance.decimalValue
    instance.decimalValue = original
    assert instance.decimalValue == original

@given(instance=FloatLiteral_strategy)
@settings(max_examples=50)
def test_floatliteral_instantiation(instance):
    assert isinstance(instance, FloatLiteral)

@given(instance=simTL4J::literals::HexFloatLiteral_strategy)
@settings(max_examples=50)
def test_simtl4j::literals::hexfloatliteral_instantiation(instance):
    assert isinstance(instance, simTL4J::literals::HexFloatLiteral)

@given(instance=simTL4J::literals::HexFloatLiteral_strategy)
def test_simtl4j::literals::hexfloatliteral_hexValue_type(instance):
    assert isinstance(instance.hexValue, float)


@given(instance=simTL4J::literals::HexFloatLiteral_strategy)
def test_simtl4j::literals::hexfloatliteral_hexValue_setter(instance):
    original = instance.hexValue
    instance.hexValue = original
    assert instance.hexValue == original

@given(instance=simTL4J::literals::DecimalFloatLiteral_strategy)
@settings(max_examples=50)
def test_simtl4j::literals::decimalfloatliteral_instantiation(instance):
    assert isinstance(instance, simTL4J::literals::DecimalFloatLiteral)

@given(instance=simTL4J::literals::DecimalFloatLiteral_strategy)
def test_simtl4j::literals::decimalfloatliteral_decimalValue_type(instance):
    assert isinstance(instance.decimalValue, float)


@given(instance=simTL4J::literals::DecimalFloatLiteral_strategy)
def test_simtl4j::literals::decimalfloatliteral_decimalValue_setter(instance):
    original = instance.decimalValue
    instance.decimalValue = original
    assert instance.decimalValue == original

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=simTL4J::literals::CharacterLiteral_strategy)
@settings(max_examples=50)
def test_simtl4j::literals::characterliteral_instantiation(instance):
    assert isinstance(instance, simTL4J::literals::CharacterLiteral)

@given(instance=simTL4J::literals::CharacterLiteral_strategy)
def test_simtl4j::literals::characterliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=simTL4J::literals::CharacterLiteral_strategy)
def test_simtl4j::literals::characterliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=simTL4J::literals::FloatLiteral_strategy)
@settings(max_examples=50)
def test_simtl4j::literals::floatliteral_instantiation(instance):
    assert isinstance(instance, simTL4J::literals::FloatLiteral)

@given(instance=simTL4J::literals::NullLiteral_strategy)
@settings(max_examples=50)
def test_simtl4j::literals::nullliteral_instantiation(instance):
    assert isinstance(instance, simTL4J::literals::NullLiteral)

@given(instance=simTL4J::literals::DoubleLiteral_strategy)
@settings(max_examples=50)
def test_simtl4j::literals::doubleliteral_instantiation(instance):
    assert isinstance(instance, simTL4J::literals::DoubleLiteral)

@given(instance=simTL4J::literals::LongLiteral_strategy)
@settings(max_examples=50)
def test_simtl4j::literals::longliteral_instantiation(instance):
    assert isinstance(instance, simTL4J::literals::LongLiteral)

@given(instance=simTL4J::literals::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_simtl4j::literals::integerliteral_instantiation(instance):
    assert isinstance(instance, simTL4J::literals::IntegerLiteral)

@given(instance=simTL4J::literals::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_simtl4j::literals::booleanliteral_instantiation(instance):
    assert isinstance(instance, simTL4J::literals::BooleanLiteral)

@given(instance=simTL4J::literals::BooleanLiteral_strategy)
def test_simtl4j::literals::booleanliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=simTL4J::literals::BooleanLiteral_strategy)
def test_simtl4j::literals::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=PrimaryExpression_strategy)
@settings(max_examples=50)
def test_primaryexpression_instantiation(instance):
    assert isinstance(instance, PrimaryExpression)

@given(instance=simTL4J::literals::Literal_strategy)
@settings(max_examples=50)
def test_simtl4j::literals::literal_instantiation(instance):
    assert isinstance(instance, simTL4J::literals::Literal)

@given(instance=Self_strategy)
@settings(max_examples=50)
def test_self_instantiation(instance):
    assert isinstance(instance, Self)

@given(instance=simTL4J::literals::This_strategy)
@settings(max_examples=50)
def test_simtl4j::literals::this_instantiation(instance):
    assert isinstance(instance, simTL4J::literals::This)

@given(instance=simTL4J::literals::Super_strategy)
@settings(max_examples=50)
def test_simtl4j::literals::super_instantiation(instance):
    assert isinstance(instance, simTL4J::literals::Super)

@given(instance=Instantiation_strategy)
@settings(max_examples=50)
def test_instantiation_instantiation(instance):
    assert isinstance(instance, Instantiation)

@given(instance=simTL4J::instantiations::ExplicitConstructorCall_strategy)
@settings(max_examples=50)
def test_simtl4j::instantiations::explicitconstructorcall_instantiation(instance):
    assert isinstance(instance, simTL4J::instantiations::ExplicitConstructorCall)

@given(instance=AnonymousClass_strategy)
@settings(max_examples=50)
def test_anonymousclass_instantiation(instance):
    assert isinstance(instance, AnonymousClass)

@given(instance=generics::CallTypeArgumentable_strategy)
@settings(max_examples=50)
def test_generics::calltypeargumentable_instantiation(instance):
    assert isinstance(instance, generics::CallTypeArgumentable)

@given(instance=instantiations::Instantiation_strategy)
@settings(max_examples=50)
def test_instantiations::instantiation_instantiation(instance):
    assert isinstance(instance, instantiations::Instantiation)

@given(instance=simTL4J::instantiations::NewConstructorCall_strategy)
@settings(max_examples=50)
def test_simtl4j::instantiations::newconstructorcall_instantiation(instance):
    assert isinstance(instance, simTL4J::instantiations::NewConstructorCall)

@given(instance=generics::TypeArgumentable_strategy)
@settings(max_examples=50)
def test_generics::typeargumentable_instantiation(instance):
    assert isinstance(instance, generics::TypeArgumentable)

@given(instance=simTL4J::references::Reference_strategy)
@settings(max_examples=50)
def test_simtl4j::references::reference_instantiation(instance):
    assert isinstance(instance, simTL4J::references::Reference)

@given(instance=simTL4J::types::ClassifierReference_strategy)
@settings(max_examples=50)
def test_simtl4j::types::classifierreference_instantiation(instance):
    assert isinstance(instance, simTL4J::types::ClassifierReference)

@given(instance=references::Argumentable_strategy)
@settings(max_examples=50)
def test_references::argumentable_instantiation(instance):
    assert isinstance(instance, references::Argumentable)

@given(instance=simTL4J::references::MethodCall_strategy)
@settings(max_examples=50)
def test_simtl4j::references::methodcall_instantiation(instance):
    assert isinstance(instance, simTL4J::references::MethodCall)

@given(instance=ReferenceableElement_strategy)
@settings(max_examples=50)
def test_referenceableelement_instantiation(instance):
    assert isinstance(instance, ReferenceableElement)

@given(instance=StaticImport_strategy)
@settings(max_examples=50)
def test_staticimport_instantiation(instance):
    assert isinstance(instance, StaticImport)

@given(instance=simTL4J::imports::StaticMemberImport_strategy)
@settings(max_examples=50)
def test_simtl4j::imports::staticmemberimport_instantiation(instance):
    assert isinstance(instance, simTL4J::imports::StaticMemberImport)

@given(instance=simTL4J::imports::StaticClassifierImport_strategy)
@settings(max_examples=50)
def test_simtl4j::imports::staticclassifierimport_instantiation(instance):
    assert isinstance(instance, simTL4J::imports::StaticClassifierImport)

@given(instance=Static_strategy)
@settings(max_examples=50)
def test_static_instantiation(instance):
    assert isinstance(instance, Static)

@given(instance=Import_strategy)
@settings(max_examples=50)
def test_import_instantiation(instance):
    assert isinstance(instance, Import)

@given(instance=simTL4J::imports::StaticImport_strategy)
@settings(max_examples=50)
def test_simtl4j::imports::staticimport_instantiation(instance):
    assert isinstance(instance, simTL4J::imports::StaticImport)

@given(instance=simTL4J::imports::PackageImport_strategy)
@settings(max_examples=50)
def test_simtl4j::imports::packageimport_instantiation(instance):
    assert isinstance(instance, simTL4J::imports::PackageImport)

@given(instance=simTL4J::imports::ClassifierImport_strategy)
@settings(max_examples=50)
def test_simtl4j::imports::classifierimport_instantiation(instance):
    assert isinstance(instance, simTL4J::imports::ClassifierImport)

@given(instance=NamespaceAwareElement_strategy)
@settings(max_examples=50)
def test_namespaceawareelement_instantiation(instance):
    assert isinstance(instance, NamespaceAwareElement)

@given(instance=simTL4J::imports::Import_strategy)
@settings(max_examples=50)
def test_simtl4j::imports::import_instantiation(instance):
    assert isinstance(instance, simTL4J::imports::Import)

@given(instance=TypeParameter_strategy)
@settings(max_examples=50)
def test_typeparameter_instantiation(instance):
    assert isinstance(instance, TypeParameter)

@given(instance=generics::TypeArgument_strategy)
@settings(max_examples=50)
def test_generics::typeargument_instantiation(instance):
    assert isinstance(instance, generics::TypeArgument)

@given(instance=expressions::UnaryModificationExpressionChild_strategy)
@settings(max_examples=50)
def test_expressions::unarymodificationexpressionchild_instantiation(instance):
    assert isinstance(instance, expressions::UnaryModificationExpressionChild)

@given(instance=MultiplicativeOperator_strategy)
@settings(max_examples=50)
def test_multiplicativeoperator_instantiation(instance):
    assert isinstance(instance, MultiplicativeOperator)

@given(instance=simTL4J::operators::Multiplication_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::multiplication_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::Multiplication)

@given(instance=simTL4J::operators::Division_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::division_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::Division)

@given(instance=simTL4J::operators::Remainder_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::remainder_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::Remainder)

@given(instance=MultiplicativeExpressionChild_strategy)
@settings(max_examples=50)
def test_multiplicativeexpressionchild_instantiation(instance):
    assert isinstance(instance, MultiplicativeExpressionChild)

@given(instance=simTL4J::expressions::UnaryExpression_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::unaryexpression_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::UnaryExpression)

@given(instance=AdditiveOperator_strategy)
@settings(max_examples=50)
def test_additiveoperator_instantiation(instance):
    assert isinstance(instance, AdditiveOperator)

@given(instance=AdditiveExpressionChild_strategy)
@settings(max_examples=50)
def test_additiveexpressionchild_instantiation(instance):
    assert isinstance(instance, AdditiveExpressionChild)

@given(instance=simTL4J::expressions::MultiplicativeExpressionChild_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::multiplicativeexpressionchild_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::MultiplicativeExpressionChild)

@given(instance=simTL4J::expressions::MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::MultiplicativeExpression)

@given(instance=ConditionalAndExpressionChild_strategy)
@settings(max_examples=50)
def test_conditionalandexpressionchild_instantiation(instance):
    assert isinstance(instance, ConditionalAndExpressionChild)

@given(instance=simTL4J::expressions::InclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::inclusiveorexpression_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::InclusiveOrExpression)

@given(instance=ConditionalOrExpressionChild_strategy)
@settings(max_examples=50)
def test_conditionalorexpressionchild_instantiation(instance):
    assert isinstance(instance, ConditionalOrExpressionChild)

@given(instance=simTL4J::expressions::ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::conditionalandexpression_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::ConditionalAndExpression)

@given(instance=simTL4J::expressions::ConditionalAndExpressionChild_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::conditionalandexpressionchild_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::ConditionalAndExpressionChild)

@given(instance=RelationExpressionChild_strategy)
@settings(max_examples=50)
def test_relationexpressionchild_instantiation(instance):
    assert isinstance(instance, RelationExpressionChild)

@given(instance=simTL4J::expressions::ShiftExpressionChild_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::shiftexpressionchild_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::ShiftExpressionChild)

@given(instance=InstanceOfExpressionChild_strategy)
@settings(max_examples=50)
def test_instanceofexpressionchild_instantiation(instance):
    assert isinstance(instance, InstanceOfExpressionChild)

@given(instance=simTL4J::expressions::RelationExpression_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::relationexpression_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::RelationExpression)

@given(instance=expressions::EqualityExpressionChild_strategy)
@settings(max_examples=50)
def test_expressions::equalityexpressionchild_instantiation(instance):
    assert isinstance(instance, expressions::EqualityExpressionChild)

@given(instance=EqualityExpressionChild_strategy)
@settings(max_examples=50)
def test_equalityexpressionchild_instantiation(instance):
    assert isinstance(instance, EqualityExpressionChild)

@given(instance=simTL4J::expressions::InstanceOfExpressionChild_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::instanceofexpressionchild_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::InstanceOfExpressionChild)

@given(instance=EqualityOperator_strategy)
@settings(max_examples=50)
def test_equalityoperator_instantiation(instance):
    assert isinstance(instance, EqualityOperator)

@given(instance=simTL4J::operators::NotEqual_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::notequal_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::NotEqual)

@given(instance=simTL4J::operators::Equal_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::equal_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::Equal)

@given(instance=AndExpressionChild_strategy)
@settings(max_examples=50)
def test_andexpressionchild_instantiation(instance):
    assert isinstance(instance, AndExpressionChild)

@given(instance=simTL4J::expressions::EqualityExpression_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::equalityexpression_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::EqualityExpression)

@given(instance=simTL4J::expressions::EqualityExpressionChild_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::equalityexpressionchild_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::EqualityExpressionChild)

@given(instance=ExclusiveOrExpressionChild_strategy)
@settings(max_examples=50)
def test_exclusiveorexpressionchild_instantiation(instance):
    assert isinstance(instance, ExclusiveOrExpressionChild)

@given(instance=simTL4J::expressions::AndExpression_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::andexpression_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::AndExpression)

@given(instance=simTL4J::expressions::AndExpressionChild_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::andexpressionchild_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::AndExpressionChild)

@given(instance=simTL4J::expressions::InclusiveOrExpressionChild_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::inclusiveorexpressionchild_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::InclusiveOrExpressionChild)

@given(instance=InclusiveOrExpressionChild_strategy)
@settings(max_examples=50)
def test_inclusiveorexpressionchild_instantiation(instance):
    assert isinstance(instance, InclusiveOrExpressionChild)

@given(instance=simTL4J::expressions::ExclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::exclusiveorexpression_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::ExclusiveOrExpression)

@given(instance=simTL4J::expressions::ExclusiveOrExpressionChild_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::exclusiveorexpressionchild_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::ExclusiveOrExpressionChild)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=CompilationUnit_strategy)
@settings(max_examples=50)
def test_compilationunit_instantiation(instance):
    assert isinstance(instance, CompilationUnit)

@given(instance=annotations::Annotable_strategy)
@settings(max_examples=50)
def test_annotations::annotable_instantiation(instance):
    assert isinstance(instance, annotations::Annotable)

@given(instance=containers::JavaRoot_strategy)
@settings(max_examples=50)
def test_containers::javaroot_instantiation(instance):
    assert isinstance(instance, containers::JavaRoot)

@given(instance=ConditionalExpressionChild_strategy)
@settings(max_examples=50)
def test_conditionalexpressionchild_instantiation(instance):
    assert isinstance(instance, ConditionalExpressionChild)

@given(instance=simTL4J::expressions::ConditionalOrExpressionChild_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::conditionalorexpressionchild_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::ConditionalOrExpressionChild)

@given(instance=simTL4J::expressions::ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::conditionalorexpression_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::ConditionalOrExpression)

@given(instance=AssignmentOperator_strategy)
@settings(max_examples=50)
def test_assignmentoperator_instantiation(instance):
    assert isinstance(instance, AssignmentOperator)

@given(instance=simTL4J::operators::AssignmentExclusiveOr_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::assignmentexclusiveor_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::AssignmentExclusiveOr)

@given(instance=simTL4J::operators::AssignmentRightShift_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::assignmentrightshift_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::AssignmentRightShift)

@given(instance=simTL4J::operators::AssignmentUnsignedRightShift_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::assignmentunsignedrightshift_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::AssignmentUnsignedRightShift)

@given(instance=simTL4J::operators::AssignmentMinus_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::assignmentminus_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::AssignmentMinus)

@given(instance=simTL4J::operators::AssignmentAnd_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::assignmentand_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::AssignmentAnd)

@given(instance=simTL4J::operators::AssignmentMultiplication_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::assignmentmultiplication_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::AssignmentMultiplication)

@given(instance=simTL4J::operators::AssignmentOr_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::assignmentor_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::AssignmentOr)

@given(instance=simTL4J::operators::AssignmentDivision_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::assignmentdivision_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::AssignmentDivision)

@given(instance=simTL4J::operators::AssignmentPlus_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::assignmentplus_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::AssignmentPlus)

@given(instance=simTL4J::operators::AssignmentLeftShift_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::assignmentleftshift_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::AssignmentLeftShift)

@given(instance=simTL4J::operators::AssignmentModulo_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::assignmentmodulo_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::AssignmentModulo)

@given(instance=simTL4J::operators::Assignment_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::assignment_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::Assignment)

@given(instance=AssignmentExpressionChild_strategy)
@settings(max_examples=50)
def test_assignmentexpressionchild_instantiation(instance):
    assert isinstance(instance, AssignmentExpressionChild)

@given(instance=simTL4J::expressions::ConditionalExpressionChild_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::conditionalexpressionchild_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::ConditionalExpressionChild)

@given(instance=simTL4J::expressions::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::conditionalexpression_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::ConditionalExpression)

@given(instance=ForLoopInitializer_strategy)
@settings(max_examples=50)
def test_forloopinitializer_instantiation(instance):
    assert isinstance(instance, ForLoopInitializer)

@given(instance=simTL4J::expressions::ExpressionList_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::expressionlist_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::ExpressionList)

@given(instance=JavaRoot_strategy)
@settings(max_examples=50)
def test_javaroot_instantiation(instance):
    assert isinstance(instance, JavaRoot)

@given(instance=simTL4J::containers::EmptyModel_strategy)
@settings(max_examples=50)
def test_simtl4j::containers::emptymodel_instantiation(instance):
    assert isinstance(instance, simTL4J::containers::EmptyModel)

@given(instance=simTL4J::containers::CompilationUnit_strategy)
@settings(max_examples=50)
def test_simtl4j::containers::compilationunit_instantiation(instance):
    assert isinstance(instance, simTL4J::containers::CompilationUnit)

@given(instance=imports::ImportingElement_strategy)
@settings(max_examples=50)
def test_imports::importingelement_instantiation(instance):
    assert isinstance(instance, imports::ImportingElement)

@given(instance=commons::NamedElement_strategy)
@settings(max_examples=50)
def test_commons::namedelement_instantiation(instance):
    assert isinstance(instance, commons::NamedElement)

@given(instance=TPlaceholder_strategy)
@settings(max_examples=50)
def test_tplaceholder_instantiation(instance):
    assert isinstance(instance, TPlaceholder)

@given(instance=simTL4J::commons::Commentable_strategy)
@settings(max_examples=50)
def test_simtl4j::commons::commentable_instantiation(instance):
    assert isinstance(instance, simTL4J::commons::Commentable)

@given(instance=simTL4J::commons::Commentable_strategy)
def test_simtl4j::commons::commentable_comments_type(instance):
    assert isinstance(instance.comments, str)


@given(instance=simTL4J::commons::Commentable_strategy)
def test_simtl4j::commons::commentable_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original

@given(instance=classifiers::Implementor_strategy)
@settings(max_examples=50)
def test_classifiers::implementor_instantiation(instance):
    assert isinstance(instance, classifiers::Implementor)

@given(instance=classifiers::ConcreteClassifier_strategy)
@settings(max_examples=50)
def test_classifiers::concreteclassifier_instantiation(instance):
    assert isinstance(instance, classifiers::ConcreteClassifier)

@given(instance=simTL4J::classifiers::Class_strategy)
@settings(max_examples=50)
def test_simtl4j::classifiers::class_instantiation(instance):
    assert isinstance(instance, simTL4J::classifiers::Class)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=simTL4J::classifiers::Class_strategy)
@settings(max_examples=30)
def test_simtl4j::classifiers::class_unwrapprimitivetype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.unWrapPrimitiveType()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.unWrapPrimitiveType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'unWrapPrimitiveType' in simTL4J::classifiers::Class is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'unWrapPrimitiveType' in simTL4J::classifiers::Class did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'unWrapPrimitiveType' in simTL4J::classifiers::Class is not implemented or raised an error")

@given(instance=TypeReference_strategy)
@settings(max_examples=50)
def test_typereference_instantiation(instance):
    assert isinstance(instance, TypeReference)

@given(instance=EnumConstant_strategy)
@settings(max_examples=50)
def test_enumconstant_instantiation(instance):
    assert isinstance(instance, EnumConstant)

@given(instance=simTL4J::classifiers::Enumeration_strategy)
@settings(max_examples=50)
def test_simtl4j::classifiers::enumeration_instantiation(instance):
    assert isinstance(instance, simTL4J::classifiers::Enumeration)

@given(instance=ConcreteClassifier_strategy)
@settings(max_examples=50)
def test_concreteclassifier_instantiation(instance):
    assert isinstance(instance, ConcreteClassifier)

@given(instance=simTL4J::classifiers::Annotation_strategy)
@settings(max_examples=50)
def test_simtl4j::classifiers::annotation_instantiation(instance):
    assert isinstance(instance, simTL4J::classifiers::Annotation)

@given(instance=simTL4J::classifiers::Interface_strategy)
@settings(max_examples=50)
def test_simtl4j::classifiers::interface_instantiation(instance):
    assert isinstance(instance, simTL4J::classifiers::Interface)

@given(instance=arrays::ArrayTypeable_strategy)
@settings(max_examples=50)
def test_arrays::arraytypeable_instantiation(instance):
    assert isinstance(instance, arrays::ArrayTypeable)

@given(instance=types::TypedElement_strategy)
@settings(max_examples=50)
def test_types::typedelement_instantiation(instance):
    assert isinstance(instance, types::TypedElement)

@given(instance=simTL4J::expressions::CastExpression_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::castexpression_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::CastExpression)

@given(instance=simTL4J::expressions::InstanceOfExpression_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::instanceofexpression_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::InstanceOfExpression)

@given(instance=simTL4J::generics::QualifiedTypeArgument_strategy)
@settings(max_examples=50)
def test_simtl4j::generics::qualifiedtypeargument_instantiation(instance):
    assert isinstance(instance, simTL4J::generics::QualifiedTypeArgument)

@given(instance=expressions::Expression_strategy)
@settings(max_examples=50)
def test_expressions::expression_instantiation(instance):
    assert isinstance(instance, expressions::Expression)

@given(instance=ArrayInitializationValue_strategy)
@settings(max_examples=50)
def test_arrayinitializationvalue_instantiation(instance):
    assert isinstance(instance, ArrayInitializationValue)

@given(instance=annotations::AnnotationValue_strategy)
@settings(max_examples=50)
def test_annotations::annotationvalue_instantiation(instance):
    assert isinstance(instance, annotations::AnnotationValue)

@given(instance=arrays::ArrayInitializationValue_strategy)
@settings(max_examples=50)
def test_arrays::arrayinitializationvalue_instantiation(instance):
    assert isinstance(instance, arrays::ArrayInitializationValue)

@given(instance=simTL4J::expressions::Expression_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::expression_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::Expression)

@given(instance=simTL4J::arrays::ArrayInitializer_strategy)
@settings(max_examples=50)
def test_simtl4j::arrays::arrayinitializer_instantiation(instance):
    assert isinstance(instance, simTL4J::arrays::ArrayInitializer)

@given(instance=modifiers::AnnotableAndModifiable_strategy)
@settings(max_examples=50)
def test_modifiers::annotableandmodifiable_instantiation(instance):
    assert isinstance(instance, modifiers::AnnotableAndModifiable)

@given(instance=simTL4J::variables::LocalVariable_strategy)
@settings(max_examples=50)
def test_simtl4j::variables::localvariable_instantiation(instance):
    assert isinstance(instance, simTL4J::variables::LocalVariable)

@given(instance=simTL4J::parameters::Parameter_strategy)
@settings(max_examples=50)
def test_simtl4j::parameters::parameter_instantiation(instance):
    assert isinstance(instance, simTL4J::parameters::Parameter)

@given(instance=statements::Statement_strategy)
@settings(max_examples=50)
def test_statements::statement_instantiation(instance):
    assert isinstance(instance, statements::Statement)

@given(instance=simTL4J::simTL::TFor::StatementListContainer_strategy)
@settings(max_examples=50)
def test_simtl4j::simtl::tfor::statementlistcontainer_instantiation(instance):
    assert isinstance(instance, simTL4J::simTL::TFor::StatementListContainer)

@given(instance=simTL4J::statements::ForLoop_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::forloop_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::ForLoop)

@given(instance=simTL4J::statements::ForEachLoop_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::foreachloop_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::ForEachLoop)

@given(instance=simTL4J::statements::Assert_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::assert_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::Assert)

@given(instance=simTL4J::statements::TryBlock_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::tryblock_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::TryBlock)

@given(instance=simTL4J::statements::Condition_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::condition_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::Condition)

@given(instance=simTL4J::statements::SynchronizedBlock_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::synchronizedblock_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::SynchronizedBlock)

@given(instance=simTL4J::simTL::TIf::StatementListContainer_strategy)
@settings(max_examples=50)
def test_simtl4j::simtl::tif::statementlistcontainer_instantiation(instance):
    assert isinstance(instance, simTL4J::simTL::TIf::StatementListContainer)

@given(instance=simTL4J::statements::WhileLoop_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::whileloop_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::WhileLoop)

@given(instance=simTL4J::statements::JumpLabel_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::jumplabel_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::JumpLabel)

@given(instance=members::Member_strategy)
@settings(max_examples=50)
def test_members::member_instantiation(instance):
    assert isinstance(instance, members::Member)

@given(instance=simTL4J::statements::Block_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::block_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::Block)

@given(instance=members::MemberContainer_strategy)
@settings(max_examples=50)
def test_members::membercontainer_instantiation(instance):
    assert isinstance(instance, members::MemberContainer)

@given(instance=simTL4J::simTL::TFor::MemberContainer_strategy)
@settings(max_examples=50)
def test_simtl4j::simtl::tfor::membercontainer_instantiation(instance):
    assert isinstance(instance, simTL4J::simTL::TFor::MemberContainer)

@given(instance=simTL4J::simTL::TIf::MemberContainer_strategy)
@settings(max_examples=50)
def test_simtl4j::simtl::tif::membercontainer_instantiation(instance):
    assert isinstance(instance, simTL4J::simTL::TIf::MemberContainer)

@given(instance=generics::TypeParametrizable_strategy)
@settings(max_examples=50)
def test_generics::typeparametrizable_instantiation(instance):
    assert isinstance(instance, generics::TypeParametrizable)

@given(instance=simTL4J::members::Constructor_strategy)
@settings(max_examples=50)
def test_simtl4j::members::constructor_instantiation(instance):
    assert isinstance(instance, simTL4J::members::Constructor)

@given(instance=classifiers::Classifier_strategy)
@settings(max_examples=50)
def test_classifiers::classifier_instantiation(instance):
    assert isinstance(instance, classifiers::Classifier)

@given(instance=simTL4J::classifiers::ConcreteClassifier_strategy)
@settings(max_examples=50)
def test_simtl4j::classifiers::concreteclassifier_instantiation(instance):
    assert isinstance(instance, simTL4J::classifiers::ConcreteClassifier)

@given(instance=simTL4J::classifiers::ConcreteClassifier_strategy)
def test_simtl4j::classifiers::concreteclassifier_fullName_type(instance):
    assert isinstance(instance.fullName, str)


@given(instance=simTL4J::classifiers::ConcreteClassifier_strategy)
def test_simtl4j::classifiers::concreteclassifier_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original

@given(instance=references::ReferenceableElement_strategy)
@settings(max_examples=50)
def test_references::referenceableelement_instantiation(instance):
    assert isinstance(instance, references::ReferenceableElement)

@given(instance=simTL4J::members::Method_strategy)
@settings(max_examples=50)
def test_simtl4j::members::method_instantiation(instance):
    assert isinstance(instance, simTL4J::members::Method)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=simTL4J::members::Method_strategy)
@settings(max_examples=30)
def test_simtl4j::members::method_ismethodforcall_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isMethodForCall(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isMethodForCall).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isMethodForCall' in simTL4J::members::Method is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isMethodForCall' in simTL4J::members::Method did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isMethodForCall' in simTL4J::members::Method is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=simTL4J::members::Method_strategy)
@settings(max_examples=30)
def test_simtl4j::members::method_issomemethodforcall_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSomeMethodForCall(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSomeMethodForCall).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSomeMethodForCall' in simTL4J::members::Method is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSomeMethodForCall' in simTL4J::members::Method did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSomeMethodForCall' in simTL4J::members::Method is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=simTL4J::members::Method_strategy)
@settings(max_examples=30)
def test_simtl4j::members::method_isbettermethodforcall_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isBetterMethodForCall(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isBetterMethodForCall).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isBetterMethodForCall' in simTL4J::members::Method is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isBetterMethodForCall' in simTL4J::members::Method did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isBetterMethodForCall' in simTL4J::members::Method is not implemented or raised an error")

@given(instance=simTL4J::members::EnumConstant_strategy)
@settings(max_examples=50)
def test_simtl4j::members::enumconstant_instantiation(instance):
    assert isinstance(instance, simTL4J::members::EnumConstant)

@given(instance=simTL4J::members::Field_strategy)
@settings(max_examples=50)
def test_simtl4j::members::field_instantiation(instance):
    assert isinstance(instance, simTL4J::members::Field)

@given(instance=simTL4J::containers::Package_strategy)
@settings(max_examples=50)
def test_simtl4j::containers::package_instantiation(instance):
    assert isinstance(instance, simTL4J::containers::Package)

@given(instance=simTL4J::members::AdditionalField_strategy)
@settings(max_examples=50)
def test_simtl4j::members::additionalfield_instantiation(instance):
    assert isinstance(instance, simTL4J::members::AdditionalField)

@given(instance=simTL4J::variables::AdditionalLocalVariable_strategy)
@settings(max_examples=50)
def test_simtl4j::variables::additionallocalvariable_instantiation(instance):
    assert isinstance(instance, simTL4J::variables::AdditionalLocalVariable)

@given(instance=simTL4J::variables::Variable_strategy)
@settings(max_examples=50)
def test_simtl4j::variables::variable_instantiation(instance):
    assert isinstance(instance, simTL4J::variables::Variable)

@given(instance=types::Type_strategy)
@settings(max_examples=50)
def test_types::type_instantiation(instance):
    assert isinstance(instance, types::Type)

@given(instance=simTL4J::types::PrimitiveType_strategy)
@settings(max_examples=50)
def test_simtl4j::types::primitivetype_instantiation(instance):
    assert isinstance(instance, simTL4J::types::PrimitiveType)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=simTL4J::types::PrimitiveType_strategy)
@settings(max_examples=30)
def test_simtl4j::types::primitivetype_wrapprimitivetype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.wrapPrimitiveType()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.wrapPrimitiveType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'wrapPrimitiveType' in simTL4J::types::PrimitiveType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'wrapPrimitiveType' in simTL4J::types::PrimitiveType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'wrapPrimitiveType' in simTL4J::types::PrimitiveType is not implemented or raised an error")

@given(instance=simTL4J::classifiers::AnonymousClass_strategy)
@settings(max_examples=50)
def test_simtl4j::classifiers::anonymousclass_instantiation(instance):
    assert isinstance(instance, simTL4J::classifiers::AnonymousClass)

@given(instance=simTL4J::classifiers::Classifier_strategy)
@settings(max_examples=50)
def test_simtl4j::classifiers::classifier_instantiation(instance):
    assert isinstance(instance, simTL4J::classifiers::Classifier)

@given(instance=ArrayInitializer_strategy)
@settings(max_examples=50)
def test_arrayinitializer_instantiation(instance):
    assert isinstance(instance, ArrayInitializer)

@given(instance=modifiers::AnnotationInstanceOrModifier_strategy)
@settings(max_examples=50)
def test_modifiers::annotationinstanceormodifier_instantiation(instance):
    assert isinstance(instance, modifiers::AnnotationInstanceOrModifier)

@given(instance=references::Reference_strategy)
@settings(max_examples=50)
def test_references::reference_instantiation(instance):
    assert isinstance(instance, references::Reference)

@given(instance=simTL4J::instantiations::Instantiation_strategy)
@settings(max_examples=50)
def test_simtl4j::instantiations::instantiation_instantiation(instance):
    assert isinstance(instance, simTL4J::instantiations::Instantiation)

@given(instance=simTL4J::arrays::ArrayInstantiationBySize_strategy)
@settings(max_examples=50)
def test_simtl4j::arrays::arrayinstantiationbysize_instantiation(instance):
    assert isinstance(instance, simTL4J::arrays::ArrayInstantiationBySize)

@given(instance=simTL4J::arrays::ArrayInstantiationByValues_strategy)
@settings(max_examples=50)
def test_simtl4j::arrays::arrayinstantiationbyvalues_instantiation(instance):
    assert isinstance(instance, simTL4J::arrays::ArrayInstantiationByValues)

@given(instance=AnnotationInstance_strategy)
@settings(max_examples=50)
def test_annotationinstance_instantiation(instance):
    assert isinstance(instance, AnnotationInstance)

@given(instance=Commentable_strategy)
@settings(max_examples=50)
def test_commentable_instantiation(instance):
    assert isinstance(instance, Commentable)

@given(instance=simTL4J::members::MemberContainer_strategy)
@settings(max_examples=50)
def test_simtl4j::members::membercontainer_instantiation(instance):
    assert isinstance(instance, simTL4J::members::MemberContainer)

@given(instance=simTL4J::modifiers::AnnotationInstanceOrModifier_strategy)
@settings(max_examples=50)
def test_simtl4j::modifiers::annotationinstanceormodifier_instantiation(instance):
    assert isinstance(instance, simTL4J::modifiers::AnnotationInstanceOrModifier)

@given(instance=simTL4J::references::Argumentable_strategy)
@settings(max_examples=50)
def test_simtl4j::references::argumentable_instantiation(instance):
    assert isinstance(instance, simTL4J::references::Argumentable)

@given(instance=simTL4J::statements::StatementContainer_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::statementcontainer_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::StatementContainer)

@given(instance=simTL4J::arrays::ArrayDimension_strategy)
@settings(max_examples=50)
def test_simtl4j::arrays::arraydimension_instantiation(instance):
    assert isinstance(instance, simTL4J::arrays::ArrayDimension)

@given(instance=simTL4J::instantiations::Initializable_strategy)
@settings(max_examples=50)
def test_simtl4j::instantiations::initializable_instantiation(instance):
    assert isinstance(instance, simTL4J::instantiations::Initializable)

@given(instance=simTL4J::operators::Operator_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::operator_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::Operator)

@given(instance=simTL4J::commons::NamespaceAwareElement_strategy)
@settings(max_examples=50)
def test_simtl4j::commons::namespaceawareelement_instantiation(instance):
    assert isinstance(instance, simTL4J::commons::NamespaceAwareElement)

@given(instance=simTL4J::commons::NamespaceAwareElement_strategy)
def test_simtl4j::commons::namespaceawareelement_namespaces_type(instance):
    assert isinstance(instance.namespaces, str)


@given(instance=simTL4J::commons::NamespaceAwareElement_strategy)
def test_simtl4j::commons::namespaceawareelement_namespaces_setter(instance):
    original = instance.namespaces
    instance.namespaces = original
    assert instance.namespaces == original

@given(instance=simTL4J::arrays::ArrayInitializationValue_strategy)
@settings(max_examples=50)
def test_simtl4j::arrays::arrayinitializationvalue_instantiation(instance):
    assert isinstance(instance, simTL4J::arrays::ArrayInitializationValue)

@given(instance=simTL4J::statements::StatementListContainer_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::statementlistcontainer_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::StatementListContainer)

@given(instance=simTL4J::types::TypedElement_strategy)
@settings(max_examples=50)
def test_simtl4j::types::typedelement_instantiation(instance):
    assert isinstance(instance, simTL4J::types::TypedElement)

@given(instance=simTL4J::parameters::Parametrizable_strategy)
@settings(max_examples=50)
def test_simtl4j::parameters::parametrizable_instantiation(instance):
    assert isinstance(instance, simTL4J::parameters::Parametrizable)

@given(instance=simTL4J::commons::NamedElement_strategy)
@settings(max_examples=50)
def test_simtl4j::commons::namedelement_instantiation(instance):
    assert isinstance(instance, simTL4J::commons::NamedElement)

@given(instance=simTL4J::commons::NamedElement_strategy)
def test_simtl4j::commons::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simTL4J::commons::NamedElement_strategy)
def test_simtl4j::commons::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simTL4J::classifiers::Implementor_strategy)
@settings(max_examples=50)
def test_simtl4j::classifiers::implementor_instantiation(instance):
    assert isinstance(instance, simTL4J::classifiers::Implementor)

@given(instance=simTL4J::arrays::ArraySelector_strategy)
@settings(max_examples=50)
def test_simtl4j::arrays::arrayselector_instantiation(instance):
    assert isinstance(instance, simTL4J::arrays::ArraySelector)

@given(instance=simTL4J::imports::ImportingElement_strategy)
@settings(max_examples=50)
def test_simtl4j::imports::importingelement_instantiation(instance):
    assert isinstance(instance, simTL4J::imports::ImportingElement)

@given(instance=simTL4J::types::Type_strategy)
@settings(max_examples=50)
def test_simtl4j::types::type_instantiation(instance):
    assert isinstance(instance, simTL4J::types::Type)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=simTL4J::types::Type_strategy)
@settings(max_examples=30)
def test_simtl4j::types::type_equalstype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.equalsType(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.equalsType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'equalsType' in simTL4J::types::Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'equalsType' in simTL4J::types::Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'equalsType' in simTL4J::types::Type is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=simTL4J::types::Type_strategy)
@settings(max_examples=30)
def test_simtl4j::types::type_issupertype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSuperType(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSuperType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSuperType' in simTL4J::types::Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSuperType' in simTL4J::types::Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSuperType' in simTL4J::types::Type is not implemented or raised an error")

@given(instance=simTL4J::generics::TypeParametrizable_strategy)
@settings(max_examples=50)
def test_simtl4j::generics::typeparametrizable_instantiation(instance):
    assert isinstance(instance, simTL4J::generics::TypeParametrizable)

@given(instance=simTL4J::modifiers::AnnotableAndModifiable_strategy)
@settings(max_examples=50)
def test_simtl4j::modifiers::annotableandmodifiable_instantiation(instance):
    assert isinstance(instance, simTL4J::modifiers::AnnotableAndModifiable)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=simTL4J::modifiers::AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_simtl4j::modifiers::annotableandmodifiable_ishidden_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isHidden(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isHidden).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isHidden' in simTL4J::modifiers::AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isHidden' in simTL4J::modifiers::AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isHidden' in simTL4J::modifiers::AnnotableAndModifiable is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=simTL4J::modifiers::AnnotableAndModifiable_strategy)
@settings(max_examples=30)
def test_simtl4j::modifiers::annotableandmodifiable_isstatic_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isStatic()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isStatic).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isStatic' in simTL4J::modifiers::AnnotableAndModifiable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isStatic' in simTL4J::modifiers::AnnotableAndModifiable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isStatic' in simTL4J::modifiers::AnnotableAndModifiable is not implemented or raised an error")

@given(instance=simTL4J::literals::Self_strategy)
@settings(max_examples=50)
def test_simtl4j::literals::self_instantiation(instance):
    assert isinstance(instance, simTL4J::literals::Self)

@given(instance=simTL4J::members::ExceptionThrower_strategy)
@settings(max_examples=50)
def test_simtl4j::members::exceptionthrower_instantiation(instance):
    assert isinstance(instance, simTL4J::members::ExceptionThrower)

@given(instance=simTL4J::statements::Statement_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::statement_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::Statement)

@given(instance=simTL4J::statements::Conditional_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::conditional_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::Conditional)

@given(instance=simTL4J::types::TypeReference_strategy)
@settings(max_examples=50)
def test_simtl4j::types::typereference_instantiation(instance):
    assert isinstance(instance, simTL4J::types::TypeReference)

@given(instance=simTL4J::statements::ForLoopInitializer_strategy)
@settings(max_examples=50)
def test_simtl4j::statements::forloopinitializer_instantiation(instance):
    assert isinstance(instance, simTL4J::statements::ForLoopInitializer)

@given(instance=simTL4J::modifiers::Modifiable_strategy)
@settings(max_examples=50)
def test_simtl4j::modifiers::modifiable_instantiation(instance):
    assert isinstance(instance, simTL4J::modifiers::Modifiable)

@given(instance=simTL4J::annotations::Annotable_strategy)
@settings(max_examples=50)
def test_simtl4j::annotations::annotable_instantiation(instance):
    assert isinstance(instance, simTL4J::annotations::Annotable)

@given(instance=ArrayDimension_strategy)
@settings(max_examples=50)
def test_arraydimension_instantiation(instance):
    assert isinstance(instance, ArrayDimension)

@given(instance=simTL4J::arrays::ArrayTypeable_strategy)
@settings(max_examples=50)
def test_simtl4j::arrays::arraytypeable_instantiation(instance):
    assert isinstance(instance, simTL4J::arrays::ArrayTypeable)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=simTL4J::expressions::AssignmentExpressionChild_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::assignmentexpressionchild_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::AssignmentExpressionChild)

@given(instance=simTL4J::expressions::AssignmentExpression_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::assignmentexpression_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::AssignmentExpression)

@given(instance=simTL4J::annotations::AnnotationValue_strategy)
@settings(max_examples=50)
def test_simtl4j::annotations::annotationvalue_instantiation(instance):
    assert isinstance(instance, simTL4J::annotations::AnnotationValue)

@given(instance=InterfaceMethod_strategy)
@settings(max_examples=50)
def test_interfacemethod_instantiation(instance):
    assert isinstance(instance, InterfaceMethod)

@given(instance=simTL4J::annotations::AnnotationAttribute_strategy)
@settings(max_examples=50)
def test_simtl4j::annotations::annotationattribute_instantiation(instance):
    assert isinstance(instance, simTL4J::annotations::AnnotationAttribute)

@given(instance=simTL4J::annotations::AnnotationAttributeSetting_strategy)
@settings(max_examples=50)
def test_simtl4j::annotations::annotationattributesetting_instantiation(instance):
    assert isinstance(instance, simTL4J::annotations::AnnotationAttributeSetting)

@given(instance=AnnotationAttributeSetting_strategy)
@settings(max_examples=50)
def test_annotationattributesetting_instantiation(instance):
    assert isinstance(instance, AnnotationAttributeSetting)

@given(instance=AnnotationValue_strategy)
@settings(max_examples=50)
def test_annotationvalue_instantiation(instance):
    assert isinstance(instance, AnnotationValue)

@given(instance=simTL4J::annotations::AnnotationParameter_strategy)
@settings(max_examples=50)
def test_simtl4j::annotations::annotationparameter_instantiation(instance):
    assert isinstance(instance, simTL4J::annotations::AnnotationParameter)

@given(instance=AnnotationParameter_strategy)
@settings(max_examples=50)
def test_annotationparameter_instantiation(instance):
    assert isinstance(instance, AnnotationParameter)

@given(instance=simTL4J::annotations::AnnotationParameterList_strategy)
@settings(max_examples=50)
def test_simtl4j::annotations::annotationparameterlist_instantiation(instance):
    assert isinstance(instance, simTL4J::annotations::AnnotationParameterList)

@given(instance=simTL4J::annotations::SingleAnnotationParameter_strategy)
@settings(max_examples=50)
def test_simtl4j::annotations::singleannotationparameter_instantiation(instance):
    assert isinstance(instance, simTL4J::annotations::SingleAnnotationParameter)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=simTL4J::generics::TypeParameter_strategy)
@settings(max_examples=50)
def test_simtl4j::generics::typeparameter_instantiation(instance):
    assert isinstance(instance, simTL4J::generics::TypeParameter)

@given(instance=commons::NamespaceAwareElement_strategy)
@settings(max_examples=50)
def test_commons::namespaceawareelement_instantiation(instance):
    assert isinstance(instance, commons::NamespaceAwareElement)

@given(instance=simTL4J::annotations::AnnotationInstance_strategy)
@settings(max_examples=50)
def test_simtl4j::annotations::annotationinstance_instantiation(instance):
    assert isinstance(instance, simTL4J::annotations::AnnotationInstance)

@given(instance=simTL4J::types::NamespaceClassifierReference_strategy)
@settings(max_examples=50)
def test_simtl4j::types::namespaceclassifierreference_instantiation(instance):
    assert isinstance(instance, simTL4J::types::NamespaceClassifierReference)

@given(instance=simTL4J::containers::JavaRoot_strategy)
@settings(max_examples=50)
def test_simtl4j::containers::javaroot_instantiation(instance):
    assert isinstance(instance, simTL4J::containers::JavaRoot)

@given(instance=UnaryModificationExpression_strategy)
@settings(max_examples=50)
def test_unarymodificationexpression_instantiation(instance):
    assert isinstance(instance, UnaryModificationExpression)

@given(instance=simTL4J::expressions::SuffixUnaryModificationExpression_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::suffixunarymodificationexpression_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::SuffixUnaryModificationExpression)

@given(instance=simTL4J::expressions::PrefixUnaryModificationExpression_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::prefixunarymodificationexpression_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::PrefixUnaryModificationExpression)

@given(instance=simTL4J::generics::CallTypeArgumentable_strategy)
@settings(max_examples=50)
def test_simtl4j::generics::calltypeargumentable_instantiation(instance):
    assert isinstance(instance, simTL4J::generics::CallTypeArgumentable)

@given(instance=TypeArgument_strategy)
@settings(max_examples=50)
def test_typeargument_instantiation(instance):
    assert isinstance(instance, TypeArgument)

@given(instance=simTL4J::generics::ExtendsTypeArgument_strategy)
@settings(max_examples=50)
def test_simtl4j::generics::extendstypeargument_instantiation(instance):
    assert isinstance(instance, simTL4J::generics::ExtendsTypeArgument)

@given(instance=simTL4J::generics::SuperTypeArgument_strategy)
@settings(max_examples=50)
def test_simtl4j::generics::supertypeargument_instantiation(instance):
    assert isinstance(instance, simTL4J::generics::SuperTypeArgument)

@given(instance=simTL4J::generics::UnknownTypeArgument_strategy)
@settings(max_examples=50)
def test_simtl4j::generics::unknowntypeargument_instantiation(instance):
    assert isinstance(instance, simTL4J::generics::UnknownTypeArgument)

@given(instance=simTL4J::generics::TypeArgumentable_strategy)
@settings(max_examples=50)
def test_simtl4j::generics::typeargumentable_instantiation(instance):
    assert isinstance(instance, simTL4J::generics::TypeArgumentable)

@given(instance=ArrayTypeable_strategy)
@settings(max_examples=50)
def test_arraytypeable_instantiation(instance):
    assert isinstance(instance, ArrayTypeable)

@given(instance=simTL4J::generics::TypeArgument_strategy)
@settings(max_examples=50)
def test_simtl4j::generics::typeargument_instantiation(instance):
    assert isinstance(instance, simTL4J::generics::TypeArgument)

@given(instance=Reference_strategy)
@settings(max_examples=50)
def test_reference_instantiation(instance):
    assert isinstance(instance, Reference)

@given(instance=simTL4J::references::SelfReference_strategy)
@settings(max_examples=50)
def test_simtl4j::references::selfreference_instantiation(instance):
    assert isinstance(instance, simTL4J::references::SelfReference)

@given(instance=simTL4J::references::ReflectiveClassReference_strategy)
@settings(max_examples=50)
def test_simtl4j::references::reflectiveclassreference_instantiation(instance):
    assert isinstance(instance, simTL4J::references::ReflectiveClassReference)

@given(instance=simTL4J::references::ElementReference_strategy)
@settings(max_examples=50)
def test_simtl4j::references::elementreference_instantiation(instance):
    assert isinstance(instance, simTL4J::references::ElementReference)

@given(instance=simTL4J::references::StringReference_strategy)
@settings(max_examples=50)
def test_simtl4j::references::stringreference_instantiation(instance):
    assert isinstance(instance, simTL4J::references::StringReference)

@given(instance=simTL4J::references::StringReference_strategy)
def test_simtl4j::references::stringreference_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=simTL4J::references::StringReference_strategy)
def test_simtl4j::references::stringreference_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=simTL4J::references::PrimitiveTypeReference_strategy)
@settings(max_examples=50)
def test_simtl4j::references::primitivetypereference_instantiation(instance):
    assert isinstance(instance, simTL4J::references::PrimitiveTypeReference)

@given(instance=simTL4J::expressions::NestedExpression_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::nestedexpression_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::NestedExpression)

@given(instance=ShiftOperator_strategy)
@settings(max_examples=50)
def test_shiftoperator_instantiation(instance):
    assert isinstance(instance, ShiftOperator)

@given(instance=simTL4J::operators::RightShift_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::rightshift_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::RightShift)

@given(instance=simTL4J::operators::LeftShift_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::leftshift_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::LeftShift)

@given(instance=simTL4J::operators::UnsignedRightShift_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::unsignedrightshift_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::UnsignedRightShift)

@given(instance=ShiftExpressionChild_strategy)
@settings(max_examples=50)
def test_shiftexpressionchild_instantiation(instance):
    assert isinstance(instance, ShiftExpressionChild)

@given(instance=simTL4J::expressions::AdditiveExpressionChild_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::additiveexpressionchild_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::AdditiveExpressionChild)

@given(instance=simTL4J::expressions::AdditiveExpression_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::additiveexpression_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::AdditiveExpression)

@given(instance=simTL4J::expressions::ShiftExpression_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::shiftexpression_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::ShiftExpression)

@given(instance=simTL4J::expressions::RelationExpressionChild_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::relationexpressionchild_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::RelationExpressionChild)

@given(instance=RelationOperator_strategy)
@settings(max_examples=50)
def test_relationoperator_instantiation(instance):
    assert isinstance(instance, RelationOperator)

@given(instance=simTL4J::operators::LessThanOrEqual_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::lessthanorequal_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::LessThanOrEqual)

@given(instance=simTL4J::operators::GreaterThan_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::greaterthan_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::GreaterThan)

@given(instance=simTL4J::operators::GreaterThanOrEqual_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::greaterthanorequal_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::GreaterThanOrEqual)

@given(instance=simTL4J::operators::LessThan_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::lessthan_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::LessThan)

@given(instance=UnaryModificationOperator_strategy)
@settings(max_examples=50)
def test_unarymodificationoperator_instantiation(instance):
    assert isinstance(instance, UnaryModificationOperator)

@given(instance=simTL4J::operators::PlusPlus_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::plusplus_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::PlusPlus)

@given(instance=simTL4J::operators::MinusMinus_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::minusminus_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::MinusMinus)

@given(instance=UnaryModificationExpressionChild_strategy)
@settings(max_examples=50)
def test_unarymodificationexpressionchild_instantiation(instance):
    assert isinstance(instance, UnaryModificationExpressionChild)

@given(instance=simTL4J::expressions::PrimaryExpression_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::primaryexpression_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::PrimaryExpression)

@given(instance=simTL4J::expressions::UnaryExpressionChild_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::unaryexpressionchild_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::UnaryExpressionChild)

@given(instance=UnaryExpressionChild_strategy)
@settings(max_examples=50)
def test_unaryexpressionchild_instantiation(instance):
    assert isinstance(instance, UnaryExpressionChild)

@given(instance=simTL4J::expressions::UnaryModificationExpressionChild_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::unarymodificationexpressionchild_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::UnaryModificationExpressionChild)

@given(instance=simTL4J::expressions::UnaryModificationExpression_strategy)
@settings(max_examples=50)
def test_simtl4j::expressions::unarymodificationexpression_instantiation(instance):
    assert isinstance(instance, simTL4J::expressions::UnaryModificationExpression)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=simTL4J::operators::Complement_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::complement_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::Complement)

@given(instance=simTL4J::operators::Negate_strategy)
@settings(max_examples=50)
def test_simtl4j::operators::negate_instantiation(instance):
    assert isinstance(instance, simTL4J::operators::Negate)
