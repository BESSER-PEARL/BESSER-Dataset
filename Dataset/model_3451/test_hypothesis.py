import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    School::Buzzer,
    School::Clock,
    School::SchoolRoom,
    School::School,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_school::buzzer_is_not_abstract():
    assert not inspect.isabstract(School::Buzzer)


def test_school::buzzer_constructor_exists():
    assert callable(School::Buzzer.__init__)


def test_school::buzzer_constructor_args():
    sig = inspect.signature(School::Buzzer.__init__)
    params = list(sig.parameters.keys())



def test_school::clock_is_not_abstract():
    assert not inspect.isabstract(School::Clock)


def test_school::clock_constructor_exists():
    assert callable(School::Clock.__init__)


def test_school::clock_constructor_args():
    sig = inspect.signature(School::Clock.__init__)
    params = list(sig.parameters.keys())



def test_school::schoolroom_is_not_abstract():
    assert not inspect.isabstract(School::SchoolRoom)


def test_school::schoolroom_constructor_exists():
    assert callable(School::SchoolRoom.__init__)


def test_school::schoolroom_constructor_args():
    sig = inspect.signature(School::SchoolRoom.__init__)
    params = list(sig.parameters.keys())



def test_school::school_is_not_abstract():
    assert not inspect.isabstract(School::School)


def test_school::school_constructor_exists():
    assert callable(School::School.__init__)


def test_school::school_constructor_args():
    sig = inspect.signature(School::School.__init__)
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
School::Buzzer_strategy = st.builds(
    School::Buzzer,
)
School::Clock_strategy = st.builds(
    School::Clock,
)
School::SchoolRoom_strategy = st.builds(
    School::SchoolRoom,
)
School::School_strategy = st.builds(
    School::School,
)

@given(instance=School::Buzzer_strategy)
@settings(max_examples=50)
def test_school::buzzer_instantiation(instance):
    assert isinstance(instance, School::Buzzer)

@given(instance=School::Clock_strategy)
@settings(max_examples=50)
def test_school::clock_instantiation(instance):
    assert isinstance(instance, School::Clock)

@given(instance=School::SchoolRoom_strategy)
@settings(max_examples=50)
def test_school::schoolroom_instantiation(instance):
    assert isinstance(instance, School::SchoolRoom)

@given(instance=School::School_strategy)
@settings(max_examples=50)
def test_school::school_instantiation(instance):
    assert isinstance(instance, School::School)
