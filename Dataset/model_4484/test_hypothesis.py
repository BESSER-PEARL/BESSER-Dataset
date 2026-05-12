import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    behaviour_MovableObject,
    behaviour_FieldObject,
    Instruction,
    behaviour_While,
    behaviour_Lift,
    behaviour_SendMessage,
    behaviour_Instruct,
    behaviour_PlaceObject,
    behaviour_Pause,
    behaviour_MoveTo,
    behaviour_WaitForMessage,
    behaviour_Condition,
    behaviour_Choice,
    behaviour_Action,
    behaviour_PerformAction,
    behaviour_Drone,
    behaviour_Instruction,
    NamedElement,
    behaviour_DroneBehaviour,
    behaviour_NamedElement,
    ConditionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_behaviour_movableobject_is_not_abstract():
    assert not inspect.isabstract(behaviour_MovableObject)


def test_behaviour_movableobject_constructor_exists():
    assert callable(behaviour_MovableObject.__init__)


def test_behaviour_movableobject_constructor_args():
    sig = inspect.signature(behaviour_MovableObject.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_fieldobject_is_not_abstract():
    assert not inspect.isabstract(behaviour_FieldObject)


def test_behaviour_fieldobject_constructor_exists():
    assert callable(behaviour_FieldObject.__init__)


def test_behaviour_fieldobject_constructor_args():
    sig = inspect.signature(behaviour_FieldObject.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_while_is_not_abstract():
    assert not inspect.isabstract(behaviour_While)


def test_behaviour_while_constructor_exists():
    assert callable(behaviour_While.__init__)


def test_behaviour_while_constructor_args():
    sig = inspect.signature(behaviour_While.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_lift_is_not_abstract():
    assert not inspect.isabstract(behaviour_Lift)


def test_behaviour_lift_constructor_exists():
    assert callable(behaviour_Lift.__init__)


def test_behaviour_lift_constructor_args():
    sig = inspect.signature(behaviour_Lift.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_sendmessage_is_not_abstract():
    assert not inspect.isabstract(behaviour_SendMessage)


def test_behaviour_sendmessage_constructor_exists():
    assert callable(behaviour_SendMessage.__init__)


def test_behaviour_sendmessage_constructor_args():
    sig = inspect.signature(behaviour_SendMessage.__init__)
    params = list(sig.parameters.keys())
    assert "messageType" in params, "Missing parameter 'messageType'"

def test_behaviour_sendmessage_has_messageType():
    assert hasattr(behaviour_SendMessage, "messageType")
    descriptor = None
    for klass in behaviour_SendMessage.__mro__:
        if "messageType" in klass.__dict__:
            descriptor = klass.__dict__["messageType"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_instruct_is_not_abstract():
    assert not inspect.isabstract(behaviour_Instruct)


def test_behaviour_instruct_constructor_exists():
    assert callable(behaviour_Instruct.__init__)


def test_behaviour_instruct_constructor_args():
    sig = inspect.signature(behaviour_Instruct.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_placeobject_is_not_abstract():
    assert not inspect.isabstract(behaviour_PlaceObject)


def test_behaviour_placeobject_constructor_exists():
    assert callable(behaviour_PlaceObject.__init__)


def test_behaviour_placeobject_constructor_args():
    sig = inspect.signature(behaviour_PlaceObject.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_pause_is_not_abstract():
    assert not inspect.isabstract(behaviour_Pause)


def test_behaviour_pause_constructor_exists():
    assert callable(behaviour_Pause.__init__)


def test_behaviour_pause_constructor_args():
    sig = inspect.signature(behaviour_Pause.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"

def test_behaviour_pause_has_duration():
    assert hasattr(behaviour_Pause, "duration")
    descriptor = None
    for klass in behaviour_Pause.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_moveto_is_not_abstract():
    assert not inspect.isabstract(behaviour_MoveTo)


def test_behaviour_moveto_constructor_exists():
    assert callable(behaviour_MoveTo.__init__)


def test_behaviour_moveto_constructor_args():
    sig = inspect.signature(behaviour_MoveTo.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_waitformessage_is_not_abstract():
    assert not inspect.isabstract(behaviour_WaitForMessage)


def test_behaviour_waitformessage_constructor_exists():
    assert callable(behaviour_WaitForMessage.__init__)


def test_behaviour_waitformessage_constructor_args():
    sig = inspect.signature(behaviour_WaitForMessage.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "timeout" in params, "Missing parameter 'timeout'"

def test_behaviour_waitformessage_has_type():
    assert hasattr(behaviour_WaitForMessage, "type")
    descriptor = None
    for klass in behaviour_WaitForMessage.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_behaviour_waitformessage_has_timeout():
    assert hasattr(behaviour_WaitForMessage, "timeout")
    descriptor = None
    for klass in behaviour_WaitForMessage.__mro__:
        if "timeout" in klass.__dict__:
            descriptor = klass.__dict__["timeout"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_condition_is_not_abstract():
    assert not inspect.isabstract(behaviour_Condition)


def test_behaviour_condition_constructor_exists():
    assert callable(behaviour_Condition.__init__)


def test_behaviour_condition_constructor_args():
    sig = inspect.signature(behaviour_Condition.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_behaviour_condition_has_operation():
    assert hasattr(behaviour_Condition, "operation")
    descriptor = None
    for klass in behaviour_Condition.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)

def test_behaviour_condition_has_value():
    assert hasattr(behaviour_Condition, "value")
    descriptor = None
    for klass in behaviour_Condition.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_behaviour_condition_has_key():
    assert hasattr(behaviour_Condition, "key")
    descriptor = None
    for klass in behaviour_Condition.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_choice_is_not_abstract():
    assert not inspect.isabstract(behaviour_Choice)


def test_behaviour_choice_constructor_exists():
    assert callable(behaviour_Choice.__init__)


def test_behaviour_choice_constructor_args():
    sig = inspect.signature(behaviour_Choice.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_action_is_not_abstract():
    assert not inspect.isabstract(behaviour_Action)


def test_behaviour_action_constructor_exists():
    assert callable(behaviour_Action.__init__)


def test_behaviour_action_constructor_args():
    sig = inspect.signature(behaviour_Action.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_performaction_is_not_abstract():
    assert not inspect.isabstract(behaviour_PerformAction)


def test_behaviour_performaction_constructor_exists():
    assert callable(behaviour_PerformAction.__init__)


def test_behaviour_performaction_constructor_args():
    sig = inspect.signature(behaviour_PerformAction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_drone_is_not_abstract():
    assert not inspect.isabstract(behaviour_Drone)


def test_behaviour_drone_constructor_exists():
    assert callable(behaviour_Drone.__init__)


def test_behaviour_drone_constructor_args():
    sig = inspect.signature(behaviour_Drone.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_instruction_is_not_abstract():
    assert not inspect.isabstract(behaviour_Instruction)


def test_behaviour_instruction_constructor_exists():
    assert callable(behaviour_Instruction.__init__)


def test_behaviour_instruction_constructor_args():
    sig = inspect.signature(behaviour_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_dronebehaviour_is_not_abstract():
    assert not inspect.isabstract(behaviour_DroneBehaviour)


def test_behaviour_dronebehaviour_constructor_exists():
    assert callable(behaviour_DroneBehaviour.__init__)


def test_behaviour_dronebehaviour_constructor_args():
    sig = inspect.signature(behaviour_DroneBehaviour.__init__)
    params = list(sig.parameters.keys())
    assert "canBeInterrupted" in params, "Missing parameter 'canBeInterrupted'"

def test_behaviour_dronebehaviour_has_canBeInterrupted():
    assert hasattr(behaviour_DroneBehaviour, "canBeInterrupted")
    descriptor = None
    for klass in behaviour_DroneBehaviour.__mro__:
        if "canBeInterrupted" in klass.__dict__:
            descriptor = klass.__dict__["canBeInterrupted"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_namedelement_is_not_abstract():
    assert not inspect.isabstract(behaviour_NamedElement)


def test_behaviour_namedelement_constructor_exists():
    assert callable(behaviour_NamedElement.__init__)


def test_behaviour_namedelement_constructor_args():
    sig = inspect.signature(behaviour_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_behaviour_namedelement_has_name():
    assert hasattr(behaviour_NamedElement, "name")
    descriptor = None
    for klass in behaviour_NamedElement.__mro__:
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
        "GREATER_THAN",
        "LESSER_THAN",
        "NOT_EQUALS",
        "EQUALS",
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
behaviour_MovableObject_strategy = st.builds(
    behaviour_MovableObject,
)
behaviour_FieldObject_strategy = st.builds(
    behaviour_FieldObject,
)
Instruction_strategy = st.builds(
    Instruction,
)
behaviour_While_strategy = st.builds(
    behaviour_While,
)
behaviour_Lift_strategy = st.builds(
    behaviour_Lift,
)
behaviour_SendMessage_strategy = st.builds(
    behaviour_SendMessage,
    messageType=
        safe_text
)
behaviour_Instruct_strategy = st.builds(
    behaviour_Instruct,
)
behaviour_PlaceObject_strategy = st.builds(
    behaviour_PlaceObject,
)
behaviour_Pause_strategy = st.builds(
    behaviour_Pause,
    duration=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
behaviour_MoveTo_strategy = st.builds(
    behaviour_MoveTo,
)
behaviour_WaitForMessage_strategy = st.builds(
    behaviour_WaitForMessage,
    type=
        safe_text,
    timeout=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
behaviour_Condition_strategy = st.builds(
    behaviour_Condition,
    operation=
        safe_text,
    value=
        safe_text,
    key=
        safe_text
)
behaviour_Choice_strategy = st.builds(
    behaviour_Choice,
)
behaviour_Action_strategy = st.builds(
    behaviour_Action,
)
behaviour_PerformAction_strategy = st.builds(
    behaviour_PerformAction,
)
behaviour_Drone_strategy = st.builds(
    behaviour_Drone,
)
behaviour_Instruction_strategy = st.builds(
    behaviour_Instruction,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
behaviour_DroneBehaviour_strategy = st.builds(
    behaviour_DroneBehaviour,
    canBeInterrupted=
        st.booleans()
)
behaviour_NamedElement_strategy = st.builds(
    behaviour_NamedElement,
    name=
        safe_text
)

@given(instance=behaviour_MovableObject_strategy)
@settings(max_examples=50)
def test_behaviour_movableobject_instantiation(instance):
    assert isinstance(instance, behaviour_MovableObject)

@given(instance=behaviour_FieldObject_strategy)
@settings(max_examples=50)
def test_behaviour_fieldobject_instantiation(instance):
    assert isinstance(instance, behaviour_FieldObject)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=behaviour_While_strategy)
@settings(max_examples=50)
def test_behaviour_while_instantiation(instance):
    assert isinstance(instance, behaviour_While)

@given(instance=behaviour_Lift_strategy)
@settings(max_examples=50)
def test_behaviour_lift_instantiation(instance):
    assert isinstance(instance, behaviour_Lift)

@given(instance=behaviour_SendMessage_strategy)
@settings(max_examples=50)
def test_behaviour_sendmessage_instantiation(instance):
    assert isinstance(instance, behaviour_SendMessage)



@given(instance=behaviour_SendMessage_strategy)
def test_behaviour_sendmessage_messageType_setter(instance):
    original = instance.messageType
    instance.messageType = original
    assert instance.messageType == original

@given(instance=behaviour_Instruct_strategy)
@settings(max_examples=50)
def test_behaviour_instruct_instantiation(instance):
    assert isinstance(instance, behaviour_Instruct)

@given(instance=behaviour_PlaceObject_strategy)
@settings(max_examples=50)
def test_behaviour_placeobject_instantiation(instance):
    assert isinstance(instance, behaviour_PlaceObject)

@given(instance=behaviour_Pause_strategy)
@settings(max_examples=50)
def test_behaviour_pause_instantiation(instance):
    assert isinstance(instance, behaviour_Pause)



@given(instance=behaviour_Pause_strategy)
def test_behaviour_pause_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=behaviour_MoveTo_strategy)
@settings(max_examples=50)
def test_behaviour_moveto_instantiation(instance):
    assert isinstance(instance, behaviour_MoveTo)

@given(instance=behaviour_WaitForMessage_strategy)
@settings(max_examples=50)
def test_behaviour_waitformessage_instantiation(instance):
    assert isinstance(instance, behaviour_WaitForMessage)



@given(instance=behaviour_WaitForMessage_strategy)
def test_behaviour_waitformessage_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=behaviour_WaitForMessage_strategy)
def test_behaviour_waitformessage_timeout_setter(instance):
    original = instance.timeout
    instance.timeout = original
    assert instance.timeout == original

@given(instance=behaviour_Condition_strategy)
@settings(max_examples=50)
def test_behaviour_condition_instantiation(instance):
    assert isinstance(instance, behaviour_Condition)



@given(instance=behaviour_Condition_strategy)
def test_behaviour_condition_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original



@given(instance=behaviour_Condition_strategy)
def test_behaviour_condition_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=behaviour_Condition_strategy)
def test_behaviour_condition_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=behaviour_Choice_strategy)
@settings(max_examples=50)
def test_behaviour_choice_instantiation(instance):
    assert isinstance(instance, behaviour_Choice)

@given(instance=behaviour_Action_strategy)
@settings(max_examples=50)
def test_behaviour_action_instantiation(instance):
    assert isinstance(instance, behaviour_Action)

@given(instance=behaviour_PerformAction_strategy)
@settings(max_examples=50)
def test_behaviour_performaction_instantiation(instance):
    assert isinstance(instance, behaviour_PerformAction)

@given(instance=behaviour_Drone_strategy)
@settings(max_examples=50)
def test_behaviour_drone_instantiation(instance):
    assert isinstance(instance, behaviour_Drone)

@given(instance=behaviour_Instruction_strategy)
@settings(max_examples=50)
def test_behaviour_instruction_instantiation(instance):
    assert isinstance(instance, behaviour_Instruction)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=behaviour_DroneBehaviour_strategy)
@settings(max_examples=50)
def test_behaviour_dronebehaviour_instantiation(instance):
    assert isinstance(instance, behaviour_DroneBehaviour)



@given(instance=behaviour_DroneBehaviour_strategy)
def test_behaviour_dronebehaviour_canBeInterrupted_setter(instance):
    original = instance.canBeInterrupted
    instance.canBeInterrupted = original
    assert instance.canBeInterrupted == original

@given(instance=behaviour_NamedElement_strategy)
@settings(max_examples=50)
def test_behaviour_namedelement_instantiation(instance):
    assert isinstance(instance, behaviour_NamedElement)



@given(instance=behaviour_NamedElement_strategy)
def test_behaviour_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
