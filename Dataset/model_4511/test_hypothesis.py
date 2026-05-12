import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AnalogAction,
    arduinoml_AnalogActionSensor,
    arduinoml_AnalogActionValue,
    Action,
    arduinoml_AnalogAction,
    arduinoml_DigitalAction,
    Condition,
    arduinoml_AnalogCondition,
    arduinoml_DigitalCondition,
    arduinoml_TimeCondition,
    arduinoml_Condition,
    arduinoml_NamedElement,
    Brick,
    arduinoml_AnalogSensor,
    arduinoml_AnalogActuator,
    arduinoml_DigitalActuator,
    arduinoml_DigitalSensor,
    arduinoml_Action,
    arduinoml_Transition,
    NamedElement,
    arduinoml_AMLState,
    arduinoml_Brick,
    arduinoml_AMLMachine,
    AnalogComparison,
    DigitalState,
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



def test_arduinoml_analogactionsensor_is_not_abstract():
    assert not inspect.isabstract(arduinoml_AnalogActionSensor)


def test_arduinoml_analogactionsensor_constructor_exists():
    assert callable(arduinoml_AnalogActionSensor.__init__)


def test_arduinoml_analogactionsensor_constructor_args():
    sig = inspect.signature(arduinoml_AnalogActionSensor.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_analogactionvalue_is_not_abstract():
    assert not inspect.isabstract(arduinoml_AnalogActionValue)


def test_arduinoml_analogactionvalue_constructor_exists():
    assert callable(arduinoml_AnalogActionValue.__init__)


def test_arduinoml_analogactionvalue_constructor_args():
    sig = inspect.signature(arduinoml_AnalogActionValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduinoml_analogactionvalue_has_value():
    assert hasattr(arduinoml_AnalogActionValue, "value")
    descriptor = None
    for klass in arduinoml_AnalogActionValue.__mro__:
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



def test_arduinoml_analogaction_is_not_abstract():
    assert not inspect.isabstract(arduinoml_AnalogAction)


def test_arduinoml_analogaction_constructor_exists():
    assert callable(arduinoml_AnalogAction.__init__)


def test_arduinoml_analogaction_constructor_args():
    sig = inspect.signature(arduinoml_AnalogAction.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_digitalaction_is_not_abstract():
    assert not inspect.isabstract(arduinoml_DigitalAction)


def test_arduinoml_digitalaction_constructor_exists():
    assert callable(arduinoml_DigitalAction.__init__)


def test_arduinoml_digitalaction_constructor_args():
    sig = inspect.signature(arduinoml_DigitalAction.__init__)
    params = list(sig.parameters.keys())
    assert "dState" in params, "Missing parameter 'dState'"

def test_arduinoml_digitalaction_has_dState():
    assert hasattr(arduinoml_DigitalAction, "dState")
    descriptor = None
    for klass in arduinoml_DigitalAction.__mro__:
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



def test_arduinoml_analogcondition_is_not_abstract():
    assert not inspect.isabstract(arduinoml_AnalogCondition)


def test_arduinoml_analogcondition_constructor_exists():
    assert callable(arduinoml_AnalogCondition.__init__)


def test_arduinoml_analogcondition_constructor_args():
    sig = inspect.signature(arduinoml_AnalogCondition.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "aComp" in params, "Missing parameter 'aComp'"

def test_arduinoml_analogcondition_has_value():
    assert hasattr(arduinoml_AnalogCondition, "value")
    descriptor = None
    for klass in arduinoml_AnalogCondition.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml_analogcondition_has_aComp():
    assert hasattr(arduinoml_AnalogCondition, "aComp")
    descriptor = None
    for klass in arduinoml_AnalogCondition.__mro__:
        if "aComp" in klass.__dict__:
            descriptor = klass.__dict__["aComp"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml_digitalcondition_is_not_abstract():
    assert not inspect.isabstract(arduinoml_DigitalCondition)


def test_arduinoml_digitalcondition_constructor_exists():
    assert callable(arduinoml_DigitalCondition.__init__)


def test_arduinoml_digitalcondition_constructor_args():
    sig = inspect.signature(arduinoml_DigitalCondition.__init__)
    params = list(sig.parameters.keys())
    assert "dState" in params, "Missing parameter 'dState'"

def test_arduinoml_digitalcondition_has_dState():
    assert hasattr(arduinoml_DigitalCondition, "dState")
    descriptor = None
    for klass in arduinoml_DigitalCondition.__mro__:
        if "dState" in klass.__dict__:
            descriptor = klass.__dict__["dState"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml_timecondition_is_not_abstract():
    assert not inspect.isabstract(arduinoml_TimeCondition)


def test_arduinoml_timecondition_constructor_exists():
    assert callable(arduinoml_TimeCondition.__init__)


def test_arduinoml_timecondition_constructor_args():
    sig = inspect.signature(arduinoml_TimeCondition.__init__)
    params = list(sig.parameters.keys())
    assert "tComp" in params, "Missing parameter 'tComp'"
    assert "time" in params, "Missing parameter 'time'"

def test_arduinoml_timecondition_has_tComp():
    assert hasattr(arduinoml_TimeCondition, "tComp")
    descriptor = None
    for klass in arduinoml_TimeCondition.__mro__:
        if "tComp" in klass.__dict__:
            descriptor = klass.__dict__["tComp"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml_timecondition_has_time():
    assert hasattr(arduinoml_TimeCondition, "time")
    descriptor = None
    for klass in arduinoml_TimeCondition.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml_condition_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Condition)


def test_arduinoml_condition_constructor_exists():
    assert callable(arduinoml_Condition.__init__)


def test_arduinoml_condition_constructor_args():
    sig = inspect.signature(arduinoml_Condition.__init__)
    params = list(sig.parameters.keys())



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



def test_brick_is_not_abstract():
    assert not inspect.isabstract(Brick)


def test_brick_constructor_exists():
    assert callable(Brick.__init__)


def test_brick_constructor_args():
    sig = inspect.signature(Brick.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_analogsensor_is_not_abstract():
    assert not inspect.isabstract(arduinoml_AnalogSensor)


def test_arduinoml_analogsensor_constructor_exists():
    assert callable(arduinoml_AnalogSensor.__init__)


def test_arduinoml_analogsensor_constructor_args():
    sig = inspect.signature(arduinoml_AnalogSensor.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_analogactuator_is_not_abstract():
    assert not inspect.isabstract(arduinoml_AnalogActuator)


def test_arduinoml_analogactuator_constructor_exists():
    assert callable(arduinoml_AnalogActuator.__init__)


def test_arduinoml_analogactuator_constructor_args():
    sig = inspect.signature(arduinoml_AnalogActuator.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_digitalactuator_is_not_abstract():
    assert not inspect.isabstract(arduinoml_DigitalActuator)


def test_arduinoml_digitalactuator_constructor_exists():
    assert callable(arduinoml_DigitalActuator.__init__)


def test_arduinoml_digitalactuator_constructor_args():
    sig = inspect.signature(arduinoml_DigitalActuator.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_digitalsensor_is_not_abstract():
    assert not inspect.isabstract(arduinoml_DigitalSensor)


def test_arduinoml_digitalsensor_constructor_exists():
    assert callable(arduinoml_DigitalSensor.__init__)


def test_arduinoml_digitalsensor_constructor_args():
    sig = inspect.signature(arduinoml_DigitalSensor.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_action_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Action)


def test_arduinoml_action_constructor_exists():
    assert callable(arduinoml_Action.__init__)


def test_arduinoml_action_constructor_args():
    sig = inspect.signature(arduinoml_Action.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_transition_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Transition)


def test_arduinoml_transition_constructor_exists():
    assert callable(arduinoml_Transition.__init__)


def test_arduinoml_transition_constructor_args():
    sig = inspect.signature(arduinoml_Transition.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_amlstate_is_not_abstract():
    assert not inspect.isabstract(arduinoml_AMLState)


def test_arduinoml_amlstate_constructor_exists():
    assert callable(arduinoml_AMLState.__init__)


def test_arduinoml_amlstate_constructor_args():
    sig = inspect.signature(arduinoml_AMLState.__init__)
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



def test_arduinoml_amlmachine_is_not_abstract():
    assert not inspect.isabstract(arduinoml_AMLMachine)


def test_arduinoml_amlmachine_constructor_exists():
    assert callable(arduinoml_AMLMachine.__init__)


def test_arduinoml_amlmachine_constructor_args():
    sig = inspect.signature(arduinoml_AMLMachine.__init__)
    params = list(sig.parameters.keys())
    assert "frequency" in params, "Missing parameter 'frequency'"

def test_arduinoml_amlmachine_has_frequency():
    assert hasattr(arduinoml_AMLMachine, "frequency")
    descriptor = None
    for klass in arduinoml_AMLMachine.__mro__:
        if "frequency" in klass.__dict__:
            descriptor = klass.__dict__["frequency"]
            break
    assert isinstance(descriptor, property)

def test_analogcomparison_exists():
    # Check that the Enumeration exists
    assert AnalogComparison is not None

def test_analogcomparison_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AnalogComparison]
    expected_literals = [
        "GREATER",
        "GREATEREQ",
        "EQUAL",
        "LOWER",
        "LOWEREQ",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AnalogComparison"

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

def test_timecomparison_exists():
    # Check that the Enumeration exists
    assert TimeComparison is not None

def test_timecomparison_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeComparison]
    expected_literals = [
        "BEFORE",
        "AFTER",
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
arduinoml_AnalogActionSensor_strategy = st.builds(
    arduinoml_AnalogActionSensor,
)
arduinoml_AnalogActionValue_strategy = st.builds(
    arduinoml_AnalogActionValue,
    value=
        st.integers()
)
Action_strategy = st.builds(
    Action,
)
arduinoml_AnalogAction_strategy = st.builds(
    arduinoml_AnalogAction,
)
arduinoml_DigitalAction_strategy = st.builds(
    arduinoml_DigitalAction,
    dState=
        safe_text
)
Condition_strategy = st.builds(
    Condition,
)
arduinoml_AnalogCondition_strategy = st.builds(
    arduinoml_AnalogCondition,
    value=
        st.integers(),
    aComp=
        safe_text
)
arduinoml_DigitalCondition_strategy = st.builds(
    arduinoml_DigitalCondition,
    dState=
        safe_text
)
arduinoml_TimeCondition_strategy = st.builds(
    arduinoml_TimeCondition,
    tComp=
        safe_text,
    time=
        st.integers()
)
arduinoml_Condition_strategy = st.builds(
    arduinoml_Condition,
)
arduinoml_NamedElement_strategy = st.builds(
    arduinoml_NamedElement,
    name=
        safe_text
)
Brick_strategy = st.builds(
    Brick,
)
arduinoml_AnalogSensor_strategy = st.builds(
    arduinoml_AnalogSensor,
)
arduinoml_AnalogActuator_strategy = st.builds(
    arduinoml_AnalogActuator,
)
arduinoml_DigitalActuator_strategy = st.builds(
    arduinoml_DigitalActuator,
)
arduinoml_DigitalSensor_strategy = st.builds(
    arduinoml_DigitalSensor,
)
arduinoml_Action_strategy = st.builds(
    arduinoml_Action,
)
arduinoml_Transition_strategy = st.builds(
    arduinoml_Transition,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
arduinoml_AMLState_strategy = st.builds(
    arduinoml_AMLState,
)
arduinoml_Brick_strategy = st.builds(
    arduinoml_Brick,
    pin=
        st.integers()
)
arduinoml_AMLMachine_strategy = st.builds(
    arduinoml_AMLMachine,
    frequency=
        st.integers()
)

@given(instance=AnalogAction_strategy)
@settings(max_examples=50)
def test_analogaction_instantiation(instance):
    assert isinstance(instance, AnalogAction)

@given(instance=arduinoml_AnalogActionSensor_strategy)
@settings(max_examples=50)
def test_arduinoml_analogactionsensor_instantiation(instance):
    assert isinstance(instance, arduinoml_AnalogActionSensor)

@given(instance=arduinoml_AnalogActionValue_strategy)
@settings(max_examples=50)
def test_arduinoml_analogactionvalue_instantiation(instance):
    assert isinstance(instance, arduinoml_AnalogActionValue)



@given(instance=arduinoml_AnalogActionValue_strategy)
def test_arduinoml_analogactionvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=arduinoml_AnalogAction_strategy)
@settings(max_examples=50)
def test_arduinoml_analogaction_instantiation(instance):
    assert isinstance(instance, arduinoml_AnalogAction)

@given(instance=arduinoml_DigitalAction_strategy)
@settings(max_examples=50)
def test_arduinoml_digitalaction_instantiation(instance):
    assert isinstance(instance, arduinoml_DigitalAction)



@given(instance=arduinoml_DigitalAction_strategy)
def test_arduinoml_digitalaction_dState_setter(instance):
    original = instance.dState
    instance.dState = original
    assert instance.dState == original

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=arduinoml_AnalogCondition_strategy)
@settings(max_examples=50)
def test_arduinoml_analogcondition_instantiation(instance):
    assert isinstance(instance, arduinoml_AnalogCondition)



@given(instance=arduinoml_AnalogCondition_strategy)
def test_arduinoml_analogcondition_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=arduinoml_AnalogCondition_strategy)
def test_arduinoml_analogcondition_aComp_setter(instance):
    original = instance.aComp
    instance.aComp = original
    assert instance.aComp == original

@given(instance=arduinoml_DigitalCondition_strategy)
@settings(max_examples=50)
def test_arduinoml_digitalcondition_instantiation(instance):
    assert isinstance(instance, arduinoml_DigitalCondition)



@given(instance=arduinoml_DigitalCondition_strategy)
def test_arduinoml_digitalcondition_dState_setter(instance):
    original = instance.dState
    instance.dState = original
    assert instance.dState == original

@given(instance=arduinoml_TimeCondition_strategy)
@settings(max_examples=50)
def test_arduinoml_timecondition_instantiation(instance):
    assert isinstance(instance, arduinoml_TimeCondition)



@given(instance=arduinoml_TimeCondition_strategy)
def test_arduinoml_timecondition_tComp_setter(instance):
    original = instance.tComp
    instance.tComp = original
    assert instance.tComp == original



@given(instance=arduinoml_TimeCondition_strategy)
def test_arduinoml_timecondition_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=arduinoml_Condition_strategy)
@settings(max_examples=50)
def test_arduinoml_condition_instantiation(instance):
    assert isinstance(instance, arduinoml_Condition)

@given(instance=arduinoml_NamedElement_strategy)
@settings(max_examples=50)
def test_arduinoml_namedelement_instantiation(instance):
    assert isinstance(instance, arduinoml_NamedElement)



@given(instance=arduinoml_NamedElement_strategy)
def test_arduinoml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Brick_strategy)
@settings(max_examples=50)
def test_brick_instantiation(instance):
    assert isinstance(instance, Brick)

@given(instance=arduinoml_AnalogSensor_strategy)
@settings(max_examples=50)
def test_arduinoml_analogsensor_instantiation(instance):
    assert isinstance(instance, arduinoml_AnalogSensor)

@given(instance=arduinoml_AnalogActuator_strategy)
@settings(max_examples=50)
def test_arduinoml_analogactuator_instantiation(instance):
    assert isinstance(instance, arduinoml_AnalogActuator)

@given(instance=arduinoml_DigitalActuator_strategy)
@settings(max_examples=50)
def test_arduinoml_digitalactuator_instantiation(instance):
    assert isinstance(instance, arduinoml_DigitalActuator)

@given(instance=arduinoml_DigitalSensor_strategy)
@settings(max_examples=50)
def test_arduinoml_digitalsensor_instantiation(instance):
    assert isinstance(instance, arduinoml_DigitalSensor)

@given(instance=arduinoml_Action_strategy)
@settings(max_examples=50)
def test_arduinoml_action_instantiation(instance):
    assert isinstance(instance, arduinoml_Action)

@given(instance=arduinoml_Transition_strategy)
@settings(max_examples=50)
def test_arduinoml_transition_instantiation(instance):
    assert isinstance(instance, arduinoml_Transition)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=arduinoml_AMLState_strategy)
@settings(max_examples=50)
def test_arduinoml_amlstate_instantiation(instance):
    assert isinstance(instance, arduinoml_AMLState)

@given(instance=arduinoml_Brick_strategy)
@settings(max_examples=50)
def test_arduinoml_brick_instantiation(instance):
    assert isinstance(instance, arduinoml_Brick)



@given(instance=arduinoml_Brick_strategy)
def test_arduinoml_brick_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original

@given(instance=arduinoml_AMLMachine_strategy)
@settings(max_examples=50)
def test_arduinoml_amlmachine_instantiation(instance):
    assert isinstance(instance, arduinoml_AMLMachine)



@given(instance=arduinoml_AMLMachine_strategy)
def test_arduinoml_amlmachine_frequency_setter(instance):
    original = instance.frequency
    instance.frequency = original
    assert instance.frequency == original
