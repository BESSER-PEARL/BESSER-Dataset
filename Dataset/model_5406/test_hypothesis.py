import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    faultTree::Transfer,
    Transfer,
    Event,
    faultTree::TransferIn,
    faultTree::TransferOut,
    faultTree::ConditioningEvent,
    faultTree::PrimaryEvent,
    faultTree::IntermediateEvent,
    faultTree::Event,
    faultTree::Gate,
    faultTree::FaultTree,
    PrimaryEventType,
    GateType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_faulttree::transfer_is_not_abstract():
    assert not inspect.isabstract(faultTree::Transfer)


def test_faulttree::transfer_constructor_exists():
    assert callable(faultTree::Transfer.__init__)


def test_faulttree::transfer_constructor_args():
    sig = inspect.signature(faultTree::Transfer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_faulttree::transfer_has_name():
    assert hasattr(faultTree::Transfer, "name")
    descriptor = None
    for klass in faultTree::Transfer.__mro__:
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



def test_faulttree::transferin_is_not_abstract():
    assert not inspect.isabstract(faultTree::TransferIn)


def test_faulttree::transferin_constructor_exists():
    assert callable(faultTree::TransferIn.__init__)


def test_faulttree::transferin_constructor_args():
    sig = inspect.signature(faultTree::TransferIn.__init__)
    params = list(sig.parameters.keys())



def test_faulttree::transferout_is_not_abstract():
    assert not inspect.isabstract(faultTree::TransferOut)


def test_faulttree::transferout_constructor_exists():
    assert callable(faultTree::TransferOut.__init__)


def test_faulttree::transferout_constructor_args():
    sig = inspect.signature(faultTree::TransferOut.__init__)
    params = list(sig.parameters.keys())



def test_faulttree::conditioningevent_is_not_abstract():
    assert not inspect.isabstract(faultTree::ConditioningEvent)


def test_faulttree::conditioningevent_constructor_exists():
    assert callable(faultTree::ConditioningEvent.__init__)


def test_faulttree::conditioningevent_constructor_args():
    sig = inspect.signature(faultTree::ConditioningEvent.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_faulttree::conditioningevent_has_condition():
    assert hasattr(faultTree::ConditioningEvent, "condition")
    descriptor = None
    for klass in faultTree::ConditioningEvent.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_faulttree::primaryevent_is_not_abstract():
    assert not inspect.isabstract(faultTree::PrimaryEvent)


def test_faulttree::primaryevent_constructor_exists():
    assert callable(faultTree::PrimaryEvent.__init__)


def test_faulttree::primaryevent_constructor_args():
    sig = inspect.signature(faultTree::PrimaryEvent.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "probability" in params, "Missing parameter 'probability'"

def test_faulttree::primaryevent_has_type():
    assert hasattr(faultTree::PrimaryEvent, "type")
    descriptor = None
    for klass in faultTree::PrimaryEvent.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_faulttree::primaryevent_has_probability():
    assert hasattr(faultTree::PrimaryEvent, "probability")
    descriptor = None
    for klass in faultTree::PrimaryEvent.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)



def test_faulttree::intermediateevent_is_not_abstract():
    assert not inspect.isabstract(faultTree::IntermediateEvent)


def test_faulttree::intermediateevent_constructor_exists():
    assert callable(faultTree::IntermediateEvent.__init__)


def test_faulttree::intermediateevent_constructor_args():
    sig = inspect.signature(faultTree::IntermediateEvent.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"

def test_faulttree::intermediateevent_has_probability():
    assert hasattr(faultTree::IntermediateEvent, "probability")
    descriptor = None
    for klass in faultTree::IntermediateEvent.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)



def test_faulttree::event_is_not_abstract():
    assert not inspect.isabstract(faultTree::Event)


def test_faulttree::event_constructor_exists():
    assert callable(faultTree::Event.__init__)


def test_faulttree::event_constructor_args():
    sig = inspect.signature(faultTree::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_faulttree::event_has_name():
    assert hasattr(faultTree::Event, "name")
    descriptor = None
    for klass in faultTree::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_faulttree::event_has_description():
    assert hasattr(faultTree::Event, "description")
    descriptor = None
    for klass in faultTree::Event.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_faulttree::gate_is_not_abstract():
    assert not inspect.isabstract(faultTree::Gate)


def test_faulttree::gate_constructor_exists():
    assert callable(faultTree::Gate.__init__)


def test_faulttree::gate_constructor_args():
    sig = inspect.signature(faultTree::Gate.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_faulttree::gate_has_probability():
    assert hasattr(faultTree::Gate, "probability")
    descriptor = None
    for klass in faultTree::Gate.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)

def test_faulttree::gate_has_type():
    assert hasattr(faultTree::Gate, "type")
    descriptor = None
    for klass in faultTree::Gate.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_faulttree::gate_has_name():
    assert hasattr(faultTree::Gate, "name")
    descriptor = None
    for klass in faultTree::Gate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_faulttree::faulttree_is_not_abstract():
    assert not inspect.isabstract(faultTree::FaultTree)


def test_faulttree::faulttree_constructor_exists():
    assert callable(faultTree::FaultTree.__init__)


def test_faulttree::faulttree_constructor_args():
    sig = inspect.signature(faultTree::FaultTree.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_faulttree::faulttree_has_name():
    assert hasattr(faultTree::FaultTree, "name")
    descriptor = None
    for klass in faultTree::FaultTree.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_primaryeventtype_exists():
    # Check that the Enumeration exists
    assert PrimaryEventType is not None

def test_primaryeventtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimaryEventType]
    expected_literals = [
        "BASIC",
        "EXTERNAL",
        "UNDEVELOPED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimaryEventType"

def test_gatetype_exists():
    # Check that the Enumeration exists
    assert GateType is not None

def test_gatetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GateType]
    expected_literals = [
        "PAND",
        "INHIBIT",
        "OR",
        "XOR",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GateType"


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
faultTree::Transfer_strategy = st.builds(
    faultTree::Transfer,
    name=
        safe_text
)
Transfer_strategy = st.builds(
    Transfer,
)
Event_strategy = st.builds(
    Event,
)
faultTree::TransferIn_strategy = st.builds(
    faultTree::TransferIn,
)
faultTree::TransferOut_strategy = st.builds(
    faultTree::TransferOut,
)
faultTree::ConditioningEvent_strategy = st.builds(
    faultTree::ConditioningEvent,
    condition=
        safe_text
)
faultTree::PrimaryEvent_strategy = st.builds(
    faultTree::PrimaryEvent,
    type=
        safe_text,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
faultTree::IntermediateEvent_strategy = st.builds(
    faultTree::IntermediateEvent,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
faultTree::Event_strategy = st.builds(
    faultTree::Event,
    name=
        safe_text,
    description=
        safe_text
)
faultTree::Gate_strategy = st.builds(
    faultTree::Gate,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        safe_text,
    name=
        safe_text
)
faultTree::FaultTree_strategy = st.builds(
    faultTree::FaultTree,
    name=
        safe_text
)

@given(instance=faultTree::Transfer_strategy)
@settings(max_examples=50)
def test_faulttree::transfer_instantiation(instance):
    assert isinstance(instance, faultTree::Transfer)

@given(instance=faultTree::Transfer_strategy)
def test_faulttree::transfer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=faultTree::Transfer_strategy)
def test_faulttree::transfer_name_setter(instance):
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

@given(instance=faultTree::TransferIn_strategy)
@settings(max_examples=50)
def test_faulttree::transferin_instantiation(instance):
    assert isinstance(instance, faultTree::TransferIn)

@given(instance=faultTree::TransferOut_strategy)
@settings(max_examples=50)
def test_faulttree::transferout_instantiation(instance):
    assert isinstance(instance, faultTree::TransferOut)

@given(instance=faultTree::ConditioningEvent_strategy)
@settings(max_examples=50)
def test_faulttree::conditioningevent_instantiation(instance):
    assert isinstance(instance, faultTree::ConditioningEvent)

@given(instance=faultTree::ConditioningEvent_strategy)
def test_faulttree::conditioningevent_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=faultTree::ConditioningEvent_strategy)
def test_faulttree::conditioningevent_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=faultTree::PrimaryEvent_strategy)
@settings(max_examples=50)
def test_faulttree::primaryevent_instantiation(instance):
    assert isinstance(instance, faultTree::PrimaryEvent)

@given(instance=faultTree::PrimaryEvent_strategy)
def test_faulttree::primaryevent_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=faultTree::PrimaryEvent_strategy)
def test_faulttree::primaryevent_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=faultTree::PrimaryEvent_strategy)
def test_faulttree::primaryevent_probability_type(instance):
    assert isinstance(instance.probability, float)


@given(instance=faultTree::PrimaryEvent_strategy)
def test_faulttree::primaryevent_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=faultTree::IntermediateEvent_strategy)
@settings(max_examples=50)
def test_faulttree::intermediateevent_instantiation(instance):
    assert isinstance(instance, faultTree::IntermediateEvent)

@given(instance=faultTree::IntermediateEvent_strategy)
def test_faulttree::intermediateevent_probability_type(instance):
    assert isinstance(instance.probability, float)


@given(instance=faultTree::IntermediateEvent_strategy)
def test_faulttree::intermediateevent_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=faultTree::Event_strategy)
@settings(max_examples=50)
def test_faulttree::event_instantiation(instance):
    assert isinstance(instance, faultTree::Event)

@given(instance=faultTree::Event_strategy)
def test_faulttree::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=faultTree::Event_strategy)
def test_faulttree::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=faultTree::Event_strategy)
def test_faulttree::event_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=faultTree::Event_strategy)
def test_faulttree::event_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=faultTree::Gate_strategy)
@settings(max_examples=50)
def test_faulttree::gate_instantiation(instance):
    assert isinstance(instance, faultTree::Gate)

@given(instance=faultTree::Gate_strategy)
def test_faulttree::gate_probability_type(instance):
    assert isinstance(instance.probability, float)


@given(instance=faultTree::Gate_strategy)
def test_faulttree::gate_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=faultTree::Gate_strategy)
def test_faulttree::gate_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=faultTree::Gate_strategy)
def test_faulttree::gate_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=faultTree::Gate_strategy)
def test_faulttree::gate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=faultTree::Gate_strategy)
def test_faulttree::gate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=faultTree::FaultTree_strategy)
@settings(max_examples=50)
def test_faulttree::faulttree_instantiation(instance):
    assert isinstance(instance, faultTree::FaultTree)

@given(instance=faultTree::FaultTree_strategy)
def test_faulttree::faulttree_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=faultTree::FaultTree_strategy)
def test_faulttree::faulttree_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
