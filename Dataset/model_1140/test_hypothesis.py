import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Activity,
    statemodel::Entity,
    Element,
    statemodel::State,
    statemodel::Statemachine,
    statemodel::Annotation,
    statemodel::Element,
    statemodel::Import,
    statemodel::Model,
    statemodel::Transition,
    statemodel::TransitionBlock,
    statemodel::Activity,
    StateType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_activity_is_not_abstract():
    assert not inspect.isabstract(Activity)


def test_activity_constructor_exists():
    assert callable(Activity.__init__)


def test_activity_constructor_args():
    sig = inspect.signature(Activity.__init__)
    params = list(sig.parameters.keys())



def test_statemodel::entity_is_not_abstract():
    assert not inspect.isabstract(statemodel::Entity)


def test_statemodel::entity_constructor_exists():
    assert callable(statemodel::Entity.__init__)


def test_statemodel::entity_constructor_args():
    sig = inspect.signature(statemodel::Entity.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_statemodel::state_is_not_abstract():
    assert not inspect.isabstract(statemodel::State)


def test_statemodel::state_constructor_exists():
    assert callable(statemodel::State.__init__)


def test_statemodel::state_constructor_args():
    sig = inspect.signature(statemodel::State.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemodel::state_has_type():
    assert hasattr(statemodel::State, "type")
    descriptor = None
    for klass in statemodel::State.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_statemodel::state_has_name():
    assert hasattr(statemodel::State, "name")
    descriptor = None
    for klass in statemodel::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemodel::statemachine_is_not_abstract():
    assert not inspect.isabstract(statemodel::Statemachine)


def test_statemodel::statemachine_constructor_exists():
    assert callable(statemodel::Statemachine.__init__)


def test_statemodel::statemachine_constructor_args():
    sig = inspect.signature(statemodel::Statemachine.__init__)
    params = list(sig.parameters.keys())



def test_statemodel::annotation_is_not_abstract():
    assert not inspect.isabstract(statemodel::Annotation)


def test_statemodel::annotation_constructor_exists():
    assert callable(statemodel::Annotation.__init__)


def test_statemodel::annotation_constructor_args():
    sig = inspect.signature(statemodel::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_statemodel::element_is_not_abstract():
    assert not inspect.isabstract(statemodel::Element)


def test_statemodel::element_constructor_exists():
    assert callable(statemodel::Element.__init__)


def test_statemodel::element_constructor_args():
    sig = inspect.signature(statemodel::Element.__init__)
    params = list(sig.parameters.keys())



def test_statemodel::import_is_not_abstract():
    assert not inspect.isabstract(statemodel::Import)


def test_statemodel::import_constructor_exists():
    assert callable(statemodel::Import.__init__)


def test_statemodel::import_constructor_args():
    sig = inspect.signature(statemodel::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_statemodel::import_has_importURI():
    assert hasattr(statemodel::Import, "importURI")
    descriptor = None
    for klass in statemodel::Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_statemodel::model_is_not_abstract():
    assert not inspect.isabstract(statemodel::Model)


def test_statemodel::model_constructor_exists():
    assert callable(statemodel::Model.__init__)


def test_statemodel::model_constructor_args():
    sig = inspect.signature(statemodel::Model.__init__)
    params = list(sig.parameters.keys())



def test_statemodel::transition_is_not_abstract():
    assert not inspect.isabstract(statemodel::Transition)


def test_statemodel::transition_constructor_exists():
    assert callable(statemodel::Transition.__init__)


def test_statemodel::transition_constructor_args():
    sig = inspect.signature(statemodel::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "guard" in params, "Missing parameter 'guard'"

def test_statemodel::transition_has_action():
    assert hasattr(statemodel::Transition, "action")
    descriptor = None
    for klass in statemodel::Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_statemodel::transition_has_guard():
    assert hasattr(statemodel::Transition, "guard")
    descriptor = None
    for klass in statemodel::Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)



def test_statemodel::transitionblock_is_not_abstract():
    assert not inspect.isabstract(statemodel::TransitionBlock)


def test_statemodel::transitionblock_constructor_exists():
    assert callable(statemodel::TransitionBlock.__init__)


def test_statemodel::transitionblock_constructor_args():
    sig = inspect.signature(statemodel::TransitionBlock.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_statemodel::transitionblock_has_event():
    assert hasattr(statemodel::TransitionBlock, "event")
    descriptor = None
    for klass in statemodel::TransitionBlock.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_statemodel::activity_is_not_abstract():
    assert not inspect.isabstract(statemodel::Activity)


def test_statemodel::activity_constructor_exists():
    assert callable(statemodel::Activity.__init__)


def test_statemodel::activity_constructor_args():
    sig = inspect.signature(statemodel::Activity.__init__)
    params = list(sig.parameters.keys())

def test_statetype_exists():
    # Check that the Enumeration exists
    assert StateType is not None

def test_statetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StateType]
    expected_literals = [
        "NONE",
        "FINAL",
        "INITIAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StateType"


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
Activity_strategy = st.builds(
    Activity,
)
statemodel::Entity_strategy = st.builds(
    statemodel::Entity,
)
Element_strategy = st.builds(
    Element,
)
statemodel::State_strategy = st.builds(
    statemodel::State,
    type=
        safe_text,
    name=
        safe_text
)
statemodel::Statemachine_strategy = st.builds(
    statemodel::Statemachine,
)
statemodel::Annotation_strategy = st.builds(
    statemodel::Annotation,
)
statemodel::Element_strategy = st.builds(
    statemodel::Element,
)
statemodel::Import_strategy = st.builds(
    statemodel::Import,
    importURI=
        safe_text
)
statemodel::Model_strategy = st.builds(
    statemodel::Model,
)
statemodel::Transition_strategy = st.builds(
    statemodel::Transition,
    action=
        safe_text,
    guard=
        safe_text
)
statemodel::TransitionBlock_strategy = st.builds(
    statemodel::TransitionBlock,
    event=
        safe_text
)
statemodel::Activity_strategy = st.builds(
    statemodel::Activity,
)

@given(instance=Activity_strategy)
@settings(max_examples=50)
def test_activity_instantiation(instance):
    assert isinstance(instance, Activity)

@given(instance=statemodel::Entity_strategy)
@settings(max_examples=50)
def test_statemodel::entity_instantiation(instance):
    assert isinstance(instance, statemodel::Entity)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=statemodel::State_strategy)
@settings(max_examples=50)
def test_statemodel::state_instantiation(instance):
    assert isinstance(instance, statemodel::State)

@given(instance=statemodel::State_strategy)
def test_statemodel::state_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=statemodel::State_strategy)
def test_statemodel::state_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=statemodel::State_strategy)
def test_statemodel::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemodel::State_strategy)
def test_statemodel::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemodel::Statemachine_strategy)
@settings(max_examples=50)
def test_statemodel::statemachine_instantiation(instance):
    assert isinstance(instance, statemodel::Statemachine)

@given(instance=statemodel::Annotation_strategy)
@settings(max_examples=50)
def test_statemodel::annotation_instantiation(instance):
    assert isinstance(instance, statemodel::Annotation)

@given(instance=statemodel::Element_strategy)
@settings(max_examples=50)
def test_statemodel::element_instantiation(instance):
    assert isinstance(instance, statemodel::Element)

@given(instance=statemodel::Import_strategy)
@settings(max_examples=50)
def test_statemodel::import_instantiation(instance):
    assert isinstance(instance, statemodel::Import)

@given(instance=statemodel::Import_strategy)
def test_statemodel::import_importURI_type(instance):
    assert isinstance(instance.importURI, str)


@given(instance=statemodel::Import_strategy)
def test_statemodel::import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=statemodel::Model_strategy)
@settings(max_examples=50)
def test_statemodel::model_instantiation(instance):
    assert isinstance(instance, statemodel::Model)

@given(instance=statemodel::Transition_strategy)
@settings(max_examples=50)
def test_statemodel::transition_instantiation(instance):
    assert isinstance(instance, statemodel::Transition)

@given(instance=statemodel::Transition_strategy)
def test_statemodel::transition_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=statemodel::Transition_strategy)
def test_statemodel::transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=statemodel::Transition_strategy)
def test_statemodel::transition_guard_type(instance):
    assert isinstance(instance.guard, str)


@given(instance=statemodel::Transition_strategy)
def test_statemodel::transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=statemodel::TransitionBlock_strategy)
@settings(max_examples=50)
def test_statemodel::transitionblock_instantiation(instance):
    assert isinstance(instance, statemodel::TransitionBlock)

@given(instance=statemodel::TransitionBlock_strategy)
def test_statemodel::transitionblock_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=statemodel::TransitionBlock_strategy)
def test_statemodel::transitionblock_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=statemodel::Activity_strategy)
@settings(max_examples=50)
def test_statemodel::activity_instantiation(instance):
    assert isinstance(instance, statemodel::Activity)
