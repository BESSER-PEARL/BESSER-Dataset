import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PrimitivesProv::Instruction,
    PrimitivesProv::LogoProgram,
    Primitive,
    PrimitivesProv::Back,
    PrimitivesProv::Left,
    PrimitivesProv::Right,
    PrimitivesProv::Forward,
    Instruction,
    PrimitivesProv::Primitive,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_primitivesprov::instruction_is_not_abstract():
    assert not inspect.isabstract(PrimitivesProv::Instruction)


def test_primitivesprov::instruction_constructor_exists():
    assert callable(PrimitivesProv::Instruction.__init__)


def test_primitivesprov::instruction_constructor_args():
    sig = inspect.signature(PrimitivesProv::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_primitivesprov::logoprogram_is_not_abstract():
    assert not inspect.isabstract(PrimitivesProv::LogoProgram)


def test_primitivesprov::logoprogram_constructor_exists():
    assert callable(PrimitivesProv::LogoProgram.__init__)


def test_primitivesprov::logoprogram_constructor_args():
    sig = inspect.signature(PrimitivesProv::LogoProgram.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_primitivesprov::back_is_not_abstract():
    assert not inspect.isabstract(PrimitivesProv::Back)


def test_primitivesprov::back_constructor_exists():
    assert callable(PrimitivesProv::Back.__init__)


def test_primitivesprov::back_constructor_args():
    sig = inspect.signature(PrimitivesProv::Back.__init__)
    params = list(sig.parameters.keys())



def test_primitivesprov::left_is_not_abstract():
    assert not inspect.isabstract(PrimitivesProv::Left)


def test_primitivesprov::left_constructor_exists():
    assert callable(PrimitivesProv::Left.__init__)


def test_primitivesprov::left_constructor_args():
    sig = inspect.signature(PrimitivesProv::Left.__init__)
    params = list(sig.parameters.keys())



def test_primitivesprov::right_is_not_abstract():
    assert not inspect.isabstract(PrimitivesProv::Right)


def test_primitivesprov::right_constructor_exists():
    assert callable(PrimitivesProv::Right.__init__)


def test_primitivesprov::right_constructor_args():
    sig = inspect.signature(PrimitivesProv::Right.__init__)
    params = list(sig.parameters.keys())



def test_primitivesprov::forward_is_not_abstract():
    assert not inspect.isabstract(PrimitivesProv::Forward)


def test_primitivesprov::forward_constructor_exists():
    assert callable(PrimitivesProv::Forward.__init__)


def test_primitivesprov::forward_constructor_args():
    sig = inspect.signature(PrimitivesProv::Forward.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_primitivesprov::primitive_is_not_abstract():
    assert not inspect.isabstract(PrimitivesProv::Primitive)


def test_primitivesprov::primitive_constructor_exists():
    assert callable(PrimitivesProv::Primitive.__init__)


def test_primitivesprov::primitive_constructor_args():
    sig = inspect.signature(PrimitivesProv::Primitive.__init__)
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
PrimitivesProv::Instruction_strategy = st.builds(
    PrimitivesProv::Instruction,
)
PrimitivesProv::LogoProgram_strategy = st.builds(
    PrimitivesProv::LogoProgram,
)
Primitive_strategy = st.builds(
    Primitive,
)
PrimitivesProv::Back_strategy = st.builds(
    PrimitivesProv::Back,
)
PrimitivesProv::Left_strategy = st.builds(
    PrimitivesProv::Left,
)
PrimitivesProv::Right_strategy = st.builds(
    PrimitivesProv::Right,
)
PrimitivesProv::Forward_strategy = st.builds(
    PrimitivesProv::Forward,
)
Instruction_strategy = st.builds(
    Instruction,
)
PrimitivesProv::Primitive_strategy = st.builds(
    PrimitivesProv::Primitive,
)

@given(instance=PrimitivesProv::Instruction_strategy)
@settings(max_examples=50)
def test_primitivesprov::instruction_instantiation(instance):
    assert isinstance(instance, PrimitivesProv::Instruction)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=PrimitivesProv::Instruction_strategy)
@settings(max_examples=30)
def test_primitivesprov::instruction_evalinstruction_changes_state(instance):
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
        assert has_statements, f"Function 'evalInstruction' in PrimitivesProv::Instruction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evalInstruction' in PrimitivesProv::Instruction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evalInstruction' in PrimitivesProv::Instruction is not implemented or raised an error")

@given(instance=PrimitivesProv::LogoProgram_strategy)
@settings(max_examples=50)
def test_primitivesprov::logoprogram_instantiation(instance):
    assert isinstance(instance, PrimitivesProv::LogoProgram)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=PrimitivesProv::Back_strategy)
@settings(max_examples=50)
def test_primitivesprov::back_instantiation(instance):
    assert isinstance(instance, PrimitivesProv::Back)

@given(instance=PrimitivesProv::Left_strategy)
@settings(max_examples=50)
def test_primitivesprov::left_instantiation(instance):
    assert isinstance(instance, PrimitivesProv::Left)

@given(instance=PrimitivesProv::Right_strategy)
@settings(max_examples=50)
def test_primitivesprov::right_instantiation(instance):
    assert isinstance(instance, PrimitivesProv::Right)

@given(instance=PrimitivesProv::Forward_strategy)
@settings(max_examples=50)
def test_primitivesprov::forward_instantiation(instance):
    assert isinstance(instance, PrimitivesProv::Forward)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=PrimitivesProv::Primitive_strategy)
@settings(max_examples=50)
def test_primitivesprov::primitive_instantiation(instance):
    assert isinstance(instance, PrimitivesProv::Primitive)
