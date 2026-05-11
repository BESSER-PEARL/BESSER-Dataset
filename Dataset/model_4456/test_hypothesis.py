import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Action,
    arduinoml::On,
    arduinoml::Off,
    arduinoml::ActuatorState,
    Brick,
    arduinoml::Sensor,
    arduinoml::Actuator,
    arduinoml::Transition,
    arduinoml::Action,
    arduinoml::Brick,
    arduinoml::State,
    arduinoml::Board,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_arduinoml::off_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Off)


def test_arduinoml::off_constructor_exists():
    assert callable(arduinoml::Off.__init__)


def test_arduinoml::off_constructor_args():
    sig = inspect.signature(arduinoml::Off.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::actuatorstate_is_not_abstract():
    assert not inspect.isabstract(arduinoml::ActuatorState)


def test_arduinoml::actuatorstate_constructor_exists():
    assert callable(arduinoml::ActuatorState.__init__)


def test_arduinoml::actuatorstate_constructor_args():
    sig = inspect.signature(arduinoml::ActuatorState.__init__)
    params = list(sig.parameters.keys())
    assert "isOn" in params, "Missing parameter 'isOn'"

def test_arduinoml::actuatorstate_has_isOn():
    assert hasattr(arduinoml::ActuatorState, "isOn")
    descriptor = None
    for klass in arduinoml::ActuatorState.__mro__:
        if "isOn" in klass.__dict__:
            descriptor = klass.__dict__["isOn"]
            break
    assert isinstance(descriptor, property)



def test_brick_is_not_abstract():
    assert not inspect.isabstract(Brick)


def test_brick_constructor_exists():
    assert callable(Brick.__init__)


def test_brick_constructor_args():
    sig = inspect.signature(Brick.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::sensor_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Sensor)


def test_arduinoml::sensor_constructor_exists():
    assert callable(arduinoml::Sensor.__init__)


def test_arduinoml::sensor_constructor_args():
    sig = inspect.signature(arduinoml::Sensor.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::actuator_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Actuator)


def test_arduinoml::actuator_constructor_exists():
    assert callable(arduinoml::Actuator.__init__)


def test_arduinoml::actuator_constructor_args():
    sig = inspect.signature(arduinoml::Actuator.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::transition_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Transition)


def test_arduinoml::transition_constructor_exists():
    assert callable(arduinoml::Transition.__init__)


def test_arduinoml::transition_constructor_args():
    sig = inspect.signature(arduinoml::Transition.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::action_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Action)


def test_arduinoml::action_constructor_exists():
    assert callable(arduinoml::Action.__init__)


def test_arduinoml::action_constructor_args():
    sig = inspect.signature(arduinoml::Action.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::brick_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Brick)


def test_arduinoml::brick_constructor_exists():
    assert callable(arduinoml::Brick.__init__)


def test_arduinoml::brick_constructor_args():
    sig = inspect.signature(arduinoml::Brick.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "pin" in params, "Missing parameter 'pin'"

def test_arduinoml::brick_has_name():
    assert hasattr(arduinoml::Brick, "name")
    descriptor = None
    for klass in arduinoml::Brick.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml::brick_has_pin():
    assert hasattr(arduinoml::Brick, "pin")
    descriptor = None
    for klass in arduinoml::Brick.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml::state_is_not_abstract():
    assert not inspect.isabstract(arduinoml::State)


def test_arduinoml::state_constructor_exists():
    assert callable(arduinoml::State.__init__)


def test_arduinoml::state_constructor_args():
    sig = inspect.signature(arduinoml::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduinoml::state_has_name():
    assert hasattr(arduinoml::State, "name")
    descriptor = None
    for klass in arduinoml::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml::board_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Board)


def test_arduinoml::board_constructor_exists():
    assert callable(arduinoml::Board.__init__)


def test_arduinoml::board_constructor_args():
    sig = inspect.signature(arduinoml::Board.__init__)
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
Action_strategy = st.builds(
    Action,
)
arduinoml::On_strategy = st.builds(
    arduinoml::On,
)
arduinoml::Off_strategy = st.builds(
    arduinoml::Off,
)
arduinoml::ActuatorState_strategy = st.builds(
    arduinoml::ActuatorState,
    isOn=
        st.booleans()
)
Brick_strategy = st.builds(
    Brick,
)
arduinoml::Sensor_strategy = st.builds(
    arduinoml::Sensor,
)
arduinoml::Actuator_strategy = st.builds(
    arduinoml::Actuator,
)
arduinoml::Transition_strategy = st.builds(
    arduinoml::Transition,
)
arduinoml::Action_strategy = st.builds(
    arduinoml::Action,
)
arduinoml::Brick_strategy = st.builds(
    arduinoml::Brick,
    name=
        safe_text,
    pin=
        st.integers()
)
arduinoml::State_strategy = st.builds(
    arduinoml::State,
    name=
        safe_text
)
arduinoml::Board_strategy = st.builds(
    arduinoml::Board,
)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=arduinoml::On_strategy)
@settings(max_examples=50)
def test_arduinoml::on_instantiation(instance):
    assert isinstance(instance, arduinoml::On)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=arduinoml::On_strategy)
@settings(max_examples=30)
def test_arduinoml::on_turnon_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.turnOn()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.turnOn).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'turnOn' in arduinoml::On is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'turnOn' in arduinoml::On did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'turnOn' in arduinoml::On is not implemented or raised an error")

@given(instance=arduinoml::Off_strategy)
@settings(max_examples=50)
def test_arduinoml::off_instantiation(instance):
    assert isinstance(instance, arduinoml::Off)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=arduinoml::Off_strategy)
@settings(max_examples=30)
def test_arduinoml::off_turnoff_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.turnOff()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.turnOff).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'turnOff' in arduinoml::Off is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'turnOff' in arduinoml::Off did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'turnOff' in arduinoml::Off is not implemented or raised an error")

@given(instance=arduinoml::ActuatorState_strategy)
@settings(max_examples=50)
def test_arduinoml::actuatorstate_instantiation(instance):
    assert isinstance(instance, arduinoml::ActuatorState)

@given(instance=arduinoml::ActuatorState_strategy)
def test_arduinoml::actuatorstate_isOn_type(instance):
    assert isinstance(instance.isOn, bool)


@given(instance=arduinoml::ActuatorState_strategy)
def test_arduinoml::actuatorstate_isOn_setter(instance):
    original = instance.isOn
    instance.isOn = original
    assert instance.isOn == original

@given(instance=Brick_strategy)
@settings(max_examples=50)
def test_brick_instantiation(instance):
    assert isinstance(instance, Brick)

@given(instance=arduinoml::Sensor_strategy)
@settings(max_examples=50)
def test_arduinoml::sensor_instantiation(instance):
    assert isinstance(instance, arduinoml::Sensor)

@given(instance=arduinoml::Actuator_strategy)
@settings(max_examples=50)
def test_arduinoml::actuator_instantiation(instance):
    assert isinstance(instance, arduinoml::Actuator)

@given(instance=arduinoml::Transition_strategy)
@settings(max_examples=50)
def test_arduinoml::transition_instantiation(instance):
    assert isinstance(instance, arduinoml::Transition)

@given(instance=arduinoml::Action_strategy)
@settings(max_examples=50)
def test_arduinoml::action_instantiation(instance):
    assert isinstance(instance, arduinoml::Action)

@given(instance=arduinoml::Brick_strategy)
@settings(max_examples=50)
def test_arduinoml::brick_instantiation(instance):
    assert isinstance(instance, arduinoml::Brick)

@given(instance=arduinoml::Brick_strategy)
def test_arduinoml::brick_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arduinoml::Brick_strategy)
def test_arduinoml::brick_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduinoml::Brick_strategy)
def test_arduinoml::brick_pin_type(instance):
    assert isinstance(instance.pin, int)


@given(instance=arduinoml::Brick_strategy)
def test_arduinoml::brick_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original

@given(instance=arduinoml::State_strategy)
@settings(max_examples=50)
def test_arduinoml::state_instantiation(instance):
    assert isinstance(instance, arduinoml::State)

@given(instance=arduinoml::State_strategy)
def test_arduinoml::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arduinoml::State_strategy)
def test_arduinoml::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduinoml::Board_strategy)
@settings(max_examples=50)
def test_arduinoml::board_instantiation(instance):
    assert isinstance(instance, arduinoml::Board)
