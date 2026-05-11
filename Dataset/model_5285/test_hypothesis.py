import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Example::A,
    B,
    Example::Bb,
    Example::Ba,
    Example::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_example::a_is_not_abstract():
    assert not inspect.isabstract(Example::A)


def test_example::a_constructor_exists():
    assert callable(Example::A.__init__)


def test_example::a_constructor_args():
    sig = inspect.signature(Example::A.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"

def test_example::a_has_a():
    assert hasattr(Example::A, "a")
    descriptor = None
    for klass in Example::A.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_example::bb_is_not_abstract():
    assert not inspect.isabstract(Example::Bb)


def test_example::bb_constructor_exists():
    assert callable(Example::Bb.__init__)


def test_example::bb_constructor_args():
    sig = inspect.signature(Example::Bb.__init__)
    params = list(sig.parameters.keys())



def test_example::ba_is_not_abstract():
    assert not inspect.isabstract(Example::Ba)


def test_example::ba_constructor_exists():
    assert callable(Example::Ba.__init__)


def test_example::ba_constructor_args():
    sig = inspect.signature(Example::Ba.__init__)
    params = list(sig.parameters.keys())
    assert "ba" in params, "Missing parameter 'ba'"

def test_example::ba_has_ba():
    assert hasattr(Example::Ba, "ba")
    descriptor = None
    for klass in Example::Ba.__mro__:
        if "ba" in klass.__dict__:
            descriptor = klass.__dict__["ba"]
            break
    assert isinstance(descriptor, property)



def test_example::b_is_not_abstract():
    assert not inspect.isabstract(Example::B)


def test_example::b_constructor_exists():
    assert callable(Example::B.__init__)


def test_example::b_constructor_args():
    sig = inspect.signature(Example::B.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_example::b_has_b():
    assert hasattr(Example::B, "b")
    descriptor = None
    for klass in Example::B.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
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
Example::A_strategy = st.builds(
    Example::A,
    a=
        safe_text
)
B_strategy = st.builds(
    B,
)
Example::Bb_strategy = st.builds(
    Example::Bb,
)
Example::Ba_strategy = st.builds(
    Example::Ba,
    ba=
        safe_text
)
Example::B_strategy = st.builds(
    Example::B,
    b=
        safe_text
)

@given(instance=Example::A_strategy)
@settings(max_examples=50)
def test_example::a_instantiation(instance):
    assert isinstance(instance, Example::A)

@given(instance=Example::A_strategy)
def test_example::a_a_type(instance):
    assert isinstance(instance.a, str)


@given(instance=Example::A_strategy)
def test_example::a_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=Example::Bb_strategy)
@settings(max_examples=50)
def test_example::bb_instantiation(instance):
    assert isinstance(instance, Example::Bb)

@given(instance=Example::Ba_strategy)
@settings(max_examples=50)
def test_example::ba_instantiation(instance):
    assert isinstance(instance, Example::Ba)

@given(instance=Example::Ba_strategy)
def test_example::ba_ba_type(instance):
    assert isinstance(instance.ba, str)


@given(instance=Example::Ba_strategy)
def test_example::ba_ba_setter(instance):
    original = instance.ba
    instance.ba = original
    assert instance.ba == original

@given(instance=Example::B_strategy)
@settings(max_examples=50)
def test_example::b_instantiation(instance):
    assert isinstance(instance, Example::B)

@given(instance=Example::B_strategy)
def test_example::b_b_type(instance):
    assert isinstance(instance.b, str)


@given(instance=Example::B_strategy)
def test_example::b_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original
