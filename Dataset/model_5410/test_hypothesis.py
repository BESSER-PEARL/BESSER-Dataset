import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Gate,
    fault_tree_XOR,
    fault_tree_PriorAND,
    fault_tree_AND,
    fault_tree_Inhibit,
    fault_tree_OR,
    Event,
    fault_tree_UndevelopedEvent,
    fault_tree_IntermediateEvent,
    fault_tree_BasicEvent,
    fault_tree_Hazard,
    IDBase,
    fault_tree_ErrorType,
    fault_tree_FaultTree,
    fault_tree_ErrorInstance,
    fault_tree_FailureType,
    fault_tree_Event,
    fault_tree_FailureInstance,
    fault_tree_Gate,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gate_is_not_abstract():
    assert not inspect.isabstract(Gate)


def test_gate_constructor_exists():
    assert callable(Gate.__init__)


def test_gate_constructor_args():
    sig = inspect.signature(Gate.__init__)
    params = list(sig.parameters.keys())



def test_fault_tree_xor_is_not_abstract():
    assert not inspect.isabstract(fault_tree_XOR)


def test_fault_tree_xor_constructor_exists():
    assert callable(fault_tree_XOR.__init__)


def test_fault_tree_xor_constructor_args():
    sig = inspect.signature(fault_tree_XOR.__init__)
    params = list(sig.parameters.keys())



def test_fault_tree_priorand_is_not_abstract():
    assert not inspect.isabstract(fault_tree_PriorAND)


def test_fault_tree_priorand_constructor_exists():
    assert callable(fault_tree_PriorAND.__init__)


def test_fault_tree_priorand_constructor_args():
    sig = inspect.signature(fault_tree_PriorAND.__init__)
    params = list(sig.parameters.keys())



def test_fault_tree_and_is_not_abstract():
    assert not inspect.isabstract(fault_tree_AND)


def test_fault_tree_and_constructor_exists():
    assert callable(fault_tree_AND.__init__)


def test_fault_tree_and_constructor_args():
    sig = inspect.signature(fault_tree_AND.__init__)
    params = list(sig.parameters.keys())



def test_fault_tree_inhibit_is_not_abstract():
    assert not inspect.isabstract(fault_tree_Inhibit)


def test_fault_tree_inhibit_constructor_exists():
    assert callable(fault_tree_Inhibit.__init__)


def test_fault_tree_inhibit_constructor_args():
    sig = inspect.signature(fault_tree_Inhibit.__init__)
    params = list(sig.parameters.keys())



def test_fault_tree_or_is_not_abstract():
    assert not inspect.isabstract(fault_tree_OR)


def test_fault_tree_or_constructor_exists():
    assert callable(fault_tree_OR.__init__)


def test_fault_tree_or_constructor_args():
    sig = inspect.signature(fault_tree_OR.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_fault_tree_undevelopedevent_is_not_abstract():
    assert not inspect.isabstract(fault_tree_UndevelopedEvent)


def test_fault_tree_undevelopedevent_constructor_exists():
    assert callable(fault_tree_UndevelopedEvent.__init__)


def test_fault_tree_undevelopedevent_constructor_args():
    sig = inspect.signature(fault_tree_UndevelopedEvent.__init__)
    params = list(sig.parameters.keys())



def test_fault_tree_intermediateevent_is_not_abstract():
    assert not inspect.isabstract(fault_tree_IntermediateEvent)


def test_fault_tree_intermediateevent_constructor_exists():
    assert callable(fault_tree_IntermediateEvent.__init__)


def test_fault_tree_intermediateevent_constructor_args():
    sig = inspect.signature(fault_tree_IntermediateEvent.__init__)
    params = list(sig.parameters.keys())



def test_fault_tree_basicevent_is_not_abstract():
    assert not inspect.isabstract(fault_tree_BasicEvent)


def test_fault_tree_basicevent_constructor_exists():
    assert callable(fault_tree_BasicEvent.__init__)


def test_fault_tree_basicevent_constructor_args():
    sig = inspect.signature(fault_tree_BasicEvent.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"

def test_fault_tree_basicevent_has_probability():
    assert hasattr(fault_tree_BasicEvent, "probability")
    descriptor = None
    for klass in fault_tree_BasicEvent.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)



def test_fault_tree_hazard_is_not_abstract():
    assert not inspect.isabstract(fault_tree_Hazard)


def test_fault_tree_hazard_constructor_exists():
    assert callable(fault_tree_Hazard.__init__)


def test_fault_tree_hazard_constructor_args():
    sig = inspect.signature(fault_tree_Hazard.__init__)
    params = list(sig.parameters.keys())



def test_idbase_is_not_abstract():
    assert not inspect.isabstract(IDBase)


def test_idbase_constructor_exists():
    assert callable(IDBase.__init__)


def test_idbase_constructor_args():
    sig = inspect.signature(IDBase.__init__)
    params = list(sig.parameters.keys())



def test_fault_tree_errortype_is_not_abstract():
    assert not inspect.isabstract(fault_tree_ErrorType)


def test_fault_tree_errortype_constructor_exists():
    assert callable(fault_tree_ErrorType.__init__)


def test_fault_tree_errortype_constructor_args():
    sig = inspect.signature(fault_tree_ErrorType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fault_tree_errortype_has_name():
    assert hasattr(fault_tree_ErrorType, "name")
    descriptor = None
    for klass in fault_tree_ErrorType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fault_tree_faulttree_is_not_abstract():
    assert not inspect.isabstract(fault_tree_FaultTree)


def test_fault_tree_faulttree_constructor_exists():
    assert callable(fault_tree_FaultTree.__init__)


def test_fault_tree_faulttree_constructor_args():
    sig = inspect.signature(fault_tree_FaultTree.__init__)
    params = list(sig.parameters.keys())



def test_fault_tree_errorinstance_is_not_abstract():
    assert not inspect.isabstract(fault_tree_ErrorInstance)


def test_fault_tree_errorinstance_constructor_exists():
    assert callable(fault_tree_ErrorInstance.__init__)


def test_fault_tree_errorinstance_constructor_args():
    sig = inspect.signature(fault_tree_ErrorInstance.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fault_tree_errorinstance_has_name():
    assert hasattr(fault_tree_ErrorInstance, "name")
    descriptor = None
    for klass in fault_tree_ErrorInstance.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fault_tree_failuretype_is_not_abstract():
    assert not inspect.isabstract(fault_tree_FailureType)


def test_fault_tree_failuretype_constructor_exists():
    assert callable(fault_tree_FailureType.__init__)


def test_fault_tree_failuretype_constructor_args():
    sig = inspect.signature(fault_tree_FailureType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fault_tree_failuretype_has_name():
    assert hasattr(fault_tree_FailureType, "name")
    descriptor = None
    for klass in fault_tree_FailureType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fault_tree_event_is_not_abstract():
    assert not inspect.isabstract(fault_tree_Event)


def test_fault_tree_event_constructor_exists():
    assert callable(fault_tree_Event.__init__)


def test_fault_tree_event_constructor_args():
    sig = inspect.signature(fault_tree_Event.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_fault_tree_event_has_description():
    assert hasattr(fault_tree_Event, "description")
    descriptor = None
    for klass in fault_tree_Event.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_fault_tree_event_has_name():
    assert hasattr(fault_tree_Event, "name")
    descriptor = None
    for klass in fault_tree_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fault_tree_failureinstance_is_not_abstract():
    assert not inspect.isabstract(fault_tree_FailureInstance)


def test_fault_tree_failureinstance_constructor_exists():
    assert callable(fault_tree_FailureInstance.__init__)


def test_fault_tree_failureinstance_constructor_args():
    sig = inspect.signature(fault_tree_FailureInstance.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fault_tree_failureinstance_has_name():
    assert hasattr(fault_tree_FailureInstance, "name")
    descriptor = None
    for klass in fault_tree_FailureInstance.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fault_tree_gate_is_not_abstract():
    assert not inspect.isabstract(fault_tree_Gate)


def test_fault_tree_gate_constructor_exists():
    assert callable(fault_tree_Gate.__init__)


def test_fault_tree_gate_constructor_args():
    sig = inspect.signature(fault_tree_Gate.__init__)
    params = list(sig.parameters.keys())


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
Gate_strategy = st.builds(
    Gate,
)
fault_tree_XOR_strategy = st.builds(
    fault_tree_XOR,
)
fault_tree_PriorAND_strategy = st.builds(
    fault_tree_PriorAND,
)
fault_tree_AND_strategy = st.builds(
    fault_tree_AND,
)
fault_tree_Inhibit_strategy = st.builds(
    fault_tree_Inhibit,
)
fault_tree_OR_strategy = st.builds(
    fault_tree_OR,
)
Event_strategy = st.builds(
    Event,
)
fault_tree_UndevelopedEvent_strategy = st.builds(
    fault_tree_UndevelopedEvent,
)
fault_tree_IntermediateEvent_strategy = st.builds(
    fault_tree_IntermediateEvent,
)
fault_tree_BasicEvent_strategy = st.builds(
    fault_tree_BasicEvent,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fault_tree_Hazard_strategy = st.builds(
    fault_tree_Hazard,
)
IDBase_strategy = st.builds(
    IDBase,
)
fault_tree_ErrorType_strategy = st.builds(
    fault_tree_ErrorType,
    name=
        safe_text
)
fault_tree_FaultTree_strategy = st.builds(
    fault_tree_FaultTree,
)
fault_tree_ErrorInstance_strategy = st.builds(
    fault_tree_ErrorInstance,
    name=
        safe_text
)
fault_tree_FailureType_strategy = st.builds(
    fault_tree_FailureType,
    name=
        safe_text
)
fault_tree_Event_strategy = st.builds(
    fault_tree_Event,
    description=
        safe_text,
    name=
        safe_text
)
fault_tree_FailureInstance_strategy = st.builds(
    fault_tree_FailureInstance,
    name=
        safe_text
)
fault_tree_Gate_strategy = st.builds(
    fault_tree_Gate,
)

@given(instance=Gate_strategy)
@settings(max_examples=50)
def test_gate_instantiation(instance):
    assert isinstance(instance, Gate)

@given(instance=fault_tree_XOR_strategy)
@settings(max_examples=50)
def test_fault_tree_xor_instantiation(instance):
    assert isinstance(instance, fault_tree_XOR)

@given(instance=fault_tree_PriorAND_strategy)
@settings(max_examples=50)
def test_fault_tree_priorand_instantiation(instance):
    assert isinstance(instance, fault_tree_PriorAND)

@given(instance=fault_tree_AND_strategy)
@settings(max_examples=50)
def test_fault_tree_and_instantiation(instance):
    assert isinstance(instance, fault_tree_AND)

@given(instance=fault_tree_Inhibit_strategy)
@settings(max_examples=50)
def test_fault_tree_inhibit_instantiation(instance):
    assert isinstance(instance, fault_tree_Inhibit)

@given(instance=fault_tree_OR_strategy)
@settings(max_examples=50)
def test_fault_tree_or_instantiation(instance):
    assert isinstance(instance, fault_tree_OR)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=fault_tree_UndevelopedEvent_strategy)
@settings(max_examples=50)
def test_fault_tree_undevelopedevent_instantiation(instance):
    assert isinstance(instance, fault_tree_UndevelopedEvent)

@given(instance=fault_tree_IntermediateEvent_strategy)
@settings(max_examples=50)
def test_fault_tree_intermediateevent_instantiation(instance):
    assert isinstance(instance, fault_tree_IntermediateEvent)

@given(instance=fault_tree_BasicEvent_strategy)
@settings(max_examples=50)
def test_fault_tree_basicevent_instantiation(instance):
    assert isinstance(instance, fault_tree_BasicEvent)



@given(instance=fault_tree_BasicEvent_strategy)
def test_fault_tree_basicevent_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=fault_tree_Hazard_strategy)
@settings(max_examples=50)
def test_fault_tree_hazard_instantiation(instance):
    assert isinstance(instance, fault_tree_Hazard)

@given(instance=IDBase_strategy)
@settings(max_examples=50)
def test_idbase_instantiation(instance):
    assert isinstance(instance, IDBase)

@given(instance=fault_tree_ErrorType_strategy)
@settings(max_examples=50)
def test_fault_tree_errortype_instantiation(instance):
    assert isinstance(instance, fault_tree_ErrorType)



@given(instance=fault_tree_ErrorType_strategy)
def test_fault_tree_errortype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fault_tree_FaultTree_strategy)
@settings(max_examples=50)
def test_fault_tree_faulttree_instantiation(instance):
    assert isinstance(instance, fault_tree_FaultTree)

@given(instance=fault_tree_ErrorInstance_strategy)
@settings(max_examples=50)
def test_fault_tree_errorinstance_instantiation(instance):
    assert isinstance(instance, fault_tree_ErrorInstance)



@given(instance=fault_tree_ErrorInstance_strategy)
def test_fault_tree_errorinstance_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fault_tree_FailureType_strategy)
@settings(max_examples=50)
def test_fault_tree_failuretype_instantiation(instance):
    assert isinstance(instance, fault_tree_FailureType)



@given(instance=fault_tree_FailureType_strategy)
def test_fault_tree_failuretype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fault_tree_Event_strategy)
@settings(max_examples=50)
def test_fault_tree_event_instantiation(instance):
    assert isinstance(instance, fault_tree_Event)



@given(instance=fault_tree_Event_strategy)
def test_fault_tree_event_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=fault_tree_Event_strategy)
def test_fault_tree_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fault_tree_FailureInstance_strategy)
@settings(max_examples=50)
def test_fault_tree_failureinstance_instantiation(instance):
    assert isinstance(instance, fault_tree_FailureInstance)



@given(instance=fault_tree_FailureInstance_strategy)
def test_fault_tree_failureinstance_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fault_tree_Gate_strategy)
@settings(max_examples=50)
def test_fault_tree_gate_instantiation(instance):
    assert isinstance(instance, fault_tree_Gate)
