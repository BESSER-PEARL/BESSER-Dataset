import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OrderedCollection,
    eol::expression::SequenceExpression,
    eol::expression::Statement,
    CollectionInitialisationExpression,
    eol::expression::ExpressionList,
    eol::expression::ExpressionRange,
    UniqueCollection,
    eol::expression::OrderedSetExpression,
    eol::expression::SetExpression,
    CollectionExpression,
    eol::expression::UniqueCollection,
    eol::expression::OrderedCollection,
    eol::expression::BagExpression,
    SummableExpression,
    ComparableExpression,
    eol::expression::RealExpression,
    eol::expression::IntegerExpression,
    eol::expression::StringExpression,
    PrimitiveExpression,
    eol::expression::BooleanExpression,
    eol::expression::SummableExpression,
    eol::expression::ComparableExpression,
    ArithmeticOperatorExpression,
    eol::expression::MultiplyOperatorExpression,
    eol::expression::MinusOperatorExpression,
    eol::expression::DivideOperatorExpression,
    FeatureCallExpression,
    eol::expression::PropertyCallExpression,
    eol::expression::FOLMethodCallExpression,
    eol::expression::MethodCallExpression,
    VariableDeclarationExpression,
    eol::expression::FormalParameterExpression,
    ComparisonOperatorExpression,
    eol::expression::LessThanOperatorExpression,
    eol::expression::EqualsOperatorExpression,
    eol::expression::LessThanOrEqualToOperatorExpression,
    eol::expression::NotEqualsOperatorExpression,
    eol::expression::GreaterThanOperatorExpression,
    eol::expression::GreaterThanOrEqualToOperatorExpression,
    eol::expression::PlusOperatorExpression,
    LogicalOperatorExpression,
    eol::expression::XorOperatorExpression,
    eol::expression::ImpliesOperatorExpression,
    eol::expression::OrOperatorExpression,
    eol::expression::AndOperatorExpression,
    BinaryOperatorExpression,
    eol::expression::ComparisonOperatorExpression,
    eol::expression::ArithmeticOperatorExpression,
    eol::expression::LogicalOperatorExpression,
    UnaryOperatorExpression,
    eol::expression::NegativeOperatorExpression,
    eol::expression::NotOperatorExpression,
    OperatorExpression,
    eol::expression::BinaryOperatorExpression,
    eol::expression::UnaryOperatorExpression,
    Expression,
    eol::expression::FeatureCallExpression,
    eol::expression::CollectionExpression,
    eol::expression::MapExpression,
    eol::expression::KeyValueExpression,
    eol::expression::NewExpression,
    eol::expression::NameExpression,
    eol::expression::EnumerationLiteralExpression,
    eol::expression::VariableDeclarationExpression,
    eol::expression::PrimitiveExpression,
    eol::expression::CollectionInitialisationExpression,
    eol::expression::OperatorExpression,
    eol::expression::Type,
    eol::expression::Expression,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_orderedcollection_is_not_abstract():
    assert not inspect.isabstract(OrderedCollection)


def test_orderedcollection_constructor_exists():
    assert callable(OrderedCollection.__init__)


def test_orderedcollection_constructor_args():
    sig = inspect.signature(OrderedCollection.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::sequenceexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::SequenceExpression)


def test_eol::expression::sequenceexpression_constructor_exists():
    assert callable(eol::expression::SequenceExpression.__init__)


def test_eol::expression::sequenceexpression_constructor_args():
    sig = inspect.signature(eol::expression::SequenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::statement_is_not_abstract():
    assert not inspect.isabstract(eol::expression::Statement)


def test_eol::expression::statement_constructor_exists():
    assert callable(eol::expression::Statement.__init__)


def test_eol::expression::statement_constructor_args():
    sig = inspect.signature(eol::expression::Statement.__init__)
    params = list(sig.parameters.keys())



def test_collectioninitialisationexpression_is_not_abstract():
    assert not inspect.isabstract(CollectionInitialisationExpression)


def test_collectioninitialisationexpression_constructor_exists():
    assert callable(CollectionInitialisationExpression.__init__)


def test_collectioninitialisationexpression_constructor_args():
    sig = inspect.signature(CollectionInitialisationExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::expressionlist_is_not_abstract():
    assert not inspect.isabstract(eol::expression::ExpressionList)


def test_eol::expression::expressionlist_constructor_exists():
    assert callable(eol::expression::ExpressionList.__init__)


def test_eol::expression::expressionlist_constructor_args():
    sig = inspect.signature(eol::expression::ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::expressionrange_is_not_abstract():
    assert not inspect.isabstract(eol::expression::ExpressionRange)


def test_eol::expression::expressionrange_constructor_exists():
    assert callable(eol::expression::ExpressionRange.__init__)


def test_eol::expression::expressionrange_constructor_args():
    sig = inspect.signature(eol::expression::ExpressionRange.__init__)
    params = list(sig.parameters.keys())



def test_uniquecollection_is_not_abstract():
    assert not inspect.isabstract(UniqueCollection)


def test_uniquecollection_constructor_exists():
    assert callable(UniqueCollection.__init__)


def test_uniquecollection_constructor_args():
    sig = inspect.signature(UniqueCollection.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::orderedsetexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::OrderedSetExpression)


def test_eol::expression::orderedsetexpression_constructor_exists():
    assert callable(eol::expression::OrderedSetExpression.__init__)


def test_eol::expression::orderedsetexpression_constructor_args():
    sig = inspect.signature(eol::expression::OrderedSetExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::setexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::SetExpression)


def test_eol::expression::setexpression_constructor_exists():
    assert callable(eol::expression::SetExpression.__init__)


def test_eol::expression::setexpression_constructor_args():
    sig = inspect.signature(eol::expression::SetExpression.__init__)
    params = list(sig.parameters.keys())



def test_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(CollectionExpression)


def test_collectionexpression_constructor_exists():
    assert callable(CollectionExpression.__init__)


def test_collectionexpression_constructor_args():
    sig = inspect.signature(CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::uniquecollection_is_not_abstract():
    assert not inspect.isabstract(eol::expression::UniqueCollection)


def test_eol::expression::uniquecollection_constructor_exists():
    assert callable(eol::expression::UniqueCollection.__init__)


def test_eol::expression::uniquecollection_constructor_args():
    sig = inspect.signature(eol::expression::UniqueCollection.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::orderedcollection_is_not_abstract():
    assert not inspect.isabstract(eol::expression::OrderedCollection)


def test_eol::expression::orderedcollection_constructor_exists():
    assert callable(eol::expression::OrderedCollection.__init__)


def test_eol::expression::orderedcollection_constructor_args():
    sig = inspect.signature(eol::expression::OrderedCollection.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::bagexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::BagExpression)


def test_eol::expression::bagexpression_constructor_exists():
    assert callable(eol::expression::BagExpression.__init__)


def test_eol::expression::bagexpression_constructor_args():
    sig = inspect.signature(eol::expression::BagExpression.__init__)
    params = list(sig.parameters.keys())



def test_summableexpression_is_not_abstract():
    assert not inspect.isabstract(SummableExpression)


def test_summableexpression_constructor_exists():
    assert callable(SummableExpression.__init__)


def test_summableexpression_constructor_args():
    sig = inspect.signature(SummableExpression.__init__)
    params = list(sig.parameters.keys())



def test_comparableexpression_is_not_abstract():
    assert not inspect.isabstract(ComparableExpression)


def test_comparableexpression_constructor_exists():
    assert callable(ComparableExpression.__init__)


def test_comparableexpression_constructor_args():
    sig = inspect.signature(ComparableExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::realexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::RealExpression)


def test_eol::expression::realexpression_constructor_exists():
    assert callable(eol::expression::RealExpression.__init__)


def test_eol::expression::realexpression_constructor_args():
    sig = inspect.signature(eol::expression::RealExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_eol::expression::realexpression_has_value():
    assert hasattr(eol::expression::RealExpression, "value")
    descriptor = None
    for klass in eol::expression::RealExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_eol::expression::integerexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::IntegerExpression)


def test_eol::expression::integerexpression_constructor_exists():
    assert callable(eol::expression::IntegerExpression.__init__)


def test_eol::expression::integerexpression_constructor_args():
    sig = inspect.signature(eol::expression::IntegerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_eol::expression::integerexpression_has_value():
    assert hasattr(eol::expression::IntegerExpression, "value")
    descriptor = None
    for klass in eol::expression::IntegerExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_eol::expression::stringexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::StringExpression)


def test_eol::expression::stringexpression_constructor_exists():
    assert callable(eol::expression::StringExpression.__init__)


def test_eol::expression::stringexpression_constructor_args():
    sig = inspect.signature(eol::expression::StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_eol::expression::stringexpression_has_value():
    assert hasattr(eol::expression::StringExpression, "value")
    descriptor = None
    for klass in eol::expression::StringExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExpression)


def test_primitiveexpression_constructor_exists():
    assert callable(PrimitiveExpression.__init__)


def test_primitiveexpression_constructor_args():
    sig = inspect.signature(PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::BooleanExpression)


def test_eol::expression::booleanexpression_constructor_exists():
    assert callable(eol::expression::BooleanExpression.__init__)


def test_eol::expression::booleanexpression_constructor_args():
    sig = inspect.signature(eol::expression::BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_eol::expression::booleanexpression_has_value():
    assert hasattr(eol::expression::BooleanExpression, "value")
    descriptor = None
    for klass in eol::expression::BooleanExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_eol::expression::summableexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::SummableExpression)


def test_eol::expression::summableexpression_constructor_exists():
    assert callable(eol::expression::SummableExpression.__init__)


def test_eol::expression::summableexpression_constructor_args():
    sig = inspect.signature(eol::expression::SummableExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::comparableexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::ComparableExpression)


def test_eol::expression::comparableexpression_constructor_exists():
    assert callable(eol::expression::ComparableExpression.__init__)


def test_eol::expression::comparableexpression_constructor_args():
    sig = inspect.signature(eol::expression::ComparableExpression.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticOperatorExpression)


def test_arithmeticoperatorexpression_constructor_exists():
    assert callable(ArithmeticOperatorExpression.__init__)


def test_arithmeticoperatorexpression_constructor_args():
    sig = inspect.signature(ArithmeticOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::multiplyoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::MultiplyOperatorExpression)


def test_eol::expression::multiplyoperatorexpression_constructor_exists():
    assert callable(eol::expression::MultiplyOperatorExpression.__init__)


def test_eol::expression::multiplyoperatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::MultiplyOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::minusoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::MinusOperatorExpression)


def test_eol::expression::minusoperatorexpression_constructor_exists():
    assert callable(eol::expression::MinusOperatorExpression.__init__)


def test_eol::expression::minusoperatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::MinusOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::divideoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::DivideOperatorExpression)


def test_eol::expression::divideoperatorexpression_constructor_exists():
    assert callable(eol::expression::DivideOperatorExpression.__init__)


def test_eol::expression::divideoperatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::DivideOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_featurecallexpression_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExpression)


def test_featurecallexpression_constructor_exists():
    assert callable(FeatureCallExpression.__init__)


def test_featurecallexpression_constructor_args():
    sig = inspect.signature(FeatureCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::propertycallexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::PropertyCallExpression)


def test_eol::expression::propertycallexpression_constructor_exists():
    assert callable(eol::expression::PropertyCallExpression.__init__)


def test_eol::expression::propertycallexpression_constructor_args():
    sig = inspect.signature(eol::expression::PropertyCallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "extended" in params, "Missing parameter 'extended'"

def test_eol::expression::propertycallexpression_has_extended():
    assert hasattr(eol::expression::PropertyCallExpression, "extended")
    descriptor = None
    for klass in eol::expression::PropertyCallExpression.__mro__:
        if "extended" in klass.__dict__:
            descriptor = klass.__dict__["extended"]
            break
    assert isinstance(descriptor, property)



def test_eol::expression::folmethodcallexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::FOLMethodCallExpression)


def test_eol::expression::folmethodcallexpression_constructor_exists():
    assert callable(eol::expression::FOLMethodCallExpression.__init__)


def test_eol::expression::folmethodcallexpression_constructor_args():
    sig = inspect.signature(eol::expression::FOLMethodCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::methodcallexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::MethodCallExpression)


def test_eol::expression::methodcallexpression_constructor_exists():
    assert callable(eol::expression::MethodCallExpression.__init__)


def test_eol::expression::methodcallexpression_constructor_args():
    sig = inspect.signature(eol::expression::MethodCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(VariableDeclarationExpression)


def test_variabledeclarationexpression_constructor_exists():
    assert callable(VariableDeclarationExpression.__init__)


def test_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::formalparameterexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::FormalParameterExpression)


def test_eol::expression::formalparameterexpression_constructor_exists():
    assert callable(eol::expression::FormalParameterExpression.__init__)


def test_eol::expression::formalparameterexpression_constructor_args():
    sig = inspect.signature(eol::expression::FormalParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_comparisonoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(ComparisonOperatorExpression)


def test_comparisonoperatorexpression_constructor_exists():
    assert callable(ComparisonOperatorExpression.__init__)


def test_comparisonoperatorexpression_constructor_args():
    sig = inspect.signature(ComparisonOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::lessthanoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::LessThanOperatorExpression)


def test_eol::expression::lessthanoperatorexpression_constructor_exists():
    assert callable(eol::expression::LessThanOperatorExpression.__init__)


def test_eol::expression::lessthanoperatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::LessThanOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::equalsoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::EqualsOperatorExpression)


def test_eol::expression::equalsoperatorexpression_constructor_exists():
    assert callable(eol::expression::EqualsOperatorExpression.__init__)


def test_eol::expression::equalsoperatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::EqualsOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::lessthanorequaltooperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::LessThanOrEqualToOperatorExpression)


def test_eol::expression::lessthanorequaltooperatorexpression_constructor_exists():
    assert callable(eol::expression::LessThanOrEqualToOperatorExpression.__init__)


def test_eol::expression::lessthanorequaltooperatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::LessThanOrEqualToOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::notequalsoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::NotEqualsOperatorExpression)


def test_eol::expression::notequalsoperatorexpression_constructor_exists():
    assert callable(eol::expression::NotEqualsOperatorExpression.__init__)


def test_eol::expression::notequalsoperatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::NotEqualsOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::greaterthanoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::GreaterThanOperatorExpression)


def test_eol::expression::greaterthanoperatorexpression_constructor_exists():
    assert callable(eol::expression::GreaterThanOperatorExpression.__init__)


def test_eol::expression::greaterthanoperatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::GreaterThanOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::greaterthanorequaltooperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::GreaterThanOrEqualToOperatorExpression)


def test_eol::expression::greaterthanorequaltooperatorexpression_constructor_exists():
    assert callable(eol::expression::GreaterThanOrEqualToOperatorExpression.__init__)


def test_eol::expression::greaterthanorequaltooperatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::GreaterThanOrEqualToOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::plusoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::PlusOperatorExpression)


def test_eol::expression::plusoperatorexpression_constructor_exists():
    assert callable(eol::expression::PlusOperatorExpression.__init__)


def test_eol::expression::plusoperatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::PlusOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_logicaloperatorexpression_is_not_abstract():
    assert not inspect.isabstract(LogicalOperatorExpression)


def test_logicaloperatorexpression_constructor_exists():
    assert callable(LogicalOperatorExpression.__init__)


def test_logicaloperatorexpression_constructor_args():
    sig = inspect.signature(LogicalOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::xoroperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::XorOperatorExpression)


def test_eol::expression::xoroperatorexpression_constructor_exists():
    assert callable(eol::expression::XorOperatorExpression.__init__)


def test_eol::expression::xoroperatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::XorOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::impliesoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::ImpliesOperatorExpression)


def test_eol::expression::impliesoperatorexpression_constructor_exists():
    assert callable(eol::expression::ImpliesOperatorExpression.__init__)


def test_eol::expression::impliesoperatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::ImpliesOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::oroperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::OrOperatorExpression)


def test_eol::expression::oroperatorexpression_constructor_exists():
    assert callable(eol::expression::OrOperatorExpression.__init__)


def test_eol::expression::oroperatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::OrOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::andoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::AndOperatorExpression)


def test_eol::expression::andoperatorexpression_constructor_exists():
    assert callable(eol::expression::AndOperatorExpression.__init__)


def test_eol::expression::andoperatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::AndOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryOperatorExpression)


def test_binaryoperatorexpression_constructor_exists():
    assert callable(BinaryOperatorExpression.__init__)


def test_binaryoperatorexpression_constructor_args():
    sig = inspect.signature(BinaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::comparisonoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::ComparisonOperatorExpression)


def test_eol::expression::comparisonoperatorexpression_constructor_exists():
    assert callable(eol::expression::ComparisonOperatorExpression.__init__)


def test_eol::expression::comparisonoperatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::ComparisonOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::arithmeticoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::ArithmeticOperatorExpression)


def test_eol::expression::arithmeticoperatorexpression_constructor_exists():
    assert callable(eol::expression::ArithmeticOperatorExpression.__init__)


def test_eol::expression::arithmeticoperatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::ArithmeticOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::logicaloperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::LogicalOperatorExpression)


def test_eol::expression::logicaloperatorexpression_constructor_exists():
    assert callable(eol::expression::LogicalOperatorExpression.__init__)


def test_eol::expression::logicaloperatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::LogicalOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryOperatorExpression)


def test_unaryoperatorexpression_constructor_exists():
    assert callable(UnaryOperatorExpression.__init__)


def test_unaryoperatorexpression_constructor_args():
    sig = inspect.signature(UnaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::negativeoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::NegativeOperatorExpression)


def test_eol::expression::negativeoperatorexpression_constructor_exists():
    assert callable(eol::expression::NegativeOperatorExpression.__init__)


def test_eol::expression::negativeoperatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::NegativeOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::notoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::NotOperatorExpression)


def test_eol::expression::notoperatorexpression_constructor_exists():
    assert callable(eol::expression::NotOperatorExpression.__init__)


def test_eol::expression::notoperatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::NotOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(OperatorExpression)


def test_operatorexpression_constructor_exists():
    assert callable(OperatorExpression.__init__)


def test_operatorexpression_constructor_args():
    sig = inspect.signature(OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::binaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::BinaryOperatorExpression)


def test_eol::expression::binaryoperatorexpression_constructor_exists():
    assert callable(eol::expression::BinaryOperatorExpression.__init__)


def test_eol::expression::binaryoperatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::BinaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::unaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::UnaryOperatorExpression)


def test_eol::expression::unaryoperatorexpression_constructor_exists():
    assert callable(eol::expression::UnaryOperatorExpression.__init__)


def test_eol::expression::unaryoperatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::UnaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::featurecallexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::FeatureCallExpression)


def test_eol::expression::featurecallexpression_constructor_exists():
    assert callable(eol::expression::FeatureCallExpression.__init__)


def test_eol::expression::featurecallexpression_constructor_args():
    sig = inspect.signature(eol::expression::FeatureCallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "arrow" in params, "Missing parameter 'arrow'"

def test_eol::expression::featurecallexpression_has_arrow():
    assert hasattr(eol::expression::FeatureCallExpression, "arrow")
    descriptor = None
    for klass in eol::expression::FeatureCallExpression.__mro__:
        if "arrow" in klass.__dict__:
            descriptor = klass.__dict__["arrow"]
            break
    assert isinstance(descriptor, property)



def test_eol::expression::collectionexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::CollectionExpression)


def test_eol::expression::collectionexpression_constructor_exists():
    assert callable(eol::expression::CollectionExpression.__init__)


def test_eol::expression::collectionexpression_constructor_args():
    sig = inspect.signature(eol::expression::CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::mapexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::MapExpression)


def test_eol::expression::mapexpression_constructor_exists():
    assert callable(eol::expression::MapExpression.__init__)


def test_eol::expression::mapexpression_constructor_args():
    sig = inspect.signature(eol::expression::MapExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::keyvalueexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::KeyValueExpression)


def test_eol::expression::keyvalueexpression_constructor_exists():
    assert callable(eol::expression::KeyValueExpression.__init__)


def test_eol::expression::keyvalueexpression_constructor_args():
    sig = inspect.signature(eol::expression::KeyValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::newexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::NewExpression)


def test_eol::expression::newexpression_constructor_exists():
    assert callable(eol::expression::NewExpression.__init__)


def test_eol::expression::newexpression_constructor_args():
    sig = inspect.signature(eol::expression::NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::nameexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::NameExpression)


def test_eol::expression::nameexpression_constructor_exists():
    assert callable(eol::expression::NameExpression.__init__)


def test_eol::expression::nameexpression_constructor_args():
    sig = inspect.signature(eol::expression::NameExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isType" in params, "Missing parameter 'isType'"

def test_eol::expression::nameexpression_has_name():
    assert hasattr(eol::expression::NameExpression, "name")
    descriptor = None
    for klass in eol::expression::NameExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_eol::expression::nameexpression_has_isType():
    assert hasattr(eol::expression::NameExpression, "isType")
    descriptor = None
    for klass in eol::expression::NameExpression.__mro__:
        if "isType" in klass.__dict__:
            descriptor = klass.__dict__["isType"]
            break
    assert isinstance(descriptor, property)



def test_eol::expression::enumerationliteralexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::EnumerationLiteralExpression)


def test_eol::expression::enumerationliteralexpression_constructor_exists():
    assert callable(eol::expression::EnumerationLiteralExpression.__init__)


def test_eol::expression::enumerationliteralexpression_constructor_args():
    sig = inspect.signature(eol::expression::EnumerationLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::VariableDeclarationExpression)


def test_eol::expression::variabledeclarationexpression_constructor_exists():
    assert callable(eol::expression::VariableDeclarationExpression.__init__)


def test_eol::expression::variabledeclarationexpression_constructor_args():
    sig = inspect.signature(eol::expression::VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "create" in params, "Missing parameter 'create'"

def test_eol::expression::variabledeclarationexpression_has_create():
    assert hasattr(eol::expression::VariableDeclarationExpression, "create")
    descriptor = None
    for klass in eol::expression::VariableDeclarationExpression.__mro__:
        if "create" in klass.__dict__:
            descriptor = klass.__dict__["create"]
            break
    assert isinstance(descriptor, property)



def test_eol::expression::primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::PrimitiveExpression)


def test_eol::expression::primitiveexpression_constructor_exists():
    assert callable(eol::expression::PrimitiveExpression.__init__)


def test_eol::expression::primitiveexpression_constructor_args():
    sig = inspect.signature(eol::expression::PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::collectioninitialisationexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::CollectionInitialisationExpression)


def test_eol::expression::collectioninitialisationexpression_constructor_exists():
    assert callable(eol::expression::CollectionInitialisationExpression.__init__)


def test_eol::expression::collectioninitialisationexpression_constructor_args():
    sig = inspect.signature(eol::expression::CollectionInitialisationExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::operatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::OperatorExpression)


def test_eol::expression::operatorexpression_constructor_exists():
    assert callable(eol::expression::OperatorExpression.__init__)


def test_eol::expression::operatorexpression_constructor_args():
    sig = inspect.signature(eol::expression::OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::type_is_not_abstract():
    assert not inspect.isabstract(eol::expression::Type)


def test_eol::expression::type_constructor_exists():
    assert callable(eol::expression::Type.__init__)


def test_eol::expression::type_constructor_args():
    sig = inspect.signature(eol::expression::Type.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression::expression_is_not_abstract():
    assert not inspect.isabstract(eol::expression::Expression)


def test_eol::expression::expression_constructor_exists():
    assert callable(eol::expression::Expression.__init__)


def test_eol::expression::expression_constructor_args():
    sig = inspect.signature(eol::expression::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "inBrackets" in params, "Missing parameter 'inBrackets'"

def test_eol::expression::expression_has_inBrackets():
    assert hasattr(eol::expression::Expression, "inBrackets")
    descriptor = None
    for klass in eol::expression::Expression.__mro__:
        if "inBrackets" in klass.__dict__:
            descriptor = klass.__dict__["inBrackets"]
            break
    assert isinstance(descriptor, property)


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
OrderedCollection_strategy = st.builds(
    OrderedCollection,
)
eol::expression::SequenceExpression_strategy = st.builds(
    eol::expression::SequenceExpression,
)
eol::expression::Statement_strategy = st.builds(
    eol::expression::Statement,
)
CollectionInitialisationExpression_strategy = st.builds(
    CollectionInitialisationExpression,
)
eol::expression::ExpressionList_strategy = st.builds(
    eol::expression::ExpressionList,
)
eol::expression::ExpressionRange_strategy = st.builds(
    eol::expression::ExpressionRange,
)
UniqueCollection_strategy = st.builds(
    UniqueCollection,
)
eol::expression::OrderedSetExpression_strategy = st.builds(
    eol::expression::OrderedSetExpression,
)
eol::expression::SetExpression_strategy = st.builds(
    eol::expression::SetExpression,
)
CollectionExpression_strategy = st.builds(
    CollectionExpression,
)
eol::expression::UniqueCollection_strategy = st.builds(
    eol::expression::UniqueCollection,
)
eol::expression::OrderedCollection_strategy = st.builds(
    eol::expression::OrderedCollection,
)
eol::expression::BagExpression_strategy = st.builds(
    eol::expression::BagExpression,
)
SummableExpression_strategy = st.builds(
    SummableExpression,
)
ComparableExpression_strategy = st.builds(
    ComparableExpression,
)
eol::expression::RealExpression_strategy = st.builds(
    eol::expression::RealExpression,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eol::expression::IntegerExpression_strategy = st.builds(
    eol::expression::IntegerExpression,
    value=
        st.integers()
)
eol::expression::StringExpression_strategy = st.builds(
    eol::expression::StringExpression,
    value=
        safe_text
)
PrimitiveExpression_strategy = st.builds(
    PrimitiveExpression,
)
eol::expression::BooleanExpression_strategy = st.builds(
    eol::expression::BooleanExpression,
    value=
        st.booleans()
)
eol::expression::SummableExpression_strategy = st.builds(
    eol::expression::SummableExpression,
)
eol::expression::ComparableExpression_strategy = st.builds(
    eol::expression::ComparableExpression,
)
ArithmeticOperatorExpression_strategy = st.builds(
    ArithmeticOperatorExpression,
)
eol::expression::MultiplyOperatorExpression_strategy = st.builds(
    eol::expression::MultiplyOperatorExpression,
)
eol::expression::MinusOperatorExpression_strategy = st.builds(
    eol::expression::MinusOperatorExpression,
)
eol::expression::DivideOperatorExpression_strategy = st.builds(
    eol::expression::DivideOperatorExpression,
)
FeatureCallExpression_strategy = st.builds(
    FeatureCallExpression,
)
eol::expression::PropertyCallExpression_strategy = st.builds(
    eol::expression::PropertyCallExpression,
    extended=
        st.booleans()
)
eol::expression::FOLMethodCallExpression_strategy = st.builds(
    eol::expression::FOLMethodCallExpression,
)
eol::expression::MethodCallExpression_strategy = st.builds(
    eol::expression::MethodCallExpression,
)
VariableDeclarationExpression_strategy = st.builds(
    VariableDeclarationExpression,
)
eol::expression::FormalParameterExpression_strategy = st.builds(
    eol::expression::FormalParameterExpression,
)
ComparisonOperatorExpression_strategy = st.builds(
    ComparisonOperatorExpression,
)
eol::expression::LessThanOperatorExpression_strategy = st.builds(
    eol::expression::LessThanOperatorExpression,
)
eol::expression::EqualsOperatorExpression_strategy = st.builds(
    eol::expression::EqualsOperatorExpression,
)
eol::expression::LessThanOrEqualToOperatorExpression_strategy = st.builds(
    eol::expression::LessThanOrEqualToOperatorExpression,
)
eol::expression::NotEqualsOperatorExpression_strategy = st.builds(
    eol::expression::NotEqualsOperatorExpression,
)
eol::expression::GreaterThanOperatorExpression_strategy = st.builds(
    eol::expression::GreaterThanOperatorExpression,
)
eol::expression::GreaterThanOrEqualToOperatorExpression_strategy = st.builds(
    eol::expression::GreaterThanOrEqualToOperatorExpression,
)
eol::expression::PlusOperatorExpression_strategy = st.builds(
    eol::expression::PlusOperatorExpression,
)
LogicalOperatorExpression_strategy = st.builds(
    LogicalOperatorExpression,
)
eol::expression::XorOperatorExpression_strategy = st.builds(
    eol::expression::XorOperatorExpression,
)
eol::expression::ImpliesOperatorExpression_strategy = st.builds(
    eol::expression::ImpliesOperatorExpression,
)
eol::expression::OrOperatorExpression_strategy = st.builds(
    eol::expression::OrOperatorExpression,
)
eol::expression::AndOperatorExpression_strategy = st.builds(
    eol::expression::AndOperatorExpression,
)
BinaryOperatorExpression_strategy = st.builds(
    BinaryOperatorExpression,
)
eol::expression::ComparisonOperatorExpression_strategy = st.builds(
    eol::expression::ComparisonOperatorExpression,
)
eol::expression::ArithmeticOperatorExpression_strategy = st.builds(
    eol::expression::ArithmeticOperatorExpression,
)
eol::expression::LogicalOperatorExpression_strategy = st.builds(
    eol::expression::LogicalOperatorExpression,
)
UnaryOperatorExpression_strategy = st.builds(
    UnaryOperatorExpression,
)
eol::expression::NegativeOperatorExpression_strategy = st.builds(
    eol::expression::NegativeOperatorExpression,
)
eol::expression::NotOperatorExpression_strategy = st.builds(
    eol::expression::NotOperatorExpression,
)
OperatorExpression_strategy = st.builds(
    OperatorExpression,
)
eol::expression::BinaryOperatorExpression_strategy = st.builds(
    eol::expression::BinaryOperatorExpression,
)
eol::expression::UnaryOperatorExpression_strategy = st.builds(
    eol::expression::UnaryOperatorExpression,
)
Expression_strategy = st.builds(
    Expression,
)
eol::expression::FeatureCallExpression_strategy = st.builds(
    eol::expression::FeatureCallExpression,
    arrow=
        st.booleans()
)
eol::expression::CollectionExpression_strategy = st.builds(
    eol::expression::CollectionExpression,
)
eol::expression::MapExpression_strategy = st.builds(
    eol::expression::MapExpression,
)
eol::expression::KeyValueExpression_strategy = st.builds(
    eol::expression::KeyValueExpression,
)
eol::expression::NewExpression_strategy = st.builds(
    eol::expression::NewExpression,
)
eol::expression::NameExpression_strategy = st.builds(
    eol::expression::NameExpression,
    name=
        safe_text,
    isType=
        st.booleans()
)
eol::expression::EnumerationLiteralExpression_strategy = st.builds(
    eol::expression::EnumerationLiteralExpression,
)
eol::expression::VariableDeclarationExpression_strategy = st.builds(
    eol::expression::VariableDeclarationExpression,
    create=
        st.booleans()
)
eol::expression::PrimitiveExpression_strategy = st.builds(
    eol::expression::PrimitiveExpression,
)
eol::expression::CollectionInitialisationExpression_strategy = st.builds(
    eol::expression::CollectionInitialisationExpression,
)
eol::expression::OperatorExpression_strategy = st.builds(
    eol::expression::OperatorExpression,
)
eol::expression::Type_strategy = st.builds(
    eol::expression::Type,
)
eol::expression::Expression_strategy = st.builds(
    eol::expression::Expression,
    inBrackets=
        st.booleans()
)

@given(instance=OrderedCollection_strategy)
@settings(max_examples=50)
def test_orderedcollection_instantiation(instance):
    assert isinstance(instance, OrderedCollection)

@given(instance=eol::expression::SequenceExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::sequenceexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::SequenceExpression)

@given(instance=eol::expression::Statement_strategy)
@settings(max_examples=50)
def test_eol::expression::statement_instantiation(instance):
    assert isinstance(instance, eol::expression::Statement)

@given(instance=CollectionInitialisationExpression_strategy)
@settings(max_examples=50)
def test_collectioninitialisationexpression_instantiation(instance):
    assert isinstance(instance, CollectionInitialisationExpression)

@given(instance=eol::expression::ExpressionList_strategy)
@settings(max_examples=50)
def test_eol::expression::expressionlist_instantiation(instance):
    assert isinstance(instance, eol::expression::ExpressionList)

@given(instance=eol::expression::ExpressionRange_strategy)
@settings(max_examples=50)
def test_eol::expression::expressionrange_instantiation(instance):
    assert isinstance(instance, eol::expression::ExpressionRange)

@given(instance=UniqueCollection_strategy)
@settings(max_examples=50)
def test_uniquecollection_instantiation(instance):
    assert isinstance(instance, UniqueCollection)

@given(instance=eol::expression::OrderedSetExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::orderedsetexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::OrderedSetExpression)

@given(instance=eol::expression::SetExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::setexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::SetExpression)

@given(instance=CollectionExpression_strategy)
@settings(max_examples=50)
def test_collectionexpression_instantiation(instance):
    assert isinstance(instance, CollectionExpression)

@given(instance=eol::expression::UniqueCollection_strategy)
@settings(max_examples=50)
def test_eol::expression::uniquecollection_instantiation(instance):
    assert isinstance(instance, eol::expression::UniqueCollection)

@given(instance=eol::expression::OrderedCollection_strategy)
@settings(max_examples=50)
def test_eol::expression::orderedcollection_instantiation(instance):
    assert isinstance(instance, eol::expression::OrderedCollection)

@given(instance=eol::expression::BagExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::bagexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::BagExpression)

@given(instance=SummableExpression_strategy)
@settings(max_examples=50)
def test_summableexpression_instantiation(instance):
    assert isinstance(instance, SummableExpression)

@given(instance=ComparableExpression_strategy)
@settings(max_examples=50)
def test_comparableexpression_instantiation(instance):
    assert isinstance(instance, ComparableExpression)

@given(instance=eol::expression::RealExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::realexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::RealExpression)

@given(instance=eol::expression::RealExpression_strategy)
def test_eol::expression::realexpression_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=eol::expression::RealExpression_strategy)
def test_eol::expression::realexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eol::expression::IntegerExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::integerexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::IntegerExpression)

@given(instance=eol::expression::IntegerExpression_strategy)
def test_eol::expression::integerexpression_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=eol::expression::IntegerExpression_strategy)
def test_eol::expression::integerexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eol::expression::StringExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::stringexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::StringExpression)

@given(instance=eol::expression::StringExpression_strategy)
def test_eol::expression::stringexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=eol::expression::StringExpression_strategy)
def test_eol::expression::stringexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_primitiveexpression_instantiation(instance):
    assert isinstance(instance, PrimitiveExpression)

@given(instance=eol::expression::BooleanExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::booleanexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::BooleanExpression)

@given(instance=eol::expression::BooleanExpression_strategy)
def test_eol::expression::booleanexpression_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=eol::expression::BooleanExpression_strategy)
def test_eol::expression::booleanexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eol::expression::SummableExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::summableexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::SummableExpression)

@given(instance=eol::expression::ComparableExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::comparableexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::ComparableExpression)

@given(instance=ArithmeticOperatorExpression_strategy)
@settings(max_examples=50)
def test_arithmeticoperatorexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticOperatorExpression)

@given(instance=eol::expression::MultiplyOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::multiplyoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::MultiplyOperatorExpression)

@given(instance=eol::expression::MinusOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::minusoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::MinusOperatorExpression)

@given(instance=eol::expression::DivideOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::divideoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::DivideOperatorExpression)

@given(instance=FeatureCallExpression_strategy)
@settings(max_examples=50)
def test_featurecallexpression_instantiation(instance):
    assert isinstance(instance, FeatureCallExpression)

@given(instance=eol::expression::PropertyCallExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::propertycallexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::PropertyCallExpression)

@given(instance=eol::expression::PropertyCallExpression_strategy)
def test_eol::expression::propertycallexpression_extended_type(instance):
    assert isinstance(instance.extended, bool)


@given(instance=eol::expression::PropertyCallExpression_strategy)
def test_eol::expression::propertycallexpression_extended_setter(instance):
    original = instance.extended
    instance.extended = original
    assert instance.extended == original

@given(instance=eol::expression::FOLMethodCallExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::folmethodcallexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::FOLMethodCallExpression)

@given(instance=eol::expression::MethodCallExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::methodcallexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::MethodCallExpression)

@given(instance=VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, VariableDeclarationExpression)

@given(instance=eol::expression::FormalParameterExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::formalparameterexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::FormalParameterExpression)

@given(instance=ComparisonOperatorExpression_strategy)
@settings(max_examples=50)
def test_comparisonoperatorexpression_instantiation(instance):
    assert isinstance(instance, ComparisonOperatorExpression)

@given(instance=eol::expression::LessThanOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::lessthanoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::LessThanOperatorExpression)

@given(instance=eol::expression::EqualsOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::equalsoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::EqualsOperatorExpression)

@given(instance=eol::expression::LessThanOrEqualToOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::lessthanorequaltooperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::LessThanOrEqualToOperatorExpression)

@given(instance=eol::expression::NotEqualsOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::notequalsoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::NotEqualsOperatorExpression)

@given(instance=eol::expression::GreaterThanOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::greaterthanoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::GreaterThanOperatorExpression)

@given(instance=eol::expression::GreaterThanOrEqualToOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::greaterthanorequaltooperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::GreaterThanOrEqualToOperatorExpression)

@given(instance=eol::expression::PlusOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::plusoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::PlusOperatorExpression)

@given(instance=LogicalOperatorExpression_strategy)
@settings(max_examples=50)
def test_logicaloperatorexpression_instantiation(instance):
    assert isinstance(instance, LogicalOperatorExpression)

@given(instance=eol::expression::XorOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::xoroperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::XorOperatorExpression)

@given(instance=eol::expression::ImpliesOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::impliesoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::ImpliesOperatorExpression)

@given(instance=eol::expression::OrOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::oroperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::OrOperatorExpression)

@given(instance=eol::expression::AndOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::andoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::AndOperatorExpression)

@given(instance=BinaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_binaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, BinaryOperatorExpression)

@given(instance=eol::expression::ComparisonOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::comparisonoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::ComparisonOperatorExpression)

@given(instance=eol::expression::ArithmeticOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::arithmeticoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::ArithmeticOperatorExpression)

@given(instance=eol::expression::LogicalOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::logicaloperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::LogicalOperatorExpression)

@given(instance=UnaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_unaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, UnaryOperatorExpression)

@given(instance=eol::expression::NegativeOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::negativeoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::NegativeOperatorExpression)

@given(instance=eol::expression::NotOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::notoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::NotOperatorExpression)

@given(instance=OperatorExpression_strategy)
@settings(max_examples=50)
def test_operatorexpression_instantiation(instance):
    assert isinstance(instance, OperatorExpression)

@given(instance=eol::expression::BinaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::binaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::BinaryOperatorExpression)

@given(instance=eol::expression::UnaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::unaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::UnaryOperatorExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=eol::expression::FeatureCallExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::featurecallexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::FeatureCallExpression)

@given(instance=eol::expression::FeatureCallExpression_strategy)
def test_eol::expression::featurecallexpression_arrow_type(instance):
    assert isinstance(instance.arrow, bool)


@given(instance=eol::expression::FeatureCallExpression_strategy)
def test_eol::expression::featurecallexpression_arrow_setter(instance):
    original = instance.arrow
    instance.arrow = original
    assert instance.arrow == original

@given(instance=eol::expression::CollectionExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::collectionexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::CollectionExpression)

@given(instance=eol::expression::MapExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::mapexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::MapExpression)

@given(instance=eol::expression::KeyValueExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::keyvalueexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::KeyValueExpression)

@given(instance=eol::expression::NewExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::newexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::NewExpression)

@given(instance=eol::expression::NameExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::nameexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::NameExpression)

@given(instance=eol::expression::NameExpression_strategy)
def test_eol::expression::nameexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eol::expression::NameExpression_strategy)
def test_eol::expression::nameexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eol::expression::NameExpression_strategy)
def test_eol::expression::nameexpression_isType_type(instance):
    assert isinstance(instance.isType, bool)


@given(instance=eol::expression::NameExpression_strategy)
def test_eol::expression::nameexpression_isType_setter(instance):
    original = instance.isType
    instance.isType = original
    assert instance.isType == original

@given(instance=eol::expression::EnumerationLiteralExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::enumerationliteralexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::EnumerationLiteralExpression)

@given(instance=eol::expression::VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::VariableDeclarationExpression)

@given(instance=eol::expression::VariableDeclarationExpression_strategy)
def test_eol::expression::variabledeclarationexpression_create_type(instance):
    assert isinstance(instance.create, bool)


@given(instance=eol::expression::VariableDeclarationExpression_strategy)
def test_eol::expression::variabledeclarationexpression_create_setter(instance):
    original = instance.create
    instance.create = original
    assert instance.create == original

@given(instance=eol::expression::PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::primitiveexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::PrimitiveExpression)

@given(instance=eol::expression::CollectionInitialisationExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::collectioninitialisationexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::CollectionInitialisationExpression)

@given(instance=eol::expression::OperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::expression::operatorexpression_instantiation(instance):
    assert isinstance(instance, eol::expression::OperatorExpression)

@given(instance=eol::expression::Type_strategy)
@settings(max_examples=50)
def test_eol::expression::type_instantiation(instance):
    assert isinstance(instance, eol::expression::Type)

@given(instance=eol::expression::Expression_strategy)
@settings(max_examples=50)
def test_eol::expression::expression_instantiation(instance):
    assert isinstance(instance, eol::expression::Expression)

@given(instance=eol::expression::Expression_strategy)
def test_eol::expression::expression_inBrackets_type(instance):
    assert isinstance(instance.inBrackets, bool)


@given(instance=eol::expression::Expression_strategy)
def test_eol::expression::expression_inBrackets_setter(instance):
    original = instance.inBrackets
    instance.inBrackets = original
    assert instance.inBrackets == original
