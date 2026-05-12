import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SuperStuff2,
    SuperStuff,
    a_B,
    a_Root,
    a_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_superstuff2_is_not_abstract():
    assert not inspect.isabstract(SuperStuff2)


def test_superstuff2_constructor_exists():
    assert callable(SuperStuff2.__init__)


def test_superstuff2_constructor_args():
    sig = inspect.signature(SuperStuff2.__init__)
    params = list(sig.parameters.keys())



def test_superstuff_is_not_abstract():
    assert not inspect.isabstract(SuperStuff)


def test_superstuff_constructor_exists():
    assert callable(SuperStuff.__init__)


def test_superstuff_constructor_args():
    sig = inspect.signature(SuperStuff.__init__)
    params = list(sig.parameters.keys())



def test_a_b_is_not_abstract():
    assert not inspect.isabstract(a_B)


def test_a_b_constructor_exists():
    assert callable(a_B.__init__)


def test_a_b_constructor_args():
    sig = inspect.signature(a_B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "nameID" in params, "Missing parameter 'nameID'"

def test_a_b_has_name():
    assert hasattr(a_B, "name")
    descriptor = None
    for klass in a_B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_a_b_has_nameID():
    assert hasattr(a_B, "nameID")
    descriptor = None
    for klass in a_B.__mro__:
        if "nameID" in klass.__dict__:
            descriptor = klass.__dict__["nameID"]
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



def test_a_a_is_not_abstract():
    assert not inspect.isabstract(a_A)


def test_a_a_constructor_exists():
    assert callable(a_A.__init__)


def test_a_a_constructor_args():
    sig = inspect.signature(a_A.__init__)
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
SuperStuff2_strategy = st.builds(
    SuperStuff2,
)
SuperStuff_strategy = st.builds(
    SuperStuff,
)
a_B_strategy = st.builds(
    a_B,
    name=
        safe_text,
    nameID=
        safe_text
)
a_Root_strategy = st.builds(
    a_Root,
    visible=
        st.booleans()
)
a_A_strategy = st.builds(
    a_A,
)

@given(instance=SuperStuff2_strategy)
@settings(max_examples=50)
def test_superstuff2_instantiation(instance):
    assert isinstance(instance, SuperStuff2)

@given(instance=SuperStuff_strategy)
@settings(max_examples=50)
def test_superstuff_instantiation(instance):
    assert isinstance(instance, SuperStuff)

@given(instance=a_B_strategy)
@settings(max_examples=50)
def test_a_b_instantiation(instance):
    assert isinstance(instance, a_B)



@given(instance=a_B_strategy)
def test_a_b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=a_B_strategy)
def test_a_b_nameID_setter(instance):
    original = instance.nameID
    instance.nameID = original
    assert instance.nameID == original

@given(instance=a_Root_strategy)
@settings(max_examples=50)
def test_a_root_instantiation(instance):
    assert isinstance(instance, a_Root)



@given(instance=a_Root_strategy)
def test_a_root_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=a_A_strategy)
@settings(max_examples=50)
def test_a_a_instantiation(instance):
    assert isinstance(instance, a_A)
