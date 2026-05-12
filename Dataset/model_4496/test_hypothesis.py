import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    arduinoML_NamedElement,
    arduinoML_Transition,
    arduinoML_Action,
    Brick,
    arduinoML_Sensor,
    arduinoML_Actuator,
    NamedElement,
    arduinoML_State,
    arduinoML_App,
    arduinoML_Brick,
    Signal,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_arduinoml_namedelement_is_not_abstract():
    assert not inspect.isabstract(arduinoML_NamedElement)


def test_arduinoml_namedelement_constructor_exists():
    assert callable(arduinoML_NamedElement.__init__)


def test_arduinoml_namedelement_constructor_args():
    sig = inspect.signature(arduinoML_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduinoml_namedelement_has_name():
    assert hasattr(arduinoML_NamedElement, "name")
    descriptor = None
    for klass in arduinoML_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml_transition_is_not_abstract():
    assert not inspect.isabstract(arduinoML_Transition)


def test_arduinoml_transition_constructor_exists():
    assert callable(arduinoML_Transition.__init__)


def test_arduinoml_transition_constructor_args():
    sig = inspect.signature(arduinoML_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduinoml_transition_has_value():
    assert hasattr(arduinoML_Transition, "value")
    descriptor = None
    for klass in arduinoML_Transition.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml_action_is_not_abstract():
    assert not inspect.isabstract(arduinoML_Action)


def test_arduinoml_action_constructor_exists():
    assert callable(arduinoML_Action.__init__)


def test_arduinoml_action_constructor_args():
    sig = inspect.signature(arduinoML_Action.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduinoml_action_has_value():
    assert hasattr(arduinoML_Action, "value")
    descriptor = None
    for klass in arduinoML_Action.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
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
    assert not inspect.isabstract(arduinoML_Sensor)


def test_arduinoml_sensor_constructor_exists():
    assert callable(arduinoML_Sensor.__init__)


def test_arduinoml_sensor_constructor_args():
    sig = inspect.signature(arduinoML_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_actuator_is_not_abstract():
    assert not inspect.isabstract(arduinoML_Actuator)


def test_arduinoml_actuator_constructor_exists():
    assert callable(arduinoML_Actuator.__init__)


def test_arduinoml_actuator_constructor_args():
    sig = inspect.signature(arduinoML_Actuator.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_state_is_not_abstract():
    assert not inspect.isabstract(arduinoML_State)


def test_arduinoml_state_constructor_exists():
    assert callable(arduinoML_State.__init__)


def test_arduinoml_state_constructor_args():
    sig = inspect.signature(arduinoML_State.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_app_is_not_abstract():
    assert not inspect.isabstract(arduinoML_App)


def test_arduinoml_app_constructor_exists():
    assert callable(arduinoML_App.__init__)


def test_arduinoml_app_constructor_args():
    sig = inspect.signature(arduinoML_App.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_brick_is_not_abstract():
    assert not inspect.isabstract(arduinoML_Brick)


def test_arduinoml_brick_constructor_exists():
    assert callable(arduinoML_Brick.__init__)


def test_arduinoml_brick_constructor_args():
    sig = inspect.signature(arduinoML_Brick.__init__)
    params = list(sig.parameters.keys())
    assert "pin" in params, "Missing parameter 'pin'"

def test_arduinoml_brick_has_pin():
    assert hasattr(arduinoML_Brick, "pin")
    descriptor = None
    for klass in arduinoML_Brick.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)

def test_signal_exists():
    # Check that the Enumeration exists
    assert Signal is not None

def test_signal_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Signal]
    expected_literals = [
        "HIGH",
        "LOW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Signal"


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
arduinoML_NamedElement_strategy = st.builds(
    arduinoML_NamedElement,
    name=
        safe_text
)
arduinoML_Transition_strategy = st.builds(
    arduinoML_Transition,
    value=
        safe_text
)
arduinoML_Action_strategy = st.builds(
    arduinoML_Action,
    value=
        safe_text
)
Brick_strategy = st.builds(
    Brick,
)
arduinoML_Sensor_strategy = st.builds(
    arduinoML_Sensor,
)
arduinoML_Actuator_strategy = st.builds(
    arduinoML_Actuator,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
arduinoML_State_strategy = st.builds(
    arduinoML_State,
)
arduinoML_App_strategy = st.builds(
    arduinoML_App,
)
arduinoML_Brick_strategy = st.builds(
    arduinoML_Brick,
    pin=
        st.integers()
)

@given(instance=arduinoML_NamedElement_strategy)
@settings(max_examples=50)
def test_arduinoml_namedelement_instantiation(instance):
    assert isinstance(instance, arduinoML_NamedElement)



@given(instance=arduinoML_NamedElement_strategy)
def test_arduinoml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduinoML_Transition_strategy)
@settings(max_examples=50)
def test_arduinoml_transition_instantiation(instance):
    assert isinstance(instance, arduinoML_Transition)



@given(instance=arduinoML_Transition_strategy)
def test_arduinoml_transition_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arduinoML_Action_strategy)
@settings(max_examples=50)
def test_arduinoml_action_instantiation(instance):
    assert isinstance(instance, arduinoML_Action)



@given(instance=arduinoML_Action_strategy)
def test_arduinoml_action_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Brick_strategy)
@settings(max_examples=50)
def test_brick_instantiation(instance):
    assert isinstance(instance, Brick)

@given(instance=arduinoML_Sensor_strategy)
@settings(max_examples=50)
def test_arduinoml_sensor_instantiation(instance):
    assert isinstance(instance, arduinoML_Sensor)

@given(instance=arduinoML_Actuator_strategy)
@settings(max_examples=50)
def test_arduinoml_actuator_instantiation(instance):
    assert isinstance(instance, arduinoML_Actuator)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=arduinoML_State_strategy)
@settings(max_examples=50)
def test_arduinoml_state_instantiation(instance):
    assert isinstance(instance, arduinoML_State)

@given(instance=arduinoML_App_strategy)
@settings(max_examples=50)
def test_arduinoml_app_instantiation(instance):
    assert isinstance(instance, arduinoML_App)

@given(instance=arduinoML_Brick_strategy)
@settings(max_examples=50)
def test_arduinoml_brick_instantiation(instance):
    assert isinstance(instance, arduinoML_Brick)



@given(instance=arduinoML_Brick_strategy)
def test_arduinoml_brick_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original
