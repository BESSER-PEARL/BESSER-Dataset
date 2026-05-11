import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Logo::Expression,
    Primitive,
    Logo::Left,
    Logo::Clear,
    Logo::Forward,
    Logo::Right,
    Logo::PenUp,
    Logo::PenDown,
    Logo::Back,
    Logo::Primitive,
    Logo::LogoProgram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_logo::expression_is_not_abstract():
    assert not inspect.isabstract(Logo::Expression)


def test_logo::expression_constructor_exists():
    assert callable(Logo::Expression.__init__)


def test_logo::expression_constructor_args():
    sig = inspect.signature(Logo::Expression.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_logo::left_is_not_abstract():
    assert not inspect.isabstract(Logo::Left)


def test_logo::left_constructor_exists():
    assert callable(Logo::Left.__init__)


def test_logo::left_constructor_args():
    sig = inspect.signature(Logo::Left.__init__)
    params = list(sig.parameters.keys())



def test_logo::clear_is_not_abstract():
    assert not inspect.isabstract(Logo::Clear)


def test_logo::clear_constructor_exists():
    assert callable(Logo::Clear.__init__)


def test_logo::clear_constructor_args():
    sig = inspect.signature(Logo::Clear.__init__)
    params = list(sig.parameters.keys())



def test_logo::forward_is_not_abstract():
    assert not inspect.isabstract(Logo::Forward)


def test_logo::forward_constructor_exists():
    assert callable(Logo::Forward.__init__)


def test_logo::forward_constructor_args():
    sig = inspect.signature(Logo::Forward.__init__)
    params = list(sig.parameters.keys())



def test_logo::right_is_not_abstract():
    assert not inspect.isabstract(Logo::Right)


def test_logo::right_constructor_exists():
    assert callable(Logo::Right.__init__)


def test_logo::right_constructor_args():
    sig = inspect.signature(Logo::Right.__init__)
    params = list(sig.parameters.keys())



def test_logo::penup_is_not_abstract():
    assert not inspect.isabstract(Logo::PenUp)


def test_logo::penup_constructor_exists():
    assert callable(Logo::PenUp.__init__)


def test_logo::penup_constructor_args():
    sig = inspect.signature(Logo::PenUp.__init__)
    params = list(sig.parameters.keys())



def test_logo::pendown_is_not_abstract():
    assert not inspect.isabstract(Logo::PenDown)


def test_logo::pendown_constructor_exists():
    assert callable(Logo::PenDown.__init__)


def test_logo::pendown_constructor_args():
    sig = inspect.signature(Logo::PenDown.__init__)
    params = list(sig.parameters.keys())



def test_logo::back_is_not_abstract():
    assert not inspect.isabstract(Logo::Back)


def test_logo::back_constructor_exists():
    assert callable(Logo::Back.__init__)


def test_logo::back_constructor_args():
    sig = inspect.signature(Logo::Back.__init__)
    params = list(sig.parameters.keys())



def test_logo::primitive_is_not_abstract():
    assert not inspect.isabstract(Logo::Primitive)


def test_logo::primitive_constructor_exists():
    assert callable(Logo::Primitive.__init__)


def test_logo::primitive_constructor_args():
    sig = inspect.signature(Logo::Primitive.__init__)
    params = list(sig.parameters.keys())



def test_logo::logoprogram_is_not_abstract():
    assert not inspect.isabstract(Logo::LogoProgram)


def test_logo::logoprogram_constructor_exists():
    assert callable(Logo::LogoProgram.__init__)


def test_logo::logoprogram_constructor_args():
    sig = inspect.signature(Logo::LogoProgram.__init__)
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
Logo::Expression_strategy = st.builds(
    Logo::Expression,
)
Primitive_strategy = st.builds(
    Primitive,
)
Logo::Left_strategy = st.builds(
    Logo::Left,
)
Logo::Clear_strategy = st.builds(
    Logo::Clear,
)
Logo::Forward_strategy = st.builds(
    Logo::Forward,
)
Logo::Right_strategy = st.builds(
    Logo::Right,
)
Logo::PenUp_strategy = st.builds(
    Logo::PenUp,
)
Logo::PenDown_strategy = st.builds(
    Logo::PenDown,
)
Logo::Back_strategy = st.builds(
    Logo::Back,
)
Logo::Primitive_strategy = st.builds(
    Logo::Primitive,
)
Logo::LogoProgram_strategy = st.builds(
    Logo::LogoProgram,
)

@given(instance=Logo::Expression_strategy)
@settings(max_examples=50)
def test_logo::expression_instantiation(instance):
    assert isinstance(instance, Logo::Expression)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Logo::Expression_strategy)
@settings(max_examples=30)
def test_logo::expression_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in Logo::Expression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in Logo::Expression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in Logo::Expression is not implemented or raised an error")

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=Logo::Left_strategy)
@settings(max_examples=50)
def test_logo::left_instantiation(instance):
    assert isinstance(instance, Logo::Left)

@given(instance=Logo::Clear_strategy)
@settings(max_examples=50)
def test_logo::clear_instantiation(instance):
    assert isinstance(instance, Logo::Clear)

@given(instance=Logo::Forward_strategy)
@settings(max_examples=50)
def test_logo::forward_instantiation(instance):
    assert isinstance(instance, Logo::Forward)

@given(instance=Logo::Right_strategy)
@settings(max_examples=50)
def test_logo::right_instantiation(instance):
    assert isinstance(instance, Logo::Right)

@given(instance=Logo::PenUp_strategy)
@settings(max_examples=50)
def test_logo::penup_instantiation(instance):
    assert isinstance(instance, Logo::PenUp)

@given(instance=Logo::PenDown_strategy)
@settings(max_examples=50)
def test_logo::pendown_instantiation(instance):
    assert isinstance(instance, Logo::PenDown)

@given(instance=Logo::Back_strategy)
@settings(max_examples=50)
def test_logo::back_instantiation(instance):
    assert isinstance(instance, Logo::Back)

@given(instance=Logo::Primitive_strategy)
@settings(max_examples=50)
def test_logo::primitive_instantiation(instance):
    assert isinstance(instance, Logo::Primitive)

@given(instance=Logo::LogoProgram_strategy)
@settings(max_examples=50)
def test_logo::logoprogram_instantiation(instance):
    assert isinstance(instance, Logo::LogoProgram)
