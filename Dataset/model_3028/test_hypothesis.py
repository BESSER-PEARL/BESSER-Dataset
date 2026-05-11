import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ElementarySymbol,
    dbl::IdSymbol,
    L1SyntaxExpression,
    dbl::PlainSymbolReference,
    dbl::CallPart,
    Annotation,
    PredefinedId,
    dbl::MetaLiteral,
    dbl::SizeOfArray,
    dbl::AnnotationLiteral,
    dbl::SuperLiteral,
    dbl::TypeLiteral,
    dbl::MeLiteral,
    dbl::PredefinedId,
    VariableAccess,
    dbl::MetaAccess,
    ElementAccess,
    dbl::TypeAccess,
    L3Expr,
    L4Expr,
    L5Expr,
    L6Expr,
    L7Expr,
    L8Expr,
    BinaryOperator,
    dbl::Greater,
    dbl::LessEqual,
    dbl::Minus,
    dbl::InstanceOf,
    dbl::Plus,
    dbl::GreaterEqual,
    dbl::And,
    dbl::Equal,
    dbl::NotEqual,
    dbl::Mul,
    dbl::Less,
    dbl::Or,
    L1Expr,
    dbl::TrueLiteral,
    dbl::StringLiteral,
    dbl::NullLiteral,
    dbl::ActiveLiteral,
    dbl::TimeLiteral,
    dbl::FalseLiteral,
    dbl::DoubleLiteral,
    dbl::IntLiteral,
    L2Expr,
    UnaryOperator,
    dbl::Not,
    dbl::Neg,
    dbl::Div,
    dbl::Mod,
    dbl::SwitchCase,
    LoopStatement,
    dbl::WhileStatement,
    Expression,
    dbl::BinaryOperator,
    dbl::L3Expr,
    dbl::L7Expr,
    dbl::ElementAccess,
    dbl::UnaryOperator,
    dbl::ParseExpr,
    dbl::L2Expr,
    dbl::L9Expr,
    dbl::L8Expr,
    dbl::L6Expr,
    dbl::L5Expr,
    dbl::L4Expr,
    dbl::L1Expr,
    dbl::LocalScope,
    AnnotateableElement,
    dbl::VariableAccess,
    Statement,
    dbl::IfStatement,
    dbl::SimpleStatement,
    dbl::LoopStatement,
    dbl::NamedElement,
    SimpleStatement,
    dbl::Yield,
    dbl::Terminate,
    dbl::YieldTo,
    dbl::ActivateObject,
    dbl::BreakStatement,
    dbl::ContinueStatement,
    dbl::Print,
    dbl::Wait,
    dbl::Return,
    dbl::FunctionCall,
    dbl::WaitUntil,
    dbl::Assignment,
    dbl::SwitchStatement,
    dbl::Advance,
    dbl::Reactivate,
    AbstractVariable,
    TypedElement,
    dbl::CreateObject,
    dbl::Cast,
    PrimitiveType,
    dbl::BoolType,
    dbl::IntType,
    dbl::StringType,
    dbl::DoubleType,
    dbl::VoidType,
    Type,
    dbl::IdExpr,
    dbl::PrimitiveType,
    dbl::TypedElement,
    dbl::ArrayDimension,
    dbl::Type,
    Concept,
    dbl::SuperClassSpecification,
    dbl::NativeBinding,
    dbl::Parameter,
    LocalScope,
    dbl::Constructor,
    dbl::LocalScopeStatement,
    dbl::ForStatement,
    ConstructiveExtensionAtContentExtensionPoint,
    dbl::Import,
    dbl::Model,
    Construct,
    NamedElement,
    dbl::Class,
    dbl::Module,
    dbl::AbstractVariable,
    dbl::ExtensibleElement,
    ConstructiveExtension,
    dbl::ClassContentExtension,
    dbl::ModuleContentExtension,
    dbl::ConstructiveExtensionAtContentExtensionPoint,
    ExtensibleElement,
    dbl::SyntaxDefinition,
    dbl::Expression,
    dbl::ExtensionSemantics,
    dbl::Statement,
    dbl::Extension,
    dbl::ConstructiveExtension,
    dbl::AnnotateableElement,
    dbl::AnnotationItem,
    dbl::Annotation,
    dbl::Variable,
    dbl::Function,
    dbl::ExpandExpr,
    dbl::Construct,
    dbl::TestStatement,
    dbl::Pattern,
    Module,
    Class,
    dbl::ExpansionPart,
    dbl::ExpansionStatement,
    Variable,
    dbl::CreateIdStatement,
    dbl::TargetStatement,
    dbl::MetaExpr,
    QuotedCode,
    dbl::QuotedModuleContent,
    dbl::QuotedStatements,
    dbl::QuotedClassContent,
    dbl::QuotedExpression,
    dbl::QuotedCode,
    dbl::CodeQuoteExpression,
    dbl::ExpandStatement,
    dbl::ExpandExpression,
    ExpansionPart,
    dbl::ExpandVariablePart,
    dbl::ExpandTextPart,
    PlainSymbolReference,
    dbl::StructuralSymbolReference,
    L2SyntaxExpression,
    dbl::SymbolSequence,
    SyntaxExpression,
    dbl::L1SyntaxExpression,
    dbl::L2SyntaxExpression,
    dbl::L3SyntaxExpression,
    dbl::SyntaxExpression,
    ComplexSymbol,
    dbl::Concept,
    dbl::MetaSymbol,
    SyntaxSymbolClassifier,
    dbl::ElementarySymbol,
    dbl::ComplexSymbol,
    dbl::SyntaxSymbolClassifier,
    dbl::Keyword,
    dbl::StringSymbol,
    dbl::IntSymbol,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_elementarysymbol_is_not_abstract():
    assert not inspect.isabstract(ElementarySymbol)


def test_elementarysymbol_constructor_exists():
    assert callable(ElementarySymbol.__init__)


def test_elementarysymbol_constructor_args():
    sig = inspect.signature(ElementarySymbol.__init__)
    params = list(sig.parameters.keys())



def test_dbl::idsymbol_is_not_abstract():
    assert not inspect.isabstract(dbl::IdSymbol)


def test_dbl::idsymbol_constructor_exists():
    assert callable(dbl::IdSymbol.__init__)


def test_dbl::idsymbol_constructor_args():
    sig = inspect.signature(dbl::IdSymbol.__init__)
    params = list(sig.parameters.keys())



def test_l1syntaxexpression_is_not_abstract():
    assert not inspect.isabstract(L1SyntaxExpression)


def test_l1syntaxexpression_constructor_exists():
    assert callable(L1SyntaxExpression.__init__)


def test_l1syntaxexpression_constructor_args():
    sig = inspect.signature(L1SyntaxExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::plainsymbolreference_is_not_abstract():
    assert not inspect.isabstract(dbl::PlainSymbolReference)


def test_dbl::plainsymbolreference_constructor_exists():
    assert callable(dbl::PlainSymbolReference.__init__)


def test_dbl::plainsymbolreference_constructor_args():
    sig = inspect.signature(dbl::PlainSymbolReference.__init__)
    params = list(sig.parameters.keys())



def test_dbl::callpart_is_not_abstract():
    assert not inspect.isabstract(dbl::CallPart)


def test_dbl::callpart_constructor_exists():
    assert callable(dbl::CallPart.__init__)


def test_dbl::callpart_constructor_args():
    sig = inspect.signature(dbl::CallPart.__init__)
    params = list(sig.parameters.keys())



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_predefinedid_is_not_abstract():
    assert not inspect.isabstract(PredefinedId)


def test_predefinedid_constructor_exists():
    assert callable(PredefinedId.__init__)


def test_predefinedid_constructor_args():
    sig = inspect.signature(PredefinedId.__init__)
    params = list(sig.parameters.keys())



def test_dbl::metaliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::MetaLiteral)


def test_dbl::metaliteral_constructor_exists():
    assert callable(dbl::MetaLiteral.__init__)


def test_dbl::metaliteral_constructor_args():
    sig = inspect.signature(dbl::MetaLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::sizeofarray_is_not_abstract():
    assert not inspect.isabstract(dbl::SizeOfArray)


def test_dbl::sizeofarray_constructor_exists():
    assert callable(dbl::SizeOfArray.__init__)


def test_dbl::sizeofarray_constructor_args():
    sig = inspect.signature(dbl::SizeOfArray.__init__)
    params = list(sig.parameters.keys())



def test_dbl::annotationliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::AnnotationLiteral)


def test_dbl::annotationliteral_constructor_exists():
    assert callable(dbl::AnnotationLiteral.__init__)


def test_dbl::annotationliteral_constructor_args():
    sig = inspect.signature(dbl::AnnotationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::superliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::SuperLiteral)


def test_dbl::superliteral_constructor_exists():
    assert callable(dbl::SuperLiteral.__init__)


def test_dbl::superliteral_constructor_args():
    sig = inspect.signature(dbl::SuperLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::typeliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::TypeLiteral)


def test_dbl::typeliteral_constructor_exists():
    assert callable(dbl::TypeLiteral.__init__)


def test_dbl::typeliteral_constructor_args():
    sig = inspect.signature(dbl::TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::meliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::MeLiteral)


def test_dbl::meliteral_constructor_exists():
    assert callable(dbl::MeLiteral.__init__)


def test_dbl::meliteral_constructor_args():
    sig = inspect.signature(dbl::MeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::predefinedid_is_not_abstract():
    assert not inspect.isabstract(dbl::PredefinedId)


def test_dbl::predefinedid_constructor_exists():
    assert callable(dbl::PredefinedId.__init__)


def test_dbl::predefinedid_constructor_args():
    sig = inspect.signature(dbl::PredefinedId.__init__)
    params = list(sig.parameters.keys())



def test_variableaccess_is_not_abstract():
    assert not inspect.isabstract(VariableAccess)


def test_variableaccess_constructor_exists():
    assert callable(VariableAccess.__init__)


def test_variableaccess_constructor_args():
    sig = inspect.signature(VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_dbl::metaaccess_is_not_abstract():
    assert not inspect.isabstract(dbl::MetaAccess)


def test_dbl::metaaccess_constructor_exists():
    assert callable(dbl::MetaAccess.__init__)


def test_dbl::metaaccess_constructor_args():
    sig = inspect.signature(dbl::MetaAccess.__init__)
    params = list(sig.parameters.keys())



def test_elementaccess_is_not_abstract():
    assert not inspect.isabstract(ElementAccess)


def test_elementaccess_constructor_exists():
    assert callable(ElementAccess.__init__)


def test_elementaccess_constructor_args():
    sig = inspect.signature(ElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_dbl::typeaccess_is_not_abstract():
    assert not inspect.isabstract(dbl::TypeAccess)


def test_dbl::typeaccess_constructor_exists():
    assert callable(dbl::TypeAccess.__init__)


def test_dbl::typeaccess_constructor_args():
    sig = inspect.signature(dbl::TypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_l3expr_is_not_abstract():
    assert not inspect.isabstract(L3Expr)


def test_l3expr_constructor_exists():
    assert callable(L3Expr.__init__)


def test_l3expr_constructor_args():
    sig = inspect.signature(L3Expr.__init__)
    params = list(sig.parameters.keys())



def test_l4expr_is_not_abstract():
    assert not inspect.isabstract(L4Expr)


def test_l4expr_constructor_exists():
    assert callable(L4Expr.__init__)


def test_l4expr_constructor_args():
    sig = inspect.signature(L4Expr.__init__)
    params = list(sig.parameters.keys())



def test_l5expr_is_not_abstract():
    assert not inspect.isabstract(L5Expr)


def test_l5expr_constructor_exists():
    assert callable(L5Expr.__init__)


def test_l5expr_constructor_args():
    sig = inspect.signature(L5Expr.__init__)
    params = list(sig.parameters.keys())



def test_l6expr_is_not_abstract():
    assert not inspect.isabstract(L6Expr)


def test_l6expr_constructor_exists():
    assert callable(L6Expr.__init__)


def test_l6expr_constructor_args():
    sig = inspect.signature(L6Expr.__init__)
    params = list(sig.parameters.keys())



def test_l7expr_is_not_abstract():
    assert not inspect.isabstract(L7Expr)


def test_l7expr_constructor_exists():
    assert callable(L7Expr.__init__)


def test_l7expr_constructor_args():
    sig = inspect.signature(L7Expr.__init__)
    params = list(sig.parameters.keys())



def test_l8expr_is_not_abstract():
    assert not inspect.isabstract(L8Expr)


def test_l8expr_constructor_exists():
    assert callable(L8Expr.__init__)


def test_l8expr_constructor_args():
    sig = inspect.signature(L8Expr.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_dbl::greater_is_not_abstract():
    assert not inspect.isabstract(dbl::Greater)


def test_dbl::greater_constructor_exists():
    assert callable(dbl::Greater.__init__)


def test_dbl::greater_constructor_args():
    sig = inspect.signature(dbl::Greater.__init__)
    params = list(sig.parameters.keys())



def test_dbl::lessequal_is_not_abstract():
    assert not inspect.isabstract(dbl::LessEqual)


def test_dbl::lessequal_constructor_exists():
    assert callable(dbl::LessEqual.__init__)


def test_dbl::lessequal_constructor_args():
    sig = inspect.signature(dbl::LessEqual.__init__)
    params = list(sig.parameters.keys())



def test_dbl::minus_is_not_abstract():
    assert not inspect.isabstract(dbl::Minus)


def test_dbl::minus_constructor_exists():
    assert callable(dbl::Minus.__init__)


def test_dbl::minus_constructor_args():
    sig = inspect.signature(dbl::Minus.__init__)
    params = list(sig.parameters.keys())



def test_dbl::instanceof_is_not_abstract():
    assert not inspect.isabstract(dbl::InstanceOf)


def test_dbl::instanceof_constructor_exists():
    assert callable(dbl::InstanceOf.__init__)


def test_dbl::instanceof_constructor_args():
    sig = inspect.signature(dbl::InstanceOf.__init__)
    params = list(sig.parameters.keys())



def test_dbl::plus_is_not_abstract():
    assert not inspect.isabstract(dbl::Plus)


def test_dbl::plus_constructor_exists():
    assert callable(dbl::Plus.__init__)


def test_dbl::plus_constructor_args():
    sig = inspect.signature(dbl::Plus.__init__)
    params = list(sig.parameters.keys())



def test_dbl::greaterequal_is_not_abstract():
    assert not inspect.isabstract(dbl::GreaterEqual)


def test_dbl::greaterequal_constructor_exists():
    assert callable(dbl::GreaterEqual.__init__)


def test_dbl::greaterequal_constructor_args():
    sig = inspect.signature(dbl::GreaterEqual.__init__)
    params = list(sig.parameters.keys())



def test_dbl::and_is_not_abstract():
    assert not inspect.isabstract(dbl::And)


def test_dbl::and_constructor_exists():
    assert callable(dbl::And.__init__)


def test_dbl::and_constructor_args():
    sig = inspect.signature(dbl::And.__init__)
    params = list(sig.parameters.keys())



def test_dbl::equal_is_not_abstract():
    assert not inspect.isabstract(dbl::Equal)


def test_dbl::equal_constructor_exists():
    assert callable(dbl::Equal.__init__)


def test_dbl::equal_constructor_args():
    sig = inspect.signature(dbl::Equal.__init__)
    params = list(sig.parameters.keys())



def test_dbl::notequal_is_not_abstract():
    assert not inspect.isabstract(dbl::NotEqual)


def test_dbl::notequal_constructor_exists():
    assert callable(dbl::NotEqual.__init__)


def test_dbl::notequal_constructor_args():
    sig = inspect.signature(dbl::NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_dbl::mul_is_not_abstract():
    assert not inspect.isabstract(dbl::Mul)


def test_dbl::mul_constructor_exists():
    assert callable(dbl::Mul.__init__)


def test_dbl::mul_constructor_args():
    sig = inspect.signature(dbl::Mul.__init__)
    params = list(sig.parameters.keys())



def test_dbl::less_is_not_abstract():
    assert not inspect.isabstract(dbl::Less)


def test_dbl::less_constructor_exists():
    assert callable(dbl::Less.__init__)


def test_dbl::less_constructor_args():
    sig = inspect.signature(dbl::Less.__init__)
    params = list(sig.parameters.keys())



def test_dbl::or_is_not_abstract():
    assert not inspect.isabstract(dbl::Or)


def test_dbl::or_constructor_exists():
    assert callable(dbl::Or.__init__)


def test_dbl::or_constructor_args():
    sig = inspect.signature(dbl::Or.__init__)
    params = list(sig.parameters.keys())



def test_l1expr_is_not_abstract():
    assert not inspect.isabstract(L1Expr)


def test_l1expr_constructor_exists():
    assert callable(L1Expr.__init__)


def test_l1expr_constructor_args():
    sig = inspect.signature(L1Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::trueliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::TrueLiteral)


def test_dbl::trueliteral_constructor_exists():
    assert callable(dbl::TrueLiteral.__init__)


def test_dbl::trueliteral_constructor_args():
    sig = inspect.signature(dbl::TrueLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::stringliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::StringLiteral)


def test_dbl::stringliteral_constructor_exists():
    assert callable(dbl::StringLiteral.__init__)


def test_dbl::stringliteral_constructor_args():
    sig = inspect.signature(dbl::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dbl::stringliteral_has_value():
    assert hasattr(dbl::StringLiteral, "value")
    descriptor = None
    for klass in dbl::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dbl::nullliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::NullLiteral)


def test_dbl::nullliteral_constructor_exists():
    assert callable(dbl::NullLiteral.__init__)


def test_dbl::nullliteral_constructor_args():
    sig = inspect.signature(dbl::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::activeliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::ActiveLiteral)


def test_dbl::activeliteral_constructor_exists():
    assert callable(dbl::ActiveLiteral.__init__)


def test_dbl::activeliteral_constructor_args():
    sig = inspect.signature(dbl::ActiveLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::timeliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::TimeLiteral)


def test_dbl::timeliteral_constructor_exists():
    assert callable(dbl::TimeLiteral.__init__)


def test_dbl::timeliteral_constructor_args():
    sig = inspect.signature(dbl::TimeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::falseliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::FalseLiteral)


def test_dbl::falseliteral_constructor_exists():
    assert callable(dbl::FalseLiteral.__init__)


def test_dbl::falseliteral_constructor_args():
    sig = inspect.signature(dbl::FalseLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::doubleliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::DoubleLiteral)


def test_dbl::doubleliteral_constructor_exists():
    assert callable(dbl::DoubleLiteral.__init__)


def test_dbl::doubleliteral_constructor_args():
    sig = inspect.signature(dbl::DoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dbl::doubleliteral_has_value():
    assert hasattr(dbl::DoubleLiteral, "value")
    descriptor = None
    for klass in dbl::DoubleLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dbl::intliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::IntLiteral)


def test_dbl::intliteral_constructor_exists():
    assert callable(dbl::IntLiteral.__init__)


def test_dbl::intliteral_constructor_args():
    sig = inspect.signature(dbl::IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dbl::intliteral_has_value():
    assert hasattr(dbl::IntLiteral, "value")
    descriptor = None
    for klass in dbl::IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_l2expr_is_not_abstract():
    assert not inspect.isabstract(L2Expr)


def test_l2expr_constructor_exists():
    assert callable(L2Expr.__init__)


def test_l2expr_constructor_args():
    sig = inspect.signature(L2Expr.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_dbl::not_is_not_abstract():
    assert not inspect.isabstract(dbl::Not)


def test_dbl::not_constructor_exists():
    assert callable(dbl::Not.__init__)


def test_dbl::not_constructor_args():
    sig = inspect.signature(dbl::Not.__init__)
    params = list(sig.parameters.keys())



def test_dbl::neg_is_not_abstract():
    assert not inspect.isabstract(dbl::Neg)


def test_dbl::neg_constructor_exists():
    assert callable(dbl::Neg.__init__)


def test_dbl::neg_constructor_args():
    sig = inspect.signature(dbl::Neg.__init__)
    params = list(sig.parameters.keys())



def test_dbl::div_is_not_abstract():
    assert not inspect.isabstract(dbl::Div)


def test_dbl::div_constructor_exists():
    assert callable(dbl::Div.__init__)


def test_dbl::div_constructor_args():
    sig = inspect.signature(dbl::Div.__init__)
    params = list(sig.parameters.keys())



def test_dbl::mod_is_not_abstract():
    assert not inspect.isabstract(dbl::Mod)


def test_dbl::mod_constructor_exists():
    assert callable(dbl::Mod.__init__)


def test_dbl::mod_constructor_args():
    sig = inspect.signature(dbl::Mod.__init__)
    params = list(sig.parameters.keys())



def test_dbl::switchcase_is_not_abstract():
    assert not inspect.isabstract(dbl::SwitchCase)


def test_dbl::switchcase_constructor_exists():
    assert callable(dbl::SwitchCase.__init__)


def test_dbl::switchcase_constructor_args():
    sig = inspect.signature(dbl::SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_loopstatement_is_not_abstract():
    assert not inspect.isabstract(LoopStatement)


def test_loopstatement_constructor_exists():
    assert callable(LoopStatement.__init__)


def test_loopstatement_constructor_args():
    sig = inspect.signature(LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::whilestatement_is_not_abstract():
    assert not inspect.isabstract(dbl::WhileStatement)


def test_dbl::whilestatement_constructor_exists():
    assert callable(dbl::WhileStatement.__init__)


def test_dbl::whilestatement_constructor_args():
    sig = inspect.signature(dbl::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::binaryoperator_is_not_abstract():
    assert not inspect.isabstract(dbl::BinaryOperator)


def test_dbl::binaryoperator_constructor_exists():
    assert callable(dbl::BinaryOperator.__init__)


def test_dbl::binaryoperator_constructor_args():
    sig = inspect.signature(dbl::BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l3expr_is_not_abstract():
    assert not inspect.isabstract(dbl::L3Expr)


def test_dbl::l3expr_constructor_exists():
    assert callable(dbl::L3Expr.__init__)


def test_dbl::l3expr_constructor_args():
    sig = inspect.signature(dbl::L3Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l7expr_is_not_abstract():
    assert not inspect.isabstract(dbl::L7Expr)


def test_dbl::l7expr_constructor_exists():
    assert callable(dbl::L7Expr.__init__)


def test_dbl::l7expr_constructor_args():
    sig = inspect.signature(dbl::L7Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::elementaccess_is_not_abstract():
    assert not inspect.isabstract(dbl::ElementAccess)


def test_dbl::elementaccess_constructor_exists():
    assert callable(dbl::ElementAccess.__init__)


def test_dbl::elementaccess_constructor_args():
    sig = inspect.signature(dbl::ElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_dbl::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(dbl::UnaryOperator)


def test_dbl::unaryoperator_constructor_exists():
    assert callable(dbl::UnaryOperator.__init__)


def test_dbl::unaryoperator_constructor_args():
    sig = inspect.signature(dbl::UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_dbl::parseexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::ParseExpr)


def test_dbl::parseexpr_constructor_exists():
    assert callable(dbl::ParseExpr.__init__)


def test_dbl::parseexpr_constructor_args():
    sig = inspect.signature(dbl::ParseExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l2expr_is_not_abstract():
    assert not inspect.isabstract(dbl::L2Expr)


def test_dbl::l2expr_constructor_exists():
    assert callable(dbl::L2Expr.__init__)


def test_dbl::l2expr_constructor_args():
    sig = inspect.signature(dbl::L2Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l9expr_is_not_abstract():
    assert not inspect.isabstract(dbl::L9Expr)


def test_dbl::l9expr_constructor_exists():
    assert callable(dbl::L9Expr.__init__)


def test_dbl::l9expr_constructor_args():
    sig = inspect.signature(dbl::L9Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l8expr_is_not_abstract():
    assert not inspect.isabstract(dbl::L8Expr)


def test_dbl::l8expr_constructor_exists():
    assert callable(dbl::L8Expr.__init__)


def test_dbl::l8expr_constructor_args():
    sig = inspect.signature(dbl::L8Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l6expr_is_not_abstract():
    assert not inspect.isabstract(dbl::L6Expr)


def test_dbl::l6expr_constructor_exists():
    assert callable(dbl::L6Expr.__init__)


def test_dbl::l6expr_constructor_args():
    sig = inspect.signature(dbl::L6Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l5expr_is_not_abstract():
    assert not inspect.isabstract(dbl::L5Expr)


def test_dbl::l5expr_constructor_exists():
    assert callable(dbl::L5Expr.__init__)


def test_dbl::l5expr_constructor_args():
    sig = inspect.signature(dbl::L5Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l4expr_is_not_abstract():
    assert not inspect.isabstract(dbl::L4Expr)


def test_dbl::l4expr_constructor_exists():
    assert callable(dbl::L4Expr.__init__)


def test_dbl::l4expr_constructor_args():
    sig = inspect.signature(dbl::L4Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l1expr_is_not_abstract():
    assert not inspect.isabstract(dbl::L1Expr)


def test_dbl::l1expr_constructor_exists():
    assert callable(dbl::L1Expr.__init__)


def test_dbl::l1expr_constructor_args():
    sig = inspect.signature(dbl::L1Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::localscope_is_not_abstract():
    assert not inspect.isabstract(dbl::LocalScope)


def test_dbl::localscope_constructor_exists():
    assert callable(dbl::LocalScope.__init__)


def test_dbl::localscope_constructor_args():
    sig = inspect.signature(dbl::LocalScope.__init__)
    params = list(sig.parameters.keys())



def test_annotateableelement_is_not_abstract():
    assert not inspect.isabstract(AnnotateableElement)


def test_annotateableelement_constructor_exists():
    assert callable(AnnotateableElement.__init__)


def test_annotateableelement_constructor_args():
    sig = inspect.signature(AnnotateableElement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::variableaccess_is_not_abstract():
    assert not inspect.isabstract(dbl::VariableAccess)


def test_dbl::variableaccess_constructor_exists():
    assert callable(dbl::VariableAccess.__init__)


def test_dbl::variableaccess_constructor_args():
    sig = inspect.signature(dbl::VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::ifstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::IfStatement)


def test_dbl::ifstatement_constructor_exists():
    assert callable(dbl::IfStatement.__init__)


def test_dbl::ifstatement_constructor_args():
    sig = inspect.signature(dbl::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::simplestatement_is_not_abstract():
    assert not inspect.isabstract(dbl::SimpleStatement)


def test_dbl::simplestatement_constructor_exists():
    assert callable(dbl::SimpleStatement.__init__)


def test_dbl::simplestatement_constructor_args():
    sig = inspect.signature(dbl::SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::loopstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::LoopStatement)


def test_dbl::loopstatement_constructor_exists():
    assert callable(dbl::LoopStatement.__init__)


def test_dbl::loopstatement_constructor_args():
    sig = inspect.signature(dbl::LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::namedelement_is_not_abstract():
    assert not inspect.isabstract(dbl::NamedElement)


def test_dbl::namedelement_constructor_exists():
    assert callable(dbl::NamedElement.__init__)


def test_dbl::namedelement_constructor_args():
    sig = inspect.signature(dbl::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dbl::namedelement_has_name():
    assert hasattr(dbl::NamedElement, "name")
    descriptor = None
    for klass in dbl::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplestatement_is_not_abstract():
    assert not inspect.isabstract(SimpleStatement)


def test_simplestatement_constructor_exists():
    assert callable(SimpleStatement.__init__)


def test_simplestatement_constructor_args():
    sig = inspect.signature(SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::yield_is_not_abstract():
    assert not inspect.isabstract(dbl::Yield)


def test_dbl::yield_constructor_exists():
    assert callable(dbl::Yield.__init__)


def test_dbl::yield_constructor_args():
    sig = inspect.signature(dbl::Yield.__init__)
    params = list(sig.parameters.keys())



def test_dbl::terminate_is_not_abstract():
    assert not inspect.isabstract(dbl::Terminate)


def test_dbl::terminate_constructor_exists():
    assert callable(dbl::Terminate.__init__)


def test_dbl::terminate_constructor_args():
    sig = inspect.signature(dbl::Terminate.__init__)
    params = list(sig.parameters.keys())



def test_dbl::yieldto_is_not_abstract():
    assert not inspect.isabstract(dbl::YieldTo)


def test_dbl::yieldto_constructor_exists():
    assert callable(dbl::YieldTo.__init__)


def test_dbl::yieldto_constructor_args():
    sig = inspect.signature(dbl::YieldTo.__init__)
    params = list(sig.parameters.keys())



def test_dbl::activateobject_is_not_abstract():
    assert not inspect.isabstract(dbl::ActivateObject)


def test_dbl::activateobject_constructor_exists():
    assert callable(dbl::ActivateObject.__init__)


def test_dbl::activateobject_constructor_args():
    sig = inspect.signature(dbl::ActivateObject.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"

def test_dbl::activateobject_has_priority():
    assert hasattr(dbl::ActivateObject, "priority")
    descriptor = None
    for klass in dbl::ActivateObject.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_dbl::breakstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::BreakStatement)


def test_dbl::breakstatement_constructor_exists():
    assert callable(dbl::BreakStatement.__init__)


def test_dbl::breakstatement_constructor_args():
    sig = inspect.signature(dbl::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::continuestatement_is_not_abstract():
    assert not inspect.isabstract(dbl::ContinueStatement)


def test_dbl::continuestatement_constructor_exists():
    assert callable(dbl::ContinueStatement.__init__)


def test_dbl::continuestatement_constructor_args():
    sig = inspect.signature(dbl::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::print_is_not_abstract():
    assert not inspect.isabstract(dbl::Print)


def test_dbl::print_constructor_exists():
    assert callable(dbl::Print.__init__)


def test_dbl::print_constructor_args():
    sig = inspect.signature(dbl::Print.__init__)
    params = list(sig.parameters.keys())



def test_dbl::wait_is_not_abstract():
    assert not inspect.isabstract(dbl::Wait)


def test_dbl::wait_constructor_exists():
    assert callable(dbl::Wait.__init__)


def test_dbl::wait_constructor_args():
    sig = inspect.signature(dbl::Wait.__init__)
    params = list(sig.parameters.keys())



def test_dbl::return_is_not_abstract():
    assert not inspect.isabstract(dbl::Return)


def test_dbl::return_constructor_exists():
    assert callable(dbl::Return.__init__)


def test_dbl::return_constructor_args():
    sig = inspect.signature(dbl::Return.__init__)
    params = list(sig.parameters.keys())



def test_dbl::functioncall_is_not_abstract():
    assert not inspect.isabstract(dbl::FunctionCall)


def test_dbl::functioncall_constructor_exists():
    assert callable(dbl::FunctionCall.__init__)


def test_dbl::functioncall_constructor_args():
    sig = inspect.signature(dbl::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_dbl::waituntil_is_not_abstract():
    assert not inspect.isabstract(dbl::WaitUntil)


def test_dbl::waituntil_constructor_exists():
    assert callable(dbl::WaitUntil.__init__)


def test_dbl::waituntil_constructor_args():
    sig = inspect.signature(dbl::WaitUntil.__init__)
    params = list(sig.parameters.keys())



def test_dbl::assignment_is_not_abstract():
    assert not inspect.isabstract(dbl::Assignment)


def test_dbl::assignment_constructor_exists():
    assert callable(dbl::Assignment.__init__)


def test_dbl::assignment_constructor_args():
    sig = inspect.signature(dbl::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_dbl::switchstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::SwitchStatement)


def test_dbl::switchstatement_constructor_exists():
    assert callable(dbl::SwitchStatement.__init__)


def test_dbl::switchstatement_constructor_args():
    sig = inspect.signature(dbl::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::advance_is_not_abstract():
    assert not inspect.isabstract(dbl::Advance)


def test_dbl::advance_constructor_exists():
    assert callable(dbl::Advance.__init__)


def test_dbl::advance_constructor_args():
    sig = inspect.signature(dbl::Advance.__init__)
    params = list(sig.parameters.keys())



def test_dbl::reactivate_is_not_abstract():
    assert not inspect.isabstract(dbl::Reactivate)


def test_dbl::reactivate_constructor_exists():
    assert callable(dbl::Reactivate.__init__)


def test_dbl::reactivate_constructor_args():
    sig = inspect.signature(dbl::Reactivate.__init__)
    params = list(sig.parameters.keys())



def test_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(AbstractVariable)


def test_abstractvariable_constructor_exists():
    assert callable(AbstractVariable.__init__)


def test_abstractvariable_constructor_args():
    sig = inspect.signature(AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::createobject_is_not_abstract():
    assert not inspect.isabstract(dbl::CreateObject)


def test_dbl::createobject_constructor_exists():
    assert callable(dbl::CreateObject.__init__)


def test_dbl::createobject_constructor_args():
    sig = inspect.signature(dbl::CreateObject.__init__)
    params = list(sig.parameters.keys())



def test_dbl::cast_is_not_abstract():
    assert not inspect.isabstract(dbl::Cast)


def test_dbl::cast_constructor_exists():
    assert callable(dbl::Cast.__init__)


def test_dbl::cast_constructor_args():
    sig = inspect.signature(dbl::Cast.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::booltype_is_not_abstract():
    assert not inspect.isabstract(dbl::BoolType)


def test_dbl::booltype_constructor_exists():
    assert callable(dbl::BoolType.__init__)


def test_dbl::booltype_constructor_args():
    sig = inspect.signature(dbl::BoolType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::inttype_is_not_abstract():
    assert not inspect.isabstract(dbl::IntType)


def test_dbl::inttype_constructor_exists():
    assert callable(dbl::IntType.__init__)


def test_dbl::inttype_constructor_args():
    sig = inspect.signature(dbl::IntType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::stringtype_is_not_abstract():
    assert not inspect.isabstract(dbl::StringType)


def test_dbl::stringtype_constructor_exists():
    assert callable(dbl::StringType.__init__)


def test_dbl::stringtype_constructor_args():
    sig = inspect.signature(dbl::StringType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::doubletype_is_not_abstract():
    assert not inspect.isabstract(dbl::DoubleType)


def test_dbl::doubletype_constructor_exists():
    assert callable(dbl::DoubleType.__init__)


def test_dbl::doubletype_constructor_args():
    sig = inspect.signature(dbl::DoubleType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::voidtype_is_not_abstract():
    assert not inspect.isabstract(dbl::VoidType)


def test_dbl::voidtype_constructor_exists():
    assert callable(dbl::VoidType.__init__)


def test_dbl::voidtype_constructor_args():
    sig = inspect.signature(dbl::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_dbl::idexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::IdExpr)


def test_dbl::idexpr_constructor_exists():
    assert callable(dbl::IdExpr.__init__)


def test_dbl::idexpr_constructor_args():
    sig = inspect.signature(dbl::IdExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::primitivetype_is_not_abstract():
    assert not inspect.isabstract(dbl::PrimitiveType)


def test_dbl::primitivetype_constructor_exists():
    assert callable(dbl::PrimitiveType.__init__)


def test_dbl::primitivetype_constructor_args():
    sig = inspect.signature(dbl::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::typedelement_is_not_abstract():
    assert not inspect.isabstract(dbl::TypedElement)


def test_dbl::typedelement_constructor_exists():
    assert callable(dbl::TypedElement.__init__)


def test_dbl::typedelement_constructor_args():
    sig = inspect.signature(dbl::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::arraydimension_is_not_abstract():
    assert not inspect.isabstract(dbl::ArrayDimension)


def test_dbl::arraydimension_constructor_exists():
    assert callable(dbl::ArrayDimension.__init__)


def test_dbl::arraydimension_constructor_args():
    sig = inspect.signature(dbl::ArrayDimension.__init__)
    params = list(sig.parameters.keys())



def test_dbl::type_is_not_abstract():
    assert not inspect.isabstract(dbl::Type)


def test_dbl::type_constructor_exists():
    assert callable(dbl::Type.__init__)


def test_dbl::type_constructor_args():
    sig = inspect.signature(dbl::Type.__init__)
    params = list(sig.parameters.keys())



def test_concept_is_not_abstract():
    assert not inspect.isabstract(Concept)


def test_concept_constructor_exists():
    assert callable(Concept.__init__)


def test_concept_constructor_args():
    sig = inspect.signature(Concept.__init__)
    params = list(sig.parameters.keys())



def test_dbl::superclassspecification_is_not_abstract():
    assert not inspect.isabstract(dbl::SuperClassSpecification)


def test_dbl::superclassspecification_constructor_exists():
    assert callable(dbl::SuperClassSpecification.__init__)


def test_dbl::superclassspecification_constructor_args():
    sig = inspect.signature(dbl::SuperClassSpecification.__init__)
    params = list(sig.parameters.keys())



def test_dbl::nativebinding_is_not_abstract():
    assert not inspect.isabstract(dbl::NativeBinding)


def test_dbl::nativebinding_constructor_exists():
    assert callable(dbl::NativeBinding.__init__)


def test_dbl::nativebinding_constructor_args():
    sig = inspect.signature(dbl::NativeBinding.__init__)
    params = list(sig.parameters.keys())
    assert "targetType" in params, "Missing parameter 'targetType'"
    assert "targetLanguage" in params, "Missing parameter 'targetLanguage'"

def test_dbl::nativebinding_has_targetType():
    assert hasattr(dbl::NativeBinding, "targetType")
    descriptor = None
    for klass in dbl::NativeBinding.__mro__:
        if "targetType" in klass.__dict__:
            descriptor = klass.__dict__["targetType"]
            break
    assert isinstance(descriptor, property)

def test_dbl::nativebinding_has_targetLanguage():
    assert hasattr(dbl::NativeBinding, "targetLanguage")
    descriptor = None
    for klass in dbl::NativeBinding.__mro__:
        if "targetLanguage" in klass.__dict__:
            descriptor = klass.__dict__["targetLanguage"]
            break
    assert isinstance(descriptor, property)



def test_dbl::parameter_is_not_abstract():
    assert not inspect.isabstract(dbl::Parameter)


def test_dbl::parameter_constructor_exists():
    assert callable(dbl::Parameter.__init__)


def test_dbl::parameter_constructor_args():
    sig = inspect.signature(dbl::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_localscope_is_not_abstract():
    assert not inspect.isabstract(LocalScope)


def test_localscope_constructor_exists():
    assert callable(LocalScope.__init__)


def test_localscope_constructor_args():
    sig = inspect.signature(LocalScope.__init__)
    params = list(sig.parameters.keys())



def test_dbl::constructor_is_not_abstract():
    assert not inspect.isabstract(dbl::Constructor)


def test_dbl::constructor_constructor_exists():
    assert callable(dbl::Constructor.__init__)


def test_dbl::constructor_constructor_args():
    sig = inspect.signature(dbl::Constructor.__init__)
    params = list(sig.parameters.keys())



def test_dbl::localscopestatement_is_not_abstract():
    assert not inspect.isabstract(dbl::LocalScopeStatement)


def test_dbl::localscopestatement_constructor_exists():
    assert callable(dbl::LocalScopeStatement.__init__)


def test_dbl::localscopestatement_constructor_args():
    sig = inspect.signature(dbl::LocalScopeStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::forstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::ForStatement)


def test_dbl::forstatement_constructor_exists():
    assert callable(dbl::ForStatement.__init__)


def test_dbl::forstatement_constructor_args():
    sig = inspect.signature(dbl::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_constructiveextensionatcontentextensionpoint_is_not_abstract():
    assert not inspect.isabstract(ConstructiveExtensionAtContentExtensionPoint)


def test_constructiveextensionatcontentextensionpoint_constructor_exists():
    assert callable(ConstructiveExtensionAtContentExtensionPoint.__init__)


def test_constructiveextensionatcontentextensionpoint_constructor_args():
    sig = inspect.signature(ConstructiveExtensionAtContentExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_dbl::import_is_not_abstract():
    assert not inspect.isabstract(dbl::Import)


def test_dbl::import_constructor_exists():
    assert callable(dbl::Import.__init__)


def test_dbl::import_constructor_args():
    sig = inspect.signature(dbl::Import.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_dbl::import_has_file():
    assert hasattr(dbl::Import, "file")
    descriptor = None
    for klass in dbl::Import.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_dbl::model_is_not_abstract():
    assert not inspect.isabstract(dbl::Model)


def test_dbl::model_constructor_exists():
    assert callable(dbl::Model.__init__)


def test_dbl::model_constructor_args():
    sig = inspect.signature(dbl::Model.__init__)
    params = list(sig.parameters.keys())



def test_construct_is_not_abstract():
    assert not inspect.isabstract(Construct)


def test_construct_constructor_exists():
    assert callable(Construct.__init__)


def test_construct_constructor_args():
    sig = inspect.signature(Construct.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::class_is_not_abstract():
    assert not inspect.isabstract(dbl::Class)


def test_dbl::class_constructor_exists():
    assert callable(dbl::Class.__init__)


def test_dbl::class_constructor_args():
    sig = inspect.signature(dbl::Class.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"

def test_dbl::class_has_active():
    assert hasattr(dbl::Class, "active")
    descriptor = None
    for klass in dbl::Class.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)



def test_dbl::module_is_not_abstract():
    assert not inspect.isabstract(dbl::Module)


def test_dbl::module_constructor_exists():
    assert callable(dbl::Module.__init__)


def test_dbl::module_constructor_args():
    sig = inspect.signature(dbl::Module.__init__)
    params = list(sig.parameters.keys())



def test_dbl::abstractvariable_is_not_abstract():
    assert not inspect.isabstract(dbl::AbstractVariable)


def test_dbl::abstractvariable_constructor_exists():
    assert callable(dbl::AbstractVariable.__init__)


def test_dbl::abstractvariable_constructor_args():
    sig = inspect.signature(dbl::AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_dbl::extensibleelement_is_not_abstract():
    assert not inspect.isabstract(dbl::ExtensibleElement)


def test_dbl::extensibleelement_constructor_exists():
    assert callable(dbl::ExtensibleElement.__init__)


def test_dbl::extensibleelement_constructor_args():
    sig = inspect.signature(dbl::ExtensibleElement.__init__)
    params = list(sig.parameters.keys())
    assert "instanceOfExtensionDefinition" in params, "Missing parameter 'instanceOfExtensionDefinition'"
    assert "concreteSyntax" in params, "Missing parameter 'concreteSyntax'"

def test_dbl::extensibleelement_has_instanceOfExtensionDefinition():
    assert hasattr(dbl::ExtensibleElement, "instanceOfExtensionDefinition")
    descriptor = None
    for klass in dbl::ExtensibleElement.__mro__:
        if "instanceOfExtensionDefinition" in klass.__dict__:
            descriptor = klass.__dict__["instanceOfExtensionDefinition"]
            break
    assert isinstance(descriptor, property)

def test_dbl::extensibleelement_has_concreteSyntax():
    assert hasattr(dbl::ExtensibleElement, "concreteSyntax")
    descriptor = None
    for klass in dbl::ExtensibleElement.__mro__:
        if "concreteSyntax" in klass.__dict__:
            descriptor = klass.__dict__["concreteSyntax"]
            break
    assert isinstance(descriptor, property)



def test_constructiveextension_is_not_abstract():
    assert not inspect.isabstract(ConstructiveExtension)


def test_constructiveextension_constructor_exists():
    assert callable(ConstructiveExtension.__init__)


def test_constructiveextension_constructor_args():
    sig = inspect.signature(ConstructiveExtension.__init__)
    params = list(sig.parameters.keys())



def test_dbl::classcontentextension_is_not_abstract():
    assert not inspect.isabstract(dbl::ClassContentExtension)


def test_dbl::classcontentextension_constructor_exists():
    assert callable(dbl::ClassContentExtension.__init__)


def test_dbl::classcontentextension_constructor_args():
    sig = inspect.signature(dbl::ClassContentExtension.__init__)
    params = list(sig.parameters.keys())



def test_dbl::modulecontentextension_is_not_abstract():
    assert not inspect.isabstract(dbl::ModuleContentExtension)


def test_dbl::modulecontentextension_constructor_exists():
    assert callable(dbl::ModuleContentExtension.__init__)


def test_dbl::modulecontentextension_constructor_args():
    sig = inspect.signature(dbl::ModuleContentExtension.__init__)
    params = list(sig.parameters.keys())



def test_dbl::constructiveextensionatcontentextensionpoint_is_not_abstract():
    assert not inspect.isabstract(dbl::ConstructiveExtensionAtContentExtensionPoint)


def test_dbl::constructiveextensionatcontentextensionpoint_constructor_exists():
    assert callable(dbl::ConstructiveExtensionAtContentExtensionPoint.__init__)


def test_dbl::constructiveextensionatcontentextensionpoint_constructor_args():
    sig = inspect.signature(dbl::ConstructiveExtensionAtContentExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_extensibleelement_is_not_abstract():
    assert not inspect.isabstract(ExtensibleElement)


def test_extensibleelement_constructor_exists():
    assert callable(ExtensibleElement.__init__)


def test_extensibleelement_constructor_args():
    sig = inspect.signature(ExtensibleElement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::syntaxdefinition_is_not_abstract():
    assert not inspect.isabstract(dbl::SyntaxDefinition)


def test_dbl::syntaxdefinition_constructor_exists():
    assert callable(dbl::SyntaxDefinition.__init__)


def test_dbl::syntaxdefinition_constructor_args():
    sig = inspect.signature(dbl::SyntaxDefinition.__init__)
    params = list(sig.parameters.keys())



def test_dbl::expression_is_not_abstract():
    assert not inspect.isabstract(dbl::Expression)


def test_dbl::expression_constructor_exists():
    assert callable(dbl::Expression.__init__)


def test_dbl::expression_constructor_args():
    sig = inspect.signature(dbl::Expression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::extensionsemantics_is_not_abstract():
    assert not inspect.isabstract(dbl::ExtensionSemantics)


def test_dbl::extensionsemantics_constructor_exists():
    assert callable(dbl::ExtensionSemantics.__init__)


def test_dbl::extensionsemantics_constructor_args():
    sig = inspect.signature(dbl::ExtensionSemantics.__init__)
    params = list(sig.parameters.keys())



def test_dbl::statement_is_not_abstract():
    assert not inspect.isabstract(dbl::Statement)


def test_dbl::statement_constructor_exists():
    assert callable(dbl::Statement.__init__)


def test_dbl::statement_constructor_args():
    sig = inspect.signature(dbl::Statement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::extension_is_not_abstract():
    assert not inspect.isabstract(dbl::Extension)


def test_dbl::extension_constructor_exists():
    assert callable(dbl::Extension.__init__)


def test_dbl::extension_constructor_args():
    sig = inspect.signature(dbl::Extension.__init__)
    params = list(sig.parameters.keys())



def test_dbl::constructiveextension_is_not_abstract():
    assert not inspect.isabstract(dbl::ConstructiveExtension)


def test_dbl::constructiveextension_constructor_exists():
    assert callable(dbl::ConstructiveExtension.__init__)


def test_dbl::constructiveextension_constructor_args():
    sig = inspect.signature(dbl::ConstructiveExtension.__init__)
    params = list(sig.parameters.keys())



def test_dbl::annotateableelement_is_not_abstract():
    assert not inspect.isabstract(dbl::AnnotateableElement)


def test_dbl::annotateableelement_constructor_exists():
    assert callable(dbl::AnnotateableElement.__init__)


def test_dbl::annotateableelement_constructor_args():
    sig = inspect.signature(dbl::AnnotateableElement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::annotationitem_is_not_abstract():
    assert not inspect.isabstract(dbl::AnnotationItem)


def test_dbl::annotationitem_constructor_exists():
    assert callable(dbl::AnnotationItem.__init__)


def test_dbl::annotationitem_constructor_args():
    sig = inspect.signature(dbl::AnnotationItem.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_dbl::annotationitem_has_value():
    assert hasattr(dbl::AnnotationItem, "value")
    descriptor = None
    for klass in dbl::AnnotationItem.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_dbl::annotationitem_has_key():
    assert hasattr(dbl::AnnotationItem, "key")
    descriptor = None
    for klass in dbl::AnnotationItem.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_dbl::annotation_is_not_abstract():
    assert not inspect.isabstract(dbl::Annotation)


def test_dbl::annotation_constructor_exists():
    assert callable(dbl::Annotation.__init__)


def test_dbl::annotation_constructor_args():
    sig = inspect.signature(dbl::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_dbl::variable_is_not_abstract():
    assert not inspect.isabstract(dbl::Variable)


def test_dbl::variable_constructor_exists():
    assert callable(dbl::Variable.__init__)


def test_dbl::variable_constructor_args():
    sig = inspect.signature(dbl::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "control" in params, "Missing parameter 'control'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_dbl::variable_has_control():
    assert hasattr(dbl::Variable, "control")
    descriptor = None
    for klass in dbl::Variable.__mro__:
        if "control" in klass.__dict__:
            descriptor = klass.__dict__["control"]
            break
    assert isinstance(descriptor, property)

def test_dbl::variable_has_class_():
    assert hasattr(dbl::Variable, "class_")
    descriptor = None
    for klass in dbl::Variable.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_dbl::function_is_not_abstract():
    assert not inspect.isabstract(dbl::Function)


def test_dbl::function_constructor_exists():
    assert callable(dbl::Function.__init__)


def test_dbl::function_constructor_args():
    sig = inspect.signature(dbl::Function.__init__)
    params = list(sig.parameters.keys())
    assert "detached" in params, "Missing parameter 'detached'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_dbl::function_has_detached():
    assert hasattr(dbl::Function, "detached")
    descriptor = None
    for klass in dbl::Function.__mro__:
        if "detached" in klass.__dict__:
            descriptor = klass.__dict__["detached"]
            break
    assert isinstance(descriptor, property)

def test_dbl::function_has_abstract():
    assert hasattr(dbl::Function, "abstract")
    descriptor = None
    for klass in dbl::Function.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_dbl::function_has_class_():
    assert hasattr(dbl::Function, "class_")
    descriptor = None
    for klass in dbl::Function.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_dbl::expandexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::ExpandExpr)


def test_dbl::expandexpr_constructor_exists():
    assert callable(dbl::ExpandExpr.__init__)


def test_dbl::expandexpr_constructor_args():
    sig = inspect.signature(dbl::ExpandExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::construct_is_not_abstract():
    assert not inspect.isabstract(dbl::Construct)


def test_dbl::construct_constructor_exists():
    assert callable(dbl::Construct.__init__)


def test_dbl::construct_constructor_args():
    sig = inspect.signature(dbl::Construct.__init__)
    params = list(sig.parameters.keys())



def test_dbl::teststatement_is_not_abstract():
    assert not inspect.isabstract(dbl::TestStatement)


def test_dbl::teststatement_constructor_exists():
    assert callable(dbl::TestStatement.__init__)


def test_dbl::teststatement_constructor_args():
    sig = inspect.signature(dbl::TestStatement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dbl::teststatement_has_value():
    assert hasattr(dbl::TestStatement, "value")
    descriptor = None
    for klass in dbl::TestStatement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dbl::pattern_is_not_abstract():
    assert not inspect.isabstract(dbl::Pattern)


def test_dbl::pattern_constructor_exists():
    assert callable(dbl::Pattern.__init__)


def test_dbl::pattern_constructor_args():
    sig = inspect.signature(dbl::Pattern.__init__)
    params = list(sig.parameters.keys())
    assert "top" in params, "Missing parameter 'top'"

def test_dbl::pattern_has_top():
    assert hasattr(dbl::Pattern, "top")
    descriptor = None
    for klass in dbl::Pattern.__mro__:
        if "top" in klass.__dict__:
            descriptor = klass.__dict__["top"]
            break
    assert isinstance(descriptor, property)



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_dbl::expansionpart_is_not_abstract():
    assert not inspect.isabstract(dbl::ExpansionPart)


def test_dbl::expansionpart_constructor_exists():
    assert callable(dbl::ExpansionPart.__init__)


def test_dbl::expansionpart_constructor_args():
    sig = inspect.signature(dbl::ExpansionPart.__init__)
    params = list(sig.parameters.keys())



def test_dbl::expansionstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::ExpansionStatement)


def test_dbl::expansionstatement_constructor_exists():
    assert callable(dbl::ExpansionStatement.__init__)


def test_dbl::expansionstatement_constructor_args():
    sig = inspect.signature(dbl::ExpansionStatement.__init__)
    params = list(sig.parameters.keys())
    assert "variableContext" in params, "Missing parameter 'variableContext'"
    assert "classContext" in params, "Missing parameter 'classContext'"
    assert "functionContext" in params, "Missing parameter 'functionContext'"

def test_dbl::expansionstatement_has_variableContext():
    assert hasattr(dbl::ExpansionStatement, "variableContext")
    descriptor = None
    for klass in dbl::ExpansionStatement.__mro__:
        if "variableContext" in klass.__dict__:
            descriptor = klass.__dict__["variableContext"]
            break
    assert isinstance(descriptor, property)

def test_dbl::expansionstatement_has_classContext():
    assert hasattr(dbl::ExpansionStatement, "classContext")
    descriptor = None
    for klass in dbl::ExpansionStatement.__mro__:
        if "classContext" in klass.__dict__:
            descriptor = klass.__dict__["classContext"]
            break
    assert isinstance(descriptor, property)

def test_dbl::expansionstatement_has_functionContext():
    assert hasattr(dbl::ExpansionStatement, "functionContext")
    descriptor = None
    for klass in dbl::ExpansionStatement.__mro__:
        if "functionContext" in klass.__dict__:
            descriptor = klass.__dict__["functionContext"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_dbl::createidstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::CreateIdStatement)


def test_dbl::createidstatement_constructor_exists():
    assert callable(dbl::CreateIdStatement.__init__)


def test_dbl::createidstatement_constructor_args():
    sig = inspect.signature(dbl::CreateIdStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::targetstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::TargetStatement)


def test_dbl::targetstatement_constructor_exists():
    assert callable(dbl::TargetStatement.__init__)


def test_dbl::targetstatement_constructor_args():
    sig = inspect.signature(dbl::TargetStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::metaexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::MetaExpr)


def test_dbl::metaexpr_constructor_exists():
    assert callable(dbl::MetaExpr.__init__)


def test_dbl::metaexpr_constructor_args():
    sig = inspect.signature(dbl::MetaExpr.__init__)
    params = list(sig.parameters.keys())



def test_quotedcode_is_not_abstract():
    assert not inspect.isabstract(QuotedCode)


def test_quotedcode_constructor_exists():
    assert callable(QuotedCode.__init__)


def test_quotedcode_constructor_args():
    sig = inspect.signature(QuotedCode.__init__)
    params = list(sig.parameters.keys())



def test_dbl::quotedmodulecontent_is_not_abstract():
    assert not inspect.isabstract(dbl::QuotedModuleContent)


def test_dbl::quotedmodulecontent_constructor_exists():
    assert callable(dbl::QuotedModuleContent.__init__)


def test_dbl::quotedmodulecontent_constructor_args():
    sig = inspect.signature(dbl::QuotedModuleContent.__init__)
    params = list(sig.parameters.keys())



def test_dbl::quotedstatements_is_not_abstract():
    assert not inspect.isabstract(dbl::QuotedStatements)


def test_dbl::quotedstatements_constructor_exists():
    assert callable(dbl::QuotedStatements.__init__)


def test_dbl::quotedstatements_constructor_args():
    sig = inspect.signature(dbl::QuotedStatements.__init__)
    params = list(sig.parameters.keys())



def test_dbl::quotedclasscontent_is_not_abstract():
    assert not inspect.isabstract(dbl::QuotedClassContent)


def test_dbl::quotedclasscontent_constructor_exists():
    assert callable(dbl::QuotedClassContent.__init__)


def test_dbl::quotedclasscontent_constructor_args():
    sig = inspect.signature(dbl::QuotedClassContent.__init__)
    params = list(sig.parameters.keys())



def test_dbl::quotedexpression_is_not_abstract():
    assert not inspect.isabstract(dbl::QuotedExpression)


def test_dbl::quotedexpression_constructor_exists():
    assert callable(dbl::QuotedExpression.__init__)


def test_dbl::quotedexpression_constructor_args():
    sig = inspect.signature(dbl::QuotedExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::quotedcode_is_not_abstract():
    assert not inspect.isabstract(dbl::QuotedCode)


def test_dbl::quotedcode_constructor_exists():
    assert callable(dbl::QuotedCode.__init__)


def test_dbl::quotedcode_constructor_args():
    sig = inspect.signature(dbl::QuotedCode.__init__)
    params = list(sig.parameters.keys())



def test_dbl::codequoteexpression_is_not_abstract():
    assert not inspect.isabstract(dbl::CodeQuoteExpression)


def test_dbl::codequoteexpression_constructor_exists():
    assert callable(dbl::CodeQuoteExpression.__init__)


def test_dbl::codequoteexpression_constructor_args():
    sig = inspect.signature(dbl::CodeQuoteExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::expandstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::ExpandStatement)


def test_dbl::expandstatement_constructor_exists():
    assert callable(dbl::ExpandStatement.__init__)


def test_dbl::expandstatement_constructor_args():
    sig = inspect.signature(dbl::ExpandStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::expandexpression_is_not_abstract():
    assert not inspect.isabstract(dbl::ExpandExpression)


def test_dbl::expandexpression_constructor_exists():
    assert callable(dbl::ExpandExpression.__init__)


def test_dbl::expandexpression_constructor_args():
    sig = inspect.signature(dbl::ExpandExpression.__init__)
    params = list(sig.parameters.keys())



def test_expansionpart_is_not_abstract():
    assert not inspect.isabstract(ExpansionPart)


def test_expansionpart_constructor_exists():
    assert callable(ExpansionPart.__init__)


def test_expansionpart_constructor_args():
    sig = inspect.signature(ExpansionPart.__init__)
    params = list(sig.parameters.keys())



def test_dbl::expandvariablepart_is_not_abstract():
    assert not inspect.isabstract(dbl::ExpandVariablePart)


def test_dbl::expandvariablepart_constructor_exists():
    assert callable(dbl::ExpandVariablePart.__init__)


def test_dbl::expandvariablepart_constructor_args():
    sig = inspect.signature(dbl::ExpandVariablePart.__init__)
    params = list(sig.parameters.keys())



def test_dbl::expandtextpart_is_not_abstract():
    assert not inspect.isabstract(dbl::ExpandTextPart)


def test_dbl::expandtextpart_constructor_exists():
    assert callable(dbl::ExpandTextPart.__init__)


def test_dbl::expandtextpart_constructor_args():
    sig = inspect.signature(dbl::ExpandTextPart.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_dbl::expandtextpart_has_text():
    assert hasattr(dbl::ExpandTextPart, "text")
    descriptor = None
    for klass in dbl::ExpandTextPart.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_plainsymbolreference_is_not_abstract():
    assert not inspect.isabstract(PlainSymbolReference)


def test_plainsymbolreference_constructor_exists():
    assert callable(PlainSymbolReference.__init__)


def test_plainsymbolreference_constructor_args():
    sig = inspect.signature(PlainSymbolReference.__init__)
    params = list(sig.parameters.keys())



def test_dbl::structuralsymbolreference_is_not_abstract():
    assert not inspect.isabstract(dbl::StructuralSymbolReference)


def test_dbl::structuralsymbolreference_constructor_exists():
    assert callable(dbl::StructuralSymbolReference.__init__)


def test_dbl::structuralsymbolreference_constructor_args():
    sig = inspect.signature(dbl::StructuralSymbolReference.__init__)
    params = list(sig.parameters.keys())
    assert "localScopedReference" in params, "Missing parameter 'localScopedReference'"
    assert "list" in params, "Missing parameter 'list'"
    assert "composite" in params, "Missing parameter 'composite'"
    assert "globalScopedReference" in params, "Missing parameter 'globalScopedReference'"

def test_dbl::structuralsymbolreference_has_localScopedReference():
    assert hasattr(dbl::StructuralSymbolReference, "localScopedReference")
    descriptor = None
    for klass in dbl::StructuralSymbolReference.__mro__:
        if "localScopedReference" in klass.__dict__:
            descriptor = klass.__dict__["localScopedReference"]
            break
    assert isinstance(descriptor, property)

def test_dbl::structuralsymbolreference_has_list():
    assert hasattr(dbl::StructuralSymbolReference, "list")
    descriptor = None
    for klass in dbl::StructuralSymbolReference.__mro__:
        if "list" in klass.__dict__:
            descriptor = klass.__dict__["list"]
            break
    assert isinstance(descriptor, property)

def test_dbl::structuralsymbolreference_has_composite():
    assert hasattr(dbl::StructuralSymbolReference, "composite")
    descriptor = None
    for klass in dbl::StructuralSymbolReference.__mro__:
        if "composite" in klass.__dict__:
            descriptor = klass.__dict__["composite"]
            break
    assert isinstance(descriptor, property)

def test_dbl::structuralsymbolreference_has_globalScopedReference():
    assert hasattr(dbl::StructuralSymbolReference, "globalScopedReference")
    descriptor = None
    for klass in dbl::StructuralSymbolReference.__mro__:
        if "globalScopedReference" in klass.__dict__:
            descriptor = klass.__dict__["globalScopedReference"]
            break
    assert isinstance(descriptor, property)



def test_l2syntaxexpression_is_not_abstract():
    assert not inspect.isabstract(L2SyntaxExpression)


def test_l2syntaxexpression_constructor_exists():
    assert callable(L2SyntaxExpression.__init__)


def test_l2syntaxexpression_constructor_args():
    sig = inspect.signature(L2SyntaxExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::symbolsequence_is_not_abstract():
    assert not inspect.isabstract(dbl::SymbolSequence)


def test_dbl::symbolsequence_constructor_exists():
    assert callable(dbl::SymbolSequence.__init__)


def test_dbl::symbolsequence_constructor_args():
    sig = inspect.signature(dbl::SymbolSequence.__init__)
    params = list(sig.parameters.keys())



def test_syntaxexpression_is_not_abstract():
    assert not inspect.isabstract(SyntaxExpression)


def test_syntaxexpression_constructor_exists():
    assert callable(SyntaxExpression.__init__)


def test_syntaxexpression_constructor_args():
    sig = inspect.signature(SyntaxExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l1syntaxexpression_is_not_abstract():
    assert not inspect.isabstract(dbl::L1SyntaxExpression)


def test_dbl::l1syntaxexpression_constructor_exists():
    assert callable(dbl::L1SyntaxExpression.__init__)


def test_dbl::l1syntaxexpression_constructor_args():
    sig = inspect.signature(dbl::L1SyntaxExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l2syntaxexpression_is_not_abstract():
    assert not inspect.isabstract(dbl::L2SyntaxExpression)


def test_dbl::l2syntaxexpression_constructor_exists():
    assert callable(dbl::L2SyntaxExpression.__init__)


def test_dbl::l2syntaxexpression_constructor_args():
    sig = inspect.signature(dbl::L2SyntaxExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l3syntaxexpression_is_not_abstract():
    assert not inspect.isabstract(dbl::L3SyntaxExpression)


def test_dbl::l3syntaxexpression_constructor_exists():
    assert callable(dbl::L3SyntaxExpression.__init__)


def test_dbl::l3syntaxexpression_constructor_args():
    sig = inspect.signature(dbl::L3SyntaxExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::syntaxexpression_is_not_abstract():
    assert not inspect.isabstract(dbl::SyntaxExpression)


def test_dbl::syntaxexpression_constructor_exists():
    assert callable(dbl::SyntaxExpression.__init__)


def test_dbl::syntaxexpression_constructor_args():
    sig = inspect.signature(dbl::SyntaxExpression.__init__)
    params = list(sig.parameters.keys())



def test_complexsymbol_is_not_abstract():
    assert not inspect.isabstract(ComplexSymbol)


def test_complexsymbol_constructor_exists():
    assert callable(ComplexSymbol.__init__)


def test_complexsymbol_constructor_args():
    sig = inspect.signature(ComplexSymbol.__init__)
    params = list(sig.parameters.keys())



def test_dbl::concept_is_not_abstract():
    assert not inspect.isabstract(dbl::Concept)


def test_dbl::concept_constructor_exists():
    assert callable(dbl::Concept.__init__)


def test_dbl::concept_constructor_args():
    sig = inspect.signature(dbl::Concept.__init__)
    params = list(sig.parameters.keys())



def test_dbl::metasymbol_is_not_abstract():
    assert not inspect.isabstract(dbl::MetaSymbol)


def test_dbl::metasymbol_constructor_exists():
    assert callable(dbl::MetaSymbol.__init__)


def test_dbl::metasymbol_constructor_args():
    sig = inspect.signature(dbl::MetaSymbol.__init__)
    params = list(sig.parameters.keys())



def test_syntaxsymbolclassifier_is_not_abstract():
    assert not inspect.isabstract(SyntaxSymbolClassifier)


def test_syntaxsymbolclassifier_constructor_exists():
    assert callable(SyntaxSymbolClassifier.__init__)


def test_syntaxsymbolclassifier_constructor_args():
    sig = inspect.signature(SyntaxSymbolClassifier.__init__)
    params = list(sig.parameters.keys())



def test_dbl::elementarysymbol_is_not_abstract():
    assert not inspect.isabstract(dbl::ElementarySymbol)


def test_dbl::elementarysymbol_constructor_exists():
    assert callable(dbl::ElementarySymbol.__init__)


def test_dbl::elementarysymbol_constructor_args():
    sig = inspect.signature(dbl::ElementarySymbol.__init__)
    params = list(sig.parameters.keys())



def test_dbl::complexsymbol_is_not_abstract():
    assert not inspect.isabstract(dbl::ComplexSymbol)


def test_dbl::complexsymbol_constructor_exists():
    assert callable(dbl::ComplexSymbol.__init__)


def test_dbl::complexsymbol_constructor_args():
    sig = inspect.signature(dbl::ComplexSymbol.__init__)
    params = list(sig.parameters.keys())



def test_dbl::syntaxsymbolclassifier_is_not_abstract():
    assert not inspect.isabstract(dbl::SyntaxSymbolClassifier)


def test_dbl::syntaxsymbolclassifier_constructor_exists():
    assert callable(dbl::SyntaxSymbolClassifier.__init__)


def test_dbl::syntaxsymbolclassifier_constructor_args():
    sig = inspect.signature(dbl::SyntaxSymbolClassifier.__init__)
    params = list(sig.parameters.keys())



def test_dbl::keyword_is_not_abstract():
    assert not inspect.isabstract(dbl::Keyword)


def test_dbl::keyword_constructor_exists():
    assert callable(dbl::Keyword.__init__)


def test_dbl::keyword_constructor_args():
    sig = inspect.signature(dbl::Keyword.__init__)
    params = list(sig.parameters.keys())
    assert "keyword" in params, "Missing parameter 'keyword'"

def test_dbl::keyword_has_keyword():
    assert hasattr(dbl::Keyword, "keyword")
    descriptor = None
    for klass in dbl::Keyword.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)



def test_dbl::stringsymbol_is_not_abstract():
    assert not inspect.isabstract(dbl::StringSymbol)


def test_dbl::stringsymbol_constructor_exists():
    assert callable(dbl::StringSymbol.__init__)


def test_dbl::stringsymbol_constructor_args():
    sig = inspect.signature(dbl::StringSymbol.__init__)
    params = list(sig.parameters.keys())



def test_dbl::intsymbol_is_not_abstract():
    assert not inspect.isabstract(dbl::IntSymbol)


def test_dbl::intsymbol_constructor_exists():
    assert callable(dbl::IntSymbol.__init__)


def test_dbl::intsymbol_constructor_args():
    sig = inspect.signature(dbl::IntSymbol.__init__)
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
ElementarySymbol_strategy = st.builds(
    ElementarySymbol,
)
dbl::IdSymbol_strategy = st.builds(
    dbl::IdSymbol,
)
L1SyntaxExpression_strategy = st.builds(
    L1SyntaxExpression,
)
dbl::PlainSymbolReference_strategy = st.builds(
    dbl::PlainSymbolReference,
)
dbl::CallPart_strategy = st.builds(
    dbl::CallPart,
)
Annotation_strategy = st.builds(
    Annotation,
)
PredefinedId_strategy = st.builds(
    PredefinedId,
)
dbl::MetaLiteral_strategy = st.builds(
    dbl::MetaLiteral,
)
dbl::SizeOfArray_strategy = st.builds(
    dbl::SizeOfArray,
)
dbl::AnnotationLiteral_strategy = st.builds(
    dbl::AnnotationLiteral,
)
dbl::SuperLiteral_strategy = st.builds(
    dbl::SuperLiteral,
)
dbl::TypeLiteral_strategy = st.builds(
    dbl::TypeLiteral,
)
dbl::MeLiteral_strategy = st.builds(
    dbl::MeLiteral,
)
dbl::PredefinedId_strategy = st.builds(
    dbl::PredefinedId,
)
VariableAccess_strategy = st.builds(
    VariableAccess,
)
dbl::MetaAccess_strategy = st.builds(
    dbl::MetaAccess,
)
ElementAccess_strategy = st.builds(
    ElementAccess,
)
dbl::TypeAccess_strategy = st.builds(
    dbl::TypeAccess,
)
L3Expr_strategy = st.builds(
    L3Expr,
)
L4Expr_strategy = st.builds(
    L4Expr,
)
L5Expr_strategy = st.builds(
    L5Expr,
)
L6Expr_strategy = st.builds(
    L6Expr,
)
L7Expr_strategy = st.builds(
    L7Expr,
)
L8Expr_strategy = st.builds(
    L8Expr,
)
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
dbl::Greater_strategy = st.builds(
    dbl::Greater,
)
dbl::LessEqual_strategy = st.builds(
    dbl::LessEqual,
)
dbl::Minus_strategy = st.builds(
    dbl::Minus,
)
dbl::InstanceOf_strategy = st.builds(
    dbl::InstanceOf,
)
dbl::Plus_strategy = st.builds(
    dbl::Plus,
)
dbl::GreaterEqual_strategy = st.builds(
    dbl::GreaterEqual,
)
dbl::And_strategy = st.builds(
    dbl::And,
)
dbl::Equal_strategy = st.builds(
    dbl::Equal,
)
dbl::NotEqual_strategy = st.builds(
    dbl::NotEqual,
)
dbl::Mul_strategy = st.builds(
    dbl::Mul,
)
dbl::Less_strategy = st.builds(
    dbl::Less,
)
dbl::Or_strategy = st.builds(
    dbl::Or,
)
L1Expr_strategy = st.builds(
    L1Expr,
)
dbl::TrueLiteral_strategy = st.builds(
    dbl::TrueLiteral,
)
dbl::StringLiteral_strategy = st.builds(
    dbl::StringLiteral,
    value=
        safe_text
)
dbl::NullLiteral_strategy = st.builds(
    dbl::NullLiteral,
)
dbl::ActiveLiteral_strategy = st.builds(
    dbl::ActiveLiteral,
)
dbl::TimeLiteral_strategy = st.builds(
    dbl::TimeLiteral,
)
dbl::FalseLiteral_strategy = st.builds(
    dbl::FalseLiteral,
)
dbl::DoubleLiteral_strategy = st.builds(
    dbl::DoubleLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
dbl::IntLiteral_strategy = st.builds(
    dbl::IntLiteral,
    value=
        st.integers()
)
L2Expr_strategy = st.builds(
    L2Expr,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
dbl::Not_strategy = st.builds(
    dbl::Not,
)
dbl::Neg_strategy = st.builds(
    dbl::Neg,
)
dbl::Div_strategy = st.builds(
    dbl::Div,
)
dbl::Mod_strategy = st.builds(
    dbl::Mod,
)
dbl::SwitchCase_strategy = st.builds(
    dbl::SwitchCase,
)
LoopStatement_strategy = st.builds(
    LoopStatement,
)
dbl::WhileStatement_strategy = st.builds(
    dbl::WhileStatement,
)
Expression_strategy = st.builds(
    Expression,
)
dbl::BinaryOperator_strategy = st.builds(
    dbl::BinaryOperator,
)
dbl::L3Expr_strategy = st.builds(
    dbl::L3Expr,
)
dbl::L7Expr_strategy = st.builds(
    dbl::L7Expr,
)
dbl::ElementAccess_strategy = st.builds(
    dbl::ElementAccess,
)
dbl::UnaryOperator_strategy = st.builds(
    dbl::UnaryOperator,
)
dbl::ParseExpr_strategy = st.builds(
    dbl::ParseExpr,
)
dbl::L2Expr_strategy = st.builds(
    dbl::L2Expr,
)
dbl::L9Expr_strategy = st.builds(
    dbl::L9Expr,
)
dbl::L8Expr_strategy = st.builds(
    dbl::L8Expr,
)
dbl::L6Expr_strategy = st.builds(
    dbl::L6Expr,
)
dbl::L5Expr_strategy = st.builds(
    dbl::L5Expr,
)
dbl::L4Expr_strategy = st.builds(
    dbl::L4Expr,
)
dbl::L1Expr_strategy = st.builds(
    dbl::L1Expr,
)
dbl::LocalScope_strategy = st.builds(
    dbl::LocalScope,
)
AnnotateableElement_strategy = st.builds(
    AnnotateableElement,
)
dbl::VariableAccess_strategy = st.builds(
    dbl::VariableAccess,
)
Statement_strategy = st.builds(
    Statement,
)
dbl::IfStatement_strategy = st.builds(
    dbl::IfStatement,
)
dbl::SimpleStatement_strategy = st.builds(
    dbl::SimpleStatement,
)
dbl::LoopStatement_strategy = st.builds(
    dbl::LoopStatement,
)
dbl::NamedElement_strategy = st.builds(
    dbl::NamedElement,
    name=
        safe_text
)
SimpleStatement_strategy = st.builds(
    SimpleStatement,
)
dbl::Yield_strategy = st.builds(
    dbl::Yield,
)
dbl::Terminate_strategy = st.builds(
    dbl::Terminate,
)
dbl::YieldTo_strategy = st.builds(
    dbl::YieldTo,
)
dbl::ActivateObject_strategy = st.builds(
    dbl::ActivateObject,
    priority=
        st.integers()
)
dbl::BreakStatement_strategy = st.builds(
    dbl::BreakStatement,
)
dbl::ContinueStatement_strategy = st.builds(
    dbl::ContinueStatement,
)
dbl::Print_strategy = st.builds(
    dbl::Print,
)
dbl::Wait_strategy = st.builds(
    dbl::Wait,
)
dbl::Return_strategy = st.builds(
    dbl::Return,
)
dbl::FunctionCall_strategy = st.builds(
    dbl::FunctionCall,
)
dbl::WaitUntil_strategy = st.builds(
    dbl::WaitUntil,
)
dbl::Assignment_strategy = st.builds(
    dbl::Assignment,
)
dbl::SwitchStatement_strategy = st.builds(
    dbl::SwitchStatement,
)
dbl::Advance_strategy = st.builds(
    dbl::Advance,
)
dbl::Reactivate_strategy = st.builds(
    dbl::Reactivate,
)
AbstractVariable_strategy = st.builds(
    AbstractVariable,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
dbl::CreateObject_strategy = st.builds(
    dbl::CreateObject,
)
dbl::Cast_strategy = st.builds(
    dbl::Cast,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
dbl::BoolType_strategy = st.builds(
    dbl::BoolType,
)
dbl::IntType_strategy = st.builds(
    dbl::IntType,
)
dbl::StringType_strategy = st.builds(
    dbl::StringType,
)
dbl::DoubleType_strategy = st.builds(
    dbl::DoubleType,
)
dbl::VoidType_strategy = st.builds(
    dbl::VoidType,
)
Type_strategy = st.builds(
    Type,
)
dbl::IdExpr_strategy = st.builds(
    dbl::IdExpr,
)
dbl::PrimitiveType_strategy = st.builds(
    dbl::PrimitiveType,
)
dbl::TypedElement_strategy = st.builds(
    dbl::TypedElement,
)
dbl::ArrayDimension_strategy = st.builds(
    dbl::ArrayDimension,
)
dbl::Type_strategy = st.builds(
    dbl::Type,
)
Concept_strategy = st.builds(
    Concept,
)
dbl::SuperClassSpecification_strategy = st.builds(
    dbl::SuperClassSpecification,
)
dbl::NativeBinding_strategy = st.builds(
    dbl::NativeBinding,
    targetType=
        safe_text,
    targetLanguage=
        safe_text
)
dbl::Parameter_strategy = st.builds(
    dbl::Parameter,
)
LocalScope_strategy = st.builds(
    LocalScope,
)
dbl::Constructor_strategy = st.builds(
    dbl::Constructor,
)
dbl::LocalScopeStatement_strategy = st.builds(
    dbl::LocalScopeStatement,
)
dbl::ForStatement_strategy = st.builds(
    dbl::ForStatement,
)
ConstructiveExtensionAtContentExtensionPoint_strategy = st.builds(
    ConstructiveExtensionAtContentExtensionPoint,
)
dbl::Import_strategy = st.builds(
    dbl::Import,
    file=
        safe_text
)
dbl::Model_strategy = st.builds(
    dbl::Model,
)
Construct_strategy = st.builds(
    Construct,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
dbl::Class_strategy = st.builds(
    dbl::Class,
    active=
        st.booleans()
)
dbl::Module_strategy = st.builds(
    dbl::Module,
)
dbl::AbstractVariable_strategy = st.builds(
    dbl::AbstractVariable,
)
dbl::ExtensibleElement_strategy = st.builds(
    dbl::ExtensibleElement,
    instanceOfExtensionDefinition=
        st.booleans(),
    concreteSyntax=
        safe_text
)
ConstructiveExtension_strategy = st.builds(
    ConstructiveExtension,
)
dbl::ClassContentExtension_strategy = st.builds(
    dbl::ClassContentExtension,
)
dbl::ModuleContentExtension_strategy = st.builds(
    dbl::ModuleContentExtension,
)
dbl::ConstructiveExtensionAtContentExtensionPoint_strategy = st.builds(
    dbl::ConstructiveExtensionAtContentExtensionPoint,
)
ExtensibleElement_strategy = st.builds(
    ExtensibleElement,
)
dbl::SyntaxDefinition_strategy = st.builds(
    dbl::SyntaxDefinition,
)
dbl::Expression_strategy = st.builds(
    dbl::Expression,
)
dbl::ExtensionSemantics_strategy = st.builds(
    dbl::ExtensionSemantics,
)
dbl::Statement_strategy = st.builds(
    dbl::Statement,
)
dbl::Extension_strategy = st.builds(
    dbl::Extension,
)
dbl::ConstructiveExtension_strategy = st.builds(
    dbl::ConstructiveExtension,
)
dbl::AnnotateableElement_strategy = st.builds(
    dbl::AnnotateableElement,
)
dbl::AnnotationItem_strategy = st.builds(
    dbl::AnnotationItem,
    value=
        safe_text,
    key=
        safe_text
)
dbl::Annotation_strategy = st.builds(
    dbl::Annotation,
)
dbl::Variable_strategy = st.builds(
    dbl::Variable,
    control=
        st.booleans(),
    class_=
        st.booleans()
)
dbl::Function_strategy = st.builds(
    dbl::Function,
    detached=
        st.booleans(),
    abstract=
        st.booleans(),
    class_=
        st.booleans()
)
dbl::ExpandExpr_strategy = st.builds(
    dbl::ExpandExpr,
)
dbl::Construct_strategy = st.builds(
    dbl::Construct,
)
dbl::TestStatement_strategy = st.builds(
    dbl::TestStatement,
    value=
        st.integers()
)
dbl::Pattern_strategy = st.builds(
    dbl::Pattern,
    top=
        st.booleans()
)
Module_strategy = st.builds(
    Module,
)
Class_strategy = st.builds(
    Class,
)
dbl::ExpansionPart_strategy = st.builds(
    dbl::ExpansionPart,
)
dbl::ExpansionStatement_strategy = st.builds(
    dbl::ExpansionStatement,
    variableContext=
        st.booleans(),
    classContext=
        st.booleans(),
    functionContext=
        st.booleans()
)
Variable_strategy = st.builds(
    Variable,
)
dbl::CreateIdStatement_strategy = st.builds(
    dbl::CreateIdStatement,
)
dbl::TargetStatement_strategy = st.builds(
    dbl::TargetStatement,
)
dbl::MetaExpr_strategy = st.builds(
    dbl::MetaExpr,
)
QuotedCode_strategy = st.builds(
    QuotedCode,
)
dbl::QuotedModuleContent_strategy = st.builds(
    dbl::QuotedModuleContent,
)
dbl::QuotedStatements_strategy = st.builds(
    dbl::QuotedStatements,
)
dbl::QuotedClassContent_strategy = st.builds(
    dbl::QuotedClassContent,
)
dbl::QuotedExpression_strategy = st.builds(
    dbl::QuotedExpression,
)
dbl::QuotedCode_strategy = st.builds(
    dbl::QuotedCode,
)
dbl::CodeQuoteExpression_strategy = st.builds(
    dbl::CodeQuoteExpression,
)
dbl::ExpandStatement_strategy = st.builds(
    dbl::ExpandStatement,
)
dbl::ExpandExpression_strategy = st.builds(
    dbl::ExpandExpression,
)
ExpansionPart_strategy = st.builds(
    ExpansionPart,
)
dbl::ExpandVariablePart_strategy = st.builds(
    dbl::ExpandVariablePart,
)
dbl::ExpandTextPart_strategy = st.builds(
    dbl::ExpandTextPart,
    text=
        safe_text
)
PlainSymbolReference_strategy = st.builds(
    PlainSymbolReference,
)
dbl::StructuralSymbolReference_strategy = st.builds(
    dbl::StructuralSymbolReference,
    localScopedReference=
        st.booleans(),
    list=
        st.booleans(),
    composite=
        st.booleans(),
    globalScopedReference=
        st.booleans()
)
L2SyntaxExpression_strategy = st.builds(
    L2SyntaxExpression,
)
dbl::SymbolSequence_strategy = st.builds(
    dbl::SymbolSequence,
)
SyntaxExpression_strategy = st.builds(
    SyntaxExpression,
)
dbl::L1SyntaxExpression_strategy = st.builds(
    dbl::L1SyntaxExpression,
)
dbl::L2SyntaxExpression_strategy = st.builds(
    dbl::L2SyntaxExpression,
)
dbl::L3SyntaxExpression_strategy = st.builds(
    dbl::L3SyntaxExpression,
)
dbl::SyntaxExpression_strategy = st.builds(
    dbl::SyntaxExpression,
)
ComplexSymbol_strategy = st.builds(
    ComplexSymbol,
)
dbl::Concept_strategy = st.builds(
    dbl::Concept,
)
dbl::MetaSymbol_strategy = st.builds(
    dbl::MetaSymbol,
)
SyntaxSymbolClassifier_strategy = st.builds(
    SyntaxSymbolClassifier,
)
dbl::ElementarySymbol_strategy = st.builds(
    dbl::ElementarySymbol,
)
dbl::ComplexSymbol_strategy = st.builds(
    dbl::ComplexSymbol,
)
dbl::SyntaxSymbolClassifier_strategy = st.builds(
    dbl::SyntaxSymbolClassifier,
)
dbl::Keyword_strategy = st.builds(
    dbl::Keyword,
    keyword=
        safe_text
)
dbl::StringSymbol_strategy = st.builds(
    dbl::StringSymbol,
)
dbl::IntSymbol_strategy = st.builds(
    dbl::IntSymbol,
)

@given(instance=ElementarySymbol_strategy)
@settings(max_examples=50)
def test_elementarysymbol_instantiation(instance):
    assert isinstance(instance, ElementarySymbol)

@given(instance=dbl::IdSymbol_strategy)
@settings(max_examples=50)
def test_dbl::idsymbol_instantiation(instance):
    assert isinstance(instance, dbl::IdSymbol)

@given(instance=L1SyntaxExpression_strategy)
@settings(max_examples=50)
def test_l1syntaxexpression_instantiation(instance):
    assert isinstance(instance, L1SyntaxExpression)

@given(instance=dbl::PlainSymbolReference_strategy)
@settings(max_examples=50)
def test_dbl::plainsymbolreference_instantiation(instance):
    assert isinstance(instance, dbl::PlainSymbolReference)

@given(instance=dbl::CallPart_strategy)
@settings(max_examples=50)
def test_dbl::callpart_instantiation(instance):
    assert isinstance(instance, dbl::CallPart)

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=PredefinedId_strategy)
@settings(max_examples=50)
def test_predefinedid_instantiation(instance):
    assert isinstance(instance, PredefinedId)

@given(instance=dbl::MetaLiteral_strategy)
@settings(max_examples=50)
def test_dbl::metaliteral_instantiation(instance):
    assert isinstance(instance, dbl::MetaLiteral)

@given(instance=dbl::SizeOfArray_strategy)
@settings(max_examples=50)
def test_dbl::sizeofarray_instantiation(instance):
    assert isinstance(instance, dbl::SizeOfArray)

@given(instance=dbl::AnnotationLiteral_strategy)
@settings(max_examples=50)
def test_dbl::annotationliteral_instantiation(instance):
    assert isinstance(instance, dbl::AnnotationLiteral)

@given(instance=dbl::SuperLiteral_strategy)
@settings(max_examples=50)
def test_dbl::superliteral_instantiation(instance):
    assert isinstance(instance, dbl::SuperLiteral)

@given(instance=dbl::TypeLiteral_strategy)
@settings(max_examples=50)
def test_dbl::typeliteral_instantiation(instance):
    assert isinstance(instance, dbl::TypeLiteral)

@given(instance=dbl::MeLiteral_strategy)
@settings(max_examples=50)
def test_dbl::meliteral_instantiation(instance):
    assert isinstance(instance, dbl::MeLiteral)

@given(instance=dbl::PredefinedId_strategy)
@settings(max_examples=50)
def test_dbl::predefinedid_instantiation(instance):
    assert isinstance(instance, dbl::PredefinedId)

@given(instance=VariableAccess_strategy)
@settings(max_examples=50)
def test_variableaccess_instantiation(instance):
    assert isinstance(instance, VariableAccess)

@given(instance=dbl::MetaAccess_strategy)
@settings(max_examples=50)
def test_dbl::metaaccess_instantiation(instance):
    assert isinstance(instance, dbl::MetaAccess)

@given(instance=ElementAccess_strategy)
@settings(max_examples=50)
def test_elementaccess_instantiation(instance):
    assert isinstance(instance, ElementAccess)

@given(instance=dbl::TypeAccess_strategy)
@settings(max_examples=50)
def test_dbl::typeaccess_instantiation(instance):
    assert isinstance(instance, dbl::TypeAccess)

@given(instance=L3Expr_strategy)
@settings(max_examples=50)
def test_l3expr_instantiation(instance):
    assert isinstance(instance, L3Expr)

@given(instance=L4Expr_strategy)
@settings(max_examples=50)
def test_l4expr_instantiation(instance):
    assert isinstance(instance, L4Expr)

@given(instance=L5Expr_strategy)
@settings(max_examples=50)
def test_l5expr_instantiation(instance):
    assert isinstance(instance, L5Expr)

@given(instance=L6Expr_strategy)
@settings(max_examples=50)
def test_l6expr_instantiation(instance):
    assert isinstance(instance, L6Expr)

@given(instance=L7Expr_strategy)
@settings(max_examples=50)
def test_l7expr_instantiation(instance):
    assert isinstance(instance, L7Expr)

@given(instance=L8Expr_strategy)
@settings(max_examples=50)
def test_l8expr_instantiation(instance):
    assert isinstance(instance, L8Expr)

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=dbl::Greater_strategy)
@settings(max_examples=50)
def test_dbl::greater_instantiation(instance):
    assert isinstance(instance, dbl::Greater)

@given(instance=dbl::LessEqual_strategy)
@settings(max_examples=50)
def test_dbl::lessequal_instantiation(instance):
    assert isinstance(instance, dbl::LessEqual)

@given(instance=dbl::Minus_strategy)
@settings(max_examples=50)
def test_dbl::minus_instantiation(instance):
    assert isinstance(instance, dbl::Minus)

@given(instance=dbl::InstanceOf_strategy)
@settings(max_examples=50)
def test_dbl::instanceof_instantiation(instance):
    assert isinstance(instance, dbl::InstanceOf)

@given(instance=dbl::Plus_strategy)
@settings(max_examples=50)
def test_dbl::plus_instantiation(instance):
    assert isinstance(instance, dbl::Plus)

@given(instance=dbl::GreaterEqual_strategy)
@settings(max_examples=50)
def test_dbl::greaterequal_instantiation(instance):
    assert isinstance(instance, dbl::GreaterEqual)

@given(instance=dbl::And_strategy)
@settings(max_examples=50)
def test_dbl::and_instantiation(instance):
    assert isinstance(instance, dbl::And)

@given(instance=dbl::Equal_strategy)
@settings(max_examples=50)
def test_dbl::equal_instantiation(instance):
    assert isinstance(instance, dbl::Equal)

@given(instance=dbl::NotEqual_strategy)
@settings(max_examples=50)
def test_dbl::notequal_instantiation(instance):
    assert isinstance(instance, dbl::NotEqual)

@given(instance=dbl::Mul_strategy)
@settings(max_examples=50)
def test_dbl::mul_instantiation(instance):
    assert isinstance(instance, dbl::Mul)

@given(instance=dbl::Less_strategy)
@settings(max_examples=50)
def test_dbl::less_instantiation(instance):
    assert isinstance(instance, dbl::Less)

@given(instance=dbl::Or_strategy)
@settings(max_examples=50)
def test_dbl::or_instantiation(instance):
    assert isinstance(instance, dbl::Or)

@given(instance=L1Expr_strategy)
@settings(max_examples=50)
def test_l1expr_instantiation(instance):
    assert isinstance(instance, L1Expr)

@given(instance=dbl::TrueLiteral_strategy)
@settings(max_examples=50)
def test_dbl::trueliteral_instantiation(instance):
    assert isinstance(instance, dbl::TrueLiteral)

@given(instance=dbl::StringLiteral_strategy)
@settings(max_examples=50)
def test_dbl::stringliteral_instantiation(instance):
    assert isinstance(instance, dbl::StringLiteral)

@given(instance=dbl::StringLiteral_strategy)
def test_dbl::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=dbl::StringLiteral_strategy)
def test_dbl::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dbl::NullLiteral_strategy)
@settings(max_examples=50)
def test_dbl::nullliteral_instantiation(instance):
    assert isinstance(instance, dbl::NullLiteral)

@given(instance=dbl::ActiveLiteral_strategy)
@settings(max_examples=50)
def test_dbl::activeliteral_instantiation(instance):
    assert isinstance(instance, dbl::ActiveLiteral)

@given(instance=dbl::TimeLiteral_strategy)
@settings(max_examples=50)
def test_dbl::timeliteral_instantiation(instance):
    assert isinstance(instance, dbl::TimeLiteral)

@given(instance=dbl::FalseLiteral_strategy)
@settings(max_examples=50)
def test_dbl::falseliteral_instantiation(instance):
    assert isinstance(instance, dbl::FalseLiteral)

@given(instance=dbl::DoubleLiteral_strategy)
@settings(max_examples=50)
def test_dbl::doubleliteral_instantiation(instance):
    assert isinstance(instance, dbl::DoubleLiteral)

@given(instance=dbl::DoubleLiteral_strategy)
def test_dbl::doubleliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=dbl::DoubleLiteral_strategy)
def test_dbl::doubleliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dbl::IntLiteral_strategy)
@settings(max_examples=50)
def test_dbl::intliteral_instantiation(instance):
    assert isinstance(instance, dbl::IntLiteral)

@given(instance=dbl::IntLiteral_strategy)
def test_dbl::intliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=dbl::IntLiteral_strategy)
def test_dbl::intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=L2Expr_strategy)
@settings(max_examples=50)
def test_l2expr_instantiation(instance):
    assert isinstance(instance, L2Expr)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=dbl::Not_strategy)
@settings(max_examples=50)
def test_dbl::not_instantiation(instance):
    assert isinstance(instance, dbl::Not)

@given(instance=dbl::Neg_strategy)
@settings(max_examples=50)
def test_dbl::neg_instantiation(instance):
    assert isinstance(instance, dbl::Neg)

@given(instance=dbl::Div_strategy)
@settings(max_examples=50)
def test_dbl::div_instantiation(instance):
    assert isinstance(instance, dbl::Div)

@given(instance=dbl::Mod_strategy)
@settings(max_examples=50)
def test_dbl::mod_instantiation(instance):
    assert isinstance(instance, dbl::Mod)

@given(instance=dbl::SwitchCase_strategy)
@settings(max_examples=50)
def test_dbl::switchcase_instantiation(instance):
    assert isinstance(instance, dbl::SwitchCase)

@given(instance=LoopStatement_strategy)
@settings(max_examples=50)
def test_loopstatement_instantiation(instance):
    assert isinstance(instance, LoopStatement)

@given(instance=dbl::WhileStatement_strategy)
@settings(max_examples=50)
def test_dbl::whilestatement_instantiation(instance):
    assert isinstance(instance, dbl::WhileStatement)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=dbl::BinaryOperator_strategy)
@settings(max_examples=50)
def test_dbl::binaryoperator_instantiation(instance):
    assert isinstance(instance, dbl::BinaryOperator)

@given(instance=dbl::L3Expr_strategy)
@settings(max_examples=50)
def test_dbl::l3expr_instantiation(instance):
    assert isinstance(instance, dbl::L3Expr)

@given(instance=dbl::L7Expr_strategy)
@settings(max_examples=50)
def test_dbl::l7expr_instantiation(instance):
    assert isinstance(instance, dbl::L7Expr)

@given(instance=dbl::ElementAccess_strategy)
@settings(max_examples=50)
def test_dbl::elementaccess_instantiation(instance):
    assert isinstance(instance, dbl::ElementAccess)

@given(instance=dbl::UnaryOperator_strategy)
@settings(max_examples=50)
def test_dbl::unaryoperator_instantiation(instance):
    assert isinstance(instance, dbl::UnaryOperator)

@given(instance=dbl::ParseExpr_strategy)
@settings(max_examples=50)
def test_dbl::parseexpr_instantiation(instance):
    assert isinstance(instance, dbl::ParseExpr)

@given(instance=dbl::L2Expr_strategy)
@settings(max_examples=50)
def test_dbl::l2expr_instantiation(instance):
    assert isinstance(instance, dbl::L2Expr)

@given(instance=dbl::L9Expr_strategy)
@settings(max_examples=50)
def test_dbl::l9expr_instantiation(instance):
    assert isinstance(instance, dbl::L9Expr)

@given(instance=dbl::L8Expr_strategy)
@settings(max_examples=50)
def test_dbl::l8expr_instantiation(instance):
    assert isinstance(instance, dbl::L8Expr)

@given(instance=dbl::L6Expr_strategy)
@settings(max_examples=50)
def test_dbl::l6expr_instantiation(instance):
    assert isinstance(instance, dbl::L6Expr)

@given(instance=dbl::L5Expr_strategy)
@settings(max_examples=50)
def test_dbl::l5expr_instantiation(instance):
    assert isinstance(instance, dbl::L5Expr)

@given(instance=dbl::L4Expr_strategy)
@settings(max_examples=50)
def test_dbl::l4expr_instantiation(instance):
    assert isinstance(instance, dbl::L4Expr)

@given(instance=dbl::L1Expr_strategy)
@settings(max_examples=50)
def test_dbl::l1expr_instantiation(instance):
    assert isinstance(instance, dbl::L1Expr)

@given(instance=dbl::LocalScope_strategy)
@settings(max_examples=50)
def test_dbl::localscope_instantiation(instance):
    assert isinstance(instance, dbl::LocalScope)

@given(instance=AnnotateableElement_strategy)
@settings(max_examples=50)
def test_annotateableelement_instantiation(instance):
    assert isinstance(instance, AnnotateableElement)

@given(instance=dbl::VariableAccess_strategy)
@settings(max_examples=50)
def test_dbl::variableaccess_instantiation(instance):
    assert isinstance(instance, dbl::VariableAccess)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=dbl::IfStatement_strategy)
@settings(max_examples=50)
def test_dbl::ifstatement_instantiation(instance):
    assert isinstance(instance, dbl::IfStatement)

@given(instance=dbl::SimpleStatement_strategy)
@settings(max_examples=50)
def test_dbl::simplestatement_instantiation(instance):
    assert isinstance(instance, dbl::SimpleStatement)

@given(instance=dbl::LoopStatement_strategy)
@settings(max_examples=50)
def test_dbl::loopstatement_instantiation(instance):
    assert isinstance(instance, dbl::LoopStatement)

@given(instance=dbl::NamedElement_strategy)
@settings(max_examples=50)
def test_dbl::namedelement_instantiation(instance):
    assert isinstance(instance, dbl::NamedElement)

@given(instance=dbl::NamedElement_strategy)
def test_dbl::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dbl::NamedElement_strategy)
def test_dbl::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimpleStatement_strategy)
@settings(max_examples=50)
def test_simplestatement_instantiation(instance):
    assert isinstance(instance, SimpleStatement)

@given(instance=dbl::Yield_strategy)
@settings(max_examples=50)
def test_dbl::yield_instantiation(instance):
    assert isinstance(instance, dbl::Yield)

@given(instance=dbl::Terminate_strategy)
@settings(max_examples=50)
def test_dbl::terminate_instantiation(instance):
    assert isinstance(instance, dbl::Terminate)

@given(instance=dbl::YieldTo_strategy)
@settings(max_examples=50)
def test_dbl::yieldto_instantiation(instance):
    assert isinstance(instance, dbl::YieldTo)

@given(instance=dbl::ActivateObject_strategy)
@settings(max_examples=50)
def test_dbl::activateobject_instantiation(instance):
    assert isinstance(instance, dbl::ActivateObject)

@given(instance=dbl::ActivateObject_strategy)
def test_dbl::activateobject_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=dbl::ActivateObject_strategy)
def test_dbl::activateobject_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=dbl::BreakStatement_strategy)
@settings(max_examples=50)
def test_dbl::breakstatement_instantiation(instance):
    assert isinstance(instance, dbl::BreakStatement)

@given(instance=dbl::ContinueStatement_strategy)
@settings(max_examples=50)
def test_dbl::continuestatement_instantiation(instance):
    assert isinstance(instance, dbl::ContinueStatement)

@given(instance=dbl::Print_strategy)
@settings(max_examples=50)
def test_dbl::print_instantiation(instance):
    assert isinstance(instance, dbl::Print)

@given(instance=dbl::Wait_strategy)
@settings(max_examples=50)
def test_dbl::wait_instantiation(instance):
    assert isinstance(instance, dbl::Wait)

@given(instance=dbl::Return_strategy)
@settings(max_examples=50)
def test_dbl::return_instantiation(instance):
    assert isinstance(instance, dbl::Return)

@given(instance=dbl::FunctionCall_strategy)
@settings(max_examples=50)
def test_dbl::functioncall_instantiation(instance):
    assert isinstance(instance, dbl::FunctionCall)

@given(instance=dbl::WaitUntil_strategy)
@settings(max_examples=50)
def test_dbl::waituntil_instantiation(instance):
    assert isinstance(instance, dbl::WaitUntil)

@given(instance=dbl::Assignment_strategy)
@settings(max_examples=50)
def test_dbl::assignment_instantiation(instance):
    assert isinstance(instance, dbl::Assignment)

@given(instance=dbl::SwitchStatement_strategy)
@settings(max_examples=50)
def test_dbl::switchstatement_instantiation(instance):
    assert isinstance(instance, dbl::SwitchStatement)

@given(instance=dbl::Advance_strategy)
@settings(max_examples=50)
def test_dbl::advance_instantiation(instance):
    assert isinstance(instance, dbl::Advance)

@given(instance=dbl::Reactivate_strategy)
@settings(max_examples=50)
def test_dbl::reactivate_instantiation(instance):
    assert isinstance(instance, dbl::Reactivate)

@given(instance=AbstractVariable_strategy)
@settings(max_examples=50)
def test_abstractvariable_instantiation(instance):
    assert isinstance(instance, AbstractVariable)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=dbl::CreateObject_strategy)
@settings(max_examples=50)
def test_dbl::createobject_instantiation(instance):
    assert isinstance(instance, dbl::CreateObject)

@given(instance=dbl::Cast_strategy)
@settings(max_examples=50)
def test_dbl::cast_instantiation(instance):
    assert isinstance(instance, dbl::Cast)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=dbl::BoolType_strategy)
@settings(max_examples=50)
def test_dbl::booltype_instantiation(instance):
    assert isinstance(instance, dbl::BoolType)

@given(instance=dbl::IntType_strategy)
@settings(max_examples=50)
def test_dbl::inttype_instantiation(instance):
    assert isinstance(instance, dbl::IntType)

@given(instance=dbl::StringType_strategy)
@settings(max_examples=50)
def test_dbl::stringtype_instantiation(instance):
    assert isinstance(instance, dbl::StringType)

@given(instance=dbl::DoubleType_strategy)
@settings(max_examples=50)
def test_dbl::doubletype_instantiation(instance):
    assert isinstance(instance, dbl::DoubleType)

@given(instance=dbl::VoidType_strategy)
@settings(max_examples=50)
def test_dbl::voidtype_instantiation(instance):
    assert isinstance(instance, dbl::VoidType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=dbl::IdExpr_strategy)
@settings(max_examples=50)
def test_dbl::idexpr_instantiation(instance):
    assert isinstance(instance, dbl::IdExpr)

@given(instance=dbl::PrimitiveType_strategy)
@settings(max_examples=50)
def test_dbl::primitivetype_instantiation(instance):
    assert isinstance(instance, dbl::PrimitiveType)

@given(instance=dbl::TypedElement_strategy)
@settings(max_examples=50)
def test_dbl::typedelement_instantiation(instance):
    assert isinstance(instance, dbl::TypedElement)

@given(instance=dbl::ArrayDimension_strategy)
@settings(max_examples=50)
def test_dbl::arraydimension_instantiation(instance):
    assert isinstance(instance, dbl::ArrayDimension)

@given(instance=dbl::Type_strategy)
@settings(max_examples=50)
def test_dbl::type_instantiation(instance):
    assert isinstance(instance, dbl::Type)

@given(instance=Concept_strategy)
@settings(max_examples=50)
def test_concept_instantiation(instance):
    assert isinstance(instance, Concept)

@given(instance=dbl::SuperClassSpecification_strategy)
@settings(max_examples=50)
def test_dbl::superclassspecification_instantiation(instance):
    assert isinstance(instance, dbl::SuperClassSpecification)

@given(instance=dbl::NativeBinding_strategy)
@settings(max_examples=50)
def test_dbl::nativebinding_instantiation(instance):
    assert isinstance(instance, dbl::NativeBinding)

@given(instance=dbl::NativeBinding_strategy)
def test_dbl::nativebinding_targetType_type(instance):
    assert isinstance(instance.targetType, str)


@given(instance=dbl::NativeBinding_strategy)
def test_dbl::nativebinding_targetType_setter(instance):
    original = instance.targetType
    instance.targetType = original
    assert instance.targetType == original

@given(instance=dbl::NativeBinding_strategy)
def test_dbl::nativebinding_targetLanguage_type(instance):
    assert isinstance(instance.targetLanguage, str)


@given(instance=dbl::NativeBinding_strategy)
def test_dbl::nativebinding_targetLanguage_setter(instance):
    original = instance.targetLanguage
    instance.targetLanguage = original
    assert instance.targetLanguage == original

@given(instance=dbl::Parameter_strategy)
@settings(max_examples=50)
def test_dbl::parameter_instantiation(instance):
    assert isinstance(instance, dbl::Parameter)

@given(instance=LocalScope_strategy)
@settings(max_examples=50)
def test_localscope_instantiation(instance):
    assert isinstance(instance, LocalScope)

@given(instance=dbl::Constructor_strategy)
@settings(max_examples=50)
def test_dbl::constructor_instantiation(instance):
    assert isinstance(instance, dbl::Constructor)

@given(instance=dbl::LocalScopeStatement_strategy)
@settings(max_examples=50)
def test_dbl::localscopestatement_instantiation(instance):
    assert isinstance(instance, dbl::LocalScopeStatement)

@given(instance=dbl::ForStatement_strategy)
@settings(max_examples=50)
def test_dbl::forstatement_instantiation(instance):
    assert isinstance(instance, dbl::ForStatement)

@given(instance=ConstructiveExtensionAtContentExtensionPoint_strategy)
@settings(max_examples=50)
def test_constructiveextensionatcontentextensionpoint_instantiation(instance):
    assert isinstance(instance, ConstructiveExtensionAtContentExtensionPoint)

@given(instance=dbl::Import_strategy)
@settings(max_examples=50)
def test_dbl::import_instantiation(instance):
    assert isinstance(instance, dbl::Import)

@given(instance=dbl::Import_strategy)
def test_dbl::import_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=dbl::Import_strategy)
def test_dbl::import_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=dbl::Model_strategy)
@settings(max_examples=50)
def test_dbl::model_instantiation(instance):
    assert isinstance(instance, dbl::Model)

@given(instance=Construct_strategy)
@settings(max_examples=50)
def test_construct_instantiation(instance):
    assert isinstance(instance, Construct)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=dbl::Class_strategy)
@settings(max_examples=50)
def test_dbl::class_instantiation(instance):
    assert isinstance(instance, dbl::Class)

@given(instance=dbl::Class_strategy)
def test_dbl::class_active_type(instance):
    assert isinstance(instance.active, bool)


@given(instance=dbl::Class_strategy)
def test_dbl::class_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=dbl::Module_strategy)
@settings(max_examples=50)
def test_dbl::module_instantiation(instance):
    assert isinstance(instance, dbl::Module)

@given(instance=dbl::AbstractVariable_strategy)
@settings(max_examples=50)
def test_dbl::abstractvariable_instantiation(instance):
    assert isinstance(instance, dbl::AbstractVariable)

@given(instance=dbl::ExtensibleElement_strategy)
@settings(max_examples=50)
def test_dbl::extensibleelement_instantiation(instance):
    assert isinstance(instance, dbl::ExtensibleElement)

@given(instance=dbl::ExtensibleElement_strategy)
def test_dbl::extensibleelement_instanceOfExtensionDefinition_type(instance):
    assert isinstance(instance.instanceOfExtensionDefinition, bool)


@given(instance=dbl::ExtensibleElement_strategy)
def test_dbl::extensibleelement_instanceOfExtensionDefinition_setter(instance):
    original = instance.instanceOfExtensionDefinition
    instance.instanceOfExtensionDefinition = original
    assert instance.instanceOfExtensionDefinition == original

@given(instance=dbl::ExtensibleElement_strategy)
def test_dbl::extensibleelement_concreteSyntax_type(instance):
    assert isinstance(instance.concreteSyntax, str)


@given(instance=dbl::ExtensibleElement_strategy)
def test_dbl::extensibleelement_concreteSyntax_setter(instance):
    original = instance.concreteSyntax
    instance.concreteSyntax = original
    assert instance.concreteSyntax == original

@given(instance=ConstructiveExtension_strategy)
@settings(max_examples=50)
def test_constructiveextension_instantiation(instance):
    assert isinstance(instance, ConstructiveExtension)

@given(instance=dbl::ClassContentExtension_strategy)
@settings(max_examples=50)
def test_dbl::classcontentextension_instantiation(instance):
    assert isinstance(instance, dbl::ClassContentExtension)

@given(instance=dbl::ModuleContentExtension_strategy)
@settings(max_examples=50)
def test_dbl::modulecontentextension_instantiation(instance):
    assert isinstance(instance, dbl::ModuleContentExtension)

@given(instance=dbl::ConstructiveExtensionAtContentExtensionPoint_strategy)
@settings(max_examples=50)
def test_dbl::constructiveextensionatcontentextensionpoint_instantiation(instance):
    assert isinstance(instance, dbl::ConstructiveExtensionAtContentExtensionPoint)

@given(instance=ExtensibleElement_strategy)
@settings(max_examples=50)
def test_extensibleelement_instantiation(instance):
    assert isinstance(instance, ExtensibleElement)

@given(instance=dbl::SyntaxDefinition_strategy)
@settings(max_examples=50)
def test_dbl::syntaxdefinition_instantiation(instance):
    assert isinstance(instance, dbl::SyntaxDefinition)

@given(instance=dbl::Expression_strategy)
@settings(max_examples=50)
def test_dbl::expression_instantiation(instance):
    assert isinstance(instance, dbl::Expression)

@given(instance=dbl::ExtensionSemantics_strategy)
@settings(max_examples=50)
def test_dbl::extensionsemantics_instantiation(instance):
    assert isinstance(instance, dbl::ExtensionSemantics)

@given(instance=dbl::Statement_strategy)
@settings(max_examples=50)
def test_dbl::statement_instantiation(instance):
    assert isinstance(instance, dbl::Statement)

@given(instance=dbl::Extension_strategy)
@settings(max_examples=50)
def test_dbl::extension_instantiation(instance):
    assert isinstance(instance, dbl::Extension)

@given(instance=dbl::ConstructiveExtension_strategy)
@settings(max_examples=50)
def test_dbl::constructiveextension_instantiation(instance):
    assert isinstance(instance, dbl::ConstructiveExtension)

@given(instance=dbl::AnnotateableElement_strategy)
@settings(max_examples=50)
def test_dbl::annotateableelement_instantiation(instance):
    assert isinstance(instance, dbl::AnnotateableElement)

@given(instance=dbl::AnnotationItem_strategy)
@settings(max_examples=50)
def test_dbl::annotationitem_instantiation(instance):
    assert isinstance(instance, dbl::AnnotationItem)

@given(instance=dbl::AnnotationItem_strategy)
def test_dbl::annotationitem_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=dbl::AnnotationItem_strategy)
def test_dbl::annotationitem_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dbl::AnnotationItem_strategy)
def test_dbl::annotationitem_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=dbl::AnnotationItem_strategy)
def test_dbl::annotationitem_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=dbl::Annotation_strategy)
@settings(max_examples=50)
def test_dbl::annotation_instantiation(instance):
    assert isinstance(instance, dbl::Annotation)

@given(instance=dbl::Variable_strategy)
@settings(max_examples=50)
def test_dbl::variable_instantiation(instance):
    assert isinstance(instance, dbl::Variable)

@given(instance=dbl::Variable_strategy)
def test_dbl::variable_control_type(instance):
    assert isinstance(instance.control, bool)


@given(instance=dbl::Variable_strategy)
def test_dbl::variable_control_setter(instance):
    original = instance.control
    instance.control = original
    assert instance.control == original

@given(instance=dbl::Variable_strategy)
def test_dbl::variable_class__type(instance):
    assert isinstance(instance.class_, bool)


@given(instance=dbl::Variable_strategy)
def test_dbl::variable_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=dbl::Function_strategy)
@settings(max_examples=50)
def test_dbl::function_instantiation(instance):
    assert isinstance(instance, dbl::Function)

@given(instance=dbl::Function_strategy)
def test_dbl::function_detached_type(instance):
    assert isinstance(instance.detached, bool)


@given(instance=dbl::Function_strategy)
def test_dbl::function_detached_setter(instance):
    original = instance.detached
    instance.detached = original
    assert instance.detached == original

@given(instance=dbl::Function_strategy)
def test_dbl::function_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=dbl::Function_strategy)
def test_dbl::function_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=dbl::Function_strategy)
def test_dbl::function_class__type(instance):
    assert isinstance(instance.class_, bool)


@given(instance=dbl::Function_strategy)
def test_dbl::function_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=dbl::ExpandExpr_strategy)
@settings(max_examples=50)
def test_dbl::expandexpr_instantiation(instance):
    assert isinstance(instance, dbl::ExpandExpr)

@given(instance=dbl::Construct_strategy)
@settings(max_examples=50)
def test_dbl::construct_instantiation(instance):
    assert isinstance(instance, dbl::Construct)

@given(instance=dbl::TestStatement_strategy)
@settings(max_examples=50)
def test_dbl::teststatement_instantiation(instance):
    assert isinstance(instance, dbl::TestStatement)

@given(instance=dbl::TestStatement_strategy)
def test_dbl::teststatement_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=dbl::TestStatement_strategy)
def test_dbl::teststatement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dbl::Pattern_strategy)
@settings(max_examples=50)
def test_dbl::pattern_instantiation(instance):
    assert isinstance(instance, dbl::Pattern)

@given(instance=dbl::Pattern_strategy)
def test_dbl::pattern_top_type(instance):
    assert isinstance(instance.top, bool)


@given(instance=dbl::Pattern_strategy)
def test_dbl::pattern_top_setter(instance):
    original = instance.top
    instance.top = original
    assert instance.top == original

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=dbl::ExpansionPart_strategy)
@settings(max_examples=50)
def test_dbl::expansionpart_instantiation(instance):
    assert isinstance(instance, dbl::ExpansionPart)

@given(instance=dbl::ExpansionStatement_strategy)
@settings(max_examples=50)
def test_dbl::expansionstatement_instantiation(instance):
    assert isinstance(instance, dbl::ExpansionStatement)

@given(instance=dbl::ExpansionStatement_strategy)
def test_dbl::expansionstatement_variableContext_type(instance):
    assert isinstance(instance.variableContext, bool)


@given(instance=dbl::ExpansionStatement_strategy)
def test_dbl::expansionstatement_variableContext_setter(instance):
    original = instance.variableContext
    instance.variableContext = original
    assert instance.variableContext == original

@given(instance=dbl::ExpansionStatement_strategy)
def test_dbl::expansionstatement_classContext_type(instance):
    assert isinstance(instance.classContext, bool)


@given(instance=dbl::ExpansionStatement_strategy)
def test_dbl::expansionstatement_classContext_setter(instance):
    original = instance.classContext
    instance.classContext = original
    assert instance.classContext == original

@given(instance=dbl::ExpansionStatement_strategy)
def test_dbl::expansionstatement_functionContext_type(instance):
    assert isinstance(instance.functionContext, bool)


@given(instance=dbl::ExpansionStatement_strategy)
def test_dbl::expansionstatement_functionContext_setter(instance):
    original = instance.functionContext
    instance.functionContext = original
    assert instance.functionContext == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=dbl::CreateIdStatement_strategy)
@settings(max_examples=50)
def test_dbl::createidstatement_instantiation(instance):
    assert isinstance(instance, dbl::CreateIdStatement)

@given(instance=dbl::TargetStatement_strategy)
@settings(max_examples=50)
def test_dbl::targetstatement_instantiation(instance):
    assert isinstance(instance, dbl::TargetStatement)

@given(instance=dbl::MetaExpr_strategy)
@settings(max_examples=50)
def test_dbl::metaexpr_instantiation(instance):
    assert isinstance(instance, dbl::MetaExpr)

@given(instance=QuotedCode_strategy)
@settings(max_examples=50)
def test_quotedcode_instantiation(instance):
    assert isinstance(instance, QuotedCode)

@given(instance=dbl::QuotedModuleContent_strategy)
@settings(max_examples=50)
def test_dbl::quotedmodulecontent_instantiation(instance):
    assert isinstance(instance, dbl::QuotedModuleContent)

@given(instance=dbl::QuotedStatements_strategy)
@settings(max_examples=50)
def test_dbl::quotedstatements_instantiation(instance):
    assert isinstance(instance, dbl::QuotedStatements)

@given(instance=dbl::QuotedClassContent_strategy)
@settings(max_examples=50)
def test_dbl::quotedclasscontent_instantiation(instance):
    assert isinstance(instance, dbl::QuotedClassContent)

@given(instance=dbl::QuotedExpression_strategy)
@settings(max_examples=50)
def test_dbl::quotedexpression_instantiation(instance):
    assert isinstance(instance, dbl::QuotedExpression)

@given(instance=dbl::QuotedCode_strategy)
@settings(max_examples=50)
def test_dbl::quotedcode_instantiation(instance):
    assert isinstance(instance, dbl::QuotedCode)

@given(instance=dbl::CodeQuoteExpression_strategy)
@settings(max_examples=50)
def test_dbl::codequoteexpression_instantiation(instance):
    assert isinstance(instance, dbl::CodeQuoteExpression)

@given(instance=dbl::ExpandStatement_strategy)
@settings(max_examples=50)
def test_dbl::expandstatement_instantiation(instance):
    assert isinstance(instance, dbl::ExpandStatement)

@given(instance=dbl::ExpandExpression_strategy)
@settings(max_examples=50)
def test_dbl::expandexpression_instantiation(instance):
    assert isinstance(instance, dbl::ExpandExpression)

@given(instance=ExpansionPart_strategy)
@settings(max_examples=50)
def test_expansionpart_instantiation(instance):
    assert isinstance(instance, ExpansionPart)

@given(instance=dbl::ExpandVariablePart_strategy)
@settings(max_examples=50)
def test_dbl::expandvariablepart_instantiation(instance):
    assert isinstance(instance, dbl::ExpandVariablePart)

@given(instance=dbl::ExpandTextPart_strategy)
@settings(max_examples=50)
def test_dbl::expandtextpart_instantiation(instance):
    assert isinstance(instance, dbl::ExpandTextPart)

@given(instance=dbl::ExpandTextPart_strategy)
def test_dbl::expandtextpart_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=dbl::ExpandTextPart_strategy)
def test_dbl::expandtextpart_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=PlainSymbolReference_strategy)
@settings(max_examples=50)
def test_plainsymbolreference_instantiation(instance):
    assert isinstance(instance, PlainSymbolReference)

@given(instance=dbl::StructuralSymbolReference_strategy)
@settings(max_examples=50)
def test_dbl::structuralsymbolreference_instantiation(instance):
    assert isinstance(instance, dbl::StructuralSymbolReference)

@given(instance=dbl::StructuralSymbolReference_strategy)
def test_dbl::structuralsymbolreference_localScopedReference_type(instance):
    assert isinstance(instance.localScopedReference, bool)


@given(instance=dbl::StructuralSymbolReference_strategy)
def test_dbl::structuralsymbolreference_localScopedReference_setter(instance):
    original = instance.localScopedReference
    instance.localScopedReference = original
    assert instance.localScopedReference == original

@given(instance=dbl::StructuralSymbolReference_strategy)
def test_dbl::structuralsymbolreference_list_type(instance):
    assert isinstance(instance.list, bool)


@given(instance=dbl::StructuralSymbolReference_strategy)
def test_dbl::structuralsymbolreference_list_setter(instance):
    original = instance.list
    instance.list = original
    assert instance.list == original

@given(instance=dbl::StructuralSymbolReference_strategy)
def test_dbl::structuralsymbolreference_composite_type(instance):
    assert isinstance(instance.composite, bool)


@given(instance=dbl::StructuralSymbolReference_strategy)
def test_dbl::structuralsymbolreference_composite_setter(instance):
    original = instance.composite
    instance.composite = original
    assert instance.composite == original

@given(instance=dbl::StructuralSymbolReference_strategy)
def test_dbl::structuralsymbolreference_globalScopedReference_type(instance):
    assert isinstance(instance.globalScopedReference, bool)


@given(instance=dbl::StructuralSymbolReference_strategy)
def test_dbl::structuralsymbolreference_globalScopedReference_setter(instance):
    original = instance.globalScopedReference
    instance.globalScopedReference = original
    assert instance.globalScopedReference == original

@given(instance=L2SyntaxExpression_strategy)
@settings(max_examples=50)
def test_l2syntaxexpression_instantiation(instance):
    assert isinstance(instance, L2SyntaxExpression)

@given(instance=dbl::SymbolSequence_strategy)
@settings(max_examples=50)
def test_dbl::symbolsequence_instantiation(instance):
    assert isinstance(instance, dbl::SymbolSequence)

@given(instance=SyntaxExpression_strategy)
@settings(max_examples=50)
def test_syntaxexpression_instantiation(instance):
    assert isinstance(instance, SyntaxExpression)

@given(instance=dbl::L1SyntaxExpression_strategy)
@settings(max_examples=50)
def test_dbl::l1syntaxexpression_instantiation(instance):
    assert isinstance(instance, dbl::L1SyntaxExpression)

@given(instance=dbl::L2SyntaxExpression_strategy)
@settings(max_examples=50)
def test_dbl::l2syntaxexpression_instantiation(instance):
    assert isinstance(instance, dbl::L2SyntaxExpression)

@given(instance=dbl::L3SyntaxExpression_strategy)
@settings(max_examples=50)
def test_dbl::l3syntaxexpression_instantiation(instance):
    assert isinstance(instance, dbl::L3SyntaxExpression)

@given(instance=dbl::SyntaxExpression_strategy)
@settings(max_examples=50)
def test_dbl::syntaxexpression_instantiation(instance):
    assert isinstance(instance, dbl::SyntaxExpression)

@given(instance=ComplexSymbol_strategy)
@settings(max_examples=50)
def test_complexsymbol_instantiation(instance):
    assert isinstance(instance, ComplexSymbol)

@given(instance=dbl::Concept_strategy)
@settings(max_examples=50)
def test_dbl::concept_instantiation(instance):
    assert isinstance(instance, dbl::Concept)

@given(instance=dbl::MetaSymbol_strategy)
@settings(max_examples=50)
def test_dbl::metasymbol_instantiation(instance):
    assert isinstance(instance, dbl::MetaSymbol)

@given(instance=SyntaxSymbolClassifier_strategy)
@settings(max_examples=50)
def test_syntaxsymbolclassifier_instantiation(instance):
    assert isinstance(instance, SyntaxSymbolClassifier)

@given(instance=dbl::ElementarySymbol_strategy)
@settings(max_examples=50)
def test_dbl::elementarysymbol_instantiation(instance):
    assert isinstance(instance, dbl::ElementarySymbol)

@given(instance=dbl::ComplexSymbol_strategy)
@settings(max_examples=50)
def test_dbl::complexsymbol_instantiation(instance):
    assert isinstance(instance, dbl::ComplexSymbol)

@given(instance=dbl::SyntaxSymbolClassifier_strategy)
@settings(max_examples=50)
def test_dbl::syntaxsymbolclassifier_instantiation(instance):
    assert isinstance(instance, dbl::SyntaxSymbolClassifier)

@given(instance=dbl::Keyword_strategy)
@settings(max_examples=50)
def test_dbl::keyword_instantiation(instance):
    assert isinstance(instance, dbl::Keyword)

@given(instance=dbl::Keyword_strategy)
def test_dbl::keyword_keyword_type(instance):
    assert isinstance(instance.keyword, str)


@given(instance=dbl::Keyword_strategy)
def test_dbl::keyword_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=dbl::StringSymbol_strategy)
@settings(max_examples=50)
def test_dbl::stringsymbol_instantiation(instance):
    assert isinstance(instance, dbl::StringSymbol)

@given(instance=dbl::IntSymbol_strategy)
@settings(max_examples=50)
def test_dbl::intsymbol_instantiation(instance):
    assert isinstance(instance, dbl::IntSymbol)
