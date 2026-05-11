import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Action,
    arduinoml::BinaryAction,
    arduinoml::AnalogAction,
    Actuator,
    arduinoml::BinaryActuator,
    arduinoml::AnalogActuator,
    Sensor,
    arduinoml::AnalogSensor,
    arduinoml::BinarySensor,
    Condition,
    arduinoml::ValueElementCondition,
    arduinoml::SingleElementCondition,
    arduinoml::Condition,
    Brick,
    arduinoml::Sensor,
    arduinoml::MultipleElementCondition,
    arduinoml::Actuator,
    arduinoml::Transition,
    arduinoml::Action,
    NamedElement,
    arduinoml::Brick,
    arduinoml::State,
    arduinoml::App,
    arduinoml::NamedElement,
    COMPARATOR,
    OPERATOR,
    SIGNAL,
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



def test_arduinoml::binaryaction_is_not_abstract():
    assert not inspect.isabstract(arduinoml::BinaryAction)


def test_arduinoml::binaryaction_constructor_exists():
    assert callable(arduinoml::BinaryAction.__init__)


def test_arduinoml::binaryaction_constructor_args():
    sig = inspect.signature(arduinoml::BinaryAction.__init__)
    params = list(sig.parameters.keys())
    assert "actionValue" in params, "Missing parameter 'actionValue'"

def test_arduinoml::binaryaction_has_actionValue():
    assert hasattr(arduinoml::BinaryAction, "actionValue")
    descriptor = None
    for klass in arduinoml::BinaryAction.__mro__:
        if "actionValue" in klass.__dict__:
            descriptor = klass.__dict__["actionValue"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml::analogaction_is_not_abstract():
    assert not inspect.isabstract(arduinoml::AnalogAction)


def test_arduinoml::analogaction_constructor_exists():
    assert callable(arduinoml::AnalogAction.__init__)


def test_arduinoml::analogaction_constructor_args():
    sig = inspect.signature(arduinoml::AnalogAction.__init__)
    params = list(sig.parameters.keys())
    assert "actionValue" in params, "Missing parameter 'actionValue'"

def test_arduinoml::analogaction_has_actionValue():
    assert hasattr(arduinoml::AnalogAction, "actionValue")
    descriptor = None
    for klass in arduinoml::AnalogAction.__mro__:
        if "actionValue" in klass.__dict__:
            descriptor = klass.__dict__["actionValue"]
            break
    assert isinstance(descriptor, property)



def test_actuator_is_not_abstract():
    assert not inspect.isabstract(Actuator)


def test_actuator_constructor_exists():
    assert callable(Actuator.__init__)


def test_actuator_constructor_args():
    sig = inspect.signature(Actuator.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::binaryactuator_is_not_abstract():
    assert not inspect.isabstract(arduinoml::BinaryActuator)


def test_arduinoml::binaryactuator_constructor_exists():
    assert callable(arduinoml::BinaryActuator.__init__)


def test_arduinoml::binaryactuator_constructor_args():
    sig = inspect.signature(arduinoml::BinaryActuator.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::analogactuator_is_not_abstract():
    assert not inspect.isabstract(arduinoml::AnalogActuator)


def test_arduinoml::analogactuator_constructor_exists():
    assert callable(arduinoml::AnalogActuator.__init__)


def test_arduinoml::analogactuator_constructor_args():
    sig = inspect.signature(arduinoml::AnalogActuator.__init__)
    params = list(sig.parameters.keys())



def test_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::analogsensor_is_not_abstract():
    assert not inspect.isabstract(arduinoml::AnalogSensor)


def test_arduinoml::analogsensor_constructor_exists():
    assert callable(arduinoml::AnalogSensor.__init__)


def test_arduinoml::analogsensor_constructor_args():
    sig = inspect.signature(arduinoml::AnalogSensor.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::binarysensor_is_not_abstract():
    assert not inspect.isabstract(arduinoml::BinarySensor)


def test_arduinoml::binarysensor_constructor_exists():
    assert callable(arduinoml::BinarySensor.__init__)


def test_arduinoml::binarysensor_constructor_args():
    sig = inspect.signature(arduinoml::BinarySensor.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::valueelementcondition_is_not_abstract():
    assert not inspect.isabstract(arduinoml::ValueElementCondition)


def test_arduinoml::valueelementcondition_constructor_exists():
    assert callable(arduinoml::ValueElementCondition.__init__)


def test_arduinoml::valueelementcondition_constructor_args():
    sig = inspect.signature(arduinoml::ValueElementCondition.__init__)
    params = list(sig.parameters.keys())
    assert "comparator" in params, "Missing parameter 'comparator'"
    assert "value" in params, "Missing parameter 'value'"

def test_arduinoml::valueelementcondition_has_comparator():
    assert hasattr(arduinoml::ValueElementCondition, "comparator")
    descriptor = None
    for klass in arduinoml::ValueElementCondition.__mro__:
        if "comparator" in klass.__dict__:
            descriptor = klass.__dict__["comparator"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml::valueelementcondition_has_value():
    assert hasattr(arduinoml::ValueElementCondition, "value")
    descriptor = None
    for klass in arduinoml::ValueElementCondition.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml::singleelementcondition_is_not_abstract():
    assert not inspect.isabstract(arduinoml::SingleElementCondition)


def test_arduinoml::singleelementcondition_constructor_exists():
    assert callable(arduinoml::SingleElementCondition.__init__)


def test_arduinoml::singleelementcondition_constructor_args():
    sig = inspect.signature(arduinoml::SingleElementCondition.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduinoml::singleelementcondition_has_value():
    assert hasattr(arduinoml::SingleElementCondition, "value")
    descriptor = None
    for klass in arduinoml::SingleElementCondition.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml::condition_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Condition)


def test_arduinoml::condition_constructor_exists():
    assert callable(arduinoml::Condition.__init__)


def test_arduinoml::condition_constructor_args():
    sig = inspect.signature(arduinoml::Condition.__init__)
    params = list(sig.parameters.keys())



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



def test_arduinoml::multipleelementcondition_is_not_abstract():
    assert not inspect.isabstract(arduinoml::MultipleElementCondition)


def test_arduinoml::multipleelementcondition_constructor_exists():
    assert callable(arduinoml::MultipleElementCondition.__init__)


def test_arduinoml::multipleelementcondition_constructor_args():
    sig = inspect.signature(arduinoml::MultipleElementCondition.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_arduinoml::multipleelementcondition_has_operators():
    assert hasattr(arduinoml::MultipleElementCondition, "operators")
    descriptor = None
    for klass in arduinoml::MultipleElementCondition.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



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



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
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



def test_arduinoml::state_is_not_abstract():
    assert not inspect.isabstract(arduinoml::State)


def test_arduinoml::state_constructor_exists():
    assert callable(arduinoml::State.__init__)


def test_arduinoml::state_constructor_args():
    sig = inspect.signature(arduinoml::State.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::app_is_not_abstract():
    assert not inspect.isabstract(arduinoml::App)


def test_arduinoml::app_constructor_exists():
    assert callable(arduinoml::App.__init__)


def test_arduinoml::app_constructor_args():
    sig = inspect.signature(arduinoml::App.__init__)
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

def test_comparator_exists():
    # Check that the Enumeration exists
    assert COMPARATOR is not None

def test_comparator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in COMPARATOR]
    expected_literals = [
        "INFERIOR",
        "SUPERIOR",
        "EQUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in COMPARATOR"

def test_operator_exists():
    # Check that the Enumeration exists
    assert OPERATOR is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OPERATOR]
    expected_literals = [
        "or_",
        "and_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OPERATOR"

def test_signal_exists():
    # Check that the Enumeration exists
    assert SIGNAL is not None

def test_signal_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SIGNAL]
    expected_literals = [
        "HIGH",
        "LOW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SIGNAL"


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
arduinoml::BinaryAction_strategy = st.builds(
    arduinoml::BinaryAction,
    actionValue=
        safe_text
)
arduinoml::AnalogAction_strategy = st.builds(
    arduinoml::AnalogAction,
    actionValue=
        st.integers()
)
Actuator_strategy = st.builds(
    Actuator,
)
arduinoml::BinaryActuator_strategy = st.builds(
    arduinoml::BinaryActuator,
)
arduinoml::AnalogActuator_strategy = st.builds(
    arduinoml::AnalogActuator,
)
Sensor_strategy = st.builds(
    Sensor,
)
arduinoml::AnalogSensor_strategy = st.builds(
    arduinoml::AnalogSensor,
)
arduinoml::BinarySensor_strategy = st.builds(
    arduinoml::BinarySensor,
)
Condition_strategy = st.builds(
    Condition,
)
arduinoml::ValueElementCondition_strategy = st.builds(
    arduinoml::ValueElementCondition,
    comparator=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
arduinoml::SingleElementCondition_strategy = st.builds(
    arduinoml::SingleElementCondition,
    value=
        safe_text
)
arduinoml::Condition_strategy = st.builds(
    arduinoml::Condition,
)
Brick_strategy = st.builds(
    Brick,
)
arduinoml::Sensor_strategy = st.builds(
    arduinoml::Sensor,
)
arduinoml::MultipleElementCondition_strategy = st.builds(
    arduinoml::MultipleElementCondition,
    operators=
        safe_text
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
NamedElement_strategy = st.builds(
    NamedElement,
)
arduinoml::Brick_strategy = st.builds(
    arduinoml::Brick,
    pin=
        safe_text
)
arduinoml::State_strategy = st.builds(
    arduinoml::State,
)
arduinoml::App_strategy = st.builds(
    arduinoml::App,
)
arduinoml::NamedElement_strategy = st.builds(
    arduinoml::NamedElement,
    name=
        safe_text
)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=arduinoml::BinaryAction_strategy)
@settings(max_examples=50)
def test_arduinoml::binaryaction_instantiation(instance):
    assert isinstance(instance, arduinoml::BinaryAction)

@given(instance=arduinoml::BinaryAction_strategy)
def test_arduinoml::binaryaction_actionValue_type(instance):
    assert isinstance(instance.actionValue, str)


@given(instance=arduinoml::BinaryAction_strategy)
def test_arduinoml::binaryaction_actionValue_setter(instance):
    original = instance.actionValue
    instance.actionValue = original
    assert instance.actionValue == original

@given(instance=arduinoml::AnalogAction_strategy)
@settings(max_examples=50)
def test_arduinoml::analogaction_instantiation(instance):
    assert isinstance(instance, arduinoml::AnalogAction)

@given(instance=arduinoml::AnalogAction_strategy)
def test_arduinoml::analogaction_actionValue_type(instance):
    assert isinstance(instance.actionValue, int)


@given(instance=arduinoml::AnalogAction_strategy)
def test_arduinoml::analogaction_actionValue_setter(instance):
    original = instance.actionValue
    instance.actionValue = original
    assert instance.actionValue == original

@given(instance=Actuator_strategy)
@settings(max_examples=50)
def test_actuator_instantiation(instance):
    assert isinstance(instance, Actuator)

@given(instance=arduinoml::BinaryActuator_strategy)
@settings(max_examples=50)
def test_arduinoml::binaryactuator_instantiation(instance):
    assert isinstance(instance, arduinoml::BinaryActuator)

@given(instance=arduinoml::AnalogActuator_strategy)
@settings(max_examples=50)
def test_arduinoml::analogactuator_instantiation(instance):
    assert isinstance(instance, arduinoml::AnalogActuator)

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)

@given(instance=arduinoml::AnalogSensor_strategy)
@settings(max_examples=50)
def test_arduinoml::analogsensor_instantiation(instance):
    assert isinstance(instance, arduinoml::AnalogSensor)

@given(instance=arduinoml::BinarySensor_strategy)
@settings(max_examples=50)
def test_arduinoml::binarysensor_instantiation(instance):
    assert isinstance(instance, arduinoml::BinarySensor)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=arduinoml::ValueElementCondition_strategy)
@settings(max_examples=50)
def test_arduinoml::valueelementcondition_instantiation(instance):
    assert isinstance(instance, arduinoml::ValueElementCondition)

@given(instance=arduinoml::ValueElementCondition_strategy)
def test_arduinoml::valueelementcondition_comparator_type(instance):
    assert isinstance(instance.comparator, str)


@given(instance=arduinoml::ValueElementCondition_strategy)
def test_arduinoml::valueelementcondition_comparator_setter(instance):
    original = instance.comparator
    instance.comparator = original
    assert instance.comparator == original

@given(instance=arduinoml::ValueElementCondition_strategy)
def test_arduinoml::valueelementcondition_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=arduinoml::ValueElementCondition_strategy)
def test_arduinoml::valueelementcondition_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arduinoml::SingleElementCondition_strategy)
@settings(max_examples=50)
def test_arduinoml::singleelementcondition_instantiation(instance):
    assert isinstance(instance, arduinoml::SingleElementCondition)

@given(instance=arduinoml::SingleElementCondition_strategy)
def test_arduinoml::singleelementcondition_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=arduinoml::SingleElementCondition_strategy)
def test_arduinoml::singleelementcondition_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arduinoml::Condition_strategy)
@settings(max_examples=50)
def test_arduinoml::condition_instantiation(instance):
    assert isinstance(instance, arduinoml::Condition)

@given(instance=Brick_strategy)
@settings(max_examples=50)
def test_brick_instantiation(instance):
    assert isinstance(instance, Brick)

@given(instance=arduinoml::Sensor_strategy)
@settings(max_examples=50)
def test_arduinoml::sensor_instantiation(instance):
    assert isinstance(instance, arduinoml::Sensor)

@given(instance=arduinoml::MultipleElementCondition_strategy)
@settings(max_examples=50)
def test_arduinoml::multipleelementcondition_instantiation(instance):
    assert isinstance(instance, arduinoml::MultipleElementCondition)

@given(instance=arduinoml::MultipleElementCondition_strategy)
def test_arduinoml::multipleelementcondition_operators_type(instance):
    assert isinstance(instance.operators, str)


@given(instance=arduinoml::MultipleElementCondition_strategy)
def test_arduinoml::multipleelementcondition_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

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

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=arduinoml::Brick_strategy)
@settings(max_examples=50)
def test_arduinoml::brick_instantiation(instance):
    assert isinstance(instance, arduinoml::Brick)

@given(instance=arduinoml::Brick_strategy)
def test_arduinoml::brick_pin_type(instance):
    assert isinstance(instance.pin, str)


@given(instance=arduinoml::Brick_strategy)
def test_arduinoml::brick_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original

@given(instance=arduinoml::State_strategy)
@settings(max_examples=50)
def test_arduinoml::state_instantiation(instance):
    assert isinstance(instance, arduinoml::State)

@given(instance=arduinoml::App_strategy)
@settings(max_examples=50)
def test_arduinoml::app_instantiation(instance):
    assert isinstance(instance, arduinoml::App)

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
