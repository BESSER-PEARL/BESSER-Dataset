import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Transition,
    arduinoML_TransitionMode,
    arduinoML_NamedElement,
    arduinoML_Transition,
    arduinoML_TransitionState,
    arduinoML_Action,
    Brick,
    arduinoML_Analog,
    arduinoML_Actuator,
    NamedElement,
    arduinoML_State,
    arduinoML_Brick,
    arduinoML_Mode,
    arduinoML_App,
    arduinoML_Digital,
    Time_unit,
    Signal,
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



def test_arduinoml_transitionmode_is_not_abstract():
    assert not inspect.isabstract(arduinoML_TransitionMode)


def test_arduinoml_transitionmode_constructor_exists():
    assert callable(arduinoML_TransitionMode.__init__)


def test_arduinoml_transitionmode_constructor_args():
    sig = inspect.signature(arduinoML_TransitionMode.__init__)
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



def test_arduinoml_transition_is_not_abstract():
    assert not inspect.isabstract(arduinoML_Transition)


def test_arduinoml_transition_constructor_exists():
    assert callable(arduinoML_Transition.__init__)


def test_arduinoml_transition_constructor_args():
    sig = inspect.signature(arduinoML_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "comp" in params, "Missing parameter 'comp'"
    assert "d_values" in params, "Missing parameter 'd_values'"
    assert "time" in params, "Missing parameter 'time'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "a_values" in params, "Missing parameter 'a_values'"

def test_arduinoml_transition_has_comp():
    assert hasattr(arduinoML_Transition, "comp")
    descriptor = None
    for klass in arduinoML_Transition.__mro__:
        if "comp" in klass.__dict__:
            descriptor = klass.__dict__["comp"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml_transition_has_d_values():
    assert hasattr(arduinoML_Transition, "d_values")
    descriptor = None
    for klass in arduinoML_Transition.__mro__:
        if "d_values" in klass.__dict__:
            descriptor = klass.__dict__["d_values"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml_transition_has_time():
    assert hasattr(arduinoML_Transition, "time")
    descriptor = None
    for klass in arduinoML_Transition.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml_transition_has_unit():
    assert hasattr(arduinoML_Transition, "unit")
    descriptor = None
    for klass in arduinoML_Transition.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml_transition_has_a_values():
    assert hasattr(arduinoML_Transition, "a_values")
    descriptor = None
    for klass in arduinoML_Transition.__mro__:
        if "a_values" in klass.__dict__:
            descriptor = klass.__dict__["a_values"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml_transitionstate_is_not_abstract():
    assert not inspect.isabstract(arduinoML_TransitionState)


def test_arduinoml_transitionstate_constructor_exists():
    assert callable(arduinoML_TransitionState.__init__)


def test_arduinoml_transitionstate_constructor_args():
    sig = inspect.signature(arduinoML_TransitionState.__init__)
    params = list(sig.parameters.keys())



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



def test_arduinoml_analog_is_not_abstract():
    assert not inspect.isabstract(arduinoML_Analog)


def test_arduinoml_analog_constructor_exists():
    assert callable(arduinoML_Analog.__init__)


def test_arduinoml_analog_constructor_args():
    sig = inspect.signature(arduinoML_Analog.__init__)
    params = list(sig.parameters.keys())
    assert "debug" in params, "Missing parameter 'debug'"

def test_arduinoml_analog_has_debug():
    assert hasattr(arduinoML_Analog, "debug")
    descriptor = None
    for klass in arduinoML_Analog.__mro__:
        if "debug" in klass.__dict__:
            descriptor = klass.__dict__["debug"]
            break
    assert isinstance(descriptor, property)



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



def test_arduinoml_mode_is_not_abstract():
    assert not inspect.isabstract(arduinoML_Mode)


def test_arduinoml_mode_constructor_exists():
    assert callable(arduinoML_Mode.__init__)


def test_arduinoml_mode_constructor_args():
    sig = inspect.signature(arduinoML_Mode.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_app_is_not_abstract():
    assert not inspect.isabstract(arduinoML_App)


def test_arduinoml_app_constructor_exists():
    assert callable(arduinoML_App.__init__)


def test_arduinoml_app_constructor_args():
    sig = inspect.signature(arduinoML_App.__init__)
    params = list(sig.parameters.keys())
    assert "monitoring" in params, "Missing parameter 'monitoring'"

def test_arduinoml_app_has_monitoring():
    assert hasattr(arduinoML_App, "monitoring")
    descriptor = None
    for klass in arduinoML_App.__mro__:
        if "monitoring" in klass.__dict__:
            descriptor = klass.__dict__["monitoring"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml_digital_is_not_abstract():
    assert not inspect.isabstract(arduinoML_Digital)


def test_arduinoml_digital_constructor_exists():
    assert callable(arduinoML_Digital.__init__)


def test_arduinoml_digital_constructor_args():
    sig = inspect.signature(arduinoML_Digital.__init__)
    params = list(sig.parameters.keys())

def test_time_unit_exists():
    # Check that the Enumeration exists
    assert Time_unit is not None

def test_time_unit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Time_unit]
    expected_literals = [
        "ms",
        "s",
        "min",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Time_unit"

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

def test_compare_exists():
    # Check that the Enumeration exists
    assert Compare is not None

def test_compare_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Compare]
    expected_literals = [
        "esup",
        "einf",
        "equal",
        "inf",
        "sup",
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
arduinoML_TransitionMode_strategy = st.builds(
    arduinoML_TransitionMode,
)
arduinoML_NamedElement_strategy = st.builds(
    arduinoML_NamedElement,
    name=
        safe_text
)
arduinoML_Transition_strategy = st.builds(
    arduinoML_Transition,
    comp=
        safe_text,
    d_values=
        safe_text,
    time=
        st.integers(),
    unit=
        safe_text,
    a_values=
        st.integers()
)
arduinoML_TransitionState_strategy = st.builds(
    arduinoML_TransitionState,
)
arduinoML_Action_strategy = st.builds(
    arduinoML_Action,
    value=
        safe_text
)
Brick_strategy = st.builds(
    Brick,
)
arduinoML_Analog_strategy = st.builds(
    arduinoML_Analog,
    debug=
        st.booleans()
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
arduinoML_Brick_strategy = st.builds(
    arduinoML_Brick,
    pin=
        st.integers()
)
arduinoML_Mode_strategy = st.builds(
    arduinoML_Mode,
)
arduinoML_App_strategy = st.builds(
    arduinoML_App,
    monitoring=
        st.booleans()
)
arduinoML_Digital_strategy = st.builds(
    arduinoML_Digital,
)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=arduinoML_TransitionMode_strategy)
@settings(max_examples=50)
def test_arduinoml_transitionmode_instantiation(instance):
    assert isinstance(instance, arduinoML_TransitionMode)

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
def test_arduinoml_transition_comp_setter(instance):
    original = instance.comp
    instance.comp = original
    assert instance.comp == original



@given(instance=arduinoML_Transition_strategy)
def test_arduinoml_transition_d_values_setter(instance):
    original = instance.d_values
    instance.d_values = original
    assert instance.d_values == original



@given(instance=arduinoML_Transition_strategy)
def test_arduinoml_transition_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=arduinoML_Transition_strategy)
def test_arduinoml_transition_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original



@given(instance=arduinoML_Transition_strategy)
def test_arduinoml_transition_a_values_setter(instance):
    original = instance.a_values
    instance.a_values = original
    assert instance.a_values == original

@given(instance=arduinoML_TransitionState_strategy)
@settings(max_examples=50)
def test_arduinoml_transitionstate_instantiation(instance):
    assert isinstance(instance, arduinoML_TransitionState)

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

@given(instance=arduinoML_Analog_strategy)
@settings(max_examples=50)
def test_arduinoml_analog_instantiation(instance):
    assert isinstance(instance, arduinoML_Analog)



@given(instance=arduinoML_Analog_strategy)
def test_arduinoml_analog_debug_setter(instance):
    original = instance.debug
    instance.debug = original
    assert instance.debug == original

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

@given(instance=arduinoML_Brick_strategy)
@settings(max_examples=50)
def test_arduinoml_brick_instantiation(instance):
    assert isinstance(instance, arduinoML_Brick)



@given(instance=arduinoML_Brick_strategy)
def test_arduinoml_brick_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original

@given(instance=arduinoML_Mode_strategy)
@settings(max_examples=50)
def test_arduinoml_mode_instantiation(instance):
    assert isinstance(instance, arduinoML_Mode)

@given(instance=arduinoML_App_strategy)
@settings(max_examples=50)
def test_arduinoml_app_instantiation(instance):
    assert isinstance(instance, arduinoML_App)



@given(instance=arduinoML_App_strategy)
def test_arduinoml_app_monitoring_setter(instance):
    original = instance.monitoring
    instance.monitoring = original
    assert instance.monitoring == original

@given(instance=arduinoML_Digital_strategy)
@settings(max_examples=50)
def test_arduinoml_digital_instantiation(instance):
    assert isinstance(instance, arduinoML_Digital)
