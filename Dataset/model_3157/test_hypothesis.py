import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ParametrizedElement,
    AccessExpression,
    TTMCConstraint::ArrayAccessExpression,
    TTMCConstraint::TupleAccessExpression,
    TTMCConstraint::RecordAccessExpression,
    TTMCConstraint::FunctionAccessExpression,
    EquivalenceExpression,
    TTMCConstraint::InequalityExpression,
    TTMCConstraint::EqualityExpression,
    PredicateExpression,
    TemporalStateExpression,
    QuantifierExpression,
    TTMCConstraint::ExistsExpression,
    TTMCConstraint::ForallExpression,
    TemporalPathExpression,
    MultiaryExpression,
    BinaryExpression,
    TTMCConstraint::EquivalenceExpression,
    TTMCConstraint::UntilExpression,
    TTMCConstraint::ReleaseExpression,
    ComparisionExpression,
    TTMCConstraint::LessEqualExpression,
    TTMCConstraint::LessExpression,
    TTMCConstraint::GreaterEqualExpression,
    TTMCConstraint::GreaterExpression,
    TTMCConstraint::ComparisionExpression,
    TTMCConstraint::FieldAssignment,
    BooleanLiteralExpression,
    TTMCConstraint::FalseExpression,
    TTMCConstraint::TrueExpression,
    BooleanExpression,
    TTMCConstraint::OrExpression,
    TTMCConstraint::ImplyExpression,
    TTMCConstraint::EqualExpression,
    TTMCConstraint::AndExpression,
    ArithmeticLiteralExpression,
    TTMCConstraint::DecimalLiteralExpression,
    TTMCConstraint::RationalLiteralExpression,
    TTMCConstraint::IntegerLiteralExpression,
    Expression,
    TTMCConstraint::UnaryExpression,
    TTMCConstraint::AccessExpression,
    TTMCConstraint::PredicateExpression,
    TTMCConstraint::ArithmeticExpression,
    TTMCConstraint::BinaryExpression,
    TTMCConstraint::LetExpression,
    TTMCConstraint::IfThenElseExpression,
    TTMCConstraint::MultiaryExpression,
    TTMCConstraint::NullaryExpression,
    ConstraintDefinition,
    TTMCConstraint::LiteralExpression,
    TemporalExpression,
    TTMCConstraint::TemporalStateExpression,
    TTMCConstraint::TemporalPathExpression,
    TTMCConstraint::TemporalExpression,
    UnaryExpression,
    TTMCConstraint::PrimedExpression,
    TTMCConstraint::InExpression,
    TTMCConstraint::GloballyExpression,
    TTMCConstraint::NextExpression,
    TTMCConstraint::TemporalExistsExpression,
    TTMCConstraint::TemporalForallExpression,
    TTMCConstraint::FinallyExpression,
    TTMCConstraint::NotExpression,
    TTMCConstraint::BooleanExpression,
    BasicTypeDefinition,
    TTMCConstraint::NaturalTypeDefinition,
    TTMCConstraint::RealTypeDefinition,
    TTMCConstraint::BooleanTypeDefinition,
    TTMCConstraint::IntegerTypeDefinition,
    TypeDefinition,
    TTMCConstraint::SubrangeTypeDefinition,
    TTMCConstraint::EnumerationTypeDefinition,
    TTMCConstraint::BasicTypeDefinition,
    Type,
    TTMCConstraint::TypeDefinition,
    TTMCConstraint::TypeReference,
    TTMCConstraint::ArrayTypeDefinition,
    TTMCConstraint::FunctionTypeDefinition,
    TTMCConstraint::BasicConstraintDefinition,
    ParametricElement,
    TTMCConstraint::SubTypeDefinition,
    TTMCConstraint::QuantifierExpression,
    NamedElement,
    TTMCConstraint::Declaration,
    TTMCConstraint::EnumerationLiteralDefinition,
    TTMCConstraint::TypeDeclaration,
    TTMCConstraint::ConstraintSpecification,
    TTMCConstraint::Expression,
    TTMCConstraint::ParametrizedElement,
    TTMCConstraint::ParametricElement,
    TTMCConstraint::NamedElement,
    DefinableDeclaration,
    TTMCConstraint::FunctionDeclaration,
    TTMCConstraint::ConstantDeclaration,
    TTMCConstraint::LetDeclaration,
    Declaration,
    TTMCConstraint::ParameterDeclaration,
    TTMCConstraint::FieldDeclaration,
    TTMCConstraint::DefinableDeclaration,
    TTMCConstraint::Type,
    TTMCConstraint::ConstraintDefinition,
    TTMCConstraint::RecordTypeDefinition,
    TTMCConstraint::TupleTypeDefinition,
    ArithmeticExpression,
    TTMCConstraint::SubtractExpression,
    TTMCConstraint::MultiplyExpression,
    TTMCConstraint::DivideExpression,
    TTMCConstraint::DivExpression,
    TTMCConstraint::AddExpression,
    TTMCConstraint::UnaryPlusExpression,
    TTMCConstraint::ModExpression,
    TTMCConstraint::UnaryMinusExpression,
    LiteralExpression,
    TTMCConstraint::TupleLiteralExpression,
    TTMCConstraint::FunctionLiteralExpression,
    TTMCConstraint::ArrayLiteralExpression,
    TTMCConstraint::RecordLiteralExpression,
    NullaryExpression,
    TTMCConstraint::EnumerationLiteralExpression,
    TTMCConstraint::ReferenceExpression,
    TTMCConstraint::BooleanLiteralExpression,
    TTMCConstraint::ArithmeticLiteralExpression,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_parametrizedelement_is_not_abstract():
    assert not inspect.isabstract(ParametrizedElement)


def test_parametrizedelement_constructor_exists():
    assert callable(ParametrizedElement.__init__)


def test_parametrizedelement_constructor_args():
    sig = inspect.signature(ParametrizedElement.__init__)
    params = list(sig.parameters.keys())



def test_accessexpression_is_not_abstract():
    assert not inspect.isabstract(AccessExpression)


def test_accessexpression_constructor_exists():
    assert callable(AccessExpression.__init__)


def test_accessexpression_constructor_args():
    sig = inspect.signature(AccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::arrayaccessexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::ArrayAccessExpression)


def test_ttmcconstraint::arrayaccessexpression_constructor_exists():
    assert callable(TTMCConstraint::ArrayAccessExpression.__init__)


def test_ttmcconstraint::arrayaccessexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::ArrayAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::tupleaccessexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::TupleAccessExpression)


def test_ttmcconstraint::tupleaccessexpression_constructor_exists():
    assert callable(TTMCConstraint::TupleAccessExpression.__init__)


def test_ttmcconstraint::tupleaccessexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::TupleAccessExpression.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_ttmcconstraint::tupleaccessexpression_has_index():
    assert hasattr(TTMCConstraint::TupleAccessExpression, "index")
    descriptor = None
    for klass in TTMCConstraint::TupleAccessExpression.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_ttmcconstraint::recordaccessexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::RecordAccessExpression)


def test_ttmcconstraint::recordaccessexpression_constructor_exists():
    assert callable(TTMCConstraint::RecordAccessExpression.__init__)


def test_ttmcconstraint::recordaccessexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::RecordAccessExpression.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_ttmcconstraint::recordaccessexpression_has_field():
    assert hasattr(TTMCConstraint::RecordAccessExpression, "field")
    descriptor = None
    for klass in TTMCConstraint::RecordAccessExpression.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_ttmcconstraint::functionaccessexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::FunctionAccessExpression)


def test_ttmcconstraint::functionaccessexpression_constructor_exists():
    assert callable(TTMCConstraint::FunctionAccessExpression.__init__)


def test_ttmcconstraint::functionaccessexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::FunctionAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_equivalenceexpression_is_not_abstract():
    assert not inspect.isabstract(EquivalenceExpression)


def test_equivalenceexpression_constructor_exists():
    assert callable(EquivalenceExpression.__init__)


def test_equivalenceexpression_constructor_args():
    sig = inspect.signature(EquivalenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::inequalityexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::InequalityExpression)


def test_ttmcconstraint::inequalityexpression_constructor_exists():
    assert callable(TTMCConstraint::InequalityExpression.__init__)


def test_ttmcconstraint::inequalityexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::InequalityExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::equalityexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::EqualityExpression)


def test_ttmcconstraint::equalityexpression_constructor_exists():
    assert callable(TTMCConstraint::EqualityExpression.__init__)


def test_ttmcconstraint::equalityexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_predicateexpression_is_not_abstract():
    assert not inspect.isabstract(PredicateExpression)


def test_predicateexpression_constructor_exists():
    assert callable(PredicateExpression.__init__)


def test_predicateexpression_constructor_args():
    sig = inspect.signature(PredicateExpression.__init__)
    params = list(sig.parameters.keys())



def test_temporalstateexpression_is_not_abstract():
    assert not inspect.isabstract(TemporalStateExpression)


def test_temporalstateexpression_constructor_exists():
    assert callable(TemporalStateExpression.__init__)


def test_temporalstateexpression_constructor_args():
    sig = inspect.signature(TemporalStateExpression.__init__)
    params = list(sig.parameters.keys())



def test_quantifierexpression_is_not_abstract():
    assert not inspect.isabstract(QuantifierExpression)


def test_quantifierexpression_constructor_exists():
    assert callable(QuantifierExpression.__init__)


def test_quantifierexpression_constructor_args():
    sig = inspect.signature(QuantifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::existsexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::ExistsExpression)


def test_ttmcconstraint::existsexpression_constructor_exists():
    assert callable(TTMCConstraint::ExistsExpression.__init__)


def test_ttmcconstraint::existsexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::ExistsExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::forallexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::ForallExpression)


def test_ttmcconstraint::forallexpression_constructor_exists():
    assert callable(TTMCConstraint::ForallExpression.__init__)


def test_ttmcconstraint::forallexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::ForallExpression.__init__)
    params = list(sig.parameters.keys())



def test_temporalpathexpression_is_not_abstract():
    assert not inspect.isabstract(TemporalPathExpression)


def test_temporalpathexpression_constructor_exists():
    assert callable(TemporalPathExpression.__init__)


def test_temporalpathexpression_constructor_args():
    sig = inspect.signature(TemporalPathExpression.__init__)
    params = list(sig.parameters.keys())



def test_multiaryexpression_is_not_abstract():
    assert not inspect.isabstract(MultiaryExpression)


def test_multiaryexpression_constructor_exists():
    assert callable(MultiaryExpression.__init__)


def test_multiaryexpression_constructor_args():
    sig = inspect.signature(MultiaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::equivalenceexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::EquivalenceExpression)


def test_ttmcconstraint::equivalenceexpression_constructor_exists():
    assert callable(TTMCConstraint::EquivalenceExpression.__init__)


def test_ttmcconstraint::equivalenceexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::EquivalenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::untilexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::UntilExpression)


def test_ttmcconstraint::untilexpression_constructor_exists():
    assert callable(TTMCConstraint::UntilExpression.__init__)


def test_ttmcconstraint::untilexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::UntilExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::releaseexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::ReleaseExpression)


def test_ttmcconstraint::releaseexpression_constructor_exists():
    assert callable(TTMCConstraint::ReleaseExpression.__init__)


def test_ttmcconstraint::releaseexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::ReleaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_comparisionexpression_is_not_abstract():
    assert not inspect.isabstract(ComparisionExpression)


def test_comparisionexpression_constructor_exists():
    assert callable(ComparisionExpression.__init__)


def test_comparisionexpression_constructor_args():
    sig = inspect.signature(ComparisionExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::lessequalexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::LessEqualExpression)


def test_ttmcconstraint::lessequalexpression_constructor_exists():
    assert callable(TTMCConstraint::LessEqualExpression.__init__)


def test_ttmcconstraint::lessequalexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::LessEqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::lessexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::LessExpression)


def test_ttmcconstraint::lessexpression_constructor_exists():
    assert callable(TTMCConstraint::LessExpression.__init__)


def test_ttmcconstraint::lessexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::LessExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::greaterequalexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::GreaterEqualExpression)


def test_ttmcconstraint::greaterequalexpression_constructor_exists():
    assert callable(TTMCConstraint::GreaterEqualExpression.__init__)


def test_ttmcconstraint::greaterequalexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::GreaterEqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::greaterexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::GreaterExpression)


def test_ttmcconstraint::greaterexpression_constructor_exists():
    assert callable(TTMCConstraint::GreaterExpression.__init__)


def test_ttmcconstraint::greaterexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::GreaterExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::comparisionexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::ComparisionExpression)


def test_ttmcconstraint::comparisionexpression_constructor_exists():
    assert callable(TTMCConstraint::ComparisionExpression.__init__)


def test_ttmcconstraint::comparisionexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::ComparisionExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::fieldassignment_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::FieldAssignment)


def test_ttmcconstraint::fieldassignment_constructor_exists():
    assert callable(TTMCConstraint::FieldAssignment.__init__)


def test_ttmcconstraint::fieldassignment_constructor_args():
    sig = inspect.signature(TTMCConstraint::FieldAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"

def test_ttmcconstraint::fieldassignment_has_reference():
    assert hasattr(TTMCConstraint::FieldAssignment, "reference")
    descriptor = None
    for klass in TTMCConstraint::FieldAssignment.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)



def test_booleanliteralexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanLiteralExpression)


def test_booleanliteralexpression_constructor_exists():
    assert callable(BooleanLiteralExpression.__init__)


def test_booleanliteralexpression_constructor_args():
    sig = inspect.signature(BooleanLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::falseexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::FalseExpression)


def test_ttmcconstraint::falseexpression_constructor_exists():
    assert callable(TTMCConstraint::FalseExpression.__init__)


def test_ttmcconstraint::falseexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::FalseExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::trueexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::TrueExpression)


def test_ttmcconstraint::trueexpression_constructor_exists():
    assert callable(TTMCConstraint::TrueExpression.__init__)


def test_ttmcconstraint::trueexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::TrueExpression.__init__)
    params = list(sig.parameters.keys())



def test_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::orexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::OrExpression)


def test_ttmcconstraint::orexpression_constructor_exists():
    assert callable(TTMCConstraint::OrExpression.__init__)


def test_ttmcconstraint::orexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::implyexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::ImplyExpression)


def test_ttmcconstraint::implyexpression_constructor_exists():
    assert callable(TTMCConstraint::ImplyExpression.__init__)


def test_ttmcconstraint::implyexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::ImplyExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::equalexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::EqualExpression)


def test_ttmcconstraint::equalexpression_constructor_exists():
    assert callable(TTMCConstraint::EqualExpression.__init__)


def test_ttmcconstraint::equalexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::EqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::andexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::AndExpression)


def test_ttmcconstraint::andexpression_constructor_exists():
    assert callable(TTMCConstraint::AndExpression.__init__)


def test_ttmcconstraint::andexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticliteralexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticLiteralExpression)


def test_arithmeticliteralexpression_constructor_exists():
    assert callable(ArithmeticLiteralExpression.__init__)


def test_arithmeticliteralexpression_constructor_args():
    sig = inspect.signature(ArithmeticLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::decimalliteralexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::DecimalLiteralExpression)


def test_ttmcconstraint::decimalliteralexpression_constructor_exists():
    assert callable(TTMCConstraint::DecimalLiteralExpression.__init__)


def test_ttmcconstraint::decimalliteralexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::DecimalLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ttmcconstraint::decimalliteralexpression_has_value():
    assert hasattr(TTMCConstraint::DecimalLiteralExpression, "value")
    descriptor = None
    for klass in TTMCConstraint::DecimalLiteralExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ttmcconstraint::rationalliteralexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::RationalLiteralExpression)


def test_ttmcconstraint::rationalliteralexpression_constructor_exists():
    assert callable(TTMCConstraint::RationalLiteralExpression.__init__)


def test_ttmcconstraint::rationalliteralexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::RationalLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "numerator" in params, "Missing parameter 'numerator'"
    assert "denominator" in params, "Missing parameter 'denominator'"

def test_ttmcconstraint::rationalliteralexpression_has_numerator():
    assert hasattr(TTMCConstraint::RationalLiteralExpression, "numerator")
    descriptor = None
    for klass in TTMCConstraint::RationalLiteralExpression.__mro__:
        if "numerator" in klass.__dict__:
            descriptor = klass.__dict__["numerator"]
            break
    assert isinstance(descriptor, property)

def test_ttmcconstraint::rationalliteralexpression_has_denominator():
    assert hasattr(TTMCConstraint::RationalLiteralExpression, "denominator")
    descriptor = None
    for klass in TTMCConstraint::RationalLiteralExpression.__mro__:
        if "denominator" in klass.__dict__:
            descriptor = klass.__dict__["denominator"]
            break
    assert isinstance(descriptor, property)



def test_ttmcconstraint::integerliteralexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::IntegerLiteralExpression)


def test_ttmcconstraint::integerliteralexpression_constructor_exists():
    assert callable(TTMCConstraint::IntegerLiteralExpression.__init__)


def test_ttmcconstraint::integerliteralexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::IntegerLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ttmcconstraint::integerliteralexpression_has_value():
    assert hasattr(TTMCConstraint::IntegerLiteralExpression, "value")
    descriptor = None
    for klass in TTMCConstraint::IntegerLiteralExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::UnaryExpression)


def test_ttmcconstraint::unaryexpression_constructor_exists():
    assert callable(TTMCConstraint::UnaryExpression.__init__)


def test_ttmcconstraint::unaryexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::accessexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::AccessExpression)


def test_ttmcconstraint::accessexpression_constructor_exists():
    assert callable(TTMCConstraint::AccessExpression.__init__)


def test_ttmcconstraint::accessexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::AccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::predicateexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::PredicateExpression)


def test_ttmcconstraint::predicateexpression_constructor_exists():
    assert callable(TTMCConstraint::PredicateExpression.__init__)


def test_ttmcconstraint::predicateexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::PredicateExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::ArithmeticExpression)


def test_ttmcconstraint::arithmeticexpression_constructor_exists():
    assert callable(TTMCConstraint::ArithmeticExpression.__init__)


def test_ttmcconstraint::arithmeticexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::BinaryExpression)


def test_ttmcconstraint::binaryexpression_constructor_exists():
    assert callable(TTMCConstraint::BinaryExpression.__init__)


def test_ttmcconstraint::binaryexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::letexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::LetExpression)


def test_ttmcconstraint::letexpression_constructor_exists():
    assert callable(TTMCConstraint::LetExpression.__init__)


def test_ttmcconstraint::letexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::LetExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::ifthenelseexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::IfThenElseExpression)


def test_ttmcconstraint::ifthenelseexpression_constructor_exists():
    assert callable(TTMCConstraint::IfThenElseExpression.__init__)


def test_ttmcconstraint::ifthenelseexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::IfThenElseExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::multiaryexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::MultiaryExpression)


def test_ttmcconstraint::multiaryexpression_constructor_exists():
    assert callable(TTMCConstraint::MultiaryExpression.__init__)


def test_ttmcconstraint::multiaryexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::MultiaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::nullaryexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::NullaryExpression)


def test_ttmcconstraint::nullaryexpression_constructor_exists():
    assert callable(TTMCConstraint::NullaryExpression.__init__)


def test_ttmcconstraint::nullaryexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::NullaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_constraintdefinition_is_not_abstract():
    assert not inspect.isabstract(ConstraintDefinition)


def test_constraintdefinition_constructor_exists():
    assert callable(ConstraintDefinition.__init__)


def test_constraintdefinition_constructor_args():
    sig = inspect.signature(ConstraintDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::literalexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::LiteralExpression)


def test_ttmcconstraint::literalexpression_constructor_exists():
    assert callable(TTMCConstraint::LiteralExpression.__init__)


def test_ttmcconstraint::literalexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_temporalexpression_is_not_abstract():
    assert not inspect.isabstract(TemporalExpression)


def test_temporalexpression_constructor_exists():
    assert callable(TemporalExpression.__init__)


def test_temporalexpression_constructor_args():
    sig = inspect.signature(TemporalExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::temporalstateexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::TemporalStateExpression)


def test_ttmcconstraint::temporalstateexpression_constructor_exists():
    assert callable(TTMCConstraint::TemporalStateExpression.__init__)


def test_ttmcconstraint::temporalstateexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::TemporalStateExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::temporalpathexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::TemporalPathExpression)


def test_ttmcconstraint::temporalpathexpression_constructor_exists():
    assert callable(TTMCConstraint::TemporalPathExpression.__init__)


def test_ttmcconstraint::temporalpathexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::TemporalPathExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::temporalexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::TemporalExpression)


def test_ttmcconstraint::temporalexpression_constructor_exists():
    assert callable(TTMCConstraint::TemporalExpression.__init__)


def test_ttmcconstraint::temporalexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::TemporalExpression.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::primedexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::PrimedExpression)


def test_ttmcconstraint::primedexpression_constructor_exists():
    assert callable(TTMCConstraint::PrimedExpression.__init__)


def test_ttmcconstraint::primedexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::PrimedExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::inexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::InExpression)


def test_ttmcconstraint::inexpression_constructor_exists():
    assert callable(TTMCConstraint::InExpression.__init__)


def test_ttmcconstraint::inexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::InExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::globallyexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::GloballyExpression)


def test_ttmcconstraint::globallyexpression_constructor_exists():
    assert callable(TTMCConstraint::GloballyExpression.__init__)


def test_ttmcconstraint::globallyexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::GloballyExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::nextexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::NextExpression)


def test_ttmcconstraint::nextexpression_constructor_exists():
    assert callable(TTMCConstraint::NextExpression.__init__)


def test_ttmcconstraint::nextexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::NextExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::temporalexistsexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::TemporalExistsExpression)


def test_ttmcconstraint::temporalexistsexpression_constructor_exists():
    assert callable(TTMCConstraint::TemporalExistsExpression.__init__)


def test_ttmcconstraint::temporalexistsexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::TemporalExistsExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::temporalforallexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::TemporalForallExpression)


def test_ttmcconstraint::temporalforallexpression_constructor_exists():
    assert callable(TTMCConstraint::TemporalForallExpression.__init__)


def test_ttmcconstraint::temporalforallexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::TemporalForallExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::finallyexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::FinallyExpression)


def test_ttmcconstraint::finallyexpression_constructor_exists():
    assert callable(TTMCConstraint::FinallyExpression.__init__)


def test_ttmcconstraint::finallyexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::FinallyExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::notexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::NotExpression)


def test_ttmcconstraint::notexpression_constructor_exists():
    assert callable(TTMCConstraint::NotExpression.__init__)


def test_ttmcconstraint::notexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::BooleanExpression)


def test_ttmcconstraint::booleanexpression_constructor_exists():
    assert callable(TTMCConstraint::BooleanExpression.__init__)


def test_ttmcconstraint::booleanexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_basictypedefinition_is_not_abstract():
    assert not inspect.isabstract(BasicTypeDefinition)


def test_basictypedefinition_constructor_exists():
    assert callable(BasicTypeDefinition.__init__)


def test_basictypedefinition_constructor_args():
    sig = inspect.signature(BasicTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::naturaltypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::NaturalTypeDefinition)


def test_ttmcconstraint::naturaltypedefinition_constructor_exists():
    assert callable(TTMCConstraint::NaturalTypeDefinition.__init__)


def test_ttmcconstraint::naturaltypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint::NaturalTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::realtypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::RealTypeDefinition)


def test_ttmcconstraint::realtypedefinition_constructor_exists():
    assert callable(TTMCConstraint::RealTypeDefinition.__init__)


def test_ttmcconstraint::realtypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint::RealTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::booleantypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::BooleanTypeDefinition)


def test_ttmcconstraint::booleantypedefinition_constructor_exists():
    assert callable(TTMCConstraint::BooleanTypeDefinition.__init__)


def test_ttmcconstraint::booleantypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint::BooleanTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::integertypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::IntegerTypeDefinition)


def test_ttmcconstraint::integertypedefinition_constructor_exists():
    assert callable(TTMCConstraint::IntegerTypeDefinition.__init__)


def test_ttmcconstraint::integertypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint::IntegerTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::subrangetypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::SubrangeTypeDefinition)


def test_ttmcconstraint::subrangetypedefinition_constructor_exists():
    assert callable(TTMCConstraint::SubrangeTypeDefinition.__init__)


def test_ttmcconstraint::subrangetypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint::SubrangeTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::enumerationtypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::EnumerationTypeDefinition)


def test_ttmcconstraint::enumerationtypedefinition_constructor_exists():
    assert callable(TTMCConstraint::EnumerationTypeDefinition.__init__)


def test_ttmcconstraint::enumerationtypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint::EnumerationTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::basictypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::BasicTypeDefinition)


def test_ttmcconstraint::basictypedefinition_constructor_exists():
    assert callable(TTMCConstraint::BasicTypeDefinition.__init__)


def test_ttmcconstraint::basictypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint::BasicTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::typedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::TypeDefinition)


def test_ttmcconstraint::typedefinition_constructor_exists():
    assert callable(TTMCConstraint::TypeDefinition.__init__)


def test_ttmcconstraint::typedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint::TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::typereference_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::TypeReference)


def test_ttmcconstraint::typereference_constructor_exists():
    assert callable(TTMCConstraint::TypeReference.__init__)


def test_ttmcconstraint::typereference_constructor_args():
    sig = inspect.signature(TTMCConstraint::TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::arraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::ArrayTypeDefinition)


def test_ttmcconstraint::arraytypedefinition_constructor_exists():
    assert callable(TTMCConstraint::ArrayTypeDefinition.__init__)


def test_ttmcconstraint::arraytypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint::ArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::functiontypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::FunctionTypeDefinition)


def test_ttmcconstraint::functiontypedefinition_constructor_exists():
    assert callable(TTMCConstraint::FunctionTypeDefinition.__init__)


def test_ttmcconstraint::functiontypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint::FunctionTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::basicconstraintdefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::BasicConstraintDefinition)


def test_ttmcconstraint::basicconstraintdefinition_constructor_exists():
    assert callable(TTMCConstraint::BasicConstraintDefinition.__init__)


def test_ttmcconstraint::basicconstraintdefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint::BasicConstraintDefinition.__init__)
    params = list(sig.parameters.keys())



def test_parametricelement_is_not_abstract():
    assert not inspect.isabstract(ParametricElement)


def test_parametricelement_constructor_exists():
    assert callable(ParametricElement.__init__)


def test_parametricelement_constructor_args():
    sig = inspect.signature(ParametricElement.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::subtypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::SubTypeDefinition)


def test_ttmcconstraint::subtypedefinition_constructor_exists():
    assert callable(TTMCConstraint::SubTypeDefinition.__init__)


def test_ttmcconstraint::subtypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint::SubTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::quantifierexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::QuantifierExpression)


def test_ttmcconstraint::quantifierexpression_constructor_exists():
    assert callable(TTMCConstraint::QuantifierExpression.__init__)


def test_ttmcconstraint::quantifierexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::QuantifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::declaration_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::Declaration)


def test_ttmcconstraint::declaration_constructor_exists():
    assert callable(TTMCConstraint::Declaration.__init__)


def test_ttmcconstraint::declaration_constructor_args():
    sig = inspect.signature(TTMCConstraint::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::enumerationliteraldefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::EnumerationLiteralDefinition)


def test_ttmcconstraint::enumerationliteraldefinition_constructor_exists():
    assert callable(TTMCConstraint::EnumerationLiteralDefinition.__init__)


def test_ttmcconstraint::enumerationliteraldefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint::EnumerationLiteralDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::TypeDeclaration)


def test_ttmcconstraint::typedeclaration_constructor_exists():
    assert callable(TTMCConstraint::TypeDeclaration.__init__)


def test_ttmcconstraint::typedeclaration_constructor_args():
    sig = inspect.signature(TTMCConstraint::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::constraintspecification_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::ConstraintSpecification)


def test_ttmcconstraint::constraintspecification_constructor_exists():
    assert callable(TTMCConstraint::ConstraintSpecification.__init__)


def test_ttmcconstraint::constraintspecification_constructor_args():
    sig = inspect.signature(TTMCConstraint::ConstraintSpecification.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::expression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::Expression)


def test_ttmcconstraint::expression_constructor_exists():
    assert callable(TTMCConstraint::Expression.__init__)


def test_ttmcconstraint::expression_constructor_args():
    sig = inspect.signature(TTMCConstraint::Expression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::parametrizedelement_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::ParametrizedElement)


def test_ttmcconstraint::parametrizedelement_constructor_exists():
    assert callable(TTMCConstraint::ParametrizedElement.__init__)


def test_ttmcconstraint::parametrizedelement_constructor_args():
    sig = inspect.signature(TTMCConstraint::ParametrizedElement.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::parametricelement_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::ParametricElement)


def test_ttmcconstraint::parametricelement_constructor_exists():
    assert callable(TTMCConstraint::ParametricElement.__init__)


def test_ttmcconstraint::parametricelement_constructor_args():
    sig = inspect.signature(TTMCConstraint::ParametricElement.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::namedelement_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::NamedElement)


def test_ttmcconstraint::namedelement_constructor_exists():
    assert callable(TTMCConstraint::NamedElement.__init__)


def test_ttmcconstraint::namedelement_constructor_args():
    sig = inspect.signature(TTMCConstraint::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ttmcconstraint::namedelement_has_name():
    assert hasattr(TTMCConstraint::NamedElement, "name")
    descriptor = None
    for klass in TTMCConstraint::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_definabledeclaration_is_not_abstract():
    assert not inspect.isabstract(DefinableDeclaration)


def test_definabledeclaration_constructor_exists():
    assert callable(DefinableDeclaration.__init__)


def test_definabledeclaration_constructor_args():
    sig = inspect.signature(DefinableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::FunctionDeclaration)


def test_ttmcconstraint::functiondeclaration_constructor_exists():
    assert callable(TTMCConstraint::FunctionDeclaration.__init__)


def test_ttmcconstraint::functiondeclaration_constructor_args():
    sig = inspect.signature(TTMCConstraint::FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::ConstantDeclaration)


def test_ttmcconstraint::constantdeclaration_constructor_exists():
    assert callable(TTMCConstraint::ConstantDeclaration.__init__)


def test_ttmcconstraint::constantdeclaration_constructor_args():
    sig = inspect.signature(TTMCConstraint::ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::letdeclaration_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::LetDeclaration)


def test_ttmcconstraint::letdeclaration_constructor_exists():
    assert callable(TTMCConstraint::LetDeclaration.__init__)


def test_ttmcconstraint::letdeclaration_constructor_args():
    sig = inspect.signature(TTMCConstraint::LetDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::ParameterDeclaration)


def test_ttmcconstraint::parameterdeclaration_constructor_exists():
    assert callable(TTMCConstraint::ParameterDeclaration.__init__)


def test_ttmcconstraint::parameterdeclaration_constructor_args():
    sig = inspect.signature(TTMCConstraint::ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::FieldDeclaration)


def test_ttmcconstraint::fielddeclaration_constructor_exists():
    assert callable(TTMCConstraint::FieldDeclaration.__init__)


def test_ttmcconstraint::fielddeclaration_constructor_args():
    sig = inspect.signature(TTMCConstraint::FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::definabledeclaration_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::DefinableDeclaration)


def test_ttmcconstraint::definabledeclaration_constructor_exists():
    assert callable(TTMCConstraint::DefinableDeclaration.__init__)


def test_ttmcconstraint::definabledeclaration_constructor_args():
    sig = inspect.signature(TTMCConstraint::DefinableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::type_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::Type)


def test_ttmcconstraint::type_constructor_exists():
    assert callable(TTMCConstraint::Type.__init__)


def test_ttmcconstraint::type_constructor_args():
    sig = inspect.signature(TTMCConstraint::Type.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::constraintdefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::ConstraintDefinition)


def test_ttmcconstraint::constraintdefinition_constructor_exists():
    assert callable(TTMCConstraint::ConstraintDefinition.__init__)


def test_ttmcconstraint::constraintdefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint::ConstraintDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::recordtypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::RecordTypeDefinition)


def test_ttmcconstraint::recordtypedefinition_constructor_exists():
    assert callable(TTMCConstraint::RecordTypeDefinition.__init__)


def test_ttmcconstraint::recordtypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint::RecordTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::tupletypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::TupleTypeDefinition)


def test_ttmcconstraint::tupletypedefinition_constructor_exists():
    assert callable(TTMCConstraint::TupleTypeDefinition.__init__)


def test_ttmcconstraint::tupletypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint::TupleTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticExpression)


def test_arithmeticexpression_constructor_exists():
    assert callable(ArithmeticExpression.__init__)


def test_arithmeticexpression_constructor_args():
    sig = inspect.signature(ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::subtractexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::SubtractExpression)


def test_ttmcconstraint::subtractexpression_constructor_exists():
    assert callable(TTMCConstraint::SubtractExpression.__init__)


def test_ttmcconstraint::subtractexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::SubtractExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::multiplyexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::MultiplyExpression)


def test_ttmcconstraint::multiplyexpression_constructor_exists():
    assert callable(TTMCConstraint::MultiplyExpression.__init__)


def test_ttmcconstraint::multiplyexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::MultiplyExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::divideexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::DivideExpression)


def test_ttmcconstraint::divideexpression_constructor_exists():
    assert callable(TTMCConstraint::DivideExpression.__init__)


def test_ttmcconstraint::divideexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::DivideExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::divexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::DivExpression)


def test_ttmcconstraint::divexpression_constructor_exists():
    assert callable(TTMCConstraint::DivExpression.__init__)


def test_ttmcconstraint::divexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::DivExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::addexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::AddExpression)


def test_ttmcconstraint::addexpression_constructor_exists():
    assert callable(TTMCConstraint::AddExpression.__init__)


def test_ttmcconstraint::addexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::AddExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::unaryplusexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::UnaryPlusExpression)


def test_ttmcconstraint::unaryplusexpression_constructor_exists():
    assert callable(TTMCConstraint::UnaryPlusExpression.__init__)


def test_ttmcconstraint::unaryplusexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::UnaryPlusExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::modexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::ModExpression)


def test_ttmcconstraint::modexpression_constructor_exists():
    assert callable(TTMCConstraint::ModExpression.__init__)


def test_ttmcconstraint::modexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::ModExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::unaryminusexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::UnaryMinusExpression)


def test_ttmcconstraint::unaryminusexpression_constructor_exists():
    assert callable(TTMCConstraint::UnaryMinusExpression.__init__)


def test_ttmcconstraint::unaryminusexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::UnaryMinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_literalexpression_is_not_abstract():
    assert not inspect.isabstract(LiteralExpression)


def test_literalexpression_constructor_exists():
    assert callable(LiteralExpression.__init__)


def test_literalexpression_constructor_args():
    sig = inspect.signature(LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::tupleliteralexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::TupleLiteralExpression)


def test_ttmcconstraint::tupleliteralexpression_constructor_exists():
    assert callable(TTMCConstraint::TupleLiteralExpression.__init__)


def test_ttmcconstraint::tupleliteralexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::TupleLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::functionliteralexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::FunctionLiteralExpression)


def test_ttmcconstraint::functionliteralexpression_constructor_exists():
    assert callable(TTMCConstraint::FunctionLiteralExpression.__init__)


def test_ttmcconstraint::functionliteralexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::FunctionLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::arrayliteralexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::ArrayLiteralExpression)


def test_ttmcconstraint::arrayliteralexpression_constructor_exists():
    assert callable(TTMCConstraint::ArrayLiteralExpression.__init__)


def test_ttmcconstraint::arrayliteralexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::ArrayLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::recordliteralexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::RecordLiteralExpression)


def test_ttmcconstraint::recordliteralexpression_constructor_exists():
    assert callable(TTMCConstraint::RecordLiteralExpression.__init__)


def test_ttmcconstraint::recordliteralexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::RecordLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_nullaryexpression_is_not_abstract():
    assert not inspect.isabstract(NullaryExpression)


def test_nullaryexpression_constructor_exists():
    assert callable(NullaryExpression.__init__)


def test_nullaryexpression_constructor_args():
    sig = inspect.signature(NullaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::enumerationliteralexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::EnumerationLiteralExpression)


def test_ttmcconstraint::enumerationliteralexpression_constructor_exists():
    assert callable(TTMCConstraint::EnumerationLiteralExpression.__init__)


def test_ttmcconstraint::enumerationliteralexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::EnumerationLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::referenceexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::ReferenceExpression)


def test_ttmcconstraint::referenceexpression_constructor_exists():
    assert callable(TTMCConstraint::ReferenceExpression.__init__)


def test_ttmcconstraint::referenceexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::ReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::booleanliteralexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::BooleanLiteralExpression)


def test_ttmcconstraint::booleanliteralexpression_constructor_exists():
    assert callable(TTMCConstraint::BooleanLiteralExpression.__init__)


def test_ttmcconstraint::booleanliteralexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::BooleanLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint::arithmeticliteralexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint::ArithmeticLiteralExpression)


def test_ttmcconstraint::arithmeticliteralexpression_constructor_exists():
    assert callable(TTMCConstraint::ArithmeticLiteralExpression.__init__)


def test_ttmcconstraint::arithmeticliteralexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint::ArithmeticLiteralExpression.__init__)
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
ParametrizedElement_strategy = st.builds(
    ParametrizedElement,
)
AccessExpression_strategy = st.builds(
    AccessExpression,
)
TTMCConstraint::ArrayAccessExpression_strategy = st.builds(
    TTMCConstraint::ArrayAccessExpression,
)
TTMCConstraint::TupleAccessExpression_strategy = st.builds(
    TTMCConstraint::TupleAccessExpression,
    index=
        safe_text
)
TTMCConstraint::RecordAccessExpression_strategy = st.builds(
    TTMCConstraint::RecordAccessExpression,
    field=
        safe_text
)
TTMCConstraint::FunctionAccessExpression_strategy = st.builds(
    TTMCConstraint::FunctionAccessExpression,
)
EquivalenceExpression_strategy = st.builds(
    EquivalenceExpression,
)
TTMCConstraint::InequalityExpression_strategy = st.builds(
    TTMCConstraint::InequalityExpression,
)
TTMCConstraint::EqualityExpression_strategy = st.builds(
    TTMCConstraint::EqualityExpression,
)
PredicateExpression_strategy = st.builds(
    PredicateExpression,
)
TemporalStateExpression_strategy = st.builds(
    TemporalStateExpression,
)
QuantifierExpression_strategy = st.builds(
    QuantifierExpression,
)
TTMCConstraint::ExistsExpression_strategy = st.builds(
    TTMCConstraint::ExistsExpression,
)
TTMCConstraint::ForallExpression_strategy = st.builds(
    TTMCConstraint::ForallExpression,
)
TemporalPathExpression_strategy = st.builds(
    TemporalPathExpression,
)
MultiaryExpression_strategy = st.builds(
    MultiaryExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
TTMCConstraint::EquivalenceExpression_strategy = st.builds(
    TTMCConstraint::EquivalenceExpression,
)
TTMCConstraint::UntilExpression_strategy = st.builds(
    TTMCConstraint::UntilExpression,
)
TTMCConstraint::ReleaseExpression_strategy = st.builds(
    TTMCConstraint::ReleaseExpression,
)
ComparisionExpression_strategy = st.builds(
    ComparisionExpression,
)
TTMCConstraint::LessEqualExpression_strategy = st.builds(
    TTMCConstraint::LessEqualExpression,
)
TTMCConstraint::LessExpression_strategy = st.builds(
    TTMCConstraint::LessExpression,
)
TTMCConstraint::GreaterEqualExpression_strategy = st.builds(
    TTMCConstraint::GreaterEqualExpression,
)
TTMCConstraint::GreaterExpression_strategy = st.builds(
    TTMCConstraint::GreaterExpression,
)
TTMCConstraint::ComparisionExpression_strategy = st.builds(
    TTMCConstraint::ComparisionExpression,
)
TTMCConstraint::FieldAssignment_strategy = st.builds(
    TTMCConstraint::FieldAssignment,
    reference=
        safe_text
)
BooleanLiteralExpression_strategy = st.builds(
    BooleanLiteralExpression,
)
TTMCConstraint::FalseExpression_strategy = st.builds(
    TTMCConstraint::FalseExpression,
)
TTMCConstraint::TrueExpression_strategy = st.builds(
    TTMCConstraint::TrueExpression,
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
TTMCConstraint::OrExpression_strategy = st.builds(
    TTMCConstraint::OrExpression,
)
TTMCConstraint::ImplyExpression_strategy = st.builds(
    TTMCConstraint::ImplyExpression,
)
TTMCConstraint::EqualExpression_strategy = st.builds(
    TTMCConstraint::EqualExpression,
)
TTMCConstraint::AndExpression_strategy = st.builds(
    TTMCConstraint::AndExpression,
)
ArithmeticLiteralExpression_strategy = st.builds(
    ArithmeticLiteralExpression,
)
TTMCConstraint::DecimalLiteralExpression_strategy = st.builds(
    TTMCConstraint::DecimalLiteralExpression,
    value=
        safe_text
)
TTMCConstraint::RationalLiteralExpression_strategy = st.builds(
    TTMCConstraint::RationalLiteralExpression,
    numerator=
        safe_text,
    denominator=
        safe_text
)
TTMCConstraint::IntegerLiteralExpression_strategy = st.builds(
    TTMCConstraint::IntegerLiteralExpression,
    value=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
TTMCConstraint::UnaryExpression_strategy = st.builds(
    TTMCConstraint::UnaryExpression,
)
TTMCConstraint::AccessExpression_strategy = st.builds(
    TTMCConstraint::AccessExpression,
)
TTMCConstraint::PredicateExpression_strategy = st.builds(
    TTMCConstraint::PredicateExpression,
)
TTMCConstraint::ArithmeticExpression_strategy = st.builds(
    TTMCConstraint::ArithmeticExpression,
)
TTMCConstraint::BinaryExpression_strategy = st.builds(
    TTMCConstraint::BinaryExpression,
)
TTMCConstraint::LetExpression_strategy = st.builds(
    TTMCConstraint::LetExpression,
)
TTMCConstraint::IfThenElseExpression_strategy = st.builds(
    TTMCConstraint::IfThenElseExpression,
)
TTMCConstraint::MultiaryExpression_strategy = st.builds(
    TTMCConstraint::MultiaryExpression,
)
TTMCConstraint::NullaryExpression_strategy = st.builds(
    TTMCConstraint::NullaryExpression,
)
ConstraintDefinition_strategy = st.builds(
    ConstraintDefinition,
)
TTMCConstraint::LiteralExpression_strategy = st.builds(
    TTMCConstraint::LiteralExpression,
)
TemporalExpression_strategy = st.builds(
    TemporalExpression,
)
TTMCConstraint::TemporalStateExpression_strategy = st.builds(
    TTMCConstraint::TemporalStateExpression,
)
TTMCConstraint::TemporalPathExpression_strategy = st.builds(
    TTMCConstraint::TemporalPathExpression,
)
TTMCConstraint::TemporalExpression_strategy = st.builds(
    TTMCConstraint::TemporalExpression,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
TTMCConstraint::PrimedExpression_strategy = st.builds(
    TTMCConstraint::PrimedExpression,
)
TTMCConstraint::InExpression_strategy = st.builds(
    TTMCConstraint::InExpression,
)
TTMCConstraint::GloballyExpression_strategy = st.builds(
    TTMCConstraint::GloballyExpression,
)
TTMCConstraint::NextExpression_strategy = st.builds(
    TTMCConstraint::NextExpression,
)
TTMCConstraint::TemporalExistsExpression_strategy = st.builds(
    TTMCConstraint::TemporalExistsExpression,
)
TTMCConstraint::TemporalForallExpression_strategy = st.builds(
    TTMCConstraint::TemporalForallExpression,
)
TTMCConstraint::FinallyExpression_strategy = st.builds(
    TTMCConstraint::FinallyExpression,
)
TTMCConstraint::NotExpression_strategy = st.builds(
    TTMCConstraint::NotExpression,
)
TTMCConstraint::BooleanExpression_strategy = st.builds(
    TTMCConstraint::BooleanExpression,
)
BasicTypeDefinition_strategy = st.builds(
    BasicTypeDefinition,
)
TTMCConstraint::NaturalTypeDefinition_strategy = st.builds(
    TTMCConstraint::NaturalTypeDefinition,
)
TTMCConstraint::RealTypeDefinition_strategy = st.builds(
    TTMCConstraint::RealTypeDefinition,
)
TTMCConstraint::BooleanTypeDefinition_strategy = st.builds(
    TTMCConstraint::BooleanTypeDefinition,
)
TTMCConstraint::IntegerTypeDefinition_strategy = st.builds(
    TTMCConstraint::IntegerTypeDefinition,
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
TTMCConstraint::SubrangeTypeDefinition_strategy = st.builds(
    TTMCConstraint::SubrangeTypeDefinition,
)
TTMCConstraint::EnumerationTypeDefinition_strategy = st.builds(
    TTMCConstraint::EnumerationTypeDefinition,
)
TTMCConstraint::BasicTypeDefinition_strategy = st.builds(
    TTMCConstraint::BasicTypeDefinition,
)
Type_strategy = st.builds(
    Type,
)
TTMCConstraint::TypeDefinition_strategy = st.builds(
    TTMCConstraint::TypeDefinition,
)
TTMCConstraint::TypeReference_strategy = st.builds(
    TTMCConstraint::TypeReference,
)
TTMCConstraint::ArrayTypeDefinition_strategy = st.builds(
    TTMCConstraint::ArrayTypeDefinition,
)
TTMCConstraint::FunctionTypeDefinition_strategy = st.builds(
    TTMCConstraint::FunctionTypeDefinition,
)
TTMCConstraint::BasicConstraintDefinition_strategy = st.builds(
    TTMCConstraint::BasicConstraintDefinition,
)
ParametricElement_strategy = st.builds(
    ParametricElement,
)
TTMCConstraint::SubTypeDefinition_strategy = st.builds(
    TTMCConstraint::SubTypeDefinition,
)
TTMCConstraint::QuantifierExpression_strategy = st.builds(
    TTMCConstraint::QuantifierExpression,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
TTMCConstraint::Declaration_strategy = st.builds(
    TTMCConstraint::Declaration,
)
TTMCConstraint::EnumerationLiteralDefinition_strategy = st.builds(
    TTMCConstraint::EnumerationLiteralDefinition,
)
TTMCConstraint::TypeDeclaration_strategy = st.builds(
    TTMCConstraint::TypeDeclaration,
)
TTMCConstraint::ConstraintSpecification_strategy = st.builds(
    TTMCConstraint::ConstraintSpecification,
)
TTMCConstraint::Expression_strategy = st.builds(
    TTMCConstraint::Expression,
)
TTMCConstraint::ParametrizedElement_strategy = st.builds(
    TTMCConstraint::ParametrizedElement,
)
TTMCConstraint::ParametricElement_strategy = st.builds(
    TTMCConstraint::ParametricElement,
)
TTMCConstraint::NamedElement_strategy = st.builds(
    TTMCConstraint::NamedElement,
    name=
        safe_text
)
DefinableDeclaration_strategy = st.builds(
    DefinableDeclaration,
)
TTMCConstraint::FunctionDeclaration_strategy = st.builds(
    TTMCConstraint::FunctionDeclaration,
)
TTMCConstraint::ConstantDeclaration_strategy = st.builds(
    TTMCConstraint::ConstantDeclaration,
)
TTMCConstraint::LetDeclaration_strategy = st.builds(
    TTMCConstraint::LetDeclaration,
)
Declaration_strategy = st.builds(
    Declaration,
)
TTMCConstraint::ParameterDeclaration_strategy = st.builds(
    TTMCConstraint::ParameterDeclaration,
)
TTMCConstraint::FieldDeclaration_strategy = st.builds(
    TTMCConstraint::FieldDeclaration,
)
TTMCConstraint::DefinableDeclaration_strategy = st.builds(
    TTMCConstraint::DefinableDeclaration,
)
TTMCConstraint::Type_strategy = st.builds(
    TTMCConstraint::Type,
)
TTMCConstraint::ConstraintDefinition_strategy = st.builds(
    TTMCConstraint::ConstraintDefinition,
)
TTMCConstraint::RecordTypeDefinition_strategy = st.builds(
    TTMCConstraint::RecordTypeDefinition,
)
TTMCConstraint::TupleTypeDefinition_strategy = st.builds(
    TTMCConstraint::TupleTypeDefinition,
)
ArithmeticExpression_strategy = st.builds(
    ArithmeticExpression,
)
TTMCConstraint::SubtractExpression_strategy = st.builds(
    TTMCConstraint::SubtractExpression,
)
TTMCConstraint::MultiplyExpression_strategy = st.builds(
    TTMCConstraint::MultiplyExpression,
)
TTMCConstraint::DivideExpression_strategy = st.builds(
    TTMCConstraint::DivideExpression,
)
TTMCConstraint::DivExpression_strategy = st.builds(
    TTMCConstraint::DivExpression,
)
TTMCConstraint::AddExpression_strategy = st.builds(
    TTMCConstraint::AddExpression,
)
TTMCConstraint::UnaryPlusExpression_strategy = st.builds(
    TTMCConstraint::UnaryPlusExpression,
)
TTMCConstraint::ModExpression_strategy = st.builds(
    TTMCConstraint::ModExpression,
)
TTMCConstraint::UnaryMinusExpression_strategy = st.builds(
    TTMCConstraint::UnaryMinusExpression,
)
LiteralExpression_strategy = st.builds(
    LiteralExpression,
)
TTMCConstraint::TupleLiteralExpression_strategy = st.builds(
    TTMCConstraint::TupleLiteralExpression,
)
TTMCConstraint::FunctionLiteralExpression_strategy = st.builds(
    TTMCConstraint::FunctionLiteralExpression,
)
TTMCConstraint::ArrayLiteralExpression_strategy = st.builds(
    TTMCConstraint::ArrayLiteralExpression,
)
TTMCConstraint::RecordLiteralExpression_strategy = st.builds(
    TTMCConstraint::RecordLiteralExpression,
)
NullaryExpression_strategy = st.builds(
    NullaryExpression,
)
TTMCConstraint::EnumerationLiteralExpression_strategy = st.builds(
    TTMCConstraint::EnumerationLiteralExpression,
)
TTMCConstraint::ReferenceExpression_strategy = st.builds(
    TTMCConstraint::ReferenceExpression,
)
TTMCConstraint::BooleanLiteralExpression_strategy = st.builds(
    TTMCConstraint::BooleanLiteralExpression,
)
TTMCConstraint::ArithmeticLiteralExpression_strategy = st.builds(
    TTMCConstraint::ArithmeticLiteralExpression,
)

@given(instance=ParametrizedElement_strategy)
@settings(max_examples=50)
def test_parametrizedelement_instantiation(instance):
    assert isinstance(instance, ParametrizedElement)

@given(instance=AccessExpression_strategy)
@settings(max_examples=50)
def test_accessexpression_instantiation(instance):
    assert isinstance(instance, AccessExpression)

@given(instance=TTMCConstraint::ArrayAccessExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::arrayaccessexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::ArrayAccessExpression)

@given(instance=TTMCConstraint::TupleAccessExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::tupleaccessexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::TupleAccessExpression)

@given(instance=TTMCConstraint::TupleAccessExpression_strategy)
def test_ttmcconstraint::tupleaccessexpression_index_type(instance):
    assert isinstance(instance.index, str)


@given(instance=TTMCConstraint::TupleAccessExpression_strategy)
def test_ttmcconstraint::tupleaccessexpression_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=TTMCConstraint::RecordAccessExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::recordaccessexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::RecordAccessExpression)

@given(instance=TTMCConstraint::RecordAccessExpression_strategy)
def test_ttmcconstraint::recordaccessexpression_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=TTMCConstraint::RecordAccessExpression_strategy)
def test_ttmcconstraint::recordaccessexpression_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=TTMCConstraint::FunctionAccessExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::functionaccessexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::FunctionAccessExpression)

@given(instance=EquivalenceExpression_strategy)
@settings(max_examples=50)
def test_equivalenceexpression_instantiation(instance):
    assert isinstance(instance, EquivalenceExpression)

@given(instance=TTMCConstraint::InequalityExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::inequalityexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::InequalityExpression)

@given(instance=TTMCConstraint::EqualityExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::equalityexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::EqualityExpression)

@given(instance=PredicateExpression_strategy)
@settings(max_examples=50)
def test_predicateexpression_instantiation(instance):
    assert isinstance(instance, PredicateExpression)

@given(instance=TemporalStateExpression_strategy)
@settings(max_examples=50)
def test_temporalstateexpression_instantiation(instance):
    assert isinstance(instance, TemporalStateExpression)

@given(instance=QuantifierExpression_strategy)
@settings(max_examples=50)
def test_quantifierexpression_instantiation(instance):
    assert isinstance(instance, QuantifierExpression)

@given(instance=TTMCConstraint::ExistsExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::existsexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::ExistsExpression)

@given(instance=TTMCConstraint::ForallExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::forallexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::ForallExpression)

@given(instance=TemporalPathExpression_strategy)
@settings(max_examples=50)
def test_temporalpathexpression_instantiation(instance):
    assert isinstance(instance, TemporalPathExpression)

@given(instance=MultiaryExpression_strategy)
@settings(max_examples=50)
def test_multiaryexpression_instantiation(instance):
    assert isinstance(instance, MultiaryExpression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=TTMCConstraint::EquivalenceExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::equivalenceexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::EquivalenceExpression)

@given(instance=TTMCConstraint::UntilExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::untilexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::UntilExpression)

@given(instance=TTMCConstraint::ReleaseExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::releaseexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::ReleaseExpression)

@given(instance=ComparisionExpression_strategy)
@settings(max_examples=50)
def test_comparisionexpression_instantiation(instance):
    assert isinstance(instance, ComparisionExpression)

@given(instance=TTMCConstraint::LessEqualExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::lessequalexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::LessEqualExpression)

@given(instance=TTMCConstraint::LessExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::lessexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::LessExpression)

@given(instance=TTMCConstraint::GreaterEqualExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::greaterequalexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::GreaterEqualExpression)

@given(instance=TTMCConstraint::GreaterExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::greaterexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::GreaterExpression)

@given(instance=TTMCConstraint::ComparisionExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::comparisionexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::ComparisionExpression)

@given(instance=TTMCConstraint::FieldAssignment_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::fieldassignment_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::FieldAssignment)

@given(instance=TTMCConstraint::FieldAssignment_strategy)
def test_ttmcconstraint::fieldassignment_reference_type(instance):
    assert isinstance(instance.reference, str)


@given(instance=TTMCConstraint::FieldAssignment_strategy)
def test_ttmcconstraint::fieldassignment_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=BooleanLiteralExpression_strategy)
@settings(max_examples=50)
def test_booleanliteralexpression_instantiation(instance):
    assert isinstance(instance, BooleanLiteralExpression)

@given(instance=TTMCConstraint::FalseExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::falseexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::FalseExpression)

@given(instance=TTMCConstraint::TrueExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::trueexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::TrueExpression)

@given(instance=BooleanExpression_strategy)
@settings(max_examples=50)
def test_booleanexpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)

@given(instance=TTMCConstraint::OrExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::orexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::OrExpression)

@given(instance=TTMCConstraint::ImplyExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::implyexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::ImplyExpression)

@given(instance=TTMCConstraint::EqualExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::equalexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::EqualExpression)

@given(instance=TTMCConstraint::AndExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::andexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::AndExpression)

@given(instance=ArithmeticLiteralExpression_strategy)
@settings(max_examples=50)
def test_arithmeticliteralexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticLiteralExpression)

@given(instance=TTMCConstraint::DecimalLiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::decimalliteralexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::DecimalLiteralExpression)

@given(instance=TTMCConstraint::DecimalLiteralExpression_strategy)
def test_ttmcconstraint::decimalliteralexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=TTMCConstraint::DecimalLiteralExpression_strategy)
def test_ttmcconstraint::decimalliteralexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=TTMCConstraint::RationalLiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::rationalliteralexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::RationalLiteralExpression)

@given(instance=TTMCConstraint::RationalLiteralExpression_strategy)
def test_ttmcconstraint::rationalliteralexpression_numerator_type(instance):
    assert isinstance(instance.numerator, str)


@given(instance=TTMCConstraint::RationalLiteralExpression_strategy)
def test_ttmcconstraint::rationalliteralexpression_numerator_setter(instance):
    original = instance.numerator
    instance.numerator = original
    assert instance.numerator == original

@given(instance=TTMCConstraint::RationalLiteralExpression_strategy)
def test_ttmcconstraint::rationalliteralexpression_denominator_type(instance):
    assert isinstance(instance.denominator, str)


@given(instance=TTMCConstraint::RationalLiteralExpression_strategy)
def test_ttmcconstraint::rationalliteralexpression_denominator_setter(instance):
    original = instance.denominator
    instance.denominator = original
    assert instance.denominator == original

@given(instance=TTMCConstraint::IntegerLiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::integerliteralexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::IntegerLiteralExpression)

@given(instance=TTMCConstraint::IntegerLiteralExpression_strategy)
def test_ttmcconstraint::integerliteralexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=TTMCConstraint::IntegerLiteralExpression_strategy)
def test_ttmcconstraint::integerliteralexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=TTMCConstraint::UnaryExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::unaryexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::UnaryExpression)

@given(instance=TTMCConstraint::AccessExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::accessexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::AccessExpression)

@given(instance=TTMCConstraint::PredicateExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::predicateexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::PredicateExpression)

@given(instance=TTMCConstraint::ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::arithmeticexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::ArithmeticExpression)

@given(instance=TTMCConstraint::BinaryExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::binaryexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::BinaryExpression)

@given(instance=TTMCConstraint::LetExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::letexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::LetExpression)

@given(instance=TTMCConstraint::IfThenElseExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::ifthenelseexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::IfThenElseExpression)

@given(instance=TTMCConstraint::MultiaryExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::multiaryexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::MultiaryExpression)

@given(instance=TTMCConstraint::NullaryExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::nullaryexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::NullaryExpression)

@given(instance=ConstraintDefinition_strategy)
@settings(max_examples=50)
def test_constraintdefinition_instantiation(instance):
    assert isinstance(instance, ConstraintDefinition)

@given(instance=TTMCConstraint::LiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::literalexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::LiteralExpression)

@given(instance=TemporalExpression_strategy)
@settings(max_examples=50)
def test_temporalexpression_instantiation(instance):
    assert isinstance(instance, TemporalExpression)

@given(instance=TTMCConstraint::TemporalStateExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::temporalstateexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::TemporalStateExpression)

@given(instance=TTMCConstraint::TemporalPathExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::temporalpathexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::TemporalPathExpression)

@given(instance=TTMCConstraint::TemporalExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::temporalexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::TemporalExpression)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=TTMCConstraint::PrimedExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::primedexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::PrimedExpression)

@given(instance=TTMCConstraint::InExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::inexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::InExpression)

@given(instance=TTMCConstraint::GloballyExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::globallyexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::GloballyExpression)

@given(instance=TTMCConstraint::NextExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::nextexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::NextExpression)

@given(instance=TTMCConstraint::TemporalExistsExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::temporalexistsexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::TemporalExistsExpression)

@given(instance=TTMCConstraint::TemporalForallExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::temporalforallexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::TemporalForallExpression)

@given(instance=TTMCConstraint::FinallyExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::finallyexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::FinallyExpression)

@given(instance=TTMCConstraint::NotExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::notexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::NotExpression)

@given(instance=TTMCConstraint::BooleanExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::booleanexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::BooleanExpression)

@given(instance=BasicTypeDefinition_strategy)
@settings(max_examples=50)
def test_basictypedefinition_instantiation(instance):
    assert isinstance(instance, BasicTypeDefinition)

@given(instance=TTMCConstraint::NaturalTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::naturaltypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::NaturalTypeDefinition)

@given(instance=TTMCConstraint::RealTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::realtypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::RealTypeDefinition)

@given(instance=TTMCConstraint::BooleanTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::booleantypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::BooleanTypeDefinition)

@given(instance=TTMCConstraint::IntegerTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::integertypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::IntegerTypeDefinition)

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=TTMCConstraint::SubrangeTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::subrangetypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::SubrangeTypeDefinition)

@given(instance=TTMCConstraint::EnumerationTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::enumerationtypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::EnumerationTypeDefinition)

@given(instance=TTMCConstraint::BasicTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::basictypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::BasicTypeDefinition)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=TTMCConstraint::TypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::typedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::TypeDefinition)

@given(instance=TTMCConstraint::TypeReference_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::typereference_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::TypeReference)

@given(instance=TTMCConstraint::ArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::arraytypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::ArrayTypeDefinition)

@given(instance=TTMCConstraint::FunctionTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::functiontypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::FunctionTypeDefinition)

@given(instance=TTMCConstraint::BasicConstraintDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::basicconstraintdefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::BasicConstraintDefinition)

@given(instance=ParametricElement_strategy)
@settings(max_examples=50)
def test_parametricelement_instantiation(instance):
    assert isinstance(instance, ParametricElement)

@given(instance=TTMCConstraint::SubTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::subtypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::SubTypeDefinition)

@given(instance=TTMCConstraint::QuantifierExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::quantifierexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::QuantifierExpression)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=TTMCConstraint::Declaration_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::declaration_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::Declaration)

@given(instance=TTMCConstraint::EnumerationLiteralDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::enumerationliteraldefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::EnumerationLiteralDefinition)

@given(instance=TTMCConstraint::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::typedeclaration_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::TypeDeclaration)

@given(instance=TTMCConstraint::ConstraintSpecification_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::constraintspecification_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::ConstraintSpecification)

@given(instance=TTMCConstraint::Expression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::expression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::Expression)

@given(instance=TTMCConstraint::ParametrizedElement_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::parametrizedelement_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::ParametrizedElement)

@given(instance=TTMCConstraint::ParametricElement_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::parametricelement_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::ParametricElement)

@given(instance=TTMCConstraint::NamedElement_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::namedelement_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::NamedElement)

@given(instance=TTMCConstraint::NamedElement_strategy)
def test_ttmcconstraint::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=TTMCConstraint::NamedElement_strategy)
def test_ttmcconstraint::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DefinableDeclaration_strategy)
@settings(max_examples=50)
def test_definabledeclaration_instantiation(instance):
    assert isinstance(instance, DefinableDeclaration)

@given(instance=TTMCConstraint::FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::functiondeclaration_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::FunctionDeclaration)

@given(instance=TTMCConstraint::ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::constantdeclaration_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::ConstantDeclaration)

@given(instance=TTMCConstraint::LetDeclaration_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::letdeclaration_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::LetDeclaration)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=TTMCConstraint::ParameterDeclaration_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::parameterdeclaration_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::ParameterDeclaration)

@given(instance=TTMCConstraint::FieldDeclaration_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::fielddeclaration_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::FieldDeclaration)

@given(instance=TTMCConstraint::DefinableDeclaration_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::definabledeclaration_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::DefinableDeclaration)

@given(instance=TTMCConstraint::Type_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::type_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::Type)

@given(instance=TTMCConstraint::ConstraintDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::constraintdefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::ConstraintDefinition)

@given(instance=TTMCConstraint::RecordTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::recordtypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::RecordTypeDefinition)

@given(instance=TTMCConstraint::TupleTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::tupletypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::TupleTypeDefinition)

@given(instance=ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticExpression)

@given(instance=TTMCConstraint::SubtractExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::subtractexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::SubtractExpression)

@given(instance=TTMCConstraint::MultiplyExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::multiplyexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::MultiplyExpression)

@given(instance=TTMCConstraint::DivideExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::divideexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::DivideExpression)

@given(instance=TTMCConstraint::DivExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::divexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::DivExpression)

@given(instance=TTMCConstraint::AddExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::addexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::AddExpression)

@given(instance=TTMCConstraint::UnaryPlusExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::unaryplusexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::UnaryPlusExpression)

@given(instance=TTMCConstraint::ModExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::modexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::ModExpression)

@given(instance=TTMCConstraint::UnaryMinusExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::unaryminusexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::UnaryMinusExpression)

@given(instance=LiteralExpression_strategy)
@settings(max_examples=50)
def test_literalexpression_instantiation(instance):
    assert isinstance(instance, LiteralExpression)

@given(instance=TTMCConstraint::TupleLiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::tupleliteralexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::TupleLiteralExpression)

@given(instance=TTMCConstraint::FunctionLiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::functionliteralexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::FunctionLiteralExpression)

@given(instance=TTMCConstraint::ArrayLiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::arrayliteralexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::ArrayLiteralExpression)

@given(instance=TTMCConstraint::RecordLiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::recordliteralexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::RecordLiteralExpression)

@given(instance=NullaryExpression_strategy)
@settings(max_examples=50)
def test_nullaryexpression_instantiation(instance):
    assert isinstance(instance, NullaryExpression)

@given(instance=TTMCConstraint::EnumerationLiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::enumerationliteralexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::EnumerationLiteralExpression)

@given(instance=TTMCConstraint::ReferenceExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::referenceexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::ReferenceExpression)

@given(instance=TTMCConstraint::BooleanLiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::booleanliteralexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::BooleanLiteralExpression)

@given(instance=TTMCConstraint::ArithmeticLiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint::arithmeticliteralexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint::ArithmeticLiteralExpression)
