import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Activity,
    statemodel_Entity,
    Element,
    statemodel_State,
    statemodel_Statemachine,
    statemodel_Annotation,
    statemodel_Element,
    statemodel_Import,
    statemodel_Model,
    statemodel_Transition,
    statemodel_TransitionBlock,
    statemodel_Activity,
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



def test_statemodel_entity_is_not_abstract():
    assert not inspect.isabstract(statemodel_Entity)


def test_statemodel_entity_constructor_exists():
    assert callable(statemodel_Entity.__init__)


def test_statemodel_entity_constructor_args():
    sig = inspect.signature(statemodel_Entity.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_statemodel_state_is_not_abstract():
    assert not inspect.isabstract(statemodel_State)


def test_statemodel_state_constructor_exists():
    assert callable(statemodel_State.__init__)


def test_statemodel_state_constructor_args():
    sig = inspect.signature(statemodel_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_statemodel_state_has_name():
    assert hasattr(statemodel_State, "name")
    descriptor = None
    for klass in statemodel_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statemodel_state_has_type():
    assert hasattr(statemodel_State, "type")
    descriptor = None
    for klass in statemodel_State.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_statemodel_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemodel_Statemachine)


def test_statemodel_statemachine_constructor_exists():
    assert callable(statemodel_Statemachine.__init__)


def test_statemodel_statemachine_constructor_args():
    sig = inspect.signature(statemodel_Statemachine.__init__)
    params = list(sig.parameters.keys())



def test_statemodel_annotation_is_not_abstract():
    assert not inspect.isabstract(statemodel_Annotation)


def test_statemodel_annotation_constructor_exists():
    assert callable(statemodel_Annotation.__init__)


def test_statemodel_annotation_constructor_args():
    sig = inspect.signature(statemodel_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_statemodel_element_is_not_abstract():
    assert not inspect.isabstract(statemodel_Element)


def test_statemodel_element_constructor_exists():
    assert callable(statemodel_Element.__init__)


def test_statemodel_element_constructor_args():
    sig = inspect.signature(statemodel_Element.__init__)
    params = list(sig.parameters.keys())



def test_statemodel_import_is_not_abstract():
    assert not inspect.isabstract(statemodel_Import)


def test_statemodel_import_constructor_exists():
    assert callable(statemodel_Import.__init__)


def test_statemodel_import_constructor_args():
    sig = inspect.signature(statemodel_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_statemodel_import_has_importURI():
    assert hasattr(statemodel_Import, "importURI")
    descriptor = None
    for klass in statemodel_Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_statemodel_model_is_not_abstract():
    assert not inspect.isabstract(statemodel_Model)


def test_statemodel_model_constructor_exists():
    assert callable(statemodel_Model.__init__)


def test_statemodel_model_constructor_args():
    sig = inspect.signature(statemodel_Model.__init__)
    params = list(sig.parameters.keys())



def test_statemodel_transition_is_not_abstract():
    assert not inspect.isabstract(statemodel_Transition)


def test_statemodel_transition_constructor_exists():
    assert callable(statemodel_Transition.__init__)


def test_statemodel_transition_constructor_args():
    sig = inspect.signature(statemodel_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "guard" in params, "Missing parameter 'guard'"

def test_statemodel_transition_has_action():
    assert hasattr(statemodel_Transition, "action")
    descriptor = None
    for klass in statemodel_Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_statemodel_transition_has_guard():
    assert hasattr(statemodel_Transition, "guard")
    descriptor = None
    for klass in statemodel_Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)



def test_statemodel_transitionblock_is_not_abstract():
    assert not inspect.isabstract(statemodel_TransitionBlock)


def test_statemodel_transitionblock_constructor_exists():
    assert callable(statemodel_TransitionBlock.__init__)


def test_statemodel_transitionblock_constructor_args():
    sig = inspect.signature(statemodel_TransitionBlock.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_statemodel_transitionblock_has_event():
    assert hasattr(statemodel_TransitionBlock, "event")
    descriptor = None
    for klass in statemodel_TransitionBlock.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_statemodel_activity_is_not_abstract():
    assert not inspect.isabstract(statemodel_Activity)


def test_statemodel_activity_constructor_exists():
    assert callable(statemodel_Activity.__init__)


def test_statemodel_activity_constructor_args():
    sig = inspect.signature(statemodel_Activity.__init__)
    params = list(sig.parameters.keys())

def test_statetype_exists():
    # Check that the Enumeration exists
    assert StateType is not None

def test_statetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StateType]
    expected_literals = [
        "FINAL",
        "NONE",
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
statemodel_Entity_strategy = st.builds(
    statemodel_Entity,
)
Element_strategy = st.builds(
    Element,
)
statemodel_State_strategy = st.builds(
    statemodel_State,
    name=
        safe_text,
    type=
        safe_text
)
statemodel_Statemachine_strategy = st.builds(
    statemodel_Statemachine,
)
statemodel_Annotation_strategy = st.builds(
    statemodel_Annotation,
)
statemodel_Element_strategy = st.builds(
    statemodel_Element,
)
statemodel_Import_strategy = st.builds(
    statemodel_Import,
    importURI=
        safe_text
)
statemodel_Model_strategy = st.builds(
    statemodel_Model,
)
statemodel_Transition_strategy = st.builds(
    statemodel_Transition,
    action=
        safe_text,
    guard=
        safe_text
)
statemodel_TransitionBlock_strategy = st.builds(
    statemodel_TransitionBlock,
    event=
        safe_text
)
statemodel_Activity_strategy = st.builds(
    statemodel_Activity,
)

@given(instance=Activity_strategy)
@settings(max_examples=50)
def test_activity_instantiation(instance):
    assert isinstance(instance, Activity)

@given(instance=statemodel_Entity_strategy)
@settings(max_examples=50)
def test_statemodel_entity_instantiation(instance):
    assert isinstance(instance, statemodel_Entity)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=statemodel_State_strategy)
@settings(max_examples=50)
def test_statemodel_state_instantiation(instance):
    assert isinstance(instance, statemodel_State)



@given(instance=statemodel_State_strategy)
def test_statemodel_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=statemodel_State_strategy)
def test_statemodel_state_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=statemodel_Statemachine_strategy)
@settings(max_examples=50)
def test_statemodel_statemachine_instantiation(instance):
    assert isinstance(instance, statemodel_Statemachine)

@given(instance=statemodel_Annotation_strategy)
@settings(max_examples=50)
def test_statemodel_annotation_instantiation(instance):
    assert isinstance(instance, statemodel_Annotation)

@given(instance=statemodel_Element_strategy)
@settings(max_examples=50)
def test_statemodel_element_instantiation(instance):
    assert isinstance(instance, statemodel_Element)

@given(instance=statemodel_Import_strategy)
@settings(max_examples=50)
def test_statemodel_import_instantiation(instance):
    assert isinstance(instance, statemodel_Import)



@given(instance=statemodel_Import_strategy)
def test_statemodel_import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=statemodel_Model_strategy)
@settings(max_examples=50)
def test_statemodel_model_instantiation(instance):
    assert isinstance(instance, statemodel_Model)

@given(instance=statemodel_Transition_strategy)
@settings(max_examples=50)
def test_statemodel_transition_instantiation(instance):
    assert isinstance(instance, statemodel_Transition)



@given(instance=statemodel_Transition_strategy)
def test_statemodel_transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=statemodel_Transition_strategy)
def test_statemodel_transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=statemodel_TransitionBlock_strategy)
@settings(max_examples=50)
def test_statemodel_transitionblock_instantiation(instance):
    assert isinstance(instance, statemodel_TransitionBlock)



@given(instance=statemodel_TransitionBlock_strategy)
def test_statemodel_transitionblock_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=statemodel_Activity_strategy)
@settings(max_examples=50)
def test_statemodel_activity_instantiation(instance):
    assert isinstance(instance, statemodel_Activity)
