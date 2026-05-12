import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    A_A,
    A_A2,
    A_A1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_a_is_not_abstract():
    assert not inspect.isabstract(A_A)


def test_a_a_constructor_exists():
    assert callable(A_A.__init__)


def test_a_a_constructor_args():
    sig = inspect.signature(A_A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_a_a_has_name():
    assert hasattr(A_A, "name")
    descriptor = None
    for klass in A_A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_a_a2_is_not_abstract():
    assert not inspect.isabstract(A_A2)


def test_a_a2_constructor_exists():
    assert callable(A_A2.__init__)


def test_a_a2_constructor_args():
    sig = inspect.signature(A_A2.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_a_a2_has_description():
    assert hasattr(A_A2, "description")
    descriptor = None
    for klass in A_A2.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_a_a1_is_not_abstract():
    assert not inspect.isabstract(A_A1)


def test_a_a1_constructor_exists():
    assert callable(A_A1.__init__)


def test_a_a1_constructor_args():
    sig = inspect.signature(A_A1.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_a_a1_has_description():
    assert hasattr(A_A1, "description")
    descriptor = None
    for klass in A_A1.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
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
A_A_strategy = st.builds(
    A_A,
    name=
        safe_text
)
A_A2_strategy = st.builds(
    A_A2,
    description=
        safe_text
)
A_A1_strategy = st.builds(
    A_A1,
    description=
        safe_text
)

@given(instance=A_A_strategy)
@settings(max_examples=50)
def test_a_a_instantiation(instance):
    assert isinstance(instance, A_A)



@given(instance=A_A_strategy)
def test_a_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=A_A2_strategy)
@settings(max_examples=50)
def test_a_a2_instantiation(instance):
    assert isinstance(instance, A_A2)



@given(instance=A_A2_strategy)
def test_a_a2_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=A_A1_strategy)
@settings(max_examples=50)
def test_a_a1_instantiation(instance):
    assert isinstance(instance, A_A1)



@given(instance=A_A1_strategy)
def test_a_a1_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
