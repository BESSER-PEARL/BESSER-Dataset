import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ComparisonExpression,
    model::GreaterEqualExpression,
    model::GreaterExpression,
    EquivalenceExpression,
    model::InequalityExpression,
    model::EqualityExpression,
    PredicateExpression,
    QuantifierExpression,
    model::ExistsExpression,
    model::ForallExpression,
    ArgumentedElement,
    AccessExpression,
    model::RecordAccessExpression,
    model::ArrayAccessExpression,
    model::SelectExpression,
    model::FunctionAccessExpression,
    model::LessEqualExpression,
    model::LessExpression,
    BooleanLiteralExpression,
    model::FalseExpression,
    model::TrueExpression,
    BooleanExpression,
    ArithmeticLiteralExpression,
    model::RationalLiteralExpression,
    model::DecimalLiteralExpression,
    model::IntegerLiteralExpression,
    ArithmeticExpression,
    LiteralExpression,
    model::FieldAssignment,
    model::RecordLiteralExpression,
    BinaryExpression,
    model::ModExpression,
    model::ImplyExpression,
    model::DivExpression,
    model::SubtractExpression,
    model::EquivalenceExpression,
    model::ComparisonExpression,
    model::DivideExpression,
    MultiaryExpression,
    model::XorExpression,
    model::MultiplyExpression,
    model::OrExpression,
    model::AndExpression,
    model::AddExpression,
    EnumerableExpression,
    model::IntegerRangeLiteralExpression,
    model::ArrayLiteralExpression,
    Expression,
    model::EnumerableExpression,
    model::UnaryExpression,
    model::IfThenElseExpression,
    model::LiteralExpression,
    model::AccessExpression,
    model::NullaryExpression,
    ConstraintDefinition,
    model::ConstraintDefinition,
    UnaryExpression,
    model::UnaryMinusExpression,
    model::UnaryPlusExpression,
    model::NotExpression,
    ElseExpression,
    model::DefaultExpression,
    NullaryExpression,
    model::ArithmeticLiteralExpression,
    model::EnumerationLiteralExpression,
    model::BooleanLiteralExpression,
    model::ReferenceExpression,
    model::OpaqueExpression,
    LogicExpression,
    model::ElseExpression,
    model::PredicateExpression,
    model::BooleanExpression,
    model::LogicExpression,
    model::ArithmeticExpression,
    model::MultiaryExpression,
    model::BinaryExpression,
    CompositeTypeDefinition,
    model::FunctionTypeDefinition,
    model::RecordTypeDefinition,
    EnumerableTypeDefinition,
    model::ArrayTypeDefinition,
    model::IntegerRangeTypeDefinition,
    model::EnumerationTypeDefinition,
    model::EnumerableTypeDefinition,
    Declaration,
    model::ValueDeclaration,
    model::Type,
    model::BasicConstraintDefinition,
    model::TypeDeclaration,
    ParametricElement,
    model::FunctionDeclaration,
    model::QuantifierExpression,
    NamedElement,
    model::InitializableElement,
    model::Declaration,
    model::EnumerationLiteralDefinition,
    model::ExpressionPackage,
    NumericalTypeDefinition,
    model::DecimalTypeDefinition,
    model::RationalTypeDefinition,
    model::SubrangeTypeDefinition,
    model::IntegerTypeDefinition,
    TypeDefinition,
    model::BooleanTypeDefinition,
    model::VoidTypeDefinition,
    model::CompositeTypeDefinition,
    model::NumericalTypeDefinition,
    Type,
    model::TypeDefinition,
    model::TypeReference,
    FunctionDeclaration,
    InitializableElement,
    model::LambdaDeclaration,
    ValueDeclaration,
    model::FieldDeclaration,
    model::ConstantDeclaration,
    model::VariableDeclaration,
    model::Comment,
    model::CommentableElement,
    model::NamedElement,
    model::Expression,
    model::ArgumentedElement,
    model::ParameterDeclaration,
    model::ParametricElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_comparisonexpression_is_not_abstract():
    assert not inspect.isabstract(ComparisonExpression)


def test_comparisonexpression_constructor_exists():
    assert callable(ComparisonExpression.__init__)


def test_comparisonexpression_constructor_args():
    sig = inspect.signature(ComparisonExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::greaterequalexpression_is_not_abstract():
    assert not inspect.isabstract(model::GreaterEqualExpression)


def test_model::greaterequalexpression_constructor_exists():
    assert callable(model::GreaterEqualExpression.__init__)


def test_model::greaterequalexpression_constructor_args():
    sig = inspect.signature(model::GreaterEqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::greaterexpression_is_not_abstract():
    assert not inspect.isabstract(model::GreaterExpression)


def test_model::greaterexpression_constructor_exists():
    assert callable(model::GreaterExpression.__init__)


def test_model::greaterexpression_constructor_args():
    sig = inspect.signature(model::GreaterExpression.__init__)
    params = list(sig.parameters.keys())



def test_equivalenceexpression_is_not_abstract():
    assert not inspect.isabstract(EquivalenceExpression)


def test_equivalenceexpression_constructor_exists():
    assert callable(EquivalenceExpression.__init__)


def test_equivalenceexpression_constructor_args():
    sig = inspect.signature(EquivalenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::inequalityexpression_is_not_abstract():
    assert not inspect.isabstract(model::InequalityExpression)


def test_model::inequalityexpression_constructor_exists():
    assert callable(model::InequalityExpression.__init__)


def test_model::inequalityexpression_constructor_args():
    sig = inspect.signature(model::InequalityExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::equalityexpression_is_not_abstract():
    assert not inspect.isabstract(model::EqualityExpression)


def test_model::equalityexpression_constructor_exists():
    assert callable(model::EqualityExpression.__init__)


def test_model::equalityexpression_constructor_args():
    sig = inspect.signature(model::EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_predicateexpression_is_not_abstract():
    assert not inspect.isabstract(PredicateExpression)


def test_predicateexpression_constructor_exists():
    assert callable(PredicateExpression.__init__)


def test_predicateexpression_constructor_args():
    sig = inspect.signature(PredicateExpression.__init__)
    params = list(sig.parameters.keys())



def test_quantifierexpression_is_not_abstract():
    assert not inspect.isabstract(QuantifierExpression)


def test_quantifierexpression_constructor_exists():
    assert callable(QuantifierExpression.__init__)


def test_quantifierexpression_constructor_args():
    sig = inspect.signature(QuantifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::existsexpression_is_not_abstract():
    assert not inspect.isabstract(model::ExistsExpression)


def test_model::existsexpression_constructor_exists():
    assert callable(model::ExistsExpression.__init__)


def test_model::existsexpression_constructor_args():
    sig = inspect.signature(model::ExistsExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::forallexpression_is_not_abstract():
    assert not inspect.isabstract(model::ForallExpression)


def test_model::forallexpression_constructor_exists():
    assert callable(model::ForallExpression.__init__)


def test_model::forallexpression_constructor_args():
    sig = inspect.signature(model::ForallExpression.__init__)
    params = list(sig.parameters.keys())



def test_argumentedelement_is_not_abstract():
    assert not inspect.isabstract(ArgumentedElement)


def test_argumentedelement_constructor_exists():
    assert callable(ArgumentedElement.__init__)


def test_argumentedelement_constructor_args():
    sig = inspect.signature(ArgumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_accessexpression_is_not_abstract():
    assert not inspect.isabstract(AccessExpression)


def test_accessexpression_constructor_exists():
    assert callable(AccessExpression.__init__)


def test_accessexpression_constructor_args():
    sig = inspect.signature(AccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::recordaccessexpression_is_not_abstract():
    assert not inspect.isabstract(model::RecordAccessExpression)


def test_model::recordaccessexpression_constructor_exists():
    assert callable(model::RecordAccessExpression.__init__)


def test_model::recordaccessexpression_constructor_args():
    sig = inspect.signature(model::RecordAccessExpression.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_model::recordaccessexpression_has_field():
    assert hasattr(model::RecordAccessExpression, "field")
    descriptor = None
    for klass in model::RecordAccessExpression.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_model::arrayaccessexpression_is_not_abstract():
    assert not inspect.isabstract(model::ArrayAccessExpression)


def test_model::arrayaccessexpression_constructor_exists():
    assert callable(model::ArrayAccessExpression.__init__)


def test_model::arrayaccessexpression_constructor_args():
    sig = inspect.signature(model::ArrayAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::selectexpression_is_not_abstract():
    assert not inspect.isabstract(model::SelectExpression)


def test_model::selectexpression_constructor_exists():
    assert callable(model::SelectExpression.__init__)


def test_model::selectexpression_constructor_args():
    sig = inspect.signature(model::SelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::functionaccessexpression_is_not_abstract():
    assert not inspect.isabstract(model::FunctionAccessExpression)


def test_model::functionaccessexpression_constructor_exists():
    assert callable(model::FunctionAccessExpression.__init__)


def test_model::functionaccessexpression_constructor_args():
    sig = inspect.signature(model::FunctionAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::lessequalexpression_is_not_abstract():
    assert not inspect.isabstract(model::LessEqualExpression)


def test_model::lessequalexpression_constructor_exists():
    assert callable(model::LessEqualExpression.__init__)


def test_model::lessequalexpression_constructor_args():
    sig = inspect.signature(model::LessEqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::lessexpression_is_not_abstract():
    assert not inspect.isabstract(model::LessExpression)


def test_model::lessexpression_constructor_exists():
    assert callable(model::LessExpression.__init__)


def test_model::lessexpression_constructor_args():
    sig = inspect.signature(model::LessExpression.__init__)
    params = list(sig.parameters.keys())



def test_booleanliteralexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanLiteralExpression)


def test_booleanliteralexpression_constructor_exists():
    assert callable(BooleanLiteralExpression.__init__)


def test_booleanliteralexpression_constructor_args():
    sig = inspect.signature(BooleanLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::falseexpression_is_not_abstract():
    assert not inspect.isabstract(model::FalseExpression)


def test_model::falseexpression_constructor_exists():
    assert callable(model::FalseExpression.__init__)


def test_model::falseexpression_constructor_args():
    sig = inspect.signature(model::FalseExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::trueexpression_is_not_abstract():
    assert not inspect.isabstract(model::TrueExpression)


def test_model::trueexpression_constructor_exists():
    assert callable(model::TrueExpression.__init__)


def test_model::trueexpression_constructor_args():
    sig = inspect.signature(model::TrueExpression.__init__)
    params = list(sig.parameters.keys())



def test_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticliteralexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticLiteralExpression)


def test_arithmeticliteralexpression_constructor_exists():
    assert callable(ArithmeticLiteralExpression.__init__)


def test_arithmeticliteralexpression_constructor_args():
    sig = inspect.signature(ArithmeticLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::rationalliteralexpression_is_not_abstract():
    assert not inspect.isabstract(model::RationalLiteralExpression)


def test_model::rationalliteralexpression_constructor_exists():
    assert callable(model::RationalLiteralExpression.__init__)


def test_model::rationalliteralexpression_constructor_args():
    sig = inspect.signature(model::RationalLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "denominator" in params, "Missing parameter 'denominator'"
    assert "numerator" in params, "Missing parameter 'numerator'"

def test_model::rationalliteralexpression_has_denominator():
    assert hasattr(model::RationalLiteralExpression, "denominator")
    descriptor = None
    for klass in model::RationalLiteralExpression.__mro__:
        if "denominator" in klass.__dict__:
            descriptor = klass.__dict__["denominator"]
            break
    assert isinstance(descriptor, property)

def test_model::rationalliteralexpression_has_numerator():
    assert hasattr(model::RationalLiteralExpression, "numerator")
    descriptor = None
    for klass in model::RationalLiteralExpression.__mro__:
        if "numerator" in klass.__dict__:
            descriptor = klass.__dict__["numerator"]
            break
    assert isinstance(descriptor, property)



def test_model::decimalliteralexpression_is_not_abstract():
    assert not inspect.isabstract(model::DecimalLiteralExpression)


def test_model::decimalliteralexpression_constructor_exists():
    assert callable(model::DecimalLiteralExpression.__init__)


def test_model::decimalliteralexpression_constructor_args():
    sig = inspect.signature(model::DecimalLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model::decimalliteralexpression_has_value():
    assert hasattr(model::DecimalLiteralExpression, "value")
    descriptor = None
    for klass in model::DecimalLiteralExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model::integerliteralexpression_is_not_abstract():
    assert not inspect.isabstract(model::IntegerLiteralExpression)


def test_model::integerliteralexpression_constructor_exists():
    assert callable(model::IntegerLiteralExpression.__init__)


def test_model::integerliteralexpression_constructor_args():
    sig = inspect.signature(model::IntegerLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model::integerliteralexpression_has_value():
    assert hasattr(model::IntegerLiteralExpression, "value")
    descriptor = None
    for klass in model::IntegerLiteralExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticExpression)


def test_arithmeticexpression_constructor_exists():
    assert callable(ArithmeticExpression.__init__)


def test_arithmeticexpression_constructor_args():
    sig = inspect.signature(ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_literalexpression_is_not_abstract():
    assert not inspect.isabstract(LiteralExpression)


def test_literalexpression_constructor_exists():
    assert callable(LiteralExpression.__init__)


def test_literalexpression_constructor_args():
    sig = inspect.signature(LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::fieldassignment_is_not_abstract():
    assert not inspect.isabstract(model::FieldAssignment)


def test_model::fieldassignment_constructor_exists():
    assert callable(model::FieldAssignment.__init__)


def test_model::fieldassignment_constructor_args():
    sig = inspect.signature(model::FieldAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"

def test_model::fieldassignment_has_reference():
    assert hasattr(model::FieldAssignment, "reference")
    descriptor = None
    for klass in model::FieldAssignment.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)



def test_model::recordliteralexpression_is_not_abstract():
    assert not inspect.isabstract(model::RecordLiteralExpression)


def test_model::recordliteralexpression_constructor_exists():
    assert callable(model::RecordLiteralExpression.__init__)


def test_model::recordliteralexpression_constructor_args():
    sig = inspect.signature(model::RecordLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::modexpression_is_not_abstract():
    assert not inspect.isabstract(model::ModExpression)


def test_model::modexpression_constructor_exists():
    assert callable(model::ModExpression.__init__)


def test_model::modexpression_constructor_args():
    sig = inspect.signature(model::ModExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::implyexpression_is_not_abstract():
    assert not inspect.isabstract(model::ImplyExpression)


def test_model::implyexpression_constructor_exists():
    assert callable(model::ImplyExpression.__init__)


def test_model::implyexpression_constructor_args():
    sig = inspect.signature(model::ImplyExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::divexpression_is_not_abstract():
    assert not inspect.isabstract(model::DivExpression)


def test_model::divexpression_constructor_exists():
    assert callable(model::DivExpression.__init__)


def test_model::divexpression_constructor_args():
    sig = inspect.signature(model::DivExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::subtractexpression_is_not_abstract():
    assert not inspect.isabstract(model::SubtractExpression)


def test_model::subtractexpression_constructor_exists():
    assert callable(model::SubtractExpression.__init__)


def test_model::subtractexpression_constructor_args():
    sig = inspect.signature(model::SubtractExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::equivalenceexpression_is_not_abstract():
    assert not inspect.isabstract(model::EquivalenceExpression)


def test_model::equivalenceexpression_constructor_exists():
    assert callable(model::EquivalenceExpression.__init__)


def test_model::equivalenceexpression_constructor_args():
    sig = inspect.signature(model::EquivalenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::comparisonexpression_is_not_abstract():
    assert not inspect.isabstract(model::ComparisonExpression)


def test_model::comparisonexpression_constructor_exists():
    assert callable(model::ComparisonExpression.__init__)


def test_model::comparisonexpression_constructor_args():
    sig = inspect.signature(model::ComparisonExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::divideexpression_is_not_abstract():
    assert not inspect.isabstract(model::DivideExpression)


def test_model::divideexpression_constructor_exists():
    assert callable(model::DivideExpression.__init__)


def test_model::divideexpression_constructor_args():
    sig = inspect.signature(model::DivideExpression.__init__)
    params = list(sig.parameters.keys())



def test_multiaryexpression_is_not_abstract():
    assert not inspect.isabstract(MultiaryExpression)


def test_multiaryexpression_constructor_exists():
    assert callable(MultiaryExpression.__init__)


def test_multiaryexpression_constructor_args():
    sig = inspect.signature(MultiaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::xorexpression_is_not_abstract():
    assert not inspect.isabstract(model::XorExpression)


def test_model::xorexpression_constructor_exists():
    assert callable(model::XorExpression.__init__)


def test_model::xorexpression_constructor_args():
    sig = inspect.signature(model::XorExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::multiplyexpression_is_not_abstract():
    assert not inspect.isabstract(model::MultiplyExpression)


def test_model::multiplyexpression_constructor_exists():
    assert callable(model::MultiplyExpression.__init__)


def test_model::multiplyexpression_constructor_args():
    sig = inspect.signature(model::MultiplyExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::orexpression_is_not_abstract():
    assert not inspect.isabstract(model::OrExpression)


def test_model::orexpression_constructor_exists():
    assert callable(model::OrExpression.__init__)


def test_model::orexpression_constructor_args():
    sig = inspect.signature(model::OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::andexpression_is_not_abstract():
    assert not inspect.isabstract(model::AndExpression)


def test_model::andexpression_constructor_exists():
    assert callable(model::AndExpression.__init__)


def test_model::andexpression_constructor_args():
    sig = inspect.signature(model::AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::addexpression_is_not_abstract():
    assert not inspect.isabstract(model::AddExpression)


def test_model::addexpression_constructor_exists():
    assert callable(model::AddExpression.__init__)


def test_model::addexpression_constructor_args():
    sig = inspect.signature(model::AddExpression.__init__)
    params = list(sig.parameters.keys())



def test_enumerableexpression_is_not_abstract():
    assert not inspect.isabstract(EnumerableExpression)


def test_enumerableexpression_constructor_exists():
    assert callable(EnumerableExpression.__init__)


def test_enumerableexpression_constructor_args():
    sig = inspect.signature(EnumerableExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::integerrangeliteralexpression_is_not_abstract():
    assert not inspect.isabstract(model::IntegerRangeLiteralExpression)


def test_model::integerrangeliteralexpression_constructor_exists():
    assert callable(model::IntegerRangeLiteralExpression.__init__)


def test_model::integerrangeliteralexpression_constructor_args():
    sig = inspect.signature(model::IntegerRangeLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "leftInclusive" in params, "Missing parameter 'leftInclusive'"
    assert "rightInclusive" in params, "Missing parameter 'rightInclusive'"

def test_model::integerrangeliteralexpression_has_leftInclusive():
    assert hasattr(model::IntegerRangeLiteralExpression, "leftInclusive")
    descriptor = None
    for klass in model::IntegerRangeLiteralExpression.__mro__:
        if "leftInclusive" in klass.__dict__:
            descriptor = klass.__dict__["leftInclusive"]
            break
    assert isinstance(descriptor, property)

def test_model::integerrangeliteralexpression_has_rightInclusive():
    assert hasattr(model::IntegerRangeLiteralExpression, "rightInclusive")
    descriptor = None
    for klass in model::IntegerRangeLiteralExpression.__mro__:
        if "rightInclusive" in klass.__dict__:
            descriptor = klass.__dict__["rightInclusive"]
            break
    assert isinstance(descriptor, property)



def test_model::arrayliteralexpression_is_not_abstract():
    assert not inspect.isabstract(model::ArrayLiteralExpression)


def test_model::arrayliteralexpression_constructor_exists():
    assert callable(model::ArrayLiteralExpression.__init__)


def test_model::arrayliteralexpression_constructor_args():
    sig = inspect.signature(model::ArrayLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_model::enumerableexpression_is_not_abstract():
    assert not inspect.isabstract(model::EnumerableExpression)


def test_model::enumerableexpression_constructor_exists():
    assert callable(model::EnumerableExpression.__init__)


def test_model::enumerableexpression_constructor_args():
    sig = inspect.signature(model::EnumerableExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(model::UnaryExpression)


def test_model::unaryexpression_constructor_exists():
    assert callable(model::UnaryExpression.__init__)


def test_model::unaryexpression_constructor_args():
    sig = inspect.signature(model::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::ifthenelseexpression_is_not_abstract():
    assert not inspect.isabstract(model::IfThenElseExpression)


def test_model::ifthenelseexpression_constructor_exists():
    assert callable(model::IfThenElseExpression.__init__)


def test_model::ifthenelseexpression_constructor_args():
    sig = inspect.signature(model::IfThenElseExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::literalexpression_is_not_abstract():
    assert not inspect.isabstract(model::LiteralExpression)


def test_model::literalexpression_constructor_exists():
    assert callable(model::LiteralExpression.__init__)


def test_model::literalexpression_constructor_args():
    sig = inspect.signature(model::LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::accessexpression_is_not_abstract():
    assert not inspect.isabstract(model::AccessExpression)


def test_model::accessexpression_constructor_exists():
    assert callable(model::AccessExpression.__init__)


def test_model::accessexpression_constructor_args():
    sig = inspect.signature(model::AccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::nullaryexpression_is_not_abstract():
    assert not inspect.isabstract(model::NullaryExpression)


def test_model::nullaryexpression_constructor_exists():
    assert callable(model::NullaryExpression.__init__)


def test_model::nullaryexpression_constructor_args():
    sig = inspect.signature(model::NullaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_constraintdefinition_is_not_abstract():
    assert not inspect.isabstract(ConstraintDefinition)


def test_constraintdefinition_constructor_exists():
    assert callable(ConstraintDefinition.__init__)


def test_constraintdefinition_constructor_args():
    sig = inspect.signature(ConstraintDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model::constraintdefinition_is_not_abstract():
    assert not inspect.isabstract(model::ConstraintDefinition)


def test_model::constraintdefinition_constructor_exists():
    assert callable(model::ConstraintDefinition.__init__)


def test_model::constraintdefinition_constructor_args():
    sig = inspect.signature(model::ConstraintDefinition.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::unaryminusexpression_is_not_abstract():
    assert not inspect.isabstract(model::UnaryMinusExpression)


def test_model::unaryminusexpression_constructor_exists():
    assert callable(model::UnaryMinusExpression.__init__)


def test_model::unaryminusexpression_constructor_args():
    sig = inspect.signature(model::UnaryMinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::unaryplusexpression_is_not_abstract():
    assert not inspect.isabstract(model::UnaryPlusExpression)


def test_model::unaryplusexpression_constructor_exists():
    assert callable(model::UnaryPlusExpression.__init__)


def test_model::unaryplusexpression_constructor_args():
    sig = inspect.signature(model::UnaryPlusExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::notexpression_is_not_abstract():
    assert not inspect.isabstract(model::NotExpression)


def test_model::notexpression_constructor_exists():
    assert callable(model::NotExpression.__init__)


def test_model::notexpression_constructor_args():
    sig = inspect.signature(model::NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_elseexpression_is_not_abstract():
    assert not inspect.isabstract(ElseExpression)


def test_elseexpression_constructor_exists():
    assert callable(ElseExpression.__init__)


def test_elseexpression_constructor_args():
    sig = inspect.signature(ElseExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::defaultexpression_is_not_abstract():
    assert not inspect.isabstract(model::DefaultExpression)


def test_model::defaultexpression_constructor_exists():
    assert callable(model::DefaultExpression.__init__)


def test_model::defaultexpression_constructor_args():
    sig = inspect.signature(model::DefaultExpression.__init__)
    params = list(sig.parameters.keys())



def test_nullaryexpression_is_not_abstract():
    assert not inspect.isabstract(NullaryExpression)


def test_nullaryexpression_constructor_exists():
    assert callable(NullaryExpression.__init__)


def test_nullaryexpression_constructor_args():
    sig = inspect.signature(NullaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::arithmeticliteralexpression_is_not_abstract():
    assert not inspect.isabstract(model::ArithmeticLiteralExpression)


def test_model::arithmeticliteralexpression_constructor_exists():
    assert callable(model::ArithmeticLiteralExpression.__init__)


def test_model::arithmeticliteralexpression_constructor_args():
    sig = inspect.signature(model::ArithmeticLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::enumerationliteralexpression_is_not_abstract():
    assert not inspect.isabstract(model::EnumerationLiteralExpression)


def test_model::enumerationliteralexpression_constructor_exists():
    assert callable(model::EnumerationLiteralExpression.__init__)


def test_model::enumerationliteralexpression_constructor_args():
    sig = inspect.signature(model::EnumerationLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::booleanliteralexpression_is_not_abstract():
    assert not inspect.isabstract(model::BooleanLiteralExpression)


def test_model::booleanliteralexpression_constructor_exists():
    assert callable(model::BooleanLiteralExpression.__init__)


def test_model::booleanliteralexpression_constructor_args():
    sig = inspect.signature(model::BooleanLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::referenceexpression_is_not_abstract():
    assert not inspect.isabstract(model::ReferenceExpression)


def test_model::referenceexpression_constructor_exists():
    assert callable(model::ReferenceExpression.__init__)


def test_model::referenceexpression_constructor_args():
    sig = inspect.signature(model::ReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(model::OpaqueExpression)


def test_model::opaqueexpression_constructor_exists():
    assert callable(model::OpaqueExpression.__init__)


def test_model::opaqueexpression_constructor_args():
    sig = inspect.signature(model::OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_model::opaqueexpression_has_expression():
    assert hasattr(model::OpaqueExpression, "expression")
    descriptor = None
    for klass in model::OpaqueExpression.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_logicexpression_is_not_abstract():
    assert not inspect.isabstract(LogicExpression)


def test_logicexpression_constructor_exists():
    assert callable(LogicExpression.__init__)


def test_logicexpression_constructor_args():
    sig = inspect.signature(LogicExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::elseexpression_is_not_abstract():
    assert not inspect.isabstract(model::ElseExpression)


def test_model::elseexpression_constructor_exists():
    assert callable(model::ElseExpression.__init__)


def test_model::elseexpression_constructor_args():
    sig = inspect.signature(model::ElseExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::predicateexpression_is_not_abstract():
    assert not inspect.isabstract(model::PredicateExpression)


def test_model::predicateexpression_constructor_exists():
    assert callable(model::PredicateExpression.__init__)


def test_model::predicateexpression_constructor_args():
    sig = inspect.signature(model::PredicateExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(model::BooleanExpression)


def test_model::booleanexpression_constructor_exists():
    assert callable(model::BooleanExpression.__init__)


def test_model::booleanexpression_constructor_args():
    sig = inspect.signature(model::BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::logicexpression_is_not_abstract():
    assert not inspect.isabstract(model::LogicExpression)


def test_model::logicexpression_constructor_exists():
    assert callable(model::LogicExpression.__init__)


def test_model::logicexpression_constructor_args():
    sig = inspect.signature(model::LogicExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(model::ArithmeticExpression)


def test_model::arithmeticexpression_constructor_exists():
    assert callable(model::ArithmeticExpression.__init__)


def test_model::arithmeticexpression_constructor_args():
    sig = inspect.signature(model::ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::multiaryexpression_is_not_abstract():
    assert not inspect.isabstract(model::MultiaryExpression)


def test_model::multiaryexpression_constructor_exists():
    assert callable(model::MultiaryExpression.__init__)


def test_model::multiaryexpression_constructor_args():
    sig = inspect.signature(model::MultiaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(model::BinaryExpression)


def test_model::binaryexpression_constructor_exists():
    assert callable(model::BinaryExpression.__init__)


def test_model::binaryexpression_constructor_args():
    sig = inspect.signature(model::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_compositetypedefinition_is_not_abstract():
    assert not inspect.isabstract(CompositeTypeDefinition)


def test_compositetypedefinition_constructor_exists():
    assert callable(CompositeTypeDefinition.__init__)


def test_compositetypedefinition_constructor_args():
    sig = inspect.signature(CompositeTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model::functiontypedefinition_is_not_abstract():
    assert not inspect.isabstract(model::FunctionTypeDefinition)


def test_model::functiontypedefinition_constructor_exists():
    assert callable(model::FunctionTypeDefinition.__init__)


def test_model::functiontypedefinition_constructor_args():
    sig = inspect.signature(model::FunctionTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model::recordtypedefinition_is_not_abstract():
    assert not inspect.isabstract(model::RecordTypeDefinition)


def test_model::recordtypedefinition_constructor_exists():
    assert callable(model::RecordTypeDefinition.__init__)


def test_model::recordtypedefinition_constructor_args():
    sig = inspect.signature(model::RecordTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_enumerabletypedefinition_is_not_abstract():
    assert not inspect.isabstract(EnumerableTypeDefinition)


def test_enumerabletypedefinition_constructor_exists():
    assert callable(EnumerableTypeDefinition.__init__)


def test_enumerabletypedefinition_constructor_args():
    sig = inspect.signature(EnumerableTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model::arraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(model::ArrayTypeDefinition)


def test_model::arraytypedefinition_constructor_exists():
    assert callable(model::ArrayTypeDefinition.__init__)


def test_model::arraytypedefinition_constructor_args():
    sig = inspect.signature(model::ArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model::integerrangetypedefinition_is_not_abstract():
    assert not inspect.isabstract(model::IntegerRangeTypeDefinition)


def test_model::integerrangetypedefinition_constructor_exists():
    assert callable(model::IntegerRangeTypeDefinition.__init__)


def test_model::integerrangetypedefinition_constructor_args():
    sig = inspect.signature(model::IntegerRangeTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model::enumerationtypedefinition_is_not_abstract():
    assert not inspect.isabstract(model::EnumerationTypeDefinition)


def test_model::enumerationtypedefinition_constructor_exists():
    assert callable(model::EnumerationTypeDefinition.__init__)


def test_model::enumerationtypedefinition_constructor_args():
    sig = inspect.signature(model::EnumerationTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model::enumerabletypedefinition_is_not_abstract():
    assert not inspect.isabstract(model::EnumerableTypeDefinition)


def test_model::enumerabletypedefinition_constructor_exists():
    assert callable(model::EnumerableTypeDefinition.__init__)


def test_model::enumerabletypedefinition_constructor_args():
    sig = inspect.signature(model::EnumerableTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_model::valuedeclaration_is_not_abstract():
    assert not inspect.isabstract(model::ValueDeclaration)


def test_model::valuedeclaration_constructor_exists():
    assert callable(model::ValueDeclaration.__init__)


def test_model::valuedeclaration_constructor_args():
    sig = inspect.signature(model::ValueDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model::type_is_not_abstract():
    assert not inspect.isabstract(model::Type)


def test_model::type_constructor_exists():
    assert callable(model::Type.__init__)


def test_model::type_constructor_args():
    sig = inspect.signature(model::Type.__init__)
    params = list(sig.parameters.keys())



def test_model::basicconstraintdefinition_is_not_abstract():
    assert not inspect.isabstract(model::BasicConstraintDefinition)


def test_model::basicconstraintdefinition_constructor_exists():
    assert callable(model::BasicConstraintDefinition.__init__)


def test_model::basicconstraintdefinition_constructor_args():
    sig = inspect.signature(model::BasicConstraintDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(model::TypeDeclaration)


def test_model::typedeclaration_constructor_exists():
    assert callable(model::TypeDeclaration.__init__)


def test_model::typedeclaration_constructor_args():
    sig = inspect.signature(model::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_parametricelement_is_not_abstract():
    assert not inspect.isabstract(ParametricElement)


def test_parametricelement_constructor_exists():
    assert callable(ParametricElement.__init__)


def test_parametricelement_constructor_args():
    sig = inspect.signature(ParametricElement.__init__)
    params = list(sig.parameters.keys())



def test_model::functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(model::FunctionDeclaration)


def test_model::functiondeclaration_constructor_exists():
    assert callable(model::FunctionDeclaration.__init__)


def test_model::functiondeclaration_constructor_args():
    sig = inspect.signature(model::FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model::quantifierexpression_is_not_abstract():
    assert not inspect.isabstract(model::QuantifierExpression)


def test_model::quantifierexpression_constructor_exists():
    assert callable(model::QuantifierExpression.__init__)


def test_model::quantifierexpression_constructor_args():
    sig = inspect.signature(model::QuantifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_model::initializableelement_is_not_abstract():
    assert not inspect.isabstract(model::InitializableElement)


def test_model::initializableelement_constructor_exists():
    assert callable(model::InitializableElement.__init__)


def test_model::initializableelement_constructor_args():
    sig = inspect.signature(model::InitializableElement.__init__)
    params = list(sig.parameters.keys())



def test_model::declaration_is_not_abstract():
    assert not inspect.isabstract(model::Declaration)


def test_model::declaration_constructor_exists():
    assert callable(model::Declaration.__init__)


def test_model::declaration_constructor_args():
    sig = inspect.signature(model::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_model::enumerationliteraldefinition_is_not_abstract():
    assert not inspect.isabstract(model::EnumerationLiteralDefinition)


def test_model::enumerationliteraldefinition_constructor_exists():
    assert callable(model::EnumerationLiteralDefinition.__init__)


def test_model::enumerationliteraldefinition_constructor_args():
    sig = inspect.signature(model::EnumerationLiteralDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model::expressionpackage_is_not_abstract():
    assert not inspect.isabstract(model::ExpressionPackage)


def test_model::expressionpackage_constructor_exists():
    assert callable(model::ExpressionPackage.__init__)


def test_model::expressionpackage_constructor_args():
    sig = inspect.signature(model::ExpressionPackage.__init__)
    params = list(sig.parameters.keys())



def test_numericaltypedefinition_is_not_abstract():
    assert not inspect.isabstract(NumericalTypeDefinition)


def test_numericaltypedefinition_constructor_exists():
    assert callable(NumericalTypeDefinition.__init__)


def test_numericaltypedefinition_constructor_args():
    sig = inspect.signature(NumericalTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model::decimaltypedefinition_is_not_abstract():
    assert not inspect.isabstract(model::DecimalTypeDefinition)


def test_model::decimaltypedefinition_constructor_exists():
    assert callable(model::DecimalTypeDefinition.__init__)


def test_model::decimaltypedefinition_constructor_args():
    sig = inspect.signature(model::DecimalTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model::rationaltypedefinition_is_not_abstract():
    assert not inspect.isabstract(model::RationalTypeDefinition)


def test_model::rationaltypedefinition_constructor_exists():
    assert callable(model::RationalTypeDefinition.__init__)


def test_model::rationaltypedefinition_constructor_args():
    sig = inspect.signature(model::RationalTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model::subrangetypedefinition_is_not_abstract():
    assert not inspect.isabstract(model::SubrangeTypeDefinition)


def test_model::subrangetypedefinition_constructor_exists():
    assert callable(model::SubrangeTypeDefinition.__init__)


def test_model::subrangetypedefinition_constructor_args():
    sig = inspect.signature(model::SubrangeTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model::integertypedefinition_is_not_abstract():
    assert not inspect.isabstract(model::IntegerTypeDefinition)


def test_model::integertypedefinition_constructor_exists():
    assert callable(model::IntegerTypeDefinition.__init__)


def test_model::integertypedefinition_constructor_args():
    sig = inspect.signature(model::IntegerTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model::booleantypedefinition_is_not_abstract():
    assert not inspect.isabstract(model::BooleanTypeDefinition)


def test_model::booleantypedefinition_constructor_exists():
    assert callable(model::BooleanTypeDefinition.__init__)


def test_model::booleantypedefinition_constructor_args():
    sig = inspect.signature(model::BooleanTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model::voidtypedefinition_is_not_abstract():
    assert not inspect.isabstract(model::VoidTypeDefinition)


def test_model::voidtypedefinition_constructor_exists():
    assert callable(model::VoidTypeDefinition.__init__)


def test_model::voidtypedefinition_constructor_args():
    sig = inspect.signature(model::VoidTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model::compositetypedefinition_is_not_abstract():
    assert not inspect.isabstract(model::CompositeTypeDefinition)


def test_model::compositetypedefinition_constructor_exists():
    assert callable(model::CompositeTypeDefinition.__init__)


def test_model::compositetypedefinition_constructor_args():
    sig = inspect.signature(model::CompositeTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model::numericaltypedefinition_is_not_abstract():
    assert not inspect.isabstract(model::NumericalTypeDefinition)


def test_model::numericaltypedefinition_constructor_exists():
    assert callable(model::NumericalTypeDefinition.__init__)


def test_model::numericaltypedefinition_constructor_args():
    sig = inspect.signature(model::NumericalTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_model::typedefinition_is_not_abstract():
    assert not inspect.isabstract(model::TypeDefinition)


def test_model::typedefinition_constructor_exists():
    assert callable(model::TypeDefinition.__init__)


def test_model::typedefinition_constructor_args():
    sig = inspect.signature(model::TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model::typereference_is_not_abstract():
    assert not inspect.isabstract(model::TypeReference)


def test_model::typereference_constructor_exists():
    assert callable(model::TypeReference.__init__)


def test_model::typereference_constructor_args():
    sig = inspect.signature(model::TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(FunctionDeclaration)


def test_functiondeclaration_constructor_exists():
    assert callable(FunctionDeclaration.__init__)


def test_functiondeclaration_constructor_args():
    sig = inspect.signature(FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_initializableelement_is_not_abstract():
    assert not inspect.isabstract(InitializableElement)


def test_initializableelement_constructor_exists():
    assert callable(InitializableElement.__init__)


def test_initializableelement_constructor_args():
    sig = inspect.signature(InitializableElement.__init__)
    params = list(sig.parameters.keys())



def test_model::lambdadeclaration_is_not_abstract():
    assert not inspect.isabstract(model::LambdaDeclaration)


def test_model::lambdadeclaration_constructor_exists():
    assert callable(model::LambdaDeclaration.__init__)


def test_model::lambdadeclaration_constructor_args():
    sig = inspect.signature(model::LambdaDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_valuedeclaration_is_not_abstract():
    assert not inspect.isabstract(ValueDeclaration)


def test_valuedeclaration_constructor_exists():
    assert callable(ValueDeclaration.__init__)


def test_valuedeclaration_constructor_args():
    sig = inspect.signature(ValueDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model::fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(model::FieldDeclaration)


def test_model::fielddeclaration_constructor_exists():
    assert callable(model::FieldDeclaration.__init__)


def test_model::fielddeclaration_constructor_args():
    sig = inspect.signature(model::FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model::constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(model::ConstantDeclaration)


def test_model::constantdeclaration_constructor_exists():
    assert callable(model::ConstantDeclaration.__init__)


def test_model::constantdeclaration_constructor_args():
    sig = inspect.signature(model::ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(model::VariableDeclaration)


def test_model::variabledeclaration_constructor_exists():
    assert callable(model::VariableDeclaration.__init__)


def test_model::variabledeclaration_constructor_args():
    sig = inspect.signature(model::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model::comment_is_not_abstract():
    assert not inspect.isabstract(model::Comment)


def test_model::comment_constructor_exists():
    assert callable(model::Comment.__init__)


def test_model::comment_constructor_args():
    sig = inspect.signature(model::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_model::comment_has_comment():
    assert hasattr(model::Comment, "comment")
    descriptor = None
    for klass in model::Comment.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_model::commentableelement_is_not_abstract():
    assert not inspect.isabstract(model::CommentableElement)


def test_model::commentableelement_constructor_exists():
    assert callable(model::CommentableElement.__init__)


def test_model::commentableelement_constructor_args():
    sig = inspect.signature(model::CommentableElement.__init__)
    params = list(sig.parameters.keys())



def test_model::namedelement_is_not_abstract():
    assert not inspect.isabstract(model::NamedElement)


def test_model::namedelement_constructor_exists():
    assert callable(model::NamedElement.__init__)


def test_model::namedelement_constructor_args():
    sig = inspect.signature(model::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::namedelement_has_name():
    assert hasattr(model::NamedElement, "name")
    descriptor = None
    for klass in model::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::expression_is_not_abstract():
    assert not inspect.isabstract(model::Expression)


def test_model::expression_constructor_exists():
    assert callable(model::Expression.__init__)


def test_model::expression_constructor_args():
    sig = inspect.signature(model::Expression.__init__)
    params = list(sig.parameters.keys())



def test_model::argumentedelement_is_not_abstract():
    assert not inspect.isabstract(model::ArgumentedElement)


def test_model::argumentedelement_constructor_exists():
    assert callable(model::ArgumentedElement.__init__)


def test_model::argumentedelement_constructor_args():
    sig = inspect.signature(model::ArgumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_model::parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(model::ParameterDeclaration)


def test_model::parameterdeclaration_constructor_exists():
    assert callable(model::ParameterDeclaration.__init__)


def test_model::parameterdeclaration_constructor_args():
    sig = inspect.signature(model::ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model::parametricelement_is_not_abstract():
    assert not inspect.isabstract(model::ParametricElement)


def test_model::parametricelement_constructor_exists():
    assert callable(model::ParametricElement.__init__)


def test_model::parametricelement_constructor_args():
    sig = inspect.signature(model::ParametricElement.__init__)
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
ComparisonExpression_strategy = st.builds(
    ComparisonExpression,
)
model::GreaterEqualExpression_strategy = st.builds(
    model::GreaterEqualExpression,
)
model::GreaterExpression_strategy = st.builds(
    model::GreaterExpression,
)
EquivalenceExpression_strategy = st.builds(
    EquivalenceExpression,
)
model::InequalityExpression_strategy = st.builds(
    model::InequalityExpression,
)
model::EqualityExpression_strategy = st.builds(
    model::EqualityExpression,
)
PredicateExpression_strategy = st.builds(
    PredicateExpression,
)
QuantifierExpression_strategy = st.builds(
    QuantifierExpression,
)
model::ExistsExpression_strategy = st.builds(
    model::ExistsExpression,
)
model::ForallExpression_strategy = st.builds(
    model::ForallExpression,
)
ArgumentedElement_strategy = st.builds(
    ArgumentedElement,
)
AccessExpression_strategy = st.builds(
    AccessExpression,
)
model::RecordAccessExpression_strategy = st.builds(
    model::RecordAccessExpression,
    field=
        safe_text
)
model::ArrayAccessExpression_strategy = st.builds(
    model::ArrayAccessExpression,
)
model::SelectExpression_strategy = st.builds(
    model::SelectExpression,
)
model::FunctionAccessExpression_strategy = st.builds(
    model::FunctionAccessExpression,
)
model::LessEqualExpression_strategy = st.builds(
    model::LessEqualExpression,
)
model::LessExpression_strategy = st.builds(
    model::LessExpression,
)
BooleanLiteralExpression_strategy = st.builds(
    BooleanLiteralExpression,
)
model::FalseExpression_strategy = st.builds(
    model::FalseExpression,
)
model::TrueExpression_strategy = st.builds(
    model::TrueExpression,
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
ArithmeticLiteralExpression_strategy = st.builds(
    ArithmeticLiteralExpression,
)
model::RationalLiteralExpression_strategy = st.builds(
    model::RationalLiteralExpression,
    denominator=
        safe_text,
    numerator=
        safe_text
)
model::DecimalLiteralExpression_strategy = st.builds(
    model::DecimalLiteralExpression,
    value=
        safe_text
)
model::IntegerLiteralExpression_strategy = st.builds(
    model::IntegerLiteralExpression,
    value=
        safe_text
)
ArithmeticExpression_strategy = st.builds(
    ArithmeticExpression,
)
LiteralExpression_strategy = st.builds(
    LiteralExpression,
)
model::FieldAssignment_strategy = st.builds(
    model::FieldAssignment,
    reference=
        safe_text
)
model::RecordLiteralExpression_strategy = st.builds(
    model::RecordLiteralExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
model::ModExpression_strategy = st.builds(
    model::ModExpression,
)
model::ImplyExpression_strategy = st.builds(
    model::ImplyExpression,
)
model::DivExpression_strategy = st.builds(
    model::DivExpression,
)
model::SubtractExpression_strategy = st.builds(
    model::SubtractExpression,
)
model::EquivalenceExpression_strategy = st.builds(
    model::EquivalenceExpression,
)
model::ComparisonExpression_strategy = st.builds(
    model::ComparisonExpression,
)
model::DivideExpression_strategy = st.builds(
    model::DivideExpression,
)
MultiaryExpression_strategy = st.builds(
    MultiaryExpression,
)
model::XorExpression_strategy = st.builds(
    model::XorExpression,
)
model::MultiplyExpression_strategy = st.builds(
    model::MultiplyExpression,
)
model::OrExpression_strategy = st.builds(
    model::OrExpression,
)
model::AndExpression_strategy = st.builds(
    model::AndExpression,
)
model::AddExpression_strategy = st.builds(
    model::AddExpression,
)
EnumerableExpression_strategy = st.builds(
    EnumerableExpression,
)
model::IntegerRangeLiteralExpression_strategy = st.builds(
    model::IntegerRangeLiteralExpression,
    leftInclusive=
        st.booleans(),
    rightInclusive=
        st.booleans()
)
model::ArrayLiteralExpression_strategy = st.builds(
    model::ArrayLiteralExpression,
)
Expression_strategy = st.builds(
    Expression,
)
model::EnumerableExpression_strategy = st.builds(
    model::EnumerableExpression,
)
model::UnaryExpression_strategy = st.builds(
    model::UnaryExpression,
)
model::IfThenElseExpression_strategy = st.builds(
    model::IfThenElseExpression,
)
model::LiteralExpression_strategy = st.builds(
    model::LiteralExpression,
)
model::AccessExpression_strategy = st.builds(
    model::AccessExpression,
)
model::NullaryExpression_strategy = st.builds(
    model::NullaryExpression,
)
ConstraintDefinition_strategy = st.builds(
    ConstraintDefinition,
)
model::ConstraintDefinition_strategy = st.builds(
    model::ConstraintDefinition,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
model::UnaryMinusExpression_strategy = st.builds(
    model::UnaryMinusExpression,
)
model::UnaryPlusExpression_strategy = st.builds(
    model::UnaryPlusExpression,
)
model::NotExpression_strategy = st.builds(
    model::NotExpression,
)
ElseExpression_strategy = st.builds(
    ElseExpression,
)
model::DefaultExpression_strategy = st.builds(
    model::DefaultExpression,
)
NullaryExpression_strategy = st.builds(
    NullaryExpression,
)
model::ArithmeticLiteralExpression_strategy = st.builds(
    model::ArithmeticLiteralExpression,
)
model::EnumerationLiteralExpression_strategy = st.builds(
    model::EnumerationLiteralExpression,
)
model::BooleanLiteralExpression_strategy = st.builds(
    model::BooleanLiteralExpression,
)
model::ReferenceExpression_strategy = st.builds(
    model::ReferenceExpression,
)
model::OpaqueExpression_strategy = st.builds(
    model::OpaqueExpression,
    expression=
        safe_text
)
LogicExpression_strategy = st.builds(
    LogicExpression,
)
model::ElseExpression_strategy = st.builds(
    model::ElseExpression,
)
model::PredicateExpression_strategy = st.builds(
    model::PredicateExpression,
)
model::BooleanExpression_strategy = st.builds(
    model::BooleanExpression,
)
model::LogicExpression_strategy = st.builds(
    model::LogicExpression,
)
model::ArithmeticExpression_strategy = st.builds(
    model::ArithmeticExpression,
)
model::MultiaryExpression_strategy = st.builds(
    model::MultiaryExpression,
)
model::BinaryExpression_strategy = st.builds(
    model::BinaryExpression,
)
CompositeTypeDefinition_strategy = st.builds(
    CompositeTypeDefinition,
)
model::FunctionTypeDefinition_strategy = st.builds(
    model::FunctionTypeDefinition,
)
model::RecordTypeDefinition_strategy = st.builds(
    model::RecordTypeDefinition,
)
EnumerableTypeDefinition_strategy = st.builds(
    EnumerableTypeDefinition,
)
model::ArrayTypeDefinition_strategy = st.builds(
    model::ArrayTypeDefinition,
)
model::IntegerRangeTypeDefinition_strategy = st.builds(
    model::IntegerRangeTypeDefinition,
)
model::EnumerationTypeDefinition_strategy = st.builds(
    model::EnumerationTypeDefinition,
)
model::EnumerableTypeDefinition_strategy = st.builds(
    model::EnumerableTypeDefinition,
)
Declaration_strategy = st.builds(
    Declaration,
)
model::ValueDeclaration_strategy = st.builds(
    model::ValueDeclaration,
)
model::Type_strategy = st.builds(
    model::Type,
)
model::BasicConstraintDefinition_strategy = st.builds(
    model::BasicConstraintDefinition,
)
model::TypeDeclaration_strategy = st.builds(
    model::TypeDeclaration,
)
ParametricElement_strategy = st.builds(
    ParametricElement,
)
model::FunctionDeclaration_strategy = st.builds(
    model::FunctionDeclaration,
)
model::QuantifierExpression_strategy = st.builds(
    model::QuantifierExpression,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
model::InitializableElement_strategy = st.builds(
    model::InitializableElement,
)
model::Declaration_strategy = st.builds(
    model::Declaration,
)
model::EnumerationLiteralDefinition_strategy = st.builds(
    model::EnumerationLiteralDefinition,
)
model::ExpressionPackage_strategy = st.builds(
    model::ExpressionPackage,
)
NumericalTypeDefinition_strategy = st.builds(
    NumericalTypeDefinition,
)
model::DecimalTypeDefinition_strategy = st.builds(
    model::DecimalTypeDefinition,
)
model::RationalTypeDefinition_strategy = st.builds(
    model::RationalTypeDefinition,
)
model::SubrangeTypeDefinition_strategy = st.builds(
    model::SubrangeTypeDefinition,
)
model::IntegerTypeDefinition_strategy = st.builds(
    model::IntegerTypeDefinition,
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
model::BooleanTypeDefinition_strategy = st.builds(
    model::BooleanTypeDefinition,
)
model::VoidTypeDefinition_strategy = st.builds(
    model::VoidTypeDefinition,
)
model::CompositeTypeDefinition_strategy = st.builds(
    model::CompositeTypeDefinition,
)
model::NumericalTypeDefinition_strategy = st.builds(
    model::NumericalTypeDefinition,
)
Type_strategy = st.builds(
    Type,
)
model::TypeDefinition_strategy = st.builds(
    model::TypeDefinition,
)
model::TypeReference_strategy = st.builds(
    model::TypeReference,
)
FunctionDeclaration_strategy = st.builds(
    FunctionDeclaration,
)
InitializableElement_strategy = st.builds(
    InitializableElement,
)
model::LambdaDeclaration_strategy = st.builds(
    model::LambdaDeclaration,
)
ValueDeclaration_strategy = st.builds(
    ValueDeclaration,
)
model::FieldDeclaration_strategy = st.builds(
    model::FieldDeclaration,
)
model::ConstantDeclaration_strategy = st.builds(
    model::ConstantDeclaration,
)
model::VariableDeclaration_strategy = st.builds(
    model::VariableDeclaration,
)
model::Comment_strategy = st.builds(
    model::Comment,
    comment=
        safe_text
)
model::CommentableElement_strategy = st.builds(
    model::CommentableElement,
)
model::NamedElement_strategy = st.builds(
    model::NamedElement,
    name=
        safe_text
)
model::Expression_strategy = st.builds(
    model::Expression,
)
model::ArgumentedElement_strategy = st.builds(
    model::ArgumentedElement,
)
model::ParameterDeclaration_strategy = st.builds(
    model::ParameterDeclaration,
)
model::ParametricElement_strategy = st.builds(
    model::ParametricElement,
)

@given(instance=ComparisonExpression_strategy)
@settings(max_examples=50)
def test_comparisonexpression_instantiation(instance):
    assert isinstance(instance, ComparisonExpression)

@given(instance=model::GreaterEqualExpression_strategy)
@settings(max_examples=50)
def test_model::greaterequalexpression_instantiation(instance):
    assert isinstance(instance, model::GreaterEqualExpression)

@given(instance=model::GreaterExpression_strategy)
@settings(max_examples=50)
def test_model::greaterexpression_instantiation(instance):
    assert isinstance(instance, model::GreaterExpression)

@given(instance=EquivalenceExpression_strategy)
@settings(max_examples=50)
def test_equivalenceexpression_instantiation(instance):
    assert isinstance(instance, EquivalenceExpression)

@given(instance=model::InequalityExpression_strategy)
@settings(max_examples=50)
def test_model::inequalityexpression_instantiation(instance):
    assert isinstance(instance, model::InequalityExpression)

@given(instance=model::EqualityExpression_strategy)
@settings(max_examples=50)
def test_model::equalityexpression_instantiation(instance):
    assert isinstance(instance, model::EqualityExpression)

@given(instance=PredicateExpression_strategy)
@settings(max_examples=50)
def test_predicateexpression_instantiation(instance):
    assert isinstance(instance, PredicateExpression)

@given(instance=QuantifierExpression_strategy)
@settings(max_examples=50)
def test_quantifierexpression_instantiation(instance):
    assert isinstance(instance, QuantifierExpression)

@given(instance=model::ExistsExpression_strategy)
@settings(max_examples=50)
def test_model::existsexpression_instantiation(instance):
    assert isinstance(instance, model::ExistsExpression)

@given(instance=model::ForallExpression_strategy)
@settings(max_examples=50)
def test_model::forallexpression_instantiation(instance):
    assert isinstance(instance, model::ForallExpression)

@given(instance=ArgumentedElement_strategy)
@settings(max_examples=50)
def test_argumentedelement_instantiation(instance):
    assert isinstance(instance, ArgumentedElement)

@given(instance=AccessExpression_strategy)
@settings(max_examples=50)
def test_accessexpression_instantiation(instance):
    assert isinstance(instance, AccessExpression)

@given(instance=model::RecordAccessExpression_strategy)
@settings(max_examples=50)
def test_model::recordaccessexpression_instantiation(instance):
    assert isinstance(instance, model::RecordAccessExpression)

@given(instance=model::RecordAccessExpression_strategy)
def test_model::recordaccessexpression_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=model::RecordAccessExpression_strategy)
def test_model::recordaccessexpression_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=model::ArrayAccessExpression_strategy)
@settings(max_examples=50)
def test_model::arrayaccessexpression_instantiation(instance):
    assert isinstance(instance, model::ArrayAccessExpression)

@given(instance=model::SelectExpression_strategy)
@settings(max_examples=50)
def test_model::selectexpression_instantiation(instance):
    assert isinstance(instance, model::SelectExpression)

@given(instance=model::FunctionAccessExpression_strategy)
@settings(max_examples=50)
def test_model::functionaccessexpression_instantiation(instance):
    assert isinstance(instance, model::FunctionAccessExpression)

@given(instance=model::LessEqualExpression_strategy)
@settings(max_examples=50)
def test_model::lessequalexpression_instantiation(instance):
    assert isinstance(instance, model::LessEqualExpression)

@given(instance=model::LessExpression_strategy)
@settings(max_examples=50)
def test_model::lessexpression_instantiation(instance):
    assert isinstance(instance, model::LessExpression)

@given(instance=BooleanLiteralExpression_strategy)
@settings(max_examples=50)
def test_booleanliteralexpression_instantiation(instance):
    assert isinstance(instance, BooleanLiteralExpression)

@given(instance=model::FalseExpression_strategy)
@settings(max_examples=50)
def test_model::falseexpression_instantiation(instance):
    assert isinstance(instance, model::FalseExpression)

@given(instance=model::TrueExpression_strategy)
@settings(max_examples=50)
def test_model::trueexpression_instantiation(instance):
    assert isinstance(instance, model::TrueExpression)

@given(instance=BooleanExpression_strategy)
@settings(max_examples=50)
def test_booleanexpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)

@given(instance=ArithmeticLiteralExpression_strategy)
@settings(max_examples=50)
def test_arithmeticliteralexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticLiteralExpression)

@given(instance=model::RationalLiteralExpression_strategy)
@settings(max_examples=50)
def test_model::rationalliteralexpression_instantiation(instance):
    assert isinstance(instance, model::RationalLiteralExpression)

@given(instance=model::RationalLiteralExpression_strategy)
def test_model::rationalliteralexpression_denominator_type(instance):
    assert isinstance(instance.denominator, str)


@given(instance=model::RationalLiteralExpression_strategy)
def test_model::rationalliteralexpression_denominator_setter(instance):
    original = instance.denominator
    instance.denominator = original
    assert instance.denominator == original

@given(instance=model::RationalLiteralExpression_strategy)
def test_model::rationalliteralexpression_numerator_type(instance):
    assert isinstance(instance.numerator, str)


@given(instance=model::RationalLiteralExpression_strategy)
def test_model::rationalliteralexpression_numerator_setter(instance):
    original = instance.numerator
    instance.numerator = original
    assert instance.numerator == original

@given(instance=model::DecimalLiteralExpression_strategy)
@settings(max_examples=50)
def test_model::decimalliteralexpression_instantiation(instance):
    assert isinstance(instance, model::DecimalLiteralExpression)

@given(instance=model::DecimalLiteralExpression_strategy)
def test_model::decimalliteralexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=model::DecimalLiteralExpression_strategy)
def test_model::decimalliteralexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model::IntegerLiteralExpression_strategy)
@settings(max_examples=50)
def test_model::integerliteralexpression_instantiation(instance):
    assert isinstance(instance, model::IntegerLiteralExpression)

@given(instance=model::IntegerLiteralExpression_strategy)
def test_model::integerliteralexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=model::IntegerLiteralExpression_strategy)
def test_model::integerliteralexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticExpression)

@given(instance=LiteralExpression_strategy)
@settings(max_examples=50)
def test_literalexpression_instantiation(instance):
    assert isinstance(instance, LiteralExpression)

@given(instance=model::FieldAssignment_strategy)
@settings(max_examples=50)
def test_model::fieldassignment_instantiation(instance):
    assert isinstance(instance, model::FieldAssignment)

@given(instance=model::FieldAssignment_strategy)
def test_model::fieldassignment_reference_type(instance):
    assert isinstance(instance.reference, str)


@given(instance=model::FieldAssignment_strategy)
def test_model::fieldassignment_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=model::RecordLiteralExpression_strategy)
@settings(max_examples=50)
def test_model::recordliteralexpression_instantiation(instance):
    assert isinstance(instance, model::RecordLiteralExpression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=model::ModExpression_strategy)
@settings(max_examples=50)
def test_model::modexpression_instantiation(instance):
    assert isinstance(instance, model::ModExpression)

@given(instance=model::ImplyExpression_strategy)
@settings(max_examples=50)
def test_model::implyexpression_instantiation(instance):
    assert isinstance(instance, model::ImplyExpression)

@given(instance=model::DivExpression_strategy)
@settings(max_examples=50)
def test_model::divexpression_instantiation(instance):
    assert isinstance(instance, model::DivExpression)

@given(instance=model::SubtractExpression_strategy)
@settings(max_examples=50)
def test_model::subtractexpression_instantiation(instance):
    assert isinstance(instance, model::SubtractExpression)

@given(instance=model::EquivalenceExpression_strategy)
@settings(max_examples=50)
def test_model::equivalenceexpression_instantiation(instance):
    assert isinstance(instance, model::EquivalenceExpression)

@given(instance=model::ComparisonExpression_strategy)
@settings(max_examples=50)
def test_model::comparisonexpression_instantiation(instance):
    assert isinstance(instance, model::ComparisonExpression)

@given(instance=model::DivideExpression_strategy)
@settings(max_examples=50)
def test_model::divideexpression_instantiation(instance):
    assert isinstance(instance, model::DivideExpression)

@given(instance=MultiaryExpression_strategy)
@settings(max_examples=50)
def test_multiaryexpression_instantiation(instance):
    assert isinstance(instance, MultiaryExpression)

@given(instance=model::XorExpression_strategy)
@settings(max_examples=50)
def test_model::xorexpression_instantiation(instance):
    assert isinstance(instance, model::XorExpression)

@given(instance=model::MultiplyExpression_strategy)
@settings(max_examples=50)
def test_model::multiplyexpression_instantiation(instance):
    assert isinstance(instance, model::MultiplyExpression)

@given(instance=model::OrExpression_strategy)
@settings(max_examples=50)
def test_model::orexpression_instantiation(instance):
    assert isinstance(instance, model::OrExpression)

@given(instance=model::AndExpression_strategy)
@settings(max_examples=50)
def test_model::andexpression_instantiation(instance):
    assert isinstance(instance, model::AndExpression)

@given(instance=model::AddExpression_strategy)
@settings(max_examples=50)
def test_model::addexpression_instantiation(instance):
    assert isinstance(instance, model::AddExpression)

@given(instance=EnumerableExpression_strategy)
@settings(max_examples=50)
def test_enumerableexpression_instantiation(instance):
    assert isinstance(instance, EnumerableExpression)

@given(instance=model::IntegerRangeLiteralExpression_strategy)
@settings(max_examples=50)
def test_model::integerrangeliteralexpression_instantiation(instance):
    assert isinstance(instance, model::IntegerRangeLiteralExpression)

@given(instance=model::IntegerRangeLiteralExpression_strategy)
def test_model::integerrangeliteralexpression_leftInclusive_type(instance):
    assert isinstance(instance.leftInclusive, bool)


@given(instance=model::IntegerRangeLiteralExpression_strategy)
def test_model::integerrangeliteralexpression_leftInclusive_setter(instance):
    original = instance.leftInclusive
    instance.leftInclusive = original
    assert instance.leftInclusive == original

@given(instance=model::IntegerRangeLiteralExpression_strategy)
def test_model::integerrangeliteralexpression_rightInclusive_type(instance):
    assert isinstance(instance.rightInclusive, bool)


@given(instance=model::IntegerRangeLiteralExpression_strategy)
def test_model::integerrangeliteralexpression_rightInclusive_setter(instance):
    original = instance.rightInclusive
    instance.rightInclusive = original
    assert instance.rightInclusive == original

@given(instance=model::ArrayLiteralExpression_strategy)
@settings(max_examples=50)
def test_model::arrayliteralexpression_instantiation(instance):
    assert isinstance(instance, model::ArrayLiteralExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=model::EnumerableExpression_strategy)
@settings(max_examples=50)
def test_model::enumerableexpression_instantiation(instance):
    assert isinstance(instance, model::EnumerableExpression)

@given(instance=model::UnaryExpression_strategy)
@settings(max_examples=50)
def test_model::unaryexpression_instantiation(instance):
    assert isinstance(instance, model::UnaryExpression)

@given(instance=model::IfThenElseExpression_strategy)
@settings(max_examples=50)
def test_model::ifthenelseexpression_instantiation(instance):
    assert isinstance(instance, model::IfThenElseExpression)

@given(instance=model::LiteralExpression_strategy)
@settings(max_examples=50)
def test_model::literalexpression_instantiation(instance):
    assert isinstance(instance, model::LiteralExpression)

@given(instance=model::AccessExpression_strategy)
@settings(max_examples=50)
def test_model::accessexpression_instantiation(instance):
    assert isinstance(instance, model::AccessExpression)

@given(instance=model::NullaryExpression_strategy)
@settings(max_examples=50)
def test_model::nullaryexpression_instantiation(instance):
    assert isinstance(instance, model::NullaryExpression)

@given(instance=ConstraintDefinition_strategy)
@settings(max_examples=50)
def test_constraintdefinition_instantiation(instance):
    assert isinstance(instance, ConstraintDefinition)

@given(instance=model::ConstraintDefinition_strategy)
@settings(max_examples=50)
def test_model::constraintdefinition_instantiation(instance):
    assert isinstance(instance, model::ConstraintDefinition)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=model::UnaryMinusExpression_strategy)
@settings(max_examples=50)
def test_model::unaryminusexpression_instantiation(instance):
    assert isinstance(instance, model::UnaryMinusExpression)

@given(instance=model::UnaryPlusExpression_strategy)
@settings(max_examples=50)
def test_model::unaryplusexpression_instantiation(instance):
    assert isinstance(instance, model::UnaryPlusExpression)

@given(instance=model::NotExpression_strategy)
@settings(max_examples=50)
def test_model::notexpression_instantiation(instance):
    assert isinstance(instance, model::NotExpression)

@given(instance=ElseExpression_strategy)
@settings(max_examples=50)
def test_elseexpression_instantiation(instance):
    assert isinstance(instance, ElseExpression)

@given(instance=model::DefaultExpression_strategy)
@settings(max_examples=50)
def test_model::defaultexpression_instantiation(instance):
    assert isinstance(instance, model::DefaultExpression)

@given(instance=NullaryExpression_strategy)
@settings(max_examples=50)
def test_nullaryexpression_instantiation(instance):
    assert isinstance(instance, NullaryExpression)

@given(instance=model::ArithmeticLiteralExpression_strategy)
@settings(max_examples=50)
def test_model::arithmeticliteralexpression_instantiation(instance):
    assert isinstance(instance, model::ArithmeticLiteralExpression)

@given(instance=model::EnumerationLiteralExpression_strategy)
@settings(max_examples=50)
def test_model::enumerationliteralexpression_instantiation(instance):
    assert isinstance(instance, model::EnumerationLiteralExpression)

@given(instance=model::BooleanLiteralExpression_strategy)
@settings(max_examples=50)
def test_model::booleanliteralexpression_instantiation(instance):
    assert isinstance(instance, model::BooleanLiteralExpression)

@given(instance=model::ReferenceExpression_strategy)
@settings(max_examples=50)
def test_model::referenceexpression_instantiation(instance):
    assert isinstance(instance, model::ReferenceExpression)

@given(instance=model::OpaqueExpression_strategy)
@settings(max_examples=50)
def test_model::opaqueexpression_instantiation(instance):
    assert isinstance(instance, model::OpaqueExpression)

@given(instance=model::OpaqueExpression_strategy)
def test_model::opaqueexpression_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=model::OpaqueExpression_strategy)
def test_model::opaqueexpression_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=LogicExpression_strategy)
@settings(max_examples=50)
def test_logicexpression_instantiation(instance):
    assert isinstance(instance, LogicExpression)

@given(instance=model::ElseExpression_strategy)
@settings(max_examples=50)
def test_model::elseexpression_instantiation(instance):
    assert isinstance(instance, model::ElseExpression)

@given(instance=model::PredicateExpression_strategy)
@settings(max_examples=50)
def test_model::predicateexpression_instantiation(instance):
    assert isinstance(instance, model::PredicateExpression)

@given(instance=model::BooleanExpression_strategy)
@settings(max_examples=50)
def test_model::booleanexpression_instantiation(instance):
    assert isinstance(instance, model::BooleanExpression)

@given(instance=model::LogicExpression_strategy)
@settings(max_examples=50)
def test_model::logicexpression_instantiation(instance):
    assert isinstance(instance, model::LogicExpression)

@given(instance=model::ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_model::arithmeticexpression_instantiation(instance):
    assert isinstance(instance, model::ArithmeticExpression)

@given(instance=model::MultiaryExpression_strategy)
@settings(max_examples=50)
def test_model::multiaryexpression_instantiation(instance):
    assert isinstance(instance, model::MultiaryExpression)

@given(instance=model::BinaryExpression_strategy)
@settings(max_examples=50)
def test_model::binaryexpression_instantiation(instance):
    assert isinstance(instance, model::BinaryExpression)

@given(instance=CompositeTypeDefinition_strategy)
@settings(max_examples=50)
def test_compositetypedefinition_instantiation(instance):
    assert isinstance(instance, CompositeTypeDefinition)

@given(instance=model::FunctionTypeDefinition_strategy)
@settings(max_examples=50)
def test_model::functiontypedefinition_instantiation(instance):
    assert isinstance(instance, model::FunctionTypeDefinition)

@given(instance=model::RecordTypeDefinition_strategy)
@settings(max_examples=50)
def test_model::recordtypedefinition_instantiation(instance):
    assert isinstance(instance, model::RecordTypeDefinition)

@given(instance=EnumerableTypeDefinition_strategy)
@settings(max_examples=50)
def test_enumerabletypedefinition_instantiation(instance):
    assert isinstance(instance, EnumerableTypeDefinition)

@given(instance=model::ArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_model::arraytypedefinition_instantiation(instance):
    assert isinstance(instance, model::ArrayTypeDefinition)

@given(instance=model::IntegerRangeTypeDefinition_strategy)
@settings(max_examples=50)
def test_model::integerrangetypedefinition_instantiation(instance):
    assert isinstance(instance, model::IntegerRangeTypeDefinition)

@given(instance=model::EnumerationTypeDefinition_strategy)
@settings(max_examples=50)
def test_model::enumerationtypedefinition_instantiation(instance):
    assert isinstance(instance, model::EnumerationTypeDefinition)

@given(instance=model::EnumerableTypeDefinition_strategy)
@settings(max_examples=50)
def test_model::enumerabletypedefinition_instantiation(instance):
    assert isinstance(instance, model::EnumerableTypeDefinition)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=model::ValueDeclaration_strategy)
@settings(max_examples=50)
def test_model::valuedeclaration_instantiation(instance):
    assert isinstance(instance, model::ValueDeclaration)

@given(instance=model::Type_strategy)
@settings(max_examples=50)
def test_model::type_instantiation(instance):
    assert isinstance(instance, model::Type)

@given(instance=model::BasicConstraintDefinition_strategy)
@settings(max_examples=50)
def test_model::basicconstraintdefinition_instantiation(instance):
    assert isinstance(instance, model::BasicConstraintDefinition)

@given(instance=model::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_model::typedeclaration_instantiation(instance):
    assert isinstance(instance, model::TypeDeclaration)

@given(instance=ParametricElement_strategy)
@settings(max_examples=50)
def test_parametricelement_instantiation(instance):
    assert isinstance(instance, ParametricElement)

@given(instance=model::FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_model::functiondeclaration_instantiation(instance):
    assert isinstance(instance, model::FunctionDeclaration)

@given(instance=model::QuantifierExpression_strategy)
@settings(max_examples=50)
def test_model::quantifierexpression_instantiation(instance):
    assert isinstance(instance, model::QuantifierExpression)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=model::InitializableElement_strategy)
@settings(max_examples=50)
def test_model::initializableelement_instantiation(instance):
    assert isinstance(instance, model::InitializableElement)

@given(instance=model::Declaration_strategy)
@settings(max_examples=50)
def test_model::declaration_instantiation(instance):
    assert isinstance(instance, model::Declaration)

@given(instance=model::EnumerationLiteralDefinition_strategy)
@settings(max_examples=50)
def test_model::enumerationliteraldefinition_instantiation(instance):
    assert isinstance(instance, model::EnumerationLiteralDefinition)

@given(instance=model::ExpressionPackage_strategy)
@settings(max_examples=50)
def test_model::expressionpackage_instantiation(instance):
    assert isinstance(instance, model::ExpressionPackage)

@given(instance=NumericalTypeDefinition_strategy)
@settings(max_examples=50)
def test_numericaltypedefinition_instantiation(instance):
    assert isinstance(instance, NumericalTypeDefinition)

@given(instance=model::DecimalTypeDefinition_strategy)
@settings(max_examples=50)
def test_model::decimaltypedefinition_instantiation(instance):
    assert isinstance(instance, model::DecimalTypeDefinition)

@given(instance=model::RationalTypeDefinition_strategy)
@settings(max_examples=50)
def test_model::rationaltypedefinition_instantiation(instance):
    assert isinstance(instance, model::RationalTypeDefinition)

@given(instance=model::SubrangeTypeDefinition_strategy)
@settings(max_examples=50)
def test_model::subrangetypedefinition_instantiation(instance):
    assert isinstance(instance, model::SubrangeTypeDefinition)

@given(instance=model::IntegerTypeDefinition_strategy)
@settings(max_examples=50)
def test_model::integertypedefinition_instantiation(instance):
    assert isinstance(instance, model::IntegerTypeDefinition)

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=model::BooleanTypeDefinition_strategy)
@settings(max_examples=50)
def test_model::booleantypedefinition_instantiation(instance):
    assert isinstance(instance, model::BooleanTypeDefinition)

@given(instance=model::VoidTypeDefinition_strategy)
@settings(max_examples=50)
def test_model::voidtypedefinition_instantiation(instance):
    assert isinstance(instance, model::VoidTypeDefinition)

@given(instance=model::CompositeTypeDefinition_strategy)
@settings(max_examples=50)
def test_model::compositetypedefinition_instantiation(instance):
    assert isinstance(instance, model::CompositeTypeDefinition)

@given(instance=model::NumericalTypeDefinition_strategy)
@settings(max_examples=50)
def test_model::numericaltypedefinition_instantiation(instance):
    assert isinstance(instance, model::NumericalTypeDefinition)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=model::TypeDefinition_strategy)
@settings(max_examples=50)
def test_model::typedefinition_instantiation(instance):
    assert isinstance(instance, model::TypeDefinition)

@given(instance=model::TypeReference_strategy)
@settings(max_examples=50)
def test_model::typereference_instantiation(instance):
    assert isinstance(instance, model::TypeReference)

@given(instance=FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_functiondeclaration_instantiation(instance):
    assert isinstance(instance, FunctionDeclaration)

@given(instance=InitializableElement_strategy)
@settings(max_examples=50)
def test_initializableelement_instantiation(instance):
    assert isinstance(instance, InitializableElement)

@given(instance=model::LambdaDeclaration_strategy)
@settings(max_examples=50)
def test_model::lambdadeclaration_instantiation(instance):
    assert isinstance(instance, model::LambdaDeclaration)

@given(instance=ValueDeclaration_strategy)
@settings(max_examples=50)
def test_valuedeclaration_instantiation(instance):
    assert isinstance(instance, ValueDeclaration)

@given(instance=model::FieldDeclaration_strategy)
@settings(max_examples=50)
def test_model::fielddeclaration_instantiation(instance):
    assert isinstance(instance, model::FieldDeclaration)

@given(instance=model::ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_model::constantdeclaration_instantiation(instance):
    assert isinstance(instance, model::ConstantDeclaration)

@given(instance=model::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_model::variabledeclaration_instantiation(instance):
    assert isinstance(instance, model::VariableDeclaration)

@given(instance=model::Comment_strategy)
@settings(max_examples=50)
def test_model::comment_instantiation(instance):
    assert isinstance(instance, model::Comment)

@given(instance=model::Comment_strategy)
def test_model::comment_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=model::Comment_strategy)
def test_model::comment_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=model::CommentableElement_strategy)
@settings(max_examples=50)
def test_model::commentableelement_instantiation(instance):
    assert isinstance(instance, model::CommentableElement)

@given(instance=model::NamedElement_strategy)
@settings(max_examples=50)
def test_model::namedelement_instantiation(instance):
    assert isinstance(instance, model::NamedElement)

@given(instance=model::NamedElement_strategy)
def test_model::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::NamedElement_strategy)
def test_model::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::Expression_strategy)
@settings(max_examples=50)
def test_model::expression_instantiation(instance):
    assert isinstance(instance, model::Expression)

@given(instance=model::ArgumentedElement_strategy)
@settings(max_examples=50)
def test_model::argumentedelement_instantiation(instance):
    assert isinstance(instance, model::ArgumentedElement)

@given(instance=model::ParameterDeclaration_strategy)
@settings(max_examples=50)
def test_model::parameterdeclaration_instantiation(instance):
    assert isinstance(instance, model::ParameterDeclaration)

@given(instance=model::ParametricElement_strategy)
@settings(max_examples=50)
def test_model::parametricelement_instantiation(instance):
    assert isinstance(instance, model::ParametricElement)
