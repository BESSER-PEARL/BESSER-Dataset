import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    introduction_con,
    introduction_Y,
    introduction_X,
    introduction_A,
    A,
    introduction_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_introduction_con_is_not_abstract():
    assert not inspect.isabstract(introduction_con)


def test_introduction_con_constructor_exists():
    assert callable(introduction_con.__init__)


def test_introduction_con_constructor_args():
    sig = inspect.signature(introduction_con.__init__)
    params = list(sig.parameters.keys())



def test_introduction_y_is_not_abstract():
    assert not inspect.isabstract(introduction_Y)


def test_introduction_y_constructor_exists():
    assert callable(introduction_Y.__init__)


def test_introduction_y_constructor_args():
    sig = inspect.signature(introduction_Y.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "test" in params, "Missing parameter 'test'"

def test_introduction_y_has_id():
    assert hasattr(introduction_Y, "id")
    descriptor = None
    for klass in introduction_Y.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_introduction_y_has_test():
    assert hasattr(introduction_Y, "test")
    descriptor = None
    for klass in introduction_Y.__mro__:
        if "test" in klass.__dict__:
            descriptor = klass.__dict__["test"]
            break
    assert isinstance(descriptor, property)



def test_introduction_x_is_not_abstract():
    assert not inspect.isabstract(introduction_X)


def test_introduction_x_constructor_exists():
    assert callable(introduction_X.__init__)


def test_introduction_x_constructor_args():
    sig = inspect.signature(introduction_X.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_introduction_x_has_id():
    assert hasattr(introduction_X, "id")
    descriptor = None
    for klass in introduction_X.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_introduction_a_is_not_abstract():
    assert not inspect.isabstract(introduction_A)


def test_introduction_a_constructor_exists():
    assert callable(introduction_A.__init__)


def test_introduction_a_constructor_args():
    sig = inspect.signature(introduction_A.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_introduction_a_has_id():
    assert hasattr(introduction_A, "id")
    descriptor = None
    for klass in introduction_A.__mro__:
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



def test_introduction_b_is_not_abstract():
    assert not inspect.isabstract(introduction_B)


def test_introduction_b_constructor_exists():
    assert callable(introduction_B.__init__)


def test_introduction_b_constructor_args():
    sig = inspect.signature(introduction_B.__init__)
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
introduction_con_strategy = st.builds(
    introduction_con,
)
introduction_Y_strategy = st.builds(
    introduction_Y,
    id=
        safe_text,
    test=
        st.integers()
)
introduction_X_strategy = st.builds(
    introduction_X,
    id=
        safe_text
)
introduction_A_strategy = st.builds(
    introduction_A,
    id=
        safe_text
)
A_strategy = st.builds(
    A,
)
introduction_B_strategy = st.builds(
    introduction_B,
)

@given(instance=introduction_con_strategy)
@settings(max_examples=50)
def test_introduction_con_instantiation(instance):
    assert isinstance(instance, introduction_con)

@given(instance=introduction_Y_strategy)
@settings(max_examples=50)
def test_introduction_y_instantiation(instance):
    assert isinstance(instance, introduction_Y)



@given(instance=introduction_Y_strategy)
def test_introduction_y_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=introduction_Y_strategy)
def test_introduction_y_test_setter(instance):
    original = instance.test
    instance.test = original
    assert instance.test == original

@given(instance=introduction_X_strategy)
@settings(max_examples=50)
def test_introduction_x_instantiation(instance):
    assert isinstance(instance, introduction_X)



@given(instance=introduction_X_strategy)
def test_introduction_x_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=introduction_A_strategy)
@settings(max_examples=50)
def test_introduction_a_instantiation(instance):
    assert isinstance(instance, introduction_A)



@given(instance=introduction_A_strategy)
def test_introduction_a_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=introduction_B_strategy)
@settings(max_examples=50)
def test_introduction_b_instantiation(instance):
    assert isinstance(instance, introduction_B)
