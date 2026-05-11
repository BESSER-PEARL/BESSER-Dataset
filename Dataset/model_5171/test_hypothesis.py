import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    b::Y,
    b::B,
    b::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b::y_is_not_abstract():
    assert not inspect.isabstract(b::Y)


def test_b::y_constructor_exists():
    assert callable(b::Y.__init__)


def test_b::y_constructor_args():
    sig = inspect.signature(b::Y.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "info" in params, "Missing parameter 'info'"

def test_b::y_has_label():
    assert hasattr(b::Y, "label")
    descriptor = None
    for klass in b::Y.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_b::y_has_info():
    assert hasattr(b::Y, "info")
    descriptor = None
    for klass in b::Y.__mro__:
        if "info" in klass.__dict__:
            descriptor = klass.__dict__["info"]
            break
    assert isinstance(descriptor, property)



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
b::Y_strategy = st.builds(
    b::Y,
    label=
        safe_text,
    info=
        safe_text
)
b::B_strategy = st.builds(
    b::B,
    id=
        safe_text
)
b::Model_strategy = st.builds(
    b::Model,
)

@given(instance=b::Y_strategy)
@settings(max_examples=50)
def test_b::y_instantiation(instance):
    assert isinstance(instance, b::Y)

@given(instance=b::Y_strategy)
def test_b::y_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=b::Y_strategy)
def test_b::y_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=b::Y_strategy)
def test_b::y_info_type(instance):
    assert isinstance(instance.info, str)


@given(instance=b::Y_strategy)
def test_b::y_info_setter(instance):
    original = instance.info
    instance.info = original
    assert instance.info == original

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
