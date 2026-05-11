import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Condition,
    arduinoml::SimpleCondition,
    arduinoml::MultipleCondition,
    arduinoml::Transition,
    NamedElement,
    arduinoml::State,
    arduinoml::Condition,
    arduinoml::Brick,
    arduinoml::App,
    arduinoml::NamedElement,
    arduinoml::Action,
    Brick,
    arduinoml::Actuator,
    arduinoml::Sensor,
    BrickType,
    OPERATOR,
    COMPARATOR,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::simplecondition_is_not_abstract():
    assert not inspect.isabstract(arduinoml::SimpleCondition)


def test_arduinoml::simplecondition_constructor_exists():
    assert callable(arduinoml::SimpleCondition.__init__)


def test_arduinoml::simplecondition_constructor_args():
    sig = inspect.signature(arduinoml::SimpleCondition.__init__)
    params = list(sig.parameters.keys())
    assert "comparator" in params, "Missing parameter 'comparator'"
    assert "value" in params, "Missing parameter 'value'"

def test_arduinoml::simplecondition_has_comparator():
    assert hasattr(arduinoml::SimpleCondition, "comparator")
    descriptor = None
    for klass in arduinoml::SimpleCondition.__mro__:
        if "comparator" in klass.__dict__:
            descriptor = klass.__dict__["comparator"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml::simplecondition_has_value():
    assert hasattr(arduinoml::SimpleCondition, "value")
    descriptor = None
    for klass in arduinoml::SimpleCondition.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml::multiplecondition_is_not_abstract():
    assert not inspect.isabstract(arduinoml::MultipleCondition)


def test_arduinoml::multiplecondition_constructor_exists():
    assert callable(arduinoml::MultipleCondition.__init__)


def test_arduinoml::multiplecondition_constructor_args():
    sig = inspect.signature(arduinoml::MultipleCondition.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_arduinoml::multiplecondition_has_operators():
    assert hasattr(arduinoml::MultipleCondition, "operators")
    descriptor = None
    for klass in arduinoml::MultipleCondition.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



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



def test_arduinoml::state_is_not_abstract():
    assert not inspect.isabstract(arduinoml::State)


def test_arduinoml::state_constructor_exists():
    assert callable(arduinoml::State.__init__)


def test_arduinoml::state_constructor_args():
    sig = inspect.signature(arduinoml::State.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::condition_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Condition)


def test_arduinoml::condition_constructor_exists():
    assert callable(arduinoml::Condition.__init__)


def test_arduinoml::condition_constructor_args():
    sig = inspect.signature(arduinoml::Condition.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::brick_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Brick)


def test_arduinoml::brick_constructor_exists():
    assert callable(arduinoml::Brick.__init__)


def test_arduinoml::brick_constructor_args():
    sig = inspect.signature(arduinoml::Brick.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "pin" in params, "Missing parameter 'pin'"

def test_arduinoml::brick_has_type():
    assert hasattr(arduinoml::Brick, "type")
    descriptor = None
    for klass in arduinoml::Brick.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml::brick_has_pin():
    assert hasattr(arduinoml::Brick, "pin")
    descriptor = None
    for klass in arduinoml::Brick.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)



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



def test_arduinoml::action_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Action)


def test_arduinoml::action_constructor_exists():
    assert callable(arduinoml::Action.__init__)


def test_arduinoml::action_constructor_args():
    sig = inspect.signature(arduinoml::Action.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduinoml::action_has_value():
    assert hasattr(arduinoml::Action, "value")
    descriptor = None
    for klass in arduinoml::Action.__mro__:
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



def test_arduinoml::actuator_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Actuator)


def test_arduinoml::actuator_constructor_exists():
    assert callable(arduinoml::Actuator.__init__)


def test_arduinoml::actuator_constructor_args():
    sig = inspect.signature(arduinoml::Actuator.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::sensor_is_not_abstract():
    assert not inspect.isabstract(arduinoml::Sensor)


def test_arduinoml::sensor_constructor_exists():
    assert callable(arduinoml::Sensor.__init__)


def test_arduinoml::sensor_constructor_args():
    sig = inspect.signature(arduinoml::Sensor.__init__)
    params = list(sig.parameters.keys())

def test_bricktype_exists():
    # Check that the Enumeration exists
    assert BrickType is not None

def test_bricktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BrickType]
    expected_literals = [
        "DIGITAL",
        "ANALOGICAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BrickType"

def test_operator_exists():
    # Check that the Enumeration exists
    assert OPERATOR is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OPERATOR]
    expected_literals = [
        "OR",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OPERATOR"

def test_comparator_exists():
    # Check that the Enumeration exists
    assert COMPARATOR is not None

def test_comparator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in COMPARATOR]
    expected_literals = [
        "INFERIOR",
        "INFERIOR_OR_EQUALS",
        "EQUALS",
        "SUPERIOR",
        "SUPERIOR_OR_EQUALS",
        "NON_EQUALS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in COMPARATOR"


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
Condition_strategy = st.builds(
    Condition,
)
arduinoml::SimpleCondition_strategy = st.builds(
    arduinoml::SimpleCondition,
    comparator=
        safe_text,
    value=
        safe_text
)
arduinoml::MultipleCondition_strategy = st.builds(
    arduinoml::MultipleCondition,
    operators=
        safe_text
)
arduinoml::Transition_strategy = st.builds(
    arduinoml::Transition,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
arduinoml::State_strategy = st.builds(
    arduinoml::State,
)
arduinoml::Condition_strategy = st.builds(
    arduinoml::Condition,
)
arduinoml::Brick_strategy = st.builds(
    arduinoml::Brick,
    type=
        safe_text,
    pin=
        st.integers()
)
arduinoml::App_strategy = st.builds(
    arduinoml::App,
)
arduinoml::NamedElement_strategy = st.builds(
    arduinoml::NamedElement,
    name=
        safe_text
)
arduinoml::Action_strategy = st.builds(
    arduinoml::Action,
    value=
        safe_text
)
Brick_strategy = st.builds(
    Brick,
)
arduinoml::Actuator_strategy = st.builds(
    arduinoml::Actuator,
)
arduinoml::Sensor_strategy = st.builds(
    arduinoml::Sensor,
)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=arduinoml::SimpleCondition_strategy)
@settings(max_examples=50)
def test_arduinoml::simplecondition_instantiation(instance):
    assert isinstance(instance, arduinoml::SimpleCondition)

@given(instance=arduinoml::SimpleCondition_strategy)
def test_arduinoml::simplecondition_comparator_type(instance):
    assert isinstance(instance.comparator, str)


@given(instance=arduinoml::SimpleCondition_strategy)
def test_arduinoml::simplecondition_comparator_setter(instance):
    original = instance.comparator
    instance.comparator = original
    assert instance.comparator == original

@given(instance=arduinoml::SimpleCondition_strategy)
def test_arduinoml::simplecondition_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=arduinoml::SimpleCondition_strategy)
def test_arduinoml::simplecondition_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arduinoml::MultipleCondition_strategy)
@settings(max_examples=50)
def test_arduinoml::multiplecondition_instantiation(instance):
    assert isinstance(instance, arduinoml::MultipleCondition)

@given(instance=arduinoml::MultipleCondition_strategy)
def test_arduinoml::multiplecondition_operators_type(instance):
    assert isinstance(instance.operators, str)


@given(instance=arduinoml::MultipleCondition_strategy)
def test_arduinoml::multiplecondition_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=arduinoml::Transition_strategy)
@settings(max_examples=50)
def test_arduinoml::transition_instantiation(instance):
    assert isinstance(instance, arduinoml::Transition)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=arduinoml::State_strategy)
@settings(max_examples=50)
def test_arduinoml::state_instantiation(instance):
    assert isinstance(instance, arduinoml::State)

@given(instance=arduinoml::Condition_strategy)
@settings(max_examples=50)
def test_arduinoml::condition_instantiation(instance):
    assert isinstance(instance, arduinoml::Condition)

@given(instance=arduinoml::Brick_strategy)
@settings(max_examples=50)
def test_arduinoml::brick_instantiation(instance):
    assert isinstance(instance, arduinoml::Brick)

@given(instance=arduinoml::Brick_strategy)
def test_arduinoml::brick_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=arduinoml::Brick_strategy)
def test_arduinoml::brick_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=arduinoml::Brick_strategy)
def test_arduinoml::brick_pin_type(instance):
    assert isinstance(instance.pin, int)


@given(instance=arduinoml::Brick_strategy)
def test_arduinoml::brick_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original

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

@given(instance=arduinoml::Action_strategy)
@settings(max_examples=50)
def test_arduinoml::action_instantiation(instance):
    assert isinstance(instance, arduinoml::Action)

@given(instance=arduinoml::Action_strategy)
def test_arduinoml::action_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=arduinoml::Action_strategy)
def test_arduinoml::action_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Brick_strategy)
@settings(max_examples=50)
def test_brick_instantiation(instance):
    assert isinstance(instance, Brick)

@given(instance=arduinoml::Actuator_strategy)
@settings(max_examples=50)
def test_arduinoml::actuator_instantiation(instance):
    assert isinstance(instance, arduinoml::Actuator)

@given(instance=arduinoml::Sensor_strategy)
@settings(max_examples=50)
def test_arduinoml::sensor_instantiation(instance):
    assert isinstance(instance, arduinoml::Sensor)
