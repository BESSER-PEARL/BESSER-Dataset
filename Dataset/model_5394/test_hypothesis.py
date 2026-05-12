import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    C,
    b_B,
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



def test_b_b_is_not_abstract():
    assert not inspect.isabstract(b_B)


def test_b_b_constructor_exists():
    assert callable(b_B.__init__)


def test_b_b_constructor_args():
    sig = inspect.signature(b_B.__init__)
    params = list(sig.parameters.keys())
    assert "to_enum" in params, "Missing parameter 'to_enum'"
    assert "custom_datatype" in params, "Missing parameter 'custom_datatype'"

def test_b_b_has_to_enum():
    assert hasattr(b_B, "to_enum")
    descriptor = None
    for klass in b_B.__mro__:
        if "to_enum" in klass.__dict__:
            descriptor = klass.__dict__["to_enum"]
            break
    assert isinstance(descriptor, property)

def test_b_b_has_custom_datatype():
    assert hasattr(b_B, "custom_datatype")
    descriptor = None
    for klass in b_B.__mro__:
        if "custom_datatype" in klass.__dict__:
            descriptor = klass.__dict__["custom_datatype"]
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
b_B_strategy = st.builds(
    b_B,
    to_enum=
        safe_text,
    custom_datatype=
        safe_text
)

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)

@given(instance=b_B_strategy)
@settings(max_examples=50)
def test_b_b_instantiation(instance):
    assert isinstance(instance, b_B)



@given(instance=b_B_strategy)
def test_b_b_to_enum_setter(instance):
    original = instance.to_enum
    instance.to_enum = original
    assert instance.to_enum == original



@given(instance=b_B_strategy)
def test_b_b_custom_datatype_setter(instance):
    original = instance.custom_datatype
    instance.custom_datatype = original
    assert instance.custom_datatype == original
