import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Gate,
    fault::tree::PriorAND,
    fault::tree::AND,
    fault::tree::Inhibit,
    fault::tree::XOR,
    fault::tree::OR,
    Event,
    fault::tree::UndevelopedEvent,
    fault::tree::IntermediateEvent,
    fault::tree::BasicEvent,
    fault::tree::Hazard,
    IDBase,
    fault::tree::ErrorInstance,
    fault::tree::FaultTree,
    fault::tree::ErrorType,
    fault::tree::FailureInstance,
    fault::tree::FailureType,
    fault::tree::Event,
    fault::tree::Gate,
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



def test_fault::tree::priorand_is_not_abstract():
    assert not inspect.isabstract(fault::tree::PriorAND)


def test_fault::tree::priorand_constructor_exists():
    assert callable(fault::tree::PriorAND.__init__)


def test_fault::tree::priorand_constructor_args():
    sig = inspect.signature(fault::tree::PriorAND.__init__)
    params = list(sig.parameters.keys())



def test_fault::tree::and_is_not_abstract():
    assert not inspect.isabstract(fault::tree::AND)


def test_fault::tree::and_constructor_exists():
    assert callable(fault::tree::AND.__init__)


def test_fault::tree::and_constructor_args():
    sig = inspect.signature(fault::tree::AND.__init__)
    params = list(sig.parameters.keys())



def test_fault::tree::inhibit_is_not_abstract():
    assert not inspect.isabstract(fault::tree::Inhibit)


def test_fault::tree::inhibit_constructor_exists():
    assert callable(fault::tree::Inhibit.__init__)


def test_fault::tree::inhibit_constructor_args():
    sig = inspect.signature(fault::tree::Inhibit.__init__)
    params = list(sig.parameters.keys())



def test_fault::tree::xor_is_not_abstract():
    assert not inspect.isabstract(fault::tree::XOR)


def test_fault::tree::xor_constructor_exists():
    assert callable(fault::tree::XOR.__init__)


def test_fault::tree::xor_constructor_args():
    sig = inspect.signature(fault::tree::XOR.__init__)
    params = list(sig.parameters.keys())



def test_fault::tree::or_is_not_abstract():
    assert not inspect.isabstract(fault::tree::OR)


def test_fault::tree::or_constructor_exists():
    assert callable(fault::tree::OR.__init__)


def test_fault::tree::or_constructor_args():
    sig = inspect.signature(fault::tree::OR.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_fault::tree::undevelopedevent_is_not_abstract():
    assert not inspect.isabstract(fault::tree::UndevelopedEvent)


def test_fault::tree::undevelopedevent_constructor_exists():
    assert callable(fault::tree::UndevelopedEvent.__init__)


def test_fault::tree::undevelopedevent_constructor_args():
    sig = inspect.signature(fault::tree::UndevelopedEvent.__init__)
    params = list(sig.parameters.keys())



def test_fault::tree::intermediateevent_is_not_abstract():
    assert not inspect.isabstract(fault::tree::IntermediateEvent)


def test_fault::tree::intermediateevent_constructor_exists():
    assert callable(fault::tree::IntermediateEvent.__init__)


def test_fault::tree::intermediateevent_constructor_args():
    sig = inspect.signature(fault::tree::IntermediateEvent.__init__)
    params = list(sig.parameters.keys())



def test_fault::tree::basicevent_is_not_abstract():
    assert not inspect.isabstract(fault::tree::BasicEvent)


def test_fault::tree::basicevent_constructor_exists():
    assert callable(fault::tree::BasicEvent.__init__)


def test_fault::tree::basicevent_constructor_args():
    sig = inspect.signature(fault::tree::BasicEvent.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"

def test_fault::tree::basicevent_has_probability():
    assert hasattr(fault::tree::BasicEvent, "probability")
    descriptor = None
    for klass in fault::tree::BasicEvent.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)



def test_fault::tree::hazard_is_not_abstract():
    assert not inspect.isabstract(fault::tree::Hazard)


def test_fault::tree::hazard_constructor_exists():
    assert callable(fault::tree::Hazard.__init__)


def test_fault::tree::hazard_constructor_args():
    sig = inspect.signature(fault::tree::Hazard.__init__)
    params = list(sig.parameters.keys())



def test_idbase_is_not_abstract():
    assert not inspect.isabstract(IDBase)


def test_idbase_constructor_exists():
    assert callable(IDBase.__init__)


def test_idbase_constructor_args():
    sig = inspect.signature(IDBase.__init__)
    params = list(sig.parameters.keys())



def test_fault::tree::errorinstance_is_not_abstract():
    assert not inspect.isabstract(fault::tree::ErrorInstance)


def test_fault::tree::errorinstance_constructor_exists():
    assert callable(fault::tree::ErrorInstance.__init__)


def test_fault::tree::errorinstance_constructor_args():
    sig = inspect.signature(fault::tree::ErrorInstance.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fault::tree::errorinstance_has_name():
    assert hasattr(fault::tree::ErrorInstance, "name")
    descriptor = None
    for klass in fault::tree::ErrorInstance.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fault::tree::faulttree_is_not_abstract():
    assert not inspect.isabstract(fault::tree::FaultTree)


def test_fault::tree::faulttree_constructor_exists():
    assert callable(fault::tree::FaultTree.__init__)


def test_fault::tree::faulttree_constructor_args():
    sig = inspect.signature(fault::tree::FaultTree.__init__)
    params = list(sig.parameters.keys())



def test_fault::tree::errortype_is_not_abstract():
    assert not inspect.isabstract(fault::tree::ErrorType)


def test_fault::tree::errortype_constructor_exists():
    assert callable(fault::tree::ErrorType.__init__)


def test_fault::tree::errortype_constructor_args():
    sig = inspect.signature(fault::tree::ErrorType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fault::tree::errortype_has_name():
    assert hasattr(fault::tree::ErrorType, "name")
    descriptor = None
    for klass in fault::tree::ErrorType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fault::tree::failureinstance_is_not_abstract():
    assert not inspect.isabstract(fault::tree::FailureInstance)


def test_fault::tree::failureinstance_constructor_exists():
    assert callable(fault::tree::FailureInstance.__init__)


def test_fault::tree::failureinstance_constructor_args():
    sig = inspect.signature(fault::tree::FailureInstance.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fault::tree::failureinstance_has_name():
    assert hasattr(fault::tree::FailureInstance, "name")
    descriptor = None
    for klass in fault::tree::FailureInstance.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fault::tree::failuretype_is_not_abstract():
    assert not inspect.isabstract(fault::tree::FailureType)


def test_fault::tree::failuretype_constructor_exists():
    assert callable(fault::tree::FailureType.__init__)


def test_fault::tree::failuretype_constructor_args():
    sig = inspect.signature(fault::tree::FailureType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fault::tree::failuretype_has_name():
    assert hasattr(fault::tree::FailureType, "name")
    descriptor = None
    for klass in fault::tree::FailureType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fault::tree::event_is_not_abstract():
    assert not inspect.isabstract(fault::tree::Event)


def test_fault::tree::event_constructor_exists():
    assert callable(fault::tree::Event.__init__)


def test_fault::tree::event_constructor_args():
    sig = inspect.signature(fault::tree::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_fault::tree::event_has_name():
    assert hasattr(fault::tree::Event, "name")
    descriptor = None
    for klass in fault::tree::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fault::tree::event_has_description():
    assert hasattr(fault::tree::Event, "description")
    descriptor = None
    for klass in fault::tree::Event.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_fault::tree::gate_is_not_abstract():
    assert not inspect.isabstract(fault::tree::Gate)


def test_fault::tree::gate_constructor_exists():
    assert callable(fault::tree::Gate.__init__)


def test_fault::tree::gate_constructor_args():
    sig = inspect.signature(fault::tree::Gate.__init__)
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
fault::tree::PriorAND_strategy = st.builds(
    fault::tree::PriorAND,
)
fault::tree::AND_strategy = st.builds(
    fault::tree::AND,
)
fault::tree::Inhibit_strategy = st.builds(
    fault::tree::Inhibit,
)
fault::tree::XOR_strategy = st.builds(
    fault::tree::XOR,
)
fault::tree::OR_strategy = st.builds(
    fault::tree::OR,
)
Event_strategy = st.builds(
    Event,
)
fault::tree::UndevelopedEvent_strategy = st.builds(
    fault::tree::UndevelopedEvent,
)
fault::tree::IntermediateEvent_strategy = st.builds(
    fault::tree::IntermediateEvent,
)
fault::tree::BasicEvent_strategy = st.builds(
    fault::tree::BasicEvent,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fault::tree::Hazard_strategy = st.builds(
    fault::tree::Hazard,
)
IDBase_strategy = st.builds(
    IDBase,
)
fault::tree::ErrorInstance_strategy = st.builds(
    fault::tree::ErrorInstance,
    name=
        safe_text
)
fault::tree::FaultTree_strategy = st.builds(
    fault::tree::FaultTree,
)
fault::tree::ErrorType_strategy = st.builds(
    fault::tree::ErrorType,
    name=
        safe_text
)
fault::tree::FailureInstance_strategy = st.builds(
    fault::tree::FailureInstance,
    name=
        safe_text
)
fault::tree::FailureType_strategy = st.builds(
    fault::tree::FailureType,
    name=
        safe_text
)
fault::tree::Event_strategy = st.builds(
    fault::tree::Event,
    name=
        safe_text,
    description=
        safe_text
)
fault::tree::Gate_strategy = st.builds(
    fault::tree::Gate,
)

@given(instance=Gate_strategy)
@settings(max_examples=50)
def test_gate_instantiation(instance):
    assert isinstance(instance, Gate)

@given(instance=fault::tree::PriorAND_strategy)
@settings(max_examples=50)
def test_fault::tree::priorand_instantiation(instance):
    assert isinstance(instance, fault::tree::PriorAND)

@given(instance=fault::tree::AND_strategy)
@settings(max_examples=50)
def test_fault::tree::and_instantiation(instance):
    assert isinstance(instance, fault::tree::AND)

@given(instance=fault::tree::Inhibit_strategy)
@settings(max_examples=50)
def test_fault::tree::inhibit_instantiation(instance):
    assert isinstance(instance, fault::tree::Inhibit)

@given(instance=fault::tree::XOR_strategy)
@settings(max_examples=50)
def test_fault::tree::xor_instantiation(instance):
    assert isinstance(instance, fault::tree::XOR)

@given(instance=fault::tree::OR_strategy)
@settings(max_examples=50)
def test_fault::tree::or_instantiation(instance):
    assert isinstance(instance, fault::tree::OR)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=fault::tree::UndevelopedEvent_strategy)
@settings(max_examples=50)
def test_fault::tree::undevelopedevent_instantiation(instance):
    assert isinstance(instance, fault::tree::UndevelopedEvent)

@given(instance=fault::tree::IntermediateEvent_strategy)
@settings(max_examples=50)
def test_fault::tree::intermediateevent_instantiation(instance):
    assert isinstance(instance, fault::tree::IntermediateEvent)

@given(instance=fault::tree::BasicEvent_strategy)
@settings(max_examples=50)
def test_fault::tree::basicevent_instantiation(instance):
    assert isinstance(instance, fault::tree::BasicEvent)

@given(instance=fault::tree::BasicEvent_strategy)
def test_fault::tree::basicevent_probability_type(instance):
    assert isinstance(instance.probability, float)


@given(instance=fault::tree::BasicEvent_strategy)
def test_fault::tree::basicevent_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=fault::tree::Hazard_strategy)
@settings(max_examples=50)
def test_fault::tree::hazard_instantiation(instance):
    assert isinstance(instance, fault::tree::Hazard)

@given(instance=IDBase_strategy)
@settings(max_examples=50)
def test_idbase_instantiation(instance):
    assert isinstance(instance, IDBase)

@given(instance=fault::tree::ErrorInstance_strategy)
@settings(max_examples=50)
def test_fault::tree::errorinstance_instantiation(instance):
    assert isinstance(instance, fault::tree::ErrorInstance)

@given(instance=fault::tree::ErrorInstance_strategy)
def test_fault::tree::errorinstance_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fault::tree::ErrorInstance_strategy)
def test_fault::tree::errorinstance_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fault::tree::FaultTree_strategy)
@settings(max_examples=50)
def test_fault::tree::faulttree_instantiation(instance):
    assert isinstance(instance, fault::tree::FaultTree)

@given(instance=fault::tree::ErrorType_strategy)
@settings(max_examples=50)
def test_fault::tree::errortype_instantiation(instance):
    assert isinstance(instance, fault::tree::ErrorType)

@given(instance=fault::tree::ErrorType_strategy)
def test_fault::tree::errortype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fault::tree::ErrorType_strategy)
def test_fault::tree::errortype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fault::tree::FailureInstance_strategy)
@settings(max_examples=50)
def test_fault::tree::failureinstance_instantiation(instance):
    assert isinstance(instance, fault::tree::FailureInstance)

@given(instance=fault::tree::FailureInstance_strategy)
def test_fault::tree::failureinstance_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fault::tree::FailureInstance_strategy)
def test_fault::tree::failureinstance_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fault::tree::FailureType_strategy)
@settings(max_examples=50)
def test_fault::tree::failuretype_instantiation(instance):
    assert isinstance(instance, fault::tree::FailureType)

@given(instance=fault::tree::FailureType_strategy)
def test_fault::tree::failuretype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fault::tree::FailureType_strategy)
def test_fault::tree::failuretype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fault::tree::Event_strategy)
@settings(max_examples=50)
def test_fault::tree::event_instantiation(instance):
    assert isinstance(instance, fault::tree::Event)

@given(instance=fault::tree::Event_strategy)
def test_fault::tree::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fault::tree::Event_strategy)
def test_fault::tree::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fault::tree::Event_strategy)
def test_fault::tree::event_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=fault::tree::Event_strategy)
def test_fault::tree::event_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=fault::tree::Gate_strategy)
@settings(max_examples=50)
def test_fault::tree::gate_instantiation(instance):
    assert isinstance(instance, fault::tree::Gate)
