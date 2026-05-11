import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    b::B,
    b::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b::b_is_not_abstract():
    assert not inspect.isabstract(b::B)


def test_b::b_constructor_exists():
    assert callable(b::B.__init__)


def test_b::b_constructor_args():
    sig = inspect.signature(b::B.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_b::b_has_id():
    assert hasattr(b::B, "id")
    descriptor = None
    for klass in b::B.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_b::model_is_not_abstract():
    assert not inspect.isabstract(b::Model)


def test_b::model_constructor_exists():
    assert callable(b::Model.__init__)


def test_b::model_constructor_args():
    sig = inspect.signature(b::Model.__init__)
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
b::B_strategy = st.builds(
    b::B,
    id=
        safe_text
)
b::Model_strategy = st.builds(
    b::Model,
)

@given(instance=b::B_strategy)
@settings(max_examples=50)
def test_b::b_instantiation(instance):
    assert isinstance(instance, b::B)

@given(instance=b::B_strategy)
def test_b::b_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=b::B_strategy)
def test_b::b_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=b::Model_strategy)
@settings(max_examples=50)
def test_b::model_instantiation(instance):
    assert isinstance(instance, b::Model)
