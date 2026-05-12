import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Invariant,
    statemachines::EventBElement,
    StatemachineOwner,
    EventBNamed,
    AbstractNode,
    statemachines::Final,
    statemachines::Initial,
    statemachines::State,
    EventBElement,
    Event,
    EventBLabeled,
    EventBCommentedElement,
    statemachines::Transition,
    statemachines::StatemachineOwner,
    statemachines::EventBNamedCommentedElement,
    statemachines::AbstractNode,
    Diagram,
    AbstractExtension,
    EventBNamedCommentedElement,
    statemachines::Statemachine,
    TranslationKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_invariant_is_not_abstract():
    assert not inspect.isabstract(Invariant)


def test_invariant_constructor_exists():
    assert callable(Invariant.__init__)


def test_invariant_constructor_args():
    sig = inspect.signature(Invariant.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::eventbelement_is_not_abstract():
    assert not inspect.isabstract(statemachines::EventBElement)


def test_statemachines::eventbelement_constructor_exists():
    assert callable(statemachines::EventBElement.__init__)


def test_statemachines::eventbelement_constructor_args():
    sig = inspect.signature(statemachines::EventBElement.__init__)
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



def test_statemachines::final_is_not_abstract():
    assert not inspect.isabstract(statemachines::Final)


def test_statemachines::final_constructor_exists():
    assert callable(statemachines::Final.__init__)


def test_statemachines::final_constructor_args():
    sig = inspect.signature(statemachines::Final.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::initial_is_not_abstract():
    assert not inspect.isabstract(statemachines::Initial)


def test_statemachines::initial_constructor_exists():
    assert callable(statemachines::Initial.__init__)


def test_statemachines::initial_constructor_args():
    sig = inspect.signature(statemachines::Initial.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::state_is_not_abstract():
    assert not inspect.isabstract(statemachines::State)


def test_statemachines::state_constructor_exists():
    assert callable(statemachines::State.__init__)


def test_statemachines::state_constructor_args():
    sig = inspect.signature(statemachines::State.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"

def test_statemachines::state_has_active():
    assert hasattr(statemachines::State, "active")
    descriptor = None
    for klass in statemachines::State.__mro__:
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



def test_statemachines::transition_is_not_abstract():
    assert not inspect.isabstract(statemachines::Transition)


def test_statemachines::transition_constructor_exists():
    assert callable(statemachines::Transition.__init__)


def test_statemachines::transition_constructor_args():
    sig = inspect.signature(statemachines::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "operations" in params, "Missing parameter 'operations'"

def test_statemachines::transition_has_operations():
    assert hasattr(statemachines::Transition, "operations")
    descriptor = None
    for klass in statemachines::Transition.__mro__:
        if "operations" in klass.__dict__:
            descriptor = klass.__dict__["operations"]
            break
    assert isinstance(descriptor, property)



def test_statemachines::statemachineowner_is_not_abstract():
    assert not inspect.isabstract(statemachines::StatemachineOwner)


def test_statemachines::statemachineowner_constructor_exists():
    assert callable(statemachines::StatemachineOwner.__init__)


def test_statemachines::statemachineowner_constructor_args():
    sig = inspect.signature(statemachines::StatemachineOwner.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::eventbnamedcommentedelement_is_not_abstract():
    assert not inspect.isabstract(statemachines::EventBNamedCommentedElement)


def test_statemachines::eventbnamedcommentedelement_constructor_exists():
    assert callable(statemachines::EventBNamedCommentedElement.__init__)


def test_statemachines::eventbnamedcommentedelement_constructor_args():
    sig = inspect.signature(statemachines::EventBNamedCommentedElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::abstractnode_is_not_abstract():
    assert not inspect.isabstract(statemachines::AbstractNode)


def test_statemachines::abstractnode_constructor_exists():
    assert callable(statemachines::AbstractNode.__init__)


def test_statemachines::abstractnode_constructor_args():
    sig = inspect.signature(statemachines::AbstractNode.__init__)
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



def test_statemachines::statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachines::Statemachine)


def test_statemachines::statemachine_constructor_exists():
    assert callable(statemachines::Statemachine.__init__)


def test_statemachines::statemachine_constructor_args():
    sig = inspect.signature(statemachines::Statemachine.__init__)
    params = list(sig.parameters.keys())
    assert "selfName" in params, "Missing parameter 'selfName'"
    assert "translation" in params, "Missing parameter 'translation'"

def test_statemachines::statemachine_has_selfName():
    assert hasattr(statemachines::Statemachine, "selfName")
    descriptor = None
    for klass in statemachines::Statemachine.__mro__:
        if "selfName" in klass.__dict__:
            descriptor = klass.__dict__["selfName"]
            break
    assert isinstance(descriptor, property)

def test_statemachines::statemachine_has_translation():
    assert hasattr(statemachines::Statemachine, "translation")
    descriptor = None
    for klass in statemachines::Statemachine.__mro__:
        if "translation" in klass.__dict__:
            descriptor = klass.__dict__["translation"]
            break
    assert isinstance(descriptor, property)

def test_translationkind_exists():
    # Check that the Enumeration exists
    assert TranslationKind is not None

def test_translationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TranslationKind]
    expected_literals = [
        "REFINEDVAR",
        "MULTIVAR",
        "SINGLEVAR",
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
Invariant_strategy = st.builds(
    Invariant,
)
statemachines::EventBElement_strategy = st.builds(
    statemachines::EventBElement,
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
statemachines::Final_strategy = st.builds(
    statemachines::Final,
)
statemachines::Initial_strategy = st.builds(
    statemachines::Initial,
)
statemachines::State_strategy = st.builds(
    statemachines::State,
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
statemachines::Transition_strategy = st.builds(
    statemachines::Transition,
    operations=
        safe_text
)
statemachines::StatemachineOwner_strategy = st.builds(
    statemachines::StatemachineOwner,
)
statemachines::EventBNamedCommentedElement_strategy = st.builds(
    statemachines::EventBNamedCommentedElement,
)
statemachines::AbstractNode_strategy = st.builds(
    statemachines::AbstractNode,
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
statemachines::Statemachine_strategy = st.builds(
    statemachines::Statemachine,
    selfName=
        safe_text,
    translation=
        safe_text
)

@given(instance=Invariant_strategy)
@settings(max_examples=50)
def test_invariant_instantiation(instance):
    assert isinstance(instance, Invariant)

@given(instance=statemachines::EventBElement_strategy)
@settings(max_examples=50)
def test_statemachines::eventbelement_instantiation(instance):
    assert isinstance(instance, statemachines::EventBElement)

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

@given(instance=statemachines::Final_strategy)
@settings(max_examples=50)
def test_statemachines::final_instantiation(instance):
    assert isinstance(instance, statemachines::Final)

@given(instance=statemachines::Initial_strategy)
@settings(max_examples=50)
def test_statemachines::initial_instantiation(instance):
    assert isinstance(instance, statemachines::Initial)

@given(instance=statemachines::State_strategy)
@settings(max_examples=50)
def test_statemachines::state_instantiation(instance):
    assert isinstance(instance, statemachines::State)

@given(instance=statemachines::State_strategy)
def test_statemachines::state_active_type(instance):
    assert isinstance(instance.active, bool)


@given(instance=statemachines::State_strategy)
def test_statemachines::state_active_setter(instance):
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

@given(instance=statemachines::Transition_strategy)
@settings(max_examples=50)
def test_statemachines::transition_instantiation(instance):
    assert isinstance(instance, statemachines::Transition)

@given(instance=statemachines::Transition_strategy)
def test_statemachines::transition_operations_type(instance):
    assert isinstance(instance.operations, str)


@given(instance=statemachines::Transition_strategy)
def test_statemachines::transition_operations_setter(instance):
    original = instance.operations
    instance.operations = original
    assert instance.operations == original

@given(instance=statemachines::StatemachineOwner_strategy)
@settings(max_examples=50)
def test_statemachines::statemachineowner_instantiation(instance):
    assert isinstance(instance, statemachines::StatemachineOwner)

@given(instance=statemachines::EventBNamedCommentedElement_strategy)
@settings(max_examples=50)
def test_statemachines::eventbnamedcommentedelement_instantiation(instance):
    assert isinstance(instance, statemachines::EventBNamedCommentedElement)

@given(instance=statemachines::AbstractNode_strategy)
@settings(max_examples=50)
def test_statemachines::abstractnode_instantiation(instance):
    assert isinstance(instance, statemachines::AbstractNode)

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

@given(instance=statemachines::Statemachine_strategy)
@settings(max_examples=50)
def test_statemachines::statemachine_instantiation(instance):
    assert isinstance(instance, statemachines::Statemachine)

@given(instance=statemachines::Statemachine_strategy)
def test_statemachines::statemachine_selfName_type(instance):
    assert isinstance(instance.selfName, str)


@given(instance=statemachines::Statemachine_strategy)
def test_statemachines::statemachine_selfName_setter(instance):
    original = instance.selfName
    instance.selfName = original
    assert instance.selfName == original

@given(instance=statemachines::Statemachine_strategy)
def test_statemachines::statemachine_translation_type(instance):
    assert isinstance(instance.translation, str)


@given(instance=statemachines::Statemachine_strategy)
def test_statemachines::statemachine_translation_setter(instance):
    original = instance.translation
    instance.translation = original
    assert instance.translation == original
