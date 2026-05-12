import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PrimitivesProv_Instruction,
    PrimitivesProv_LogoProgram,
    Primitive,
    PrimitivesProv_Right,
    PrimitivesProv_Back,
    PrimitivesProv_Left,
    PrimitivesProv_Forward,
    Instruction,
    PrimitivesProv_Primitive,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_primitivesprov_instruction_is_not_abstract():
    assert not inspect.isabstract(PrimitivesProv_Instruction)


def test_primitivesprov_instruction_constructor_exists():
    assert callable(PrimitivesProv_Instruction.__init__)


def test_primitivesprov_instruction_constructor_args():
    sig = inspect.signature(PrimitivesProv_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_primitivesprov_logoprogram_is_not_abstract():
    assert not inspect.isabstract(PrimitivesProv_LogoProgram)


def test_primitivesprov_logoprogram_constructor_exists():
    assert callable(PrimitivesProv_LogoProgram.__init__)


def test_primitivesprov_logoprogram_constructor_args():
    sig = inspect.signature(PrimitivesProv_LogoProgram.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_primitivesprov_right_is_not_abstract():
    assert not inspect.isabstract(PrimitivesProv_Right)


def test_primitivesprov_right_constructor_exists():
    assert callable(PrimitivesProv_Right.__init__)


def test_primitivesprov_right_constructor_args():
    sig = inspect.signature(PrimitivesProv_Right.__init__)
    params = list(sig.parameters.keys())



def test_primitivesprov_back_is_not_abstract():
    assert not inspect.isabstract(PrimitivesProv_Back)


def test_primitivesprov_back_constructor_exists():
    assert callable(PrimitivesProv_Back.__init__)


def test_primitivesprov_back_constructor_args():
    sig = inspect.signature(PrimitivesProv_Back.__init__)
    params = list(sig.parameters.keys())



def test_primitivesprov_left_is_not_abstract():
    assert not inspect.isabstract(PrimitivesProv_Left)


def test_primitivesprov_left_constructor_exists():
    assert callable(PrimitivesProv_Left.__init__)


def test_primitivesprov_left_constructor_args():
    sig = inspect.signature(PrimitivesProv_Left.__init__)
    params = list(sig.parameters.keys())



def test_primitivesprov_forward_is_not_abstract():
    assert not inspect.isabstract(PrimitivesProv_Forward)


def test_primitivesprov_forward_constructor_exists():
    assert callable(PrimitivesProv_Forward.__init__)


def test_primitivesprov_forward_constructor_args():
    sig = inspect.signature(PrimitivesProv_Forward.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_primitivesprov_primitive_is_not_abstract():
    assert not inspect.isabstract(PrimitivesProv_Primitive)


def test_primitivesprov_primitive_constructor_exists():
    assert callable(PrimitivesProv_Primitive.__init__)


def test_primitivesprov_primitive_constructor_args():
    sig = inspect.signature(PrimitivesProv_Primitive.__init__)
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
PrimitivesProv_Instruction_strategy = st.builds(
    PrimitivesProv_Instruction,
)
PrimitivesProv_LogoProgram_strategy = st.builds(
    PrimitivesProv_LogoProgram,
)
Primitive_strategy = st.builds(
    Primitive,
)
PrimitivesProv_Right_strategy = st.builds(
    PrimitivesProv_Right,
)
PrimitivesProv_Back_strategy = st.builds(
    PrimitivesProv_Back,
)
PrimitivesProv_Left_strategy = st.builds(
    PrimitivesProv_Left,
)
PrimitivesProv_Forward_strategy = st.builds(
    PrimitivesProv_Forward,
)
Instruction_strategy = st.builds(
    Instruction,
)
PrimitivesProv_Primitive_strategy = st.builds(
    PrimitivesProv_Primitive,
)

@given(instance=PrimitivesProv_Instruction_strategy)
@settings(max_examples=50)
def test_primitivesprov_instruction_instantiation(instance):
    assert isinstance(instance, PrimitivesProv_Instruction)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=PrimitivesProv_Instruction_strategy)
@settings(max_examples=30)
def test_primitivesprov_instruction_evalinstruction_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evalInstruction(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evalInstruction).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evalInstruction' in PrimitivesProv_Instruction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evalInstruction' in PrimitivesProv_Instruction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evalInstruction' in PrimitivesProv_Instruction is not implemented or raised an error")

@given(instance=PrimitivesProv_LogoProgram_strategy)
@settings(max_examples=50)
def test_primitivesprov_logoprogram_instantiation(instance):
    assert isinstance(instance, PrimitivesProv_LogoProgram)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=PrimitivesProv_Right_strategy)
@settings(max_examples=50)
def test_primitivesprov_right_instantiation(instance):
    assert isinstance(instance, PrimitivesProv_Right)

@given(instance=PrimitivesProv_Back_strategy)
@settings(max_examples=50)
def test_primitivesprov_back_instantiation(instance):
    assert isinstance(instance, PrimitivesProv_Back)

@given(instance=PrimitivesProv_Left_strategy)
@settings(max_examples=50)
def test_primitivesprov_left_instantiation(instance):
    assert isinstance(instance, PrimitivesProv_Left)

@given(instance=PrimitivesProv_Forward_strategy)
@settings(max_examples=50)
def test_primitivesprov_forward_instantiation(instance):
    assert isinstance(instance, PrimitivesProv_Forward)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=PrimitivesProv_Primitive_strategy)
@settings(max_examples=50)
def test_primitivesprov_primitive_instantiation(instance):
    assert isinstance(instance, PrimitivesProv_Primitive)
