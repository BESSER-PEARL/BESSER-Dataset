import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    C,
    b::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_c_constructor_exists():
    assert callable(C.__init__)


def test_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())



def test_b::b_is_not_abstract():
    assert not inspect.isabstract(b::B)


def test_b::b_constructor_exists():
    assert callable(b::B.__init__)


def test_b::b_constructor_args():
    sig = inspect.signature(b::B.__init__)
    params = list(sig.parameters.keys())
    assert "custom_datatype" in params, "Missing parameter 'custom_datatype'"
    assert "to_enum" in params, "Missing parameter 'to_enum'"

def test_b::b_has_custom_datatype():
    assert hasattr(b::B, "custom_datatype")
    descriptor = None
    for klass in b::B.__mro__:
        if "custom_datatype" in klass.__dict__:
            descriptor = klass.__dict__["custom_datatype"]
            break
    assert isinstance(descriptor, property)

def test_b::b_has_to_enum():
    assert hasattr(b::B, "to_enum")
    descriptor = None
    for klass in b::B.__mro__:
        if "to_enum" in klass.__dict__:
            descriptor = klass.__dict__["to_enum"]
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
C_strategy = st.builds(
    C,
)
b::B_strategy = st.builds(
    b::B,
    custom_datatype=
        safe_text,
    to_enum=
        safe_text
)

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)

@given(instance=b::B_strategy)
@settings(max_examples=50)
def test_b::b_instantiation(instance):
    assert isinstance(instance, b::B)

@given(instance=b::B_strategy)
def test_b::b_custom_datatype_type(instance):
    assert isinstance(instance.custom_datatype, str)


@given(instance=b::B_strategy)
def test_b::b_custom_datatype_setter(instance):
    original = instance.custom_datatype
    instance.custom_datatype = original
    assert instance.custom_datatype == original

@given(instance=b::B_strategy)
def test_b::b_to_enum_type(instance):
    assert isinstance(instance.to_enum, str)


@given(instance=b::B_strategy)
def test_b::b_to_enum_setter(instance):
    original = instance.to_enum
    instance.to_enum = original
    assert instance.to_enum == original
