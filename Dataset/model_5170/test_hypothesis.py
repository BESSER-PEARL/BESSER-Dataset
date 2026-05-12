import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    b_B,
    b_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b_b_is_not_abstract():
    assert not inspect.isabstract(b_B)


def test_b_b_constructor_exists():
    assert callable(b_B.__init__)


def test_b_b_constructor_args():
    sig = inspect.signature(b_B.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_b_b_has_id():
    assert hasattr(b_B, "id")
    descriptor = None
    for klass in b_B.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_b_model_is_not_abstract():
    assert not inspect.isabstract(b_Model)


def test_b_model_constructor_exists():
    assert callable(b_Model.__init__)


def test_b_model_constructor_args():
    sig = inspect.signature(b_Model.__init__)
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
b_B_strategy = st.builds(
    b_B,
    id=
        safe_text
)
b_Model_strategy = st.builds(
    b_Model,
)

@given(instance=b_B_strategy)
@settings(max_examples=50)
def test_b_b_instantiation(instance):
    assert isinstance(instance, b_B)



@given(instance=b_B_strategy)
def test_b_b_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=b_Model_strategy)
@settings(max_examples=50)
def test_b_model_instantiation(instance):
    assert isinstance(instance, b_Model)
