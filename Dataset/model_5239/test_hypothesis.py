import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    introduction::con,
    introduction::Y,
    introduction::X,
    introduction::A,
    A,
    introduction::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_introduction::con_is_not_abstract():
    assert not inspect.isabstract(introduction::con)


def test_introduction::con_constructor_exists():
    assert callable(introduction::con.__init__)


def test_introduction::con_constructor_args():
    sig = inspect.signature(introduction::con.__init__)
    params = list(sig.parameters.keys())



def test_introduction::y_is_not_abstract():
    assert not inspect.isabstract(introduction::Y)


def test_introduction::y_constructor_exists():
    assert callable(introduction::Y.__init__)


def test_introduction::y_constructor_args():
    sig = inspect.signature(introduction::Y.__init__)
    params = list(sig.parameters.keys())
    assert "test" in params, "Missing parameter 'test'"
    assert "id" in params, "Missing parameter 'id'"

def test_introduction::y_has_test():
    assert hasattr(introduction::Y, "test")
    descriptor = None
    for klass in introduction::Y.__mro__:
        if "test" in klass.__dict__:
            descriptor = klass.__dict__["test"]
            break
    assert isinstance(descriptor, property)

def test_introduction::y_has_id():
    assert hasattr(introduction::Y, "id")
    descriptor = None
    for klass in introduction::Y.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_introduction::x_is_not_abstract():
    assert not inspect.isabstract(introduction::X)


def test_introduction::x_constructor_exists():
    assert callable(introduction::X.__init__)


def test_introduction::x_constructor_args():
    sig = inspect.signature(introduction::X.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_introduction::x_has_id():
    assert hasattr(introduction::X, "id")
    descriptor = None
    for klass in introduction::X.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_introduction::a_is_not_abstract():
    assert not inspect.isabstract(introduction::A)


def test_introduction::a_constructor_exists():
    assert callable(introduction::A.__init__)


def test_introduction::a_constructor_args():
    sig = inspect.signature(introduction::A.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_introduction::a_has_id():
    assert hasattr(introduction::A, "id")
    descriptor = None
    for klass in introduction::A.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_introduction::b_is_not_abstract():
    assert not inspect.isabstract(introduction::B)


def test_introduction::b_constructor_exists():
    assert callable(introduction::B.__init__)


def test_introduction::b_constructor_args():
    sig = inspect.signature(introduction::B.__init__)
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
introduction::con_strategy = st.builds(
    introduction::con,
)
introduction::Y_strategy = st.builds(
    introduction::Y,
    test=
        st.integers(),
    id=
        safe_text
)
introduction::X_strategy = st.builds(
    introduction::X,
    id=
        safe_text
)
introduction::A_strategy = st.builds(
    introduction::A,
    id=
        safe_text
)
A_strategy = st.builds(
    A,
)
introduction::B_strategy = st.builds(
    introduction::B,
)

@given(instance=introduction::con_strategy)
@settings(max_examples=50)
def test_introduction::con_instantiation(instance):
    assert isinstance(instance, introduction::con)

@given(instance=introduction::Y_strategy)
@settings(max_examples=50)
def test_introduction::y_instantiation(instance):
    assert isinstance(instance, introduction::Y)

@given(instance=introduction::Y_strategy)
def test_introduction::y_test_type(instance):
    assert isinstance(instance.test, int)


@given(instance=introduction::Y_strategy)
def test_introduction::y_test_setter(instance):
    original = instance.test
    instance.test = original
    assert instance.test == original

@given(instance=introduction::Y_strategy)
def test_introduction::y_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=introduction::Y_strategy)
def test_introduction::y_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=introduction::X_strategy)
@settings(max_examples=50)
def test_introduction::x_instantiation(instance):
    assert isinstance(instance, introduction::X)

@given(instance=introduction::X_strategy)
def test_introduction::x_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=introduction::X_strategy)
def test_introduction::x_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=introduction::A_strategy)
@settings(max_examples=50)
def test_introduction::a_instantiation(instance):
    assert isinstance(instance, introduction::A)

@given(instance=introduction::A_strategy)
def test_introduction::a_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=introduction::A_strategy)
def test_introduction::a_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=introduction::B_strategy)
@settings(max_examples=50)
def test_introduction::b_instantiation(instance):
    assert isinstance(instance, introduction::B)
