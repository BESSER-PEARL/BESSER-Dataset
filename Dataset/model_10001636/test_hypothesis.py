import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Elevator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_elevator_is_not_abstract():
    assert not inspect.isabstract(Elevator)


def test_elevator_constructor_exists():
    assert callable(Elevator.__init__)


def test_elevator_constructor_args():
    sig = inspect.signature(Elevator.__init__)
    params = list(sig.parameters.keys())
    assert "Floor" in params, "Missing parameter 'Floor'"

def test_elevator_has_Floor():
    assert hasattr(Elevator, "Floor")
    descriptor = None
    for klass in Elevator.__mro__:
        if "Floor" in klass.__dict__:
            descriptor = klass.__dict__["Floor"]
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
Elevator_strategy = st.builds(
    Elevator,
    Floor=
        st.integers()
)

@given(instance=Elevator_strategy)
@settings(max_examples=50)
def test_elevator_instantiation(instance):
    assert isinstance(instance, Elevator)



@given(instance=Elevator_strategy)
def test_elevator_Floor_setter(instance):
    original = instance.Floor
    instance.Floor = original
    assert instance.Floor == original
