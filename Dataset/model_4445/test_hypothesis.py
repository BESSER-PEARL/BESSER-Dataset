import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Transition,
    arduinoML::TransitionMode,
    arduinoML::NamedElement,
    arduinoML::Transition,
    arduinoML::TransitionState,
    arduinoML::Action,
    Brick,
    arduinoML::Analog,
    arduinoML::Actuator,
    NamedElement,
    arduinoML::State,
    arduinoML::Brick,
    arduinoML::Mode,
    arduinoML::App,
    arduinoML::Digital,
    Signal,
    Time_unit,
    Compare,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::transitionmode_is_not_abstract():
    assert not inspect.isabstract(arduinoML::TransitionMode)


def test_arduinoml::transitionmode_constructor_exists():
    assert callable(arduinoML::TransitionMode.__init__)


def test_arduinoml::transitionmode_constructor_args():
    sig = inspect.signature(arduinoML::TransitionMode.__init__)
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



def test_arduinoml::transition_is_not_abstract():
    assert not inspect.isabstract(arduinoML::Transition)


def test_arduinoml::transition_constructor_exists():
    assert callable(arduinoML::Transition.__init__)


def test_arduinoml::transition_constructor_args():
    sig = inspect.signature(arduinoML::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "comp" in params, "Missing parameter 'comp'"
    assert "a_values" in params, "Missing parameter 'a_values'"
    assert "d_values" in params, "Missing parameter 'd_values'"
    assert "time" in params, "Missing parameter 'time'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_arduinoml::transition_has_comp():
    assert hasattr(arduinoML::Transition, "comp")
    descriptor = None
    for klass in arduinoML::Transition.__mro__:
        if "comp" in klass.__dict__:
            descriptor = klass.__dict__["comp"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml::transition_has_a_values():
    assert hasattr(arduinoML::Transition, "a_values")
    descriptor = None
    for klass in arduinoML::Transition.__mro__:
        if "a_values" in klass.__dict__:
            descriptor = klass.__dict__["a_values"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml::transition_has_d_values():
    assert hasattr(arduinoML::Transition, "d_values")
    descriptor = None
    for klass in arduinoML::Transition.__mro__:
        if "d_values" in klass.__dict__:
            descriptor = klass.__dict__["d_values"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml::transition_has_time():
    assert hasattr(arduinoML::Transition, "time")
    descriptor = None
    for klass in arduinoML::Transition.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml::transition_has_unit():
    assert hasattr(arduinoML::Transition, "unit")
    descriptor = None
    for klass in arduinoML::Transition.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml::transitionstate_is_not_abstract():
    assert not inspect.isabstract(arduinoML::TransitionState)


def test_arduinoml::transitionstate_constructor_exists():
    assert callable(arduinoML::TransitionState.__init__)


def test_arduinoml::transitionstate_constructor_args():
    sig = inspect.signature(arduinoML::TransitionState.__init__)
    params = list(sig.parameters.keys())



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



def test_arduinoml::analog_is_not_abstract():
    assert not inspect.isabstract(arduinoML::Analog)


def test_arduinoml::analog_constructor_exists():
    assert callable(arduinoML::Analog.__init__)


def test_arduinoml::analog_constructor_args():
    sig = inspect.signature(arduinoML::Analog.__init__)
    params = list(sig.parameters.keys())
    assert "debug" in params, "Missing parameter 'debug'"

def test_arduinoml::analog_has_debug():
    assert hasattr(arduinoML::Analog, "debug")
    descriptor = None
    for klass in arduinoML::Analog.__mro__:
        if "debug" in klass.__dict__:
            descriptor = klass.__dict__["debug"]
            break
    assert isinstance(descriptor, property)



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



def test_arduinoml::mode_is_not_abstract():
    assert not inspect.isabstract(arduinoML::Mode)


def test_arduinoml::mode_constructor_exists():
    assert callable(arduinoML::Mode.__init__)


def test_arduinoml::mode_constructor_args():
    sig = inspect.signature(arduinoML::Mode.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::app_is_not_abstract():
    assert not inspect.isabstract(arduinoML::App)


def test_arduinoml::app_constructor_exists():
    assert callable(arduinoML::App.__init__)


def test_arduinoml::app_constructor_args():
    sig = inspect.signature(arduinoML::App.__init__)
    params = list(sig.parameters.keys())
    assert "monitoring" in params, "Missing parameter 'monitoring'"

def test_arduinoml::app_has_monitoring():
    assert hasattr(arduinoML::App, "monitoring")
    descriptor = None
    for klass in arduinoML::App.__mro__:
        if "monitoring" in klass.__dict__:
            descriptor = klass.__dict__["monitoring"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml::digital_is_not_abstract():
    assert not inspect.isabstract(arduinoML::Digital)


def test_arduinoml::digital_constructor_exists():
    assert callable(arduinoML::Digital.__init__)


def test_arduinoml::digital_constructor_args():
    sig = inspect.signature(arduinoML::Digital.__init__)
    params = list(sig.parameters.keys())

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

def test_time_unit_exists():
    # Check that the Enumeration exists
    assert Time_unit is not None

def test_time_unit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Time_unit]
    expected_literals = [
        "s",
        "ms",
        "min",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Time_unit"

def test_compare_exists():
    # Check that the Enumeration exists
    assert Compare is not None

def test_compare_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Compare]
    expected_literals = [
        "sup",
        "equal",
        "inf",
        "esup",
        "einf",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Compare"


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
Transition_strategy = st.builds(
    Transition,
)
arduinoML::TransitionMode_strategy = st.builds(
    arduinoML::TransitionMode,
)
arduinoML::NamedElement_strategy = st.builds(
    arduinoML::NamedElement,
    name=
        safe_text
)
arduinoML::Transition_strategy = st.builds(
    arduinoML::Transition,
    comp=
        safe_text,
    a_values=
        st.integers(),
    d_values=
        safe_text,
    time=
        st.integers(),
    unit=
        safe_text
)
arduinoML::TransitionState_strategy = st.builds(
    arduinoML::TransitionState,
)
arduinoML::Action_strategy = st.builds(
    arduinoML::Action,
    value=
        safe_text
)
Brick_strategy = st.builds(
    Brick,
)
arduinoML::Analog_strategy = st.builds(
    arduinoML::Analog,
    debug=
        st.booleans()
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
arduinoML::Brick_strategy = st.builds(
    arduinoML::Brick,
    pin=
        st.integers()
)
arduinoML::Mode_strategy = st.builds(
    arduinoML::Mode,
)
arduinoML::App_strategy = st.builds(
    arduinoML::App,
    monitoring=
        st.booleans()
)
arduinoML::Digital_strategy = st.builds(
    arduinoML::Digital,
)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=arduinoML::TransitionMode_strategy)
@settings(max_examples=50)
def test_arduinoml::transitionmode_instantiation(instance):
    assert isinstance(instance, arduinoML::TransitionMode)

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
def test_arduinoml::transition_comp_type(instance):
    assert isinstance(instance.comp, str)


@given(instance=arduinoML::Transition_strategy)
def test_arduinoml::transition_comp_setter(instance):
    original = instance.comp
    instance.comp = original
    assert instance.comp == original

@given(instance=arduinoML::Transition_strategy)
def test_arduinoml::transition_a_values_type(instance):
    assert isinstance(instance.a_values, int)


@given(instance=arduinoML::Transition_strategy)
def test_arduinoml::transition_a_values_setter(instance):
    original = instance.a_values
    instance.a_values = original
    assert instance.a_values == original

@given(instance=arduinoML::Transition_strategy)
def test_arduinoml::transition_d_values_type(instance):
    assert isinstance(instance.d_values, str)


@given(instance=arduinoML::Transition_strategy)
def test_arduinoml::transition_d_values_setter(instance):
    original = instance.d_values
    instance.d_values = original
    assert instance.d_values == original

@given(instance=arduinoML::Transition_strategy)
def test_arduinoml::transition_time_type(instance):
    assert isinstance(instance.time, int)


@given(instance=arduinoML::Transition_strategy)
def test_arduinoml::transition_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=arduinoML::Transition_strategy)
def test_arduinoml::transition_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=arduinoML::Transition_strategy)
def test_arduinoml::transition_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=arduinoML::TransitionState_strategy)
@settings(max_examples=50)
def test_arduinoml::transitionstate_instantiation(instance):
    assert isinstance(instance, arduinoML::TransitionState)

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

@given(instance=arduinoML::Analog_strategy)
@settings(max_examples=50)
def test_arduinoml::analog_instantiation(instance):
    assert isinstance(instance, arduinoML::Analog)

@given(instance=arduinoML::Analog_strategy)
def test_arduinoml::analog_debug_type(instance):
    assert isinstance(instance.debug, bool)


@given(instance=arduinoML::Analog_strategy)
def test_arduinoml::analog_debug_setter(instance):
    original = instance.debug
    instance.debug = original
    assert instance.debug == original

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

@given(instance=arduinoML::Mode_strategy)
@settings(max_examples=50)
def test_arduinoml::mode_instantiation(instance):
    assert isinstance(instance, arduinoML::Mode)

@given(instance=arduinoML::App_strategy)
@settings(max_examples=50)
def test_arduinoml::app_instantiation(instance):
    assert isinstance(instance, arduinoML::App)

@given(instance=arduinoML::App_strategy)
def test_arduinoml::app_monitoring_type(instance):
    assert isinstance(instance.monitoring, bool)


@given(instance=arduinoML::App_strategy)
def test_arduinoml::app_monitoring_setter(instance):
    original = instance.monitoring
    instance.monitoring = original
    assert instance.monitoring == original

@given(instance=arduinoML::Digital_strategy)
@settings(max_examples=50)
def test_arduinoml::digital_instantiation(instance):
    assert isinstance(instance, arduinoML::Digital)
