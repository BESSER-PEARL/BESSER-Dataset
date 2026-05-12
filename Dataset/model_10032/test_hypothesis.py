import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CoachBus::Coach,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_coachbus::coach_is_not_abstract():
    assert not inspect.isabstract(CoachBus::Coach)


def test_coachbus::coach_constructor_exists():
    assert callable(CoachBus::Coach.__init__)


def test_coachbus::coach_constructor_args():
    sig = inspect.signature(CoachBus::Coach.__init__)
    params = list(sig.parameters.keys())
    assert "noOfSeats" in params, "Missing parameter 'noOfSeats'"

def test_coachbus::coach_has_noOfSeats():
    assert hasattr(CoachBus::Coach, "noOfSeats")
    descriptor = None
    for klass in CoachBus::Coach.__mro__:
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
CoachBus::Coach_strategy = st.builds(
    CoachBus::Coach,
    noOfSeats=
        st.integers()
)

@given(instance=CoachBus::Coach_strategy)
@settings(max_examples=50)
def test_coachbus::coach_instantiation(instance):
    assert isinstance(instance, CoachBus::Coach)

@given(instance=CoachBus::Coach_strategy)
def test_coachbus::coach_noOfSeats_type(instance):
    assert isinstance(instance.noOfSeats, int)


@given(instance=CoachBus::Coach_strategy)
def test_coachbus::coach_noOfSeats_setter(instance):
    original = instance.noOfSeats
    instance.noOfSeats = original
    assert instance.noOfSeats == original
