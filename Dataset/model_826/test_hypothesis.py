import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    wheel_Transition,
    wheel_State,
    wheel_WheelSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_wheel_transition_is_not_abstract():
    assert not inspect.isabstract(wheel_Transition)


def test_wheel_transition_constructor_exists():
    assert callable(wheel_Transition.__init__)


def test_wheel_transition_constructor_args():
    sig = inspect.signature(wheel_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"
    assert "time" in params, "Missing parameter 'time'"

def test_wheel_transition_has_speed():
    assert hasattr(wheel_Transition, "speed")
    descriptor = None
    for klass in wheel_Transition.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_wheel_transition_has_time():
    assert hasattr(wheel_Transition, "time")
    descriptor = None
    for klass in wheel_Transition.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_wheel_state_is_not_abstract():
    assert not inspect.isabstract(wheel_State)


def test_wheel_state_constructor_exists():
    assert callable(wheel_State.__init__)


def test_wheel_state_constructor_args():
    sig = inspect.signature(wheel_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wheel_state_has_name():
    assert hasattr(wheel_State, "name")
    descriptor = None
    for klass in wheel_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wheel_wheelsm_is_not_abstract():
    assert not inspect.isabstract(wheel_WheelSM)


def test_wheel_wheelsm_constructor_exists():
    assert callable(wheel_WheelSM.__init__)


def test_wheel_wheelsm_constructor_args():
    sig = inspect.signature(wheel_WheelSM.__init__)
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
wheel_Transition_strategy = st.builds(
    wheel_Transition,
    speed=
        safe_text,
    time=
        safe_text
)
wheel_State_strategy = st.builds(
    wheel_State,
    name=
        safe_text
)
wheel_WheelSM_strategy = st.builds(
    wheel_WheelSM,
)

@given(instance=wheel_Transition_strategy)
@settings(max_examples=50)
def test_wheel_transition_instantiation(instance):
    assert isinstance(instance, wheel_Transition)



@given(instance=wheel_Transition_strategy)
def test_wheel_transition_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original



@given(instance=wheel_Transition_strategy)
def test_wheel_transition_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=wheel_State_strategy)
@settings(max_examples=50)
def test_wheel_state_instantiation(instance):
    assert isinstance(instance, wheel_State)



@given(instance=wheel_State_strategy)
def test_wheel_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=wheel_WheelSM_strategy)
@settings(max_examples=50)
def test_wheel_wheelsm_instantiation(instance):
    assert isinstance(instance, wheel_WheelSM)
