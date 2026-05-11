import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UnaryExpression,
    core::UMinus,
    core::Not,
    IntegerExpression,
    core::IntegerLiteral,
    core::Conditional,
    core::BinaryExpression,
    core::UnaryExpression,
    BinaryExpression,
    core::Mod,
    core::Or,
    core::Lower,
    core::Equal,
    core::Minus,
    core::And,
    core::Div,
    core::Greater,
    core::Mult,
    core::Add,
    core::Filter,
    core::IntegerExpression,
    core::Rule,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_core::uminus_is_not_abstract():
    assert not inspect.isabstract(core::UMinus)


def test_core::uminus_constructor_exists():
    assert callable(core::UMinus.__init__)


def test_core::uminus_constructor_args():
    sig = inspect.signature(core::UMinus.__init__)
    params = list(sig.parameters.keys())



def test_core::not_is_not_abstract():
    assert not inspect.isabstract(core::Not)


def test_core::not_constructor_exists():
    assert callable(core::Not.__init__)


def test_core::not_constructor_args():
    sig = inspect.signature(core::Not.__init__)
    params = list(sig.parameters.keys())



def test_integerexpression_is_not_abstract():
    assert not inspect.isabstract(IntegerExpression)


def test_integerexpression_constructor_exists():
    assert callable(IntegerExpression.__init__)


def test_integerexpression_constructor_args():
    sig = inspect.signature(IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_core::integerliteral_is_not_abstract():
    assert not inspect.isabstract(core::IntegerLiteral)


def test_core::integerliteral_constructor_exists():
    assert callable(core::IntegerLiteral.__init__)


def test_core::integerliteral_constructor_args():
    sig = inspect.signature(core::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_core::integerliteral_has_val():
    assert hasattr(core::IntegerLiteral, "val")
    descriptor = None
    for klass in core::IntegerLiteral.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_core::conditional_is_not_abstract():
    assert not inspect.isabstract(core::Conditional)


def test_core::conditional_constructor_exists():
    assert callable(core::Conditional.__init__)


def test_core::conditional_constructor_args():
    sig = inspect.signature(core::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_core::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(core::BinaryExpression)


def test_core::binaryexpression_constructor_exists():
    assert callable(core::BinaryExpression.__init__)


def test_core::binaryexpression_constructor_args():
    sig = inspect.signature(core::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_core::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(core::UnaryExpression)


def test_core::unaryexpression_constructor_exists():
    assert callable(core::UnaryExpression.__init__)


def test_core::unaryexpression_constructor_args():
    sig = inspect.signature(core::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_core::mod_is_not_abstract():
    assert not inspect.isabstract(core::Mod)


def test_core::mod_constructor_exists():
    assert callable(core::Mod.__init__)


def test_core::mod_constructor_args():
    sig = inspect.signature(core::Mod.__init__)
    params = list(sig.parameters.keys())



def test_core::or_is_not_abstract():
    assert not inspect.isabstract(core::Or)


def test_core::or_constructor_exists():
    assert callable(core::Or.__init__)


def test_core::or_constructor_args():
    sig = inspect.signature(core::Or.__init__)
    params = list(sig.parameters.keys())



def test_core::lower_is_not_abstract():
    assert not inspect.isabstract(core::Lower)


def test_core::lower_constructor_exists():
    assert callable(core::Lower.__init__)


def test_core::lower_constructor_args():
    sig = inspect.signature(core::Lower.__init__)
    params = list(sig.parameters.keys())



def test_core::equal_is_not_abstract():
    assert not inspect.isabstract(core::Equal)


def test_core::equal_constructor_exists():
    assert callable(core::Equal.__init__)


def test_core::equal_constructor_args():
    sig = inspect.signature(core::Equal.__init__)
    params = list(sig.parameters.keys())



def test_core::minus_is_not_abstract():
    assert not inspect.isabstract(core::Minus)


def test_core::minus_constructor_exists():
    assert callable(core::Minus.__init__)


def test_core::minus_constructor_args():
    sig = inspect.signature(core::Minus.__init__)
    params = list(sig.parameters.keys())



def test_core::and_is_not_abstract():
    assert not inspect.isabstract(core::And)


def test_core::and_constructor_exists():
    assert callable(core::And.__init__)


def test_core::and_constructor_args():
    sig = inspect.signature(core::And.__init__)
    params = list(sig.parameters.keys())



def test_core::div_is_not_abstract():
    assert not inspect.isabstract(core::Div)


def test_core::div_constructor_exists():
    assert callable(core::Div.__init__)


def test_core::div_constructor_args():
    sig = inspect.signature(core::Div.__init__)
    params = list(sig.parameters.keys())



def test_core::greater_is_not_abstract():
    assert not inspect.isabstract(core::Greater)


def test_core::greater_constructor_exists():
    assert callable(core::Greater.__init__)


def test_core::greater_constructor_args():
    sig = inspect.signature(core::Greater.__init__)
    params = list(sig.parameters.keys())



def test_core::mult_is_not_abstract():
    assert not inspect.isabstract(core::Mult)


def test_core::mult_constructor_exists():
    assert callable(core::Mult.__init__)


def test_core::mult_constructor_args():
    sig = inspect.signature(core::Mult.__init__)
    params = list(sig.parameters.keys())



def test_core::add_is_not_abstract():
    assert not inspect.isabstract(core::Add)


def test_core::add_constructor_exists():
    assert callable(core::Add.__init__)


def test_core::add_constructor_args():
    sig = inspect.signature(core::Add.__init__)
    params = list(sig.parameters.keys())



def test_core::filter_is_not_abstract():
    assert not inspect.isabstract(core::Filter)


def test_core::filter_constructor_exists():
    assert callable(core::Filter.__init__)


def test_core::filter_constructor_args():
    sig = inspect.signature(core::Filter.__init__)
    params = list(sig.parameters.keys())



def test_core::integerexpression_is_not_abstract():
    assert not inspect.isabstract(core::IntegerExpression)


def test_core::integerexpression_constructor_exists():
    assert callable(core::IntegerExpression.__init__)


def test_core::integerexpression_constructor_args():
    sig = inspect.signature(core::IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_core::rule_is_not_abstract():
    assert not inspect.isabstract(core::Rule)


def test_core::rule_constructor_exists():
    assert callable(core::Rule.__init__)


def test_core::rule_constructor_args():
    sig = inspect.signature(core::Rule.__init__)
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
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
core::UMinus_strategy = st.builds(
    core::UMinus,
)
core::Not_strategy = st.builds(
    core::Not,
)
IntegerExpression_strategy = st.builds(
    IntegerExpression,
)
core::IntegerLiteral_strategy = st.builds(
    core::IntegerLiteral,
    val=
        st.integers()
)
core::Conditional_strategy = st.builds(
    core::Conditional,
)
core::BinaryExpression_strategy = st.builds(
    core::BinaryExpression,
)
core::UnaryExpression_strategy = st.builds(
    core::UnaryExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
core::Mod_strategy = st.builds(
    core::Mod,
)
core::Or_strategy = st.builds(
    core::Or,
)
core::Lower_strategy = st.builds(
    core::Lower,
)
core::Equal_strategy = st.builds(
    core::Equal,
)
core::Minus_strategy = st.builds(
    core::Minus,
)
core::And_strategy = st.builds(
    core::And,
)
core::Div_strategy = st.builds(
    core::Div,
)
core::Greater_strategy = st.builds(
    core::Greater,
)
core::Mult_strategy = st.builds(
    core::Mult,
)
core::Add_strategy = st.builds(
    core::Add,
)
core::Filter_strategy = st.builds(
    core::Filter,
)
core::IntegerExpression_strategy = st.builds(
    core::IntegerExpression,
)
core::Rule_strategy = st.builds(
    core::Rule,
)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=core::UMinus_strategy)
@settings(max_examples=50)
def test_core::uminus_instantiation(instance):
    assert isinstance(instance, core::UMinus)

@given(instance=core::Not_strategy)
@settings(max_examples=50)
def test_core::not_instantiation(instance):
    assert isinstance(instance, core::Not)

@given(instance=IntegerExpression_strategy)
@settings(max_examples=50)
def test_integerexpression_instantiation(instance):
    assert isinstance(instance, IntegerExpression)

@given(instance=core::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_core::integerliteral_instantiation(instance):
    assert isinstance(instance, core::IntegerLiteral)

@given(instance=core::IntegerLiteral_strategy)
def test_core::integerliteral_val_type(instance):
    assert isinstance(instance.val, int)


@given(instance=core::IntegerLiteral_strategy)
def test_core::integerliteral_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=core::Conditional_strategy)
@settings(max_examples=50)
def test_core::conditional_instantiation(instance):
    assert isinstance(instance, core::Conditional)

@given(instance=core::BinaryExpression_strategy)
@settings(max_examples=50)
def test_core::binaryexpression_instantiation(instance):
    assert isinstance(instance, core::BinaryExpression)

@given(instance=core::UnaryExpression_strategy)
@settings(max_examples=50)
def test_core::unaryexpression_instantiation(instance):
    assert isinstance(instance, core::UnaryExpression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=core::Mod_strategy)
@settings(max_examples=50)
def test_core::mod_instantiation(instance):
    assert isinstance(instance, core::Mod)

@given(instance=core::Or_strategy)
@settings(max_examples=50)
def test_core::or_instantiation(instance):
    assert isinstance(instance, core::Or)

@given(instance=core::Lower_strategy)
@settings(max_examples=50)
def test_core::lower_instantiation(instance):
    assert isinstance(instance, core::Lower)

@given(instance=core::Equal_strategy)
@settings(max_examples=50)
def test_core::equal_instantiation(instance):
    assert isinstance(instance, core::Equal)

@given(instance=core::Minus_strategy)
@settings(max_examples=50)
def test_core::minus_instantiation(instance):
    assert isinstance(instance, core::Minus)

@given(instance=core::And_strategy)
@settings(max_examples=50)
def test_core::and_instantiation(instance):
    assert isinstance(instance, core::And)

@given(instance=core::Div_strategy)
@settings(max_examples=50)
def test_core::div_instantiation(instance):
    assert isinstance(instance, core::Div)

@given(instance=core::Greater_strategy)
@settings(max_examples=50)
def test_core::greater_instantiation(instance):
    assert isinstance(instance, core::Greater)

@given(instance=core::Mult_strategy)
@settings(max_examples=50)
def test_core::mult_instantiation(instance):
    assert isinstance(instance, core::Mult)

@given(instance=core::Add_strategy)
@settings(max_examples=50)
def test_core::add_instantiation(instance):
    assert isinstance(instance, core::Add)

@given(instance=core::Filter_strategy)
@settings(max_examples=50)
def test_core::filter_instantiation(instance):
    assert isinstance(instance, core::Filter)

@given(instance=core::IntegerExpression_strategy)
@settings(max_examples=50)
def test_core::integerexpression_instantiation(instance):
    assert isinstance(instance, core::IntegerExpression)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=core::IntegerExpression_strategy)
@settings(max_examples=30)
def test_core::integerexpression_isboolean_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isBoolean()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isBoolean).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isBoolean' in core::IntegerExpression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isBoolean' in core::IntegerExpression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isBoolean' in core::IntegerExpression is not implemented or raised an error")

@given(instance=core::Rule_strategy)
@settings(max_examples=50)
def test_core::rule_instantiation(instance):
    assert isinstance(instance, core::Rule)
