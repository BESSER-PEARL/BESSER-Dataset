import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TypeB::BStringElement,
    TypeB::BDoubleElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typeb::bstringelement_is_not_abstract():
    assert not inspect.isabstract(TypeB::BStringElement)


def test_typeb::bstringelement_constructor_exists():
    assert callable(TypeB::BStringElement.__init__)


def test_typeb::bstringelement_constructor_args():
    sig = inspect.signature(TypeB::BStringElement.__init__)
    params = list(sig.parameters.keys())
    assert "stringValue" in params, "Missing parameter 'stringValue'"

def test_typeb::bstringelement_has_stringValue():
    assert hasattr(TypeB::BStringElement, "stringValue")
    descriptor = None
    for klass in TypeB::BStringElement.__mro__:
        if "stringValue" in klass.__dict__:
            descriptor = klass.__dict__["stringValue"]
            break
    assert isinstance(descriptor, property)



def test_typeb::bdoubleelement_is_not_abstract():
    assert not inspect.isabstract(TypeB::BDoubleElement)


def test_typeb::bdoubleelement_constructor_exists():
    assert callable(TypeB::BDoubleElement.__init__)


def test_typeb::bdoubleelement_constructor_args():
    sig = inspect.signature(TypeB::BDoubleElement.__init__)
    params = list(sig.parameters.keys())
    assert "doubleValue" in params, "Missing parameter 'doubleValue'"

def test_typeb::bdoubleelement_has_doubleValue():
    assert hasattr(TypeB::BDoubleElement, "doubleValue")
    descriptor = None
    for klass in TypeB::BDoubleElement.__mro__:
        if "doubleValue" in klass.__dict__:
            descriptor = klass.__dict__["doubleValue"]
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
TypeB::BStringElement_strategy = st.builds(
    TypeB::BStringElement,
    stringValue=
        safe_text
)
TypeB::BDoubleElement_strategy = st.builds(
    TypeB::BDoubleElement,
    doubleValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=TypeB::BStringElement_strategy)
@settings(max_examples=50)
def test_typeb::bstringelement_instantiation(instance):
    assert isinstance(instance, TypeB::BStringElement)

@given(instance=TypeB::BStringElement_strategy)
def test_typeb::bstringelement_stringValue_type(instance):
    assert isinstance(instance.stringValue, str)


@given(instance=TypeB::BStringElement_strategy)
def test_typeb::bstringelement_stringValue_setter(instance):
    original = instance.stringValue
    instance.stringValue = original
    assert instance.stringValue == original

@given(instance=TypeB::BDoubleElement_strategy)
@settings(max_examples=50)
def test_typeb::bdoubleelement_instantiation(instance):
    assert isinstance(instance, TypeB::BDoubleElement)

@given(instance=TypeB::BDoubleElement_strategy)
def test_typeb::bdoubleelement_doubleValue_type(instance):
    assert isinstance(instance.doubleValue, float)


@given(instance=TypeB::BDoubleElement_strategy)
def test_typeb::bdoubleelement_doubleValue_setter(instance):
    original = instance.doubleValue
    instance.doubleValue = original
    assert instance.doubleValue == original
