import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    foo::J,
    J,
    foo::B,
    B,
    foo::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_foo::j_is_not_abstract():
    assert not inspect.isabstract(foo::J)


def test_foo::j_constructor_exists():
    assert callable(foo::J.__init__)


def test_foo::j_constructor_args():
    sig = inspect.signature(foo::J.__init__)
    params = list(sig.parameters.keys())



def test_j_is_not_abstract():
    assert not inspect.isabstract(J)


def test_j_constructor_exists():
    assert callable(J.__init__)


def test_j_constructor_args():
    sig = inspect.signature(J.__init__)
    params = list(sig.parameters.keys())



def test_foo::b_is_not_abstract():
    assert not inspect.isabstract(foo::B)


def test_foo::b_constructor_exists():
    assert callable(foo::B.__init__)


def test_foo::b_constructor_args():
    sig = inspect.signature(foo::B.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_foo::a_is_not_abstract():
    assert not inspect.isabstract(foo::A)


def test_foo::a_constructor_exists():
    assert callable(foo::A.__init__)


def test_foo::a_constructor_args():
    sig = inspect.signature(foo::A.__init__)
    params = list(sig.parameters.keys())
    assert "fooA" in params, "Missing parameter 'fooA'"

def test_foo::a_has_fooA():
    assert hasattr(foo::A, "fooA")
    descriptor = None
    for klass in foo::A.__mro__:
        if "fooA" in klass.__dict__:
            descriptor = klass.__dict__["fooA"]
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
foo::J_strategy = st.builds(
    foo::J,
)
J_strategy = st.builds(
    J,
)
foo::B_strategy = st.builds(
    foo::B,
)
B_strategy = st.builds(
    B,
)
foo::A_strategy = st.builds(
    foo::A,
    fooA=
        safe_text
)

@given(instance=foo::J_strategy)
@settings(max_examples=50)
def test_foo::j_instantiation(instance):
    assert isinstance(instance, foo::J)

@given(instance=J_strategy)
@settings(max_examples=50)
def test_j_instantiation(instance):
    assert isinstance(instance, J)

@given(instance=foo::B_strategy)
@settings(max_examples=50)
def test_foo::b_instantiation(instance):
    assert isinstance(instance, foo::B)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=foo::A_strategy)
@settings(max_examples=50)
def test_foo::a_instantiation(instance):
    assert isinstance(instance, foo::A)

@given(instance=foo::A_strategy)
def test_foo::a_fooA_type(instance):
    assert isinstance(instance.fooA, str)


@given(instance=foo::A_strategy)
def test_foo::a_fooA_setter(instance):
    original = instance.fooA
    instance.fooA = original
    assert instance.fooA == original
