import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Predicate,
    expression::PredicateInOperator,
    expression::PredicateComparisonOperator,
    expression::PredicateEqualityOperator,
    expression::PredicateIsNull,
    expression::PredicateLikeOperator,
    expression::PredicateIsEmpty,
    expression::PredicateIsOperator,
    expression::PredicateBooleanOperator,
    Literal,
    expression::StringLiteral,
    expression::TimeLiteral,
    expression::BooleanLiteral,
    expression::IntegerLiteral,
    expression::NullLiteral,
    Expression,
    expression::Variable,
    expression::Predicate,
    expression::Literal,
    expression::Expression,
    BooleanOperator,
    ComparisionOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_predicate_is_not_abstract():
    assert not inspect.isabstract(Predicate)


def test_predicate_constructor_exists():
    assert callable(Predicate.__init__)


def test_predicate_constructor_args():
    sig = inspect.signature(Predicate.__init__)
    params = list(sig.parameters.keys())



def test_expression::predicateinoperator_is_not_abstract():
    assert not inspect.isabstract(expression::PredicateInOperator)


def test_expression::predicateinoperator_constructor_exists():
    assert callable(expression::PredicateInOperator.__init__)


def test_expression::predicateinoperator_constructor_args():
    sig = inspect.signature(expression::PredicateInOperator.__init__)
    params = list(sig.parameters.keys())



def test_expression::predicatecomparisonoperator_is_not_abstract():
    assert not inspect.isabstract(expression::PredicateComparisonOperator)


def test_expression::predicatecomparisonoperator_constructor_exists():
    assert callable(expression::PredicateComparisonOperator.__init__)


def test_expression::predicatecomparisonoperator_constructor_args():
    sig = inspect.signature(expression::PredicateComparisonOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_expression::predicatecomparisonoperator_has_operator():
    assert hasattr(expression::PredicateComparisonOperator, "operator")
    descriptor = None
    for klass in expression::PredicateComparisonOperator.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_expression::predicateequalityoperator_is_not_abstract():
    assert not inspect.isabstract(expression::PredicateEqualityOperator)


def test_expression::predicateequalityoperator_constructor_exists():
    assert callable(expression::PredicateEqualityOperator.__init__)


def test_expression::predicateequalityoperator_constructor_args():
    sig = inspect.signature(expression::PredicateEqualityOperator.__init__)
    params = list(sig.parameters.keys())



def test_expression::predicateisnull_is_not_abstract():
    assert not inspect.isabstract(expression::PredicateIsNull)


def test_expression::predicateisnull_constructor_exists():
    assert callable(expression::PredicateIsNull.__init__)


def test_expression::predicateisnull_constructor_args():
    sig = inspect.signature(expression::PredicateIsNull.__init__)
    params = list(sig.parameters.keys())



def test_expression::predicatelikeoperator_is_not_abstract():
    assert not inspect.isabstract(expression::PredicateLikeOperator)


def test_expression::predicatelikeoperator_constructor_exists():
    assert callable(expression::PredicateLikeOperator.__init__)


def test_expression::predicatelikeoperator_constructor_args():
    sig = inspect.signature(expression::PredicateLikeOperator.__init__)
    params = list(sig.parameters.keys())



def test_expression::predicateisempty_is_not_abstract():
    assert not inspect.isabstract(expression::PredicateIsEmpty)


def test_expression::predicateisempty_constructor_exists():
    assert callable(expression::PredicateIsEmpty.__init__)


def test_expression::predicateisempty_constructor_args():
    sig = inspect.signature(expression::PredicateIsEmpty.__init__)
    params = list(sig.parameters.keys())



def test_expression::predicateisoperator_is_not_abstract():
    assert not inspect.isabstract(expression::PredicateIsOperator)


def test_expression::predicateisoperator_constructor_exists():
    assert callable(expression::PredicateIsOperator.__init__)


def test_expression::predicateisoperator_constructor_args():
    sig = inspect.signature(expression::PredicateIsOperator.__init__)
    params = list(sig.parameters.keys())



def test_expression::predicatebooleanoperator_is_not_abstract():
    assert not inspect.isabstract(expression::PredicateBooleanOperator)


def test_expression::predicatebooleanoperator_constructor_exists():
    assert callable(expression::PredicateBooleanOperator.__init__)


def test_expression::predicatebooleanoperator_constructor_args():
    sig = inspect.signature(expression::PredicateBooleanOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_expression::predicatebooleanoperator_has_operator():
    assert hasattr(expression::PredicateBooleanOperator, "operator")
    descriptor = None
    for klass in expression::PredicateBooleanOperator.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_expression::stringliteral_is_not_abstract():
    assert not inspect.isabstract(expression::StringLiteral)


def test_expression::stringliteral_constructor_exists():
    assert callable(expression::StringLiteral.__init__)


def test_expression::stringliteral_constructor_args():
    sig = inspect.signature(expression::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expression::stringliteral_has_value():
    assert hasattr(expression::StringLiteral, "value")
    descriptor = None
    for klass in expression::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression::timeliteral_is_not_abstract():
    assert not inspect.isabstract(expression::TimeLiteral)


def test_expression::timeliteral_constructor_exists():
    assert callable(expression::TimeLiteral.__init__)


def test_expression::timeliteral_constructor_args():
    sig = inspect.signature(expression::TimeLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expression::timeliteral_has_value():
    assert hasattr(expression::TimeLiteral, "value")
    descriptor = None
    for klass in expression::TimeLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(expression::BooleanLiteral)


def test_expression::booleanliteral_constructor_exists():
    assert callable(expression::BooleanLiteral.__init__)


def test_expression::booleanliteral_constructor_args():
    sig = inspect.signature(expression::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expression::booleanliteral_has_value():
    assert hasattr(expression::BooleanLiteral, "value")
    descriptor = None
    for klass in expression::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression::integerliteral_is_not_abstract():
    assert not inspect.isabstract(expression::IntegerLiteral)


def test_expression::integerliteral_constructor_exists():
    assert callable(expression::IntegerLiteral.__init__)


def test_expression::integerliteral_constructor_args():
    sig = inspect.signature(expression::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expression::integerliteral_has_value():
    assert hasattr(expression::IntegerLiteral, "value")
    descriptor = None
    for klass in expression::IntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression::nullliteral_is_not_abstract():
    assert not inspect.isabstract(expression::NullLiteral)


def test_expression::nullliteral_constructor_exists():
    assert callable(expression::NullLiteral.__init__)


def test_expression::nullliteral_constructor_args():
    sig = inspect.signature(expression::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_expression::variable_is_not_abstract():
    assert not inspect.isabstract(expression::Variable)


def test_expression::variable_constructor_exists():
    assert callable(expression::Variable.__init__)


def test_expression::variable_constructor_args():
    sig = inspect.signature(expression::Variable.__init__)
    params = list(sig.parameters.keys())



def test_expression::predicate_is_not_abstract():
    assert not inspect.isabstract(expression::Predicate)


def test_expression::predicate_constructor_exists():
    assert callable(expression::Predicate.__init__)


def test_expression::predicate_constructor_args():
    sig = inspect.signature(expression::Predicate.__init__)
    params = list(sig.parameters.keys())
    assert "negated" in params, "Missing parameter 'negated'"

def test_expression::predicate_has_negated():
    assert hasattr(expression::Predicate, "negated")
    descriptor = None
    for klass in expression::Predicate.__mro__:
        if "negated" in klass.__dict__:
            descriptor = klass.__dict__["negated"]
            break
    assert isinstance(descriptor, property)



def test_expression::literal_is_not_abstract():
    assert not inspect.isabstract(expression::Literal)


def test_expression::literal_constructor_exists():
    assert callable(expression::Literal.__init__)


def test_expression::literal_constructor_args():
    sig = inspect.signature(expression::Literal.__init__)
    params = list(sig.parameters.keys())



def test_expression::expression_is_not_abstract():
    assert not inspect.isabstract(expression::Expression)


def test_expression::expression_constructor_exists():
    assert callable(expression::Expression.__init__)


def test_expression::expression_constructor_args():
    sig = inspect.signature(expression::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "suffixes" in params, "Missing parameter 'suffixes'"

def test_expression::expression_has_suffixes():
    assert hasattr(expression::Expression, "suffixes")
    descriptor = None
    for klass in expression::Expression.__mro__:
        if "suffixes" in klass.__dict__:
            descriptor = klass.__dict__["suffixes"]
            break
    assert isinstance(descriptor, property)

def test_booleanoperator_exists():
    # Check that the Enumeration exists
    assert BooleanOperator is not None

def test_booleanoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanOperator]
    expected_literals = [
        "And",
        "Or",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanOperator"

def test_comparisionoperator_exists():
    # Check that the Enumeration exists
    assert ComparisionOperator is not None

def test_comparisionoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComparisionOperator]
    expected_literals = [
        "GreaterThan",
        "LessThan",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComparisionOperator"


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
Predicate_strategy = st.builds(
    Predicate,
)
expression::PredicateInOperator_strategy = st.builds(
    expression::PredicateInOperator,
)
expression::PredicateComparisonOperator_strategy = st.builds(
    expression::PredicateComparisonOperator,
    operator=
        safe_text
)
expression::PredicateEqualityOperator_strategy = st.builds(
    expression::PredicateEqualityOperator,
)
expression::PredicateIsNull_strategy = st.builds(
    expression::PredicateIsNull,
)
expression::PredicateLikeOperator_strategy = st.builds(
    expression::PredicateLikeOperator,
)
expression::PredicateIsEmpty_strategy = st.builds(
    expression::PredicateIsEmpty,
)
expression::PredicateIsOperator_strategy = st.builds(
    expression::PredicateIsOperator,
)
expression::PredicateBooleanOperator_strategy = st.builds(
    expression::PredicateBooleanOperator,
    operator=
        safe_text
)
Literal_strategy = st.builds(
    Literal,
)
expression::StringLiteral_strategy = st.builds(
    expression::StringLiteral,
    value=
        safe_text
)
expression::TimeLiteral_strategy = st.builds(
    expression::TimeLiteral,
    value=
        safe_text
)
expression::BooleanLiteral_strategy = st.builds(
    expression::BooleanLiteral,
    value=
        st.booleans()
)
expression::IntegerLiteral_strategy = st.builds(
    expression::IntegerLiteral,
    value=
        st.integers()
)
expression::NullLiteral_strategy = st.builds(
    expression::NullLiteral,
)
Expression_strategy = st.builds(
    Expression,
)
expression::Variable_strategy = st.builds(
    expression::Variable,
)
expression::Predicate_strategy = st.builds(
    expression::Predicate,
    negated=
        st.booleans()
)
expression::Literal_strategy = st.builds(
    expression::Literal,
)
expression::Expression_strategy = st.builds(
    expression::Expression,
    suffixes=
        safe_text
)

@given(instance=Predicate_strategy)
@settings(max_examples=50)
def test_predicate_instantiation(instance):
    assert isinstance(instance, Predicate)

@given(instance=expression::PredicateInOperator_strategy)
@settings(max_examples=50)
def test_expression::predicateinoperator_instantiation(instance):
    assert isinstance(instance, expression::PredicateInOperator)

@given(instance=expression::PredicateComparisonOperator_strategy)
@settings(max_examples=50)
def test_expression::predicatecomparisonoperator_instantiation(instance):
    assert isinstance(instance, expression::PredicateComparisonOperator)

@given(instance=expression::PredicateComparisonOperator_strategy)
def test_expression::predicatecomparisonoperator_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=expression::PredicateComparisonOperator_strategy)
def test_expression::predicatecomparisonoperator_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=expression::PredicateEqualityOperator_strategy)
@settings(max_examples=50)
def test_expression::predicateequalityoperator_instantiation(instance):
    assert isinstance(instance, expression::PredicateEqualityOperator)

@given(instance=expression::PredicateIsNull_strategy)
@settings(max_examples=50)
def test_expression::predicateisnull_instantiation(instance):
    assert isinstance(instance, expression::PredicateIsNull)

@given(instance=expression::PredicateLikeOperator_strategy)
@settings(max_examples=50)
def test_expression::predicatelikeoperator_instantiation(instance):
    assert isinstance(instance, expression::PredicateLikeOperator)

@given(instance=expression::PredicateIsEmpty_strategy)
@settings(max_examples=50)
def test_expression::predicateisempty_instantiation(instance):
    assert isinstance(instance, expression::PredicateIsEmpty)

@given(instance=expression::PredicateIsOperator_strategy)
@settings(max_examples=50)
def test_expression::predicateisoperator_instantiation(instance):
    assert isinstance(instance, expression::PredicateIsOperator)

@given(instance=expression::PredicateBooleanOperator_strategy)
@settings(max_examples=50)
def test_expression::predicatebooleanoperator_instantiation(instance):
    assert isinstance(instance, expression::PredicateBooleanOperator)

@given(instance=expression::PredicateBooleanOperator_strategy)
def test_expression::predicatebooleanoperator_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=expression::PredicateBooleanOperator_strategy)
def test_expression::predicatebooleanoperator_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=expression::StringLiteral_strategy)
@settings(max_examples=50)
def test_expression::stringliteral_instantiation(instance):
    assert isinstance(instance, expression::StringLiteral)

@given(instance=expression::StringLiteral_strategy)
def test_expression::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=expression::StringLiteral_strategy)
def test_expression::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expression::TimeLiteral_strategy)
@settings(max_examples=50)
def test_expression::timeliteral_instantiation(instance):
    assert isinstance(instance, expression::TimeLiteral)

@given(instance=expression::TimeLiteral_strategy)
def test_expression::timeliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=expression::TimeLiteral_strategy)
def test_expression::timeliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expression::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_expression::booleanliteral_instantiation(instance):
    assert isinstance(instance, expression::BooleanLiteral)

@given(instance=expression::BooleanLiteral_strategy)
def test_expression::booleanliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=expression::BooleanLiteral_strategy)
def test_expression::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expression::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_expression::integerliteral_instantiation(instance):
    assert isinstance(instance, expression::IntegerLiteral)

@given(instance=expression::IntegerLiteral_strategy)
def test_expression::integerliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=expression::IntegerLiteral_strategy)
def test_expression::integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expression::NullLiteral_strategy)
@settings(max_examples=50)
def test_expression::nullliteral_instantiation(instance):
    assert isinstance(instance, expression::NullLiteral)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=expression::Variable_strategy)
@settings(max_examples=50)
def test_expression::variable_instantiation(instance):
    assert isinstance(instance, expression::Variable)

@given(instance=expression::Predicate_strategy)
@settings(max_examples=50)
def test_expression::predicate_instantiation(instance):
    assert isinstance(instance, expression::Predicate)

@given(instance=expression::Predicate_strategy)
def test_expression::predicate_negated_type(instance):
    assert isinstance(instance.negated, bool)


@given(instance=expression::Predicate_strategy)
def test_expression::predicate_negated_setter(instance):
    original = instance.negated
    instance.negated = original
    assert instance.negated == original

@given(instance=expression::Literal_strategy)
@settings(max_examples=50)
def test_expression::literal_instantiation(instance):
    assert isinstance(instance, expression::Literal)

@given(instance=expression::Expression_strategy)
@settings(max_examples=50)
def test_expression::expression_instantiation(instance):
    assert isinstance(instance, expression::Expression)

@given(instance=expression::Expression_strategy)
def test_expression::expression_suffixes_type(instance):
    assert isinstance(instance.suffixes, str)


@given(instance=expression::Expression_strategy)
def test_expression::expression_suffixes_setter(instance):
    original = instance.suffixes
    instance.suffixes = original
    assert instance.suffixes == original
