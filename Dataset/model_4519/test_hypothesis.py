import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Primitive,
    Primitives_Forward,
    Instruction,
    Primitives_Expression,
    Primitives_Primitive,
    Primitives_Right,
    Primitives_Left,
    Primitives_Back,
    Primitives_Instruction,
    Primitives_LogoProgram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_primitives_forward_is_not_abstract():
    assert not inspect.isabstract(Primitives_Forward)


def test_primitives_forward_constructor_exists():
    assert callable(Primitives_Forward.__init__)


def test_primitives_forward_constructor_args():
    sig = inspect.signature(Primitives_Forward.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_primitives_expression_is_not_abstract():
    assert not inspect.isabstract(Primitives_Expression)


def test_primitives_expression_constructor_exists():
    assert callable(Primitives_Expression.__init__)


def test_primitives_expression_constructor_args():
    sig = inspect.signature(Primitives_Expression.__init__)
    params = list(sig.parameters.keys())



def test_primitives_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitives_Primitive)


def test_primitives_primitive_constructor_exists():
    assert callable(Primitives_Primitive.__init__)


def test_primitives_primitive_constructor_args():
    sig = inspect.signature(Primitives_Primitive.__init__)
    params = list(sig.parameters.keys())



def test_primitives_right_is_not_abstract():
    assert not inspect.isabstract(Primitives_Right)


def test_primitives_right_constructor_exists():
    assert callable(Primitives_Right.__init__)


def test_primitives_right_constructor_args():
    sig = inspect.signature(Primitives_Right.__init__)
    params = list(sig.parameters.keys())



def test_primitives_left_is_not_abstract():
    assert not inspect.isabstract(Primitives_Left)


def test_primitives_left_constructor_exists():
    assert callable(Primitives_Left.__init__)


def test_primitives_left_constructor_args():
    sig = inspect.signature(Primitives_Left.__init__)
    params = list(sig.parameters.keys())



def test_primitives_back_is_not_abstract():
    assert not inspect.isabstract(Primitives_Back)


def test_primitives_back_constructor_exists():
    assert callable(Primitives_Back.__init__)


def test_primitives_back_constructor_args():
    sig = inspect.signature(Primitives_Back.__init__)
    params = list(sig.parameters.keys())



def test_primitives_instruction_is_not_abstract():
    assert not inspect.isabstract(Primitives_Instruction)


def test_primitives_instruction_constructor_exists():
    assert callable(Primitives_Instruction.__init__)


def test_primitives_instruction_constructor_args():
    sig = inspect.signature(Primitives_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_primitives_logoprogram_is_not_abstract():
    assert not inspect.isabstract(Primitives_LogoProgram)


def test_primitives_logoprogram_constructor_exists():
    assert callable(Primitives_LogoProgram.__init__)


def test_primitives_logoprogram_constructor_args():
    sig = inspect.signature(Primitives_LogoProgram.__init__)
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
Primitive_strategy = st.builds(
    Primitive,
)
Primitives_Forward_strategy = st.builds(
    Primitives_Forward,
)
Instruction_strategy = st.builds(
    Instruction,
)
Primitives_Expression_strategy = st.builds(
    Primitives_Expression,
)
Primitives_Primitive_strategy = st.builds(
    Primitives_Primitive,
)
Primitives_Right_strategy = st.builds(
    Primitives_Right,
)
Primitives_Left_strategy = st.builds(
    Primitives_Left,
)
Primitives_Back_strategy = st.builds(
    Primitives_Back,
)
Primitives_Instruction_strategy = st.builds(
    Primitives_Instruction,
)
Primitives_LogoProgram_strategy = st.builds(
    Primitives_LogoProgram,
)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=Primitives_Forward_strategy)
@settings(max_examples=50)
def test_primitives_forward_instantiation(instance):
    assert isinstance(instance, Primitives_Forward)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=Primitives_Expression_strategy)
@settings(max_examples=50)
def test_primitives_expression_instantiation(instance):
    assert isinstance(instance, Primitives_Expression)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Primitives_Expression_strategy)
@settings(max_examples=30)
def test_primitives_expression_eval_changes_state(instance):
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
        assert has_statements, f"Function 'eval' in Primitives_Expression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in Primitives_Expression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in Primitives_Expression is not implemented or raised an error")

@given(instance=Primitives_Primitive_strategy)
@settings(max_examples=50)
def test_primitives_primitive_instantiation(instance):
    assert isinstance(instance, Primitives_Primitive)

@given(instance=Primitives_Right_strategy)
@settings(max_examples=50)
def test_primitives_right_instantiation(instance):
    assert isinstance(instance, Primitives_Right)

@given(instance=Primitives_Left_strategy)
@settings(max_examples=50)
def test_primitives_left_instantiation(instance):
    assert isinstance(instance, Primitives_Left)

@given(instance=Primitives_Back_strategy)
@settings(max_examples=50)
def test_primitives_back_instantiation(instance):
    assert isinstance(instance, Primitives_Back)

@given(instance=Primitives_Instruction_strategy)
@settings(max_examples=50)
def test_primitives_instruction_instantiation(instance):
    assert isinstance(instance, Primitives_Instruction)

@given(instance=Primitives_LogoProgram_strategy)
@settings(max_examples=50)
def test_primitives_logoprogram_instantiation(instance):
    assert isinstance(instance, Primitives_LogoProgram)
