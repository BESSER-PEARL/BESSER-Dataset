import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    wheel::Transition,
    wheel::State,
    wheel::WheelSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_wheel::transition_is_not_abstract():
    assert not inspect.isabstract(wheel::Transition)


def test_wheel::transition_constructor_exists():
    assert callable(wheel::Transition.__init__)


def test_wheel::transition_constructor_args():
    sig = inspect.signature(wheel::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"
    assert "time" in params, "Missing parameter 'time'"

def test_wheel::transition_has_speed():
    assert hasattr(wheel::Transition, "speed")
    descriptor = None
    for klass in wheel::Transition.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_wheel::transition_has_time():
    assert hasattr(wheel::Transition, "time")
    descriptor = None
    for klass in wheel::Transition.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_wheel::state_is_not_abstract():
    assert not inspect.isabstract(wheel::State)


def test_wheel::state_constructor_exists():
    assert callable(wheel::State.__init__)


def test_wheel::state_constructor_args():
    sig = inspect.signature(wheel::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wheel::state_has_name():
    assert hasattr(wheel::State, "name")
    descriptor = None
    for klass in wheel::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wheel::wheelsm_is_not_abstract():
    assert not inspect.isabstract(wheel::WheelSM)


def test_wheel::wheelsm_constructor_exists():
    assert callable(wheel::WheelSM.__init__)


def test_wheel::wheelsm_constructor_args():
    sig = inspect.signature(wheel::WheelSM.__init__)
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
wheel::Transition_strategy = st.builds(
    wheel::Transition,
    speed=
        safe_text,
    time=
        safe_text
)
wheel::State_strategy = st.builds(
    wheel::State,
    name=
        safe_text
)
wheel::WheelSM_strategy = st.builds(
    wheel::WheelSM,
)

@given(instance=wheel::Transition_strategy)
@settings(max_examples=50)
def test_wheel::transition_instantiation(instance):
    assert isinstance(instance, wheel::Transition)

@given(instance=wheel::Transition_strategy)
def test_wheel::transition_speed_type(instance):
    assert isinstance(instance.speed, str)


@given(instance=wheel::Transition_strategy)
def test_wheel::transition_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=wheel::Transition_strategy)
def test_wheel::transition_time_type(instance):
    assert isinstance(instance.time, str)


@given(instance=wheel::Transition_strategy)
def test_wheel::transition_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=wheel::State_strategy)
@settings(max_examples=50)
def test_wheel::state_instantiation(instance):
    assert isinstance(instance, wheel::State)

@given(instance=wheel::State_strategy)
def test_wheel::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=wheel::State_strategy)
def test_wheel::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=wheel::WheelSM_strategy)
@settings(max_examples=50)
def test_wheel::wheelsm_instantiation(instance):
    assert isinstance(instance, wheel::WheelSM)
