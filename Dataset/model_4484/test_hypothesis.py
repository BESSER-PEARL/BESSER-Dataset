import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    behaviour::MovableObject,
    behaviour::FieldObject,
    Instruction,
    behaviour::SendMessage,
    behaviour::While,
    behaviour::Instruct,
    behaviour::Pause,
    behaviour::PlaceObject,
    behaviour::Lift,
    behaviour::MoveTo,
    behaviour::WaitForMessage,
    behaviour::Condition,
    behaviour::Choice,
    behaviour::Action,
    behaviour::PerformAction,
    behaviour::Drone,
    behaviour::Instruction,
    NamedElement,
    behaviour::DroneBehaviour,
    behaviour::NamedElement,
    ConditionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_behaviour::movableobject_is_not_abstract():
    assert not inspect.isabstract(behaviour::MovableObject)


def test_behaviour::movableobject_constructor_exists():
    assert callable(behaviour::MovableObject.__init__)


def test_behaviour::movableobject_constructor_args():
    sig = inspect.signature(behaviour::MovableObject.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::fieldobject_is_not_abstract():
    assert not inspect.isabstract(behaviour::FieldObject)


def test_behaviour::fieldobject_constructor_exists():
    assert callable(behaviour::FieldObject.__init__)


def test_behaviour::fieldobject_constructor_args():
    sig = inspect.signature(behaviour::FieldObject.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::sendmessage_is_not_abstract():
    assert not inspect.isabstract(behaviour::SendMessage)


def test_behaviour::sendmessage_constructor_exists():
    assert callable(behaviour::SendMessage.__init__)


def test_behaviour::sendmessage_constructor_args():
    sig = inspect.signature(behaviour::SendMessage.__init__)
    params = list(sig.parameters.keys())
    assert "messageType" in params, "Missing parameter 'messageType'"

def test_behaviour::sendmessage_has_messageType():
    assert hasattr(behaviour::SendMessage, "messageType")
    descriptor = None
    for klass in behaviour::SendMessage.__mro__:
        if "messageType" in klass.__dict__:
            descriptor = klass.__dict__["messageType"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::while_is_not_abstract():
    assert not inspect.isabstract(behaviour::While)


def test_behaviour::while_constructor_exists():
    assert callable(behaviour::While.__init__)


def test_behaviour::while_constructor_args():
    sig = inspect.signature(behaviour::While.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::instruct_is_not_abstract():
    assert not inspect.isabstract(behaviour::Instruct)


def test_behaviour::instruct_constructor_exists():
    assert callable(behaviour::Instruct.__init__)


def test_behaviour::instruct_constructor_args():
    sig = inspect.signature(behaviour::Instruct.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::pause_is_not_abstract():
    assert not inspect.isabstract(behaviour::Pause)


def test_behaviour::pause_constructor_exists():
    assert callable(behaviour::Pause.__init__)


def test_behaviour::pause_constructor_args():
    sig = inspect.signature(behaviour::Pause.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"

def test_behaviour::pause_has_duration():
    assert hasattr(behaviour::Pause, "duration")
    descriptor = None
    for klass in behaviour::Pause.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::placeobject_is_not_abstract():
    assert not inspect.isabstract(behaviour::PlaceObject)


def test_behaviour::placeobject_constructor_exists():
    assert callable(behaviour::PlaceObject.__init__)


def test_behaviour::placeobject_constructor_args():
    sig = inspect.signature(behaviour::PlaceObject.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::lift_is_not_abstract():
    assert not inspect.isabstract(behaviour::Lift)


def test_behaviour::lift_constructor_exists():
    assert callable(behaviour::Lift.__init__)


def test_behaviour::lift_constructor_args():
    sig = inspect.signature(behaviour::Lift.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::moveto_is_not_abstract():
    assert not inspect.isabstract(behaviour::MoveTo)


def test_behaviour::moveto_constructor_exists():
    assert callable(behaviour::MoveTo.__init__)


def test_behaviour::moveto_constructor_args():
    sig = inspect.signature(behaviour::MoveTo.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::waitformessage_is_not_abstract():
    assert not inspect.isabstract(behaviour::WaitForMessage)


def test_behaviour::waitformessage_constructor_exists():
    assert callable(behaviour::WaitForMessage.__init__)


def test_behaviour::waitformessage_constructor_args():
    sig = inspect.signature(behaviour::WaitForMessage.__init__)
    params = list(sig.parameters.keys())
    assert "timeout" in params, "Missing parameter 'timeout'"
    assert "type" in params, "Missing parameter 'type'"

def test_behaviour::waitformessage_has_timeout():
    assert hasattr(behaviour::WaitForMessage, "timeout")
    descriptor = None
    for klass in behaviour::WaitForMessage.__mro__:
        if "timeout" in klass.__dict__:
            descriptor = klass.__dict__["timeout"]
            break
    assert isinstance(descriptor, property)

def test_behaviour::waitformessage_has_type():
    assert hasattr(behaviour::WaitForMessage, "type")
    descriptor = None
    for klass in behaviour::WaitForMessage.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::condition_is_not_abstract():
    assert not inspect.isabstract(behaviour::Condition)


def test_behaviour::condition_constructor_exists():
    assert callable(behaviour::Condition.__init__)


def test_behaviour::condition_constructor_args():
    sig = inspect.signature(behaviour::Condition.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "operation" in params, "Missing parameter 'operation'"
    assert "key" in params, "Missing parameter 'key'"

def test_behaviour::condition_has_value():
    assert hasattr(behaviour::Condition, "value")
    descriptor = None
    for klass in behaviour::Condition.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_behaviour::condition_has_operation():
    assert hasattr(behaviour::Condition, "operation")
    descriptor = None
    for klass in behaviour::Condition.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)

def test_behaviour::condition_has_key():
    assert hasattr(behaviour::Condition, "key")
    descriptor = None
    for klass in behaviour::Condition.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::choice_is_not_abstract():
    assert not inspect.isabstract(behaviour::Choice)


def test_behaviour::choice_constructor_exists():
    assert callable(behaviour::Choice.__init__)


def test_behaviour::choice_constructor_args():
    sig = inspect.signature(behaviour::Choice.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::action_is_not_abstract():
    assert not inspect.isabstract(behaviour::Action)


def test_behaviour::action_constructor_exists():
    assert callable(behaviour::Action.__init__)


def test_behaviour::action_constructor_args():
    sig = inspect.signature(behaviour::Action.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::performaction_is_not_abstract():
    assert not inspect.isabstract(behaviour::PerformAction)


def test_behaviour::performaction_constructor_exists():
    assert callable(behaviour::PerformAction.__init__)


def test_behaviour::performaction_constructor_args():
    sig = inspect.signature(behaviour::PerformAction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::drone_is_not_abstract():
    assert not inspect.isabstract(behaviour::Drone)


def test_behaviour::drone_constructor_exists():
    assert callable(behaviour::Drone.__init__)


def test_behaviour::drone_constructor_args():
    sig = inspect.signature(behaviour::Drone.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::instruction_is_not_abstract():
    assert not inspect.isabstract(behaviour::Instruction)


def test_behaviour::instruction_constructor_exists():
    assert callable(behaviour::Instruction.__init__)


def test_behaviour::instruction_constructor_args():
    sig = inspect.signature(behaviour::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::dronebehaviour_is_not_abstract():
    assert not inspect.isabstract(behaviour::DroneBehaviour)


def test_behaviour::dronebehaviour_constructor_exists():
    assert callable(behaviour::DroneBehaviour.__init__)


def test_behaviour::dronebehaviour_constructor_args():
    sig = inspect.signature(behaviour::DroneBehaviour.__init__)
    params = list(sig.parameters.keys())
    assert "canBeInterrupted" in params, "Missing parameter 'canBeInterrupted'"

def test_behaviour::dronebehaviour_has_canBeInterrupted():
    assert hasattr(behaviour::DroneBehaviour, "canBeInterrupted")
    descriptor = None
    for klass in behaviour::DroneBehaviour.__mro__:
        if "canBeInterrupted" in klass.__dict__:
            descriptor = klass.__dict__["canBeInterrupted"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::namedelement_is_not_abstract():
    assert not inspect.isabstract(behaviour::NamedElement)


def test_behaviour::namedelement_constructor_exists():
    assert callable(behaviour::NamedElement.__init__)


def test_behaviour::namedelement_constructor_args():
    sig = inspect.signature(behaviour::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_behaviour::namedelement_has_name():
    assert hasattr(behaviour::NamedElement, "name")
    descriptor = None
    for klass in behaviour::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_conditionkind_exists():
    # Check that the Enumeration exists
    assert ConditionKind is not None

def test_conditionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConditionKind]
    expected_literals = [
        "LESSER_THAN",
        "GREATER_THAN",
        "EQUALS",
        "NOT_EQUALS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConditionKind"


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
behaviour::MovableObject_strategy = st.builds(
    behaviour::MovableObject,
)
behaviour::FieldObject_strategy = st.builds(
    behaviour::FieldObject,
)
Instruction_strategy = st.builds(
    Instruction,
)
behaviour::SendMessage_strategy = st.builds(
    behaviour::SendMessage,
    messageType=
        safe_text
)
behaviour::While_strategy = st.builds(
    behaviour::While,
)
behaviour::Instruct_strategy = st.builds(
    behaviour::Instruct,
)
behaviour::Pause_strategy = st.builds(
    behaviour::Pause,
    duration=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
behaviour::PlaceObject_strategy = st.builds(
    behaviour::PlaceObject,
)
behaviour::Lift_strategy = st.builds(
    behaviour::Lift,
)
behaviour::MoveTo_strategy = st.builds(
    behaviour::MoveTo,
)
behaviour::WaitForMessage_strategy = st.builds(
    behaviour::WaitForMessage,
    timeout=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        safe_text
)
behaviour::Condition_strategy = st.builds(
    behaviour::Condition,
    value=
        safe_text,
    operation=
        safe_text,
    key=
        safe_text
)
behaviour::Choice_strategy = st.builds(
    behaviour::Choice,
)
behaviour::Action_strategy = st.builds(
    behaviour::Action,
)
behaviour::PerformAction_strategy = st.builds(
    behaviour::PerformAction,
)
behaviour::Drone_strategy = st.builds(
    behaviour::Drone,
)
behaviour::Instruction_strategy = st.builds(
    behaviour::Instruction,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
behaviour::DroneBehaviour_strategy = st.builds(
    behaviour::DroneBehaviour,
    canBeInterrupted=
        st.booleans()
)
behaviour::NamedElement_strategy = st.builds(
    behaviour::NamedElement,
    name=
        safe_text
)

@given(instance=behaviour::MovableObject_strategy)
@settings(max_examples=50)
def test_behaviour::movableobject_instantiation(instance):
    assert isinstance(instance, behaviour::MovableObject)

@given(instance=behaviour::FieldObject_strategy)
@settings(max_examples=50)
def test_behaviour::fieldobject_instantiation(instance):
    assert isinstance(instance, behaviour::FieldObject)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=behaviour::SendMessage_strategy)
@settings(max_examples=50)
def test_behaviour::sendmessage_instantiation(instance):
    assert isinstance(instance, behaviour::SendMessage)

@given(instance=behaviour::SendMessage_strategy)
def test_behaviour::sendmessage_messageType_type(instance):
    assert isinstance(instance.messageType, str)


@given(instance=behaviour::SendMessage_strategy)
def test_behaviour::sendmessage_messageType_setter(instance):
    original = instance.messageType
    instance.messageType = original
    assert instance.messageType == original

@given(instance=behaviour::While_strategy)
@settings(max_examples=50)
def test_behaviour::while_instantiation(instance):
    assert isinstance(instance, behaviour::While)

@given(instance=behaviour::Instruct_strategy)
@settings(max_examples=50)
def test_behaviour::instruct_instantiation(instance):
    assert isinstance(instance, behaviour::Instruct)

@given(instance=behaviour::Pause_strategy)
@settings(max_examples=50)
def test_behaviour::pause_instantiation(instance):
    assert isinstance(instance, behaviour::Pause)

@given(instance=behaviour::Pause_strategy)
def test_behaviour::pause_duration_type(instance):
    assert isinstance(instance.duration, float)


@given(instance=behaviour::Pause_strategy)
def test_behaviour::pause_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=behaviour::PlaceObject_strategy)
@settings(max_examples=50)
def test_behaviour::placeobject_instantiation(instance):
    assert isinstance(instance, behaviour::PlaceObject)

@given(instance=behaviour::Lift_strategy)
@settings(max_examples=50)
def test_behaviour::lift_instantiation(instance):
    assert isinstance(instance, behaviour::Lift)

@given(instance=behaviour::MoveTo_strategy)
@settings(max_examples=50)
def test_behaviour::moveto_instantiation(instance):
    assert isinstance(instance, behaviour::MoveTo)

@given(instance=behaviour::WaitForMessage_strategy)
@settings(max_examples=50)
def test_behaviour::waitformessage_instantiation(instance):
    assert isinstance(instance, behaviour::WaitForMessage)

@given(instance=behaviour::WaitForMessage_strategy)
def test_behaviour::waitformessage_timeout_type(instance):
    assert isinstance(instance.timeout, float)


@given(instance=behaviour::WaitForMessage_strategy)
def test_behaviour::waitformessage_timeout_setter(instance):
    original = instance.timeout
    instance.timeout = original
    assert instance.timeout == original

@given(instance=behaviour::WaitForMessage_strategy)
def test_behaviour::waitformessage_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=behaviour::WaitForMessage_strategy)
def test_behaviour::waitformessage_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=behaviour::Condition_strategy)
@settings(max_examples=50)
def test_behaviour::condition_instantiation(instance):
    assert isinstance(instance, behaviour::Condition)

@given(instance=behaviour::Condition_strategy)
def test_behaviour::condition_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=behaviour::Condition_strategy)
def test_behaviour::condition_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=behaviour::Condition_strategy)
def test_behaviour::condition_operation_type(instance):
    assert isinstance(instance.operation, str)


@given(instance=behaviour::Condition_strategy)
def test_behaviour::condition_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=behaviour::Condition_strategy)
def test_behaviour::condition_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=behaviour::Condition_strategy)
def test_behaviour::condition_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=behaviour::Choice_strategy)
@settings(max_examples=50)
def test_behaviour::choice_instantiation(instance):
    assert isinstance(instance, behaviour::Choice)

@given(instance=behaviour::Action_strategy)
@settings(max_examples=50)
def test_behaviour::action_instantiation(instance):
    assert isinstance(instance, behaviour::Action)

@given(instance=behaviour::PerformAction_strategy)
@settings(max_examples=50)
def test_behaviour::performaction_instantiation(instance):
    assert isinstance(instance, behaviour::PerformAction)

@given(instance=behaviour::Drone_strategy)
@settings(max_examples=50)
def test_behaviour::drone_instantiation(instance):
    assert isinstance(instance, behaviour::Drone)

@given(instance=behaviour::Instruction_strategy)
@settings(max_examples=50)
def test_behaviour::instruction_instantiation(instance):
    assert isinstance(instance, behaviour::Instruction)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=behaviour::DroneBehaviour_strategy)
@settings(max_examples=50)
def test_behaviour::dronebehaviour_instantiation(instance):
    assert isinstance(instance, behaviour::DroneBehaviour)

@given(instance=behaviour::DroneBehaviour_strategy)
def test_behaviour::dronebehaviour_canBeInterrupted_type(instance):
    assert isinstance(instance.canBeInterrupted, bool)


@given(instance=behaviour::DroneBehaviour_strategy)
def test_behaviour::dronebehaviour_canBeInterrupted_setter(instance):
    original = instance.canBeInterrupted
    instance.canBeInterrupted = original
    assert instance.canBeInterrupted == original

@given(instance=behaviour::NamedElement_strategy)
@settings(max_examples=50)
def test_behaviour::namedelement_instantiation(instance):
    assert isinstance(instance, behaviour::NamedElement)

@given(instance=behaviour::NamedElement_strategy)
def test_behaviour::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=behaviour::NamedElement_strategy)
def test_behaviour::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
