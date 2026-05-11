import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Abc::C,
    Abc::classB,
    Abc::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abc::c_is_not_abstract():
    assert not inspect.isabstract(Abc::C)


def test_abc::c_constructor_exists():
    assert callable(Abc::C.__init__)


def test_abc::c_constructor_args():
    sig = inspect.signature(Abc::C.__init__)
    params = list(sig.parameters.keys())



def test_abc::classb_is_not_abstract():
    assert not inspect.isabstract(Abc::classB)


def test_abc::classb_constructor_exists():
    assert callable(Abc::classB.__init__)


def test_abc::classb_constructor_args():
    sig = inspect.signature(Abc::classB.__init__)
    params = list(sig.parameters.keys())



def test_abc::a_is_not_abstract():
    assert not inspect.isabstract(Abc::A)


def test_abc::a_constructor_exists():
    assert callable(Abc::A.__init__)


def test_abc::a_constructor_args():
    sig = inspect.signature(Abc::A.__init__)
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
Abc::C_strategy = st.builds(
    Abc::C,
)
Abc::classB_strategy = st.builds(
    Abc::classB,
)
Abc::A_strategy = st.builds(
    Abc::A,
)

@given(instance=Abc::C_strategy)
@settings(max_examples=50)
def test_abc::c_instantiation(instance):
    assert isinstance(instance, Abc::C)

@given(instance=Abc::classB_strategy)
@settings(max_examples=50)
def test_abc::classb_instantiation(instance):
    assert isinstance(instance, Abc::classB)

@given(instance=Abc::A_strategy)
@settings(max_examples=50)
def test_abc::a_instantiation(instance):
    assert isinstance(instance, Abc::A)
