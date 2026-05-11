import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Primitive,
    Primitives::Forward,
    Instruction,
    Primitives::Expression,
    Primitives::Primitive,
    Primitives::Right,
    Primitives::Left,
    Primitives::Back,
    Primitives::Instruction,
    Primitives::LogoProgram,
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



def test_primitives::forward_is_not_abstract():
    assert not inspect.isabstract(Primitives::Forward)


def test_primitives::forward_constructor_exists():
    assert callable(Primitives::Forward.__init__)


def test_primitives::forward_constructor_args():
    sig = inspect.signature(Primitives::Forward.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_primitives::expression_is_not_abstract():
    assert not inspect.isabstract(Primitives::Expression)


def test_primitives::expression_constructor_exists():
    assert callable(Primitives::Expression.__init__)


def test_primitives::expression_constructor_args():
    sig = inspect.signature(Primitives::Expression.__init__)
    params = list(sig.parameters.keys())



def test_primitives::primitive_is_not_abstract():
    assert not inspect.isabstract(Primitives::Primitive)


def test_primitives::primitive_constructor_exists():
    assert callable(Primitives::Primitive.__init__)


def test_primitives::primitive_constructor_args():
    sig = inspect.signature(Primitives::Primitive.__init__)
    params = list(sig.parameters.keys())



def test_primitives::right_is_not_abstract():
    assert not inspect.isabstract(Primitives::Right)


def test_primitives::right_constructor_exists():
    assert callable(Primitives::Right.__init__)


def test_primitives::right_constructor_args():
    sig = inspect.signature(Primitives::Right.__init__)
    params = list(sig.parameters.keys())



def test_primitives::left_is_not_abstract():
    assert not inspect.isabstract(Primitives::Left)


def test_primitives::left_constructor_exists():
    assert callable(Primitives::Left.__init__)


def test_primitives::left_constructor_args():
    sig = inspect.signature(Primitives::Left.__init__)
    params = list(sig.parameters.keys())



def test_primitives::back_is_not_abstract():
    assert not inspect.isabstract(Primitives::Back)


def test_primitives::back_constructor_exists():
    assert callable(Primitives::Back.__init__)


def test_primitives::back_constructor_args():
    sig = inspect.signature(Primitives::Back.__init__)
    params = list(sig.parameters.keys())



def test_primitives::instruction_is_not_abstract():
    assert not inspect.isabstract(Primitives::Instruction)


def test_primitives::instruction_constructor_exists():
    assert callable(Primitives::Instruction.__init__)


def test_primitives::instruction_constructor_args():
    sig = inspect.signature(Primitives::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_primitives::logoprogram_is_not_abstract():
    assert not inspect.isabstract(Primitives::LogoProgram)


def test_primitives::logoprogram_constructor_exists():
    assert callable(Primitives::LogoProgram.__init__)


def test_primitives::logoprogram_constructor_args():
    sig = inspect.signature(Primitives::LogoProgram.__init__)
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
Primitives::Forward_strategy = st.builds(
    Primitives::Forward,
)
Instruction_strategy = st.builds(
    Instruction,
)
Primitives::Expression_strategy = st.builds(
    Primitives::Expression,
)
Primitives::Primitive_strategy = st.builds(
    Primitives::Primitive,
)
Primitives::Right_strategy = st.builds(
    Primitives::Right,
)
Primitives::Left_strategy = st.builds(
    Primitives::Left,
)
Primitives::Back_strategy = st.builds(
    Primitives::Back,
)
Primitives::Instruction_strategy = st.builds(
    Primitives::Instruction,
)
Primitives::LogoProgram_strategy = st.builds(
    Primitives::LogoProgram,
)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=Primitives::Forward_strategy)
@settings(max_examples=50)
def test_primitives::forward_instantiation(instance):
    assert isinstance(instance, Primitives::Forward)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=Primitives::Expression_strategy)
@settings(max_examples=50)
def test_primitives::expression_instantiation(instance):
    assert isinstance(instance, Primitives::Expression)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Primitives::Expression_strategy)
@settings(max_examples=30)
def test_primitives::expression_eval_changes_state(instance):
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
        assert has_statements, f"Function 'eval' in Primitives::Expression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in Primitives::Expression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in Primitives::Expression is not implemented or raised an error")

@given(instance=Primitives::Primitive_strategy)
@settings(max_examples=50)
def test_primitives::primitive_instantiation(instance):
    assert isinstance(instance, Primitives::Primitive)

@given(instance=Primitives::Right_strategy)
@settings(max_examples=50)
def test_primitives::right_instantiation(instance):
    assert isinstance(instance, Primitives::Right)

@given(instance=Primitives::Left_strategy)
@settings(max_examples=50)
def test_primitives::left_instantiation(instance):
    assert isinstance(instance, Primitives::Left)

@given(instance=Primitives::Back_strategy)
@settings(max_examples=50)
def test_primitives::back_instantiation(instance):
    assert isinstance(instance, Primitives::Back)

@given(instance=Primitives::Instruction_strategy)
@settings(max_examples=50)
def test_primitives::instruction_instantiation(instance):
    assert isinstance(instance, Primitives::Instruction)

@given(instance=Primitives::LogoProgram_strategy)
@settings(max_examples=50)
def test_primitives::logoprogram_instantiation(instance):
    assert isinstance(instance, Primitives::LogoProgram)
