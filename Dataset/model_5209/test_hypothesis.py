import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    m::pa::C,
    m::pa::B,
    m::pa::A,
    m::ToplevelClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_m::pa::c_is_not_abstract():
    assert not inspect.isabstract(m::pa::C)


def test_m::pa::c_constructor_exists():
    assert callable(m::pa::C.__init__)


def test_m::pa::c_constructor_args():
    sig = inspect.signature(m::pa::C.__init__)
    params = list(sig.parameters.keys())



def test_m::pa::b_is_not_abstract():
    assert not inspect.isabstract(m::pa::B)


def test_m::pa::b_constructor_exists():
    assert callable(m::pa::B.__init__)


def test_m::pa::b_constructor_args():
    sig = inspect.signature(m::pa::B.__init__)
    params = list(sig.parameters.keys())



def test_m::pa::a_is_not_abstract():
    assert not inspect.isabstract(m::pa::A)


def test_m::pa::a_constructor_exists():
    assert callable(m::pa::A.__init__)


def test_m::pa::a_constructor_args():
    sig = inspect.signature(m::pa::A.__init__)
    params = list(sig.parameters.keys())



def test_m::toplevelclass_is_not_abstract():
    assert not inspect.isabstract(m::ToplevelClass)


def test_m::toplevelclass_constructor_exists():
    assert callable(m::ToplevelClass.__init__)


def test_m::toplevelclass_constructor_args():
    sig = inspect.signature(m::ToplevelClass.__init__)
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
m::pa::C_strategy = st.builds(
    m::pa::C,
)
m::pa::B_strategy = st.builds(
    m::pa::B,
)
m::pa::A_strategy = st.builds(
    m::pa::A,
)
m::ToplevelClass_strategy = st.builds(
    m::ToplevelClass,
)

@given(instance=m::pa::C_strategy)
@settings(max_examples=50)
def test_m::pa::c_instantiation(instance):
    assert isinstance(instance, m::pa::C)

@given(instance=m::pa::B_strategy)
@settings(max_examples=50)
def test_m::pa::b_instantiation(instance):
    assert isinstance(instance, m::pa::B)

@given(instance=m::pa::A_strategy)
@settings(max_examples=50)
def test_m::pa::a_instantiation(instance):
    assert isinstance(instance, m::pa::A)

@given(instance=m::ToplevelClass_strategy)
@settings(max_examples=50)
def test_m::toplevelclass_instantiation(instance):
    assert isinstance(instance, m::ToplevelClass)
