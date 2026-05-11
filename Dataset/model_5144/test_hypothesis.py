import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    a::B,
    a::A,
    a::Root,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a::b_is_not_abstract():
    assert not inspect.isabstract(a::B)


def test_a::b_constructor_exists():
    assert callable(a::B.__init__)


def test_a::b_constructor_args():
    sig = inspect.signature(a::B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_a::b_has_name():
    assert hasattr(a::B, "name")
    descriptor = None
    for klass in a::B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_a::a_is_not_abstract():
    assert not inspect.isabstract(a::A)


def test_a::a_constructor_exists():
    assert callable(a::A.__init__)


def test_a::a_constructor_args():
    sig = inspect.signature(a::A.__init__)
    params = list(sig.parameters.keys())
    assert "names" in params, "Missing parameter 'names'"
    assert "tob" in params, "Missing parameter 'tob'"

def test_a::a_has_names():
    assert hasattr(a::A, "names")
    descriptor = None
    for klass in a::A.__mro__:
        if "names" in klass.__dict__:
            descriptor = klass.__dict__["names"]
            break
    assert isinstance(descriptor, property)

def test_a::a_has_tob():
    assert hasattr(a::A, "tob")
    descriptor = None
    for klass in a::A.__mro__:
        if "tob" in klass.__dict__:
            descriptor = klass.__dict__["tob"]
            break
    assert isinstance(descriptor, property)



def test_a::root_is_not_abstract():
    assert not inspect.isabstract(a::Root)


def test_a::root_constructor_exists():
    assert callable(a::Root.__init__)


def test_a::root_constructor_args():
    sig = inspect.signature(a::Root.__init__)
    params = list(sig.parameters.keys())
    assert "visible" in params, "Missing parameter 'visible'"

def test_a::root_has_visible():
    assert hasattr(a::Root, "visible")
    descriptor = None
    for klass in a::Root.__mro__:
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
a::B_strategy = st.builds(
    a::B,
    name=
        safe_text
)
a::A_strategy = st.builds(
    a::A,
    names=
        safe_text,
    tob=
        safe_text
)
a::Root_strategy = st.builds(
    a::Root,
    visible=
        st.booleans()
)

@given(instance=a::B_strategy)
@settings(max_examples=50)
def test_a::b_instantiation(instance):
    assert isinstance(instance, a::B)

@given(instance=a::B_strategy)
def test_a::b_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=a::B_strategy)
def test_a::b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=a::A_strategy)
@settings(max_examples=50)
def test_a::a_instantiation(instance):
    assert isinstance(instance, a::A)

@given(instance=a::A_strategy)
def test_a::a_names_type(instance):
    assert isinstance(instance.names, str)


@given(instance=a::A_strategy)
def test_a::a_names_setter(instance):
    original = instance.names
    instance.names = original
    assert instance.names == original

@given(instance=a::A_strategy)
def test_a::a_tob_type(instance):
    assert isinstance(instance.tob, str)


@given(instance=a::A_strategy)
def test_a::a_tob_setter(instance):
    original = instance.tob
    instance.tob = original
    assert instance.tob == original

@given(instance=a::Root_strategy)
@settings(max_examples=50)
def test_a::root_instantiation(instance):
    assert isinstance(instance, a::Root)

@given(instance=a::Root_strategy)
def test_a::root_visible_type(instance):
    assert isinstance(instance.visible, bool)


@given(instance=a::Root_strategy)
def test_a::root_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original
