import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Event,
    faultTree::IntermediateEvent,
    faultTree::ProbabalisticEvent,
    FTElement,
    faultTree::Event,
    faultTree::FaultTree,
    faultTree::Gate,
    faultTree::Connector,
    faultTree::FTElement,
    ProbabalisticEvent,
    faultTree::UndevelopedEvent,
    faultTree::ExternalEvent,
    faultTree::BasicEvent,
    Gate,
    faultTree::AND::Gate,
    faultTree::OR::Gate,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_faulttree::intermediateevent_is_not_abstract():
    assert not inspect.isabstract(faultTree::IntermediateEvent)


def test_faulttree::intermediateevent_constructor_exists():
    assert callable(faultTree::IntermediateEvent.__init__)


def test_faulttree::intermediateevent_constructor_args():
    sig = inspect.signature(faultTree::IntermediateEvent.__init__)
    params = list(sig.parameters.keys())



def test_faulttree::probabalisticevent_is_not_abstract():
    assert not inspect.isabstract(faultTree::ProbabalisticEvent)


def test_faulttree::probabalisticevent_constructor_exists():
    assert callable(faultTree::ProbabalisticEvent.__init__)


def test_faulttree::probabalisticevent_constructor_args():
    sig = inspect.signature(faultTree::ProbabalisticEvent.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"

def test_faulttree::probabalisticevent_has_probability():
    assert hasattr(faultTree::ProbabalisticEvent, "probability")
    descriptor = None
    for klass in faultTree::ProbabalisticEvent.__mro__:
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



def test_faulttree::event_is_not_abstract():
    assert not inspect.isabstract(faultTree::Event)


def test_faulttree::event_constructor_exists():
    assert callable(faultTree::Event.__init__)


def test_faulttree::event_constructor_args():
    sig = inspect.signature(faultTree::Event.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "title" in params, "Missing parameter 'title'"

def test_faulttree::event_has_description():
    assert hasattr(faultTree::Event, "description")
    descriptor = None
    for klass in faultTree::Event.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_faulttree::event_has_title():
    assert hasattr(faultTree::Event, "title")
    descriptor = None
    for klass in faultTree::Event.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_faulttree::faulttree_is_not_abstract():
    assert not inspect.isabstract(faultTree::FaultTree)


def test_faulttree::faulttree_constructor_exists():
    assert callable(faultTree::FaultTree.__init__)


def test_faulttree::faulttree_constructor_args():
    sig = inspect.signature(faultTree::FaultTree.__init__)
    params = list(sig.parameters.keys())



def test_faulttree::gate_is_not_abstract():
    assert not inspect.isabstract(faultTree::Gate)


def test_faulttree::gate_constructor_exists():
    assert callable(faultTree::Gate.__init__)


def test_faulttree::gate_constructor_args():
    sig = inspect.signature(faultTree::Gate.__init__)
    params = list(sig.parameters.keys())



def test_faulttree::connector_is_not_abstract():
    assert not inspect.isabstract(faultTree::Connector)


def test_faulttree::connector_constructor_exists():
    assert callable(faultTree::Connector.__init__)


def test_faulttree::connector_constructor_args():
    sig = inspect.signature(faultTree::Connector.__init__)
    params = list(sig.parameters.keys())



def test_faulttree::ftelement_is_not_abstract():
    assert not inspect.isabstract(faultTree::FTElement)


def test_faulttree::ftelement_constructor_exists():
    assert callable(faultTree::FTElement.__init__)


def test_faulttree::ftelement_constructor_args():
    sig = inspect.signature(faultTree::FTElement.__init__)
    params = list(sig.parameters.keys())



def test_probabalisticevent_is_not_abstract():
    assert not inspect.isabstract(ProbabalisticEvent)


def test_probabalisticevent_constructor_exists():
    assert callable(ProbabalisticEvent.__init__)


def test_probabalisticevent_constructor_args():
    sig = inspect.signature(ProbabalisticEvent.__init__)
    params = list(sig.parameters.keys())



def test_faulttree::undevelopedevent_is_not_abstract():
    assert not inspect.isabstract(faultTree::UndevelopedEvent)


def test_faulttree::undevelopedevent_constructor_exists():
    assert callable(faultTree::UndevelopedEvent.__init__)


def test_faulttree::undevelopedevent_constructor_args():
    sig = inspect.signature(faultTree::UndevelopedEvent.__init__)
    params = list(sig.parameters.keys())



def test_faulttree::externalevent_is_not_abstract():
    assert not inspect.isabstract(faultTree::ExternalEvent)


def test_faulttree::externalevent_constructor_exists():
    assert callable(faultTree::ExternalEvent.__init__)


def test_faulttree::externalevent_constructor_args():
    sig = inspect.signature(faultTree::ExternalEvent.__init__)
    params = list(sig.parameters.keys())



def test_faulttree::basicevent_is_not_abstract():
    assert not inspect.isabstract(faultTree::BasicEvent)


def test_faulttree::basicevent_constructor_exists():
    assert callable(faultTree::BasicEvent.__init__)


def test_faulttree::basicevent_constructor_args():
    sig = inspect.signature(faultTree::BasicEvent.__init__)
    params = list(sig.parameters.keys())



def test_gate_is_not_abstract():
    assert not inspect.isabstract(Gate)


def test_gate_constructor_exists():
    assert callable(Gate.__init__)


def test_gate_constructor_args():
    sig = inspect.signature(Gate.__init__)
    params = list(sig.parameters.keys())



def test_faulttree::and::gate_is_not_abstract():
    assert not inspect.isabstract(faultTree::AND::Gate)


def test_faulttree::and::gate_constructor_exists():
    assert callable(faultTree::AND::Gate.__init__)


def test_faulttree::and::gate_constructor_args():
    sig = inspect.signature(faultTree::AND::Gate.__init__)
    params = list(sig.parameters.keys())



def test_faulttree::or::gate_is_not_abstract():
    assert not inspect.isabstract(faultTree::OR::Gate)


def test_faulttree::or::gate_constructor_exists():
    assert callable(faultTree::OR::Gate.__init__)


def test_faulttree::or::gate_constructor_args():
    sig = inspect.signature(faultTree::OR::Gate.__init__)
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
Event_strategy = st.builds(
    Event,
)
faultTree::IntermediateEvent_strategy = st.builds(
    faultTree::IntermediateEvent,
)
faultTree::ProbabalisticEvent_strategy = st.builds(
    faultTree::ProbabalisticEvent,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
FTElement_strategy = st.builds(
    FTElement,
)
faultTree::Event_strategy = st.builds(
    faultTree::Event,
    description=
        safe_text,
    title=
        safe_text
)
faultTree::FaultTree_strategy = st.builds(
    faultTree::FaultTree,
)
faultTree::Gate_strategy = st.builds(
    faultTree::Gate,
)
faultTree::Connector_strategy = st.builds(
    faultTree::Connector,
)
faultTree::FTElement_strategy = st.builds(
    faultTree::FTElement,
)
ProbabalisticEvent_strategy = st.builds(
    ProbabalisticEvent,
)
faultTree::UndevelopedEvent_strategy = st.builds(
    faultTree::UndevelopedEvent,
)
faultTree::ExternalEvent_strategy = st.builds(
    faultTree::ExternalEvent,
)
faultTree::BasicEvent_strategy = st.builds(
    faultTree::BasicEvent,
)
Gate_strategy = st.builds(
    Gate,
)
faultTree::AND::Gate_strategy = st.builds(
    faultTree::AND::Gate,
)
faultTree::OR::Gate_strategy = st.builds(
    faultTree::OR::Gate,
)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=faultTree::IntermediateEvent_strategy)
@settings(max_examples=50)
def test_faulttree::intermediateevent_instantiation(instance):
    assert isinstance(instance, faultTree::IntermediateEvent)

@given(instance=faultTree::ProbabalisticEvent_strategy)
@settings(max_examples=50)
def test_faulttree::probabalisticevent_instantiation(instance):
    assert isinstance(instance, faultTree::ProbabalisticEvent)

@given(instance=faultTree::ProbabalisticEvent_strategy)
def test_faulttree::probabalisticevent_probability_type(instance):
    assert isinstance(instance.probability, float)


@given(instance=faultTree::ProbabalisticEvent_strategy)
def test_faulttree::probabalisticevent_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=FTElement_strategy)
@settings(max_examples=50)
def test_ftelement_instantiation(instance):
    assert isinstance(instance, FTElement)

@given(instance=faultTree::Event_strategy)
@settings(max_examples=50)
def test_faulttree::event_instantiation(instance):
    assert isinstance(instance, faultTree::Event)

@given(instance=faultTree::Event_strategy)
def test_faulttree::event_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=faultTree::Event_strategy)
def test_faulttree::event_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=faultTree::Event_strategy)
def test_faulttree::event_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=faultTree::Event_strategy)
def test_faulttree::event_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=faultTree::FaultTree_strategy)
@settings(max_examples=50)
def test_faulttree::faulttree_instantiation(instance):
    assert isinstance(instance, faultTree::FaultTree)

@given(instance=faultTree::Gate_strategy)
@settings(max_examples=50)
def test_faulttree::gate_instantiation(instance):
    assert isinstance(instance, faultTree::Gate)

@given(instance=faultTree::Connector_strategy)
@settings(max_examples=50)
def test_faulttree::connector_instantiation(instance):
    assert isinstance(instance, faultTree::Connector)

@given(instance=faultTree::FTElement_strategy)
@settings(max_examples=50)
def test_faulttree::ftelement_instantiation(instance):
    assert isinstance(instance, faultTree::FTElement)

@given(instance=ProbabalisticEvent_strategy)
@settings(max_examples=50)
def test_probabalisticevent_instantiation(instance):
    assert isinstance(instance, ProbabalisticEvent)

@given(instance=faultTree::UndevelopedEvent_strategy)
@settings(max_examples=50)
def test_faulttree::undevelopedevent_instantiation(instance):
    assert isinstance(instance, faultTree::UndevelopedEvent)

@given(instance=faultTree::ExternalEvent_strategy)
@settings(max_examples=50)
def test_faulttree::externalevent_instantiation(instance):
    assert isinstance(instance, faultTree::ExternalEvent)

@given(instance=faultTree::BasicEvent_strategy)
@settings(max_examples=50)
def test_faulttree::basicevent_instantiation(instance):
    assert isinstance(instance, faultTree::BasicEvent)

@given(instance=Gate_strategy)
@settings(max_examples=50)
def test_gate_instantiation(instance):
    assert isinstance(instance, Gate)

@given(instance=faultTree::AND::Gate_strategy)
@settings(max_examples=50)
def test_faulttree::and::gate_instantiation(instance):
    assert isinstance(instance, faultTree::AND::Gate)

@given(instance=faultTree::OR::Gate_strategy)
@settings(max_examples=50)
def test_faulttree::or::gate_instantiation(instance):
    assert isinstance(instance, faultTree::OR::Gate)
