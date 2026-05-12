import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simplek_B,
    simplek_A,
    simplek_Content,
    simplek_Base,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplek_b_is_not_abstract():
    assert not inspect.isabstract(simplek_B)


def test_simplek_b_constructor_exists():
    assert callable(simplek_B.__init__)


def test_simplek_b_constructor_args():
    sig = inspect.signature(simplek_B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplek_b_has_name():
    assert hasattr(simplek_B, "name")
    descriptor = None
    for klass in simplek_B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplek_a_is_not_abstract():
    assert not inspect.isabstract(simplek_A)


def test_simplek_a_constructor_exists():
    assert callable(simplek_A.__init__)


def test_simplek_a_constructor_args():
    sig = inspect.signature(simplek_A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplek_a_has_name():
    assert hasattr(simplek_A, "name")
    descriptor = None
    for klass in simplek_A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplek_content_is_not_abstract():
    assert not inspect.isabstract(simplek_Content)


def test_simplek_content_constructor_exists():
    assert callable(simplek_Content.__init__)


def test_simplek_content_constructor_args():
    sig = inspect.signature(simplek_Content.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplek_content_has_name():
    assert hasattr(simplek_Content, "name")
    descriptor = None
    for klass in simplek_Content.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplek_base_is_not_abstract():
    assert not inspect.isabstract(simplek_Base)


def test_simplek_base_constructor_exists():
    assert callable(simplek_Base.__init__)


def test_simplek_base_constructor_args():
    sig = inspect.signature(simplek_Base.__init__)
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
simplek_B_strategy = st.builds(
    simplek_B,
    name=
        safe_text
)
simplek_A_strategy = st.builds(
    simplek_A,
    name=
        safe_text
)
simplek_Content_strategy = st.builds(
    simplek_Content,
    name=
        safe_text
)
simplek_Base_strategy = st.builds(
    simplek_Base,
)

@given(instance=simplek_B_strategy)
@settings(max_examples=50)
def test_simplek_b_instantiation(instance):
    assert isinstance(instance, simplek_B)



@given(instance=simplek_B_strategy)
def test_simplek_b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplek_A_strategy)
@settings(max_examples=50)
def test_simplek_a_instantiation(instance):
    assert isinstance(instance, simplek_A)



@given(instance=simplek_A_strategy)
def test_simplek_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplek_Content_strategy)
@settings(max_examples=50)
def test_simplek_content_instantiation(instance):
    assert isinstance(instance, simplek_Content)



@given(instance=simplek_Content_strategy)
def test_simplek_content_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplek_Base_strategy)
@settings(max_examples=50)
def test_simplek_base_instantiation(instance):
    assert isinstance(instance, simplek_Base)
