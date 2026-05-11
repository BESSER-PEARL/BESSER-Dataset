import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Condition,
    arduinoML::BaseCondition,
    arduinoML::Condition,
    arduinoML::NamedElement,
    arduinoML::BooleanCondition,
    NamedElement,
    arduinoML::Brick,
    arduinoML::SinkError,
    arduinoML::Transition,
    arduinoML::Action,
    arduinoML::State,
    arduinoML::App,
    Brick,
    arduinoML::Sensor,
    arduinoML::Actuator,
    Operator,
    Signal,
    Type,
    Comparator,
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



def test_arduinoml::basecondition_is_not_abstract():
    assert not inspect.isabstract(arduinoML::BaseCondition)


def test_arduinoml::basecondition_constructor_exists():
    assert callable(arduinoML::BaseCondition.__init__)


def test_arduinoml::basecondition_constructor_args():
    sig = inspect.signature(arduinoML::BaseCondition.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::condition_is_not_abstract():
    assert not inspect.isabstract(arduinoML::Condition)


def test_arduinoml::condition_constructor_exists():
    assert callable(arduinoML::Condition.__init__)


def test_arduinoml::condition_constructor_args():
    sig = inspect.signature(arduinoML::Condition.__init__)
    params = list(sig.parameters.keys())
    assert "comparator" in params, "Missing parameter 'comparator'"
    assert "analogvalue" in params, "Missing parameter 'analogvalue'"
    assert "value" in params, "Missing parameter 'value'"

def test_arduinoml::condition_has_comparator():
    assert hasattr(arduinoML::Condition, "comparator")
    descriptor = None
    for klass in arduinoML::Condition.__mro__:
        if "comparator" in klass.__dict__:
            descriptor = klass.__dict__["comparator"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml::condition_has_analogvalue():
    assert hasattr(arduinoML::Condition, "analogvalue")
    descriptor = None
    for klass in arduinoML::Condition.__mro__:
        if "analogvalue" in klass.__dict__:
            descriptor = klass.__dict__["analogvalue"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml::condition_has_value():
    assert hasattr(arduinoML::Condition, "value")
    descriptor = None
    for klass in arduinoML::Condition.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



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



def test_arduinoml::booleancondition_is_not_abstract():
    assert not inspect.isabstract(arduinoML::BooleanCondition)


def test_arduinoml::booleancondition_constructor_exists():
    assert callable(arduinoML::BooleanCondition.__init__)


def test_arduinoml::booleancondition_constructor_args():
    sig = inspect.signature(arduinoML::BooleanCondition.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_arduinoml::booleancondition_has_operator():
    assert hasattr(arduinoML::BooleanCondition, "operator")
    descriptor = None
    for klass in arduinoML::BooleanCondition.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_arduinoml::brick_is_not_abstract():
    assert not inspect.isabstract(arduinoML::Brick)


def test_arduinoml::brick_constructor_exists():
    assert callable(arduinoML::Brick.__init__)


def test_arduinoml::brick_constructor_args():
    sig = inspect.signature(arduinoML::Brick.__init__)
    params = list(sig.parameters.keys())
    assert "pin" in params, "Missing parameter 'pin'"
    assert "type" in params, "Missing parameter 'type'"

def test_arduinoml::brick_has_pin():
    assert hasattr(arduinoML::Brick, "pin")
    descriptor = None
    for klass in arduinoML::Brick.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml::brick_has_type():
    assert hasattr(arduinoML::Brick, "type")
    descriptor = None
    for klass in arduinoML::Brick.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_arduinoml::sinkerror_is_not_abstract():
    assert not inspect.isabstract(arduinoML::SinkError)


def test_arduinoml::sinkerror_constructor_exists():
    assert callable(arduinoML::SinkError.__init__)


def test_arduinoml::sinkerror_constructor_args():
    sig = inspect.signature(arduinoML::SinkError.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduinoml::sinkerror_has_value():
    assert hasattr(arduinoML::SinkError, "value")
    descriptor = None
    for klass in arduinoML::SinkError.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



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
    assert "analogvalue" in params, "Missing parameter 'analogvalue'"
    assert "value" in params, "Missing parameter 'value'"

def test_arduinoml::action_has_analogvalue():
    assert hasattr(arduinoML::Action, "analogvalue")
    descriptor = None
    for klass in arduinoML::Action.__mro__:
        if "analogvalue" in klass.__dict__:
            descriptor = klass.__dict__["analogvalue"]
            break
    assert isinstance(descriptor, property)

def test_arduinoml::action_has_value():
    assert hasattr(arduinoML::Action, "value")
    descriptor = None
    for klass in arduinoML::Action.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



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

def test_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "OR",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"

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

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "digital",
        "analog",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"

def test_comparator_exists():
    # Check that the Enumeration exists
    assert Comparator is not None

def test_comparator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Comparator]
    expected_literals = [
        "sup",
        "inf",
        "equ",
        "esup",
        "einf",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Comparator"


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
arduinoML::BaseCondition_strategy = st.builds(
    arduinoML::BaseCondition,
)
arduinoML::Condition_strategy = st.builds(
    arduinoML::Condition,
    comparator=
        safe_text,
    analogvalue=
        st.integers(),
    value=
        safe_text
)
arduinoML::NamedElement_strategy = st.builds(
    arduinoML::NamedElement,
    name=
        safe_text
)
arduinoML::BooleanCondition_strategy = st.builds(
    arduinoML::BooleanCondition,
    operator=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
arduinoML::Brick_strategy = st.builds(
    arduinoML::Brick,
    pin=
        st.integers(),
    type=
        safe_text
)
arduinoML::SinkError_strategy = st.builds(
    arduinoML::SinkError,
    value=
        st.integers()
)
arduinoML::Transition_strategy = st.builds(
    arduinoML::Transition,
)
arduinoML::Action_strategy = st.builds(
    arduinoML::Action,
    analogvalue=
        st.integers(),
    value=
        safe_text
)
arduinoML::State_strategy = st.builds(
    arduinoML::State,
)
arduinoML::App_strategy = st.builds(
    arduinoML::App,
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

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=arduinoML::BaseCondition_strategy)
@settings(max_examples=50)
def test_arduinoml::basecondition_instantiation(instance):
    assert isinstance(instance, arduinoML::BaseCondition)

@given(instance=arduinoML::Condition_strategy)
@settings(max_examples=50)
def test_arduinoml::condition_instantiation(instance):
    assert isinstance(instance, arduinoML::Condition)

@given(instance=arduinoML::Condition_strategy)
def test_arduinoml::condition_comparator_type(instance):
    assert isinstance(instance.comparator, str)


@given(instance=arduinoML::Condition_strategy)
def test_arduinoml::condition_comparator_setter(instance):
    original = instance.comparator
    instance.comparator = original
    assert instance.comparator == original

@given(instance=arduinoML::Condition_strategy)
def test_arduinoml::condition_analogvalue_type(instance):
    assert isinstance(instance.analogvalue, int)


@given(instance=arduinoML::Condition_strategy)
def test_arduinoml::condition_analogvalue_setter(instance):
    original = instance.analogvalue
    instance.analogvalue = original
    assert instance.analogvalue == original

@given(instance=arduinoML::Condition_strategy)
def test_arduinoml::condition_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=arduinoML::Condition_strategy)
def test_arduinoml::condition_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

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

@given(instance=arduinoML::BooleanCondition_strategy)
@settings(max_examples=50)
def test_arduinoml::booleancondition_instantiation(instance):
    assert isinstance(instance, arduinoML::BooleanCondition)

@given(instance=arduinoML::BooleanCondition_strategy)
def test_arduinoml::booleancondition_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=arduinoML::BooleanCondition_strategy)
def test_arduinoml::booleancondition_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

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

@given(instance=arduinoML::Brick_strategy)
def test_arduinoml::brick_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=arduinoML::Brick_strategy)
def test_arduinoml::brick_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=arduinoML::SinkError_strategy)
@settings(max_examples=50)
def test_arduinoml::sinkerror_instantiation(instance):
    assert isinstance(instance, arduinoML::SinkError)

@given(instance=arduinoML::SinkError_strategy)
def test_arduinoml::sinkerror_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=arduinoML::SinkError_strategy)
def test_arduinoml::sinkerror_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arduinoML::Transition_strategy)
@settings(max_examples=50)
def test_arduinoml::transition_instantiation(instance):
    assert isinstance(instance, arduinoML::Transition)

@given(instance=arduinoML::Action_strategy)
@settings(max_examples=50)
def test_arduinoml::action_instantiation(instance):
    assert isinstance(instance, arduinoML::Action)

@given(instance=arduinoML::Action_strategy)
def test_arduinoml::action_analogvalue_type(instance):
    assert isinstance(instance.analogvalue, int)


@given(instance=arduinoML::Action_strategy)
def test_arduinoml::action_analogvalue_setter(instance):
    original = instance.analogvalue
    instance.analogvalue = original
    assert instance.analogvalue == original

@given(instance=arduinoML::Action_strategy)
def test_arduinoml::action_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=arduinoML::Action_strategy)
def test_arduinoml::action_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arduinoML::State_strategy)
@settings(max_examples=50)
def test_arduinoml::state_instantiation(instance):
    assert isinstance(instance, arduinoML::State)

@given(instance=arduinoML::App_strategy)
@settings(max_examples=50)
def test_arduinoml::app_instantiation(instance):
    assert isinstance(instance, arduinoML::App)

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
