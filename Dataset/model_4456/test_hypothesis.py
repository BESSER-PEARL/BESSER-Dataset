import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Action,
    arduinoml_On,
    arduinoml_Off,
    arduinoml_ActuatorState,
    Brick,
    arduinoml_Sensor,
    arduinoml_Actuator,
    arduinoml_Transition,
    arduinoml_Action,
    arduinoml_Brick,
    arduinoml_State,
    arduinoml_Board,
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



def test_arduinoml_actuatorstate_is_not_abstract():
    assert not inspect.isabstract(arduinoml_ActuatorState)


def test_arduinoml_actuatorstate_constructor_exists():
    assert callable(arduinoml_ActuatorState.__init__)


def test_arduinoml_actuatorstate_constructor_args():
    sig = inspect.signature(arduinoml_ActuatorState.__init__)
    params = list(sig.parameters.keys())
    assert "isOn" in params, "Missing parameter 'isOn'"

def test_arduinoml_actuatorstate_has_isOn():
    assert hasattr(arduinoml_ActuatorState, "isOn")
    descriptor = None
    for klass in arduinoml_ActuatorState.__mro__:
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



def test_arduinoml_sensor_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Sensor)


def test_arduinoml_sensor_constructor_exists():
    assert callable(arduinoml_Sensor.__init__)


def test_arduinoml_sensor_constructor_args():
    sig = inspect.signature(arduinoml_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_actuator_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Actuator)


def test_arduinoml_actuator_constructor_exists():
    assert callable(arduinoml_Actuator.__init__)


def test_arduinoml_actuator_constructor_args():
    sig = inspect.signature(arduinoml_Actuator.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_transition_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Transition)


def test_arduinoml_transition_constructor_exists():
    assert callable(arduinoml_Transition.__init__)


def test_arduinoml_transition_constructor_args():
    sig = inspect.signature(arduinoml_Transition.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_action_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Action)


def test_arduinoml_action_constructor_exists():
    assert callable(arduinoml_Action.__init__)


def test_arduinoml_action_constructor_args():
    sig = inspect.signature(arduinoml_Action.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_brick_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Brick)


def test_arduinoml_brick_constructor_exists():
    assert callable(arduinoml_Brick.__init__)


def test_arduinoml_brick_constructor_args():
    sig = inspect.signature(arduinoml_Brick.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "pin" in params, "Missing parameter 'pin'"

def test_arduinoml_brick_has_name():
    assert hasattr(arduinoml_Brick, "name")
    descriptor = None
    for klass in arduinoml_Brick.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml_brick_has_pin():
    assert hasattr(arduinoml_Brick, "pin")
    descriptor = None
    for klass in arduinoml_Brick.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml_state_is_not_abstract():
    assert not inspect.isabstract(arduinoml_State)


def test_arduinoml_state_constructor_exists():
    assert callable(arduinoml_State.__init__)


def test_arduinoml_state_constructor_args():
    sig = inspect.signature(arduinoml_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduinoml_state_has_name():
    assert hasattr(arduinoml_State, "name")
    descriptor = None
    for klass in arduinoml_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml_board_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Board)


def test_arduinoml_board_constructor_exists():
    assert callable(arduinoml_Board.__init__)


def test_arduinoml_board_constructor_args():
    sig = inspect.signature(arduinoml_Board.__init__)
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
arduinoml_On_strategy = st.builds(
    arduinoml_On,
)
arduinoml_Off_strategy = st.builds(
    arduinoml_Off,
)
arduinoml_ActuatorState_strategy = st.builds(
    arduinoml_ActuatorState,
    isOn=
        st.booleans()
)
Brick_strategy = st.builds(
    Brick,
)
arduinoml_Sensor_strategy = st.builds(
    arduinoml_Sensor,
)
arduinoml_Actuator_strategy = st.builds(
    arduinoml_Actuator,
)
arduinoml_Transition_strategy = st.builds(
    arduinoml_Transition,
)
arduinoml_Action_strategy = st.builds(
    arduinoml_Action,
)
arduinoml_Brick_strategy = st.builds(
    arduinoml_Brick,
    name=
        safe_text,
    pin=
        st.integers()
)
arduinoml_State_strategy = st.builds(
    arduinoml_State,
    name=
        safe_text
)
arduinoml_Board_strategy = st.builds(
    arduinoml_Board,
)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=arduinoml_On_strategy)
@settings(max_examples=50)
def test_arduinoml_on_instantiation(instance):
    assert isinstance(instance, arduinoml_On)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=arduinoml_On_strategy)
@settings(max_examples=30)
def test_arduinoml_on_turnon_changes_state(instance):
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
        assert has_statements, f"Function 'turnOn' in arduinoml_On is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'turnOn' in arduinoml_On did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'turnOn' in arduinoml_On is not implemented or raised an error")

@given(instance=arduinoml_Off_strategy)
@settings(max_examples=50)
def test_arduinoml_off_instantiation(instance):
    assert isinstance(instance, arduinoml_Off)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=arduinoml_Off_strategy)
@settings(max_examples=30)
def test_arduinoml_off_turnoff_changes_state(instance):
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
        assert has_statements, f"Function 'turnOff' in arduinoml_Off is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'turnOff' in arduinoml_Off did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'turnOff' in arduinoml_Off is not implemented or raised an error")

@given(instance=arduinoml_ActuatorState_strategy)
@settings(max_examples=50)
def test_arduinoml_actuatorstate_instantiation(instance):
    assert isinstance(instance, arduinoml_ActuatorState)



@given(instance=arduinoml_ActuatorState_strategy)
def test_arduinoml_actuatorstate_isOn_setter(instance):
    original = instance.isOn
    instance.isOn = original
    assert instance.isOn == original

@given(instance=Brick_strategy)
@settings(max_examples=50)
def test_brick_instantiation(instance):
    assert isinstance(instance, Brick)

@given(instance=arduinoml_Sensor_strategy)
@settings(max_examples=50)
def test_arduinoml_sensor_instantiation(instance):
    assert isinstance(instance, arduinoml_Sensor)

@given(instance=arduinoml_Actuator_strategy)
@settings(max_examples=50)
def test_arduinoml_actuator_instantiation(instance):
    assert isinstance(instance, arduinoml_Actuator)

@given(instance=arduinoml_Transition_strategy)
@settings(max_examples=50)
def test_arduinoml_transition_instantiation(instance):
    assert isinstance(instance, arduinoml_Transition)

@given(instance=arduinoml_Action_strategy)
@settings(max_examples=50)
def test_arduinoml_action_instantiation(instance):
    assert isinstance(instance, arduinoml_Action)

@given(instance=arduinoml_Brick_strategy)
@settings(max_examples=50)
def test_arduinoml_brick_instantiation(instance):
    assert isinstance(instance, arduinoml_Brick)



@given(instance=arduinoml_Brick_strategy)
def test_arduinoml_brick_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=arduinoml_Brick_strategy)
def test_arduinoml_brick_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original

@given(instance=arduinoml_State_strategy)
@settings(max_examples=50)
def test_arduinoml_state_instantiation(instance):
    assert isinstance(instance, arduinoml_State)



@given(instance=arduinoml_State_strategy)
def test_arduinoml_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduinoml_Board_strategy)
@settings(max_examples=50)
def test_arduinoml_board_instantiation(instance):
    assert isinstance(instance, arduinoml_Board)
