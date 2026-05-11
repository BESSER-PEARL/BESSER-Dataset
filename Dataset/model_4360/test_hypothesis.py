import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Statement,
    simple::lang::IfStatement,
    simple::lang::ExpressionStatement,
    FeatureCallExpression,
    simple::lang::PropertyCallExpression,
    simple::lang::MethodCallExpression,
    simple::lang::AssignmentStatement,
    simple::lang::WhileStatement,
    BinaryExpression,
    simple::lang::ComparisonExpression,
    simple::lang::ArithmeticExpression,
    simple::lang::LogicalExpression,
    Expression,
    simple::lang::FeatureCallExpression,
    simple::lang::BinaryExpression,
    simple::lang::Type,
    simple::lang::Expression,
    simple::lang::Statement,
    simple::lang::SimpleLang,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_simple::lang::ifstatement_is_not_abstract():
    assert not inspect.isabstract(simple::lang::IfStatement)


def test_simple::lang::ifstatement_constructor_exists():
    assert callable(simple::lang::IfStatement.__init__)


def test_simple::lang::ifstatement_constructor_args():
    sig = inspect.signature(simple::lang::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_simple::lang::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(simple::lang::ExpressionStatement)


def test_simple::lang::expressionstatement_constructor_exists():
    assert callable(simple::lang::ExpressionStatement.__init__)


def test_simple::lang::expressionstatement_constructor_args():
    sig = inspect.signature(simple::lang::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_featurecallexpression_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExpression)


def test_featurecallexpression_constructor_exists():
    assert callable(FeatureCallExpression.__init__)


def test_featurecallexpression_constructor_args():
    sig = inspect.signature(FeatureCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_simple::lang::propertycallexpression_is_not_abstract():
    assert not inspect.isabstract(simple::lang::PropertyCallExpression)


def test_simple::lang::propertycallexpression_constructor_exists():
    assert callable(simple::lang::PropertyCallExpression.__init__)


def test_simple::lang::propertycallexpression_constructor_args():
    sig = inspect.signature(simple::lang::PropertyCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_simple::lang::methodcallexpression_is_not_abstract():
    assert not inspect.isabstract(simple::lang::MethodCallExpression)


def test_simple::lang::methodcallexpression_constructor_exists():
    assert callable(simple::lang::MethodCallExpression.__init__)


def test_simple::lang::methodcallexpression_constructor_args():
    sig = inspect.signature(simple::lang::MethodCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_simple::lang::assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(simple::lang::AssignmentStatement)


def test_simple::lang::assignmentstatement_constructor_exists():
    assert callable(simple::lang::AssignmentStatement.__init__)


def test_simple::lang::assignmentstatement_constructor_args():
    sig = inspect.signature(simple::lang::AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_simple::lang::whilestatement_is_not_abstract():
    assert not inspect.isabstract(simple::lang::WhileStatement)


def test_simple::lang::whilestatement_constructor_exists():
    assert callable(simple::lang::WhileStatement.__init__)


def test_simple::lang::whilestatement_constructor_args():
    sig = inspect.signature(simple::lang::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_simple::lang::comparisonexpression_is_not_abstract():
    assert not inspect.isabstract(simple::lang::ComparisonExpression)


def test_simple::lang::comparisonexpression_constructor_exists():
    assert callable(simple::lang::ComparisonExpression.__init__)


def test_simple::lang::comparisonexpression_constructor_args():
    sig = inspect.signature(simple::lang::ComparisonExpression.__init__)
    params = list(sig.parameters.keys())



def test_simple::lang::arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(simple::lang::ArithmeticExpression)


def test_simple::lang::arithmeticexpression_constructor_exists():
    assert callable(simple::lang::ArithmeticExpression.__init__)


def test_simple::lang::arithmeticexpression_constructor_args():
    sig = inspect.signature(simple::lang::ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_simple::lang::logicalexpression_is_not_abstract():
    assert not inspect.isabstract(simple::lang::LogicalExpression)


def test_simple::lang::logicalexpression_constructor_exists():
    assert callable(simple::lang::LogicalExpression.__init__)


def test_simple::lang::logicalexpression_constructor_args():
    sig = inspect.signature(simple::lang::LogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_simple::lang::featurecallexpression_is_not_abstract():
    assert not inspect.isabstract(simple::lang::FeatureCallExpression)


def test_simple::lang::featurecallexpression_constructor_exists():
    assert callable(simple::lang::FeatureCallExpression.__init__)


def test_simple::lang::featurecallexpression_constructor_args():
    sig = inspect.signature(simple::lang::FeatureCallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simple::lang::featurecallexpression_has_name():
    assert hasattr(simple::lang::FeatureCallExpression, "name")
    descriptor = None
    for klass in simple::lang::FeatureCallExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simple::lang::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(simple::lang::BinaryExpression)


def test_simple::lang::binaryexpression_constructor_exists():
    assert callable(simple::lang::BinaryExpression.__init__)


def test_simple::lang::binaryexpression_constructor_args():
    sig = inspect.signature(simple::lang::BinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_simple::lang::binaryexpression_has_operator():
    assert hasattr(simple::lang::BinaryExpression, "operator")
    descriptor = None
    for klass in simple::lang::BinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_simple::lang::type_is_not_abstract():
    assert not inspect.isabstract(simple::lang::Type)


def test_simple::lang::type_constructor_exists():
    assert callable(simple::lang::Type.__init__)


def test_simple::lang::type_constructor_args():
    sig = inspect.signature(simple::lang::Type.__init__)
    params = list(sig.parameters.keys())



def test_simple::lang::expression_is_not_abstract():
    assert not inspect.isabstract(simple::lang::Expression)


def test_simple::lang::expression_constructor_exists():
    assert callable(simple::lang::Expression.__init__)


def test_simple::lang::expression_constructor_args():
    sig = inspect.signature(simple::lang::Expression.__init__)
    params = list(sig.parameters.keys())



def test_simple::lang::statement_is_not_abstract():
    assert not inspect.isabstract(simple::lang::Statement)


def test_simple::lang::statement_constructor_exists():
    assert callable(simple::lang::Statement.__init__)


def test_simple::lang::statement_constructor_args():
    sig = inspect.signature(simple::lang::Statement.__init__)
    params = list(sig.parameters.keys())



def test_simple::lang::simplelang_is_not_abstract():
    assert not inspect.isabstract(simple::lang::SimpleLang)


def test_simple::lang::simplelang_constructor_exists():
    assert callable(simple::lang::SimpleLang.__init__)


def test_simple::lang::simplelang_constructor_args():
    sig = inspect.signature(simple::lang::SimpleLang.__init__)
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
Statement_strategy = st.builds(
    Statement,
)
simple::lang::IfStatement_strategy = st.builds(
    simple::lang::IfStatement,
)
simple::lang::ExpressionStatement_strategy = st.builds(
    simple::lang::ExpressionStatement,
)
FeatureCallExpression_strategy = st.builds(
    FeatureCallExpression,
)
simple::lang::PropertyCallExpression_strategy = st.builds(
    simple::lang::PropertyCallExpression,
)
simple::lang::MethodCallExpression_strategy = st.builds(
    simple::lang::MethodCallExpression,
)
simple::lang::AssignmentStatement_strategy = st.builds(
    simple::lang::AssignmentStatement,
)
simple::lang::WhileStatement_strategy = st.builds(
    simple::lang::WhileStatement,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
simple::lang::ComparisonExpression_strategy = st.builds(
    simple::lang::ComparisonExpression,
)
simple::lang::ArithmeticExpression_strategy = st.builds(
    simple::lang::ArithmeticExpression,
)
simple::lang::LogicalExpression_strategy = st.builds(
    simple::lang::LogicalExpression,
)
Expression_strategy = st.builds(
    Expression,
)
simple::lang::FeatureCallExpression_strategy = st.builds(
    simple::lang::FeatureCallExpression,
    name=
        safe_text
)
simple::lang::BinaryExpression_strategy = st.builds(
    simple::lang::BinaryExpression,
    operator=
        safe_text
)
simple::lang::Type_strategy = st.builds(
    simple::lang::Type,
)
simple::lang::Expression_strategy = st.builds(
    simple::lang::Expression,
)
simple::lang::Statement_strategy = st.builds(
    simple::lang::Statement,
)
simple::lang::SimpleLang_strategy = st.builds(
    simple::lang::SimpleLang,
)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=simple::lang::IfStatement_strategy)
@settings(max_examples=50)
def test_simple::lang::ifstatement_instantiation(instance):
    assert isinstance(instance, simple::lang::IfStatement)

@given(instance=simple::lang::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_simple::lang::expressionstatement_instantiation(instance):
    assert isinstance(instance, simple::lang::ExpressionStatement)

@given(instance=FeatureCallExpression_strategy)
@settings(max_examples=50)
def test_featurecallexpression_instantiation(instance):
    assert isinstance(instance, FeatureCallExpression)

@given(instance=simple::lang::PropertyCallExpression_strategy)
@settings(max_examples=50)
def test_simple::lang::propertycallexpression_instantiation(instance):
    assert isinstance(instance, simple::lang::PropertyCallExpression)

@given(instance=simple::lang::MethodCallExpression_strategy)
@settings(max_examples=50)
def test_simple::lang::methodcallexpression_instantiation(instance):
    assert isinstance(instance, simple::lang::MethodCallExpression)

@given(instance=simple::lang::AssignmentStatement_strategy)
@settings(max_examples=50)
def test_simple::lang::assignmentstatement_instantiation(instance):
    assert isinstance(instance, simple::lang::AssignmentStatement)

@given(instance=simple::lang::WhileStatement_strategy)
@settings(max_examples=50)
def test_simple::lang::whilestatement_instantiation(instance):
    assert isinstance(instance, simple::lang::WhileStatement)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=simple::lang::ComparisonExpression_strategy)
@settings(max_examples=50)
def test_simple::lang::comparisonexpression_instantiation(instance):
    assert isinstance(instance, simple::lang::ComparisonExpression)

@given(instance=simple::lang::ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_simple::lang::arithmeticexpression_instantiation(instance):
    assert isinstance(instance, simple::lang::ArithmeticExpression)

@given(instance=simple::lang::LogicalExpression_strategy)
@settings(max_examples=50)
def test_simple::lang::logicalexpression_instantiation(instance):
    assert isinstance(instance, simple::lang::LogicalExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=simple::lang::FeatureCallExpression_strategy)
@settings(max_examples=50)
def test_simple::lang::featurecallexpression_instantiation(instance):
    assert isinstance(instance, simple::lang::FeatureCallExpression)

@given(instance=simple::lang::FeatureCallExpression_strategy)
def test_simple::lang::featurecallexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simple::lang::FeatureCallExpression_strategy)
def test_simple::lang::featurecallexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simple::lang::BinaryExpression_strategy)
@settings(max_examples=50)
def test_simple::lang::binaryexpression_instantiation(instance):
    assert isinstance(instance, simple::lang::BinaryExpression)

@given(instance=simple::lang::BinaryExpression_strategy)
def test_simple::lang::binaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=simple::lang::BinaryExpression_strategy)
def test_simple::lang::binaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=simple::lang::Type_strategy)
@settings(max_examples=50)
def test_simple::lang::type_instantiation(instance):
    assert isinstance(instance, simple::lang::Type)

@given(instance=simple::lang::Expression_strategy)
@settings(max_examples=50)
def test_simple::lang::expression_instantiation(instance):
    assert isinstance(instance, simple::lang::Expression)

@given(instance=simple::lang::Statement_strategy)
@settings(max_examples=50)
def test_simple::lang::statement_instantiation(instance):
    assert isinstance(instance, simple::lang::Statement)

@given(instance=simple::lang::SimpleLang_strategy)
@settings(max_examples=50)
def test_simple::lang::simplelang_instantiation(instance):
    assert isinstance(instance, simple::lang::SimpleLang)
