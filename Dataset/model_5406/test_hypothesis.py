import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    faultTree_Transfer,
    Transfer,
    Event,
    faultTree_TransferIn,
    faultTree_TransferOut,
    faultTree_ConditioningEvent,
    faultTree_PrimaryEvent,
    faultTree_IntermediateEvent,
    faultTree_Event,
    faultTree_Gate,
    faultTree_FaultTree,
    GateType,
    PrimaryEventType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_faulttree_transfer_is_not_abstract():
    assert not inspect.isabstract(faultTree_Transfer)


def test_faulttree_transfer_constructor_exists():
    assert callable(faultTree_Transfer.__init__)


def test_faulttree_transfer_constructor_args():
    sig = inspect.signature(faultTree_Transfer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_faulttree_transfer_has_name():
    assert hasattr(faultTree_Transfer, "name")
    descriptor = None
    for klass in faultTree_Transfer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_transfer_is_not_abstract():
    assert not inspect.isabstract(Transfer)


def test_transfer_constructor_exists():
    assert callable(Transfer.__init__)


def test_transfer_constructor_args():
    sig = inspect.signature(Transfer.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_faulttree_transferin_is_not_abstract():
    assert not inspect.isabstract(faultTree_TransferIn)


def test_faulttree_transferin_constructor_exists():
    assert callable(faultTree_TransferIn.__init__)


def test_faulttree_transferin_constructor_args():
    sig = inspect.signature(faultTree_TransferIn.__init__)
    params = list(sig.parameters.keys())



def test_faulttree_transferout_is_not_abstract():
    assert not inspect.isabstract(faultTree_TransferOut)


def test_faulttree_transferout_constructor_exists():
    assert callable(faultTree_TransferOut.__init__)


def test_faulttree_transferout_constructor_args():
    sig = inspect.signature(faultTree_TransferOut.__init__)
    params = list(sig.parameters.keys())



def test_faulttree_conditioningevent_is_not_abstract():
    assert not inspect.isabstract(faultTree_ConditioningEvent)


def test_faulttree_conditioningevent_constructor_exists():
    assert callable(faultTree_ConditioningEvent.__init__)


def test_faulttree_conditioningevent_constructor_args():
    sig = inspect.signature(faultTree_ConditioningEvent.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_faulttree_conditioningevent_has_condition():
    assert hasattr(faultTree_ConditioningEvent, "condition")
    descriptor = None
    for klass in faultTree_ConditioningEvent.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_faulttree_primaryevent_is_not_abstract():
    assert not inspect.isabstract(faultTree_PrimaryEvent)


def test_faulttree_primaryevent_constructor_exists():
    assert callable(faultTree_PrimaryEvent.__init__)


def test_faulttree_primaryevent_constructor_args():
    sig = inspect.signature(faultTree_PrimaryEvent.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"
    assert "type" in params, "Missing parameter 'type'"

def test_faulttree_primaryevent_has_probability():
    assert hasattr(faultTree_PrimaryEvent, "probability")
    descriptor = None
    for klass in faultTree_PrimaryEvent.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)

def test_faulttree_primaryevent_has_type():
    assert hasattr(faultTree_PrimaryEvent, "type")
    descriptor = None
    for klass in faultTree_PrimaryEvent.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_faulttree_intermediateevent_is_not_abstract():
    assert not inspect.isabstract(faultTree_IntermediateEvent)


def test_faulttree_intermediateevent_constructor_exists():
    assert callable(faultTree_IntermediateEvent.__init__)


def test_faulttree_intermediateevent_constructor_args():
    sig = inspect.signature(faultTree_IntermediateEvent.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"

def test_faulttree_intermediateevent_has_probability():
    assert hasattr(faultTree_IntermediateEvent, "probability")
    descriptor = None
    for klass in faultTree_IntermediateEvent.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)



def test_faulttree_event_is_not_abstract():
    assert not inspect.isabstract(faultTree_Event)


def test_faulttree_event_constructor_exists():
    assert callable(faultTree_Event.__init__)


def test_faulttree_event_constructor_args():
    sig = inspect.signature(faultTree_Event.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_faulttree_event_has_description():
    assert hasattr(faultTree_Event, "description")
    descriptor = None
    for klass in faultTree_Event.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_faulttree_event_has_name():
    assert hasattr(faultTree_Event, "name")
    descriptor = None
    for klass in faultTree_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_faulttree_gate_is_not_abstract():
    assert not inspect.isabstract(faultTree_Gate)


def test_faulttree_gate_constructor_exists():
    assert callable(faultTree_Gate.__init__)


def test_faulttree_gate_constructor_args():
    sig = inspect.signature(faultTree_Gate.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "probability" in params, "Missing parameter 'probability'"

def test_faulttree_gate_has_name():
    assert hasattr(faultTree_Gate, "name")
    descriptor = None
    for klass in faultTree_Gate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_faulttree_gate_has_type():
    assert hasattr(faultTree_Gate, "type")
    descriptor = None
    for klass in faultTree_Gate.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_faulttree_gate_has_probability():
    assert hasattr(faultTree_Gate, "probability")
    descriptor = None
    for klass in faultTree_Gate.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)



def test_faulttree_faulttree_is_not_abstract():
    assert not inspect.isabstract(faultTree_FaultTree)


def test_faulttree_faulttree_constructor_exists():
    assert callable(faultTree_FaultTree.__init__)


def test_faulttree_faulttree_constructor_args():
    sig = inspect.signature(faultTree_FaultTree.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_faulttree_faulttree_has_name():
    assert hasattr(faultTree_FaultTree, "name")
    descriptor = None
    for klass in faultTree_FaultTree.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_gatetype_exists():
    # Check that the Enumeration exists
    assert GateType is not None

def test_gatetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GateType]
    expected_literals = [
        "OR",
        "PAND",
        "INHIBIT",
        "AND",
        "XOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GateType"

def test_primaryeventtype_exists():
    # Check that the Enumeration exists
    assert PrimaryEventType is not None

def test_primaryeventtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimaryEventType]
    expected_literals = [
        "UNDEVELOPED",
        "BASIC",
        "EXTERNAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimaryEventType"


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
faultTree_Transfer_strategy = st.builds(
    faultTree_Transfer,
    name=
        safe_text
)
Transfer_strategy = st.builds(
    Transfer,
)
Event_strategy = st.builds(
    Event,
)
faultTree_TransferIn_strategy = st.builds(
    faultTree_TransferIn,
)
faultTree_TransferOut_strategy = st.builds(
    faultTree_TransferOut,
)
faultTree_ConditioningEvent_strategy = st.builds(
    faultTree_ConditioningEvent,
    condition=
        safe_text
)
faultTree_PrimaryEvent_strategy = st.builds(
    faultTree_PrimaryEvent,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        safe_text
)
faultTree_IntermediateEvent_strategy = st.builds(
    faultTree_IntermediateEvent,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
faultTree_Event_strategy = st.builds(
    faultTree_Event,
    description=
        safe_text,
    name=
        safe_text
)
faultTree_Gate_strategy = st.builds(
    faultTree_Gate,
    name=
        safe_text,
    type=
        safe_text,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
faultTree_FaultTree_strategy = st.builds(
    faultTree_FaultTree,
    name=
        safe_text
)

@given(instance=faultTree_Transfer_strategy)
@settings(max_examples=50)
def test_faulttree_transfer_instantiation(instance):
    assert isinstance(instance, faultTree_Transfer)



@given(instance=faultTree_Transfer_strategy)
def test_faulttree_transfer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Transfer_strategy)
@settings(max_examples=50)
def test_transfer_instantiation(instance):
    assert isinstance(instance, Transfer)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=faultTree_TransferIn_strategy)
@settings(max_examples=50)
def test_faulttree_transferin_instantiation(instance):
    assert isinstance(instance, faultTree_TransferIn)

@given(instance=faultTree_TransferOut_strategy)
@settings(max_examples=50)
def test_faulttree_transferout_instantiation(instance):
    assert isinstance(instance, faultTree_TransferOut)

@given(instance=faultTree_ConditioningEvent_strategy)
@settings(max_examples=50)
def test_faulttree_conditioningevent_instantiation(instance):
    assert isinstance(instance, faultTree_ConditioningEvent)



@given(instance=faultTree_ConditioningEvent_strategy)
def test_faulttree_conditioningevent_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=faultTree_PrimaryEvent_strategy)
@settings(max_examples=50)
def test_faulttree_primaryevent_instantiation(instance):
    assert isinstance(instance, faultTree_PrimaryEvent)



@given(instance=faultTree_PrimaryEvent_strategy)
def test_faulttree_primaryevent_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original



@given(instance=faultTree_PrimaryEvent_strategy)
def test_faulttree_primaryevent_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=faultTree_IntermediateEvent_strategy)
@settings(max_examples=50)
def test_faulttree_intermediateevent_instantiation(instance):
    assert isinstance(instance, faultTree_IntermediateEvent)



@given(instance=faultTree_IntermediateEvent_strategy)
def test_faulttree_intermediateevent_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=faultTree_Event_strategy)
@settings(max_examples=50)
def test_faulttree_event_instantiation(instance):
    assert isinstance(instance, faultTree_Event)



@given(instance=faultTree_Event_strategy)
def test_faulttree_event_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=faultTree_Event_strategy)
def test_faulttree_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=faultTree_Gate_strategy)
@settings(max_examples=50)
def test_faulttree_gate_instantiation(instance):
    assert isinstance(instance, faultTree_Gate)



@given(instance=faultTree_Gate_strategy)
def test_faulttree_gate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=faultTree_Gate_strategy)
def test_faulttree_gate_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=faultTree_Gate_strategy)
def test_faulttree_gate_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=faultTree_FaultTree_strategy)
@settings(max_examples=50)
def test_faulttree_faulttree_instantiation(instance):
    assert isinstance(instance, faultTree_FaultTree)



@given(instance=faultTree_FaultTree_strategy)
def test_faulttree_faulttree_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
