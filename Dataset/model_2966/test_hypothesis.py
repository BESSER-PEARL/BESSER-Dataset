import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Attribute::NodeVar,
    Attribute::NodeInOut,
    Attribute::NodeOut,
    Attribute::NodeIn,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_attribute::nodevar_is_not_abstract():
    assert not inspect.isabstract(Attribute::NodeVar)


def test_attribute::nodevar_constructor_exists():
    assert callable(Attribute::NodeVar.__init__)


def test_attribute::nodevar_constructor_args():
    sig = inspect.signature(Attribute::NodeVar.__init__)
    params = list(sig.parameters.keys())
    assert "Number" in params, "Missing parameter 'Number'"

def test_attribute::nodevar_has_Number():
    assert hasattr(Attribute::NodeVar, "Number")
    descriptor = None
    for klass in Attribute::NodeVar.__mro__:
        if "Number" in klass.__dict__:
            descriptor = klass.__dict__["Number"]
            break
    assert isinstance(descriptor, property)



def test_attribute::nodeinout_is_not_abstract():
    assert not inspect.isabstract(Attribute::NodeInOut)


def test_attribute::nodeinout_constructor_exists():
    assert callable(Attribute::NodeInOut.__init__)


def test_attribute::nodeinout_constructor_args():
    sig = inspect.signature(Attribute::NodeInOut.__init__)
    params = list(sig.parameters.keys())
    assert "Number" in params, "Missing parameter 'Number'"

def test_attribute::nodeinout_has_Number():
    assert hasattr(Attribute::NodeInOut, "Number")
    descriptor = None
    for klass in Attribute::NodeInOut.__mro__:
        if "Number" in klass.__dict__:
            descriptor = klass.__dict__["Number"]
            break
    assert isinstance(descriptor, property)



def test_attribute::nodeout_is_not_abstract():
    assert not inspect.isabstract(Attribute::NodeOut)


def test_attribute::nodeout_constructor_exists():
    assert callable(Attribute::NodeOut.__init__)


def test_attribute::nodeout_constructor_args():
    sig = inspect.signature(Attribute::NodeOut.__init__)
    params = list(sig.parameters.keys())
    assert "Number" in params, "Missing parameter 'Number'"

def test_attribute::nodeout_has_Number():
    assert hasattr(Attribute::NodeOut, "Number")
    descriptor = None
    for klass in Attribute::NodeOut.__mro__:
        if "Number" in klass.__dict__:
            descriptor = klass.__dict__["Number"]
            break
    assert isinstance(descriptor, property)



def test_attribute::nodein_is_not_abstract():
    assert not inspect.isabstract(Attribute::NodeIn)


def test_attribute::nodein_constructor_exists():
    assert callable(Attribute::NodeIn.__init__)


def test_attribute::nodein_constructor_args():
    sig = inspect.signature(Attribute::NodeIn.__init__)
    params = list(sig.parameters.keys())
    assert "Number" in params, "Missing parameter 'Number'"

def test_attribute::nodein_has_Number():
    assert hasattr(Attribute::NodeIn, "Number")
    descriptor = None
    for klass in Attribute::NodeIn.__mro__:
        if "Number" in klass.__dict__:
            descriptor = klass.__dict__["Number"]
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
Attribute::NodeVar_strategy = st.builds(
    Attribute::NodeVar,
    Number=
        st.integers()
)
Attribute::NodeInOut_strategy = st.builds(
    Attribute::NodeInOut,
    Number=
        st.integers()
)
Attribute::NodeOut_strategy = st.builds(
    Attribute::NodeOut,
    Number=
        st.integers()
)
Attribute::NodeIn_strategy = st.builds(
    Attribute::NodeIn,
    Number=
        st.integers()
)

@given(instance=Attribute::NodeVar_strategy)
@settings(max_examples=50)
def test_attribute::nodevar_instantiation(instance):
    assert isinstance(instance, Attribute::NodeVar)

@given(instance=Attribute::NodeVar_strategy)
def test_attribute::nodevar_Number_type(instance):
    assert isinstance(instance.Number, int)


@given(instance=Attribute::NodeVar_strategy)
def test_attribute::nodevar_Number_setter(instance):
    original = instance.Number
    instance.Number = original
    assert instance.Number == original

@given(instance=Attribute::NodeInOut_strategy)
@settings(max_examples=50)
def test_attribute::nodeinout_instantiation(instance):
    assert isinstance(instance, Attribute::NodeInOut)

@given(instance=Attribute::NodeInOut_strategy)
def test_attribute::nodeinout_Number_type(instance):
    assert isinstance(instance.Number, int)


@given(instance=Attribute::NodeInOut_strategy)
def test_attribute::nodeinout_Number_setter(instance):
    original = instance.Number
    instance.Number = original
    assert instance.Number == original

@given(instance=Attribute::NodeOut_strategy)
@settings(max_examples=50)
def test_attribute::nodeout_instantiation(instance):
    assert isinstance(instance, Attribute::NodeOut)

@given(instance=Attribute::NodeOut_strategy)
def test_attribute::nodeout_Number_type(instance):
    assert isinstance(instance.Number, int)


@given(instance=Attribute::NodeOut_strategy)
def test_attribute::nodeout_Number_setter(instance):
    original = instance.Number
    instance.Number = original
    assert instance.Number == original

@given(instance=Attribute::NodeIn_strategy)
@settings(max_examples=50)
def test_attribute::nodein_instantiation(instance):
    assert isinstance(instance, Attribute::NodeIn)

@given(instance=Attribute::NodeIn_strategy)
def test_attribute::nodein_Number_type(instance):
    assert isinstance(instance.Number, int)


@given(instance=Attribute::NodeIn_strategy)
def test_attribute::nodein_Number_setter(instance):
    original = instance.Number
    instance.Number = original
    assert instance.Number == original
