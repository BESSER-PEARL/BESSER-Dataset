import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Signal,
    arduinoML_DigitalSignal,
    Actuator,
    arduinoML_LCDScreenActuator,
    Sensor,
    arduinoML_KeyboardSensor,
    arduinoML_StringSignal,
    arduinoML_App,
    arduinoML_Signal,
    arduinoML_Transition,
    arduinoML_Action,
    arduinoML_NamedElement,
    Brick,
    arduinoML_Sensor,
    arduinoML_Actuator,
    NamedElement,
    arduinoML_State,
    arduinoML_Condition,
    arduinoML_Brick,
    DigitalSignalEnum,
    Operator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_signal_is_not_abstract():
    assert not inspect.isabstract(Signal)


def test_signal_constructor_exists():
    assert callable(Signal.__init__)


def test_signal_constructor_args():
    sig = inspect.signature(Signal.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_digitalsignal_is_not_abstract():
    assert not inspect.isabstract(arduinoML_DigitalSignal)


def test_arduinoml_digitalsignal_constructor_exists():
    assert callable(arduinoML_DigitalSignal.__init__)


def test_arduinoml_digitalsignal_constructor_args():
    sig = inspect.signature(arduinoML_DigitalSignal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduinoml_digitalsignal_has_value():
    assert hasattr(arduinoML_DigitalSignal, "value")
    descriptor = None
    for klass in arduinoML_DigitalSignal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_actuator_is_not_abstract():
    assert not inspect.isabstract(Actuator)


def test_actuator_constructor_exists():
    assert callable(Actuator.__init__)


def test_actuator_constructor_args():
    sig = inspect.signature(Actuator.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_lcdscreenactuator_is_not_abstract():
    assert not inspect.isabstract(arduinoML_LCDScreenActuator)


def test_arduinoml_lcdscreenactuator_constructor_exists():
    assert callable(arduinoML_LCDScreenActuator.__init__)


def test_arduinoml_lcdscreenactuator_constructor_args():
    sig = inspect.signature(arduinoML_LCDScreenActuator.__init__)
    params = list(sig.parameters.keys())



def test_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_keyboardsensor_is_not_abstract():
    assert not inspect.isabstract(arduinoML_KeyboardSensor)


def test_arduinoml_keyboardsensor_constructor_exists():
    assert callable(arduinoML_KeyboardSensor.__init__)


def test_arduinoml_keyboardsensor_constructor_args():
    sig = inspect.signature(arduinoML_KeyboardSensor.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_stringsignal_is_not_abstract():
    assert not inspect.isabstract(arduinoML_StringSignal)


def test_arduinoml_stringsignal_constructor_exists():
    assert callable(arduinoML_StringSignal.__init__)


def test_arduinoml_stringsignal_constructor_args():
    sig = inspect.signature(arduinoML_StringSignal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduinoml_stringsignal_has_value():
    assert hasattr(arduinoML_StringSignal, "value")
    descriptor = None
    for klass in arduinoML_StringSignal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml_app_is_not_abstract():
    assert not inspect.isabstract(arduinoML_App)


def test_arduinoml_app_constructor_exists():
    assert callable(arduinoML_App.__init__)


def test_arduinoml_app_constructor_args():
    sig = inspect.signature(arduinoML_App.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduinoml_app_has_name():
    assert hasattr(arduinoML_App, "name")
    descriptor = None
    for klass in arduinoML_App.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml_signal_is_not_abstract():
    assert not inspect.isabstract(arduinoML_Signal)


def test_arduinoml_signal_constructor_exists():
    assert callable(arduinoML_Signal.__init__)


def test_arduinoml_signal_constructor_args():
    sig = inspect.signature(arduinoML_Signal.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_transition_is_not_abstract():
    assert not inspect.isabstract(arduinoML_Transition)


def test_arduinoml_transition_constructor_exists():
    assert callable(arduinoML_Transition.__init__)


def test_arduinoml_transition_constructor_args():
    sig = inspect.signature(arduinoML_Transition.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_action_is_not_abstract():
    assert not inspect.isabstract(arduinoML_Action)


def test_arduinoml_action_constructor_exists():
    assert callable(arduinoML_Action.__init__)


def test_arduinoml_action_constructor_args():
    sig = inspect.signature(arduinoML_Action.__init__)
    params = list(sig.parameters.keys())



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



def test_arduinoml_condition_is_not_abstract():
    assert not inspect.isabstract(arduinoML_Condition)


def test_arduinoml_condition_constructor_exists():
    assert callable(arduinoML_Condition.__init__)


def test_arduinoml_condition_constructor_args():
    sig = inspect.signature(arduinoML_Condition.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_arduinoml_condition_has_operator():
    assert hasattr(arduinoML_Condition, "operator")
    descriptor = None
    for klass in arduinoML_Condition.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml_brick_is_not_abstract():
    assert not inspect.isabstract(arduinoML_Brick)


def test_arduinoml_brick_constructor_exists():
    assert callable(arduinoML_Brick.__init__)


def test_arduinoml_brick_constructor_args():
    sig = inspect.signature(arduinoML_Brick.__init__)
    params = list(sig.parameters.keys())
    assert "pins" in params, "Missing parameter 'pins'"

def test_arduinoml_brick_has_pins():
    assert hasattr(arduinoML_Brick, "pins")
    descriptor = None
    for klass in arduinoML_Brick.__mro__:
        if "pins" in klass.__dict__:
            descriptor = klass.__dict__["pins"]
            break
    assert isinstance(descriptor, property)

def test_digitalsignalenum_exists():
    # Check that the Enumeration exists
    assert DigitalSignalEnum is not None

def test_digitalsignalenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DigitalSignalEnum]
    expected_literals = [
        "LOW",
        "HIGH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DigitalSignalEnum"

def test_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "AND",
        "OR",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"


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
Signal_strategy = st.builds(
    Signal,
)
arduinoML_DigitalSignal_strategy = st.builds(
    arduinoML_DigitalSignal,
    value=
        safe_text
)
Actuator_strategy = st.builds(
    Actuator,
)
arduinoML_LCDScreenActuator_strategy = st.builds(
    arduinoML_LCDScreenActuator,
)
Sensor_strategy = st.builds(
    Sensor,
)
arduinoML_KeyboardSensor_strategy = st.builds(
    arduinoML_KeyboardSensor,
)
arduinoML_StringSignal_strategy = st.builds(
    arduinoML_StringSignal,
    value=
        safe_text
)
arduinoML_App_strategy = st.builds(
    arduinoML_App,
    name=
        safe_text
)
arduinoML_Signal_strategy = st.builds(
    arduinoML_Signal,
)
arduinoML_Transition_strategy = st.builds(
    arduinoML_Transition,
)
arduinoML_Action_strategy = st.builds(
    arduinoML_Action,
)
arduinoML_NamedElement_strategy = st.builds(
    arduinoML_NamedElement,
    name=
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
arduinoML_Condition_strategy = st.builds(
    arduinoML_Condition,
    operator=
        safe_text
)
arduinoML_Brick_strategy = st.builds(
    arduinoML_Brick,
    pins=
        st.integers()
)

@given(instance=Signal_strategy)
@settings(max_examples=50)
def test_signal_instantiation(instance):
    assert isinstance(instance, Signal)

@given(instance=arduinoML_DigitalSignal_strategy)
@settings(max_examples=50)
def test_arduinoml_digitalsignal_instantiation(instance):
    assert isinstance(instance, arduinoML_DigitalSignal)



@given(instance=arduinoML_DigitalSignal_strategy)
def test_arduinoml_digitalsignal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Actuator_strategy)
@settings(max_examples=50)
def test_actuator_instantiation(instance):
    assert isinstance(instance, Actuator)

@given(instance=arduinoML_LCDScreenActuator_strategy)
@settings(max_examples=50)
def test_arduinoml_lcdscreenactuator_instantiation(instance):
    assert isinstance(instance, arduinoML_LCDScreenActuator)

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)

@given(instance=arduinoML_KeyboardSensor_strategy)
@settings(max_examples=50)
def test_arduinoml_keyboardsensor_instantiation(instance):
    assert isinstance(instance, arduinoML_KeyboardSensor)

@given(instance=arduinoML_StringSignal_strategy)
@settings(max_examples=50)
def test_arduinoml_stringsignal_instantiation(instance):
    assert isinstance(instance, arduinoML_StringSignal)



@given(instance=arduinoML_StringSignal_strategy)
def test_arduinoml_stringsignal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arduinoML_App_strategy)
@settings(max_examples=50)
def test_arduinoml_app_instantiation(instance):
    assert isinstance(instance, arduinoML_App)



@given(instance=arduinoML_App_strategy)
def test_arduinoml_app_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduinoML_Signal_strategy)
@settings(max_examples=50)
def test_arduinoml_signal_instantiation(instance):
    assert isinstance(instance, arduinoML_Signal)

@given(instance=arduinoML_Transition_strategy)
@settings(max_examples=50)
def test_arduinoml_transition_instantiation(instance):
    assert isinstance(instance, arduinoML_Transition)

@given(instance=arduinoML_Action_strategy)
@settings(max_examples=50)
def test_arduinoml_action_instantiation(instance):
    assert isinstance(instance, arduinoML_Action)

@given(instance=arduinoML_NamedElement_strategy)
@settings(max_examples=50)
def test_arduinoml_namedelement_instantiation(instance):
    assert isinstance(instance, arduinoML_NamedElement)



@given(instance=arduinoML_NamedElement_strategy)
def test_arduinoml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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

@given(instance=arduinoML_Condition_strategy)
@settings(max_examples=50)
def test_arduinoml_condition_instantiation(instance):
    assert isinstance(instance, arduinoML_Condition)



@given(instance=arduinoML_Condition_strategy)
def test_arduinoml_condition_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=arduinoML_Brick_strategy)
@settings(max_examples=50)
def test_arduinoml_brick_instantiation(instance):
    assert isinstance(instance, arduinoML_Brick)



@given(instance=arduinoML_Brick_strategy)
def test_arduinoml_brick_pins_setter(instance):
    original = instance.pins
    instance.pins = original
    assert instance.pins == original
