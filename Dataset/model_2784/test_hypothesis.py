import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    use_registered_classes_C,
    use_registered_classes_B,
    use_registered_classes_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_use_registered_classes_c_is_not_abstract():
    assert not inspect.isabstract(use_registered_classes_C)


def test_use_registered_classes_c_constructor_exists():
    assert callable(use_registered_classes_C.__init__)


def test_use_registered_classes_c_constructor_args():
    sig = inspect.signature(use_registered_classes_C.__init__)
    params = list(sig.parameters.keys())



def test_use_registered_classes_b_is_not_abstract():
    assert not inspect.isabstract(use_registered_classes_B)


def test_use_registered_classes_b_constructor_exists():
    assert callable(use_registered_classes_B.__init__)


def test_use_registered_classes_b_constructor_args():
    sig = inspect.signature(use_registered_classes_B.__init__)
    params = list(sig.parameters.keys())



def test_use_registered_classes_a_is_not_abstract():
    assert not inspect.isabstract(use_registered_classes_A)


def test_use_registered_classes_a_constructor_exists():
    assert callable(use_registered_classes_A.__init__)


def test_use_registered_classes_a_constructor_args():
    sig = inspect.signature(use_registered_classes_A.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "z" in params, "Missing parameter 'z'"

def test_use_registered_classes_a_has_x():
    assert hasattr(use_registered_classes_A, "x")
    descriptor = None
    for klass in use_registered_classes_A.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_use_registered_classes_a_has_y():
    assert hasattr(use_registered_classes_A, "y")
    descriptor = None
    for klass in use_registered_classes_A.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_use_registered_classes_a_has_z():
    assert hasattr(use_registered_classes_A, "z")
    descriptor = None
    for klass in use_registered_classes_A.__mro__:
        if "z" in klass.__dict__:
            descriptor = klass.__dict__["z"]
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
use_registered_classes_C_strategy = st.builds(
    use_registered_classes_C,
)
use_registered_classes_B_strategy = st.builds(
    use_registered_classes_B,
)
use_registered_classes_A_strategy = st.builds(
    use_registered_classes_A,
    x=
        st.integers(),
    y=
        safe_text,
    z=
        safe_text
)

@given(instance=use_registered_classes_C_strategy)
@settings(max_examples=50)
def test_use_registered_classes_c_instantiation(instance):
    assert isinstance(instance, use_registered_classes_C)

@given(instance=use_registered_classes_B_strategy)
@settings(max_examples=50)
def test_use_registered_classes_b_instantiation(instance):
    assert isinstance(instance, use_registered_classes_B)

@given(instance=use_registered_classes_A_strategy)
@settings(max_examples=50)
def test_use_registered_classes_a_instantiation(instance):
    assert isinstance(instance, use_registered_classes_A)



@given(instance=use_registered_classes_A_strategy)
def test_use_registered_classes_a_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=use_registered_classes_A_strategy)
def test_use_registered_classes_a_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=use_registered_classes_A_strategy)
def test_use_registered_classes_a_z_setter(instance):
    original = instance.z
    instance.z = original
    assert instance.z == original
