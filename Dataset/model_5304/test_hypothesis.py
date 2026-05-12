import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    A,
    root_SubA,
    root_B,
    SuperA,
    root_A,
    root_SuperA,
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



def test_root_suba_is_not_abstract():
    assert not inspect.isabstract(root_SubA)


def test_root_suba_constructor_exists():
    assert callable(root_SubA.__init__)


def test_root_suba_constructor_args():
    sig = inspect.signature(root_SubA.__init__)
    params = list(sig.parameters.keys())



def test_root_b_is_not_abstract():
    assert not inspect.isabstract(root_B)


def test_root_b_constructor_exists():
    assert callable(root_B.__init__)


def test_root_b_constructor_args():
    sig = inspect.signature(root_B.__init__)
    params = list(sig.parameters.keys())



def test_supera_is_not_abstract():
    assert not inspect.isabstract(SuperA)


def test_supera_constructor_exists():
    assert callable(SuperA.__init__)


def test_supera_constructor_args():
    sig = inspect.signature(SuperA.__init__)
    params = list(sig.parameters.keys())



def test_root_a_is_not_abstract():
    assert not inspect.isabstract(root_A)


def test_root_a_constructor_exists():
    assert callable(root_A.__init__)


def test_root_a_constructor_args():
    sig = inspect.signature(root_A.__init__)
    params = list(sig.parameters.keys())



def test_root_supera_is_not_abstract():
    assert not inspect.isabstract(root_SuperA)


def test_root_supera_constructor_exists():
    assert callable(root_SuperA.__init__)


def test_root_supera_constructor_args():
    sig = inspect.signature(root_SuperA.__init__)
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
root_SubA_strategy = st.builds(
    root_SubA,
)
root_B_strategy = st.builds(
    root_B,
)
SuperA_strategy = st.builds(
    SuperA,
)
root_A_strategy = st.builds(
    root_A,
)
root_SuperA_strategy = st.builds(
    root_SuperA,
)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=root_SubA_strategy)
@settings(max_examples=50)
def test_root_suba_instantiation(instance):
    assert isinstance(instance, root_SubA)

@given(instance=root_B_strategy)
@settings(max_examples=50)
def test_root_b_instantiation(instance):
    assert isinstance(instance, root_B)

@given(instance=SuperA_strategy)
@settings(max_examples=50)
def test_supera_instantiation(instance):
    assert isinstance(instance, SuperA)

@given(instance=root_A_strategy)
@settings(max_examples=50)
def test_root_a_instantiation(instance):
    assert isinstance(instance, root_A)

@given(instance=root_SuperA_strategy)
@settings(max_examples=50)
def test_root_supera_instantiation(instance):
    assert isinstance(instance, root_SuperA)
