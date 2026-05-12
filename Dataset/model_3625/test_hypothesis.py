import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    minuml1_BooleanExpression,
    StateMachine,
    minuml1_ActivityGraph,
    ModelElement,
    minuml1_Guard,
    minuml1_StateVertex,
    minuml1_Transition,
    minuml1_StateMachine,
    minuml1_Partition,
    minuml1_ModelElement,
    State,
    minuml1_ObjectFlowState,
    minuml1_FinalState,
    minuml1_ActionState,
    minuml1_CompositeState,
    StateVertex,
    minuml1_Pseudostate,
    minuml1_State,
    PseudostateKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_minuml1_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(minuml1_BooleanExpression)


def test_minuml1_booleanexpression_constructor_exists():
    assert callable(minuml1_BooleanExpression.__init__)


def test_minuml1_booleanexpression_constructor_args():
    sig = inspect.signature(minuml1_BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_minuml1_booleanexpression_has_body():
    assert hasattr(minuml1_BooleanExpression, "body")
    descriptor = None
    for klass in minuml1_BooleanExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_minuml1_booleanexpression_has_language():
    assert hasattr(minuml1_BooleanExpression, "language")
    descriptor = None
    for klass in minuml1_BooleanExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_minuml1_activitygraph_is_not_abstract():
    assert not inspect.isabstract(minuml1_ActivityGraph)


def test_minuml1_activitygraph_constructor_exists():
    assert callable(minuml1_ActivityGraph.__init__)


def test_minuml1_activitygraph_constructor_args():
    sig = inspect.signature(minuml1_ActivityGraph.__init__)
    params = list(sig.parameters.keys())



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_minuml1_guard_is_not_abstract():
    assert not inspect.isabstract(minuml1_Guard)


def test_minuml1_guard_constructor_exists():
    assert callable(minuml1_Guard.__init__)


def test_minuml1_guard_constructor_args():
    sig = inspect.signature(minuml1_Guard.__init__)
    params = list(sig.parameters.keys())



def test_minuml1_statevertex_is_not_abstract():
    assert not inspect.isabstract(minuml1_StateVertex)


def test_minuml1_statevertex_constructor_exists():
    assert callable(minuml1_StateVertex.__init__)


def test_minuml1_statevertex_constructor_args():
    sig = inspect.signature(minuml1_StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_minuml1_transition_is_not_abstract():
    assert not inspect.isabstract(minuml1_Transition)


def test_minuml1_transition_constructor_exists():
    assert callable(minuml1_Transition.__init__)


def test_minuml1_transition_constructor_args():
    sig = inspect.signature(minuml1_Transition.__init__)
    params = list(sig.parameters.keys())



def test_minuml1_statemachine_is_not_abstract():
    assert not inspect.isabstract(minuml1_StateMachine)


def test_minuml1_statemachine_constructor_exists():
    assert callable(minuml1_StateMachine.__init__)


def test_minuml1_statemachine_constructor_args():
    sig = inspect.signature(minuml1_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_minuml1_partition_is_not_abstract():
    assert not inspect.isabstract(minuml1_Partition)


def test_minuml1_partition_constructor_exists():
    assert callable(minuml1_Partition.__init__)


def test_minuml1_partition_constructor_args():
    sig = inspect.signature(minuml1_Partition.__init__)
    params = list(sig.parameters.keys())



def test_minuml1_modelelement_is_not_abstract():
    assert not inspect.isabstract(minuml1_ModelElement)


def test_minuml1_modelelement_constructor_exists():
    assert callable(minuml1_ModelElement.__init__)


def test_minuml1_modelelement_constructor_args():
    sig = inspect.signature(minuml1_ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minuml1_modelelement_has_name():
    assert hasattr(minuml1_ModelElement, "name")
    descriptor = None
    for klass in minuml1_ModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_minuml1_objectflowstate_is_not_abstract():
    assert not inspect.isabstract(minuml1_ObjectFlowState)


def test_minuml1_objectflowstate_constructor_exists():
    assert callable(minuml1_ObjectFlowState.__init__)


def test_minuml1_objectflowstate_constructor_args():
    sig = inspect.signature(minuml1_ObjectFlowState.__init__)
    params = list(sig.parameters.keys())



def test_minuml1_finalstate_is_not_abstract():
    assert not inspect.isabstract(minuml1_FinalState)


def test_minuml1_finalstate_constructor_exists():
    assert callable(minuml1_FinalState.__init__)


def test_minuml1_finalstate_constructor_args():
    sig = inspect.signature(minuml1_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_minuml1_actionstate_is_not_abstract():
    assert not inspect.isabstract(minuml1_ActionState)


def test_minuml1_actionstate_constructor_exists():
    assert callable(minuml1_ActionState.__init__)


def test_minuml1_actionstate_constructor_args():
    sig = inspect.signature(minuml1_ActionState.__init__)
    params = list(sig.parameters.keys())
    assert "isDynamic" in params, "Missing parameter 'isDynamic'"

def test_minuml1_actionstate_has_isDynamic():
    assert hasattr(minuml1_ActionState, "isDynamic")
    descriptor = None
    for klass in minuml1_ActionState.__mro__:
        if "isDynamic" in klass.__dict__:
            descriptor = klass.__dict__["isDynamic"]
            break
    assert isinstance(descriptor, property)



def test_minuml1_compositestate_is_not_abstract():
    assert not inspect.isabstract(minuml1_CompositeState)


def test_minuml1_compositestate_constructor_exists():
    assert callable(minuml1_CompositeState.__init__)


def test_minuml1_compositestate_constructor_args():
    sig = inspect.signature(minuml1_CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_statevertex_is_not_abstract():
    assert not inspect.isabstract(StateVertex)


def test_statevertex_constructor_exists():
    assert callable(StateVertex.__init__)


def test_statevertex_constructor_args():
    sig = inspect.signature(StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_minuml1_pseudostate_is_not_abstract():
    assert not inspect.isabstract(minuml1_Pseudostate)


def test_minuml1_pseudostate_constructor_exists():
    assert callable(minuml1_Pseudostate.__init__)


def test_minuml1_pseudostate_constructor_args():
    sig = inspect.signature(minuml1_Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_minuml1_pseudostate_has_kind():
    assert hasattr(minuml1_Pseudostate, "kind")
    descriptor = None
    for klass in minuml1_Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_minuml1_state_is_not_abstract():
    assert not inspect.isabstract(minuml1_State)


def test_minuml1_state_constructor_exists():
    assert callable(minuml1_State.__init__)


def test_minuml1_state_constructor_args():
    sig = inspect.signature(minuml1_State.__init__)
    params = list(sig.parameters.keys())

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "fork",
        "inital",
        "junction",
        "join",
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
minuml1_BooleanExpression_strategy = st.builds(
    minuml1_BooleanExpression,
    body=
        safe_text,
    language=
        safe_text
)
StateMachine_strategy = st.builds(
    StateMachine,
)
minuml1_ActivityGraph_strategy = st.builds(
    minuml1_ActivityGraph,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
minuml1_Guard_strategy = st.builds(
    minuml1_Guard,
)
minuml1_StateVertex_strategy = st.builds(
    minuml1_StateVertex,
)
minuml1_Transition_strategy = st.builds(
    minuml1_Transition,
)
minuml1_StateMachine_strategy = st.builds(
    minuml1_StateMachine,
)
minuml1_Partition_strategy = st.builds(
    minuml1_Partition,
)
minuml1_ModelElement_strategy = st.builds(
    minuml1_ModelElement,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
minuml1_ObjectFlowState_strategy = st.builds(
    minuml1_ObjectFlowState,
)
minuml1_FinalState_strategy = st.builds(
    minuml1_FinalState,
)
minuml1_ActionState_strategy = st.builds(
    minuml1_ActionState,
    isDynamic=
        st.booleans()
)
minuml1_CompositeState_strategy = st.builds(
    minuml1_CompositeState,
)
StateVertex_strategy = st.builds(
    StateVertex,
)
minuml1_Pseudostate_strategy = st.builds(
    minuml1_Pseudostate,
    kind=
        safe_text
)
minuml1_State_strategy = st.builds(
    minuml1_State,
)

@given(instance=minuml1_BooleanExpression_strategy)
@settings(max_examples=50)
def test_minuml1_booleanexpression_instantiation(instance):
    assert isinstance(instance, minuml1_BooleanExpression)



@given(instance=minuml1_BooleanExpression_strategy)
def test_minuml1_booleanexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=minuml1_BooleanExpression_strategy)
def test_minuml1_booleanexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=minuml1_ActivityGraph_strategy)
@settings(max_examples=50)
def test_minuml1_activitygraph_instantiation(instance):
    assert isinstance(instance, minuml1_ActivityGraph)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=minuml1_Guard_strategy)
@settings(max_examples=50)
def test_minuml1_guard_instantiation(instance):
    assert isinstance(instance, minuml1_Guard)

@given(instance=minuml1_StateVertex_strategy)
@settings(max_examples=50)
def test_minuml1_statevertex_instantiation(instance):
    assert isinstance(instance, minuml1_StateVertex)

@given(instance=minuml1_Transition_strategy)
@settings(max_examples=50)
def test_minuml1_transition_instantiation(instance):
    assert isinstance(instance, minuml1_Transition)

@given(instance=minuml1_StateMachine_strategy)
@settings(max_examples=50)
def test_minuml1_statemachine_instantiation(instance):
    assert isinstance(instance, minuml1_StateMachine)

@given(instance=minuml1_Partition_strategy)
@settings(max_examples=50)
def test_minuml1_partition_instantiation(instance):
    assert isinstance(instance, minuml1_Partition)

@given(instance=minuml1_ModelElement_strategy)
@settings(max_examples=50)
def test_minuml1_modelelement_instantiation(instance):
    assert isinstance(instance, minuml1_ModelElement)



@given(instance=minuml1_ModelElement_strategy)
def test_minuml1_modelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=minuml1_ObjectFlowState_strategy)
@settings(max_examples=50)
def test_minuml1_objectflowstate_instantiation(instance):
    assert isinstance(instance, minuml1_ObjectFlowState)

@given(instance=minuml1_FinalState_strategy)
@settings(max_examples=50)
def test_minuml1_finalstate_instantiation(instance):
    assert isinstance(instance, minuml1_FinalState)

@given(instance=minuml1_ActionState_strategy)
@settings(max_examples=50)
def test_minuml1_actionstate_instantiation(instance):
    assert isinstance(instance, minuml1_ActionState)



@given(instance=minuml1_ActionState_strategy)
def test_minuml1_actionstate_isDynamic_setter(instance):
    original = instance.isDynamic
    instance.isDynamic = original
    assert instance.isDynamic == original

@given(instance=minuml1_CompositeState_strategy)
@settings(max_examples=50)
def test_minuml1_compositestate_instantiation(instance):
    assert isinstance(instance, minuml1_CompositeState)

@given(instance=StateVertex_strategy)
@settings(max_examples=50)
def test_statevertex_instantiation(instance):
    assert isinstance(instance, StateVertex)

@given(instance=minuml1_Pseudostate_strategy)
@settings(max_examples=50)
def test_minuml1_pseudostate_instantiation(instance):
    assert isinstance(instance, minuml1_Pseudostate)



@given(instance=minuml1_Pseudostate_strategy)
def test_minuml1_pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=minuml1_State_strategy)
@settings(max_examples=50)
def test_minuml1_state_instantiation(instance):
    assert isinstance(instance, minuml1_State)
