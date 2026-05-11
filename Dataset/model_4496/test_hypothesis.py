import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    arduinoML::NamedElement,
    arduinoML::Transition,
    arduinoML::Action,
    Brick,
    arduinoML::Sensor,
    arduinoML::Actuator,
    NamedElement,
    arduinoML::State,
    arduinoML::App,
    arduinoML::Brick,
    Signal,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_arduinoml::transition_is_not_abstract():
    assert not inspect.isabstract(arduinoML::Transition)


def test_arduinoml::transition_constructor_exists():
    assert callable(arduinoML::Transition.__init__)


def test_arduinoml::transition_constructor_args():
    sig = inspect.signature(arduinoML::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduinoml::transition_has_value():
    assert hasattr(arduinoML::Transition, "value")
    descriptor = None
    for klass in arduinoML::Transition.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml::action_is_not_abstract():
    assert not inspect.isabstract(arduinoML::Action)


def test_arduinoml::action_constructor_exists():
    assert callable(arduinoML::Action.__init__)


def test_arduinoml::action_constructor_args():
    sig = inspect.signature(arduinoML::Action.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduinoml::action_has_value():
    assert hasattr(arduinoML::Action, "value")
    descriptor = None
    for klass in arduinoML::Action.__mro__:
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



def test_arduinoml::state_is_not_abstract():
    assert not inspect.isabstract(arduinoML::State)


def test_arduinoml::state_constructor_exists():
    assert callable(arduinoML::State.__init__)


def test_arduinoml::state_constructor_args():
    sig = inspect.signature(arduinoML::State.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::app_is_not_abstract():
    assert not inspect.isabstract(arduinoML::App)


def test_arduinoml::app_constructor_exists():
    assert callable(arduinoML::App.__init__)


def test_arduinoml::app_constructor_args():
    sig = inspect.signature(arduinoML::App.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::brick_is_not_abstract():
    assert not inspect.isabstract(arduinoML::Brick)


def test_arduinoml::brick_constructor_exists():
    assert callable(arduinoML::Brick.__init__)


def test_arduinoml::brick_constructor_args():
    sig = inspect.signature(arduinoML::Brick.__init__)
    params = list(sig.parameters.keys())
    assert "pin" in params, "Missing parameter 'pin'"

def test_arduinoml::brick_has_pin():
    assert hasattr(arduinoML::Brick, "pin")
    descriptor = None
    for klass in arduinoML::Brick.__mro__:
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
        "LOW",
        "HIGH",
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
arduinoML::NamedElement_strategy = st.builds(
    arduinoML::NamedElement,
    name=
        safe_text
)
arduinoML::Transition_strategy = st.builds(
    arduinoML::Transition,
    value=
        safe_text
)
arduinoML::Action_strategy = st.builds(
    arduinoML::Action,
    value=
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
arduinoML::State_strategy = st.builds(
    arduinoML::State,
)
arduinoML::App_strategy = st.builds(
    arduinoML::App,
)
arduinoML::Brick_strategy = st.builds(
    arduinoML::Brick,
    pin=
        st.integers()
)

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

@given(instance=arduinoML::Transition_strategy)
@settings(max_examples=50)
def test_arduinoml::transition_instantiation(instance):
    assert isinstance(instance, arduinoML::Transition)

@given(instance=arduinoML::Transition_strategy)
def test_arduinoml::transition_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=arduinoML::Transition_strategy)
def test_arduinoml::transition_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arduinoML::Action_strategy)
@settings(max_examples=50)
def test_arduinoml::action_instantiation(instance):
    assert isinstance(instance, arduinoML::Action)

@given(instance=arduinoML::Action_strategy)
def test_arduinoml::action_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=arduinoML::Action_strategy)
def test_arduinoml::action_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

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

@given(instance=arduinoML::State_strategy)
@settings(max_examples=50)
def test_arduinoml::state_instantiation(instance):
    assert isinstance(instance, arduinoML::State)

@given(instance=arduinoML::App_strategy)
@settings(max_examples=50)
def test_arduinoml::app_instantiation(instance):
    assert isinstance(instance, arduinoML::App)

@given(instance=arduinoML::Brick_strategy)
@settings(max_examples=50)
def test_arduinoml::brick_instantiation(instance):
    assert isinstance(instance, arduinoML::Brick)

@given(instance=arduinoML::Brick_strategy)
def test_arduinoml::brick_pin_type(instance):
    assert isinstance(instance.pin, int)


@given(instance=arduinoML::Brick_strategy)
def test_arduinoml::brick_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original
