import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PredefinedId,
    odemcustom::TypeLiteral,
    odemcustom::MetaLiteral,
    odemcustom::SetOp,
    odemcustom::SuperLiteral,
    odemcustom::MeLiteral,
    UnaryOperator,
    odemcustom::Neg,
    BinaryOperator,
    odemcustom::Div,
    odemcustom::GreaterEqual,
    odemcustom::Mul,
    odemcustom::Mod,
    odemcustom::Greater,
    odemcustom::LessEqual,
    odemcustom::And,
    odemcustom::Or,
    odemcustom::Less,
    odemcustom::Minus,
    odemcustom::Plus,
    Expression,
    odemcustom::UnaryOperator,
    odemcustom::BinaryOperator,
    odemcustom::L1Expr,
    CompositeStatement,
    odemcustom::WhileStatement,
    odemcustom::ForEachStatement,
    odemcustom::IfStatement,
    SetStatement,
    odemcustom::EmptySet,
    odemcustom::AddToSet,
    odemcustom::RemoveFromSet,
    odemcustom::StatementExpression,
    SimpleStatement,
    odemcustom::Print,
    odemcustom::BreakStatement,
    odemcustom::Assignment,
    odemcustom::SetStatement,
    odemcustom::Advance,
    odemcustom::ContinueStatement,
    odemcustom::ExpressionStatement,
    Construct,
    odemcustom::Statement,
    odemcustom::CodeBlock,
    odemcustom::ActivateObject,
    odemcustom::Reactivate,
    odemcustom::Wait,
    odemcustom::Terminate,
    odemcustom::WaitUntil,
    odemcustom::Return,
    StatementExpression,
    odemcustom::ProcedureCall,
    ExpressionStatement,
    odemcustom::DeprecatedProcedureCallStatement,
    odemcustom::Constructor,
    ClassSimilar,
    Classifier,
    ExpandableElement,
    odemcustom::NamedElement,
    Statement,
    odemcustom::CompositeStatement,
    odemcustom::SimpleStatement,
    AbstractVariable,
    odemcustom::AnnotatableElement,
    odemcustom::Expression,
    odemcustom::KeyValuePair,
    odemcustom::AnnotationApplication,
    odemcustom::Interface,
    odemcustom::Clazz,
    ModifierExtensionsContainer,
    odemcustom::NativeBinding,
    ReferableRhsType,
    odemcustom::TypedElement,
    odemcustom::Type,
    odemcustom::ModifierExtensionsContainer,
    odemcustom::Extension,
    odemcustom::EmbeddableExtensionsContainer,
    odemcustom::IdResolution,
    odemcustom::Variable,
    odemcustom::Parameter,
    AnnotatableElement,
    CodeBlock,
    odemcustom::StartCodeBlock,
    TypedElement,
    PrimitiveType,
    odemcustom::IntType,
    odemcustom::BoolType,
    odemcustom::DoubleType,
    odemcustom::StringType,
    odemcustom::VoidType,
    Type,
    odemcustom::IdExpr,
    odemcustom::PrimitiveType,
    odemcustom::Import,
    odemcustom::Model,
    NamedExtension,
    odemcustom::ClassAugment,
    EmbeddableExtensionsContainer,
    odemcustom::ClassSimilar,
    NamedElement,
    odemcustom::Classifier,
    odemcustom::AbstractVariable,
    odemcustom::SimpleAnnotation,
    odemcustom::ExtensionDefinition,
    odemcustom::Annotation,
    odemcustom::Procedure,
    odemcustom::Module,
    odemcustom::Construct,
    odemcustom::PotentiallyHiddenIdElements,
    odemcustom::IncludePattern,
    odemcustom::ConsiderIdElements,
    odemcustom::FindContainer,
    odemcustom::ExpandStatement,
    odemcustom::ExpandExpression,
    odemcustom::TestStatement,
    odemcustom::ExpandableElement,
    Module,
    QuotedCode,
    odemcustom::QuotedModuleContent,
    odemcustom::QuotedStatements,
    odemcustom::QuotedClassContent,
    odemcustom::QuotedExpression,
    odemcustom::QuotedCode,
    odemcustom::CodeQuoteExpression,
    odemcustom::ExpandSection,
    odemcustom::TargetStatement,
    odemcustom::MetaExpr,
    odemcustom::MappingPart,
    MappingPart,
    odemcustom::DynamicMappingPart,
    odemcustom::FixedMappingPart,
    odemcustom::ResumeGenStatement,
    odemcustom::SaveGenStatement,
    odemcustom::ResetGenContextStatement,
    odemcustom::SetGenContextStatement,
    odemcustom::MappingStatement,
    odemcustom::Pattern,
    StructuredPropertyType,
    odemcustom::ReferencePropertyType,
    odemcustom::CompositePropertyType,
    PropertyType,
    odemcustom::StringPropertyType,
    odemcustom::IntPropertyType,
    odemcustom::StructuredPropertyType,
    odemcustom::BooleanPropertyType,
    odemcustom::IdPropertyType,
    odemcustom::PropertyType,
    odemcustom::ReferableRhsType,
    odemcustom::TsRule,
    odemcustom::ExtensionRule,
    odemcustom::Mapping,
    odemcustom::TextualSyntaxDef,
    RhsExpression,
    odemcustom::AtLeastOneExpr,
    odemcustom::ArbitraryExpr,
    odemcustom::AlternativeExpr,
    odemcustom::PropertyBindingExpr,
    odemcustom::TerminalExpr,
    odemcustom::RuntimeExpr,
    odemcustom::OptionalExpr,
    odemcustom::SequenceExpr,
    odemcustom::RuleExpr,
    odemcustom::RhsExpression,
    odemcustom::PredefinedId,
    odemcustom::DepIdentifiableElement,
    odemcustom::DoubleLiteral,
    odemcustom::FalseLiteral,
    odemcustom::TrueLiteral,
    odemcustom::ModuleContentExtension,
    odemcustom::ClassContentExtension,
    Extension,
    odemcustom::NamedExtension,
    VariableAccess,
    odemcustom::MetaAccess,
    ElementAccess,
    odemcustom::VariableAccess,
    odemcustom::TypeAccess,
    odemcustom::ElementAccess,
    odemcustom::ArgumentExpression,
    odemcustom::EvalExpr,
    odemcustom::ActiveLiteral,
    odemcustom::TimeLiteral,
    odemcustom::NullLiteral,
    odemcustom::Cast,
    odemcustom::CreateObject,
    odemcustom::Not,
    odemcustom::InstanceOf,
    odemcustom::Equal,
    odemcustom::NotEqual,
    odemcustom::IntLiteral,
    odemcustom::StringLiteral,
    SetOp,
    odemcustom::IndexOf,
    odemcustom::LastInSet,
    odemcustom::AfterInSet,
    odemcustom::ObjectAt,
    odemcustom::BeforeInSet,
    odemcustom::FirstInSet,
    odemcustom::Contains,
    odemcustom::SizeOfSet,
    BindingExprOpKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_predefinedid_is_not_abstract():
    assert not inspect.isabstract(PredefinedId)


def test_predefinedid_constructor_exists():
    assert callable(PredefinedId.__init__)


def test_predefinedid_constructor_args():
    sig = inspect.signature(PredefinedId.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::typeliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom::TypeLiteral)


def test_odemcustom::typeliteral_constructor_exists():
    assert callable(odemcustom::TypeLiteral.__init__)


def test_odemcustom::typeliteral_constructor_args():
    sig = inspect.signature(odemcustom::TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::metaliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom::MetaLiteral)


def test_odemcustom::metaliteral_constructor_exists():
    assert callable(odemcustom::MetaLiteral.__init__)


def test_odemcustom::metaliteral_constructor_args():
    sig = inspect.signature(odemcustom::MetaLiteral.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::setop_is_not_abstract():
    assert not inspect.isabstract(odemcustom::SetOp)


def test_odemcustom::setop_constructor_exists():
    assert callable(odemcustom::SetOp.__init__)


def test_odemcustom::setop_constructor_args():
    sig = inspect.signature(odemcustom::SetOp.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::superliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom::SuperLiteral)


def test_odemcustom::superliteral_constructor_exists():
    assert callable(odemcustom::SuperLiteral.__init__)


def test_odemcustom::superliteral_constructor_args():
    sig = inspect.signature(odemcustom::SuperLiteral.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::meliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom::MeLiteral)


def test_odemcustom::meliteral_constructor_exists():
    assert callable(odemcustom::MeLiteral.__init__)


def test_odemcustom::meliteral_constructor_args():
    sig = inspect.signature(odemcustom::MeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::neg_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Neg)


def test_odemcustom::neg_constructor_exists():
    assert callable(odemcustom::Neg.__init__)


def test_odemcustom::neg_constructor_args():
    sig = inspect.signature(odemcustom::Neg.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::div_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Div)


def test_odemcustom::div_constructor_exists():
    assert callable(odemcustom::Div.__init__)


def test_odemcustom::div_constructor_args():
    sig = inspect.signature(odemcustom::Div.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::greaterequal_is_not_abstract():
    assert not inspect.isabstract(odemcustom::GreaterEqual)


def test_odemcustom::greaterequal_constructor_exists():
    assert callable(odemcustom::GreaterEqual.__init__)


def test_odemcustom::greaterequal_constructor_args():
    sig = inspect.signature(odemcustom::GreaterEqual.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::mul_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Mul)


def test_odemcustom::mul_constructor_exists():
    assert callable(odemcustom::Mul.__init__)


def test_odemcustom::mul_constructor_args():
    sig = inspect.signature(odemcustom::Mul.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::mod_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Mod)


def test_odemcustom::mod_constructor_exists():
    assert callable(odemcustom::Mod.__init__)


def test_odemcustom::mod_constructor_args():
    sig = inspect.signature(odemcustom::Mod.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::greater_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Greater)


def test_odemcustom::greater_constructor_exists():
    assert callable(odemcustom::Greater.__init__)


def test_odemcustom::greater_constructor_args():
    sig = inspect.signature(odemcustom::Greater.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::lessequal_is_not_abstract():
    assert not inspect.isabstract(odemcustom::LessEqual)


def test_odemcustom::lessequal_constructor_exists():
    assert callable(odemcustom::LessEqual.__init__)


def test_odemcustom::lessequal_constructor_args():
    sig = inspect.signature(odemcustom::LessEqual.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::and_is_not_abstract():
    assert not inspect.isabstract(odemcustom::And)


def test_odemcustom::and_constructor_exists():
    assert callable(odemcustom::And.__init__)


def test_odemcustom::and_constructor_args():
    sig = inspect.signature(odemcustom::And.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::or_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Or)


def test_odemcustom::or_constructor_exists():
    assert callable(odemcustom::Or.__init__)


def test_odemcustom::or_constructor_args():
    sig = inspect.signature(odemcustom::Or.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::less_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Less)


def test_odemcustom::less_constructor_exists():
    assert callable(odemcustom::Less.__init__)


def test_odemcustom::less_constructor_args():
    sig = inspect.signature(odemcustom::Less.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::minus_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Minus)


def test_odemcustom::minus_constructor_exists():
    assert callable(odemcustom::Minus.__init__)


def test_odemcustom::minus_constructor_args():
    sig = inspect.signature(odemcustom::Minus.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::plus_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Plus)


def test_odemcustom::plus_constructor_exists():
    assert callable(odemcustom::Plus.__init__)


def test_odemcustom::plus_constructor_args():
    sig = inspect.signature(odemcustom::Plus.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(odemcustom::UnaryOperator)


def test_odemcustom::unaryoperator_constructor_exists():
    assert callable(odemcustom::UnaryOperator.__init__)


def test_odemcustom::unaryoperator_constructor_args():
    sig = inspect.signature(odemcustom::UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::binaryoperator_is_not_abstract():
    assert not inspect.isabstract(odemcustom::BinaryOperator)


def test_odemcustom::binaryoperator_constructor_exists():
    assert callable(odemcustom::BinaryOperator.__init__)


def test_odemcustom::binaryoperator_constructor_args():
    sig = inspect.signature(odemcustom::BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::l1expr_is_not_abstract():
    assert not inspect.isabstract(odemcustom::L1Expr)


def test_odemcustom::l1expr_constructor_exists():
    assert callable(odemcustom::L1Expr.__init__)


def test_odemcustom::l1expr_constructor_args():
    sig = inspect.signature(odemcustom::L1Expr.__init__)
    params = list(sig.parameters.keys())



def test_compositestatement_is_not_abstract():
    assert not inspect.isabstract(CompositeStatement)


def test_compositestatement_constructor_exists():
    assert callable(CompositeStatement.__init__)


def test_compositestatement_constructor_args():
    sig = inspect.signature(CompositeStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::whilestatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::WhileStatement)


def test_odemcustom::whilestatement_constructor_exists():
    assert callable(odemcustom::WhileStatement.__init__)


def test_odemcustom::whilestatement_constructor_args():
    sig = inspect.signature(odemcustom::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::foreachstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ForEachStatement)


def test_odemcustom::foreachstatement_constructor_exists():
    assert callable(odemcustom::ForEachStatement.__init__)


def test_odemcustom::foreachstatement_constructor_args():
    sig = inspect.signature(odemcustom::ForEachStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::ifstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::IfStatement)


def test_odemcustom::ifstatement_constructor_exists():
    assert callable(odemcustom::IfStatement.__init__)


def test_odemcustom::ifstatement_constructor_args():
    sig = inspect.signature(odemcustom::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_setstatement_is_not_abstract():
    assert not inspect.isabstract(SetStatement)


def test_setstatement_constructor_exists():
    assert callable(SetStatement.__init__)


def test_setstatement_constructor_args():
    sig = inspect.signature(SetStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::emptyset_is_not_abstract():
    assert not inspect.isabstract(odemcustom::EmptySet)


def test_odemcustom::emptyset_constructor_exists():
    assert callable(odemcustom::EmptySet.__init__)


def test_odemcustom::emptyset_constructor_args():
    sig = inspect.signature(odemcustom::EmptySet.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::addtoset_is_not_abstract():
    assert not inspect.isabstract(odemcustom::AddToSet)


def test_odemcustom::addtoset_constructor_exists():
    assert callable(odemcustom::AddToSet.__init__)


def test_odemcustom::addtoset_constructor_args():
    sig = inspect.signature(odemcustom::AddToSet.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::removefromset_is_not_abstract():
    assert not inspect.isabstract(odemcustom::RemoveFromSet)


def test_odemcustom::removefromset_constructor_exists():
    assert callable(odemcustom::RemoveFromSet.__init__)


def test_odemcustom::removefromset_constructor_args():
    sig = inspect.signature(odemcustom::RemoveFromSet.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::statementexpression_is_not_abstract():
    assert not inspect.isabstract(odemcustom::StatementExpression)


def test_odemcustom::statementexpression_constructor_exists():
    assert callable(odemcustom::StatementExpression.__init__)


def test_odemcustom::statementexpression_constructor_args():
    sig = inspect.signature(odemcustom::StatementExpression.__init__)
    params = list(sig.parameters.keys())



def test_simplestatement_is_not_abstract():
    assert not inspect.isabstract(SimpleStatement)


def test_simplestatement_constructor_exists():
    assert callable(SimpleStatement.__init__)


def test_simplestatement_constructor_args():
    sig = inspect.signature(SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::print_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Print)


def test_odemcustom::print_constructor_exists():
    assert callable(odemcustom::Print.__init__)


def test_odemcustom::print_constructor_args():
    sig = inspect.signature(odemcustom::Print.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::breakstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::BreakStatement)


def test_odemcustom::breakstatement_constructor_exists():
    assert callable(odemcustom::BreakStatement.__init__)


def test_odemcustom::breakstatement_constructor_args():
    sig = inspect.signature(odemcustom::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::assignment_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Assignment)


def test_odemcustom::assignment_constructor_exists():
    assert callable(odemcustom::Assignment.__init__)


def test_odemcustom::assignment_constructor_args():
    sig = inspect.signature(odemcustom::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::setstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::SetStatement)


def test_odemcustom::setstatement_constructor_exists():
    assert callable(odemcustom::SetStatement.__init__)


def test_odemcustom::setstatement_constructor_args():
    sig = inspect.signature(odemcustom::SetStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::advance_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Advance)


def test_odemcustom::advance_constructor_exists():
    assert callable(odemcustom::Advance.__init__)


def test_odemcustom::advance_constructor_args():
    sig = inspect.signature(odemcustom::Advance.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::continuestatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ContinueStatement)


def test_odemcustom::continuestatement_constructor_exists():
    assert callable(odemcustom::ContinueStatement.__init__)


def test_odemcustom::continuestatement_constructor_args():
    sig = inspect.signature(odemcustom::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ExpressionStatement)


def test_odemcustom::expressionstatement_constructor_exists():
    assert callable(odemcustom::ExpressionStatement.__init__)


def test_odemcustom::expressionstatement_constructor_args():
    sig = inspect.signature(odemcustom::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_construct_is_not_abstract():
    assert not inspect.isabstract(Construct)


def test_construct_constructor_exists():
    assert callable(Construct.__init__)


def test_construct_constructor_args():
    sig = inspect.signature(Construct.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::statement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Statement)


def test_odemcustom::statement_constructor_exists():
    assert callable(odemcustom::Statement.__init__)


def test_odemcustom::statement_constructor_args():
    sig = inspect.signature(odemcustom::Statement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::codeblock_is_not_abstract():
    assert not inspect.isabstract(odemcustom::CodeBlock)


def test_odemcustom::codeblock_constructor_exists():
    assert callable(odemcustom::CodeBlock.__init__)


def test_odemcustom::codeblock_constructor_args():
    sig = inspect.signature(odemcustom::CodeBlock.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::activateobject_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ActivateObject)


def test_odemcustom::activateobject_constructor_exists():
    assert callable(odemcustom::ActivateObject.__init__)


def test_odemcustom::activateobject_constructor_args():
    sig = inspect.signature(odemcustom::ActivateObject.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"

def test_odemcustom::activateobject_has_priority():
    assert hasattr(odemcustom::ActivateObject, "priority")
    descriptor = None
    for klass in odemcustom::ActivateObject.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom::reactivate_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Reactivate)


def test_odemcustom::reactivate_constructor_exists():
    assert callable(odemcustom::Reactivate.__init__)


def test_odemcustom::reactivate_constructor_args():
    sig = inspect.signature(odemcustom::Reactivate.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::wait_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Wait)


def test_odemcustom::wait_constructor_exists():
    assert callable(odemcustom::Wait.__init__)


def test_odemcustom::wait_constructor_args():
    sig = inspect.signature(odemcustom::Wait.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::terminate_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Terminate)


def test_odemcustom::terminate_constructor_exists():
    assert callable(odemcustom::Terminate.__init__)


def test_odemcustom::terminate_constructor_args():
    sig = inspect.signature(odemcustom::Terminate.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::waituntil_is_not_abstract():
    assert not inspect.isabstract(odemcustom::WaitUntil)


def test_odemcustom::waituntil_constructor_exists():
    assert callable(odemcustom::WaitUntil.__init__)


def test_odemcustom::waituntil_constructor_args():
    sig = inspect.signature(odemcustom::WaitUntil.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::return_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Return)


def test_odemcustom::return_constructor_exists():
    assert callable(odemcustom::Return.__init__)


def test_odemcustom::return_constructor_args():
    sig = inspect.signature(odemcustom::Return.__init__)
    params = list(sig.parameters.keys())



def test_statementexpression_is_not_abstract():
    assert not inspect.isabstract(StatementExpression)


def test_statementexpression_constructor_exists():
    assert callable(StatementExpression.__init__)


def test_statementexpression_constructor_args():
    sig = inspect.signature(StatementExpression.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::procedurecall_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ProcedureCall)


def test_odemcustom::procedurecall_constructor_exists():
    assert callable(odemcustom::ProcedureCall.__init__)


def test_odemcustom::procedurecall_constructor_args():
    sig = inspect.signature(odemcustom::ProcedureCall.__init__)
    params = list(sig.parameters.keys())



def test_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(ExpressionStatement)


def test_expressionstatement_constructor_exists():
    assert callable(ExpressionStatement.__init__)


def test_expressionstatement_constructor_args():
    sig = inspect.signature(ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::deprecatedprocedurecallstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::DeprecatedProcedureCallStatement)


def test_odemcustom::deprecatedprocedurecallstatement_constructor_exists():
    assert callable(odemcustom::DeprecatedProcedureCallStatement.__init__)


def test_odemcustom::deprecatedprocedurecallstatement_constructor_args():
    sig = inspect.signature(odemcustom::DeprecatedProcedureCallStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::constructor_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Constructor)


def test_odemcustom::constructor_constructor_exists():
    assert callable(odemcustom::Constructor.__init__)


def test_odemcustom::constructor_constructor_args():
    sig = inspect.signature(odemcustom::Constructor.__init__)
    params = list(sig.parameters.keys())



def test_classsimilar_is_not_abstract():
    assert not inspect.isabstract(ClassSimilar)


def test_classsimilar_constructor_exists():
    assert callable(ClassSimilar.__init__)


def test_classsimilar_constructor_args():
    sig = inspect.signature(ClassSimilar.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_expandableelement_is_not_abstract():
    assert not inspect.isabstract(ExpandableElement)


def test_expandableelement_constructor_exists():
    assert callable(ExpandableElement.__init__)


def test_expandableelement_constructor_args():
    sig = inspect.signature(ExpandableElement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::namedelement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::NamedElement)


def test_odemcustom::namedelement_constructor_exists():
    assert callable(odemcustom::NamedElement.__init__)


def test_odemcustom::namedelement_constructor_args():
    sig = inspect.signature(odemcustom::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_odemcustom::namedelement_has_name():
    assert hasattr(odemcustom::NamedElement, "name")
    descriptor = None
    for klass in odemcustom::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::compositestatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::CompositeStatement)


def test_odemcustom::compositestatement_constructor_exists():
    assert callable(odemcustom::CompositeStatement.__init__)


def test_odemcustom::compositestatement_constructor_args():
    sig = inspect.signature(odemcustom::CompositeStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::simplestatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::SimpleStatement)


def test_odemcustom::simplestatement_constructor_exists():
    assert callable(odemcustom::SimpleStatement.__init__)


def test_odemcustom::simplestatement_constructor_args():
    sig = inspect.signature(odemcustom::SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(AbstractVariable)


def test_abstractvariable_constructor_exists():
    assert callable(AbstractVariable.__init__)


def test_abstractvariable_constructor_args():
    sig = inspect.signature(AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::annotatableelement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::AnnotatableElement)


def test_odemcustom::annotatableelement_constructor_exists():
    assert callable(odemcustom::AnnotatableElement.__init__)


def test_odemcustom::annotatableelement_constructor_args():
    sig = inspect.signature(odemcustom::AnnotatableElement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::expression_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Expression)


def test_odemcustom::expression_constructor_exists():
    assert callable(odemcustom::Expression.__init__)


def test_odemcustom::expression_constructor_args():
    sig = inspect.signature(odemcustom::Expression.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::keyvaluepair_is_not_abstract():
    assert not inspect.isabstract(odemcustom::KeyValuePair)


def test_odemcustom::keyvaluepair_constructor_exists():
    assert callable(odemcustom::KeyValuePair.__init__)


def test_odemcustom::keyvaluepair_constructor_args():
    sig = inspect.signature(odemcustom::KeyValuePair.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::annotationapplication_is_not_abstract():
    assert not inspect.isabstract(odemcustom::AnnotationApplication)


def test_odemcustom::annotationapplication_constructor_exists():
    assert callable(odemcustom::AnnotationApplication.__init__)


def test_odemcustom::annotationapplication_constructor_args():
    sig = inspect.signature(odemcustom::AnnotationApplication.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::interface_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Interface)


def test_odemcustom::interface_constructor_exists():
    assert callable(odemcustom::Interface.__init__)


def test_odemcustom::interface_constructor_args():
    sig = inspect.signature(odemcustom::Interface.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::clazz_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Clazz)


def test_odemcustom::clazz_constructor_exists():
    assert callable(odemcustom::Clazz.__init__)


def test_odemcustom::clazz_constructor_args():
    sig = inspect.signature(odemcustom::Clazz.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"

def test_odemcustom::clazz_has_active():
    assert hasattr(odemcustom::Clazz, "active")
    descriptor = None
    for klass in odemcustom::Clazz.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)



def test_modifierextensionscontainer_is_not_abstract():
    assert not inspect.isabstract(ModifierExtensionsContainer)


def test_modifierextensionscontainer_constructor_exists():
    assert callable(ModifierExtensionsContainer.__init__)


def test_modifierextensionscontainer_constructor_args():
    sig = inspect.signature(ModifierExtensionsContainer.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::nativebinding_is_not_abstract():
    assert not inspect.isabstract(odemcustom::NativeBinding)


def test_odemcustom::nativebinding_constructor_exists():
    assert callable(odemcustom::NativeBinding.__init__)


def test_odemcustom::nativebinding_constructor_args():
    sig = inspect.signature(odemcustom::NativeBinding.__init__)
    params = list(sig.parameters.keys())
    assert "targetType" in params, "Missing parameter 'targetType'"
    assert "targetLanguage" in params, "Missing parameter 'targetLanguage'"

def test_odemcustom::nativebinding_has_targetType():
    assert hasattr(odemcustom::NativeBinding, "targetType")
    descriptor = None
    for klass in odemcustom::NativeBinding.__mro__:
        if "targetType" in klass.__dict__:
            descriptor = klass.__dict__["targetType"]
            break
    assert isinstance(descriptor, property)

def test_odemcustom::nativebinding_has_targetLanguage():
    assert hasattr(odemcustom::NativeBinding, "targetLanguage")
    descriptor = None
    for klass in odemcustom::NativeBinding.__mro__:
        if "targetLanguage" in klass.__dict__:
            descriptor = klass.__dict__["targetLanguage"]
            break
    assert isinstance(descriptor, property)



def test_referablerhstype_is_not_abstract():
    assert not inspect.isabstract(ReferableRhsType)


def test_referablerhstype_constructor_exists():
    assert callable(ReferableRhsType.__init__)


def test_referablerhstype_constructor_args():
    sig = inspect.signature(ReferableRhsType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::typedelement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::TypedElement)


def test_odemcustom::typedelement_constructor_exists():
    assert callable(odemcustom::TypedElement.__init__)


def test_odemcustom::typedelement_constructor_args():
    sig = inspect.signature(odemcustom::TypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "isList" in params, "Missing parameter 'isList'"

def test_odemcustom::typedelement_has_isList():
    assert hasattr(odemcustom::TypedElement, "isList")
    descriptor = None
    for klass in odemcustom::TypedElement.__mro__:
        if "isList" in klass.__dict__:
            descriptor = klass.__dict__["isList"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom::type_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Type)


def test_odemcustom::type_constructor_exists():
    assert callable(odemcustom::Type.__init__)


def test_odemcustom::type_constructor_args():
    sig = inspect.signature(odemcustom::Type.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::modifierextensionscontainer_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ModifierExtensionsContainer)


def test_odemcustom::modifierextensionscontainer_constructor_exists():
    assert callable(odemcustom::ModifierExtensionsContainer.__init__)


def test_odemcustom::modifierextensionscontainer_constructor_args():
    sig = inspect.signature(odemcustom::ModifierExtensionsContainer.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::extension_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Extension)


def test_odemcustom::extension_constructor_exists():
    assert callable(odemcustom::Extension.__init__)


def test_odemcustom::extension_constructor_args():
    sig = inspect.signature(odemcustom::Extension.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::embeddableextensionscontainer_is_not_abstract():
    assert not inspect.isabstract(odemcustom::EmbeddableExtensionsContainer)


def test_odemcustom::embeddableextensionscontainer_constructor_exists():
    assert callable(odemcustom::EmbeddableExtensionsContainer.__init__)


def test_odemcustom::embeddableextensionscontainer_constructor_args():
    sig = inspect.signature(odemcustom::EmbeddableExtensionsContainer.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::idresolution_is_not_abstract():
    assert not inspect.isabstract(odemcustom::IdResolution)


def test_odemcustom::idresolution_constructor_exists():
    assert callable(odemcustom::IdResolution.__init__)


def test_odemcustom::idresolution_constructor_args():
    sig = inspect.signature(odemcustom::IdResolution.__init__)
    params = list(sig.parameters.keys())
    assert "metaModelPlatformURI" in params, "Missing parameter 'metaModelPlatformURI'"

def test_odemcustom::idresolution_has_metaModelPlatformURI():
    assert hasattr(odemcustom::IdResolution, "metaModelPlatformURI")
    descriptor = None
    for klass in odemcustom::IdResolution.__mro__:
        if "metaModelPlatformURI" in klass.__dict__:
            descriptor = klass.__dict__["metaModelPlatformURI"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom::variable_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Variable)


def test_odemcustom::variable_constructor_exists():
    assert callable(odemcustom::Variable.__init__)


def test_odemcustom::variable_constructor_args():
    sig = inspect.signature(odemcustom::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "control" in params, "Missing parameter 'control'"
    assert "clazz" in params, "Missing parameter 'clazz'"

def test_odemcustom::variable_has_control():
    assert hasattr(odemcustom::Variable, "control")
    descriptor = None
    for klass in odemcustom::Variable.__mro__:
        if "control" in klass.__dict__:
            descriptor = klass.__dict__["control"]
            break
    assert isinstance(descriptor, property)

def test_odemcustom::variable_has_clazz():
    assert hasattr(odemcustom::Variable, "clazz")
    descriptor = None
    for klass in odemcustom::Variable.__mro__:
        if "clazz" in klass.__dict__:
            descriptor = klass.__dict__["clazz"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom::parameter_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Parameter)


def test_odemcustom::parameter_constructor_exists():
    assert callable(odemcustom::Parameter.__init__)


def test_odemcustom::parameter_constructor_args():
    sig = inspect.signature(odemcustom::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_annotatableelement_is_not_abstract():
    assert not inspect.isabstract(AnnotatableElement)


def test_annotatableelement_constructor_exists():
    assert callable(AnnotatableElement.__init__)


def test_annotatableelement_constructor_args():
    sig = inspect.signature(AnnotatableElement.__init__)
    params = list(sig.parameters.keys())



def test_codeblock_is_not_abstract():
    assert not inspect.isabstract(CodeBlock)


def test_codeblock_constructor_exists():
    assert callable(CodeBlock.__init__)


def test_codeblock_constructor_args():
    sig = inspect.signature(CodeBlock.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::startcodeblock_is_not_abstract():
    assert not inspect.isabstract(odemcustom::StartCodeBlock)


def test_odemcustom::startcodeblock_constructor_exists():
    assert callable(odemcustom::StartCodeBlock.__init__)


def test_odemcustom::startcodeblock_constructor_args():
    sig = inspect.signature(odemcustom::StartCodeBlock.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::inttype_is_not_abstract():
    assert not inspect.isabstract(odemcustom::IntType)


def test_odemcustom::inttype_constructor_exists():
    assert callable(odemcustom::IntType.__init__)


def test_odemcustom::inttype_constructor_args():
    sig = inspect.signature(odemcustom::IntType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::booltype_is_not_abstract():
    assert not inspect.isabstract(odemcustom::BoolType)


def test_odemcustom::booltype_constructor_exists():
    assert callable(odemcustom::BoolType.__init__)


def test_odemcustom::booltype_constructor_args():
    sig = inspect.signature(odemcustom::BoolType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::doubletype_is_not_abstract():
    assert not inspect.isabstract(odemcustom::DoubleType)


def test_odemcustom::doubletype_constructor_exists():
    assert callable(odemcustom::DoubleType.__init__)


def test_odemcustom::doubletype_constructor_args():
    sig = inspect.signature(odemcustom::DoubleType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::stringtype_is_not_abstract():
    assert not inspect.isabstract(odemcustom::StringType)


def test_odemcustom::stringtype_constructor_exists():
    assert callable(odemcustom::StringType.__init__)


def test_odemcustom::stringtype_constructor_args():
    sig = inspect.signature(odemcustom::StringType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::voidtype_is_not_abstract():
    assert not inspect.isabstract(odemcustom::VoidType)


def test_odemcustom::voidtype_constructor_exists():
    assert callable(odemcustom::VoidType.__init__)


def test_odemcustom::voidtype_constructor_args():
    sig = inspect.signature(odemcustom::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::idexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom::IdExpr)


def test_odemcustom::idexpr_constructor_exists():
    assert callable(odemcustom::IdExpr.__init__)


def test_odemcustom::idexpr_constructor_args():
    sig = inspect.signature(odemcustom::IdExpr.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::primitivetype_is_not_abstract():
    assert not inspect.isabstract(odemcustom::PrimitiveType)


def test_odemcustom::primitivetype_constructor_exists():
    assert callable(odemcustom::PrimitiveType.__init__)


def test_odemcustom::primitivetype_constructor_args():
    sig = inspect.signature(odemcustom::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::import_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Import)


def test_odemcustom::import_constructor_exists():
    assert callable(odemcustom::Import.__init__)


def test_odemcustom::import_constructor_args():
    sig = inspect.signature(odemcustom::Import.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_odemcustom::import_has_file():
    assert hasattr(odemcustom::Import, "file")
    descriptor = None
    for klass in odemcustom::Import.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom::model_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Model)


def test_odemcustom::model_constructor_exists():
    assert callable(odemcustom::Model.__init__)


def test_odemcustom::model_constructor_args():
    sig = inspect.signature(odemcustom::Model.__init__)
    params = list(sig.parameters.keys())



def test_namedextension_is_not_abstract():
    assert not inspect.isabstract(NamedExtension)


def test_namedextension_constructor_exists():
    assert callable(NamedExtension.__init__)


def test_namedextension_constructor_args():
    sig = inspect.signature(NamedExtension.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::classaugment_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ClassAugment)


def test_odemcustom::classaugment_constructor_exists():
    assert callable(odemcustom::ClassAugment.__init__)


def test_odemcustom::classaugment_constructor_args():
    sig = inspect.signature(odemcustom::ClassAugment.__init__)
    params = list(sig.parameters.keys())



def test_embeddableextensionscontainer_is_not_abstract():
    assert not inspect.isabstract(EmbeddableExtensionsContainer)


def test_embeddableextensionscontainer_constructor_exists():
    assert callable(EmbeddableExtensionsContainer.__init__)


def test_embeddableextensionscontainer_constructor_args():
    sig = inspect.signature(EmbeddableExtensionsContainer.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::classsimilar_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ClassSimilar)


def test_odemcustom::classsimilar_constructor_exists():
    assert callable(odemcustom::ClassSimilar.__init__)


def test_odemcustom::classsimilar_constructor_args():
    sig = inspect.signature(odemcustom::ClassSimilar.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::classifier_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Classifier)


def test_odemcustom::classifier_constructor_exists():
    assert callable(odemcustom::Classifier.__init__)


def test_odemcustom::classifier_constructor_args():
    sig = inspect.signature(odemcustom::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::abstractvariable_is_not_abstract():
    assert not inspect.isabstract(odemcustom::AbstractVariable)


def test_odemcustom::abstractvariable_constructor_exists():
    assert callable(odemcustom::AbstractVariable.__init__)


def test_odemcustom::abstractvariable_constructor_args():
    sig = inspect.signature(odemcustom::AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::simpleannotation_is_not_abstract():
    assert not inspect.isabstract(odemcustom::SimpleAnnotation)


def test_odemcustom::simpleannotation_constructor_exists():
    assert callable(odemcustom::SimpleAnnotation.__init__)


def test_odemcustom::simpleannotation_constructor_args():
    sig = inspect.signature(odemcustom::SimpleAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_odemcustom::simpleannotation_has_value():
    assert hasattr(odemcustom::SimpleAnnotation, "value")
    descriptor = None
    for klass in odemcustom::SimpleAnnotation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom::extensiondefinition_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ExtensionDefinition)


def test_odemcustom::extensiondefinition_constructor_exists():
    assert callable(odemcustom::ExtensionDefinition.__init__)


def test_odemcustom::extensiondefinition_constructor_args():
    sig = inspect.signature(odemcustom::ExtensionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::annotation_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Annotation)


def test_odemcustom::annotation_constructor_exists():
    assert callable(odemcustom::Annotation.__init__)


def test_odemcustom::annotation_constructor_args():
    sig = inspect.signature(odemcustom::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::procedure_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Procedure)


def test_odemcustom::procedure_constructor_exists():
    assert callable(odemcustom::Procedure.__init__)


def test_odemcustom::procedure_constructor_args():
    sig = inspect.signature(odemcustom::Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "clazz" in params, "Missing parameter 'clazz'"

def test_odemcustom::procedure_has_clazz():
    assert hasattr(odemcustom::Procedure, "clazz")
    descriptor = None
    for klass in odemcustom::Procedure.__mro__:
        if "clazz" in klass.__dict__:
            descriptor = klass.__dict__["clazz"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom::module_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Module)


def test_odemcustom::module_constructor_exists():
    assert callable(odemcustom::Module.__init__)


def test_odemcustom::module_constructor_args():
    sig = inspect.signature(odemcustom::Module.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::construct_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Construct)


def test_odemcustom::construct_constructor_exists():
    assert callable(odemcustom::Construct.__init__)


def test_odemcustom::construct_constructor_args():
    sig = inspect.signature(odemcustom::Construct.__init__)
    params = list(sig.parameters.keys())
    assert "concreteSyntax" in params, "Missing parameter 'concreteSyntax'"

def test_odemcustom::construct_has_concreteSyntax():
    assert hasattr(odemcustom::Construct, "concreteSyntax")
    descriptor = None
    for klass in odemcustom::Construct.__mro__:
        if "concreteSyntax" in klass.__dict__:
            descriptor = klass.__dict__["concreteSyntax"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom::potentiallyhiddenidelements_is_not_abstract():
    assert not inspect.isabstract(odemcustom::PotentiallyHiddenIdElements)


def test_odemcustom::potentiallyhiddenidelements_constructor_exists():
    assert callable(odemcustom::PotentiallyHiddenIdElements.__init__)


def test_odemcustom::potentiallyhiddenidelements_constructor_args():
    sig = inspect.signature(odemcustom::PotentiallyHiddenIdElements.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::includepattern_is_not_abstract():
    assert not inspect.isabstract(odemcustom::IncludePattern)


def test_odemcustom::includepattern_constructor_exists():
    assert callable(odemcustom::IncludePattern.__init__)


def test_odemcustom::includepattern_constructor_args():
    sig = inspect.signature(odemcustom::IncludePattern.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::consideridelements_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ConsiderIdElements)


def test_odemcustom::consideridelements_constructor_exists():
    assert callable(odemcustom::ConsiderIdElements.__init__)


def test_odemcustom::consideridelements_constructor_args():
    sig = inspect.signature(odemcustom::ConsiderIdElements.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::findcontainer_is_not_abstract():
    assert not inspect.isabstract(odemcustom::FindContainer)


def test_odemcustom::findcontainer_constructor_exists():
    assert callable(odemcustom::FindContainer.__init__)


def test_odemcustom::findcontainer_constructor_args():
    sig = inspect.signature(odemcustom::FindContainer.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::expandstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ExpandStatement)


def test_odemcustom::expandstatement_constructor_exists():
    assert callable(odemcustom::ExpandStatement.__init__)


def test_odemcustom::expandstatement_constructor_args():
    sig = inspect.signature(odemcustom::ExpandStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::expandexpression_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ExpandExpression)


def test_odemcustom::expandexpression_constructor_exists():
    assert callable(odemcustom::ExpandExpression.__init__)


def test_odemcustom::expandexpression_constructor_args():
    sig = inspect.signature(odemcustom::ExpandExpression.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::teststatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::TestStatement)


def test_odemcustom::teststatement_constructor_exists():
    assert callable(odemcustom::TestStatement.__init__)


def test_odemcustom::teststatement_constructor_args():
    sig = inspect.signature(odemcustom::TestStatement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_odemcustom::teststatement_has_value():
    assert hasattr(odemcustom::TestStatement, "value")
    descriptor = None
    for klass in odemcustom::TestStatement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom::expandableelement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ExpandableElement)


def test_odemcustom::expandableelement_constructor_exists():
    assert callable(odemcustom::ExpandableElement.__init__)


def test_odemcustom::expandableelement_constructor_args():
    sig = inspect.signature(odemcustom::ExpandableElement.__init__)
    params = list(sig.parameters.keys())



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
    params = list(sig.parameters.keys())



def test_quotedcode_is_not_abstract():
    assert not inspect.isabstract(QuotedCode)


def test_quotedcode_constructor_exists():
    assert callable(QuotedCode.__init__)


def test_quotedcode_constructor_args():
    sig = inspect.signature(QuotedCode.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::quotedmodulecontent_is_not_abstract():
    assert not inspect.isabstract(odemcustom::QuotedModuleContent)


def test_odemcustom::quotedmodulecontent_constructor_exists():
    assert callable(odemcustom::QuotedModuleContent.__init__)


def test_odemcustom::quotedmodulecontent_constructor_args():
    sig = inspect.signature(odemcustom::QuotedModuleContent.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::quotedstatements_is_not_abstract():
    assert not inspect.isabstract(odemcustom::QuotedStatements)


def test_odemcustom::quotedstatements_constructor_exists():
    assert callable(odemcustom::QuotedStatements.__init__)


def test_odemcustom::quotedstatements_constructor_args():
    sig = inspect.signature(odemcustom::QuotedStatements.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::quotedclasscontent_is_not_abstract():
    assert not inspect.isabstract(odemcustom::QuotedClassContent)


def test_odemcustom::quotedclasscontent_constructor_exists():
    assert callable(odemcustom::QuotedClassContent.__init__)


def test_odemcustom::quotedclasscontent_constructor_args():
    sig = inspect.signature(odemcustom::QuotedClassContent.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::quotedexpression_is_not_abstract():
    assert not inspect.isabstract(odemcustom::QuotedExpression)


def test_odemcustom::quotedexpression_constructor_exists():
    assert callable(odemcustom::QuotedExpression.__init__)


def test_odemcustom::quotedexpression_constructor_args():
    sig = inspect.signature(odemcustom::QuotedExpression.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::quotedcode_is_not_abstract():
    assert not inspect.isabstract(odemcustom::QuotedCode)


def test_odemcustom::quotedcode_constructor_exists():
    assert callable(odemcustom::QuotedCode.__init__)


def test_odemcustom::quotedcode_constructor_args():
    sig = inspect.signature(odemcustom::QuotedCode.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::codequoteexpression_is_not_abstract():
    assert not inspect.isabstract(odemcustom::CodeQuoteExpression)


def test_odemcustom::codequoteexpression_constructor_exists():
    assert callable(odemcustom::CodeQuoteExpression.__init__)


def test_odemcustom::codequoteexpression_constructor_args():
    sig = inspect.signature(odemcustom::CodeQuoteExpression.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::expandsection_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ExpandSection)


def test_odemcustom::expandsection_constructor_exists():
    assert callable(odemcustom::ExpandSection.__init__)


def test_odemcustom::expandsection_constructor_args():
    sig = inspect.signature(odemcustom::ExpandSection.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::targetstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::TargetStatement)


def test_odemcustom::targetstatement_constructor_exists():
    assert callable(odemcustom::TargetStatement.__init__)


def test_odemcustom::targetstatement_constructor_args():
    sig = inspect.signature(odemcustom::TargetStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::metaexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom::MetaExpr)


def test_odemcustom::metaexpr_constructor_exists():
    assert callable(odemcustom::MetaExpr.__init__)


def test_odemcustom::metaexpr_constructor_args():
    sig = inspect.signature(odemcustom::MetaExpr.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::mappingpart_is_not_abstract():
    assert not inspect.isabstract(odemcustom::MappingPart)


def test_odemcustom::mappingpart_constructor_exists():
    assert callable(odemcustom::MappingPart.__init__)


def test_odemcustom::mappingpart_constructor_args():
    sig = inspect.signature(odemcustom::MappingPart.__init__)
    params = list(sig.parameters.keys())



def test_mappingpart_is_not_abstract():
    assert not inspect.isabstract(MappingPart)


def test_mappingpart_constructor_exists():
    assert callable(MappingPart.__init__)


def test_mappingpart_constructor_args():
    sig = inspect.signature(MappingPart.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::dynamicmappingpart_is_not_abstract():
    assert not inspect.isabstract(odemcustom::DynamicMappingPart)


def test_odemcustom::dynamicmappingpart_constructor_exists():
    assert callable(odemcustom::DynamicMappingPart.__init__)


def test_odemcustom::dynamicmappingpart_constructor_args():
    sig = inspect.signature(odemcustom::DynamicMappingPart.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::fixedmappingpart_is_not_abstract():
    assert not inspect.isabstract(odemcustom::FixedMappingPart)


def test_odemcustom::fixedmappingpart_constructor_exists():
    assert callable(odemcustom::FixedMappingPart.__init__)


def test_odemcustom::fixedmappingpart_constructor_args():
    sig = inspect.signature(odemcustom::FixedMappingPart.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_odemcustom::fixedmappingpart_has_code():
    assert hasattr(odemcustom::FixedMappingPart, "code")
    descriptor = None
    for klass in odemcustom::FixedMappingPart.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom::resumegenstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ResumeGenStatement)


def test_odemcustom::resumegenstatement_constructor_exists():
    assert callable(odemcustom::ResumeGenStatement.__init__)


def test_odemcustom::resumegenstatement_constructor_args():
    sig = inspect.signature(odemcustom::ResumeGenStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::savegenstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::SaveGenStatement)


def test_odemcustom::savegenstatement_constructor_exists():
    assert callable(odemcustom::SaveGenStatement.__init__)


def test_odemcustom::savegenstatement_constructor_args():
    sig = inspect.signature(odemcustom::SaveGenStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::resetgencontextstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ResetGenContextStatement)


def test_odemcustom::resetgencontextstatement_constructor_exists():
    assert callable(odemcustom::ResetGenContextStatement.__init__)


def test_odemcustom::resetgencontextstatement_constructor_args():
    sig = inspect.signature(odemcustom::ResetGenContextStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::setgencontextstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::SetGenContextStatement)


def test_odemcustom::setgencontextstatement_constructor_exists():
    assert callable(odemcustom::SetGenContextStatement.__init__)


def test_odemcustom::setgencontextstatement_constructor_args():
    sig = inspect.signature(odemcustom::SetGenContextStatement.__init__)
    params = list(sig.parameters.keys())
    assert "addAfterContext" in params, "Missing parameter 'addAfterContext'"

def test_odemcustom::setgencontextstatement_has_addAfterContext():
    assert hasattr(odemcustom::SetGenContextStatement, "addAfterContext")
    descriptor = None
    for klass in odemcustom::SetGenContextStatement.__mro__:
        if "addAfterContext" in klass.__dict__:
            descriptor = klass.__dict__["addAfterContext"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom::mappingstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::MappingStatement)


def test_odemcustom::mappingstatement_constructor_exists():
    assert callable(odemcustom::MappingStatement.__init__)


def test_odemcustom::mappingstatement_constructor_args():
    sig = inspect.signature(odemcustom::MappingStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::pattern_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Pattern)


def test_odemcustom::pattern_constructor_exists():
    assert callable(odemcustom::Pattern.__init__)


def test_odemcustom::pattern_constructor_args():
    sig = inspect.signature(odemcustom::Pattern.__init__)
    params = list(sig.parameters.keys())
    assert "top" in params, "Missing parameter 'top'"

def test_odemcustom::pattern_has_top():
    assert hasattr(odemcustom::Pattern, "top")
    descriptor = None
    for klass in odemcustom::Pattern.__mro__:
        if "top" in klass.__dict__:
            descriptor = klass.__dict__["top"]
            break
    assert isinstance(descriptor, property)



def test_structuredpropertytype_is_not_abstract():
    assert not inspect.isabstract(StructuredPropertyType)


def test_structuredpropertytype_constructor_exists():
    assert callable(StructuredPropertyType.__init__)


def test_structuredpropertytype_constructor_args():
    sig = inspect.signature(StructuredPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::referencepropertytype_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ReferencePropertyType)


def test_odemcustom::referencepropertytype_constructor_exists():
    assert callable(odemcustom::ReferencePropertyType.__init__)


def test_odemcustom::referencepropertytype_constructor_args():
    sig = inspect.signature(odemcustom::ReferencePropertyType.__init__)
    params = list(sig.parameters.keys())
    assert "rawReference" in params, "Missing parameter 'rawReference'"

def test_odemcustom::referencepropertytype_has_rawReference():
    assert hasattr(odemcustom::ReferencePropertyType, "rawReference")
    descriptor = None
    for klass in odemcustom::ReferencePropertyType.__mro__:
        if "rawReference" in klass.__dict__:
            descriptor = klass.__dict__["rawReference"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom::compositepropertytype_is_not_abstract():
    assert not inspect.isabstract(odemcustom::CompositePropertyType)


def test_odemcustom::compositepropertytype_constructor_exists():
    assert callable(odemcustom::CompositePropertyType.__init__)


def test_odemcustom::compositepropertytype_constructor_args():
    sig = inspect.signature(odemcustom::CompositePropertyType.__init__)
    params = list(sig.parameters.keys())
    assert "list" in params, "Missing parameter 'list'"

def test_odemcustom::compositepropertytype_has_list():
    assert hasattr(odemcustom::CompositePropertyType, "list")
    descriptor = None
    for klass in odemcustom::CompositePropertyType.__mro__:
        if "list" in klass.__dict__:
            descriptor = klass.__dict__["list"]
            break
    assert isinstance(descriptor, property)



def test_propertytype_is_not_abstract():
    assert not inspect.isabstract(PropertyType)


def test_propertytype_constructor_exists():
    assert callable(PropertyType.__init__)


def test_propertytype_constructor_args():
    sig = inspect.signature(PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::stringpropertytype_is_not_abstract():
    assert not inspect.isabstract(odemcustom::StringPropertyType)


def test_odemcustom::stringpropertytype_constructor_exists():
    assert callable(odemcustom::StringPropertyType.__init__)


def test_odemcustom::stringpropertytype_constructor_args():
    sig = inspect.signature(odemcustom::StringPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::intpropertytype_is_not_abstract():
    assert not inspect.isabstract(odemcustom::IntPropertyType)


def test_odemcustom::intpropertytype_constructor_exists():
    assert callable(odemcustom::IntPropertyType.__init__)


def test_odemcustom::intpropertytype_constructor_args():
    sig = inspect.signature(odemcustom::IntPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::structuredpropertytype_is_not_abstract():
    assert not inspect.isabstract(odemcustom::StructuredPropertyType)


def test_odemcustom::structuredpropertytype_constructor_exists():
    assert callable(odemcustom::StructuredPropertyType.__init__)


def test_odemcustom::structuredpropertytype_constructor_args():
    sig = inspect.signature(odemcustom::StructuredPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::booleanpropertytype_is_not_abstract():
    assert not inspect.isabstract(odemcustom::BooleanPropertyType)


def test_odemcustom::booleanpropertytype_constructor_exists():
    assert callable(odemcustom::BooleanPropertyType.__init__)


def test_odemcustom::booleanpropertytype_constructor_args():
    sig = inspect.signature(odemcustom::BooleanPropertyType.__init__)
    params = list(sig.parameters.keys())
    assert "terminal" in params, "Missing parameter 'terminal'"

def test_odemcustom::booleanpropertytype_has_terminal():
    assert hasattr(odemcustom::BooleanPropertyType, "terminal")
    descriptor = None
    for klass in odemcustom::BooleanPropertyType.__mro__:
        if "terminal" in klass.__dict__:
            descriptor = klass.__dict__["terminal"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom::idpropertytype_is_not_abstract():
    assert not inspect.isabstract(odemcustom::IdPropertyType)


def test_odemcustom::idpropertytype_constructor_exists():
    assert callable(odemcustom::IdPropertyType.__init__)


def test_odemcustom::idpropertytype_constructor_args():
    sig = inspect.signature(odemcustom::IdPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::propertytype_is_not_abstract():
    assert not inspect.isabstract(odemcustom::PropertyType)


def test_odemcustom::propertytype_constructor_exists():
    assert callable(odemcustom::PropertyType.__init__)


def test_odemcustom::propertytype_constructor_args():
    sig = inspect.signature(odemcustom::PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::referablerhstype_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ReferableRhsType)


def test_odemcustom::referablerhstype_constructor_exists():
    assert callable(odemcustom::ReferableRhsType.__init__)


def test_odemcustom::referablerhstype_constructor_args():
    sig = inspect.signature(odemcustom::ReferableRhsType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::tsrule_is_not_abstract():
    assert not inspect.isabstract(odemcustom::TsRule)


def test_odemcustom::tsrule_constructor_exists():
    assert callable(odemcustom::TsRule.__init__)


def test_odemcustom::tsrule_constructor_args():
    sig = inspect.signature(odemcustom::TsRule.__init__)
    params = list(sig.parameters.keys())
    assert "metaClassName" in params, "Missing parameter 'metaClassName'"

def test_odemcustom::tsrule_has_metaClassName():
    assert hasattr(odemcustom::TsRule, "metaClassName")
    descriptor = None
    for klass in odemcustom::TsRule.__mro__:
        if "metaClassName" in klass.__dict__:
            descriptor = klass.__dict__["metaClassName"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom::extensionrule_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ExtensionRule)


def test_odemcustom::extensionrule_constructor_exists():
    assert callable(odemcustom::ExtensionRule.__init__)


def test_odemcustom::extensionrule_constructor_args():
    sig = inspect.signature(odemcustom::ExtensionRule.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::mapping_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Mapping)


def test_odemcustom::mapping_constructor_exists():
    assert callable(odemcustom::Mapping.__init__)


def test_odemcustom::mapping_constructor_args():
    sig = inspect.signature(odemcustom::Mapping.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::textualsyntaxdef_is_not_abstract():
    assert not inspect.isabstract(odemcustom::TextualSyntaxDef)


def test_odemcustom::textualsyntaxdef_constructor_exists():
    assert callable(odemcustom::TextualSyntaxDef.__init__)


def test_odemcustom::textualsyntaxdef_constructor_args():
    sig = inspect.signature(odemcustom::TextualSyntaxDef.__init__)
    params = list(sig.parameters.keys())



def test_rhsexpression_is_not_abstract():
    assert not inspect.isabstract(RhsExpression)


def test_rhsexpression_constructor_exists():
    assert callable(RhsExpression.__init__)


def test_rhsexpression_constructor_args():
    sig = inspect.signature(RhsExpression.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::atleastoneexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom::AtLeastOneExpr)


def test_odemcustom::atleastoneexpr_constructor_exists():
    assert callable(odemcustom::AtLeastOneExpr.__init__)


def test_odemcustom::atleastoneexpr_constructor_args():
    sig = inspect.signature(odemcustom::AtLeastOneExpr.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::arbitraryexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ArbitraryExpr)


def test_odemcustom::arbitraryexpr_constructor_exists():
    assert callable(odemcustom::ArbitraryExpr.__init__)


def test_odemcustom::arbitraryexpr_constructor_args():
    sig = inspect.signature(odemcustom::ArbitraryExpr.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::alternativeexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom::AlternativeExpr)


def test_odemcustom::alternativeexpr_constructor_exists():
    assert callable(odemcustom::AlternativeExpr.__init__)


def test_odemcustom::alternativeexpr_constructor_args():
    sig = inspect.signature(odemcustom::AlternativeExpr.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::propertybindingexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom::PropertyBindingExpr)


def test_odemcustom::propertybindingexpr_constructor_exists():
    assert callable(odemcustom::PropertyBindingExpr.__init__)


def test_odemcustom::propertybindingexpr_constructor_args():
    sig = inspect.signature(odemcustom::PropertyBindingExpr.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_odemcustom::propertybindingexpr_has_operator():
    assert hasattr(odemcustom::PropertyBindingExpr, "operator")
    descriptor = None
    for klass in odemcustom::PropertyBindingExpr.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom::terminalexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom::TerminalExpr)


def test_odemcustom::terminalexpr_constructor_exists():
    assert callable(odemcustom::TerminalExpr.__init__)


def test_odemcustom::terminalexpr_constructor_args():
    sig = inspect.signature(odemcustom::TerminalExpr.__init__)
    params = list(sig.parameters.keys())
    assert "terminal" in params, "Missing parameter 'terminal'"

def test_odemcustom::terminalexpr_has_terminal():
    assert hasattr(odemcustom::TerminalExpr, "terminal")
    descriptor = None
    for klass in odemcustom::TerminalExpr.__mro__:
        if "terminal" in klass.__dict__:
            descriptor = klass.__dict__["terminal"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom::runtimeexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom::RuntimeExpr)


def test_odemcustom::runtimeexpr_constructor_exists():
    assert callable(odemcustom::RuntimeExpr.__init__)


def test_odemcustom::runtimeexpr_constructor_args():
    sig = inspect.signature(odemcustom::RuntimeExpr.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::optionalexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom::OptionalExpr)


def test_odemcustom::optionalexpr_constructor_exists():
    assert callable(odemcustom::OptionalExpr.__init__)


def test_odemcustom::optionalexpr_constructor_args():
    sig = inspect.signature(odemcustom::OptionalExpr.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::sequenceexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom::SequenceExpr)


def test_odemcustom::sequenceexpr_constructor_exists():
    assert callable(odemcustom::SequenceExpr.__init__)


def test_odemcustom::sequenceexpr_constructor_args():
    sig = inspect.signature(odemcustom::SequenceExpr.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::ruleexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom::RuleExpr)


def test_odemcustom::ruleexpr_constructor_exists():
    assert callable(odemcustom::RuleExpr.__init__)


def test_odemcustom::ruleexpr_constructor_args():
    sig = inspect.signature(odemcustom::RuleExpr.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::rhsexpression_is_not_abstract():
    assert not inspect.isabstract(odemcustom::RhsExpression)


def test_odemcustom::rhsexpression_constructor_exists():
    assert callable(odemcustom::RhsExpression.__init__)


def test_odemcustom::rhsexpression_constructor_args():
    sig = inspect.signature(odemcustom::RhsExpression.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::predefinedid_is_not_abstract():
    assert not inspect.isabstract(odemcustom::PredefinedId)


def test_odemcustom::predefinedid_constructor_exists():
    assert callable(odemcustom::PredefinedId.__init__)


def test_odemcustom::predefinedid_constructor_args():
    sig = inspect.signature(odemcustom::PredefinedId.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::depidentifiableelement_is_not_abstract():
    assert not inspect.isabstract(odemcustom::DepIdentifiableElement)


def test_odemcustom::depidentifiableelement_constructor_exists():
    assert callable(odemcustom::DepIdentifiableElement.__init__)


def test_odemcustom::depidentifiableelement_constructor_args():
    sig = inspect.signature(odemcustom::DepIdentifiableElement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::doubleliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom::DoubleLiteral)


def test_odemcustom::doubleliteral_constructor_exists():
    assert callable(odemcustom::DoubleLiteral.__init__)


def test_odemcustom::doubleliteral_constructor_args():
    sig = inspect.signature(odemcustom::DoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_odemcustom::doubleliteral_has_value():
    assert hasattr(odemcustom::DoubleLiteral, "value")
    descriptor = None
    for klass in odemcustom::DoubleLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom::falseliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom::FalseLiteral)


def test_odemcustom::falseliteral_constructor_exists():
    assert callable(odemcustom::FalseLiteral.__init__)


def test_odemcustom::falseliteral_constructor_args():
    sig = inspect.signature(odemcustom::FalseLiteral.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::trueliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom::TrueLiteral)


def test_odemcustom::trueliteral_constructor_exists():
    assert callable(odemcustom::TrueLiteral.__init__)


def test_odemcustom::trueliteral_constructor_args():
    sig = inspect.signature(odemcustom::TrueLiteral.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::modulecontentextension_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ModuleContentExtension)


def test_odemcustom::modulecontentextension_constructor_exists():
    assert callable(odemcustom::ModuleContentExtension.__init__)


def test_odemcustom::modulecontentextension_constructor_args():
    sig = inspect.signature(odemcustom::ModuleContentExtension.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::classcontentextension_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ClassContentExtension)


def test_odemcustom::classcontentextension_constructor_exists():
    assert callable(odemcustom::ClassContentExtension.__init__)


def test_odemcustom::classcontentextension_constructor_args():
    sig = inspect.signature(odemcustom::ClassContentExtension.__init__)
    params = list(sig.parameters.keys())



def test_extension_is_not_abstract():
    assert not inspect.isabstract(Extension)


def test_extension_constructor_exists():
    assert callable(Extension.__init__)


def test_extension_constructor_args():
    sig = inspect.signature(Extension.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::namedextension_is_not_abstract():
    assert not inspect.isabstract(odemcustom::NamedExtension)


def test_odemcustom::namedextension_constructor_exists():
    assert callable(odemcustom::NamedExtension.__init__)


def test_odemcustom::namedextension_constructor_args():
    sig = inspect.signature(odemcustom::NamedExtension.__init__)
    params = list(sig.parameters.keys())



def test_variableaccess_is_not_abstract():
    assert not inspect.isabstract(VariableAccess)


def test_variableaccess_constructor_exists():
    assert callable(VariableAccess.__init__)


def test_variableaccess_constructor_args():
    sig = inspect.signature(VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::metaaccess_is_not_abstract():
    assert not inspect.isabstract(odemcustom::MetaAccess)


def test_odemcustom::metaaccess_constructor_exists():
    assert callable(odemcustom::MetaAccess.__init__)


def test_odemcustom::metaaccess_constructor_args():
    sig = inspect.signature(odemcustom::MetaAccess.__init__)
    params = list(sig.parameters.keys())



def test_elementaccess_is_not_abstract():
    assert not inspect.isabstract(ElementAccess)


def test_elementaccess_constructor_exists():
    assert callable(ElementAccess.__init__)


def test_elementaccess_constructor_args():
    sig = inspect.signature(ElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::variableaccess_is_not_abstract():
    assert not inspect.isabstract(odemcustom::VariableAccess)


def test_odemcustom::variableaccess_constructor_exists():
    assert callable(odemcustom::VariableAccess.__init__)


def test_odemcustom::variableaccess_constructor_args():
    sig = inspect.signature(odemcustom::VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::typeaccess_is_not_abstract():
    assert not inspect.isabstract(odemcustom::TypeAccess)


def test_odemcustom::typeaccess_constructor_exists():
    assert callable(odemcustom::TypeAccess.__init__)


def test_odemcustom::typeaccess_constructor_args():
    sig = inspect.signature(odemcustom::TypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::elementaccess_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ElementAccess)


def test_odemcustom::elementaccess_constructor_exists():
    assert callable(odemcustom::ElementAccess.__init__)


def test_odemcustom::elementaccess_constructor_args():
    sig = inspect.signature(odemcustom::ElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::argumentexpression_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ArgumentExpression)


def test_odemcustom::argumentexpression_constructor_exists():
    assert callable(odemcustom::ArgumentExpression.__init__)


def test_odemcustom::argumentexpression_constructor_args():
    sig = inspect.signature(odemcustom::ArgumentExpression.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::evalexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom::EvalExpr)


def test_odemcustom::evalexpr_constructor_exists():
    assert callable(odemcustom::EvalExpr.__init__)


def test_odemcustom::evalexpr_constructor_args():
    sig = inspect.signature(odemcustom::EvalExpr.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::activeliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ActiveLiteral)


def test_odemcustom::activeliteral_constructor_exists():
    assert callable(odemcustom::ActiveLiteral.__init__)


def test_odemcustom::activeliteral_constructor_args():
    sig = inspect.signature(odemcustom::ActiveLiteral.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::timeliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom::TimeLiteral)


def test_odemcustom::timeliteral_constructor_exists():
    assert callable(odemcustom::TimeLiteral.__init__)


def test_odemcustom::timeliteral_constructor_args():
    sig = inspect.signature(odemcustom::TimeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::nullliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom::NullLiteral)


def test_odemcustom::nullliteral_constructor_exists():
    assert callable(odemcustom::NullLiteral.__init__)


def test_odemcustom::nullliteral_constructor_args():
    sig = inspect.signature(odemcustom::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::cast_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Cast)


def test_odemcustom::cast_constructor_exists():
    assert callable(odemcustom::Cast.__init__)


def test_odemcustom::cast_constructor_args():
    sig = inspect.signature(odemcustom::Cast.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::createobject_is_not_abstract():
    assert not inspect.isabstract(odemcustom::CreateObject)


def test_odemcustom::createobject_constructor_exists():
    assert callable(odemcustom::CreateObject.__init__)


def test_odemcustom::createobject_constructor_args():
    sig = inspect.signature(odemcustom::CreateObject.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::not_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Not)


def test_odemcustom::not_constructor_exists():
    assert callable(odemcustom::Not.__init__)


def test_odemcustom::not_constructor_args():
    sig = inspect.signature(odemcustom::Not.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::instanceof_is_not_abstract():
    assert not inspect.isabstract(odemcustom::InstanceOf)


def test_odemcustom::instanceof_constructor_exists():
    assert callable(odemcustom::InstanceOf.__init__)


def test_odemcustom::instanceof_constructor_args():
    sig = inspect.signature(odemcustom::InstanceOf.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::equal_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Equal)


def test_odemcustom::equal_constructor_exists():
    assert callable(odemcustom::Equal.__init__)


def test_odemcustom::equal_constructor_args():
    sig = inspect.signature(odemcustom::Equal.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::notequal_is_not_abstract():
    assert not inspect.isabstract(odemcustom::NotEqual)


def test_odemcustom::notequal_constructor_exists():
    assert callable(odemcustom::NotEqual.__init__)


def test_odemcustom::notequal_constructor_args():
    sig = inspect.signature(odemcustom::NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::intliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom::IntLiteral)


def test_odemcustom::intliteral_constructor_exists():
    assert callable(odemcustom::IntLiteral.__init__)


def test_odemcustom::intliteral_constructor_args():
    sig = inspect.signature(odemcustom::IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_odemcustom::intliteral_has_value():
    assert hasattr(odemcustom::IntLiteral, "value")
    descriptor = None
    for klass in odemcustom::IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom::stringliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom::StringLiteral)


def test_odemcustom::stringliteral_constructor_exists():
    assert callable(odemcustom::StringLiteral.__init__)


def test_odemcustom::stringliteral_constructor_args():
    sig = inspect.signature(odemcustom::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_odemcustom::stringliteral_has_value():
    assert hasattr(odemcustom::StringLiteral, "value")
    descriptor = None
    for klass in odemcustom::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_setop_is_not_abstract():
    assert not inspect.isabstract(SetOp)


def test_setop_constructor_exists():
    assert callable(SetOp.__init__)


def test_setop_constructor_args():
    sig = inspect.signature(SetOp.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::indexof_is_not_abstract():
    assert not inspect.isabstract(odemcustom::IndexOf)


def test_odemcustom::indexof_constructor_exists():
    assert callable(odemcustom::IndexOf.__init__)


def test_odemcustom::indexof_constructor_args():
    sig = inspect.signature(odemcustom::IndexOf.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::lastinset_is_not_abstract():
    assert not inspect.isabstract(odemcustom::LastInSet)


def test_odemcustom::lastinset_constructor_exists():
    assert callable(odemcustom::LastInSet.__init__)


def test_odemcustom::lastinset_constructor_args():
    sig = inspect.signature(odemcustom::LastInSet.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::afterinset_is_not_abstract():
    assert not inspect.isabstract(odemcustom::AfterInSet)


def test_odemcustom::afterinset_constructor_exists():
    assert callable(odemcustom::AfterInSet.__init__)


def test_odemcustom::afterinset_constructor_args():
    sig = inspect.signature(odemcustom::AfterInSet.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::objectat_is_not_abstract():
    assert not inspect.isabstract(odemcustom::ObjectAt)


def test_odemcustom::objectat_constructor_exists():
    assert callable(odemcustom::ObjectAt.__init__)


def test_odemcustom::objectat_constructor_args():
    sig = inspect.signature(odemcustom::ObjectAt.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::beforeinset_is_not_abstract():
    assert not inspect.isabstract(odemcustom::BeforeInSet)


def test_odemcustom::beforeinset_constructor_exists():
    assert callable(odemcustom::BeforeInSet.__init__)


def test_odemcustom::beforeinset_constructor_args():
    sig = inspect.signature(odemcustom::BeforeInSet.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::firstinset_is_not_abstract():
    assert not inspect.isabstract(odemcustom::FirstInSet)


def test_odemcustom::firstinset_constructor_exists():
    assert callable(odemcustom::FirstInSet.__init__)


def test_odemcustom::firstinset_constructor_args():
    sig = inspect.signature(odemcustom::FirstInSet.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::contains_is_not_abstract():
    assert not inspect.isabstract(odemcustom::Contains)


def test_odemcustom::contains_constructor_exists():
    assert callable(odemcustom::Contains.__init__)


def test_odemcustom::contains_constructor_args():
    sig = inspect.signature(odemcustom::Contains.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom::sizeofset_is_not_abstract():
    assert not inspect.isabstract(odemcustom::SizeOfSet)


def test_odemcustom::sizeofset_constructor_exists():
    assert callable(odemcustom::SizeOfSet.__init__)


def test_odemcustom::sizeofset_constructor_args():
    sig = inspect.signature(odemcustom::SizeOfSet.__init__)
    params = list(sig.parameters.keys())

def test_bindingexpropkind_exists():
    # Check that the Enumeration exists
    assert BindingExprOpKind is not None

def test_bindingexpropkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BindingExprOpKind]
    expected_literals = [
        "ASSIGN",
        "ADD",
        "BOOL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BindingExprOpKind"


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
PredefinedId_strategy = st.builds(
    PredefinedId,
)
odemcustom::TypeLiteral_strategy = st.builds(
    odemcustom::TypeLiteral,
)
odemcustom::MetaLiteral_strategy = st.builds(
    odemcustom::MetaLiteral,
)
odemcustom::SetOp_strategy = st.builds(
    odemcustom::SetOp,
)
odemcustom::SuperLiteral_strategy = st.builds(
    odemcustom::SuperLiteral,
)
odemcustom::MeLiteral_strategy = st.builds(
    odemcustom::MeLiteral,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
odemcustom::Neg_strategy = st.builds(
    odemcustom::Neg,
)
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
odemcustom::Div_strategy = st.builds(
    odemcustom::Div,
)
odemcustom::GreaterEqual_strategy = st.builds(
    odemcustom::GreaterEqual,
)
odemcustom::Mul_strategy = st.builds(
    odemcustom::Mul,
)
odemcustom::Mod_strategy = st.builds(
    odemcustom::Mod,
)
odemcustom::Greater_strategy = st.builds(
    odemcustom::Greater,
)
odemcustom::LessEqual_strategy = st.builds(
    odemcustom::LessEqual,
)
odemcustom::And_strategy = st.builds(
    odemcustom::And,
)
odemcustom::Or_strategy = st.builds(
    odemcustom::Or,
)
odemcustom::Less_strategy = st.builds(
    odemcustom::Less,
)
odemcustom::Minus_strategy = st.builds(
    odemcustom::Minus,
)
odemcustom::Plus_strategy = st.builds(
    odemcustom::Plus,
)
Expression_strategy = st.builds(
    Expression,
)
odemcustom::UnaryOperator_strategy = st.builds(
    odemcustom::UnaryOperator,
)
odemcustom::BinaryOperator_strategy = st.builds(
    odemcustom::BinaryOperator,
)
odemcustom::L1Expr_strategy = st.builds(
    odemcustom::L1Expr,
)
CompositeStatement_strategy = st.builds(
    CompositeStatement,
)
odemcustom::WhileStatement_strategy = st.builds(
    odemcustom::WhileStatement,
)
odemcustom::ForEachStatement_strategy = st.builds(
    odemcustom::ForEachStatement,
)
odemcustom::IfStatement_strategy = st.builds(
    odemcustom::IfStatement,
)
SetStatement_strategy = st.builds(
    SetStatement,
)
odemcustom::EmptySet_strategy = st.builds(
    odemcustom::EmptySet,
)
odemcustom::AddToSet_strategy = st.builds(
    odemcustom::AddToSet,
)
odemcustom::RemoveFromSet_strategy = st.builds(
    odemcustom::RemoveFromSet,
)
odemcustom::StatementExpression_strategy = st.builds(
    odemcustom::StatementExpression,
)
SimpleStatement_strategy = st.builds(
    SimpleStatement,
)
odemcustom::Print_strategy = st.builds(
    odemcustom::Print,
)
odemcustom::BreakStatement_strategy = st.builds(
    odemcustom::BreakStatement,
)
odemcustom::Assignment_strategy = st.builds(
    odemcustom::Assignment,
)
odemcustom::SetStatement_strategy = st.builds(
    odemcustom::SetStatement,
)
odemcustom::Advance_strategy = st.builds(
    odemcustom::Advance,
)
odemcustom::ContinueStatement_strategy = st.builds(
    odemcustom::ContinueStatement,
)
odemcustom::ExpressionStatement_strategy = st.builds(
    odemcustom::ExpressionStatement,
)
Construct_strategy = st.builds(
    Construct,
)
odemcustom::Statement_strategy = st.builds(
    odemcustom::Statement,
)
odemcustom::CodeBlock_strategy = st.builds(
    odemcustom::CodeBlock,
)
odemcustom::ActivateObject_strategy = st.builds(
    odemcustom::ActivateObject,
    priority=
        st.integers()
)
odemcustom::Reactivate_strategy = st.builds(
    odemcustom::Reactivate,
)
odemcustom::Wait_strategy = st.builds(
    odemcustom::Wait,
)
odemcustom::Terminate_strategy = st.builds(
    odemcustom::Terminate,
)
odemcustom::WaitUntil_strategy = st.builds(
    odemcustom::WaitUntil,
)
odemcustom::Return_strategy = st.builds(
    odemcustom::Return,
)
StatementExpression_strategy = st.builds(
    StatementExpression,
)
odemcustom::ProcedureCall_strategy = st.builds(
    odemcustom::ProcedureCall,
)
ExpressionStatement_strategy = st.builds(
    ExpressionStatement,
)
odemcustom::DeprecatedProcedureCallStatement_strategy = st.builds(
    odemcustom::DeprecatedProcedureCallStatement,
)
odemcustom::Constructor_strategy = st.builds(
    odemcustom::Constructor,
)
ClassSimilar_strategy = st.builds(
    ClassSimilar,
)
Classifier_strategy = st.builds(
    Classifier,
)
ExpandableElement_strategy = st.builds(
    ExpandableElement,
)
odemcustom::NamedElement_strategy = st.builds(
    odemcustom::NamedElement,
    name=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
odemcustom::CompositeStatement_strategy = st.builds(
    odemcustom::CompositeStatement,
)
odemcustom::SimpleStatement_strategy = st.builds(
    odemcustom::SimpleStatement,
)
AbstractVariable_strategy = st.builds(
    AbstractVariable,
)
odemcustom::AnnotatableElement_strategy = st.builds(
    odemcustom::AnnotatableElement,
)
odemcustom::Expression_strategy = st.builds(
    odemcustom::Expression,
)
odemcustom::KeyValuePair_strategy = st.builds(
    odemcustom::KeyValuePair,
)
odemcustom::AnnotationApplication_strategy = st.builds(
    odemcustom::AnnotationApplication,
)
odemcustom::Interface_strategy = st.builds(
    odemcustom::Interface,
)
odemcustom::Clazz_strategy = st.builds(
    odemcustom::Clazz,
    active=
        st.booleans()
)
ModifierExtensionsContainer_strategy = st.builds(
    ModifierExtensionsContainer,
)
odemcustom::NativeBinding_strategy = st.builds(
    odemcustom::NativeBinding,
    targetType=
        safe_text,
    targetLanguage=
        safe_text
)
ReferableRhsType_strategy = st.builds(
    ReferableRhsType,
)
odemcustom::TypedElement_strategy = st.builds(
    odemcustom::TypedElement,
    isList=
        st.booleans()
)
odemcustom::Type_strategy = st.builds(
    odemcustom::Type,
)
odemcustom::ModifierExtensionsContainer_strategy = st.builds(
    odemcustom::ModifierExtensionsContainer,
)
odemcustom::Extension_strategy = st.builds(
    odemcustom::Extension,
)
odemcustom::EmbeddableExtensionsContainer_strategy = st.builds(
    odemcustom::EmbeddableExtensionsContainer,
)
odemcustom::IdResolution_strategy = st.builds(
    odemcustom::IdResolution,
    metaModelPlatformURI=
        safe_text
)
odemcustom::Variable_strategy = st.builds(
    odemcustom::Variable,
    control=
        st.booleans(),
    clazz=
        st.booleans()
)
odemcustom::Parameter_strategy = st.builds(
    odemcustom::Parameter,
)
AnnotatableElement_strategy = st.builds(
    AnnotatableElement,
)
CodeBlock_strategy = st.builds(
    CodeBlock,
)
odemcustom::StartCodeBlock_strategy = st.builds(
    odemcustom::StartCodeBlock,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
odemcustom::IntType_strategy = st.builds(
    odemcustom::IntType,
)
odemcustom::BoolType_strategy = st.builds(
    odemcustom::BoolType,
)
odemcustom::DoubleType_strategy = st.builds(
    odemcustom::DoubleType,
)
odemcustom::StringType_strategy = st.builds(
    odemcustom::StringType,
)
odemcustom::VoidType_strategy = st.builds(
    odemcustom::VoidType,
)
Type_strategy = st.builds(
    Type,
)
odemcustom::IdExpr_strategy = st.builds(
    odemcustom::IdExpr,
)
odemcustom::PrimitiveType_strategy = st.builds(
    odemcustom::PrimitiveType,
)
odemcustom::Import_strategy = st.builds(
    odemcustom::Import,
    file=
        safe_text
)
odemcustom::Model_strategy = st.builds(
    odemcustom::Model,
)
NamedExtension_strategy = st.builds(
    NamedExtension,
)
odemcustom::ClassAugment_strategy = st.builds(
    odemcustom::ClassAugment,
)
EmbeddableExtensionsContainer_strategy = st.builds(
    EmbeddableExtensionsContainer,
)
odemcustom::ClassSimilar_strategy = st.builds(
    odemcustom::ClassSimilar,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
odemcustom::Classifier_strategy = st.builds(
    odemcustom::Classifier,
)
odemcustom::AbstractVariable_strategy = st.builds(
    odemcustom::AbstractVariable,
)
odemcustom::SimpleAnnotation_strategy = st.builds(
    odemcustom::SimpleAnnotation,
    value=
        safe_text
)
odemcustom::ExtensionDefinition_strategy = st.builds(
    odemcustom::ExtensionDefinition,
)
odemcustom::Annotation_strategy = st.builds(
    odemcustom::Annotation,
)
odemcustom::Procedure_strategy = st.builds(
    odemcustom::Procedure,
    clazz=
        st.booleans()
)
odemcustom::Module_strategy = st.builds(
    odemcustom::Module,
)
odemcustom::Construct_strategy = st.builds(
    odemcustom::Construct,
    concreteSyntax=
        safe_text
)
odemcustom::PotentiallyHiddenIdElements_strategy = st.builds(
    odemcustom::PotentiallyHiddenIdElements,
)
odemcustom::IncludePattern_strategy = st.builds(
    odemcustom::IncludePattern,
)
odemcustom::ConsiderIdElements_strategy = st.builds(
    odemcustom::ConsiderIdElements,
)
odemcustom::FindContainer_strategy = st.builds(
    odemcustom::FindContainer,
)
odemcustom::ExpandStatement_strategy = st.builds(
    odemcustom::ExpandStatement,
)
odemcustom::ExpandExpression_strategy = st.builds(
    odemcustom::ExpandExpression,
)
odemcustom::TestStatement_strategy = st.builds(
    odemcustom::TestStatement,
    value=
        safe_text
)
odemcustom::ExpandableElement_strategy = st.builds(
    odemcustom::ExpandableElement,
)
Module_strategy = st.builds(
    Module,
)
QuotedCode_strategy = st.builds(
    QuotedCode,
)
odemcustom::QuotedModuleContent_strategy = st.builds(
    odemcustom::QuotedModuleContent,
)
odemcustom::QuotedStatements_strategy = st.builds(
    odemcustom::QuotedStatements,
)
odemcustom::QuotedClassContent_strategy = st.builds(
    odemcustom::QuotedClassContent,
)
odemcustom::QuotedExpression_strategy = st.builds(
    odemcustom::QuotedExpression,
)
odemcustom::QuotedCode_strategy = st.builds(
    odemcustom::QuotedCode,
)
odemcustom::CodeQuoteExpression_strategy = st.builds(
    odemcustom::CodeQuoteExpression,
)
odemcustom::ExpandSection_strategy = st.builds(
    odemcustom::ExpandSection,
)
odemcustom::TargetStatement_strategy = st.builds(
    odemcustom::TargetStatement,
)
odemcustom::MetaExpr_strategy = st.builds(
    odemcustom::MetaExpr,
)
odemcustom::MappingPart_strategy = st.builds(
    odemcustom::MappingPart,
)
MappingPart_strategy = st.builds(
    MappingPart,
)
odemcustom::DynamicMappingPart_strategy = st.builds(
    odemcustom::DynamicMappingPart,
)
odemcustom::FixedMappingPart_strategy = st.builds(
    odemcustom::FixedMappingPart,
    code=
        safe_text
)
odemcustom::ResumeGenStatement_strategy = st.builds(
    odemcustom::ResumeGenStatement,
)
odemcustom::SaveGenStatement_strategy = st.builds(
    odemcustom::SaveGenStatement,
)
odemcustom::ResetGenContextStatement_strategy = st.builds(
    odemcustom::ResetGenContextStatement,
)
odemcustom::SetGenContextStatement_strategy = st.builds(
    odemcustom::SetGenContextStatement,
    addAfterContext=
        st.booleans()
)
odemcustom::MappingStatement_strategy = st.builds(
    odemcustom::MappingStatement,
)
odemcustom::Pattern_strategy = st.builds(
    odemcustom::Pattern,
    top=
        st.booleans()
)
StructuredPropertyType_strategy = st.builds(
    StructuredPropertyType,
)
odemcustom::ReferencePropertyType_strategy = st.builds(
    odemcustom::ReferencePropertyType,
    rawReference=
        st.booleans()
)
odemcustom::CompositePropertyType_strategy = st.builds(
    odemcustom::CompositePropertyType,
    list=
        st.booleans()
)
PropertyType_strategy = st.builds(
    PropertyType,
)
odemcustom::StringPropertyType_strategy = st.builds(
    odemcustom::StringPropertyType,
)
odemcustom::IntPropertyType_strategy = st.builds(
    odemcustom::IntPropertyType,
)
odemcustom::StructuredPropertyType_strategy = st.builds(
    odemcustom::StructuredPropertyType,
)
odemcustom::BooleanPropertyType_strategy = st.builds(
    odemcustom::BooleanPropertyType,
    terminal=
        safe_text
)
odemcustom::IdPropertyType_strategy = st.builds(
    odemcustom::IdPropertyType,
)
odemcustom::PropertyType_strategy = st.builds(
    odemcustom::PropertyType,
)
odemcustom::ReferableRhsType_strategy = st.builds(
    odemcustom::ReferableRhsType,
)
odemcustom::TsRule_strategy = st.builds(
    odemcustom::TsRule,
    metaClassName=
        safe_text
)
odemcustom::ExtensionRule_strategy = st.builds(
    odemcustom::ExtensionRule,
)
odemcustom::Mapping_strategy = st.builds(
    odemcustom::Mapping,
)
odemcustom::TextualSyntaxDef_strategy = st.builds(
    odemcustom::TextualSyntaxDef,
)
RhsExpression_strategy = st.builds(
    RhsExpression,
)
odemcustom::AtLeastOneExpr_strategy = st.builds(
    odemcustom::AtLeastOneExpr,
)
odemcustom::ArbitraryExpr_strategy = st.builds(
    odemcustom::ArbitraryExpr,
)
odemcustom::AlternativeExpr_strategy = st.builds(
    odemcustom::AlternativeExpr,
)
odemcustom::PropertyBindingExpr_strategy = st.builds(
    odemcustom::PropertyBindingExpr,
    operator=
        safe_text
)
odemcustom::TerminalExpr_strategy = st.builds(
    odemcustom::TerminalExpr,
    terminal=
        safe_text
)
odemcustom::RuntimeExpr_strategy = st.builds(
    odemcustom::RuntimeExpr,
)
odemcustom::OptionalExpr_strategy = st.builds(
    odemcustom::OptionalExpr,
)
odemcustom::SequenceExpr_strategy = st.builds(
    odemcustom::SequenceExpr,
)
odemcustom::RuleExpr_strategy = st.builds(
    odemcustom::RuleExpr,
)
odemcustom::RhsExpression_strategy = st.builds(
    odemcustom::RhsExpression,
)
odemcustom::PredefinedId_strategy = st.builds(
    odemcustom::PredefinedId,
)
odemcustom::DepIdentifiableElement_strategy = st.builds(
    odemcustom::DepIdentifiableElement,
)
odemcustom::DoubleLiteral_strategy = st.builds(
    odemcustom::DoubleLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
odemcustom::FalseLiteral_strategy = st.builds(
    odemcustom::FalseLiteral,
)
odemcustom::TrueLiteral_strategy = st.builds(
    odemcustom::TrueLiteral,
)
odemcustom::ModuleContentExtension_strategy = st.builds(
    odemcustom::ModuleContentExtension,
)
odemcustom::ClassContentExtension_strategy = st.builds(
    odemcustom::ClassContentExtension,
)
Extension_strategy = st.builds(
    Extension,
)
odemcustom::NamedExtension_strategy = st.builds(
    odemcustom::NamedExtension,
)
VariableAccess_strategy = st.builds(
    VariableAccess,
)
odemcustom::MetaAccess_strategy = st.builds(
    odemcustom::MetaAccess,
)
ElementAccess_strategy = st.builds(
    ElementAccess,
)
odemcustom::VariableAccess_strategy = st.builds(
    odemcustom::VariableAccess,
)
odemcustom::TypeAccess_strategy = st.builds(
    odemcustom::TypeAccess,
)
odemcustom::ElementAccess_strategy = st.builds(
    odemcustom::ElementAccess,
)
odemcustom::ArgumentExpression_strategy = st.builds(
    odemcustom::ArgumentExpression,
)
odemcustom::EvalExpr_strategy = st.builds(
    odemcustom::EvalExpr,
)
odemcustom::ActiveLiteral_strategy = st.builds(
    odemcustom::ActiveLiteral,
)
odemcustom::TimeLiteral_strategy = st.builds(
    odemcustom::TimeLiteral,
)
odemcustom::NullLiteral_strategy = st.builds(
    odemcustom::NullLiteral,
)
odemcustom::Cast_strategy = st.builds(
    odemcustom::Cast,
)
odemcustom::CreateObject_strategy = st.builds(
    odemcustom::CreateObject,
)
odemcustom::Not_strategy = st.builds(
    odemcustom::Not,
)
odemcustom::InstanceOf_strategy = st.builds(
    odemcustom::InstanceOf,
)
odemcustom::Equal_strategy = st.builds(
    odemcustom::Equal,
)
odemcustom::NotEqual_strategy = st.builds(
    odemcustom::NotEqual,
)
odemcustom::IntLiteral_strategy = st.builds(
    odemcustom::IntLiteral,
    value=
        st.integers()
)
odemcustom::StringLiteral_strategy = st.builds(
    odemcustom::StringLiteral,
    value=
        safe_text
)
SetOp_strategy = st.builds(
    SetOp,
)
odemcustom::IndexOf_strategy = st.builds(
    odemcustom::IndexOf,
)
odemcustom::LastInSet_strategy = st.builds(
    odemcustom::LastInSet,
)
odemcustom::AfterInSet_strategy = st.builds(
    odemcustom::AfterInSet,
)
odemcustom::ObjectAt_strategy = st.builds(
    odemcustom::ObjectAt,
)
odemcustom::BeforeInSet_strategy = st.builds(
    odemcustom::BeforeInSet,
)
odemcustom::FirstInSet_strategy = st.builds(
    odemcustom::FirstInSet,
)
odemcustom::Contains_strategy = st.builds(
    odemcustom::Contains,
)
odemcustom::SizeOfSet_strategy = st.builds(
    odemcustom::SizeOfSet,
)

@given(instance=PredefinedId_strategy)
@settings(max_examples=50)
def test_predefinedid_instantiation(instance):
    assert isinstance(instance, PredefinedId)

@given(instance=odemcustom::TypeLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom::typeliteral_instantiation(instance):
    assert isinstance(instance, odemcustom::TypeLiteral)

@given(instance=odemcustom::MetaLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom::metaliteral_instantiation(instance):
    assert isinstance(instance, odemcustom::MetaLiteral)

@given(instance=odemcustom::SetOp_strategy)
@settings(max_examples=50)
def test_odemcustom::setop_instantiation(instance):
    assert isinstance(instance, odemcustom::SetOp)

@given(instance=odemcustom::SuperLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom::superliteral_instantiation(instance):
    assert isinstance(instance, odemcustom::SuperLiteral)

@given(instance=odemcustom::MeLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom::meliteral_instantiation(instance):
    assert isinstance(instance, odemcustom::MeLiteral)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=odemcustom::Neg_strategy)
@settings(max_examples=50)
def test_odemcustom::neg_instantiation(instance):
    assert isinstance(instance, odemcustom::Neg)

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=odemcustom::Div_strategy)
@settings(max_examples=50)
def test_odemcustom::div_instantiation(instance):
    assert isinstance(instance, odemcustom::Div)

@given(instance=odemcustom::GreaterEqual_strategy)
@settings(max_examples=50)
def test_odemcustom::greaterequal_instantiation(instance):
    assert isinstance(instance, odemcustom::GreaterEqual)

@given(instance=odemcustom::Mul_strategy)
@settings(max_examples=50)
def test_odemcustom::mul_instantiation(instance):
    assert isinstance(instance, odemcustom::Mul)

@given(instance=odemcustom::Mod_strategy)
@settings(max_examples=50)
def test_odemcustom::mod_instantiation(instance):
    assert isinstance(instance, odemcustom::Mod)

@given(instance=odemcustom::Greater_strategy)
@settings(max_examples=50)
def test_odemcustom::greater_instantiation(instance):
    assert isinstance(instance, odemcustom::Greater)

@given(instance=odemcustom::LessEqual_strategy)
@settings(max_examples=50)
def test_odemcustom::lessequal_instantiation(instance):
    assert isinstance(instance, odemcustom::LessEqual)

@given(instance=odemcustom::And_strategy)
@settings(max_examples=50)
def test_odemcustom::and_instantiation(instance):
    assert isinstance(instance, odemcustom::And)

@given(instance=odemcustom::Or_strategy)
@settings(max_examples=50)
def test_odemcustom::or_instantiation(instance):
    assert isinstance(instance, odemcustom::Or)

@given(instance=odemcustom::Less_strategy)
@settings(max_examples=50)
def test_odemcustom::less_instantiation(instance):
    assert isinstance(instance, odemcustom::Less)

@given(instance=odemcustom::Minus_strategy)
@settings(max_examples=50)
def test_odemcustom::minus_instantiation(instance):
    assert isinstance(instance, odemcustom::Minus)

@given(instance=odemcustom::Plus_strategy)
@settings(max_examples=50)
def test_odemcustom::plus_instantiation(instance):
    assert isinstance(instance, odemcustom::Plus)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=odemcustom::UnaryOperator_strategy)
@settings(max_examples=50)
def test_odemcustom::unaryoperator_instantiation(instance):
    assert isinstance(instance, odemcustom::UnaryOperator)

@given(instance=odemcustom::BinaryOperator_strategy)
@settings(max_examples=50)
def test_odemcustom::binaryoperator_instantiation(instance):
    assert isinstance(instance, odemcustom::BinaryOperator)

@given(instance=odemcustom::L1Expr_strategy)
@settings(max_examples=50)
def test_odemcustom::l1expr_instantiation(instance):
    assert isinstance(instance, odemcustom::L1Expr)

@given(instance=CompositeStatement_strategy)
@settings(max_examples=50)
def test_compositestatement_instantiation(instance):
    assert isinstance(instance, CompositeStatement)

@given(instance=odemcustom::WhileStatement_strategy)
@settings(max_examples=50)
def test_odemcustom::whilestatement_instantiation(instance):
    assert isinstance(instance, odemcustom::WhileStatement)

@given(instance=odemcustom::ForEachStatement_strategy)
@settings(max_examples=50)
def test_odemcustom::foreachstatement_instantiation(instance):
    assert isinstance(instance, odemcustom::ForEachStatement)

@given(instance=odemcustom::IfStatement_strategy)
@settings(max_examples=50)
def test_odemcustom::ifstatement_instantiation(instance):
    assert isinstance(instance, odemcustom::IfStatement)

@given(instance=SetStatement_strategy)
@settings(max_examples=50)
def test_setstatement_instantiation(instance):
    assert isinstance(instance, SetStatement)

@given(instance=odemcustom::EmptySet_strategy)
@settings(max_examples=50)
def test_odemcustom::emptyset_instantiation(instance):
    assert isinstance(instance, odemcustom::EmptySet)

@given(instance=odemcustom::AddToSet_strategy)
@settings(max_examples=50)
def test_odemcustom::addtoset_instantiation(instance):
    assert isinstance(instance, odemcustom::AddToSet)

@given(instance=odemcustom::RemoveFromSet_strategy)
@settings(max_examples=50)
def test_odemcustom::removefromset_instantiation(instance):
    assert isinstance(instance, odemcustom::RemoveFromSet)

@given(instance=odemcustom::StatementExpression_strategy)
@settings(max_examples=50)
def test_odemcustom::statementexpression_instantiation(instance):
    assert isinstance(instance, odemcustom::StatementExpression)

@given(instance=SimpleStatement_strategy)
@settings(max_examples=50)
def test_simplestatement_instantiation(instance):
    assert isinstance(instance, SimpleStatement)

@given(instance=odemcustom::Print_strategy)
@settings(max_examples=50)
def test_odemcustom::print_instantiation(instance):
    assert isinstance(instance, odemcustom::Print)

@given(instance=odemcustom::BreakStatement_strategy)
@settings(max_examples=50)
def test_odemcustom::breakstatement_instantiation(instance):
    assert isinstance(instance, odemcustom::BreakStatement)

@given(instance=odemcustom::Assignment_strategy)
@settings(max_examples=50)
def test_odemcustom::assignment_instantiation(instance):
    assert isinstance(instance, odemcustom::Assignment)

@given(instance=odemcustom::SetStatement_strategy)
@settings(max_examples=50)
def test_odemcustom::setstatement_instantiation(instance):
    assert isinstance(instance, odemcustom::SetStatement)

@given(instance=odemcustom::Advance_strategy)
@settings(max_examples=50)
def test_odemcustom::advance_instantiation(instance):
    assert isinstance(instance, odemcustom::Advance)

@given(instance=odemcustom::ContinueStatement_strategy)
@settings(max_examples=50)
def test_odemcustom::continuestatement_instantiation(instance):
    assert isinstance(instance, odemcustom::ContinueStatement)

@given(instance=odemcustom::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_odemcustom::expressionstatement_instantiation(instance):
    assert isinstance(instance, odemcustom::ExpressionStatement)

@given(instance=Construct_strategy)
@settings(max_examples=50)
def test_construct_instantiation(instance):
    assert isinstance(instance, Construct)

@given(instance=odemcustom::Statement_strategy)
@settings(max_examples=50)
def test_odemcustom::statement_instantiation(instance):
    assert isinstance(instance, odemcustom::Statement)

@given(instance=odemcustom::CodeBlock_strategy)
@settings(max_examples=50)
def test_odemcustom::codeblock_instantiation(instance):
    assert isinstance(instance, odemcustom::CodeBlock)

@given(instance=odemcustom::ActivateObject_strategy)
@settings(max_examples=50)
def test_odemcustom::activateobject_instantiation(instance):
    assert isinstance(instance, odemcustom::ActivateObject)

@given(instance=odemcustom::ActivateObject_strategy)
def test_odemcustom::activateobject_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=odemcustom::ActivateObject_strategy)
def test_odemcustom::activateobject_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=odemcustom::Reactivate_strategy)
@settings(max_examples=50)
def test_odemcustom::reactivate_instantiation(instance):
    assert isinstance(instance, odemcustom::Reactivate)

@given(instance=odemcustom::Wait_strategy)
@settings(max_examples=50)
def test_odemcustom::wait_instantiation(instance):
    assert isinstance(instance, odemcustom::Wait)

@given(instance=odemcustom::Terminate_strategy)
@settings(max_examples=50)
def test_odemcustom::terminate_instantiation(instance):
    assert isinstance(instance, odemcustom::Terminate)

@given(instance=odemcustom::WaitUntil_strategy)
@settings(max_examples=50)
def test_odemcustom::waituntil_instantiation(instance):
    assert isinstance(instance, odemcustom::WaitUntil)

@given(instance=odemcustom::Return_strategy)
@settings(max_examples=50)
def test_odemcustom::return_instantiation(instance):
    assert isinstance(instance, odemcustom::Return)

@given(instance=StatementExpression_strategy)
@settings(max_examples=50)
def test_statementexpression_instantiation(instance):
    assert isinstance(instance, StatementExpression)

@given(instance=odemcustom::ProcedureCall_strategy)
@settings(max_examples=50)
def test_odemcustom::procedurecall_instantiation(instance):
    assert isinstance(instance, odemcustom::ProcedureCall)

@given(instance=ExpressionStatement_strategy)
@settings(max_examples=50)
def test_expressionstatement_instantiation(instance):
    assert isinstance(instance, ExpressionStatement)

@given(instance=odemcustom::DeprecatedProcedureCallStatement_strategy)
@settings(max_examples=50)
def test_odemcustom::deprecatedprocedurecallstatement_instantiation(instance):
    assert isinstance(instance, odemcustom::DeprecatedProcedureCallStatement)

@given(instance=odemcustom::Constructor_strategy)
@settings(max_examples=50)
def test_odemcustom::constructor_instantiation(instance):
    assert isinstance(instance, odemcustom::Constructor)

@given(instance=ClassSimilar_strategy)
@settings(max_examples=50)
def test_classsimilar_instantiation(instance):
    assert isinstance(instance, ClassSimilar)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=ExpandableElement_strategy)
@settings(max_examples=50)
def test_expandableelement_instantiation(instance):
    assert isinstance(instance, ExpandableElement)

@given(instance=odemcustom::NamedElement_strategy)
@settings(max_examples=50)
def test_odemcustom::namedelement_instantiation(instance):
    assert isinstance(instance, odemcustom::NamedElement)

@given(instance=odemcustom::NamedElement_strategy)
def test_odemcustom::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=odemcustom::NamedElement_strategy)
def test_odemcustom::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=odemcustom::CompositeStatement_strategy)
@settings(max_examples=50)
def test_odemcustom::compositestatement_instantiation(instance):
    assert isinstance(instance, odemcustom::CompositeStatement)

@given(instance=odemcustom::SimpleStatement_strategy)
@settings(max_examples=50)
def test_odemcustom::simplestatement_instantiation(instance):
    assert isinstance(instance, odemcustom::SimpleStatement)

@given(instance=AbstractVariable_strategy)
@settings(max_examples=50)
def test_abstractvariable_instantiation(instance):
    assert isinstance(instance, AbstractVariable)

@given(instance=odemcustom::AnnotatableElement_strategy)
@settings(max_examples=50)
def test_odemcustom::annotatableelement_instantiation(instance):
    assert isinstance(instance, odemcustom::AnnotatableElement)

@given(instance=odemcustom::Expression_strategy)
@settings(max_examples=50)
def test_odemcustom::expression_instantiation(instance):
    assert isinstance(instance, odemcustom::Expression)

@given(instance=odemcustom::KeyValuePair_strategy)
@settings(max_examples=50)
def test_odemcustom::keyvaluepair_instantiation(instance):
    assert isinstance(instance, odemcustom::KeyValuePair)

@given(instance=odemcustom::AnnotationApplication_strategy)
@settings(max_examples=50)
def test_odemcustom::annotationapplication_instantiation(instance):
    assert isinstance(instance, odemcustom::AnnotationApplication)

@given(instance=odemcustom::Interface_strategy)
@settings(max_examples=50)
def test_odemcustom::interface_instantiation(instance):
    assert isinstance(instance, odemcustom::Interface)

@given(instance=odemcustom::Clazz_strategy)
@settings(max_examples=50)
def test_odemcustom::clazz_instantiation(instance):
    assert isinstance(instance, odemcustom::Clazz)

@given(instance=odemcustom::Clazz_strategy)
def test_odemcustom::clazz_active_type(instance):
    assert isinstance(instance.active, bool)


@given(instance=odemcustom::Clazz_strategy)
def test_odemcustom::clazz_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=ModifierExtensionsContainer_strategy)
@settings(max_examples=50)
def test_modifierextensionscontainer_instantiation(instance):
    assert isinstance(instance, ModifierExtensionsContainer)

@given(instance=odemcustom::NativeBinding_strategy)
@settings(max_examples=50)
def test_odemcustom::nativebinding_instantiation(instance):
    assert isinstance(instance, odemcustom::NativeBinding)

@given(instance=odemcustom::NativeBinding_strategy)
def test_odemcustom::nativebinding_targetType_type(instance):
    assert isinstance(instance.targetType, str)


@given(instance=odemcustom::NativeBinding_strategy)
def test_odemcustom::nativebinding_targetType_setter(instance):
    original = instance.targetType
    instance.targetType = original
    assert instance.targetType == original

@given(instance=odemcustom::NativeBinding_strategy)
def test_odemcustom::nativebinding_targetLanguage_type(instance):
    assert isinstance(instance.targetLanguage, str)


@given(instance=odemcustom::NativeBinding_strategy)
def test_odemcustom::nativebinding_targetLanguage_setter(instance):
    original = instance.targetLanguage
    instance.targetLanguage = original
    assert instance.targetLanguage == original

@given(instance=ReferableRhsType_strategy)
@settings(max_examples=50)
def test_referablerhstype_instantiation(instance):
    assert isinstance(instance, ReferableRhsType)

@given(instance=odemcustom::TypedElement_strategy)
@settings(max_examples=50)
def test_odemcustom::typedelement_instantiation(instance):
    assert isinstance(instance, odemcustom::TypedElement)

@given(instance=odemcustom::TypedElement_strategy)
def test_odemcustom::typedelement_isList_type(instance):
    assert isinstance(instance.isList, bool)


@given(instance=odemcustom::TypedElement_strategy)
def test_odemcustom::typedelement_isList_setter(instance):
    original = instance.isList
    instance.isList = original
    assert instance.isList == original

@given(instance=odemcustom::Type_strategy)
@settings(max_examples=50)
def test_odemcustom::type_instantiation(instance):
    assert isinstance(instance, odemcustom::Type)

@given(instance=odemcustom::ModifierExtensionsContainer_strategy)
@settings(max_examples=50)
def test_odemcustom::modifierextensionscontainer_instantiation(instance):
    assert isinstance(instance, odemcustom::ModifierExtensionsContainer)

@given(instance=odemcustom::Extension_strategy)
@settings(max_examples=50)
def test_odemcustom::extension_instantiation(instance):
    assert isinstance(instance, odemcustom::Extension)

@given(instance=odemcustom::EmbeddableExtensionsContainer_strategy)
@settings(max_examples=50)
def test_odemcustom::embeddableextensionscontainer_instantiation(instance):
    assert isinstance(instance, odemcustom::EmbeddableExtensionsContainer)

@given(instance=odemcustom::IdResolution_strategy)
@settings(max_examples=50)
def test_odemcustom::idresolution_instantiation(instance):
    assert isinstance(instance, odemcustom::IdResolution)

@given(instance=odemcustom::IdResolution_strategy)
def test_odemcustom::idresolution_metaModelPlatformURI_type(instance):
    assert isinstance(instance.metaModelPlatformURI, str)


@given(instance=odemcustom::IdResolution_strategy)
def test_odemcustom::idresolution_metaModelPlatformURI_setter(instance):
    original = instance.metaModelPlatformURI
    instance.metaModelPlatformURI = original
    assert instance.metaModelPlatformURI == original

@given(instance=odemcustom::Variable_strategy)
@settings(max_examples=50)
def test_odemcustom::variable_instantiation(instance):
    assert isinstance(instance, odemcustom::Variable)

@given(instance=odemcustom::Variable_strategy)
def test_odemcustom::variable_control_type(instance):
    assert isinstance(instance.control, bool)


@given(instance=odemcustom::Variable_strategy)
def test_odemcustom::variable_control_setter(instance):
    original = instance.control
    instance.control = original
    assert instance.control == original

@given(instance=odemcustom::Variable_strategy)
def test_odemcustom::variable_clazz_type(instance):
    assert isinstance(instance.clazz, bool)


@given(instance=odemcustom::Variable_strategy)
def test_odemcustom::variable_clazz_setter(instance):
    original = instance.clazz
    instance.clazz = original
    assert instance.clazz == original

@given(instance=odemcustom::Parameter_strategy)
@settings(max_examples=50)
def test_odemcustom::parameter_instantiation(instance):
    assert isinstance(instance, odemcustom::Parameter)

@given(instance=AnnotatableElement_strategy)
@settings(max_examples=50)
def test_annotatableelement_instantiation(instance):
    assert isinstance(instance, AnnotatableElement)

@given(instance=CodeBlock_strategy)
@settings(max_examples=50)
def test_codeblock_instantiation(instance):
    assert isinstance(instance, CodeBlock)

@given(instance=odemcustom::StartCodeBlock_strategy)
@settings(max_examples=50)
def test_odemcustom::startcodeblock_instantiation(instance):
    assert isinstance(instance, odemcustom::StartCodeBlock)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=odemcustom::IntType_strategy)
@settings(max_examples=50)
def test_odemcustom::inttype_instantiation(instance):
    assert isinstance(instance, odemcustom::IntType)

@given(instance=odemcustom::BoolType_strategy)
@settings(max_examples=50)
def test_odemcustom::booltype_instantiation(instance):
    assert isinstance(instance, odemcustom::BoolType)

@given(instance=odemcustom::DoubleType_strategy)
@settings(max_examples=50)
def test_odemcustom::doubletype_instantiation(instance):
    assert isinstance(instance, odemcustom::DoubleType)

@given(instance=odemcustom::StringType_strategy)
@settings(max_examples=50)
def test_odemcustom::stringtype_instantiation(instance):
    assert isinstance(instance, odemcustom::StringType)

@given(instance=odemcustom::VoidType_strategy)
@settings(max_examples=50)
def test_odemcustom::voidtype_instantiation(instance):
    assert isinstance(instance, odemcustom::VoidType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=odemcustom::IdExpr_strategy)
@settings(max_examples=50)
def test_odemcustom::idexpr_instantiation(instance):
    assert isinstance(instance, odemcustom::IdExpr)

@given(instance=odemcustom::PrimitiveType_strategy)
@settings(max_examples=50)
def test_odemcustom::primitivetype_instantiation(instance):
    assert isinstance(instance, odemcustom::PrimitiveType)

@given(instance=odemcustom::Import_strategy)
@settings(max_examples=50)
def test_odemcustom::import_instantiation(instance):
    assert isinstance(instance, odemcustom::Import)

@given(instance=odemcustom::Import_strategy)
def test_odemcustom::import_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=odemcustom::Import_strategy)
def test_odemcustom::import_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=odemcustom::Model_strategy)
@settings(max_examples=50)
def test_odemcustom::model_instantiation(instance):
    assert isinstance(instance, odemcustom::Model)

@given(instance=NamedExtension_strategy)
@settings(max_examples=50)
def test_namedextension_instantiation(instance):
    assert isinstance(instance, NamedExtension)

@given(instance=odemcustom::ClassAugment_strategy)
@settings(max_examples=50)
def test_odemcustom::classaugment_instantiation(instance):
    assert isinstance(instance, odemcustom::ClassAugment)

@given(instance=EmbeddableExtensionsContainer_strategy)
@settings(max_examples=50)
def test_embeddableextensionscontainer_instantiation(instance):
    assert isinstance(instance, EmbeddableExtensionsContainer)

@given(instance=odemcustom::ClassSimilar_strategy)
@settings(max_examples=50)
def test_odemcustom::classsimilar_instantiation(instance):
    assert isinstance(instance, odemcustom::ClassSimilar)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=odemcustom::Classifier_strategy)
@settings(max_examples=50)
def test_odemcustom::classifier_instantiation(instance):
    assert isinstance(instance, odemcustom::Classifier)

@given(instance=odemcustom::AbstractVariable_strategy)
@settings(max_examples=50)
def test_odemcustom::abstractvariable_instantiation(instance):
    assert isinstance(instance, odemcustom::AbstractVariable)

@given(instance=odemcustom::SimpleAnnotation_strategy)
@settings(max_examples=50)
def test_odemcustom::simpleannotation_instantiation(instance):
    assert isinstance(instance, odemcustom::SimpleAnnotation)

@given(instance=odemcustom::SimpleAnnotation_strategy)
def test_odemcustom::simpleannotation_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=odemcustom::SimpleAnnotation_strategy)
def test_odemcustom::simpleannotation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=odemcustom::ExtensionDefinition_strategy)
@settings(max_examples=50)
def test_odemcustom::extensiondefinition_instantiation(instance):
    assert isinstance(instance, odemcustom::ExtensionDefinition)

@given(instance=odemcustom::Annotation_strategy)
@settings(max_examples=50)
def test_odemcustom::annotation_instantiation(instance):
    assert isinstance(instance, odemcustom::Annotation)

@given(instance=odemcustom::Procedure_strategy)
@settings(max_examples=50)
def test_odemcustom::procedure_instantiation(instance):
    assert isinstance(instance, odemcustom::Procedure)

@given(instance=odemcustom::Procedure_strategy)
def test_odemcustom::procedure_clazz_type(instance):
    assert isinstance(instance.clazz, bool)


@given(instance=odemcustom::Procedure_strategy)
def test_odemcustom::procedure_clazz_setter(instance):
    original = instance.clazz
    instance.clazz = original
    assert instance.clazz == original

@given(instance=odemcustom::Module_strategy)
@settings(max_examples=50)
def test_odemcustom::module_instantiation(instance):
    assert isinstance(instance, odemcustom::Module)

@given(instance=odemcustom::Construct_strategy)
@settings(max_examples=50)
def test_odemcustom::construct_instantiation(instance):
    assert isinstance(instance, odemcustom::Construct)

@given(instance=odemcustom::Construct_strategy)
def test_odemcustom::construct_concreteSyntax_type(instance):
    assert isinstance(instance.concreteSyntax, str)


@given(instance=odemcustom::Construct_strategy)
def test_odemcustom::construct_concreteSyntax_setter(instance):
    original = instance.concreteSyntax
    instance.concreteSyntax = original
    assert instance.concreteSyntax == original

@given(instance=odemcustom::PotentiallyHiddenIdElements_strategy)
@settings(max_examples=50)
def test_odemcustom::potentiallyhiddenidelements_instantiation(instance):
    assert isinstance(instance, odemcustom::PotentiallyHiddenIdElements)

@given(instance=odemcustom::IncludePattern_strategy)
@settings(max_examples=50)
def test_odemcustom::includepattern_instantiation(instance):
    assert isinstance(instance, odemcustom::IncludePattern)

@given(instance=odemcustom::ConsiderIdElements_strategy)
@settings(max_examples=50)
def test_odemcustom::consideridelements_instantiation(instance):
    assert isinstance(instance, odemcustom::ConsiderIdElements)

@given(instance=odemcustom::FindContainer_strategy)
@settings(max_examples=50)
def test_odemcustom::findcontainer_instantiation(instance):
    assert isinstance(instance, odemcustom::FindContainer)

@given(instance=odemcustom::ExpandStatement_strategy)
@settings(max_examples=50)
def test_odemcustom::expandstatement_instantiation(instance):
    assert isinstance(instance, odemcustom::ExpandStatement)

@given(instance=odemcustom::ExpandExpression_strategy)
@settings(max_examples=50)
def test_odemcustom::expandexpression_instantiation(instance):
    assert isinstance(instance, odemcustom::ExpandExpression)

@given(instance=odemcustom::TestStatement_strategy)
@settings(max_examples=50)
def test_odemcustom::teststatement_instantiation(instance):
    assert isinstance(instance, odemcustom::TestStatement)

@given(instance=odemcustom::TestStatement_strategy)
def test_odemcustom::teststatement_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=odemcustom::TestStatement_strategy)
def test_odemcustom::teststatement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=odemcustom::ExpandableElement_strategy)
@settings(max_examples=50)
def test_odemcustom::expandableelement_instantiation(instance):
    assert isinstance(instance, odemcustom::ExpandableElement)

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=QuotedCode_strategy)
@settings(max_examples=50)
def test_quotedcode_instantiation(instance):
    assert isinstance(instance, QuotedCode)

@given(instance=odemcustom::QuotedModuleContent_strategy)
@settings(max_examples=50)
def test_odemcustom::quotedmodulecontent_instantiation(instance):
    assert isinstance(instance, odemcustom::QuotedModuleContent)

@given(instance=odemcustom::QuotedStatements_strategy)
@settings(max_examples=50)
def test_odemcustom::quotedstatements_instantiation(instance):
    assert isinstance(instance, odemcustom::QuotedStatements)

@given(instance=odemcustom::QuotedClassContent_strategy)
@settings(max_examples=50)
def test_odemcustom::quotedclasscontent_instantiation(instance):
    assert isinstance(instance, odemcustom::QuotedClassContent)

@given(instance=odemcustom::QuotedExpression_strategy)
@settings(max_examples=50)
def test_odemcustom::quotedexpression_instantiation(instance):
    assert isinstance(instance, odemcustom::QuotedExpression)

@given(instance=odemcustom::QuotedCode_strategy)
@settings(max_examples=50)
def test_odemcustom::quotedcode_instantiation(instance):
    assert isinstance(instance, odemcustom::QuotedCode)

@given(instance=odemcustom::CodeQuoteExpression_strategy)
@settings(max_examples=50)
def test_odemcustom::codequoteexpression_instantiation(instance):
    assert isinstance(instance, odemcustom::CodeQuoteExpression)

@given(instance=odemcustom::ExpandSection_strategy)
@settings(max_examples=50)
def test_odemcustom::expandsection_instantiation(instance):
    assert isinstance(instance, odemcustom::ExpandSection)

@given(instance=odemcustom::TargetStatement_strategy)
@settings(max_examples=50)
def test_odemcustom::targetstatement_instantiation(instance):
    assert isinstance(instance, odemcustom::TargetStatement)

@given(instance=odemcustom::MetaExpr_strategy)
@settings(max_examples=50)
def test_odemcustom::metaexpr_instantiation(instance):
    assert isinstance(instance, odemcustom::MetaExpr)

@given(instance=odemcustom::MappingPart_strategy)
@settings(max_examples=50)
def test_odemcustom::mappingpart_instantiation(instance):
    assert isinstance(instance, odemcustom::MappingPart)

@given(instance=MappingPart_strategy)
@settings(max_examples=50)
def test_mappingpart_instantiation(instance):
    assert isinstance(instance, MappingPart)

@given(instance=odemcustom::DynamicMappingPart_strategy)
@settings(max_examples=50)
def test_odemcustom::dynamicmappingpart_instantiation(instance):
    assert isinstance(instance, odemcustom::DynamicMappingPart)

@given(instance=odemcustom::FixedMappingPart_strategy)
@settings(max_examples=50)
def test_odemcustom::fixedmappingpart_instantiation(instance):
    assert isinstance(instance, odemcustom::FixedMappingPart)

@given(instance=odemcustom::FixedMappingPart_strategy)
def test_odemcustom::fixedmappingpart_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=odemcustom::FixedMappingPart_strategy)
def test_odemcustom::fixedmappingpart_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=odemcustom::ResumeGenStatement_strategy)
@settings(max_examples=50)
def test_odemcustom::resumegenstatement_instantiation(instance):
    assert isinstance(instance, odemcustom::ResumeGenStatement)

@given(instance=odemcustom::SaveGenStatement_strategy)
@settings(max_examples=50)
def test_odemcustom::savegenstatement_instantiation(instance):
    assert isinstance(instance, odemcustom::SaveGenStatement)

@given(instance=odemcustom::ResetGenContextStatement_strategy)
@settings(max_examples=50)
def test_odemcustom::resetgencontextstatement_instantiation(instance):
    assert isinstance(instance, odemcustom::ResetGenContextStatement)

@given(instance=odemcustom::SetGenContextStatement_strategy)
@settings(max_examples=50)
def test_odemcustom::setgencontextstatement_instantiation(instance):
    assert isinstance(instance, odemcustom::SetGenContextStatement)

@given(instance=odemcustom::SetGenContextStatement_strategy)
def test_odemcustom::setgencontextstatement_addAfterContext_type(instance):
    assert isinstance(instance.addAfterContext, bool)


@given(instance=odemcustom::SetGenContextStatement_strategy)
def test_odemcustom::setgencontextstatement_addAfterContext_setter(instance):
    original = instance.addAfterContext
    instance.addAfterContext = original
    assert instance.addAfterContext == original

@given(instance=odemcustom::MappingStatement_strategy)
@settings(max_examples=50)
def test_odemcustom::mappingstatement_instantiation(instance):
    assert isinstance(instance, odemcustom::MappingStatement)

@given(instance=odemcustom::Pattern_strategy)
@settings(max_examples=50)
def test_odemcustom::pattern_instantiation(instance):
    assert isinstance(instance, odemcustom::Pattern)

@given(instance=odemcustom::Pattern_strategy)
def test_odemcustom::pattern_top_type(instance):
    assert isinstance(instance.top, bool)


@given(instance=odemcustom::Pattern_strategy)
def test_odemcustom::pattern_top_setter(instance):
    original = instance.top
    instance.top = original
    assert instance.top == original

@given(instance=StructuredPropertyType_strategy)
@settings(max_examples=50)
def test_structuredpropertytype_instantiation(instance):
    assert isinstance(instance, StructuredPropertyType)

@given(instance=odemcustom::ReferencePropertyType_strategy)
@settings(max_examples=50)
def test_odemcustom::referencepropertytype_instantiation(instance):
    assert isinstance(instance, odemcustom::ReferencePropertyType)

@given(instance=odemcustom::ReferencePropertyType_strategy)
def test_odemcustom::referencepropertytype_rawReference_type(instance):
    assert isinstance(instance.rawReference, bool)


@given(instance=odemcustom::ReferencePropertyType_strategy)
def test_odemcustom::referencepropertytype_rawReference_setter(instance):
    original = instance.rawReference
    instance.rawReference = original
    assert instance.rawReference == original

@given(instance=odemcustom::CompositePropertyType_strategy)
@settings(max_examples=50)
def test_odemcustom::compositepropertytype_instantiation(instance):
    assert isinstance(instance, odemcustom::CompositePropertyType)

@given(instance=odemcustom::CompositePropertyType_strategy)
def test_odemcustom::compositepropertytype_list_type(instance):
    assert isinstance(instance.list, bool)


@given(instance=odemcustom::CompositePropertyType_strategy)
def test_odemcustom::compositepropertytype_list_setter(instance):
    original = instance.list
    instance.list = original
    assert instance.list == original

@given(instance=PropertyType_strategy)
@settings(max_examples=50)
def test_propertytype_instantiation(instance):
    assert isinstance(instance, PropertyType)

@given(instance=odemcustom::StringPropertyType_strategy)
@settings(max_examples=50)
def test_odemcustom::stringpropertytype_instantiation(instance):
    assert isinstance(instance, odemcustom::StringPropertyType)

@given(instance=odemcustom::IntPropertyType_strategy)
@settings(max_examples=50)
def test_odemcustom::intpropertytype_instantiation(instance):
    assert isinstance(instance, odemcustom::IntPropertyType)

@given(instance=odemcustom::StructuredPropertyType_strategy)
@settings(max_examples=50)
def test_odemcustom::structuredpropertytype_instantiation(instance):
    assert isinstance(instance, odemcustom::StructuredPropertyType)

@given(instance=odemcustom::BooleanPropertyType_strategy)
@settings(max_examples=50)
def test_odemcustom::booleanpropertytype_instantiation(instance):
    assert isinstance(instance, odemcustom::BooleanPropertyType)

@given(instance=odemcustom::BooleanPropertyType_strategy)
def test_odemcustom::booleanpropertytype_terminal_type(instance):
    assert isinstance(instance.terminal, str)


@given(instance=odemcustom::BooleanPropertyType_strategy)
def test_odemcustom::booleanpropertytype_terminal_setter(instance):
    original = instance.terminal
    instance.terminal = original
    assert instance.terminal == original

@given(instance=odemcustom::IdPropertyType_strategy)
@settings(max_examples=50)
def test_odemcustom::idpropertytype_instantiation(instance):
    assert isinstance(instance, odemcustom::IdPropertyType)

@given(instance=odemcustom::PropertyType_strategy)
@settings(max_examples=50)
def test_odemcustom::propertytype_instantiation(instance):
    assert isinstance(instance, odemcustom::PropertyType)

@given(instance=odemcustom::ReferableRhsType_strategy)
@settings(max_examples=50)
def test_odemcustom::referablerhstype_instantiation(instance):
    assert isinstance(instance, odemcustom::ReferableRhsType)

@given(instance=odemcustom::TsRule_strategy)
@settings(max_examples=50)
def test_odemcustom::tsrule_instantiation(instance):
    assert isinstance(instance, odemcustom::TsRule)

@given(instance=odemcustom::TsRule_strategy)
def test_odemcustom::tsrule_metaClassName_type(instance):
    assert isinstance(instance.metaClassName, str)


@given(instance=odemcustom::TsRule_strategy)
def test_odemcustom::tsrule_metaClassName_setter(instance):
    original = instance.metaClassName
    instance.metaClassName = original
    assert instance.metaClassName == original

@given(instance=odemcustom::ExtensionRule_strategy)
@settings(max_examples=50)
def test_odemcustom::extensionrule_instantiation(instance):
    assert isinstance(instance, odemcustom::ExtensionRule)

@given(instance=odemcustom::Mapping_strategy)
@settings(max_examples=50)
def test_odemcustom::mapping_instantiation(instance):
    assert isinstance(instance, odemcustom::Mapping)

@given(instance=odemcustom::TextualSyntaxDef_strategy)
@settings(max_examples=50)
def test_odemcustom::textualsyntaxdef_instantiation(instance):
    assert isinstance(instance, odemcustom::TextualSyntaxDef)

@given(instance=RhsExpression_strategy)
@settings(max_examples=50)
def test_rhsexpression_instantiation(instance):
    assert isinstance(instance, RhsExpression)

@given(instance=odemcustom::AtLeastOneExpr_strategy)
@settings(max_examples=50)
def test_odemcustom::atleastoneexpr_instantiation(instance):
    assert isinstance(instance, odemcustom::AtLeastOneExpr)

@given(instance=odemcustom::ArbitraryExpr_strategy)
@settings(max_examples=50)
def test_odemcustom::arbitraryexpr_instantiation(instance):
    assert isinstance(instance, odemcustom::ArbitraryExpr)

@given(instance=odemcustom::AlternativeExpr_strategy)
@settings(max_examples=50)
def test_odemcustom::alternativeexpr_instantiation(instance):
    assert isinstance(instance, odemcustom::AlternativeExpr)

@given(instance=odemcustom::PropertyBindingExpr_strategy)
@settings(max_examples=50)
def test_odemcustom::propertybindingexpr_instantiation(instance):
    assert isinstance(instance, odemcustom::PropertyBindingExpr)

@given(instance=odemcustom::PropertyBindingExpr_strategy)
def test_odemcustom::propertybindingexpr_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=odemcustom::PropertyBindingExpr_strategy)
def test_odemcustom::propertybindingexpr_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=odemcustom::TerminalExpr_strategy)
@settings(max_examples=50)
def test_odemcustom::terminalexpr_instantiation(instance):
    assert isinstance(instance, odemcustom::TerminalExpr)

@given(instance=odemcustom::TerminalExpr_strategy)
def test_odemcustom::terminalexpr_terminal_type(instance):
    assert isinstance(instance.terminal, str)


@given(instance=odemcustom::TerminalExpr_strategy)
def test_odemcustom::terminalexpr_terminal_setter(instance):
    original = instance.terminal
    instance.terminal = original
    assert instance.terminal == original

@given(instance=odemcustom::RuntimeExpr_strategy)
@settings(max_examples=50)
def test_odemcustom::runtimeexpr_instantiation(instance):
    assert isinstance(instance, odemcustom::RuntimeExpr)

@given(instance=odemcustom::OptionalExpr_strategy)
@settings(max_examples=50)
def test_odemcustom::optionalexpr_instantiation(instance):
    assert isinstance(instance, odemcustom::OptionalExpr)

@given(instance=odemcustom::SequenceExpr_strategy)
@settings(max_examples=50)
def test_odemcustom::sequenceexpr_instantiation(instance):
    assert isinstance(instance, odemcustom::SequenceExpr)

@given(instance=odemcustom::RuleExpr_strategy)
@settings(max_examples=50)
def test_odemcustom::ruleexpr_instantiation(instance):
    assert isinstance(instance, odemcustom::RuleExpr)

@given(instance=odemcustom::RhsExpression_strategy)
@settings(max_examples=50)
def test_odemcustom::rhsexpression_instantiation(instance):
    assert isinstance(instance, odemcustom::RhsExpression)

@given(instance=odemcustom::PredefinedId_strategy)
@settings(max_examples=50)
def test_odemcustom::predefinedid_instantiation(instance):
    assert isinstance(instance, odemcustom::PredefinedId)

@given(instance=odemcustom::DepIdentifiableElement_strategy)
@settings(max_examples=50)
def test_odemcustom::depidentifiableelement_instantiation(instance):
    assert isinstance(instance, odemcustom::DepIdentifiableElement)

@given(instance=odemcustom::DoubleLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom::doubleliteral_instantiation(instance):
    assert isinstance(instance, odemcustom::DoubleLiteral)

@given(instance=odemcustom::DoubleLiteral_strategy)
def test_odemcustom::doubleliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=odemcustom::DoubleLiteral_strategy)
def test_odemcustom::doubleliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=odemcustom::FalseLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom::falseliteral_instantiation(instance):
    assert isinstance(instance, odemcustom::FalseLiteral)

@given(instance=odemcustom::TrueLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom::trueliteral_instantiation(instance):
    assert isinstance(instance, odemcustom::TrueLiteral)

@given(instance=odemcustom::ModuleContentExtension_strategy)
@settings(max_examples=50)
def test_odemcustom::modulecontentextension_instantiation(instance):
    assert isinstance(instance, odemcustom::ModuleContentExtension)

@given(instance=odemcustom::ClassContentExtension_strategy)
@settings(max_examples=50)
def test_odemcustom::classcontentextension_instantiation(instance):
    assert isinstance(instance, odemcustom::ClassContentExtension)

@given(instance=Extension_strategy)
@settings(max_examples=50)
def test_extension_instantiation(instance):
    assert isinstance(instance, Extension)

@given(instance=odemcustom::NamedExtension_strategy)
@settings(max_examples=50)
def test_odemcustom::namedextension_instantiation(instance):
    assert isinstance(instance, odemcustom::NamedExtension)

@given(instance=VariableAccess_strategy)
@settings(max_examples=50)
def test_variableaccess_instantiation(instance):
    assert isinstance(instance, VariableAccess)

@given(instance=odemcustom::MetaAccess_strategy)
@settings(max_examples=50)
def test_odemcustom::metaaccess_instantiation(instance):
    assert isinstance(instance, odemcustom::MetaAccess)

@given(instance=ElementAccess_strategy)
@settings(max_examples=50)
def test_elementaccess_instantiation(instance):
    assert isinstance(instance, ElementAccess)

@given(instance=odemcustom::VariableAccess_strategy)
@settings(max_examples=50)
def test_odemcustom::variableaccess_instantiation(instance):
    assert isinstance(instance, odemcustom::VariableAccess)

@given(instance=odemcustom::TypeAccess_strategy)
@settings(max_examples=50)
def test_odemcustom::typeaccess_instantiation(instance):
    assert isinstance(instance, odemcustom::TypeAccess)

@given(instance=odemcustom::ElementAccess_strategy)
@settings(max_examples=50)
def test_odemcustom::elementaccess_instantiation(instance):
    assert isinstance(instance, odemcustom::ElementAccess)

@given(instance=odemcustom::ArgumentExpression_strategy)
@settings(max_examples=50)
def test_odemcustom::argumentexpression_instantiation(instance):
    assert isinstance(instance, odemcustom::ArgumentExpression)

@given(instance=odemcustom::EvalExpr_strategy)
@settings(max_examples=50)
def test_odemcustom::evalexpr_instantiation(instance):
    assert isinstance(instance, odemcustom::EvalExpr)

@given(instance=odemcustom::ActiveLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom::activeliteral_instantiation(instance):
    assert isinstance(instance, odemcustom::ActiveLiteral)

@given(instance=odemcustom::TimeLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom::timeliteral_instantiation(instance):
    assert isinstance(instance, odemcustom::TimeLiteral)

@given(instance=odemcustom::NullLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom::nullliteral_instantiation(instance):
    assert isinstance(instance, odemcustom::NullLiteral)

@given(instance=odemcustom::Cast_strategy)
@settings(max_examples=50)
def test_odemcustom::cast_instantiation(instance):
    assert isinstance(instance, odemcustom::Cast)

@given(instance=odemcustom::CreateObject_strategy)
@settings(max_examples=50)
def test_odemcustom::createobject_instantiation(instance):
    assert isinstance(instance, odemcustom::CreateObject)

@given(instance=odemcustom::Not_strategy)
@settings(max_examples=50)
def test_odemcustom::not_instantiation(instance):
    assert isinstance(instance, odemcustom::Not)

@given(instance=odemcustom::InstanceOf_strategy)
@settings(max_examples=50)
def test_odemcustom::instanceof_instantiation(instance):
    assert isinstance(instance, odemcustom::InstanceOf)

@given(instance=odemcustom::Equal_strategy)
@settings(max_examples=50)
def test_odemcustom::equal_instantiation(instance):
    assert isinstance(instance, odemcustom::Equal)

@given(instance=odemcustom::NotEqual_strategy)
@settings(max_examples=50)
def test_odemcustom::notequal_instantiation(instance):
    assert isinstance(instance, odemcustom::NotEqual)

@given(instance=odemcustom::IntLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom::intliteral_instantiation(instance):
    assert isinstance(instance, odemcustom::IntLiteral)

@given(instance=odemcustom::IntLiteral_strategy)
def test_odemcustom::intliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=odemcustom::IntLiteral_strategy)
def test_odemcustom::intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=odemcustom::StringLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom::stringliteral_instantiation(instance):
    assert isinstance(instance, odemcustom::StringLiteral)

@given(instance=odemcustom::StringLiteral_strategy)
def test_odemcustom::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=odemcustom::StringLiteral_strategy)
def test_odemcustom::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SetOp_strategy)
@settings(max_examples=50)
def test_setop_instantiation(instance):
    assert isinstance(instance, SetOp)

@given(instance=odemcustom::IndexOf_strategy)
@settings(max_examples=50)
def test_odemcustom::indexof_instantiation(instance):
    assert isinstance(instance, odemcustom::IndexOf)

@given(instance=odemcustom::LastInSet_strategy)
@settings(max_examples=50)
def test_odemcustom::lastinset_instantiation(instance):
    assert isinstance(instance, odemcustom::LastInSet)

@given(instance=odemcustom::AfterInSet_strategy)
@settings(max_examples=50)
def test_odemcustom::afterinset_instantiation(instance):
    assert isinstance(instance, odemcustom::AfterInSet)

@given(instance=odemcustom::ObjectAt_strategy)
@settings(max_examples=50)
def test_odemcustom::objectat_instantiation(instance):
    assert isinstance(instance, odemcustom::ObjectAt)

@given(instance=odemcustom::BeforeInSet_strategy)
@settings(max_examples=50)
def test_odemcustom::beforeinset_instantiation(instance):
    assert isinstance(instance, odemcustom::BeforeInSet)

@given(instance=odemcustom::FirstInSet_strategy)
@settings(max_examples=50)
def test_odemcustom::firstinset_instantiation(instance):
    assert isinstance(instance, odemcustom::FirstInSet)

@given(instance=odemcustom::Contains_strategy)
@settings(max_examples=50)
def test_odemcustom::contains_instantiation(instance):
    assert isinstance(instance, odemcustom::Contains)

@given(instance=odemcustom::SizeOfSet_strategy)
@settings(max_examples=50)
def test_odemcustom::sizeofset_instantiation(instance):
    assert isinstance(instance, odemcustom::SizeOfSet)
