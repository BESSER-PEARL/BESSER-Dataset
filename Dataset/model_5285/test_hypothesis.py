import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Example_B,
    Example_A,
    B,
    Example_Bb,
    Example_Ba,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_example_b_is_not_abstract():
    assert not inspect.isabstract(Example_B)


def test_example_b_constructor_exists():
    assert callable(Example_B.__init__)


def test_example_b_constructor_args():
    sig = inspect.signature(Example_B.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_example_b_has_b():
    assert hasattr(Example_B, "b")
    descriptor = None
    for klass in Example_B.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_example_a_is_not_abstract():
    assert not inspect.isabstract(Example_A)


def test_example_a_constructor_exists():
    assert callable(Example_A.__init__)


def test_example_a_constructor_args():
    sig = inspect.signature(Example_A.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"

def test_example_a_has_a():
    assert hasattr(Example_A, "a")
    descriptor = None
    for klass in Example_A.__mro__:
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



def test_example_bb_is_not_abstract():
    assert not inspect.isabstract(Example_Bb)


def test_example_bb_constructor_exists():
    assert callable(Example_Bb.__init__)


def test_example_bb_constructor_args():
    sig = inspect.signature(Example_Bb.__init__)
    params = list(sig.parameters.keys())



def test_example_ba_is_not_abstract():
    assert not inspect.isabstract(Example_Ba)


def test_example_ba_constructor_exists():
    assert callable(Example_Ba.__init__)


def test_example_ba_constructor_args():
    sig = inspect.signature(Example_Ba.__init__)
    params = list(sig.parameters.keys())
    assert "ba" in params, "Missing parameter 'ba'"

def test_example_ba_has_ba():
    assert hasattr(Example_Ba, "ba")
    descriptor = None
    for klass in Example_Ba.__mro__:
        if "ba" in klass.__dict__:
            descriptor = klass.__dict__["ba"]
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
Example_B_strategy = st.builds(
    Example_B,
    b=
        safe_text
)
Example_A_strategy = st.builds(
    Example_A,
    a=
        safe_text
)
B_strategy = st.builds(
    B,
)
Example_Bb_strategy = st.builds(
    Example_Bb,
)
Example_Ba_strategy = st.builds(
    Example_Ba,
    ba=
        safe_text
)

@given(instance=Example_B_strategy)
@settings(max_examples=50)
def test_example_b_instantiation(instance):
    assert isinstance(instance, Example_B)



@given(instance=Example_B_strategy)
def test_example_b_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=Example_A_strategy)
@settings(max_examples=50)
def test_example_a_instantiation(instance):
    assert isinstance(instance, Example_A)



@given(instance=Example_A_strategy)
def test_example_a_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=Example_Bb_strategy)
@settings(max_examples=50)
def test_example_bb_instantiation(instance):
    assert isinstance(instance, Example_Bb)

@given(instance=Example_Ba_strategy)
@settings(max_examples=50)
def test_example_ba_instantiation(instance):
    assert isinstance(instance, Example_Ba)



@given(instance=Example_Ba_strategy)
def test_example_ba_ba_setter(instance):
    original = instance.ba
    instance.ba = original
    assert instance.ba == original
