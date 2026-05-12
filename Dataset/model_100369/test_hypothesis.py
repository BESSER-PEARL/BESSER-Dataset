import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fsm_NamedElement,
    Statement,
    State,
    fsm_FinalState,
    Pseudostate,
    fsm_Fork,
    fsm_Join,
    fsm_Conditional,
    fsm_ShallowHistory,
    fsm_Junction,
    fsm_InitialState,
    fsm_Constraint,
    fsm_Statement,
    fsm_Trigger,
    fsm_Program,
    AbstractState,
    fsm_Pseudostate,
    fsm_State,
    NamedElement,
    fsm_Transition,
    fsm_Region,
    fsm_AbstractState,
    fsm_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm_namedelement_is_not_abstract():
    assert not inspect.isabstract(fsm_NamedElement)


def test_fsm_namedelement_constructor_exists():
    assert callable(fsm_NamedElement.__init__)


def test_fsm_namedelement_constructor_args():
    sig = inspect.signature(fsm_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_namedelement_has_name():
    assert hasattr(fsm_NamedElement, "name")
    descriptor = None
    for klass in fsm_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_fsm_finalstate_is_not_abstract():
    assert not inspect.isabstract(fsm_FinalState)


def test_fsm_finalstate_constructor_exists():
    assert callable(fsm_FinalState.__init__)


def test_fsm_finalstate_constructor_args():
    sig = inspect.signature(fsm_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_pseudostate_is_not_abstract():
    assert not inspect.isabstract(Pseudostate)


def test_pseudostate_constructor_exists():
    assert callable(Pseudostate.__init__)


def test_pseudostate_constructor_args():
    sig = inspect.signature(Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_fsm_fork_is_not_abstract():
    assert not inspect.isabstract(fsm_Fork)


def test_fsm_fork_constructor_exists():
    assert callable(fsm_Fork.__init__)


def test_fsm_fork_constructor_args():
    sig = inspect.signature(fsm_Fork.__init__)
    params = list(sig.parameters.keys())



def test_fsm_join_is_not_abstract():
    assert not inspect.isabstract(fsm_Join)


def test_fsm_join_constructor_exists():
    assert callable(fsm_Join.__init__)


def test_fsm_join_constructor_args():
    sig = inspect.signature(fsm_Join.__init__)
    params = list(sig.parameters.keys())



def test_fsm_conditional_is_not_abstract():
    assert not inspect.isabstract(fsm_Conditional)


def test_fsm_conditional_constructor_exists():
    assert callable(fsm_Conditional.__init__)


def test_fsm_conditional_constructor_args():
    sig = inspect.signature(fsm_Conditional.__init__)
    params = list(sig.parameters.keys())



def test_fsm_shallowhistory_is_not_abstract():
    assert not inspect.isabstract(fsm_ShallowHistory)


def test_fsm_shallowhistory_constructor_exists():
    assert callable(fsm_ShallowHistory.__init__)


def test_fsm_shallowhistory_constructor_args():
    sig = inspect.signature(fsm_ShallowHistory.__init__)
    params = list(sig.parameters.keys())



def test_fsm_junction_is_not_abstract():
    assert not inspect.isabstract(fsm_Junction)


def test_fsm_junction_constructor_exists():
    assert callable(fsm_Junction.__init__)


def test_fsm_junction_constructor_args():
    sig = inspect.signature(fsm_Junction.__init__)
    params = list(sig.parameters.keys())



def test_fsm_initialstate_is_not_abstract():
    assert not inspect.isabstract(fsm_InitialState)


def test_fsm_initialstate_constructor_exists():
    assert callable(fsm_InitialState.__init__)


def test_fsm_initialstate_constructor_args():
    sig = inspect.signature(fsm_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_constraint_is_not_abstract():
    assert not inspect.isabstract(fsm_Constraint)


def test_fsm_constraint_constructor_exists():
    assert callable(fsm_Constraint.__init__)


def test_fsm_constraint_constructor_args():
    sig = inspect.signature(fsm_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_fsm_statement_is_not_abstract():
    assert not inspect.isabstract(fsm_Statement)


def test_fsm_statement_constructor_exists():
    assert callable(fsm_Statement.__init__)


def test_fsm_statement_constructor_args():
    sig = inspect.signature(fsm_Statement.__init__)
    params = list(sig.parameters.keys())



def test_fsm_trigger_is_not_abstract():
    assert not inspect.isabstract(fsm_Trigger)


def test_fsm_trigger_constructor_exists():
    assert callable(fsm_Trigger.__init__)


def test_fsm_trigger_constructor_args():
    sig = inspect.signature(fsm_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_fsm_trigger_has_expression():
    assert hasattr(fsm_Trigger, "expression")
    descriptor = None
    for klass in fsm_Trigger.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_fsm_program_is_not_abstract():
    assert not inspect.isabstract(fsm_Program)


def test_fsm_program_constructor_exists():
    assert callable(fsm_Program.__init__)


def test_fsm_program_constructor_args():
    sig = inspect.signature(fsm_Program.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_pseudostate_is_not_abstract():
    assert not inspect.isabstract(fsm_Pseudostate)


def test_fsm_pseudostate_constructor_exists():
    assert callable(fsm_Pseudostate.__init__)


def test_fsm_pseudostate_constructor_args():
    sig = inspect.signature(fsm_Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_fsm_state_is_not_abstract():
    assert not inspect.isabstract(fsm_State)


def test_fsm_state_constructor_exists():
    assert callable(fsm_State.__init__)


def test_fsm_state_constructor_args():
    sig = inspect.signature(fsm_State.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_Transition)


def test_fsm_transition_constructor_exists():
    assert callable(fsm_Transition.__init__)


def test_fsm_transition_constructor_args():
    sig = inspect.signature(fsm_Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsm_region_is_not_abstract():
    assert not inspect.isabstract(fsm_Region)


def test_fsm_region_constructor_exists():
    assert callable(fsm_Region.__init__)


def test_fsm_region_constructor_args():
    sig = inspect.signature(fsm_Region.__init__)
    params = list(sig.parameters.keys())



def test_fsm_abstractstate_is_not_abstract():
    assert not inspect.isabstract(fsm_AbstractState)


def test_fsm_abstractstate_constructor_exists():
    assert callable(fsm_AbstractState.__init__)


def test_fsm_abstractstate_constructor_args():
    sig = inspect.signature(fsm_AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(fsm_StateMachine)


def test_fsm_statemachine_constructor_exists():
    assert callable(fsm_StateMachine.__init__)


def test_fsm_statemachine_constructor_args():
    sig = inspect.signature(fsm_StateMachine.__init__)
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
fsm_NamedElement_strategy = st.builds(
    fsm_NamedElement,
    name=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
State_strategy = st.builds(
    State,
)
fsm_FinalState_strategy = st.builds(
    fsm_FinalState,
)
Pseudostate_strategy = st.builds(
    Pseudostate,
)
fsm_Fork_strategy = st.builds(
    fsm_Fork,
)
fsm_Join_strategy = st.builds(
    fsm_Join,
)
fsm_Conditional_strategy = st.builds(
    fsm_Conditional,
)
fsm_ShallowHistory_strategy = st.builds(
    fsm_ShallowHistory,
)
fsm_Junction_strategy = st.builds(
    fsm_Junction,
)
fsm_InitialState_strategy = st.builds(
    fsm_InitialState,
)
fsm_Constraint_strategy = st.builds(
    fsm_Constraint,
)
fsm_Statement_strategy = st.builds(
    fsm_Statement,
)
fsm_Trigger_strategy = st.builds(
    fsm_Trigger,
    expression=
        safe_text
)
fsm_Program_strategy = st.builds(
    fsm_Program,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
fsm_Pseudostate_strategy = st.builds(
    fsm_Pseudostate,
)
fsm_State_strategy = st.builds(
    fsm_State,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
fsm_Transition_strategy = st.builds(
    fsm_Transition,
)
fsm_Region_strategy = st.builds(
    fsm_Region,
)
fsm_AbstractState_strategy = st.builds(
    fsm_AbstractState,
)
fsm_StateMachine_strategy = st.builds(
    fsm_StateMachine,
)

@given(instance=fsm_NamedElement_strategy)
@settings(max_examples=50)
def test_fsm_namedelement_instantiation(instance):
    assert isinstance(instance, fsm_NamedElement)



@given(instance=fsm_NamedElement_strategy)
def test_fsm_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=fsm_FinalState_strategy)
@settings(max_examples=50)
def test_fsm_finalstate_instantiation(instance):
    assert isinstance(instance, fsm_FinalState)

@given(instance=Pseudostate_strategy)
@settings(max_examples=50)
def test_pseudostate_instantiation(instance):
    assert isinstance(instance, Pseudostate)

@given(instance=fsm_Fork_strategy)
@settings(max_examples=50)
def test_fsm_fork_instantiation(instance):
    assert isinstance(instance, fsm_Fork)

@given(instance=fsm_Join_strategy)
@settings(max_examples=50)
def test_fsm_join_instantiation(instance):
    assert isinstance(instance, fsm_Join)

@given(instance=fsm_Conditional_strategy)
@settings(max_examples=50)
def test_fsm_conditional_instantiation(instance):
    assert isinstance(instance, fsm_Conditional)

@given(instance=fsm_ShallowHistory_strategy)
@settings(max_examples=50)
def test_fsm_shallowhistory_instantiation(instance):
    assert isinstance(instance, fsm_ShallowHistory)

@given(instance=fsm_Junction_strategy)
@settings(max_examples=50)
def test_fsm_junction_instantiation(instance):
    assert isinstance(instance, fsm_Junction)

@given(instance=fsm_InitialState_strategy)
@settings(max_examples=50)
def test_fsm_initialstate_instantiation(instance):
    assert isinstance(instance, fsm_InitialState)

@given(instance=fsm_Constraint_strategy)
@settings(max_examples=50)
def test_fsm_constraint_instantiation(instance):
    assert isinstance(instance, fsm_Constraint)

@given(instance=fsm_Statement_strategy)
@settings(max_examples=50)
def test_fsm_statement_instantiation(instance):
    assert isinstance(instance, fsm_Statement)

@given(instance=fsm_Trigger_strategy)
@settings(max_examples=50)
def test_fsm_trigger_instantiation(instance):
    assert isinstance(instance, fsm_Trigger)



@given(instance=fsm_Trigger_strategy)
def test_fsm_trigger_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=fsm_Program_strategy)
@settings(max_examples=50)
def test_fsm_program_instantiation(instance):
    assert isinstance(instance, fsm_Program)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=fsm_Pseudostate_strategy)
@settings(max_examples=50)
def test_fsm_pseudostate_instantiation(instance):
    assert isinstance(instance, fsm_Pseudostate)

@given(instance=fsm_State_strategy)
@settings(max_examples=50)
def test_fsm_state_instantiation(instance):
    assert isinstance(instance, fsm_State)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=fsm_Transition_strategy)
@settings(max_examples=50)
def test_fsm_transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)

@given(instance=fsm_Region_strategy)
@settings(max_examples=50)
def test_fsm_region_instantiation(instance):
    assert isinstance(instance, fsm_Region)

@given(instance=fsm_AbstractState_strategy)
@settings(max_examples=50)
def test_fsm_abstractstate_instantiation(instance):
    assert isinstance(instance, fsm_AbstractState)

@given(instance=fsm_StateMachine_strategy)
@settings(max_examples=50)
def test_fsm_statemachine_instantiation(instance):
    assert isinstance(instance, fsm_StateMachine)
