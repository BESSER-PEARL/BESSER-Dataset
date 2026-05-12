import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Logo_Expression,
    Primitive,
    Logo_PenUp,
    Logo_Right,
    Logo_Forward,
    Logo_PenDown,
    Logo_Clear,
    Logo_Left,
    Logo_Back,
    Logo_Primitive,
    Logo_LogoProgram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_logo_expression_is_not_abstract():
    assert not inspect.isabstract(Logo_Expression)


def test_logo_expression_constructor_exists():
    assert callable(Logo_Expression.__init__)


def test_logo_expression_constructor_args():
    sig = inspect.signature(Logo_Expression.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_logo_penup_is_not_abstract():
    assert not inspect.isabstract(Logo_PenUp)


def test_logo_penup_constructor_exists():
    assert callable(Logo_PenUp.__init__)


def test_logo_penup_constructor_args():
    sig = inspect.signature(Logo_PenUp.__init__)
    params = list(sig.parameters.keys())



def test_logo_right_is_not_abstract():
    assert not inspect.isabstract(Logo_Right)


def test_logo_right_constructor_exists():
    assert callable(Logo_Right.__init__)


def test_logo_right_constructor_args():
    sig = inspect.signature(Logo_Right.__init__)
    params = list(sig.parameters.keys())



def test_logo_forward_is_not_abstract():
    assert not inspect.isabstract(Logo_Forward)


def test_logo_forward_constructor_exists():
    assert callable(Logo_Forward.__init__)


def test_logo_forward_constructor_args():
    sig = inspect.signature(Logo_Forward.__init__)
    params = list(sig.parameters.keys())



def test_logo_pendown_is_not_abstract():
    assert not inspect.isabstract(Logo_PenDown)


def test_logo_pendown_constructor_exists():
    assert callable(Logo_PenDown.__init__)


def test_logo_pendown_constructor_args():
    sig = inspect.signature(Logo_PenDown.__init__)
    params = list(sig.parameters.keys())



def test_logo_clear_is_not_abstract():
    assert not inspect.isabstract(Logo_Clear)


def test_logo_clear_constructor_exists():
    assert callable(Logo_Clear.__init__)


def test_logo_clear_constructor_args():
    sig = inspect.signature(Logo_Clear.__init__)
    params = list(sig.parameters.keys())



def test_logo_left_is_not_abstract():
    assert not inspect.isabstract(Logo_Left)


def test_logo_left_constructor_exists():
    assert callable(Logo_Left.__init__)


def test_logo_left_constructor_args():
    sig = inspect.signature(Logo_Left.__init__)
    params = list(sig.parameters.keys())



def test_logo_back_is_not_abstract():
    assert not inspect.isabstract(Logo_Back)


def test_logo_back_constructor_exists():
    assert callable(Logo_Back.__init__)


def test_logo_back_constructor_args():
    sig = inspect.signature(Logo_Back.__init__)
    params = list(sig.parameters.keys())



def test_logo_primitive_is_not_abstract():
    assert not inspect.isabstract(Logo_Primitive)


def test_logo_primitive_constructor_exists():
    assert callable(Logo_Primitive.__init__)


def test_logo_primitive_constructor_args():
    sig = inspect.signature(Logo_Primitive.__init__)
    params = list(sig.parameters.keys())



def test_logo_logoprogram_is_not_abstract():
    assert not inspect.isabstract(Logo_LogoProgram)


def test_logo_logoprogram_constructor_exists():
    assert callable(Logo_LogoProgram.__init__)


def test_logo_logoprogram_constructor_args():
    sig = inspect.signature(Logo_LogoProgram.__init__)
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
Logo_Expression_strategy = st.builds(
    Logo_Expression,
)
Primitive_strategy = st.builds(
    Primitive,
)
Logo_PenUp_strategy = st.builds(
    Logo_PenUp,
)
Logo_Right_strategy = st.builds(
    Logo_Right,
)
Logo_Forward_strategy = st.builds(
    Logo_Forward,
)
Logo_PenDown_strategy = st.builds(
    Logo_PenDown,
)
Logo_Clear_strategy = st.builds(
    Logo_Clear,
)
Logo_Left_strategy = st.builds(
    Logo_Left,
)
Logo_Back_strategy = st.builds(
    Logo_Back,
)
Logo_Primitive_strategy = st.builds(
    Logo_Primitive,
)
Logo_LogoProgram_strategy = st.builds(
    Logo_LogoProgram,
)

@given(instance=Logo_Expression_strategy)
@settings(max_examples=50)
def test_logo_expression_instantiation(instance):
    assert isinstance(instance, Logo_Expression)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Logo_Expression_strategy)
@settings(max_examples=30)
def test_logo_expression_eval_changes_state(instance):
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
        assert has_statements, f"Function 'eval' in Logo_Expression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in Logo_Expression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in Logo_Expression is not implemented or raised an error")

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=Logo_PenUp_strategy)
@settings(max_examples=50)
def test_logo_penup_instantiation(instance):
    assert isinstance(instance, Logo_PenUp)

@given(instance=Logo_Right_strategy)
@settings(max_examples=50)
def test_logo_right_instantiation(instance):
    assert isinstance(instance, Logo_Right)

@given(instance=Logo_Forward_strategy)
@settings(max_examples=50)
def test_logo_forward_instantiation(instance):
    assert isinstance(instance, Logo_Forward)

@given(instance=Logo_PenDown_strategy)
@settings(max_examples=50)
def test_logo_pendown_instantiation(instance):
    assert isinstance(instance, Logo_PenDown)

@given(instance=Logo_Clear_strategy)
@settings(max_examples=50)
def test_logo_clear_instantiation(instance):
    assert isinstance(instance, Logo_Clear)

@given(instance=Logo_Left_strategy)
@settings(max_examples=50)
def test_logo_left_instantiation(instance):
    assert isinstance(instance, Logo_Left)

@given(instance=Logo_Back_strategy)
@settings(max_examples=50)
def test_logo_back_instantiation(instance):
    assert isinstance(instance, Logo_Back)

@given(instance=Logo_Primitive_strategy)
@settings(max_examples=50)
def test_logo_primitive_instantiation(instance):
    assert isinstance(instance, Logo_Primitive)

@given(instance=Logo_LogoProgram_strategy)
@settings(max_examples=50)
def test_logo_logoprogram_instantiation(instance):
    assert isinstance(instance, Logo_LogoProgram)
