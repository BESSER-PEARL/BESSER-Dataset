import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    minuml1::ActionState,
    minuml1::CompositeState,
    StateMachine,
    minuml1::ActivityGraph,
    ModelElement,
    minuml1::Transition,
    minuml1::Partition,
    minuml1::StateMachine,
    minuml1::ModelElement,
    StateVertex,
    minuml1::State,
    minuml1::StateVertex,
    minuml1::BooleanExpression,
    minuml1::Guard,
    minuml1::FinalState,
    minuml1::ObjectFlowState,
    minuml1::Pseudostate,
    PseudostateKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_minuml1::actionstate_is_not_abstract():
    assert not inspect.isabstract(minuml1::ActionState)


def test_minuml1::actionstate_constructor_exists():
    assert callable(minuml1::ActionState.__init__)


def test_minuml1::actionstate_constructor_args():
    sig = inspect.signature(minuml1::ActionState.__init__)
    params = list(sig.parameters.keys())
    assert "isDynamic" in params, "Missing parameter 'isDynamic'"

def test_minuml1::actionstate_has_isDynamic():
    assert hasattr(minuml1::ActionState, "isDynamic")
    descriptor = None
    for klass in minuml1::ActionState.__mro__:
        if "isDynamic" in klass.__dict__:
            descriptor = klass.__dict__["isDynamic"]
            break
    assert isinstance(descriptor, property)



def test_minuml1::compositestate_is_not_abstract():
    assert not inspect.isabstract(minuml1::CompositeState)


def test_minuml1::compositestate_constructor_exists():
    assert callable(minuml1::CompositeState.__init__)


def test_minuml1::compositestate_constructor_args():
    sig = inspect.signature(minuml1::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_minuml1::activitygraph_is_not_abstract():
    assert not inspect.isabstract(minuml1::ActivityGraph)


def test_minuml1::activitygraph_constructor_exists():
    assert callable(minuml1::ActivityGraph.__init__)


def test_minuml1::activitygraph_constructor_args():
    sig = inspect.signature(minuml1::ActivityGraph.__init__)
    params = list(sig.parameters.keys())



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_minuml1::transition_is_not_abstract():
    assert not inspect.isabstract(minuml1::Transition)


def test_minuml1::transition_constructor_exists():
    assert callable(minuml1::Transition.__init__)


def test_minuml1::transition_constructor_args():
    sig = inspect.signature(minuml1::Transition.__init__)
    params = list(sig.parameters.keys())



def test_minuml1::partition_is_not_abstract():
    assert not inspect.isabstract(minuml1::Partition)


def test_minuml1::partition_constructor_exists():
    assert callable(minuml1::Partition.__init__)


def test_minuml1::partition_constructor_args():
    sig = inspect.signature(minuml1::Partition.__init__)
    params = list(sig.parameters.keys())



def test_minuml1::statemachine_is_not_abstract():
    assert not inspect.isabstract(minuml1::StateMachine)


def test_minuml1::statemachine_constructor_exists():
    assert callable(minuml1::StateMachine.__init__)


def test_minuml1::statemachine_constructor_args():
    sig = inspect.signature(minuml1::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_minuml1::modelelement_is_not_abstract():
    assert not inspect.isabstract(minuml1::ModelElement)


def test_minuml1::modelelement_constructor_exists():
    assert callable(minuml1::ModelElement.__init__)


def test_minuml1::modelelement_constructor_args():
    sig = inspect.signature(minuml1::ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minuml1::modelelement_has_name():
    assert hasattr(minuml1::ModelElement, "name")
    descriptor = None
    for klass in minuml1::ModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statevertex_is_not_abstract():
    assert not inspect.isabstract(StateVertex)


def test_statevertex_constructor_exists():
    assert callable(StateVertex.__init__)


def test_statevertex_constructor_args():
    sig = inspect.signature(StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_minuml1::state_is_not_abstract():
    assert not inspect.isabstract(minuml1::State)


def test_minuml1::state_constructor_exists():
    assert callable(minuml1::State.__init__)


def test_minuml1::state_constructor_args():
    sig = inspect.signature(minuml1::State.__init__)
    params = list(sig.parameters.keys())



def test_minuml1::statevertex_is_not_abstract():
    assert not inspect.isabstract(minuml1::StateVertex)


def test_minuml1::statevertex_constructor_exists():
    assert callable(minuml1::StateVertex.__init__)


def test_minuml1::statevertex_constructor_args():
    sig = inspect.signature(minuml1::StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_minuml1::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(minuml1::BooleanExpression)


def test_minuml1::booleanexpression_constructor_exists():
    assert callable(minuml1::BooleanExpression.__init__)


def test_minuml1::booleanexpression_constructor_args():
    sig = inspect.signature(minuml1::BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"

def test_minuml1::booleanexpression_has_language():
    assert hasattr(minuml1::BooleanExpression, "language")
    descriptor = None
    for klass in minuml1::BooleanExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_minuml1::booleanexpression_has_body():
    assert hasattr(minuml1::BooleanExpression, "body")
    descriptor = None
    for klass in minuml1::BooleanExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_minuml1::guard_is_not_abstract():
    assert not inspect.isabstract(minuml1::Guard)


def test_minuml1::guard_constructor_exists():
    assert callable(minuml1::Guard.__init__)


def test_minuml1::guard_constructor_args():
    sig = inspect.signature(minuml1::Guard.__init__)
    params = list(sig.parameters.keys())



def test_minuml1::finalstate_is_not_abstract():
    assert not inspect.isabstract(minuml1::FinalState)


def test_minuml1::finalstate_constructor_exists():
    assert callable(minuml1::FinalState.__init__)


def test_minuml1::finalstate_constructor_args():
    sig = inspect.signature(minuml1::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_minuml1::objectflowstate_is_not_abstract():
    assert not inspect.isabstract(minuml1::ObjectFlowState)


def test_minuml1::objectflowstate_constructor_exists():
    assert callable(minuml1::ObjectFlowState.__init__)


def test_minuml1::objectflowstate_constructor_args():
    sig = inspect.signature(minuml1::ObjectFlowState.__init__)
    params = list(sig.parameters.keys())



def test_minuml1::pseudostate_is_not_abstract():
    assert not inspect.isabstract(minuml1::Pseudostate)


def test_minuml1::pseudostate_constructor_exists():
    assert callable(minuml1::Pseudostate.__init__)


def test_minuml1::pseudostate_constructor_args():
    sig = inspect.signature(minuml1::Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_minuml1::pseudostate_has_kind():
    assert hasattr(minuml1::Pseudostate, "kind")
    descriptor = None
    for klass in minuml1::Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "initial",
        "junction",
        "join",
        "fork",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudostateKind"


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
State_strategy = st.builds(
    State,
)
minuml1::ActionState_strategy = st.builds(
    minuml1::ActionState,
    isDynamic=
        st.booleans()
)
minuml1::CompositeState_strategy = st.builds(
    minuml1::CompositeState,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
minuml1::ActivityGraph_strategy = st.builds(
    minuml1::ActivityGraph,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
minuml1::Transition_strategy = st.builds(
    minuml1::Transition,
)
minuml1::Partition_strategy = st.builds(
    minuml1::Partition,
)
minuml1::StateMachine_strategy = st.builds(
    minuml1::StateMachine,
)
minuml1::ModelElement_strategy = st.builds(
    minuml1::ModelElement,
    name=
        safe_text
)
StateVertex_strategy = st.builds(
    StateVertex,
)
minuml1::State_strategy = st.builds(
    minuml1::State,
)
minuml1::StateVertex_strategy = st.builds(
    minuml1::StateVertex,
)
minuml1::BooleanExpression_strategy = st.builds(
    minuml1::BooleanExpression,
    language=
        safe_text,
    body=
        safe_text
)
minuml1::Guard_strategy = st.builds(
    minuml1::Guard,
)
minuml1::FinalState_strategy = st.builds(
    minuml1::FinalState,
)
minuml1::ObjectFlowState_strategy = st.builds(
    minuml1::ObjectFlowState,
)
minuml1::Pseudostate_strategy = st.builds(
    minuml1::Pseudostate,
    kind=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=minuml1::ActionState_strategy)
@settings(max_examples=50)
def test_minuml1::actionstate_instantiation(instance):
    assert isinstance(instance, minuml1::ActionState)

@given(instance=minuml1::ActionState_strategy)
def test_minuml1::actionstate_isDynamic_type(instance):
    assert isinstance(instance.isDynamic, bool)


@given(instance=minuml1::ActionState_strategy)
def test_minuml1::actionstate_isDynamic_setter(instance):
    original = instance.isDynamic
    instance.isDynamic = original
    assert instance.isDynamic == original

@given(instance=minuml1::CompositeState_strategy)
@settings(max_examples=50)
def test_minuml1::compositestate_instantiation(instance):
    assert isinstance(instance, minuml1::CompositeState)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=minuml1::ActivityGraph_strategy)
@settings(max_examples=50)
def test_minuml1::activitygraph_instantiation(instance):
    assert isinstance(instance, minuml1::ActivityGraph)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=minuml1::Transition_strategy)
@settings(max_examples=50)
def test_minuml1::transition_instantiation(instance):
    assert isinstance(instance, minuml1::Transition)

@given(instance=minuml1::Partition_strategy)
@settings(max_examples=50)
def test_minuml1::partition_instantiation(instance):
    assert isinstance(instance, minuml1::Partition)

@given(instance=minuml1::StateMachine_strategy)
@settings(max_examples=50)
def test_minuml1::statemachine_instantiation(instance):
    assert isinstance(instance, minuml1::StateMachine)

@given(instance=minuml1::ModelElement_strategy)
@settings(max_examples=50)
def test_minuml1::modelelement_instantiation(instance):
    assert isinstance(instance, minuml1::ModelElement)

@given(instance=minuml1::ModelElement_strategy)
def test_minuml1::modelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=minuml1::ModelElement_strategy)
def test_minuml1::modelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateVertex_strategy)
@settings(max_examples=50)
def test_statevertex_instantiation(instance):
    assert isinstance(instance, StateVertex)

@given(instance=minuml1::State_strategy)
@settings(max_examples=50)
def test_minuml1::state_instantiation(instance):
    assert isinstance(instance, minuml1::State)

@given(instance=minuml1::StateVertex_strategy)
@settings(max_examples=50)
def test_minuml1::statevertex_instantiation(instance):
    assert isinstance(instance, minuml1::StateVertex)

@given(instance=minuml1::BooleanExpression_strategy)
@settings(max_examples=50)
def test_minuml1::booleanexpression_instantiation(instance):
    assert isinstance(instance, minuml1::BooleanExpression)

@given(instance=minuml1::BooleanExpression_strategy)
def test_minuml1::booleanexpression_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=minuml1::BooleanExpression_strategy)
def test_minuml1::booleanexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=minuml1::BooleanExpression_strategy)
def test_minuml1::booleanexpression_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=minuml1::BooleanExpression_strategy)
def test_minuml1::booleanexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=minuml1::Guard_strategy)
@settings(max_examples=50)
def test_minuml1::guard_instantiation(instance):
    assert isinstance(instance, minuml1::Guard)

@given(instance=minuml1::FinalState_strategy)
@settings(max_examples=50)
def test_minuml1::finalstate_instantiation(instance):
    assert isinstance(instance, minuml1::FinalState)

@given(instance=minuml1::ObjectFlowState_strategy)
@settings(max_examples=50)
def test_minuml1::objectflowstate_instantiation(instance):
    assert isinstance(instance, minuml1::ObjectFlowState)

@given(instance=minuml1::Pseudostate_strategy)
@settings(max_examples=50)
def test_minuml1::pseudostate_instantiation(instance):
    assert isinstance(instance, minuml1::Pseudostate)

@given(instance=minuml1::Pseudostate_strategy)
def test_minuml1::pseudostate_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=minuml1::Pseudostate_strategy)
def test_minuml1::pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original
