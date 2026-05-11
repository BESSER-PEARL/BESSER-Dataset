import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    A::A,
    A::A2,
    A::A1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a::a_is_not_abstract():
    assert not inspect.isabstract(A::A)


def test_a::a_constructor_exists():
    assert callable(A::A.__init__)


def test_a::a_constructor_args():
    sig = inspect.signature(A::A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_a::a_has_name():
    assert hasattr(A::A, "name")
    descriptor = None
    for klass in A::A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_a::a2_is_not_abstract():
    assert not inspect.isabstract(A::A2)


def test_a::a2_constructor_exists():
    assert callable(A::A2.__init__)


def test_a::a2_constructor_args():
    sig = inspect.signature(A::A2.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_a::a2_has_description():
    assert hasattr(A::A2, "description")
    descriptor = None
    for klass in A::A2.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_a::a1_is_not_abstract():
    assert not inspect.isabstract(A::A1)


def test_a::a1_constructor_exists():
    assert callable(A::A1.__init__)


def test_a::a1_constructor_args():
    sig = inspect.signature(A::A1.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_a::a1_has_description():
    assert hasattr(A::A1, "description")
    descriptor = None
    for klass in A::A1.__mro__:
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
A::A_strategy = st.builds(
    A::A,
    name=
        safe_text
)
A::A2_strategy = st.builds(
    A::A2,
    description=
        safe_text
)
A::A1_strategy = st.builds(
    A::A1,
    description=
        safe_text
)

@given(instance=A::A_strategy)
@settings(max_examples=50)
def test_a::a_instantiation(instance):
    assert isinstance(instance, A::A)

@given(instance=A::A_strategy)
def test_a::a_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=A::A_strategy)
def test_a::a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=A::A2_strategy)
@settings(max_examples=50)
def test_a::a2_instantiation(instance):
    assert isinstance(instance, A::A2)

@given(instance=A::A2_strategy)
def test_a::a2_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=A::A2_strategy)
def test_a::a2_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=A::A1_strategy)
@settings(max_examples=50)
def test_a::a1_instantiation(instance):
    assert isinstance(instance, A::A1)

@given(instance=A::A1_strategy)
def test_a::a1_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=A::A1_strategy)
def test_a::a1_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
