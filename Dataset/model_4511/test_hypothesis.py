import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AnalogAction,
    arduinoml::AnalogActionSensor,
    arduinoml::AnalogActionValue,
    Action,
    arduinoml::AnalogAction,
    arduinoml::DigitalAction,
    Condition,
    arduinoml::AnalogCondition,
    arduinoml::DigitalCondition,
    arduinoml::TimeCondition,
    arduinoml::Condition,
    arduinoml::NamedElement,
    Brick,
    arduinoml::AnalogSensor,
    arduinoml::AnalogActuator,
    arduinoml::DigitalActuator,
    arduinoml::DigitalSensor,
    arduinoml::Action,
    arduinoml::Transition,
    NamedElement,
    arduinoml::AMLState,
    arduinoml::Brick,
    arduinoml::AMLMachine,
    DigitalState,
    AnalogComparison,
    TimeComparison,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_analogaction_is_not_abstract():
    assert not inspect.isabstract(AnalogAction)


def test_analogaction_constructor_exists():
    assert callable(AnalogAction.__init__)


def test_analogaction_constructor_args():
    sig = inspect.signature(AnalogAction.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::analogactionsensor_is_not_abstract():
    assert not inspect.isabstract(arduinoml::AnalogActionSensor)


def test_arduinoml::analogactionsensor_constructor_exists():
    assert callable(arduinoml::AnalogActionSensor.__init__)


def test_arduinoml::analogactionsensor_constructor_args():
    sig = inspect.signature(arduinoml::AnalogActionSensor.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::analogactionvalue_is_not_abstract():
    assert not inspect.isabstract(arduinoml::AnalogActionValue)


def test_arduinoml::analogactionvalue_constructor_exists():
    assert callable(arduinoml::AnalogActionValue.__init__)


def test_arduinoml::analogactionvalue_constructor_args():
    sig = inspect.signature(arduinoml::AnalogActionValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduinoml::analogactionvalue_has_value():
    assert hasattr(arduinoml::AnalogActionValue, "value")
    descriptor = None
    for klass in arduinoml::AnalogActionValue.__mro__:
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



def test_arduinoml::analogaction_is_not_abstract():
    assert not inspect.isabstract(arduinoml::AnalogAction)


def test_arduinoml::analogaction_constructor_exists():
    assert callable(arduinoml::AnalogAction.__init__)


def test_arduinoml::analogaction_constructor_args():
    sig = inspect.signature(arduinoml::AnalogAction.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::digitalaction_is_not_abstract():
    assert not inspect.isabstract(arduinoml::DigitalAction)


def test_arduinoml::digitalaction_constructor_exists():
    assert callable(arduinoml::DigitalAction.__init__)


def test_arduinoml::digitalaction_constructor_args():
    sig = inspect.signature(arduinoml::DigitalAction.__init__)
    params = list(sig.parameters.keys())
    assert "dState" in params, "Missing parameter 'dState'"

def test_arduinoml::digitalaction_has_dState():
    assert hasattr(arduinoml::DigitalAction, "dState")
    descriptor = None
    for klass in arduinoml::DigitalAction.__mro__:
        if "dState" in klass.__dict__:
            descriptor = klass.__dict__["dState"]
            break
    assert isinstance(descriptor, property)



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::analogcondition_is_not_abstract():
    assert not inspect.isabstract(arduinoml::AnalogCondition)


def test_arduinoml::analogcondition_constructor_exists():
    assert callable(arduinoml::AnalogCondition.__init__)


def test_arduinoml::analogcondition_constructor_args():
    sig = inspect.signature(arduinoml::AnalogCondition.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "aComp" in params, "Missing parameter 'aComp'"

def test_arduinoml::analogcondition_has_value():
    assert hasattr(arduinoml::AnalogCondition, "value")
    descriptor = None
    for klass in arduinoml::AnalogCondition.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml::analogcondition_has_aComp():
    assert hasattr(arduinoml::AnalogCondition, "aComp")
    descriptor = None
    for klass in arduinoml::AnalogCondition.__mro__:
        if "aComp" in klass.__dict__:
            descriptor = klass.__dict__["aComp"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml::digitalcondition_is_not_abstract():
    assert not inspect.isabstract(arduinoml::DigitalCondition)


def test_arduinoml::digitalcondition_constructor_exists():
    assert callable(arduinoml::DigitalCondition.__init__)


def test_arduinoml::digitalcondition_constructor_args():
    sig = inspect.signature(arduinoml::DigitalCondition.__init__)
    params = list(sig.parameters.keys())
    assert "dState" in params, "Missing parameter 'dState'"

def test_arduinoml::digitalcondition_has_dState():
    assert hasattr(arduinoml::DigitalCondition, "dState")
    descriptor = None
    for klass in arduinoml::DigitalCondition.__mro__:
        if "dState" in klass.__dict__:
            descriptor = klass.__dict__["dState"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml::timecondition_is_not_abstract():
    assert not inspect.isabstract(arduinoml::TimeCondition)


def test_arduinoml::timecondition_constructor_exists():
    assert callable(arduinoml::TimeCondition.__init__)


def test_arduinoml::timecondition_constructor_args():
    sig = inspect.signature(arduinoml::TimeCondition.__init__)
    params = list(sig.parameters.keys())
    assert "tComp" in params, "Missing parameter 'tComp'"
    assert "time" in params, "Missing parameter 'time'"

def test_arduinoml::timecondition_has_tComp():
    assert hasattr(arduinoml::TimeCondition, "tComp")
    descriptor = None
    for klass in arduinoml::TimeCondition.__mro__:
        if "tComp" in klass.__dict__:
            descriptor = klass.__dict__["tComp"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml::timecondition_has_time():
    assert hasattr(arduinoml::TimeCondition, "time")
    descriptor = None
    for klass in arduinoml::TimeCondition.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml::condition_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Condition)


def test_arduinoml::condition_constructor_exists():
    assert callable(arduinoml::Condition.__init__)


def test_arduinoml::condition_constructor_args():
    sig = inspect.signature(arduinoml::Condition.__init__)
    params = list(sig.parameters.keys())



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



def test_brick_is_not_abstract():
    assert not inspect.isabstract(Brick)


def test_brick_constructor_exists():
    assert callable(Brick.__init__)


def test_brick_constructor_args():
    sig = inspect.signature(Brick.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::analogsensor_is_not_abstract():
    assert not inspect.isabstract(arduinoml::AnalogSensor)


def test_arduinoml::analogsensor_constructor_exists():
    assert callable(arduinoml::AnalogSensor.__init__)


def test_arduinoml::analogsensor_constructor_args():
    sig = inspect.signature(arduinoml::AnalogSensor.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::analogactuator_is_not_abstract():
    assert not inspect.isabstract(arduinoml::AnalogActuator)


def test_arduinoml::analogactuator_constructor_exists():
    assert callable(arduinoml::AnalogActuator.__init__)


def test_arduinoml::analogactuator_constructor_args():
    sig = inspect.signature(arduinoml::AnalogActuator.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::digitalactuator_is_not_abstract():
    assert not inspect.isabstract(arduinoml::DigitalActuator)


def test_arduinoml::digitalactuator_constructor_exists():
    assert callable(arduinoml::DigitalActuator.__init__)


def test_arduinoml::digitalactuator_constructor_args():
    sig = inspect.signature(arduinoml::DigitalActuator.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::digitalsensor_is_not_abstract():
    assert not inspect.isabstract(arduinoml::DigitalSensor)


def test_arduinoml::digitalsensor_constructor_exists():
    assert callable(arduinoml::DigitalSensor.__init__)


def test_arduinoml::digitalsensor_constructor_args():
    sig = inspect.signature(arduinoml::DigitalSensor.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::action_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Action)


def test_arduinoml::action_constructor_exists():
    assert callable(arduinoml::Action.__init__)


def test_arduinoml::action_constructor_args():
    sig = inspect.signature(arduinoml::Action.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::transition_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Transition)


def test_arduinoml::transition_constructor_exists():
    assert callable(arduinoml::Transition.__init__)


def test_arduinoml::transition_constructor_args():
    sig = inspect.signature(arduinoml::Transition.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::amlstate_is_not_abstract():
    assert not inspect.isabstract(arduinoml::AMLState)


def test_arduinoml::amlstate_constructor_exists():
    assert callable(arduinoml::AMLState.__init__)


def test_arduinoml::amlstate_constructor_args():
    sig = inspect.signature(arduinoml::AMLState.__init__)
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



def test_arduinoml::amlmachine_is_not_abstract():
    assert not inspect.isabstract(arduinoml::AMLMachine)


def test_arduinoml::amlmachine_constructor_exists():
    assert callable(arduinoml::AMLMachine.__init__)


def test_arduinoml::amlmachine_constructor_args():
    sig = inspect.signature(arduinoml::AMLMachine.__init__)
    params = list(sig.parameters.keys())
    assert "frequency" in params, "Missing parameter 'frequency'"

def test_arduinoml::amlmachine_has_frequency():
    assert hasattr(arduinoml::AMLMachine, "frequency")
    descriptor = None
    for klass in arduinoml::AMLMachine.__mro__:
        if "frequency" in klass.__dict__:
            descriptor = klass.__dict__["frequency"]
            break
    assert isinstance(descriptor, property)

def test_digitalstate_exists():
    # Check that the Enumeration exists
    assert DigitalState is not None

def test_digitalstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DigitalState]
    expected_literals = [
        "OFF",
        "ON",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DigitalState"

def test_analogcomparison_exists():
    # Check that the Enumeration exists
    assert AnalogComparison is not None

def test_analogcomparison_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AnalogComparison]
    expected_literals = [
        "EQUAL",
        "GREATEREQ",
        "LOWEREQ",
        "GREATER",
        "LOWER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AnalogComparison"

def test_timecomparison_exists():
    # Check that the Enumeration exists
    assert TimeComparison is not None

def test_timecomparison_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeComparison]
    expected_literals = [
        "AFTER",
        "BEFORE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeComparison"


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
AnalogAction_strategy = st.builds(
    AnalogAction,
)
arduinoml::AnalogActionSensor_strategy = st.builds(
    arduinoml::AnalogActionSensor,
)
arduinoml::AnalogActionValue_strategy = st.builds(
    arduinoml::AnalogActionValue,
    value=
        st.integers()
)
Action_strategy = st.builds(
    Action,
)
arduinoml::AnalogAction_strategy = st.builds(
    arduinoml::AnalogAction,
)
arduinoml::DigitalAction_strategy = st.builds(
    arduinoml::DigitalAction,
    dState=
        safe_text
)
Condition_strategy = st.builds(
    Condition,
)
arduinoml::AnalogCondition_strategy = st.builds(
    arduinoml::AnalogCondition,
    value=
        st.integers(),
    aComp=
        safe_text
)
arduinoml::DigitalCondition_strategy = st.builds(
    arduinoml::DigitalCondition,
    dState=
        safe_text
)
arduinoml::TimeCondition_strategy = st.builds(
    arduinoml::TimeCondition,
    tComp=
        safe_text,
    time=
        st.integers()
)
arduinoml::Condition_strategy = st.builds(
    arduinoml::Condition,
)
arduinoml::NamedElement_strategy = st.builds(
    arduinoml::NamedElement,
    name=
        safe_text
)
Brick_strategy = st.builds(
    Brick,
)
arduinoml::AnalogSensor_strategy = st.builds(
    arduinoml::AnalogSensor,
)
arduinoml::AnalogActuator_strategy = st.builds(
    arduinoml::AnalogActuator,
)
arduinoml::DigitalActuator_strategy = st.builds(
    arduinoml::DigitalActuator,
)
arduinoml::DigitalSensor_strategy = st.builds(
    arduinoml::DigitalSensor,
)
arduinoml::Action_strategy = st.builds(
    arduinoml::Action,
)
arduinoml::Transition_strategy = st.builds(
    arduinoml::Transition,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
arduinoml::AMLState_strategy = st.builds(
    arduinoml::AMLState,
)
arduinoml::Brick_strategy = st.builds(
    arduinoml::Brick,
    pin=
        st.integers()
)
arduinoml::AMLMachine_strategy = st.builds(
    arduinoml::AMLMachine,
    frequency=
        st.integers()
)

@given(instance=AnalogAction_strategy)
@settings(max_examples=50)
def test_analogaction_instantiation(instance):
    assert isinstance(instance, AnalogAction)

@given(instance=arduinoml::AnalogActionSensor_strategy)
@settings(max_examples=50)
def test_arduinoml::analogactionsensor_instantiation(instance):
    assert isinstance(instance, arduinoml::AnalogActionSensor)

@given(instance=arduinoml::AnalogActionValue_strategy)
@settings(max_examples=50)
def test_arduinoml::analogactionvalue_instantiation(instance):
    assert isinstance(instance, arduinoml::AnalogActionValue)

@given(instance=arduinoml::AnalogActionValue_strategy)
def test_arduinoml::analogactionvalue_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=arduinoml::AnalogActionValue_strategy)
def test_arduinoml::analogactionvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=arduinoml::AnalogAction_strategy)
@settings(max_examples=50)
def test_arduinoml::analogaction_instantiation(instance):
    assert isinstance(instance, arduinoml::AnalogAction)

@given(instance=arduinoml::DigitalAction_strategy)
@settings(max_examples=50)
def test_arduinoml::digitalaction_instantiation(instance):
    assert isinstance(instance, arduinoml::DigitalAction)

@given(instance=arduinoml::DigitalAction_strategy)
def test_arduinoml::digitalaction_dState_type(instance):
    assert isinstance(instance.dState, str)


@given(instance=arduinoml::DigitalAction_strategy)
def test_arduinoml::digitalaction_dState_setter(instance):
    original = instance.dState
    instance.dState = original
    assert instance.dState == original

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=arduinoml::AnalogCondition_strategy)
@settings(max_examples=50)
def test_arduinoml::analogcondition_instantiation(instance):
    assert isinstance(instance, arduinoml::AnalogCondition)

@given(instance=arduinoml::AnalogCondition_strategy)
def test_arduinoml::analogcondition_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=arduinoml::AnalogCondition_strategy)
def test_arduinoml::analogcondition_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arduinoml::AnalogCondition_strategy)
def test_arduinoml::analogcondition_aComp_type(instance):
    assert isinstance(instance.aComp, str)


@given(instance=arduinoml::AnalogCondition_strategy)
def test_arduinoml::analogcondition_aComp_setter(instance):
    original = instance.aComp
    instance.aComp = original
    assert instance.aComp == original

@given(instance=arduinoml::DigitalCondition_strategy)
@settings(max_examples=50)
def test_arduinoml::digitalcondition_instantiation(instance):
    assert isinstance(instance, arduinoml::DigitalCondition)

@given(instance=arduinoml::DigitalCondition_strategy)
def test_arduinoml::digitalcondition_dState_type(instance):
    assert isinstance(instance.dState, str)


@given(instance=arduinoml::DigitalCondition_strategy)
def test_arduinoml::digitalcondition_dState_setter(instance):
    original = instance.dState
    instance.dState = original
    assert instance.dState == original

@given(instance=arduinoml::TimeCondition_strategy)
@settings(max_examples=50)
def test_arduinoml::timecondition_instantiation(instance):
    assert isinstance(instance, arduinoml::TimeCondition)

@given(instance=arduinoml::TimeCondition_strategy)
def test_arduinoml::timecondition_tComp_type(instance):
    assert isinstance(instance.tComp, str)


@given(instance=arduinoml::TimeCondition_strategy)
def test_arduinoml::timecondition_tComp_setter(instance):
    original = instance.tComp
    instance.tComp = original
    assert instance.tComp == original

@given(instance=arduinoml::TimeCondition_strategy)
def test_arduinoml::timecondition_time_type(instance):
    assert isinstance(instance.time, int)


@given(instance=arduinoml::TimeCondition_strategy)
def test_arduinoml::timecondition_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=arduinoml::Condition_strategy)
@settings(max_examples=50)
def test_arduinoml::condition_instantiation(instance):
    assert isinstance(instance, arduinoml::Condition)

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

@given(instance=Brick_strategy)
@settings(max_examples=50)
def test_brick_instantiation(instance):
    assert isinstance(instance, Brick)

@given(instance=arduinoml::AnalogSensor_strategy)
@settings(max_examples=50)
def test_arduinoml::analogsensor_instantiation(instance):
    assert isinstance(instance, arduinoml::AnalogSensor)

@given(instance=arduinoml::AnalogActuator_strategy)
@settings(max_examples=50)
def test_arduinoml::analogactuator_instantiation(instance):
    assert isinstance(instance, arduinoml::AnalogActuator)

@given(instance=arduinoml::DigitalActuator_strategy)
@settings(max_examples=50)
def test_arduinoml::digitalactuator_instantiation(instance):
    assert isinstance(instance, arduinoml::DigitalActuator)

@given(instance=arduinoml::DigitalSensor_strategy)
@settings(max_examples=50)
def test_arduinoml::digitalsensor_instantiation(instance):
    assert isinstance(instance, arduinoml::DigitalSensor)

@given(instance=arduinoml::Action_strategy)
@settings(max_examples=50)
def test_arduinoml::action_instantiation(instance):
    assert isinstance(instance, arduinoml::Action)

@given(instance=arduinoml::Transition_strategy)
@settings(max_examples=50)
def test_arduinoml::transition_instantiation(instance):
    assert isinstance(instance, arduinoml::Transition)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=arduinoml::AMLState_strategy)
@settings(max_examples=50)
def test_arduinoml::amlstate_instantiation(instance):
    assert isinstance(instance, arduinoml::AMLState)

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

@given(instance=arduinoml::AMLMachine_strategy)
@settings(max_examples=50)
def test_arduinoml::amlmachine_instantiation(instance):
    assert isinstance(instance, arduinoml::AMLMachine)

@given(instance=arduinoml::AMLMachine_strategy)
def test_arduinoml::amlmachine_frequency_type(instance):
    assert isinstance(instance.frequency, int)


@given(instance=arduinoml::AMLMachine_strategy)
def test_arduinoml::amlmachine_frequency_setter(instance):
    original = instance.frequency
    instance.frequency = original
    assert instance.frequency == original
