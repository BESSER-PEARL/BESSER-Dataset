import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Signal,
    arduinoML::DigitalSignal,
    Actuator,
    arduinoML::LCDScreenActuator,
    Sensor,
    arduinoML::KeyboardSensor,
    arduinoML::StringSignal,
    arduinoML::App,
    arduinoML::Signal,
    arduinoML::Transition,
    arduinoML::Action,
    arduinoML::NamedElement,
    Brick,
    arduinoML::Sensor,
    arduinoML::Actuator,
    NamedElement,
    arduinoML::Condition,
    arduinoML::State,
    arduinoML::Brick,
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



def test_arduinoml::digitalsignal_is_not_abstract():
    assert not inspect.isabstract(arduinoML::DigitalSignal)


def test_arduinoml::digitalsignal_constructor_exists():
    assert callable(arduinoML::DigitalSignal.__init__)


def test_arduinoml::digitalsignal_constructor_args():
    sig = inspect.signature(arduinoML::DigitalSignal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduinoml::digitalsignal_has_value():
    assert hasattr(arduinoML::DigitalSignal, "value")
    descriptor = None
    for klass in arduinoML::DigitalSignal.__mro__:
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



def test_arduinoml::lcdscreenactuator_is_not_abstract():
    assert not inspect.isabstract(arduinoML::LCDScreenActuator)


def test_arduinoml::lcdscreenactuator_constructor_exists():
    assert callable(arduinoML::LCDScreenActuator.__init__)


def test_arduinoml::lcdscreenactuator_constructor_args():
    sig = inspect.signature(arduinoML::LCDScreenActuator.__init__)
    params = list(sig.parameters.keys())



def test_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::keyboardsensor_is_not_abstract():
    assert not inspect.isabstract(arduinoML::KeyboardSensor)


def test_arduinoml::keyboardsensor_constructor_exists():
    assert callable(arduinoML::KeyboardSensor.__init__)


def test_arduinoml::keyboardsensor_constructor_args():
    sig = inspect.signature(arduinoML::KeyboardSensor.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::stringsignal_is_not_abstract():
    assert not inspect.isabstract(arduinoML::StringSignal)


def test_arduinoml::stringsignal_constructor_exists():
    assert callable(arduinoML::StringSignal.__init__)


def test_arduinoml::stringsignal_constructor_args():
    sig = inspect.signature(arduinoML::StringSignal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduinoml::stringsignal_has_value():
    assert hasattr(arduinoML::StringSignal, "value")
    descriptor = None
    for klass in arduinoML::StringSignal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml::app_is_not_abstract():
    assert not inspect.isabstract(arduinoML::App)


def test_arduinoml::app_constructor_exists():
    assert callable(arduinoML::App.__init__)


def test_arduinoml::app_constructor_args():
    sig = inspect.signature(arduinoML::App.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduinoml::app_has_name():
    assert hasattr(arduinoML::App, "name")
    descriptor = None
    for klass in arduinoML::App.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml::signal_is_not_abstract():
    assert not inspect.isabstract(arduinoML::Signal)


def test_arduinoml::signal_constructor_exists():
    assert callable(arduinoML::Signal.__init__)


def test_arduinoml::signal_constructor_args():
    sig = inspect.signature(arduinoML::Signal.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::transition_is_not_abstract():
    assert not inspect.isabstract(arduinoML::Transition)


def test_arduinoml::transition_constructor_exists():
    assert callable(arduinoML::Transition.__init__)


def test_arduinoml::transition_constructor_args():
    sig = inspect.signature(arduinoML::Transition.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::action_is_not_abstract():
    assert not inspect.isabstract(arduinoML::Action)


def test_arduinoml::action_constructor_exists():
    assert callable(arduinoML::Action.__init__)


def test_arduinoml::action_constructor_args():
    sig = inspect.signature(arduinoML::Action.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::namedelement_is_not_abstract():
    assert not inspect.isabstract(arduinoML::NamedElement)


def test_arduinoml::namedelement_constructor_exists():
    assert callable(arduinoML::NamedElement.__init__)


def test_arduinoml::namedelement_constructor_args():
    sig = inspect.signature(arduinoML::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduinoml::namedelement_has_name():
    assert hasattr(arduinoML::NamedElement, "name")
    descriptor = None
    for klass in arduinoML::NamedElement.__mro__:
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



def test_arduinoml::sensor_is_not_abstract():
    assert not inspect.isabstract(arduinoML::Sensor)


def test_arduinoml::sensor_constructor_exists():
    assert callable(arduinoML::Sensor.__init__)


def test_arduinoml::sensor_constructor_args():
    sig = inspect.signature(arduinoML::Sensor.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::actuator_is_not_abstract():
    assert not inspect.isabstract(arduinoML::Actuator)


def test_arduinoml::actuator_constructor_exists():
    assert callable(arduinoML::Actuator.__init__)


def test_arduinoml::actuator_constructor_args():
    sig = inspect.signature(arduinoML::Actuator.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::condition_is_not_abstract():
    assert not inspect.isabstract(arduinoML::Condition)


def test_arduinoml::condition_constructor_exists():
    assert callable(arduinoML::Condition.__init__)


def test_arduinoml::condition_constructor_args():
    sig = inspect.signature(arduinoML::Condition.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_arduinoml::condition_has_operator():
    assert hasattr(arduinoML::Condition, "operator")
    descriptor = None
    for klass in arduinoML::Condition.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml::state_is_not_abstract():
    assert not inspect.isabstract(arduinoML::State)


def test_arduinoml::state_constructor_exists():
    assert callable(arduinoML::State.__init__)


def test_arduinoml::state_constructor_args():
    sig = inspect.signature(arduinoML::State.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::brick_is_not_abstract():
    assert not inspect.isabstract(arduinoML::Brick)


def test_arduinoml::brick_constructor_exists():
    assert callable(arduinoML::Brick.__init__)


def test_arduinoml::brick_constructor_args():
    sig = inspect.signature(arduinoML::Brick.__init__)
    params = list(sig.parameters.keys())
    assert "pins" in params, "Missing parameter 'pins'"

def test_arduinoml::brick_has_pins():
    assert hasattr(arduinoML::Brick, "pins")
    descriptor = None
    for klass in arduinoML::Brick.__mro__:
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
        "NONE",
        "OR",
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
arduinoML::DigitalSignal_strategy = st.builds(
    arduinoML::DigitalSignal,
    value=
        safe_text
)
Actuator_strategy = st.builds(
    Actuator,
)
arduinoML::LCDScreenActuator_strategy = st.builds(
    arduinoML::LCDScreenActuator,
)
Sensor_strategy = st.builds(
    Sensor,
)
arduinoML::KeyboardSensor_strategy = st.builds(
    arduinoML::KeyboardSensor,
)
arduinoML::StringSignal_strategy = st.builds(
    arduinoML::StringSignal,
    value=
        safe_text
)
arduinoML::App_strategy = st.builds(
    arduinoML::App,
    name=
        safe_text
)
arduinoML::Signal_strategy = st.builds(
    arduinoML::Signal,
)
arduinoML::Transition_strategy = st.builds(
    arduinoML::Transition,
)
arduinoML::Action_strategy = st.builds(
    arduinoML::Action,
)
arduinoML::NamedElement_strategy = st.builds(
    arduinoML::NamedElement,
    name=
        safe_text
)
Brick_strategy = st.builds(
    Brick,
)
arduinoML::Sensor_strategy = st.builds(
    arduinoML::Sensor,
)
arduinoML::Actuator_strategy = st.builds(
    arduinoML::Actuator,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
arduinoML::Condition_strategy = st.builds(
    arduinoML::Condition,
    operator=
        safe_text
)
arduinoML::State_strategy = st.builds(
    arduinoML::State,
)
arduinoML::Brick_strategy = st.builds(
    arduinoML::Brick,
    pins=
        st.integers()
)

@given(instance=Signal_strategy)
@settings(max_examples=50)
def test_signal_instantiation(instance):
    assert isinstance(instance, Signal)

@given(instance=arduinoML::DigitalSignal_strategy)
@settings(max_examples=50)
def test_arduinoml::digitalsignal_instantiation(instance):
    assert isinstance(instance, arduinoML::DigitalSignal)

@given(instance=arduinoML::DigitalSignal_strategy)
def test_arduinoml::digitalsignal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=arduinoML::DigitalSignal_strategy)
def test_arduinoml::digitalsignal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Actuator_strategy)
@settings(max_examples=50)
def test_actuator_instantiation(instance):
    assert isinstance(instance, Actuator)

@given(instance=arduinoML::LCDScreenActuator_strategy)
@settings(max_examples=50)
def test_arduinoml::lcdscreenactuator_instantiation(instance):
    assert isinstance(instance, arduinoML::LCDScreenActuator)

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)

@given(instance=arduinoML::KeyboardSensor_strategy)
@settings(max_examples=50)
def test_arduinoml::keyboardsensor_instantiation(instance):
    assert isinstance(instance, arduinoML::KeyboardSensor)

@given(instance=arduinoML::StringSignal_strategy)
@settings(max_examples=50)
def test_arduinoml::stringsignal_instantiation(instance):
    assert isinstance(instance, arduinoML::StringSignal)

@given(instance=arduinoML::StringSignal_strategy)
def test_arduinoml::stringsignal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=arduinoML::StringSignal_strategy)
def test_arduinoml::stringsignal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arduinoML::App_strategy)
@settings(max_examples=50)
def test_arduinoml::app_instantiation(instance):
    assert isinstance(instance, arduinoML::App)

@given(instance=arduinoML::App_strategy)
def test_arduinoml::app_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arduinoML::App_strategy)
def test_arduinoml::app_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduinoML::Signal_strategy)
@settings(max_examples=50)
def test_arduinoml::signal_instantiation(instance):
    assert isinstance(instance, arduinoML::Signal)

@given(instance=arduinoML::Transition_strategy)
@settings(max_examples=50)
def test_arduinoml::transition_instantiation(instance):
    assert isinstance(instance, arduinoML::Transition)

@given(instance=arduinoML::Action_strategy)
@settings(max_examples=50)
def test_arduinoml::action_instantiation(instance):
    assert isinstance(instance, arduinoML::Action)

@given(instance=arduinoML::NamedElement_strategy)
@settings(max_examples=50)
def test_arduinoml::namedelement_instantiation(instance):
    assert isinstance(instance, arduinoML::NamedElement)

@given(instance=arduinoML::NamedElement_strategy)
def test_arduinoml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arduinoML::NamedElement_strategy)
def test_arduinoml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Brick_strategy)
@settings(max_examples=50)
def test_brick_instantiation(instance):
    assert isinstance(instance, Brick)

@given(instance=arduinoML::Sensor_strategy)
@settings(max_examples=50)
def test_arduinoml::sensor_instantiation(instance):
    assert isinstance(instance, arduinoML::Sensor)

@given(instance=arduinoML::Actuator_strategy)
@settings(max_examples=50)
def test_arduinoml::actuator_instantiation(instance):
    assert isinstance(instance, arduinoML::Actuator)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=arduinoML::Condition_strategy)
@settings(max_examples=50)
def test_arduinoml::condition_instantiation(instance):
    assert isinstance(instance, arduinoML::Condition)

@given(instance=arduinoML::Condition_strategy)
def test_arduinoml::condition_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=arduinoML::Condition_strategy)
def test_arduinoml::condition_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=arduinoML::State_strategy)
@settings(max_examples=50)
def test_arduinoml::state_instantiation(instance):
    assert isinstance(instance, arduinoML::State)

@given(instance=arduinoML::Brick_strategy)
@settings(max_examples=50)
def test_arduinoml::brick_instantiation(instance):
    assert isinstance(instance, arduinoML::Brick)

@given(instance=arduinoML::Brick_strategy)
def test_arduinoml::brick_pins_type(instance):
    assert isinstance(instance.pins, int)


@given(instance=arduinoML::Brick_strategy)
def test_arduinoml::brick_pins_setter(instance):
    original = instance.pins
    instance.pins = original
    assert instance.pins == original
