import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    A,
    root::SubA,
    root::B,
    SuperA,
    root::A,
    root::SuperA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_root::suba_is_not_abstract():
    assert not inspect.isabstract(root::SubA)


def test_root::suba_constructor_exists():
    assert callable(root::SubA.__init__)


def test_root::suba_constructor_args():
    sig = inspect.signature(root::SubA.__init__)
    params = list(sig.parameters.keys())



def test_root::b_is_not_abstract():
    assert not inspect.isabstract(root::B)


def test_root::b_constructor_exists():
    assert callable(root::B.__init__)


def test_root::b_constructor_args():
    sig = inspect.signature(root::B.__init__)
    params = list(sig.parameters.keys())



def test_supera_is_not_abstract():
    assert not inspect.isabstract(SuperA)


def test_supera_constructor_exists():
    assert callable(SuperA.__init__)


def test_supera_constructor_args():
    sig = inspect.signature(SuperA.__init__)
    params = list(sig.parameters.keys())



def test_root::a_is_not_abstract():
    assert not inspect.isabstract(root::A)


def test_root::a_constructor_exists():
    assert callable(root::A.__init__)


def test_root::a_constructor_args():
    sig = inspect.signature(root::A.__init__)
    params = list(sig.parameters.keys())



def test_root::supera_is_not_abstract():
    assert not inspect.isabstract(root::SuperA)


def test_root::supera_constructor_exists():
    assert callable(root::SuperA.__init__)


def test_root::supera_constructor_args():
    sig = inspect.signature(root::SuperA.__init__)
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
A_strategy = st.builds(
    A,
)
root::SubA_strategy = st.builds(
    root::SubA,
)
root::B_strategy = st.builds(
    root::B,
)
SuperA_strategy = st.builds(
    SuperA,
)
root::A_strategy = st.builds(
    root::A,
)
root::SuperA_strategy = st.builds(
    root::SuperA,
)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=root::SubA_strategy)
@settings(max_examples=50)
def test_root::suba_instantiation(instance):
    assert isinstance(instance, root::SubA)

@given(instance=root::B_strategy)
@settings(max_examples=50)
def test_root::b_instantiation(instance):
    assert isinstance(instance, root::B)

@given(instance=SuperA_strategy)
@settings(max_examples=50)
def test_supera_instantiation(instance):
    assert isinstance(instance, SuperA)

@given(instance=root::A_strategy)
@settings(max_examples=50)
def test_root::a_instantiation(instance):
    assert isinstance(instance, root::A)

@given(instance=root::SuperA_strategy)
@settings(max_examples=50)
def test_root::supera_instantiation(instance):
    assert isinstance(instance, root::SuperA)
