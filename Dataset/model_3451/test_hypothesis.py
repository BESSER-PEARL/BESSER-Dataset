import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    School_Buzzer,
    School_Clock,
    School_SchoolRoom,
    School_School,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_school_buzzer_is_not_abstract():
    assert not inspect.isabstract(School_Buzzer)


def test_school_buzzer_constructor_exists():
    assert callable(School_Buzzer.__init__)


def test_school_buzzer_constructor_args():
    sig = inspect.signature(School_Buzzer.__init__)
    params = list(sig.parameters.keys())



def test_school_clock_is_not_abstract():
    assert not inspect.isabstract(School_Clock)


def test_school_clock_constructor_exists():
    assert callable(School_Clock.__init__)


def test_school_clock_constructor_args():
    sig = inspect.signature(School_Clock.__init__)
    params = list(sig.parameters.keys())



def test_school_schoolroom_is_not_abstract():
    assert not inspect.isabstract(School_SchoolRoom)


def test_school_schoolroom_constructor_exists():
    assert callable(School_SchoolRoom.__init__)


def test_school_schoolroom_constructor_args():
    sig = inspect.signature(School_SchoolRoom.__init__)
    params = list(sig.parameters.keys())



def test_school_school_is_not_abstract():
    assert not inspect.isabstract(School_School)


def test_school_school_constructor_exists():
    assert callable(School_School.__init__)


def test_school_school_constructor_args():
    sig = inspect.signature(School_School.__init__)
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
School_Buzzer_strategy = st.builds(
    School_Buzzer,
)
School_Clock_strategy = st.builds(
    School_Clock,
)
School_SchoolRoom_strategy = st.builds(
    School_SchoolRoom,
)
School_School_strategy = st.builds(
    School_School,
)

@given(instance=School_Buzzer_strategy)
@settings(max_examples=50)
def test_school_buzzer_instantiation(instance):
    assert isinstance(instance, School_Buzzer)

@given(instance=School_Clock_strategy)
@settings(max_examples=50)
def test_school_clock_instantiation(instance):
    assert isinstance(instance, School_Clock)

@given(instance=School_SchoolRoom_strategy)
@settings(max_examples=50)
def test_school_schoolroom_instantiation(instance):
    assert isinstance(instance, School_SchoolRoom)

@given(instance=School_School_strategy)
@settings(max_examples=50)
def test_school_school_instantiation(instance):
    assert isinstance(instance, School_School)
