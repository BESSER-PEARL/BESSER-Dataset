import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    a_B,
    a_A,
    a_Root,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_b_is_not_abstract():
    assert not inspect.isabstract(a_B)


def test_a_b_constructor_exists():
    assert callable(a_B.__init__)


def test_a_b_constructor_args():
    sig = inspect.signature(a_B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_a_b_has_name():
    assert hasattr(a_B, "name")
    descriptor = None
    for klass in a_B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_a_a_is_not_abstract():
    assert not inspect.isabstract(a_A)


def test_a_a_constructor_exists():
    assert callable(a_A.__init__)


def test_a_a_constructor_args():
    sig = inspect.signature(a_A.__init__)
    params = list(sig.parameters.keys())
    assert "names" in params, "Missing parameter 'names'"
    assert "tob" in params, "Missing parameter 'tob'"

def test_a_a_has_names():
    assert hasattr(a_A, "names")
    descriptor = None
    for klass in a_A.__mro__:
        if "names" in klass.__dict__:
            descriptor = klass.__dict__["names"]
            break
    assert isinstance(descriptor, property)

def test_a_a_has_tob():
    assert hasattr(a_A, "tob")
    descriptor = None
    for klass in a_A.__mro__:
        if "tob" in klass.__dict__:
            descriptor = klass.__dict__["tob"]
            break
    assert isinstance(descriptor, property)



def test_a_root_is_not_abstract():
    assert not inspect.isabstract(a_Root)


def test_a_root_constructor_exists():
    assert callable(a_Root.__init__)


def test_a_root_constructor_args():
    sig = inspect.signature(a_Root.__init__)
    params = list(sig.parameters.keys())
    assert "visible" in params, "Missing parameter 'visible'"

def test_a_root_has_visible():
    assert hasattr(a_Root, "visible")
    descriptor = None
    for klass in a_Root.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
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
a_B_strategy = st.builds(
    a_B,
    name=
        safe_text
)
a_A_strategy = st.builds(
    a_A,
    names=
        safe_text,
    tob=
        safe_text
)
a_Root_strategy = st.builds(
    a_Root,
    visible=
        st.booleans()
)

@given(instance=a_B_strategy)
@settings(max_examples=50)
def test_a_b_instantiation(instance):
    assert isinstance(instance, a_B)



@given(instance=a_B_strategy)
def test_a_b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=a_A_strategy)
@settings(max_examples=50)
def test_a_a_instantiation(instance):
    assert isinstance(instance, a_A)



@given(instance=a_A_strategy)
def test_a_a_names_setter(instance):
    original = instance.names
    instance.names = original
    assert instance.names == original



@given(instance=a_A_strategy)
def test_a_a_tob_setter(instance):
    original = instance.tob
    instance.tob = original
    assert instance.tob == original

@given(instance=a_Root_strategy)
@settings(max_examples=50)
def test_a_root_instantiation(instance):
    assert isinstance(instance, a_Root)



@given(instance=a_Root_strategy)
def test_a_root_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original
