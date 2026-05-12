import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ProbabalisticEvent,
    faultTree_ExternalEvent,
    faultTree_UndevelopedEvent,
    faultTree_BasicEvent,
    Gate,
    faultTree_OR_Gate,
    faultTree_AND_Gate,
    Event,
    faultTree_IntermediateEvent,
    faultTree_ProbabalisticEvent,
    FTElement,
    faultTree_Gate,
    faultTree_FaultTree,
    faultTree_Event,
    faultTree_Connector,
    faultTree_FTElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_probabalisticevent_is_not_abstract():
    assert not inspect.isabstract(ProbabalisticEvent)


def test_probabalisticevent_constructor_exists():
    assert callable(ProbabalisticEvent.__init__)


def test_probabalisticevent_constructor_args():
    sig = inspect.signature(ProbabalisticEvent.__init__)
    params = list(sig.parameters.keys())



def test_faulttree_externalevent_is_not_abstract():
    assert not inspect.isabstract(faultTree_ExternalEvent)


def test_faulttree_externalevent_constructor_exists():
    assert callable(faultTree_ExternalEvent.__init__)


def test_faulttree_externalevent_constructor_args():
    sig = inspect.signature(faultTree_ExternalEvent.__init__)
    params = list(sig.parameters.keys())



def test_faulttree_undevelopedevent_is_not_abstract():
    assert not inspect.isabstract(faultTree_UndevelopedEvent)


def test_faulttree_undevelopedevent_constructor_exists():
    assert callable(faultTree_UndevelopedEvent.__init__)


def test_faulttree_undevelopedevent_constructor_args():
    sig = inspect.signature(faultTree_UndevelopedEvent.__init__)
    params = list(sig.parameters.keys())



def test_faulttree_basicevent_is_not_abstract():
    assert not inspect.isabstract(faultTree_BasicEvent)


def test_faulttree_basicevent_constructor_exists():
    assert callable(faultTree_BasicEvent.__init__)


def test_faulttree_basicevent_constructor_args():
    sig = inspect.signature(faultTree_BasicEvent.__init__)
    params = list(sig.parameters.keys())



def test_gate_is_not_abstract():
    assert not inspect.isabstract(Gate)


def test_gate_constructor_exists():
    assert callable(Gate.__init__)


def test_gate_constructor_args():
    sig = inspect.signature(Gate.__init__)
    params = list(sig.parameters.keys())



def test_faulttree_or_gate_is_not_abstract():
    assert not inspect.isabstract(faultTree_OR_Gate)


def test_faulttree_or_gate_constructor_exists():
    assert callable(faultTree_OR_Gate.__init__)


def test_faulttree_or_gate_constructor_args():
    sig = inspect.signature(faultTree_OR_Gate.__init__)
    params = list(sig.parameters.keys())



def test_faulttree_and_gate_is_not_abstract():
    assert not inspect.isabstract(faultTree_AND_Gate)


def test_faulttree_and_gate_constructor_exists():
    assert callable(faultTree_AND_Gate.__init__)


def test_faulttree_and_gate_constructor_args():
    sig = inspect.signature(faultTree_AND_Gate.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_faulttree_intermediateevent_is_not_abstract():
    assert not inspect.isabstract(faultTree_IntermediateEvent)


def test_faulttree_intermediateevent_constructor_exists():
    assert callable(faultTree_IntermediateEvent.__init__)


def test_faulttree_intermediateevent_constructor_args():
    sig = inspect.signature(faultTree_IntermediateEvent.__init__)
    params = list(sig.parameters.keys())



def test_faulttree_probabalisticevent_is_not_abstract():
    assert not inspect.isabstract(faultTree_ProbabalisticEvent)


def test_faulttree_probabalisticevent_constructor_exists():
    assert callable(faultTree_ProbabalisticEvent.__init__)


def test_faulttree_probabalisticevent_constructor_args():
    sig = inspect.signature(faultTree_ProbabalisticEvent.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"

def test_faulttree_probabalisticevent_has_probability():
    assert hasattr(faultTree_ProbabalisticEvent, "probability")
    descriptor = None
    for klass in faultTree_ProbabalisticEvent.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)



def test_ftelement_is_not_abstract():
    assert not inspect.isabstract(FTElement)


def test_ftelement_constructor_exists():
    assert callable(FTElement.__init__)


def test_ftelement_constructor_args():
    sig = inspect.signature(FTElement.__init__)
    params = list(sig.parameters.keys())



def test_faulttree_gate_is_not_abstract():
    assert not inspect.isabstract(faultTree_Gate)


def test_faulttree_gate_constructor_exists():
    assert callable(faultTree_Gate.__init__)


def test_faulttree_gate_constructor_args():
    sig = inspect.signature(faultTree_Gate.__init__)
    params = list(sig.parameters.keys())



def test_faulttree_faulttree_is_not_abstract():
    assert not inspect.isabstract(faultTree_FaultTree)


def test_faulttree_faulttree_constructor_exists():
    assert callable(faultTree_FaultTree.__init__)


def test_faulttree_faulttree_constructor_args():
    sig = inspect.signature(faultTree_FaultTree.__init__)
    params = list(sig.parameters.keys())



def test_faulttree_event_is_not_abstract():
    assert not inspect.isabstract(faultTree_Event)


def test_faulttree_event_constructor_exists():
    assert callable(faultTree_Event.__init__)


def test_faulttree_event_constructor_args():
    sig = inspect.signature(faultTree_Event.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "description" in params, "Missing parameter 'description'"

def test_faulttree_event_has_title():
    assert hasattr(faultTree_Event, "title")
    descriptor = None
    for klass in faultTree_Event.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_faulttree_event_has_description():
    assert hasattr(faultTree_Event, "description")
    descriptor = None
    for klass in faultTree_Event.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_faulttree_connector_is_not_abstract():
    assert not inspect.isabstract(faultTree_Connector)


def test_faulttree_connector_constructor_exists():
    assert callable(faultTree_Connector.__init__)


def test_faulttree_connector_constructor_args():
    sig = inspect.signature(faultTree_Connector.__init__)
    params = list(sig.parameters.keys())



def test_faulttree_ftelement_is_not_abstract():
    assert not inspect.isabstract(faultTree_FTElement)


def test_faulttree_ftelement_constructor_exists():
    assert callable(faultTree_FTElement.__init__)


def test_faulttree_ftelement_constructor_args():
    sig = inspect.signature(faultTree_FTElement.__init__)
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
ProbabalisticEvent_strategy = st.builds(
    ProbabalisticEvent,
)
faultTree_ExternalEvent_strategy = st.builds(
    faultTree_ExternalEvent,
)
faultTree_UndevelopedEvent_strategy = st.builds(
    faultTree_UndevelopedEvent,
)
faultTree_BasicEvent_strategy = st.builds(
    faultTree_BasicEvent,
)
Gate_strategy = st.builds(
    Gate,
)
faultTree_OR_Gate_strategy = st.builds(
    faultTree_OR_Gate,
)
faultTree_AND_Gate_strategy = st.builds(
    faultTree_AND_Gate,
)
Event_strategy = st.builds(
    Event,
)
faultTree_IntermediateEvent_strategy = st.builds(
    faultTree_IntermediateEvent,
)
faultTree_ProbabalisticEvent_strategy = st.builds(
    faultTree_ProbabalisticEvent,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
FTElement_strategy = st.builds(
    FTElement,
)
faultTree_Gate_strategy = st.builds(
    faultTree_Gate,
)
faultTree_FaultTree_strategy = st.builds(
    faultTree_FaultTree,
)
faultTree_Event_strategy = st.builds(
    faultTree_Event,
    title=
        safe_text,
    description=
        safe_text
)
faultTree_Connector_strategy = st.builds(
    faultTree_Connector,
)
faultTree_FTElement_strategy = st.builds(
    faultTree_FTElement,
)

@given(instance=ProbabalisticEvent_strategy)
@settings(max_examples=50)
def test_probabalisticevent_instantiation(instance):
    assert isinstance(instance, ProbabalisticEvent)

@given(instance=faultTree_ExternalEvent_strategy)
@settings(max_examples=50)
def test_faulttree_externalevent_instantiation(instance):
    assert isinstance(instance, faultTree_ExternalEvent)

@given(instance=faultTree_UndevelopedEvent_strategy)
@settings(max_examples=50)
def test_faulttree_undevelopedevent_instantiation(instance):
    assert isinstance(instance, faultTree_UndevelopedEvent)

@given(instance=faultTree_BasicEvent_strategy)
@settings(max_examples=50)
def test_faulttree_basicevent_instantiation(instance):
    assert isinstance(instance, faultTree_BasicEvent)

@given(instance=Gate_strategy)
@settings(max_examples=50)
def test_gate_instantiation(instance):
    assert isinstance(instance, Gate)

@given(instance=faultTree_OR_Gate_strategy)
@settings(max_examples=50)
def test_faulttree_or_gate_instantiation(instance):
    assert isinstance(instance, faultTree_OR_Gate)

@given(instance=faultTree_AND_Gate_strategy)
@settings(max_examples=50)
def test_faulttree_and_gate_instantiation(instance):
    assert isinstance(instance, faultTree_AND_Gate)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=faultTree_IntermediateEvent_strategy)
@settings(max_examples=50)
def test_faulttree_intermediateevent_instantiation(instance):
    assert isinstance(instance, faultTree_IntermediateEvent)

@given(instance=faultTree_ProbabalisticEvent_strategy)
@settings(max_examples=50)
def test_faulttree_probabalisticevent_instantiation(instance):
    assert isinstance(instance, faultTree_ProbabalisticEvent)



@given(instance=faultTree_ProbabalisticEvent_strategy)
def test_faulttree_probabalisticevent_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=FTElement_strategy)
@settings(max_examples=50)
def test_ftelement_instantiation(instance):
    assert isinstance(instance, FTElement)

@given(instance=faultTree_Gate_strategy)
@settings(max_examples=50)
def test_faulttree_gate_instantiation(instance):
    assert isinstance(instance, faultTree_Gate)

@given(instance=faultTree_FaultTree_strategy)
@settings(max_examples=50)
def test_faulttree_faulttree_instantiation(instance):
    assert isinstance(instance, faultTree_FaultTree)

@given(instance=faultTree_Event_strategy)
@settings(max_examples=50)
def test_faulttree_event_instantiation(instance):
    assert isinstance(instance, faultTree_Event)



@given(instance=faultTree_Event_strategy)
def test_faulttree_event_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=faultTree_Event_strategy)
def test_faulttree_event_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=faultTree_Connector_strategy)
@settings(max_examples=50)
def test_faulttree_connector_instantiation(instance):
    assert isinstance(instance, faultTree_Connector)

@given(instance=faultTree_FTElement_strategy)
@settings(max_examples=50)
def test_faulttree_ftelement_instantiation(instance):
    assert isinstance(instance, faultTree_FTElement)
