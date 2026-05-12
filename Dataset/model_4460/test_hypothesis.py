import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Condition,
    arduinoml_SimpleCondition,
    arduinoml_MultipleCondition,
    arduinoml_Transition,
    NamedElement,
    arduinoml_Brick,
    arduinoml_Condition,
    arduinoml_State,
    arduinoml_App,
    arduinoml_NamedElement,
    arduinoml_Action,
    Brick,
    arduinoml_Actuator,
    arduinoml_Sensor,
    COMPARATOR,
    OPERATOR,
    BrickType,
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



def test_arduinoml_simplecondition_is_not_abstract():
    assert not inspect.isabstract(arduinoml_SimpleCondition)


def test_arduinoml_simplecondition_constructor_exists():
    assert callable(arduinoml_SimpleCondition.__init__)


def test_arduinoml_simplecondition_constructor_args():
    sig = inspect.signature(arduinoml_SimpleCondition.__init__)
    params = list(sig.parameters.keys())
    assert "comparator" in params, "Missing parameter 'comparator'"
    assert "value" in params, "Missing parameter 'value'"

def test_arduinoml_simplecondition_has_comparator():
    assert hasattr(arduinoml_SimpleCondition, "comparator")
    descriptor = None
    for klass in arduinoml_SimpleCondition.__mro__:
        if "comparator" in klass.__dict__:
            descriptor = klass.__dict__["comparator"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml_simplecondition_has_value():
    assert hasattr(arduinoml_SimpleCondition, "value")
    descriptor = None
    for klass in arduinoml_SimpleCondition.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml_multiplecondition_is_not_abstract():
    assert not inspect.isabstract(arduinoml_MultipleCondition)


def test_arduinoml_multiplecondition_constructor_exists():
    assert callable(arduinoml_MultipleCondition.__init__)


def test_arduinoml_multiplecondition_constructor_args():
    sig = inspect.signature(arduinoml_MultipleCondition.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_arduinoml_multiplecondition_has_operators():
    assert hasattr(arduinoml_MultipleCondition, "operators")
    descriptor = None
    for klass in arduinoml_MultipleCondition.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



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



def test_arduinoml_brick_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Brick)


def test_arduinoml_brick_constructor_exists():
    assert callable(arduinoml_Brick.__init__)


def test_arduinoml_brick_constructor_args():
    sig = inspect.signature(arduinoml_Brick.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "pin" in params, "Missing parameter 'pin'"

def test_arduinoml_brick_has_type():
    assert hasattr(arduinoml_Brick, "type")
    descriptor = None
    for klass in arduinoml_Brick.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml_brick_has_pin():
    assert hasattr(arduinoml_Brick, "pin")
    descriptor = None
    for klass in arduinoml_Brick.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml_condition_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Condition)


def test_arduinoml_condition_constructor_exists():
    assert callable(arduinoml_Condition.__init__)


def test_arduinoml_condition_constructor_args():
    sig = inspect.signature(arduinoml_Condition.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_state_is_not_abstract():
    assert not inspect.isabstract(arduinoml_State)


def test_arduinoml_state_constructor_exists():
    assert callable(arduinoml_State.__init__)


def test_arduinoml_state_constructor_args():
    sig = inspect.signature(arduinoml_State.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_app_is_not_abstract():
    assert not inspect.isabstract(arduinoml_App)


def test_arduinoml_app_constructor_exists():
    assert callable(arduinoml_App.__init__)


def test_arduinoml_app_constructor_args():
    sig = inspect.signature(arduinoml_App.__init__)
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



def test_arduinoml_action_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Action)


def test_arduinoml_action_constructor_exists():
    assert callable(arduinoml_Action.__init__)


def test_arduinoml_action_constructor_args():
    sig = inspect.signature(arduinoml_Action.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduinoml_action_has_value():
    assert hasattr(arduinoml_Action, "value")
    descriptor = None
    for klass in arduinoml_Action.__mro__:
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



def test_arduinoml_actuator_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Actuator)


def test_arduinoml_actuator_constructor_exists():
    assert callable(arduinoml_Actuator.__init__)


def test_arduinoml_actuator_constructor_args():
    sig = inspect.signature(arduinoml_Actuator.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml_sensor_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Sensor)


def test_arduinoml_sensor_constructor_exists():
    assert callable(arduinoml_Sensor.__init__)


def test_arduinoml_sensor_constructor_args():
    sig = inspect.signature(arduinoml_Sensor.__init__)
    params = list(sig.parameters.keys())

def test_comparator_exists():
    # Check that the Enumeration exists
    assert COMPARATOR is not None

def test_comparator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in COMPARATOR]
    expected_literals = [
        "SUPERIOR_OR_EQUALS",
        "EQUALS",
        "INFERIOR_OR_EQUALS",
        "NON_EQUALS",
        "INFERIOR",
        "SUPERIOR",
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
        "OR",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OPERATOR"

def test_bricktype_exists():
    # Check that the Enumeration exists
    assert BrickType is not None

def test_bricktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BrickType]
    expected_literals = [
        "ANALOGICAL",
        "DIGITAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BrickType"


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
arduinoml_SimpleCondition_strategy = st.builds(
    arduinoml_SimpleCondition,
    comparator=
        safe_text,
    value=
        safe_text
)
arduinoml_MultipleCondition_strategy = st.builds(
    arduinoml_MultipleCondition,
    operators=
        safe_text
)
arduinoml_Transition_strategy = st.builds(
    arduinoml_Transition,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
arduinoml_Brick_strategy = st.builds(
    arduinoml_Brick,
    type=
        safe_text,
    pin=
        st.integers()
)
arduinoml_Condition_strategy = st.builds(
    arduinoml_Condition,
)
arduinoml_State_strategy = st.builds(
    arduinoml_State,
)
arduinoml_App_strategy = st.builds(
    arduinoml_App,
)
arduinoml_NamedElement_strategy = st.builds(
    arduinoml_NamedElement,
    name=
        safe_text
)
arduinoml_Action_strategy = st.builds(
    arduinoml_Action,
    value=
        safe_text
)
Brick_strategy = st.builds(
    Brick,
)
arduinoml_Actuator_strategy = st.builds(
    arduinoml_Actuator,
)
arduinoml_Sensor_strategy = st.builds(
    arduinoml_Sensor,
)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=arduinoml_SimpleCondition_strategy)
@settings(max_examples=50)
def test_arduinoml_simplecondition_instantiation(instance):
    assert isinstance(instance, arduinoml_SimpleCondition)



@given(instance=arduinoml_SimpleCondition_strategy)
def test_arduinoml_simplecondition_comparator_setter(instance):
    original = instance.comparator
    instance.comparator = original
    assert instance.comparator == original



@given(instance=arduinoml_SimpleCondition_strategy)
def test_arduinoml_simplecondition_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arduinoml_MultipleCondition_strategy)
@settings(max_examples=50)
def test_arduinoml_multiplecondition_instantiation(instance):
    assert isinstance(instance, arduinoml_MultipleCondition)



@given(instance=arduinoml_MultipleCondition_strategy)
def test_arduinoml_multiplecondition_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=arduinoml_Transition_strategy)
@settings(max_examples=50)
def test_arduinoml_transition_instantiation(instance):
    assert isinstance(instance, arduinoml_Transition)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=arduinoml_Brick_strategy)
@settings(max_examples=50)
def test_arduinoml_brick_instantiation(instance):
    assert isinstance(instance, arduinoml_Brick)



@given(instance=arduinoml_Brick_strategy)
def test_arduinoml_brick_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=arduinoml_Brick_strategy)
def test_arduinoml_brick_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original

@given(instance=arduinoml_Condition_strategy)
@settings(max_examples=50)
def test_arduinoml_condition_instantiation(instance):
    assert isinstance(instance, arduinoml_Condition)

@given(instance=arduinoml_State_strategy)
@settings(max_examples=50)
def test_arduinoml_state_instantiation(instance):
    assert isinstance(instance, arduinoml_State)

@given(instance=arduinoml_App_strategy)
@settings(max_examples=50)
def test_arduinoml_app_instantiation(instance):
    assert isinstance(instance, arduinoml_App)

@given(instance=arduinoml_NamedElement_strategy)
@settings(max_examples=50)
def test_arduinoml_namedelement_instantiation(instance):
    assert isinstance(instance, arduinoml_NamedElement)



@given(instance=arduinoml_NamedElement_strategy)
def test_arduinoml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduinoml_Action_strategy)
@settings(max_examples=50)
def test_arduinoml_action_instantiation(instance):
    assert isinstance(instance, arduinoml_Action)



@given(instance=arduinoml_Action_strategy)
def test_arduinoml_action_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Brick_strategy)
@settings(max_examples=50)
def test_brick_instantiation(instance):
    assert isinstance(instance, Brick)

@given(instance=arduinoml_Actuator_strategy)
@settings(max_examples=50)
def test_arduinoml_actuator_instantiation(instance):
    assert isinstance(instance, arduinoml_Actuator)

@given(instance=arduinoml_Sensor_strategy)
@settings(max_examples=50)
def test_arduinoml_sensor_instantiation(instance):
    assert isinstance(instance, arduinoml_Sensor)
