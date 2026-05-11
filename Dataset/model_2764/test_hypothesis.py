import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simplek::B,
    simplek::A,
    simplek::Content,
    simplek::Base,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplek::b_is_not_abstract():
    assert not inspect.isabstract(simplek::B)


def test_simplek::b_constructor_exists():
    assert callable(simplek::B.__init__)


def test_simplek::b_constructor_args():
    sig = inspect.signature(simplek::B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplek::b_has_name():
    assert hasattr(simplek::B, "name")
    descriptor = None
    for klass in simplek::B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplek::a_is_not_abstract():
    assert not inspect.isabstract(simplek::A)


def test_simplek::a_constructor_exists():
    assert callable(simplek::A.__init__)


def test_simplek::a_constructor_args():
    sig = inspect.signature(simplek::A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplek::a_has_name():
    assert hasattr(simplek::A, "name")
    descriptor = None
    for klass in simplek::A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplek::content_is_not_abstract():
    assert not inspect.isabstract(simplek::Content)


def test_simplek::content_constructor_exists():
    assert callable(simplek::Content.__init__)


def test_simplek::content_constructor_args():
    sig = inspect.signature(simplek::Content.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplek::content_has_name():
    assert hasattr(simplek::Content, "name")
    descriptor = None
    for klass in simplek::Content.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplek::base_is_not_abstract():
    assert not inspect.isabstract(simplek::Base)


def test_simplek::base_constructor_exists():
    assert callable(simplek::Base.__init__)


def test_simplek::base_constructor_args():
    sig = inspect.signature(simplek::Base.__init__)
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
simplek::B_strategy = st.builds(
    simplek::B,
    name=
        safe_text
)
simplek::A_strategy = st.builds(
    simplek::A,
    name=
        safe_text
)
simplek::Content_strategy = st.builds(
    simplek::Content,
    name=
        safe_text
)
simplek::Base_strategy = st.builds(
    simplek::Base,
)

@given(instance=simplek::B_strategy)
@settings(max_examples=50)
def test_simplek::b_instantiation(instance):
    assert isinstance(instance, simplek::B)

@given(instance=simplek::B_strategy)
def test_simplek::b_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplek::B_strategy)
def test_simplek::b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplek::A_strategy)
@settings(max_examples=50)
def test_simplek::a_instantiation(instance):
    assert isinstance(instance, simplek::A)

@given(instance=simplek::A_strategy)
def test_simplek::a_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplek::A_strategy)
def test_simplek::a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplek::Content_strategy)
@settings(max_examples=50)
def test_simplek::content_instantiation(instance):
    assert isinstance(instance, simplek::Content)

@given(instance=simplek::Content_strategy)
def test_simplek::content_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplek::Content_strategy)
def test_simplek::content_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplek::Base_strategy)
@settings(max_examples=50)
def test_simplek::base_instantiation(instance):
    assert isinstance(instance, simplek::Base)
