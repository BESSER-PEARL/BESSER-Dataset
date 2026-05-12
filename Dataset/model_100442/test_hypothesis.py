import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statemachines_EventBElement,
    StatemachineOwner,
    EventBNamed,
    AbstractNode,
    statemachines_Initial,
    statemachines_State,
    EventBElement,
    Event,
    EventBLabeled,
    EventBCommentedElement,
    statemachines_Transition,
    statemachines_StatemachineOwner,
    statemachines_EventBNamedCommentedElement,
    statemachines_AbstractNode,
    Diagram,
    AbstractExtension,
    EventBNamedCommentedElement,
    statemachines_Statemachine,
    Invariant,
    statemachines_Final,
    TranslationKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachines_eventbelement_is_not_abstract():
    assert not inspect.isabstract(statemachines_EventBElement)


def test_statemachines_eventbelement_constructor_exists():
    assert callable(statemachines_EventBElement.__init__)


def test_statemachines_eventbelement_constructor_args():
    sig = inspect.signature(statemachines_EventBElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachineowner_is_not_abstract():
    assert not inspect.isabstract(StatemachineOwner)


def test_statemachineowner_constructor_exists():
    assert callable(StatemachineOwner.__init__)


def test_statemachineowner_constructor_args():
    sig = inspect.signature(StatemachineOwner.__init__)
    params = list(sig.parameters.keys())



def test_eventbnamed_is_not_abstract():
    assert not inspect.isabstract(EventBNamed)


def test_eventbnamed_constructor_exists():
    assert callable(EventBNamed.__init__)


def test_eventbnamed_constructor_args():
    sig = inspect.signature(EventBNamed.__init__)
    params = list(sig.parameters.keys())



def test_abstractnode_is_not_abstract():
    assert not inspect.isabstract(AbstractNode)


def test_abstractnode_constructor_exists():
    assert callable(AbstractNode.__init__)


def test_abstractnode_constructor_args():
    sig = inspect.signature(AbstractNode.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_initial_is_not_abstract():
    assert not inspect.isabstract(statemachines_Initial)


def test_statemachines_initial_constructor_exists():
    assert callable(statemachines_Initial.__init__)


def test_statemachines_initial_constructor_args():
    sig = inspect.signature(statemachines_Initial.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_state_is_not_abstract():
    assert not inspect.isabstract(statemachines_State)


def test_statemachines_state_constructor_exists():
    assert callable(statemachines_State.__init__)


def test_statemachines_state_constructor_args():
    sig = inspect.signature(statemachines_State.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"

def test_statemachines_state_has_active():
    assert hasattr(statemachines_State, "active")
    descriptor = None
    for klass in statemachines_State.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)



def test_eventbelement_is_not_abstract():
    assert not inspect.isabstract(EventBElement)


def test_eventbelement_constructor_exists():
    assert callable(EventBElement.__init__)


def test_eventbelement_constructor_args():
    sig = inspect.signature(EventBElement.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_eventblabeled_is_not_abstract():
    assert not inspect.isabstract(EventBLabeled)


def test_eventblabeled_constructor_exists():
    assert callable(EventBLabeled.__init__)


def test_eventblabeled_constructor_args():
    sig = inspect.signature(EventBLabeled.__init__)
    params = list(sig.parameters.keys())



def test_eventbcommentedelement_is_not_abstract():
    assert not inspect.isabstract(EventBCommentedElement)


def test_eventbcommentedelement_constructor_exists():
    assert callable(EventBCommentedElement.__init__)


def test_eventbcommentedelement_constructor_args():
    sig = inspect.signature(EventBCommentedElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_transition_is_not_abstract():
    assert not inspect.isabstract(statemachines_Transition)


def test_statemachines_transition_constructor_exists():
    assert callable(statemachines_Transition.__init__)


def test_statemachines_transition_constructor_args():
    sig = inspect.signature(statemachines_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "operations" in params, "Missing parameter 'operations'"

def test_statemachines_transition_has_operations():
    assert hasattr(statemachines_Transition, "operations")
    descriptor = None
    for klass in statemachines_Transition.__mro__:
        if "operations" in klass.__dict__:
            descriptor = klass.__dict__["operations"]
            break
    assert isinstance(descriptor, property)



def test_statemachines_statemachineowner_is_not_abstract():
    assert not inspect.isabstract(statemachines_StatemachineOwner)


def test_statemachines_statemachineowner_constructor_exists():
    assert callable(statemachines_StatemachineOwner.__init__)


def test_statemachines_statemachineowner_constructor_args():
    sig = inspect.signature(statemachines_StatemachineOwner.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_eventbnamedcommentedelement_is_not_abstract():
    assert not inspect.isabstract(statemachines_EventBNamedCommentedElement)


def test_statemachines_eventbnamedcommentedelement_constructor_exists():
    assert callable(statemachines_EventBNamedCommentedElement.__init__)


def test_statemachines_eventbnamedcommentedelement_constructor_args():
    sig = inspect.signature(statemachines_EventBNamedCommentedElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_abstractnode_is_not_abstract():
    assert not inspect.isabstract(statemachines_AbstractNode)


def test_statemachines_abstractnode_constructor_exists():
    assert callable(statemachines_AbstractNode.__init__)


def test_statemachines_abstractnode_constructor_args():
    sig = inspect.signature(statemachines_AbstractNode.__init__)
    params = list(sig.parameters.keys())



def test_diagram_is_not_abstract():
    assert not inspect.isabstract(Diagram)


def test_diagram_constructor_exists():
    assert callable(Diagram.__init__)


def test_diagram_constructor_args():
    sig = inspect.signature(Diagram.__init__)
    params = list(sig.parameters.keys())



def test_abstractextension_is_not_abstract():
    assert not inspect.isabstract(AbstractExtension)


def test_abstractextension_constructor_exists():
    assert callable(AbstractExtension.__init__)


def test_abstractextension_constructor_args():
    sig = inspect.signature(AbstractExtension.__init__)
    params = list(sig.parameters.keys())



def test_eventbnamedcommentedelement_is_not_abstract():
    assert not inspect.isabstract(EventBNamedCommentedElement)


def test_eventbnamedcommentedelement_constructor_exists():
    assert callable(EventBNamedCommentedElement.__init__)


def test_eventbnamedcommentedelement_constructor_args():
    sig = inspect.signature(EventBNamedCommentedElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachines_Statemachine)


def test_statemachines_statemachine_constructor_exists():
    assert callable(statemachines_Statemachine.__init__)


def test_statemachines_statemachine_constructor_args():
    sig = inspect.signature(statemachines_Statemachine.__init__)
    params = list(sig.parameters.keys())
    assert "translation" in params, "Missing parameter 'translation'"
    assert "selfName" in params, "Missing parameter 'selfName'"

def test_statemachines_statemachine_has_translation():
    assert hasattr(statemachines_Statemachine, "translation")
    descriptor = None
    for klass in statemachines_Statemachine.__mro__:
        if "translation" in klass.__dict__:
            descriptor = klass.__dict__["translation"]
            break
    assert isinstance(descriptor, property)

def test_statemachines_statemachine_has_selfName():
    assert hasattr(statemachines_Statemachine, "selfName")
    descriptor = None
    for klass in statemachines_Statemachine.__mro__:
        if "selfName" in klass.__dict__:
            descriptor = klass.__dict__["selfName"]
            break
    assert isinstance(descriptor, property)



def test_invariant_is_not_abstract():
    assert not inspect.isabstract(Invariant)


def test_invariant_constructor_exists():
    assert callable(Invariant.__init__)


def test_invariant_constructor_args():
    sig = inspect.signature(Invariant.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_final_is_not_abstract():
    assert not inspect.isabstract(statemachines_Final)


def test_statemachines_final_constructor_exists():
    assert callable(statemachines_Final.__init__)


def test_statemachines_final_constructor_args():
    sig = inspect.signature(statemachines_Final.__init__)
    params = list(sig.parameters.keys())

def test_translationkind_exists():
    # Check that the Enumeration exists
    assert TranslationKind is not None

def test_translationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TranslationKind]
    expected_literals = [
        "SINGLEVAR",
        "MULTIVAR",
        "REFINEDVAR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TranslationKind"


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
statemachines_EventBElement_strategy = st.builds(
    statemachines_EventBElement,
)
StatemachineOwner_strategy = st.builds(
    StatemachineOwner,
)
EventBNamed_strategy = st.builds(
    EventBNamed,
)
AbstractNode_strategy = st.builds(
    AbstractNode,
)
statemachines_Initial_strategy = st.builds(
    statemachines_Initial,
)
statemachines_State_strategy = st.builds(
    statemachines_State,
    active=
        st.booleans()
)
EventBElement_strategy = st.builds(
    EventBElement,
)
Event_strategy = st.builds(
    Event,
)
EventBLabeled_strategy = st.builds(
    EventBLabeled,
)
EventBCommentedElement_strategy = st.builds(
    EventBCommentedElement,
)
statemachines_Transition_strategy = st.builds(
    statemachines_Transition,
    operations=
        safe_text
)
statemachines_StatemachineOwner_strategy = st.builds(
    statemachines_StatemachineOwner,
)
statemachines_EventBNamedCommentedElement_strategy = st.builds(
    statemachines_EventBNamedCommentedElement,
)
statemachines_AbstractNode_strategy = st.builds(
    statemachines_AbstractNode,
)
Diagram_strategy = st.builds(
    Diagram,
)
AbstractExtension_strategy = st.builds(
    AbstractExtension,
)
EventBNamedCommentedElement_strategy = st.builds(
    EventBNamedCommentedElement,
)
statemachines_Statemachine_strategy = st.builds(
    statemachines_Statemachine,
    translation=
        safe_text,
    selfName=
        safe_text
)
Invariant_strategy = st.builds(
    Invariant,
)
statemachines_Final_strategy = st.builds(
    statemachines_Final,
)

@given(instance=statemachines_EventBElement_strategy)
@settings(max_examples=50)
def test_statemachines_eventbelement_instantiation(instance):
    assert isinstance(instance, statemachines_EventBElement)

@given(instance=StatemachineOwner_strategy)
@settings(max_examples=50)
def test_statemachineowner_instantiation(instance):
    assert isinstance(instance, StatemachineOwner)

@given(instance=EventBNamed_strategy)
@settings(max_examples=50)
def test_eventbnamed_instantiation(instance):
    assert isinstance(instance, EventBNamed)

@given(instance=AbstractNode_strategy)
@settings(max_examples=50)
def test_abstractnode_instantiation(instance):
    assert isinstance(instance, AbstractNode)

@given(instance=statemachines_Initial_strategy)
@settings(max_examples=50)
def test_statemachines_initial_instantiation(instance):
    assert isinstance(instance, statemachines_Initial)

@given(instance=statemachines_State_strategy)
@settings(max_examples=50)
def test_statemachines_state_instantiation(instance):
    assert isinstance(instance, statemachines_State)



@given(instance=statemachines_State_strategy)
def test_statemachines_state_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=EventBElement_strategy)
@settings(max_examples=50)
def test_eventbelement_instantiation(instance):
    assert isinstance(instance, EventBElement)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=EventBLabeled_strategy)
@settings(max_examples=50)
def test_eventblabeled_instantiation(instance):
    assert isinstance(instance, EventBLabeled)

@given(instance=EventBCommentedElement_strategy)
@settings(max_examples=50)
def test_eventbcommentedelement_instantiation(instance):
    assert isinstance(instance, EventBCommentedElement)

@given(instance=statemachines_Transition_strategy)
@settings(max_examples=50)
def test_statemachines_transition_instantiation(instance):
    assert isinstance(instance, statemachines_Transition)



@given(instance=statemachines_Transition_strategy)
def test_statemachines_transition_operations_setter(instance):
    original = instance.operations
    instance.operations = original
    assert instance.operations == original

@given(instance=statemachines_StatemachineOwner_strategy)
@settings(max_examples=50)
def test_statemachines_statemachineowner_instantiation(instance):
    assert isinstance(instance, statemachines_StatemachineOwner)

@given(instance=statemachines_EventBNamedCommentedElement_strategy)
@settings(max_examples=50)
def test_statemachines_eventbnamedcommentedelement_instantiation(instance):
    assert isinstance(instance, statemachines_EventBNamedCommentedElement)

@given(instance=statemachines_AbstractNode_strategy)
@settings(max_examples=50)
def test_statemachines_abstractnode_instantiation(instance):
    assert isinstance(instance, statemachines_AbstractNode)

@given(instance=Diagram_strategy)
@settings(max_examples=50)
def test_diagram_instantiation(instance):
    assert isinstance(instance, Diagram)

@given(instance=AbstractExtension_strategy)
@settings(max_examples=50)
def test_abstractextension_instantiation(instance):
    assert isinstance(instance, AbstractExtension)

@given(instance=EventBNamedCommentedElement_strategy)
@settings(max_examples=50)
def test_eventbnamedcommentedelement_instantiation(instance):
    assert isinstance(instance, EventBNamedCommentedElement)

@given(instance=statemachines_Statemachine_strategy)
@settings(max_examples=50)
def test_statemachines_statemachine_instantiation(instance):
    assert isinstance(instance, statemachines_Statemachine)



@given(instance=statemachines_Statemachine_strategy)
def test_statemachines_statemachine_translation_setter(instance):
    original = instance.translation
    instance.translation = original
    assert instance.translation == original



@given(instance=statemachines_Statemachine_strategy)
def test_statemachines_statemachine_selfName_setter(instance):
    original = instance.selfName
    instance.selfName = original
    assert instance.selfName == original

@given(instance=Invariant_strategy)
@settings(max_examples=50)
def test_invariant_instantiation(instance):
    assert isinstance(instance, Invariant)

@given(instance=statemachines_Final_strategy)
@settings(max_examples=50)
def test_statemachines_final_instantiation(instance):
    assert isinstance(instance, statemachines_Final)
