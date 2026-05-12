import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    arduinoml_NamedElement,
    arduinoml_Trigger,
    Action,
    arduinoml_Wait,
    arduinoml_On,
    arduinoml_Off,
    Brick,
    arduinoml_Actuator,
    arduinoml_Sensor,
    arduinoml_Board,
    arduinoml_Action,
    NamedElement,
    arduinoml_State,
    arduinoml_Transition,
    arduinoml_Brick,
    DigitalValue,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_arduinoml_namedelement_is_not_abstract():
    assert not inspect.isabstract(arduinoml_NamedElement)


def test_arduinoml_namedelement_constructor_exists():
    assert callable(arduinoml_NamedElement.__init__)


def test_arduinoml_namedelement_constructor_args():
    sig = inspect.signature(arduinoml_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduinoml_namedelement_has_name():
    assert hasattr(arduinoml_NamedElement, "name")
    descriptor = None
    for klass in arduinoml_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml_trigger_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Trigger)


def test_arduinoml_trigger_constructor_exists():
    assert callable(arduinoml_Trigger.__init__)


def test_arduinoml_trigger_constructor_args():
    sig = inspect.signature(arduinoml_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduinoml_trigger_has_value():
    assert hasattr(arduinoml_Trigger, "value")
    descriptor = None
    for klass in arduinoml_Trigger.__mro__:
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



def test_arduinoml_wait_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Wait)


def test_arduinoml_wait_constructor_exists():
    assert callable(arduinoml_Wait.__init__)


def test_arduinoml_wait_constructor_args():
    sig = inspect.signature(arduinoml_Wait.__init__)
    params = list(sig.parameters.keys())
    assert "waitingTime" in params, "Missing parameter 'waitingTime'"

def test_arduinoml_wait_has_waitingTime():
    assert hasattr(arduinoml_Wait, "waitingTime")
    descriptor = None
    for klass in arduinoml_Wait.__mro__:
        if "waitingTime" in klass.__dict__:
            descriptor = klass.__dict__["waitingTime"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml_on_is_not_abstract():
    assert not inspect.isabstract(arduinoml_On)


def test_arduinoml_on_constructor_exists():
    assert callable(arduinoml_On.__init__)


def test_arduinoml_on_constructor_args():
    sig = inspect.signature(arduinoml_On.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_off_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Off)


def test_arduinoml_off_constructor_exists():
    assert callable(arduinoml_Off.__init__)


def test_arduinoml_off_constructor_args():
    sig = inspect.signature(arduinoml_Off.__init__)
    params = list(sig.parameters.keys())



def test_brick_is_not_abstract():
    assert not inspect.isabstract(Brick)


def test_brick_constructor_exists():
    assert callable(Brick.__init__)


def test_brick_constructor_args():
    sig = inspect.signature(Brick.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_actuator_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Actuator)


def test_arduinoml_actuator_constructor_exists():
    assert callable(arduinoml_Actuator.__init__)


def test_arduinoml_actuator_constructor_args():
    sig = inspect.signature(arduinoml_Actuator.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_sensor_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Sensor)


def test_arduinoml_sensor_constructor_exists():
    assert callable(arduinoml_Sensor.__init__)


def test_arduinoml_sensor_constructor_args():
    sig = inspect.signature(arduinoml_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_board_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Board)


def test_arduinoml_board_constructor_exists():
    assert callable(arduinoml_Board.__init__)


def test_arduinoml_board_constructor_args():
    sig = inspect.signature(arduinoml_Board.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_action_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Action)


def test_arduinoml_action_constructor_exists():
    assert callable(arduinoml_Action.__init__)


def test_arduinoml_action_constructor_args():
    sig = inspect.signature(arduinoml_Action.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_state_is_not_abstract():
    assert not inspect.isabstract(arduinoml_State)


def test_arduinoml_state_constructor_exists():
    assert callable(arduinoml_State.__init__)


def test_arduinoml_state_constructor_args():
    sig = inspect.signature(arduinoml_State.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_transition_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Transition)


def test_arduinoml_transition_constructor_exists():
    assert callable(arduinoml_Transition.__init__)


def test_arduinoml_transition_constructor_args():
    sig = inspect.signature(arduinoml_Transition.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_brick_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Brick)


def test_arduinoml_brick_constructor_exists():
    assert callable(arduinoml_Brick.__init__)


def test_arduinoml_brick_constructor_args():
    sig = inspect.signature(arduinoml_Brick.__init__)
    params = list(sig.parameters.keys())
    assert "pin" in params, "Missing parameter 'pin'"

def test_arduinoml_brick_has_pin():
    assert hasattr(arduinoml_Brick, "pin")
    descriptor = None
    for klass in arduinoml_Brick.__mro__:
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
arduinoml_NamedElement_strategy = st.builds(
    arduinoml_NamedElement,
    name=
        safe_text
)
arduinoml_Trigger_strategy = st.builds(
    arduinoml_Trigger,
    value=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
arduinoml_Wait_strategy = st.builds(
    arduinoml_Wait,
    waitingTime=
        st.integers()
)
arduinoml_On_strategy = st.builds(
    arduinoml_On,
)
arduinoml_Off_strategy = st.builds(
    arduinoml_Off,
)
Brick_strategy = st.builds(
    Brick,
)
arduinoml_Actuator_strategy = st.builds(
    arduinoml_Actuator,
)
arduinoml_Sensor_strategy = st.builds(
    arduinoml_Sensor,
)
arduinoml_Board_strategy = st.builds(
    arduinoml_Board,
)
arduinoml_Action_strategy = st.builds(
    arduinoml_Action,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
arduinoml_State_strategy = st.builds(
    arduinoml_State,
)
arduinoml_Transition_strategy = st.builds(
    arduinoml_Transition,
)
arduinoml_Brick_strategy = st.builds(
    arduinoml_Brick,
    pin=
        st.integers()
)

@given(instance=arduinoml_NamedElement_strategy)
@settings(max_examples=50)
def test_arduinoml_namedelement_instantiation(instance):
    assert isinstance(instance, arduinoml_NamedElement)



@given(instance=arduinoml_NamedElement_strategy)
def test_arduinoml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduinoml_Trigger_strategy)
@settings(max_examples=50)
def test_arduinoml_trigger_instantiation(instance):
    assert isinstance(instance, arduinoml_Trigger)



@given(instance=arduinoml_Trigger_strategy)
def test_arduinoml_trigger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=arduinoml_Wait_strategy)
@settings(max_examples=50)
def test_arduinoml_wait_instantiation(instance):
    assert isinstance(instance, arduinoml_Wait)



@given(instance=arduinoml_Wait_strategy)
def test_arduinoml_wait_waitingTime_setter(instance):
    original = instance.waitingTime
    instance.waitingTime = original
    assert instance.waitingTime == original

@given(instance=arduinoml_On_strategy)
@settings(max_examples=50)
def test_arduinoml_on_instantiation(instance):
    assert isinstance(instance, arduinoml_On)

@given(instance=arduinoml_Off_strategy)
@settings(max_examples=50)
def test_arduinoml_off_instantiation(instance):
    assert isinstance(instance, arduinoml_Off)

@given(instance=Brick_strategy)
@settings(max_examples=50)
def test_brick_instantiation(instance):
    assert isinstance(instance, Brick)

@given(instance=arduinoml_Actuator_strategy)
@settings(max_examples=50)
def test_arduinoml_actuator_instantiation(instance):
    assert isinstance(instance, arduinoml_Actuator)

@given(instance=arduinoml_Sensor_strategy)
@settings(max_examples=50)
def test_arduinoml_sensor_instantiation(instance):
    assert isinstance(instance, arduinoml_Sensor)

@given(instance=arduinoml_Board_strategy)
@settings(max_examples=50)
def test_arduinoml_board_instantiation(instance):
    assert isinstance(instance, arduinoml_Board)

@given(instance=arduinoml_Action_strategy)
@settings(max_examples=50)
def test_arduinoml_action_instantiation(instance):
    assert isinstance(instance, arduinoml_Action)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=arduinoml_State_strategy)
@settings(max_examples=50)
def test_arduinoml_state_instantiation(instance):
    assert isinstance(instance, arduinoml_State)

@given(instance=arduinoml_Transition_strategy)
@settings(max_examples=50)
def test_arduinoml_transition_instantiation(instance):
    assert isinstance(instance, arduinoml_Transition)

@given(instance=arduinoml_Brick_strategy)
@settings(max_examples=50)
def test_arduinoml_brick_instantiation(instance):
    assert isinstance(instance, arduinoml_Brick)



@given(instance=arduinoml_Brick_strategy)
def test_arduinoml_brick_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original
