import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simplecont::X,
    simplecont::C,
    simplecont::B,
    simplecont::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplecont::x_is_not_abstract():
    assert not inspect.isabstract(simplecont::X)


def test_simplecont::x_constructor_exists():
    assert callable(simplecont::X.__init__)


def test_simplecont::x_constructor_args():
    sig = inspect.signature(simplecont::X.__init__)
    params = list(sig.parameters.keys())



def test_simplecont::c_is_not_abstract():
    assert not inspect.isabstract(simplecont::C)


def test_simplecont::c_constructor_exists():
    assert callable(simplecont::C.__init__)


def test_simplecont::c_constructor_args():
    sig = inspect.signature(simplecont::C.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_simplecont::c_has_id():
    assert hasattr(simplecont::C, "id")
    descriptor = None
    for klass in simplecont::C.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_simplecont::b_is_not_abstract():
    assert not inspect.isabstract(simplecont::B)


def test_simplecont::b_constructor_exists():
    assert callable(simplecont::B.__init__)


def test_simplecont::b_constructor_args():
    sig = inspect.signature(simplecont::B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplecont::b_has_name():
    assert hasattr(simplecont::B, "name")
    descriptor = None
    for klass in simplecont::B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplecont::a_is_not_abstract():
    assert not inspect.isabstract(simplecont::A)


def test_simplecont::a_constructor_exists():
    assert callable(simplecont::A.__init__)


def test_simplecont::a_constructor_args():
    sig = inspect.signature(simplecont::A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplecont::a_has_name():
    assert hasattr(simplecont::A, "name")
    descriptor = None
    for klass in simplecont::A.__mro__:
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
simplecont::X_strategy = st.builds(
    simplecont::X,
)
simplecont::C_strategy = st.builds(
    simplecont::C,
    id=
        safe_text
)
simplecont::B_strategy = st.builds(
    simplecont::B,
    name=
        safe_text
)
simplecont::A_strategy = st.builds(
    simplecont::A,
    name=
        safe_text
)

@given(instance=simplecont::X_strategy)
@settings(max_examples=50)
def test_simplecont::x_instantiation(instance):
    assert isinstance(instance, simplecont::X)

@given(instance=simplecont::C_strategy)
@settings(max_examples=50)
def test_simplecont::c_instantiation(instance):
    assert isinstance(instance, simplecont::C)

@given(instance=simplecont::C_strategy)
def test_simplecont::c_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=simplecont::C_strategy)
def test_simplecont::c_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=simplecont::B_strategy)
@settings(max_examples=50)
def test_simplecont::b_instantiation(instance):
    assert isinstance(instance, simplecont::B)

@given(instance=simplecont::B_strategy)
def test_simplecont::b_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplecont::B_strategy)
def test_simplecont::b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplecont::A_strategy)
@settings(max_examples=50)
def test_simplecont::a_instantiation(instance):
    assert isinstance(instance, simplecont::A)

@given(instance=simplecont::A_strategy)
def test_simplecont::a_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplecont::A_strategy)
def test_simplecont::a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
