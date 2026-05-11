import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CoachBusWithEDataType::Coach,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_coachbuswithedatatype::coach_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::Coach)


def test_coachbuswithedatatype::coach_constructor_exists():
    assert callable(CoachBusWithEDataType::Coach.__init__)


def test_coachbuswithedatatype::coach_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::Coach.__init__)
    params = list(sig.parameters.keys())
    assert "noOfSeats" in params, "Missing parameter 'noOfSeats'"

def test_coachbuswithedatatype::coach_has_noOfSeats():
    assert hasattr(CoachBusWithEDataType::Coach, "noOfSeats")
    descriptor = None
    for klass in CoachBusWithEDataType::Coach.__mro__:
        if "noOfSeats" in klass.__dict__:
            descriptor = klass.__dict__["noOfSeats"]
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
CoachBusWithEDataType::Coach_strategy = st.builds(
    CoachBusWithEDataType::Coach,
    noOfSeats=
        st.integers()
)

@given(instance=CoachBusWithEDataType::Coach_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::coach_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::Coach)

@given(instance=CoachBusWithEDataType::Coach_strategy)
def test_coachbuswithedatatype::coach_noOfSeats_type(instance):
    assert isinstance(instance.noOfSeats, int)


@given(instance=CoachBusWithEDataType::Coach_strategy)
def test_coachbuswithedatatype::coach_noOfSeats_setter(instance):
    original = instance.noOfSeats
    instance.noOfSeats = original
    assert instance.noOfSeats == original
