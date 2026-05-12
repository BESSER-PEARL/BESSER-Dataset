import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statemachines_EventOccurrence,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachines_eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(statemachines_EventOccurrence)


def test_statemachines_eventoccurrence_constructor_exists():
    assert callable(statemachines_EventOccurrence.__init__)


def test_statemachines_eventoccurrence_constructor_args():
    sig = inspect.signature(statemachines_EventOccurrence.__init__)
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
statemachines_EventOccurrence_strategy = st.builds(
    statemachines_EventOccurrence,
)

@given(instance=statemachines_EventOccurrence_strategy)
@settings(max_examples=50)
def test_statemachines_eventoccurrence_instantiation(instance):
    assert isinstance(instance, statemachines_EventOccurrence)
