import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ABC::D,
    A,
    ABC::C,
    ABC::B,
    ABC::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abc::d_is_not_abstract():
    assert not inspect.isabstract(ABC::D)


def test_abc::d_constructor_exists():
    assert callable(ABC::D.__init__)


def test_abc::d_constructor_args():
    sig = inspect.signature(ABC::D.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_abc::c_is_not_abstract():
    assert not inspect.isabstract(ABC::C)


def test_abc::c_constructor_exists():
    assert callable(ABC::C.__init__)


def test_abc::c_constructor_args():
    sig = inspect.signature(ABC::C.__init__)
    params = list(sig.parameters.keys())



def test_abc::b_is_not_abstract():
    assert not inspect.isabstract(ABC::B)


def test_abc::b_constructor_exists():
    assert callable(ABC::B.__init__)


def test_abc::b_constructor_args():
    sig = inspect.signature(ABC::B.__init__)
    params = list(sig.parameters.keys())



def test_abc::a_is_not_abstract():
    assert not inspect.isabstract(ABC::A)


def test_abc::a_constructor_exists():
    assert callable(ABC::A.__init__)


def test_abc::a_constructor_args():
    sig = inspect.signature(ABC::A.__init__)
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
ABC::D_strategy = st.builds(
    ABC::D,
)
A_strategy = st.builds(
    A,
)
ABC::C_strategy = st.builds(
    ABC::C,
)
ABC::B_strategy = st.builds(
    ABC::B,
)
ABC::A_strategy = st.builds(
    ABC::A,
)

@given(instance=ABC::D_strategy)
@settings(max_examples=50)
def test_abc::d_instantiation(instance):
    assert isinstance(instance, ABC::D)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=ABC::C_strategy)
@settings(max_examples=50)
def test_abc::c_instantiation(instance):
    assert isinstance(instance, ABC::C)

@given(instance=ABC::B_strategy)
@settings(max_examples=50)
def test_abc::b_instantiation(instance):
    assert isinstance(instance, ABC::B)

@given(instance=ABC::A_strategy)
@settings(max_examples=50)
def test_abc::a_instantiation(instance):
    assert isinstance(instance, ABC::A)
