import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Transition,
    Step,
    StepToTransition,
    TransitionToStep,
    Connection,
    Grafcet::StepToTransition,
    Grafcet::TransitionToStep,
    Grafcet,
    LocatedElement,
    Grafcet::NamedElement,
    Grafcet::LocatedElement,
    Element,
    Grafcet::Transition,
    Grafcet::Step,
    NamedElement,
    Grafcet::Element,
    Grafcet::Connection,
    Grafcet::Grafcet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_step_is_not_abstract():
    assert not inspect.isabstract(Step)


def test_step_constructor_exists():
    assert callable(Step.__init__)


def test_step_constructor_args():
    sig = inspect.signature(Step.__init__)
    params = list(sig.parameters.keys())



def test_steptotransition_is_not_abstract():
    assert not inspect.isabstract(StepToTransition)


def test_steptotransition_constructor_exists():
    assert callable(StepToTransition.__init__)


def test_steptotransition_constructor_args():
    sig = inspect.signature(StepToTransition.__init__)
    params = list(sig.parameters.keys())



def test_transitiontostep_is_not_abstract():
    assert not inspect.isabstract(TransitionToStep)


def test_transitiontostep_constructor_exists():
    assert callable(TransitionToStep.__init__)


def test_transitiontostep_constructor_args():
    sig = inspect.signature(TransitionToStep.__init__)
    params = list(sig.parameters.keys())



def test_connection_is_not_abstract():
    assert not inspect.isabstract(Connection)


def test_connection_constructor_exists():
    assert callable(Connection.__init__)


def test_connection_constructor_args():
    sig = inspect.signature(Connection.__init__)
    params = list(sig.parameters.keys())



def test_grafcet::steptotransition_is_not_abstract():
    assert not inspect.isabstract(Grafcet::StepToTransition)


def test_grafcet::steptotransition_constructor_exists():
    assert callable(Grafcet::StepToTransition.__init__)


def test_grafcet::steptotransition_constructor_args():
    sig = inspect.signature(Grafcet::StepToTransition.__init__)
    params = list(sig.parameters.keys())



def test_grafcet::transitiontostep_is_not_abstract():
    assert not inspect.isabstract(Grafcet::TransitionToStep)


def test_grafcet::transitiontostep_constructor_exists():
    assert callable(Grafcet::TransitionToStep.__init__)


def test_grafcet::transitiontostep_constructor_args():
    sig = inspect.signature(Grafcet::TransitionToStep.__init__)
    params = list(sig.parameters.keys())



def test_grafcet_is_not_abstract():
    assert not inspect.isabstract(Grafcet)


def test_grafcet_constructor_exists():
    assert callable(Grafcet.__init__)


def test_grafcet_constructor_args():
    sig = inspect.signature(Grafcet.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_grafcet::namedelement_is_not_abstract():
    assert not inspect.isabstract(Grafcet::NamedElement)


def test_grafcet::namedelement_constructor_exists():
    assert callable(Grafcet::NamedElement.__init__)


def test_grafcet::namedelement_constructor_args():
    sig = inspect.signature(Grafcet::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_grafcet::namedelement_has_name():
    assert hasattr(Grafcet::NamedElement, "name")
    descriptor = None
    for klass in Grafcet::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_grafcet::locatedelement_is_not_abstract():
    assert not inspect.isabstract(Grafcet::LocatedElement)


def test_grafcet::locatedelement_constructor_exists():
    assert callable(Grafcet::LocatedElement.__init__)


def test_grafcet::locatedelement_constructor_args():
    sig = inspect.signature(Grafcet::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_grafcet::locatedelement_has_location():
    assert hasattr(Grafcet::LocatedElement, "location")
    descriptor = None
    for klass in Grafcet::LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_grafcet::transition_is_not_abstract():
    assert not inspect.isabstract(Grafcet::Transition)


def test_grafcet::transition_constructor_exists():
    assert callable(Grafcet::Transition.__init__)


def test_grafcet::transition_constructor_args():
    sig = inspect.signature(Grafcet::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_grafcet::transition_has_condition():
    assert hasattr(Grafcet::Transition, "condition")
    descriptor = None
    for klass in Grafcet::Transition.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_grafcet::step_is_not_abstract():
    assert not inspect.isabstract(Grafcet::Step)


def test_grafcet::step_constructor_exists():
    assert callable(Grafcet::Step.__init__)


def test_grafcet::step_constructor_args():
    sig = inspect.signature(Grafcet::Step.__init__)
    params = list(sig.parameters.keys())
    assert "isActive" in params, "Missing parameter 'isActive'"
    assert "action" in params, "Missing parameter 'action'"
    assert "isInitial" in params, "Missing parameter 'isInitial'"

def test_grafcet::step_has_isActive():
    assert hasattr(Grafcet::Step, "isActive")
    descriptor = None
    for klass in Grafcet::Step.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)

def test_grafcet::step_has_action():
    assert hasattr(Grafcet::Step, "action")
    descriptor = None
    for klass in Grafcet::Step.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_grafcet::step_has_isInitial():
    assert hasattr(Grafcet::Step, "isInitial")
    descriptor = None
    for klass in Grafcet::Step.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_grafcet::element_is_not_abstract():
    assert not inspect.isabstract(Grafcet::Element)


def test_grafcet::element_constructor_exists():
    assert callable(Grafcet::Element.__init__)


def test_grafcet::element_constructor_args():
    sig = inspect.signature(Grafcet::Element.__init__)
    params = list(sig.parameters.keys())



def test_grafcet::connection_is_not_abstract():
    assert not inspect.isabstract(Grafcet::Connection)


def test_grafcet::connection_constructor_exists():
    assert callable(Grafcet::Connection.__init__)


def test_grafcet::connection_constructor_args():
    sig = inspect.signature(Grafcet::Connection.__init__)
    params = list(sig.parameters.keys())



def test_grafcet::grafcet_is_not_abstract():
    assert not inspect.isabstract(Grafcet::Grafcet)


def test_grafcet::grafcet_constructor_exists():
    assert callable(Grafcet::Grafcet.__init__)


def test_grafcet::grafcet_constructor_args():
    sig = inspect.signature(Grafcet::Grafcet.__init__)
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
Transition_strategy = st.builds(
    Transition,
)
Step_strategy = st.builds(
    Step,
)
StepToTransition_strategy = st.builds(
    StepToTransition,
)
TransitionToStep_strategy = st.builds(
    TransitionToStep,
)
Connection_strategy = st.builds(
    Connection,
)
Grafcet::StepToTransition_strategy = st.builds(
    Grafcet::StepToTransition,
)
Grafcet::TransitionToStep_strategy = st.builds(
    Grafcet::TransitionToStep,
)
Grafcet_strategy = st.builds(
    Grafcet,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
Grafcet::NamedElement_strategy = st.builds(
    Grafcet::NamedElement,
    name=
        safe_text
)
Grafcet::LocatedElement_strategy = st.builds(
    Grafcet::LocatedElement,
    location=
        safe_text
)
Element_strategy = st.builds(
    Element,
)
Grafcet::Transition_strategy = st.builds(
    Grafcet::Transition,
    condition=
        safe_text
)
Grafcet::Step_strategy = st.builds(
    Grafcet::Step,
    isActive=
        safe_text,
    action=
        safe_text,
    isInitial=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Grafcet::Element_strategy = st.builds(
    Grafcet::Element,
)
Grafcet::Connection_strategy = st.builds(
    Grafcet::Connection,
)
Grafcet::Grafcet_strategy = st.builds(
    Grafcet::Grafcet,
)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=Step_strategy)
@settings(max_examples=50)
def test_step_instantiation(instance):
    assert isinstance(instance, Step)

@given(instance=StepToTransition_strategy)
@settings(max_examples=50)
def test_steptotransition_instantiation(instance):
    assert isinstance(instance, StepToTransition)

@given(instance=TransitionToStep_strategy)
@settings(max_examples=50)
def test_transitiontostep_instantiation(instance):
    assert isinstance(instance, TransitionToStep)

@given(instance=Connection_strategy)
@settings(max_examples=50)
def test_connection_instantiation(instance):
    assert isinstance(instance, Connection)

@given(instance=Grafcet::StepToTransition_strategy)
@settings(max_examples=50)
def test_grafcet::steptotransition_instantiation(instance):
    assert isinstance(instance, Grafcet::StepToTransition)

@given(instance=Grafcet::TransitionToStep_strategy)
@settings(max_examples=50)
def test_grafcet::transitiontostep_instantiation(instance):
    assert isinstance(instance, Grafcet::TransitionToStep)

@given(instance=Grafcet_strategy)
@settings(max_examples=50)
def test_grafcet_instantiation(instance):
    assert isinstance(instance, Grafcet)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=Grafcet::NamedElement_strategy)
@settings(max_examples=50)
def test_grafcet::namedelement_instantiation(instance):
    assert isinstance(instance, Grafcet::NamedElement)

@given(instance=Grafcet::NamedElement_strategy)
def test_grafcet::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Grafcet::NamedElement_strategy)
def test_grafcet::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Grafcet::LocatedElement_strategy)
@settings(max_examples=50)
def test_grafcet::locatedelement_instantiation(instance):
    assert isinstance(instance, Grafcet::LocatedElement)

@given(instance=Grafcet::LocatedElement_strategy)
def test_grafcet::locatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=Grafcet::LocatedElement_strategy)
def test_grafcet::locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=Grafcet::Transition_strategy)
@settings(max_examples=50)
def test_grafcet::transition_instantiation(instance):
    assert isinstance(instance, Grafcet::Transition)

@given(instance=Grafcet::Transition_strategy)
def test_grafcet::transition_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=Grafcet::Transition_strategy)
def test_grafcet::transition_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=Grafcet::Step_strategy)
@settings(max_examples=50)
def test_grafcet::step_instantiation(instance):
    assert isinstance(instance, Grafcet::Step)

@given(instance=Grafcet::Step_strategy)
def test_grafcet::step_isActive_type(instance):
    assert isinstance(instance.isActive, str)


@given(instance=Grafcet::Step_strategy)
def test_grafcet::step_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=Grafcet::Step_strategy)
def test_grafcet::step_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=Grafcet::Step_strategy)
def test_grafcet::step_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=Grafcet::Step_strategy)
def test_grafcet::step_isInitial_type(instance):
    assert isinstance(instance.isInitial, str)


@given(instance=Grafcet::Step_strategy)
def test_grafcet::step_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Grafcet::Element_strategy)
@settings(max_examples=50)
def test_grafcet::element_instantiation(instance):
    assert isinstance(instance, Grafcet::Element)

@given(instance=Grafcet::Connection_strategy)
@settings(max_examples=50)
def test_grafcet::connection_instantiation(instance):
    assert isinstance(instance, Grafcet::Connection)

@given(instance=Grafcet::Grafcet_strategy)
@settings(max_examples=50)
def test_grafcet::grafcet_instantiation(instance):
    assert isinstance(instance, Grafcet::Grafcet)
