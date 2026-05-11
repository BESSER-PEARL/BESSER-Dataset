import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    arduinoml::NamedElement,
    arduinoml::Trigger,
    Action,
    arduinoml::On,
    arduinoml::Wait,
    arduinoml::Off,
    Brick,
    arduinoml::Actuator,
    arduinoml::Sensor,
    arduinoml::Board,
    arduinoml::Action,
    NamedElement,
    arduinoml::Transition,
    arduinoml::State,
    arduinoml::Brick,
    DigitalValue,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_arduinoml::namedelement_is_not_abstract():
    assert not inspect.isabstract(arduinoml::NamedElement)


def test_arduinoml::namedelement_constructor_exists():
    assert callable(arduinoml::NamedElement.__init__)


def test_arduinoml::namedelement_constructor_args():
    sig = inspect.signature(arduinoml::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduinoml::namedelement_has_name():
    assert hasattr(arduinoml::NamedElement, "name")
    descriptor = None
    for klass in arduinoml::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml::trigger_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Trigger)


def test_arduinoml::trigger_constructor_exists():
    assert callable(arduinoml::Trigger.__init__)


def test_arduinoml::trigger_constructor_args():
    sig = inspect.signature(arduinoml::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduinoml::trigger_has_value():
    assert hasattr(arduinoml::Trigger, "value")
    descriptor = None
    for klass in arduinoml::Trigger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::on_is_not_abstract():
    assert not inspect.isabstract(arduinoml::On)


def test_arduinoml::on_constructor_exists():
    assert callable(arduinoml::On.__init__)


def test_arduinoml::on_constructor_args():
    sig = inspect.signature(arduinoml::On.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::wait_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Wait)


def test_arduinoml::wait_constructor_exists():
    assert callable(arduinoml::Wait.__init__)


def test_arduinoml::wait_constructor_args():
    sig = inspect.signature(arduinoml::Wait.__init__)
    params = list(sig.parameters.keys())
    assert "waitingTime" in params, "Missing parameter 'waitingTime'"

def test_arduinoml::wait_has_waitingTime():
    assert hasattr(arduinoml::Wait, "waitingTime")
    descriptor = None
    for klass in arduinoml::Wait.__mro__:
        if "waitingTime" in klass.__dict__:
            descriptor = klass.__dict__["waitingTime"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml::off_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Off)


def test_arduinoml::off_constructor_exists():
    assert callable(arduinoml::Off.__init__)


def test_arduinoml::off_constructor_args():
    sig = inspect.signature(arduinoml::Off.__init__)
    params = list(sig.parameters.keys())



def test_brick_is_not_abstract():
    assert not inspect.isabstract(Brick)


def test_brick_constructor_exists():
    assert callable(Brick.__init__)


def test_brick_constructor_args():
    sig = inspect.signature(Brick.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::actuator_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Actuator)


def test_arduinoml::actuator_constructor_exists():
    assert callable(arduinoml::Actuator.__init__)


def test_arduinoml::actuator_constructor_args():
    sig = inspect.signature(arduinoml::Actuator.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::sensor_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Sensor)


def test_arduinoml::sensor_constructor_exists():
    assert callable(arduinoml::Sensor.__init__)


def test_arduinoml::sensor_constructor_args():
    sig = inspect.signature(arduinoml::Sensor.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::board_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Board)


def test_arduinoml::board_constructor_exists():
    assert callable(arduinoml::Board.__init__)


def test_arduinoml::board_constructor_args():
    sig = inspect.signature(arduinoml::Board.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::action_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Action)


def test_arduinoml::action_constructor_exists():
    assert callable(arduinoml::Action.__init__)


def test_arduinoml::action_constructor_args():
    sig = inspect.signature(arduinoml::Action.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::transition_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Transition)


def test_arduinoml::transition_constructor_exists():
    assert callable(arduinoml::Transition.__init__)


def test_arduinoml::transition_constructor_args():
    sig = inspect.signature(arduinoml::Transition.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::state_is_not_abstract():
    assert not inspect.isabstract(arduinoml::State)


def test_arduinoml::state_constructor_exists():
    assert callable(arduinoml::State.__init__)


def test_arduinoml::state_constructor_args():
    sig = inspect.signature(arduinoml::State.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::brick_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Brick)


def test_arduinoml::brick_constructor_exists():
    assert callable(arduinoml::Brick.__init__)


def test_arduinoml::brick_constructor_args():
    sig = inspect.signature(arduinoml::Brick.__init__)
    params = list(sig.parameters.keys())
    assert "pin" in params, "Missing parameter 'pin'"

def test_arduinoml::brick_has_pin():
    assert hasattr(arduinoml::Brick, "pin")
    descriptor = None
    for klass in arduinoml::Brick.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)

def test_digitalvalue_exists():
    # Check that the Enumeration exists
    assert DigitalValue is not None

def test_digitalvalue_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DigitalValue]
    expected_literals = [
        "OFF",
        "ON",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DigitalValue"


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
arduinoml::NamedElement_strategy = st.builds(
    arduinoml::NamedElement,
    name=
        safe_text
)
arduinoml::Trigger_strategy = st.builds(
    arduinoml::Trigger,
    value=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
arduinoml::On_strategy = st.builds(
    arduinoml::On,
)
arduinoml::Wait_strategy = st.builds(
    arduinoml::Wait,
    waitingTime=
        st.integers()
)
arduinoml::Off_strategy = st.builds(
    arduinoml::Off,
)
Brick_strategy = st.builds(
    Brick,
)
arduinoml::Actuator_strategy = st.builds(
    arduinoml::Actuator,
)
arduinoml::Sensor_strategy = st.builds(
    arduinoml::Sensor,
)
arduinoml::Board_strategy = st.builds(
    arduinoml::Board,
)
arduinoml::Action_strategy = st.builds(
    arduinoml::Action,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
arduinoml::Transition_strategy = st.builds(
    arduinoml::Transition,
)
arduinoml::State_strategy = st.builds(
    arduinoml::State,
)
arduinoml::Brick_strategy = st.builds(
    arduinoml::Brick,
    pin=
        st.integers()
)

@given(instance=arduinoml::NamedElement_strategy)
@settings(max_examples=50)
def test_arduinoml::namedelement_instantiation(instance):
    assert isinstance(instance, arduinoml::NamedElement)

@given(instance=arduinoml::NamedElement_strategy)
def test_arduinoml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arduinoml::NamedElement_strategy)
def test_arduinoml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduinoml::Trigger_strategy)
@settings(max_examples=50)
def test_arduinoml::trigger_instantiation(instance):
    assert isinstance(instance, arduinoml::Trigger)

@given(instance=arduinoml::Trigger_strategy)
def test_arduinoml::trigger_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=arduinoml::Trigger_strategy)
def test_arduinoml::trigger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=arduinoml::On_strategy)
@settings(max_examples=50)
def test_arduinoml::on_instantiation(instance):
    assert isinstance(instance, arduinoml::On)

@given(instance=arduinoml::Wait_strategy)
@settings(max_examples=50)
def test_arduinoml::wait_instantiation(instance):
    assert isinstance(instance, arduinoml::Wait)

@given(instance=arduinoml::Wait_strategy)
def test_arduinoml::wait_waitingTime_type(instance):
    assert isinstance(instance.waitingTime, int)


@given(instance=arduinoml::Wait_strategy)
def test_arduinoml::wait_waitingTime_setter(instance):
    original = instance.waitingTime
    instance.waitingTime = original
    assert instance.waitingTime == original

@given(instance=arduinoml::Off_strategy)
@settings(max_examples=50)
def test_arduinoml::off_instantiation(instance):
    assert isinstance(instance, arduinoml::Off)

@given(instance=Brick_strategy)
@settings(max_examples=50)
def test_brick_instantiation(instance):
    assert isinstance(instance, Brick)

@given(instance=arduinoml::Actuator_strategy)
@settings(max_examples=50)
def test_arduinoml::actuator_instantiation(instance):
    assert isinstance(instance, arduinoml::Actuator)

@given(instance=arduinoml::Sensor_strategy)
@settings(max_examples=50)
def test_arduinoml::sensor_instantiation(instance):
    assert isinstance(instance, arduinoml::Sensor)

@given(instance=arduinoml::Board_strategy)
@settings(max_examples=50)
def test_arduinoml::board_instantiation(instance):
    assert isinstance(instance, arduinoml::Board)

@given(instance=arduinoml::Action_strategy)
@settings(max_examples=50)
def test_arduinoml::action_instantiation(instance):
    assert isinstance(instance, arduinoml::Action)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=arduinoml::Transition_strategy)
@settings(max_examples=50)
def test_arduinoml::transition_instantiation(instance):
    assert isinstance(instance, arduinoml::Transition)

@given(instance=arduinoml::State_strategy)
@settings(max_examples=50)
def test_arduinoml::state_instantiation(instance):
    assert isinstance(instance, arduinoml::State)

@given(instance=arduinoml::Brick_strategy)
@settings(max_examples=50)
def test_arduinoml::brick_instantiation(instance):
    assert isinstance(instance, arduinoml::Brick)

@given(instance=arduinoml::Brick_strategy)
def test_arduinoml::brick_pin_type(instance):
    assert isinstance(instance.pin, int)


@given(instance=arduinoml::Brick_strategy)
def test_arduinoml::brick_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original
