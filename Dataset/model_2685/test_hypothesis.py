import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simplecont_X,
    simplecont_C,
    simplecont_B,
    simplecont_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplecont_x_is_not_abstract():
    assert not inspect.isabstract(simplecont_X)


def test_simplecont_x_constructor_exists():
    assert callable(simplecont_X.__init__)


def test_simplecont_x_constructor_args():
    sig = inspect.signature(simplecont_X.__init__)
    params = list(sig.parameters.keys())



def test_simplecont_c_is_not_abstract():
    assert not inspect.isabstract(simplecont_C)


def test_simplecont_c_constructor_exists():
    assert callable(simplecont_C.__init__)


def test_simplecont_c_constructor_args():
    sig = inspect.signature(simplecont_C.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_simplecont_c_has_id():
    assert hasattr(simplecont_C, "id")
    descriptor = None
    for klass in simplecont_C.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_simplecont_b_is_not_abstract():
    assert not inspect.isabstract(simplecont_B)


def test_simplecont_b_constructor_exists():
    assert callable(simplecont_B.__init__)


def test_simplecont_b_constructor_args():
    sig = inspect.signature(simplecont_B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplecont_b_has_name():
    assert hasattr(simplecont_B, "name")
    descriptor = None
    for klass in simplecont_B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplecont_a_is_not_abstract():
    assert not inspect.isabstract(simplecont_A)


def test_simplecont_a_constructor_exists():
    assert callable(simplecont_A.__init__)


def test_simplecont_a_constructor_args():
    sig = inspect.signature(simplecont_A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplecont_a_has_name():
    assert hasattr(simplecont_A, "name")
    descriptor = None
    for klass in simplecont_A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
simplecont_X_strategy = st.builds(
    simplecont_X,
)
simplecont_C_strategy = st.builds(
    simplecont_C,
    id=
        safe_text
)
simplecont_B_strategy = st.builds(
    simplecont_B,
    name=
        safe_text
)
simplecont_A_strategy = st.builds(
    simplecont_A,
    name=
        safe_text
)

@given(instance=simplecont_X_strategy)
@settings(max_examples=50)
def test_simplecont_x_instantiation(instance):
    assert isinstance(instance, simplecont_X)

@given(instance=simplecont_C_strategy)
@settings(max_examples=50)
def test_simplecont_c_instantiation(instance):
    assert isinstance(instance, simplecont_C)



@given(instance=simplecont_C_strategy)
def test_simplecont_c_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=simplecont_B_strategy)
@settings(max_examples=50)
def test_simplecont_b_instantiation(instance):
    assert isinstance(instance, simplecont_B)



@given(instance=simplecont_B_strategy)
def test_simplecont_b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplecont_A_strategy)
@settings(max_examples=50)
def test_simplecont_a_instantiation(instance):
    assert isinstance(instance, simplecont_A)



@given(instance=simplecont_A_strategy)
def test_simplecont_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
