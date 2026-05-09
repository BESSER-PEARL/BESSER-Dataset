import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    state::Behaviour,
    state::Constraint,
    state::StateModel,
    state::Event,
    state::OpaqueExpression,
    State,
    state::FinalState,
    NamedElement,
    state::Region,
    state::StateMachine,
    state::Trigger,
    state::Vertex,
    Vertex,
    state::PseudoState,
    state::State,
    state::NamedElement,
    state::Transition,
    PseudoStateKind,
    TransitionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_state::behaviour_is_not_abstract():
    assert not inspect.isabstract(state::Behaviour)


def test_state::behaviour_constructor_exists():
    assert callable(state::Behaviour.__init__)


def test_state::behaviour_constructor_args():
    sig = inspect.signature(state::Behaviour.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_state::behaviour_has_body():
    assert hasattr(state::Behaviour, "body")
    descriptor = None
    for klass in state::Behaviour.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_state::behaviour_has_language():
    assert hasattr(state::Behaviour, "language")
    descriptor = None
    for klass in state::Behaviour.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_state::constraint_is_not_abstract():
    assert not inspect.isabstract(state::Constraint)


def test_state::constraint_constructor_exists():
    assert callable(state::Constraint.__init__)


def test_state::constraint_constructor_args():
    sig = inspect.signature(state::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_state::statemodel_is_not_abstract():
    assert not inspect.isabstract(state::StateModel)


def test_state::statemodel_constructor_exists():
    assert callable(state::StateModel.__init__)


def test_state::statemodel_constructor_args():
    sig = inspect.signature(state::StateModel.__init__)
    params = list(sig.parameters.keys())



def test_state::event_is_not_abstract():
    assert not inspect.isabstract(state::Event)


def test_state::event_constructor_exists():
    assert callable(state::Event.__init__)


def test_state::event_constructor_args():
    sig = inspect.signature(state::Event.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_state::event_has_body():
    assert hasattr(state::Event, "body")
    descriptor = None
    for klass in state::Event.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_state::opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(state::OpaqueExpression)


def test_state::opaqueexpression_constructor_exists():
    assert callable(state::OpaqueExpression.__init__)


def test_state::opaqueexpression_constructor_args():
    sig = inspect.signature(state::OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_state::opaqueexpression_has_body():
    assert hasattr(state::OpaqueExpression, "body")
    descriptor = None
    for klass in state::OpaqueExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_state::finalstate_is_not_abstract():
    assert not inspect.isabstract(state::FinalState)


def test_state::finalstate_constructor_exists():
    assert callable(state::FinalState.__init__)


def test_state::finalstate_constructor_args():
    sig = inspect.signature(state::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_state::region_is_not_abstract():
    assert not inspect.isabstract(state::Region)


def test_state::region_constructor_exists():
    assert callable(state::Region.__init__)


def test_state::region_constructor_args():
    sig = inspect.signature(state::Region.__init__)
    params = list(sig.parameters.keys())



def test_state::statemachine_is_not_abstract():
    assert not inspect.isabstract(state::StateMachine)


def test_state::statemachine_constructor_exists():
    assert callable(state::StateMachine.__init__)


def test_state::statemachine_constructor_args():
    sig = inspect.signature(state::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_state::trigger_is_not_abstract():
    assert not inspect.isabstract(state::Trigger)


def test_state::trigger_constructor_exists():
    assert callable(state::Trigger.__init__)


def test_state::trigger_constructor_args():
    sig = inspect.signature(state::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_state::vertex_is_not_abstract():
    assert not inspect.isabstract(state::Vertex)


def test_state::vertex_constructor_exists():
    assert callable(state::Vertex.__init__)


def test_state::vertex_constructor_args():
    sig = inspect.signature(state::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_state::pseudostate_is_not_abstract():
    assert not inspect.isabstract(state::PseudoState)


def test_state::pseudostate_constructor_exists():
    assert callable(state::PseudoState.__init__)


def test_state::pseudostate_constructor_args():
    sig = inspect.signature(state::PseudoState.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_state::pseudostate_has_kind():
    assert hasattr(state::PseudoState, "kind")
    descriptor = None
    for klass in state::PseudoState.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_state::state_is_not_abstract():
    assert not inspect.isabstract(state::State)


def test_state::state_constructor_exists():
    assert callable(state::State.__init__)


def test_state::state_constructor_args():
    sig = inspect.signature(state::State.__init__)
    params = list(sig.parameters.keys())
    assert "isSimple" in params, "Missing parameter 'isSimple'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"

def test_state::state_has_isSimple():
    assert hasattr(state::State, "isSimple")
    descriptor = None
    for klass in state::State.__mro__:
        if "isSimple" in klass.__dict__:
            descriptor = klass.__dict__["isSimple"]
            break
    assert isinstance(descriptor, property)

def test_state::state_has_isComposite():
    assert hasattr(state::State, "isComposite")
    descriptor = None
    for klass in state::State.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)



def test_state::namedelement_is_not_abstract():
    assert not inspect.isabstract(state::NamedElement)


def test_state::namedelement_constructor_exists():
    assert callable(state::NamedElement.__init__)


def test_state::namedelement_constructor_args():
    sig = inspect.signature(state::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_state::namedelement_has_name():
    assert hasattr(state::NamedElement, "name")
    descriptor = None
    for klass in state::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_state::namedelement_has_id():
    assert hasattr(state::NamedElement, "id")
    descriptor = None
    for klass in state::NamedElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_state::transition_is_not_abstract():
    assert not inspect.isabstract(state::Transition)


def test_state::transition_constructor_exists():
    assert callable(state::Transition.__init__)


def test_state::transition_constructor_args():
    sig = inspect.signature(state::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_state::transition_has_kind():
    assert hasattr(state::Transition, "kind")
    descriptor = None
    for klass in state::Transition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudoStateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudoStateKind]
    expected_literals = [
        "fork",
        "join",
        "choice",
        "deep",
        "initial",
        "terminate",
        "shallow",
        "none",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudoStateKind"

def test_transitionkind_exists():
    # Check that the Enumeration exists
    assert TransitionKind is not None

def test_transitionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionKind]
    expected_literals = [
        "local",
        "internal",
        "external",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionKind"


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
state::Behaviour_strategy = st.builds(
    state::Behaviour,
    body=
        safe_text,
    language=
        safe_text
)
state::Constraint_strategy = st.builds(
    state::Constraint,
)
state::StateModel_strategy = st.builds(
    state::StateModel,
)
state::Event_strategy = st.builds(
    state::Event,
    body=
        safe_text
)
state::OpaqueExpression_strategy = st.builds(
    state::OpaqueExpression,
    body=
        safe_text
)
State_strategy = st.builds(
    State,
)
state::FinalState_strategy = st.builds(
    state::FinalState,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
state::Region_strategy = st.builds(
    state::Region,
)
state::StateMachine_strategy = st.builds(
    state::StateMachine,
)
state::Trigger_strategy = st.builds(
    state::Trigger,
)
state::Vertex_strategy = st.builds(
    state::Vertex,
)
Vertex_strategy = st.builds(
    Vertex,
)
state::PseudoState_strategy = st.builds(
    state::PseudoState,
    kind=
        safe_text
)
state::State_strategy = st.builds(
    state::State,
    isSimple=
        st.booleans(),
    isComposite=
        st.booleans()
)
state::NamedElement_strategy = st.builds(
    state::NamedElement,
    name=
        safe_text,
    id=
        safe_text
)
state::Transition_strategy = st.builds(
    state::Transition,
    kind=
        safe_text
)

@given(instance=state::Behaviour_strategy)
@settings(max_examples=50)
def test_state::behaviour_instantiation(instance):
    assert isinstance(instance, state::Behaviour)

@given(instance=state::Behaviour_strategy)
def test_state::behaviour_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=state::Behaviour_strategy)
def test_state::behaviour_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=state::Behaviour_strategy)
def test_state::behaviour_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=state::Behaviour_strategy)
def test_state::behaviour_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=state::Constraint_strategy)
@settings(max_examples=50)
def test_state::constraint_instantiation(instance):
    assert isinstance(instance, state::Constraint)

@given(instance=state::StateModel_strategy)
@settings(max_examples=50)
def test_state::statemodel_instantiation(instance):
    assert isinstance(instance, state::StateModel)

@given(instance=state::Event_strategy)
@settings(max_examples=50)
def test_state::event_instantiation(instance):
    assert isinstance(instance, state::Event)

@given(instance=state::Event_strategy)
def test_state::event_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=state::Event_strategy)
def test_state::event_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=state::OpaqueExpression_strategy)
@settings(max_examples=50)
def test_state::opaqueexpression_instantiation(instance):
    assert isinstance(instance, state::OpaqueExpression)

@given(instance=state::OpaqueExpression_strategy)
def test_state::opaqueexpression_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=state::OpaqueExpression_strategy)
def test_state::opaqueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=state::FinalState_strategy)
@settings(max_examples=50)
def test_state::finalstate_instantiation(instance):
    assert isinstance(instance, state::FinalState)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=state::Region_strategy)
@settings(max_examples=50)
def test_state::region_instantiation(instance):
    assert isinstance(instance, state::Region)

@given(instance=state::StateMachine_strategy)
@settings(max_examples=50)
def test_state::statemachine_instantiation(instance):
    assert isinstance(instance, state::StateMachine)

@given(instance=state::Trigger_strategy)
@settings(max_examples=50)
def test_state::trigger_instantiation(instance):
    assert isinstance(instance, state::Trigger)

@given(instance=state::Vertex_strategy)
@settings(max_examples=50)
def test_state::vertex_instantiation(instance):
    assert isinstance(instance, state::Vertex)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=state::PseudoState_strategy)
@settings(max_examples=50)
def test_state::pseudostate_instantiation(instance):
    assert isinstance(instance, state::PseudoState)

@given(instance=state::PseudoState_strategy)
def test_state::pseudostate_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=state::PseudoState_strategy)
def test_state::pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=state::State_strategy)
@settings(max_examples=50)
def test_state::state_instantiation(instance):
    assert isinstance(instance, state::State)

@given(instance=state::State_strategy)
def test_state::state_isSimple_type(instance):
    assert isinstance(instance.isSimple, bool)


@given(instance=state::State_strategy)
def test_state::state_isSimple_setter(instance):
    original = instance.isSimple
    instance.isSimple = original
    assert instance.isSimple == original

@given(instance=state::State_strategy)
def test_state::state_isComposite_type(instance):
    assert isinstance(instance.isComposite, bool)


@given(instance=state::State_strategy)
def test_state::state_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=state::NamedElement_strategy)
@settings(max_examples=50)
def test_state::namedelement_instantiation(instance):
    assert isinstance(instance, state::NamedElement)

@given(instance=state::NamedElement_strategy)
def test_state::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=state::NamedElement_strategy)
def test_state::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=state::NamedElement_strategy)
def test_state::namedelement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=state::NamedElement_strategy)
def test_state::namedelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=state::Transition_strategy)
@settings(max_examples=50)
def test_state::transition_instantiation(instance):
    assert isinstance(instance, state::Transition)

@given(instance=state::Transition_strategy)
def test_state::transition_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=state::Transition_strategy)
def test_state::transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original
