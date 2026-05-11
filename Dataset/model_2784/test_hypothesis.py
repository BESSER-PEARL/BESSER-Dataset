import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    use::registered::classes::C,
    use::registered::classes::B,
    use::registered::classes::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_use::registered::classes::c_is_not_abstract():
    assert not inspect.isabstract(use::registered::classes::C)


def test_use::registered::classes::c_constructor_exists():
    assert callable(use::registered::classes::C.__init__)


def test_use::registered::classes::c_constructor_args():
    sig = inspect.signature(use::registered::classes::C.__init__)
    params = list(sig.parameters.keys())



def test_use::registered::classes::b_is_not_abstract():
    assert not inspect.isabstract(use::registered::classes::B)


def test_use::registered::classes::b_constructor_exists():
    assert callable(use::registered::classes::B.__init__)


def test_use::registered::classes::b_constructor_args():
    sig = inspect.signature(use::registered::classes::B.__init__)
    params = list(sig.parameters.keys())



def test_use::registered::classes::a_is_not_abstract():
    assert not inspect.isabstract(use::registered::classes::A)


def test_use::registered::classes::a_constructor_exists():
    assert callable(use::registered::classes::A.__init__)


def test_use::registered::classes::a_constructor_args():
    sig = inspect.signature(use::registered::classes::A.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "z" in params, "Missing parameter 'z'"

def test_use::registered::classes::a_has_x():
    assert hasattr(use::registered::classes::A, "x")
    descriptor = None
    for klass in use::registered::classes::A.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_use::registered::classes::a_has_y():
    assert hasattr(use::registered::classes::A, "y")
    descriptor = None
    for klass in use::registered::classes::A.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_use::registered::classes::a_has_z():
    assert hasattr(use::registered::classes::A, "z")
    descriptor = None
    for klass in use::registered::classes::A.__mro__:
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
use::registered::classes::C_strategy = st.builds(
    use::registered::classes::C,
)
use::registered::classes::B_strategy = st.builds(
    use::registered::classes::B,
)
use::registered::classes::A_strategy = st.builds(
    use::registered::classes::A,
    x=
        st.integers(),
    y=
        safe_text,
    z=
        safe_text
)

@given(instance=use::registered::classes::C_strategy)
@settings(max_examples=50)
def test_use::registered::classes::c_instantiation(instance):
    assert isinstance(instance, use::registered::classes::C)

@given(instance=use::registered::classes::B_strategy)
@settings(max_examples=50)
def test_use::registered::classes::b_instantiation(instance):
    assert isinstance(instance, use::registered::classes::B)

@given(instance=use::registered::classes::A_strategy)
@settings(max_examples=50)
def test_use::registered::classes::a_instantiation(instance):
    assert isinstance(instance, use::registered::classes::A)

@given(instance=use::registered::classes::A_strategy)
def test_use::registered::classes::a_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=use::registered::classes::A_strategy)
def test_use::registered::classes::a_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=use::registered::classes::A_strategy)
def test_use::registered::classes::a_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=use::registered::classes::A_strategy)
def test_use::registered::classes::a_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=use::registered::classes::A_strategy)
def test_use::registered::classes::a_z_type(instance):
    assert isinstance(instance.z, str)


@given(instance=use::registered::classes::A_strategy)
def test_use::registered::classes::a_z_setter(instance):
    original = instance.z
    instance.z = original
    assert instance.z == original
