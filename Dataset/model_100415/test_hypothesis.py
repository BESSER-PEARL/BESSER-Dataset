import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    state_StateModel,
    state_Constraint,
    state_Event,
    state_OpaqueExpression,
    State,
    state_FinalState,
    state_NamedElement,
    state_Behaviour,
    NamedElement,
    state_Vertex,
    state_Transition,
    state_StateMachine,
    state_Region,
    Vertex,
    state_PseudoState,
    state_State,
    state_Trigger,
    TransitionKind,
    PseudoStateKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_state_statemodel_is_not_abstract():
    assert not inspect.isabstract(state_StateModel)


def test_state_statemodel_constructor_exists():
    assert callable(state_StateModel.__init__)


def test_state_statemodel_constructor_args():
    sig = inspect.signature(state_StateModel.__init__)
    params = list(sig.parameters.keys())



def test_state_constraint_is_not_abstract():
    assert not inspect.isabstract(state_Constraint)


def test_state_constraint_constructor_exists():
    assert callable(state_Constraint.__init__)


def test_state_constraint_constructor_args():
    sig = inspect.signature(state_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_state_event_is_not_abstract():
    assert not inspect.isabstract(state_Event)


def test_state_event_constructor_exists():
    assert callable(state_Event.__init__)


def test_state_event_constructor_args():
    sig = inspect.signature(state_Event.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_state_event_has_body():
    assert hasattr(state_Event, "body")
    descriptor = None
    for klass in state_Event.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_state_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(state_OpaqueExpression)


def test_state_opaqueexpression_constructor_exists():
    assert callable(state_OpaqueExpression.__init__)


def test_state_opaqueexpression_constructor_args():
    sig = inspect.signature(state_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_state_opaqueexpression_has_body():
    assert hasattr(state_OpaqueExpression, "body")
    descriptor = None
    for klass in state_OpaqueExpression.__mro__:
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



def test_state_finalstate_is_not_abstract():
    assert not inspect.isabstract(state_FinalState)


def test_state_finalstate_constructor_exists():
    assert callable(state_FinalState.__init__)


def test_state_finalstate_constructor_args():
    sig = inspect.signature(state_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_state_namedelement_is_not_abstract():
    assert not inspect.isabstract(state_NamedElement)


def test_state_namedelement_constructor_exists():
    assert callable(state_NamedElement.__init__)


def test_state_namedelement_constructor_args():
    sig = inspect.signature(state_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_state_namedelement_has_id():
    assert hasattr(state_NamedElement, "id")
    descriptor = None
    for klass in state_NamedElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_state_namedelement_has_name():
    assert hasattr(state_NamedElement, "name")
    descriptor = None
    for klass in state_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_state_behaviour_is_not_abstract():
    assert not inspect.isabstract(state_Behaviour)


def test_state_behaviour_constructor_exists():
    assert callable(state_Behaviour.__init__)


def test_state_behaviour_constructor_args():
    sig = inspect.signature(state_Behaviour.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_state_behaviour_has_body():
    assert hasattr(state_Behaviour, "body")
    descriptor = None
    for klass in state_Behaviour.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_state_behaviour_has_language():
    assert hasattr(state_Behaviour, "language")
    descriptor = None
    for klass in state_Behaviour.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_state_vertex_is_not_abstract():
    assert not inspect.isabstract(state_Vertex)


def test_state_vertex_constructor_exists():
    assert callable(state_Vertex.__init__)


def test_state_vertex_constructor_args():
    sig = inspect.signature(state_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_state_transition_is_not_abstract():
    assert not inspect.isabstract(state_Transition)


def test_state_transition_constructor_exists():
    assert callable(state_Transition.__init__)


def test_state_transition_constructor_args():
    sig = inspect.signature(state_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_state_transition_has_kind():
    assert hasattr(state_Transition, "kind")
    descriptor = None
    for klass in state_Transition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_state_statemachine_is_not_abstract():
    assert not inspect.isabstract(state_StateMachine)


def test_state_statemachine_constructor_exists():
    assert callable(state_StateMachine.__init__)


def test_state_statemachine_constructor_args():
    sig = inspect.signature(state_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_state_region_is_not_abstract():
    assert not inspect.isabstract(state_Region)


def test_state_region_constructor_exists():
    assert callable(state_Region.__init__)


def test_state_region_constructor_args():
    sig = inspect.signature(state_Region.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_state_pseudostate_is_not_abstract():
    assert not inspect.isabstract(state_PseudoState)


def test_state_pseudostate_constructor_exists():
    assert callable(state_PseudoState.__init__)


def test_state_pseudostate_constructor_args():
    sig = inspect.signature(state_PseudoState.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_state_pseudostate_has_kind():
    assert hasattr(state_PseudoState, "kind")
    descriptor = None
    for klass in state_PseudoState.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_state_state_is_not_abstract():
    assert not inspect.isabstract(state_State)


def test_state_state_constructor_exists():
    assert callable(state_State.__init__)


def test_state_state_constructor_args():
    sig = inspect.signature(state_State.__init__)
    params = list(sig.parameters.keys())
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isSimple" in params, "Missing parameter 'isSimple'"

def test_state_state_has_isComposite():
    assert hasattr(state_State, "isComposite")
    descriptor = None
    for klass in state_State.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_state_state_has_isSimple():
    assert hasattr(state_State, "isSimple")
    descriptor = None
    for klass in state_State.__mro__:
        if "isSimple" in klass.__dict__:
            descriptor = klass.__dict__["isSimple"]
            break
    assert isinstance(descriptor, property)



def test_state_trigger_is_not_abstract():
    assert not inspect.isabstract(state_Trigger)


def test_state_trigger_constructor_exists():
    assert callable(state_Trigger.__init__)


def test_state_trigger_constructor_args():
    sig = inspect.signature(state_Trigger.__init__)
    params = list(sig.parameters.keys())

def test_transitionkind_exists():
    # Check that the Enumeration exists
    assert TransitionKind is not None

def test_transitionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionKind]
    expected_literals = [
        "local",
        "external",
        "internal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionKind"

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudoStateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudoStateKind]
    expected_literals = [
        "join",
        "fork",
        "shallow",
        "deep",
        "none",
        "initial",
        "choice",
        "terminate",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudoStateKind"


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
state_StateModel_strategy = st.builds(
    state_StateModel,
)
state_Constraint_strategy = st.builds(
    state_Constraint,
)
state_Event_strategy = st.builds(
    state_Event,
    body=
        safe_text
)
state_OpaqueExpression_strategy = st.builds(
    state_OpaqueExpression,
    body=
        safe_text
)
State_strategy = st.builds(
    State,
)
state_FinalState_strategy = st.builds(
    state_FinalState,
)
state_NamedElement_strategy = st.builds(
    state_NamedElement,
    id=
        safe_text,
    name=
        safe_text
)
state_Behaviour_strategy = st.builds(
    state_Behaviour,
    body=
        safe_text,
    language=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
state_Vertex_strategy = st.builds(
    state_Vertex,
)
state_Transition_strategy = st.builds(
    state_Transition,
    kind=
        safe_text
)
state_StateMachine_strategy = st.builds(
    state_StateMachine,
)
state_Region_strategy = st.builds(
    state_Region,
)
Vertex_strategy = st.builds(
    Vertex,
)
state_PseudoState_strategy = st.builds(
    state_PseudoState,
    kind=
        safe_text
)
state_State_strategy = st.builds(
    state_State,
    isComposite=
        st.booleans(),
    isSimple=
        st.booleans()
)
state_Trigger_strategy = st.builds(
    state_Trigger,
)

@given(instance=state_StateModel_strategy)
@settings(max_examples=50)
def test_state_statemodel_instantiation(instance):
    assert isinstance(instance, state_StateModel)

@given(instance=state_Constraint_strategy)
@settings(max_examples=50)
def test_state_constraint_instantiation(instance):
    assert isinstance(instance, state_Constraint)

@given(instance=state_Event_strategy)
@settings(max_examples=50)
def test_state_event_instantiation(instance):
    assert isinstance(instance, state_Event)



@given(instance=state_Event_strategy)
def test_state_event_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=state_OpaqueExpression_strategy)
@settings(max_examples=50)
def test_state_opaqueexpression_instantiation(instance):
    assert isinstance(instance, state_OpaqueExpression)



@given(instance=state_OpaqueExpression_strategy)
def test_state_opaqueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=state_FinalState_strategy)
@settings(max_examples=50)
def test_state_finalstate_instantiation(instance):
    assert isinstance(instance, state_FinalState)

@given(instance=state_NamedElement_strategy)
@settings(max_examples=50)
def test_state_namedelement_instantiation(instance):
    assert isinstance(instance, state_NamedElement)



@given(instance=state_NamedElement_strategy)
def test_state_namedelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=state_NamedElement_strategy)
def test_state_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=state_Behaviour_strategy)
@settings(max_examples=50)
def test_state_behaviour_instantiation(instance):
    assert isinstance(instance, state_Behaviour)



@given(instance=state_Behaviour_strategy)
def test_state_behaviour_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=state_Behaviour_strategy)
def test_state_behaviour_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=state_Vertex_strategy)
@settings(max_examples=50)
def test_state_vertex_instantiation(instance):
    assert isinstance(instance, state_Vertex)

@given(instance=state_Transition_strategy)
@settings(max_examples=50)
def test_state_transition_instantiation(instance):
    assert isinstance(instance, state_Transition)



@given(instance=state_Transition_strategy)
def test_state_transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=state_StateMachine_strategy)
@settings(max_examples=50)
def test_state_statemachine_instantiation(instance):
    assert isinstance(instance, state_StateMachine)

@given(instance=state_Region_strategy)
@settings(max_examples=50)
def test_state_region_instantiation(instance):
    assert isinstance(instance, state_Region)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=state_PseudoState_strategy)
@settings(max_examples=50)
def test_state_pseudostate_instantiation(instance):
    assert isinstance(instance, state_PseudoState)



@given(instance=state_PseudoState_strategy)
def test_state_pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=state_State_strategy)
@settings(max_examples=50)
def test_state_state_instantiation(instance):
    assert isinstance(instance, state_State)



@given(instance=state_State_strategy)
def test_state_state_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=state_State_strategy)
def test_state_state_isSimple_setter(instance):
    original = instance.isSimple
    instance.isSimple = original
    assert instance.isSimple == original

@given(instance=state_Trigger_strategy)
@settings(max_examples=50)
def test_state_trigger_instantiation(instance):
    assert isinstance(instance, state_Trigger)
