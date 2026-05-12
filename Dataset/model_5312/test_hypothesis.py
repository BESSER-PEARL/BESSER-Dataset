import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TypeB_BStringElement,
    TypeB_BDoubleElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typeb_bstringelement_is_not_abstract():
    assert not inspect.isabstract(TypeB_BStringElement)


def test_typeb_bstringelement_constructor_exists():
    assert callable(TypeB_BStringElement.__init__)


def test_typeb_bstringelement_constructor_args():
    sig = inspect.signature(TypeB_BStringElement.__init__)
    params = list(sig.parameters.keys())
    assert "stringValue" in params, "Missing parameter 'stringValue'"

def test_typeb_bstringelement_has_stringValue():
    assert hasattr(TypeB_BStringElement, "stringValue")
    descriptor = None
    for klass in TypeB_BStringElement.__mro__:
        if "stringValue" in klass.__dict__:
            descriptor = klass.__dict__["stringValue"]
            break
    assert isinstance(descriptor, property)



def test_typeb_bdoubleelement_is_not_abstract():
    assert not inspect.isabstract(TypeB_BDoubleElement)


def test_typeb_bdoubleelement_constructor_exists():
    assert callable(TypeB_BDoubleElement.__init__)


def test_typeb_bdoubleelement_constructor_args():
    sig = inspect.signature(TypeB_BDoubleElement.__init__)
    params = list(sig.parameters.keys())
    assert "doubleValue" in params, "Missing parameter 'doubleValue'"

def test_typeb_bdoubleelement_has_doubleValue():
    assert hasattr(TypeB_BDoubleElement, "doubleValue")
    descriptor = None
    for klass in TypeB_BDoubleElement.__mro__:
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
TypeB_BStringElement_strategy = st.builds(
    TypeB_BStringElement,
    stringValue=
        safe_text
)
TypeB_BDoubleElement_strategy = st.builds(
    TypeB_BDoubleElement,
    doubleValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=TypeB_BStringElement_strategy)
@settings(max_examples=50)
def test_typeb_bstringelement_instantiation(instance):
    assert isinstance(instance, TypeB_BStringElement)



@given(instance=TypeB_BStringElement_strategy)
def test_typeb_bstringelement_stringValue_setter(instance):
    original = instance.stringValue
    instance.stringValue = original
    assert instance.stringValue == original

@given(instance=TypeB_BDoubleElement_strategy)
@settings(max_examples=50)
def test_typeb_bdoubleelement_instantiation(instance):
    assert isinstance(instance, TypeB_BDoubleElement)



@given(instance=TypeB_BDoubleElement_strategy)
def test_typeb_bdoubleelement_doubleValue_setter(instance):
    original = instance.doubleValue
    instance.doubleValue = original
    assert instance.doubleValue == original
