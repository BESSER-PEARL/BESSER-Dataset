import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsm::NamedElement,
    Statement,
    State,
    fsm::FinalState,
    Pseudostate,
    fsm::Join,
    fsm::DeepHistory,
    fsm::ShallowHistory,
    fsm::Conditional,
    fsm::Junction,
    fsm::Fork,
    fsm::InitialState,
    Trigger,
    fsm::AndTrigger,
    fsm::OrTrigger,
    fsm::NotTrigger,
    fsm::Constraint,
    fsm::Statement,
    fsm::Trigger,
    fsm::Program,
    AbstractState,
    fsm::Pseudostate,
    fsm::State,
    NamedElement,
    fsm::Transition,
    fsm::Region,
    fsm::AbstractState,
    fsm::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::namedelement_is_not_abstract():
    assert not inspect.isabstract(fsm::NamedElement)


def test_fsm::namedelement_constructor_exists():
    assert callable(fsm::NamedElement.__init__)


def test_fsm::namedelement_constructor_args():
    sig = inspect.signature(fsm::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::namedelement_has_name():
    assert hasattr(fsm::NamedElement, "name")
    descriptor = None
    for klass in fsm::NamedElement.__mro__:
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



def test_fsm::finalstate_is_not_abstract():
    assert not inspect.isabstract(fsm::FinalState)


def test_fsm::finalstate_constructor_exists():
    assert callable(fsm::FinalState.__init__)


def test_fsm::finalstate_constructor_args():
    sig = inspect.signature(fsm::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_pseudostate_is_not_abstract():
    assert not inspect.isabstract(Pseudostate)


def test_pseudostate_constructor_exists():
    assert callable(Pseudostate.__init__)


def test_pseudostate_constructor_args():
    sig = inspect.signature(Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_fsm::join_is_not_abstract():
    assert not inspect.isabstract(fsm::Join)


def test_fsm::join_constructor_exists():
    assert callable(fsm::Join.__init__)


def test_fsm::join_constructor_args():
    sig = inspect.signature(fsm::Join.__init__)
    params = list(sig.parameters.keys())



def test_fsm::deephistory_is_not_abstract():
    assert not inspect.isabstract(fsm::DeepHistory)


def test_fsm::deephistory_constructor_exists():
    assert callable(fsm::DeepHistory.__init__)


def test_fsm::deephistory_constructor_args():
    sig = inspect.signature(fsm::DeepHistory.__init__)
    params = list(sig.parameters.keys())



def test_fsm::shallowhistory_is_not_abstract():
    assert not inspect.isabstract(fsm::ShallowHistory)


def test_fsm::shallowhistory_constructor_exists():
    assert callable(fsm::ShallowHistory.__init__)


def test_fsm::shallowhistory_constructor_args():
    sig = inspect.signature(fsm::ShallowHistory.__init__)
    params = list(sig.parameters.keys())



def test_fsm::conditional_is_not_abstract():
    assert not inspect.isabstract(fsm::Conditional)


def test_fsm::conditional_constructor_exists():
    assert callable(fsm::Conditional.__init__)


def test_fsm::conditional_constructor_args():
    sig = inspect.signature(fsm::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_fsm::junction_is_not_abstract():
    assert not inspect.isabstract(fsm::Junction)


def test_fsm::junction_constructor_exists():
    assert callable(fsm::Junction.__init__)


def test_fsm::junction_constructor_args():
    sig = inspect.signature(fsm::Junction.__init__)
    params = list(sig.parameters.keys())



def test_fsm::fork_is_not_abstract():
    assert not inspect.isabstract(fsm::Fork)


def test_fsm::fork_constructor_exists():
    assert callable(fsm::Fork.__init__)


def test_fsm::fork_constructor_args():
    sig = inspect.signature(fsm::Fork.__init__)
    params = list(sig.parameters.keys())



def test_fsm::initialstate_is_not_abstract():
    assert not inspect.isabstract(fsm::InitialState)


def test_fsm::initialstate_constructor_exists():
    assert callable(fsm::InitialState.__init__)


def test_fsm::initialstate_constructor_args():
    sig = inspect.signature(fsm::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_fsm::andtrigger_is_not_abstract():
    assert not inspect.isabstract(fsm::AndTrigger)


def test_fsm::andtrigger_constructor_exists():
    assert callable(fsm::AndTrigger.__init__)


def test_fsm::andtrigger_constructor_args():
    sig = inspect.signature(fsm::AndTrigger.__init__)
    params = list(sig.parameters.keys())



def test_fsm::ortrigger_is_not_abstract():
    assert not inspect.isabstract(fsm::OrTrigger)


def test_fsm::ortrigger_constructor_exists():
    assert callable(fsm::OrTrigger.__init__)


def test_fsm::ortrigger_constructor_args():
    sig = inspect.signature(fsm::OrTrigger.__init__)
    params = list(sig.parameters.keys())



def test_fsm::nottrigger_is_not_abstract():
    assert not inspect.isabstract(fsm::NotTrigger)


def test_fsm::nottrigger_constructor_exists():
    assert callable(fsm::NotTrigger.__init__)


def test_fsm::nottrigger_constructor_args():
    sig = inspect.signature(fsm::NotTrigger.__init__)
    params = list(sig.parameters.keys())



def test_fsm::constraint_is_not_abstract():
    assert not inspect.isabstract(fsm::Constraint)


def test_fsm::constraint_constructor_exists():
    assert callable(fsm::Constraint.__init__)


def test_fsm::constraint_constructor_args():
    sig = inspect.signature(fsm::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_fsm::statement_is_not_abstract():
    assert not inspect.isabstract(fsm::Statement)


def test_fsm::statement_constructor_exists():
    assert callable(fsm::Statement.__init__)


def test_fsm::statement_constructor_args():
    sig = inspect.signature(fsm::Statement.__init__)
    params = list(sig.parameters.keys())



def test_fsm::trigger_is_not_abstract():
    assert not inspect.isabstract(fsm::Trigger)


def test_fsm::trigger_constructor_exists():
    assert callable(fsm::Trigger.__init__)


def test_fsm::trigger_constructor_args():
    sig = inspect.signature(fsm::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_fsm::trigger_has_expression():
    assert hasattr(fsm::Trigger, "expression")
    descriptor = None
    for klass in fsm::Trigger.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_fsm::program_is_not_abstract():
    assert not inspect.isabstract(fsm::Program)


def test_fsm::program_constructor_exists():
    assert callable(fsm::Program.__init__)


def test_fsm::program_constructor_args():
    sig = inspect.signature(fsm::Program.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::pseudostate_is_not_abstract():
    assert not inspect.isabstract(fsm::Pseudostate)


def test_fsm::pseudostate_constructor_exists():
    assert callable(fsm::Pseudostate.__init__)


def test_fsm::pseudostate_constructor_args():
    sig = inspect.signature(fsm::Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(fsm::State)


def test_fsm::state_constructor_exists():
    assert callable(fsm::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(fsm::State.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(fsm::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(fsm::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(fsm::Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsm::region_is_not_abstract():
    assert not inspect.isabstract(fsm::Region)


def test_fsm::region_constructor_exists():
    assert callable(fsm::Region.__init__)


def test_fsm::region_constructor_args():
    sig = inspect.signature(fsm::Region.__init__)
    params = list(sig.parameters.keys())



def test_fsm::abstractstate_is_not_abstract():
    assert not inspect.isabstract(fsm::AbstractState)


def test_fsm::abstractstate_constructor_exists():
    assert callable(fsm::AbstractState.__init__)


def test_fsm::abstractstate_constructor_args():
    sig = inspect.signature(fsm::AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(fsm::StateMachine)


def test_fsm::statemachine_constructor_exists():
    assert callable(fsm::StateMachine.__init__)


def test_fsm::statemachine_constructor_args():
    sig = inspect.signature(fsm::StateMachine.__init__)
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
fsm::NamedElement_strategy = st.builds(
    fsm::NamedElement,
    name=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
State_strategy = st.builds(
    State,
)
fsm::FinalState_strategy = st.builds(
    fsm::FinalState,
)
Pseudostate_strategy = st.builds(
    Pseudostate,
)
fsm::Join_strategy = st.builds(
    fsm::Join,
)
fsm::DeepHistory_strategy = st.builds(
    fsm::DeepHistory,
)
fsm::ShallowHistory_strategy = st.builds(
    fsm::ShallowHistory,
)
fsm::Conditional_strategy = st.builds(
    fsm::Conditional,
)
fsm::Junction_strategy = st.builds(
    fsm::Junction,
)
fsm::Fork_strategy = st.builds(
    fsm::Fork,
)
fsm::InitialState_strategy = st.builds(
    fsm::InitialState,
)
Trigger_strategy = st.builds(
    Trigger,
)
fsm::AndTrigger_strategy = st.builds(
    fsm::AndTrigger,
)
fsm::OrTrigger_strategy = st.builds(
    fsm::OrTrigger,
)
fsm::NotTrigger_strategy = st.builds(
    fsm::NotTrigger,
)
fsm::Constraint_strategy = st.builds(
    fsm::Constraint,
)
fsm::Statement_strategy = st.builds(
    fsm::Statement,
)
fsm::Trigger_strategy = st.builds(
    fsm::Trigger,
    expression=
        safe_text
)
fsm::Program_strategy = st.builds(
    fsm::Program,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
fsm::Pseudostate_strategy = st.builds(
    fsm::Pseudostate,
)
fsm::State_strategy = st.builds(
    fsm::State,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
fsm::Transition_strategy = st.builds(
    fsm::Transition,
)
fsm::Region_strategy = st.builds(
    fsm::Region,
)
fsm::AbstractState_strategy = st.builds(
    fsm::AbstractState,
)
fsm::StateMachine_strategy = st.builds(
    fsm::StateMachine,
)

@given(instance=fsm::NamedElement_strategy)
@settings(max_examples=50)
def test_fsm::namedelement_instantiation(instance):
    assert isinstance(instance, fsm::NamedElement)

@given(instance=fsm::NamedElement_strategy)
def test_fsm::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::NamedElement_strategy)
def test_fsm::namedelement_name_setter(instance):
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

@given(instance=fsm::FinalState_strategy)
@settings(max_examples=50)
def test_fsm::finalstate_instantiation(instance):
    assert isinstance(instance, fsm::FinalState)

@given(instance=Pseudostate_strategy)
@settings(max_examples=50)
def test_pseudostate_instantiation(instance):
    assert isinstance(instance, Pseudostate)

@given(instance=fsm::Join_strategy)
@settings(max_examples=50)
def test_fsm::join_instantiation(instance):
    assert isinstance(instance, fsm::Join)

@given(instance=fsm::DeepHistory_strategy)
@settings(max_examples=50)
def test_fsm::deephistory_instantiation(instance):
    assert isinstance(instance, fsm::DeepHistory)

@given(instance=fsm::ShallowHistory_strategy)
@settings(max_examples=50)
def test_fsm::shallowhistory_instantiation(instance):
    assert isinstance(instance, fsm::ShallowHistory)

@given(instance=fsm::Conditional_strategy)
@settings(max_examples=50)
def test_fsm::conditional_instantiation(instance):
    assert isinstance(instance, fsm::Conditional)

@given(instance=fsm::Junction_strategy)
@settings(max_examples=50)
def test_fsm::junction_instantiation(instance):
    assert isinstance(instance, fsm::Junction)

@given(instance=fsm::Fork_strategy)
@settings(max_examples=50)
def test_fsm::fork_instantiation(instance):
    assert isinstance(instance, fsm::Fork)

@given(instance=fsm::InitialState_strategy)
@settings(max_examples=50)
def test_fsm::initialstate_instantiation(instance):
    assert isinstance(instance, fsm::InitialState)

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=fsm::AndTrigger_strategy)
@settings(max_examples=50)
def test_fsm::andtrigger_instantiation(instance):
    assert isinstance(instance, fsm::AndTrigger)

@given(instance=fsm::OrTrigger_strategy)
@settings(max_examples=50)
def test_fsm::ortrigger_instantiation(instance):
    assert isinstance(instance, fsm::OrTrigger)

@given(instance=fsm::NotTrigger_strategy)
@settings(max_examples=50)
def test_fsm::nottrigger_instantiation(instance):
    assert isinstance(instance, fsm::NotTrigger)

@given(instance=fsm::Constraint_strategy)
@settings(max_examples=50)
def test_fsm::constraint_instantiation(instance):
    assert isinstance(instance, fsm::Constraint)

@given(instance=fsm::Statement_strategy)
@settings(max_examples=50)
def test_fsm::statement_instantiation(instance):
    assert isinstance(instance, fsm::Statement)

@given(instance=fsm::Trigger_strategy)
@settings(max_examples=50)
def test_fsm::trigger_instantiation(instance):
    assert isinstance(instance, fsm::Trigger)

@given(instance=fsm::Trigger_strategy)
def test_fsm::trigger_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=fsm::Trigger_strategy)
def test_fsm::trigger_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=fsm::Program_strategy)
@settings(max_examples=50)
def test_fsm::program_instantiation(instance):
    assert isinstance(instance, fsm::Program)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=fsm::Pseudostate_strategy)
@settings(max_examples=50)
def test_fsm::pseudostate_instantiation(instance):
    assert isinstance(instance, fsm::Pseudostate)

@given(instance=fsm::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, fsm::State)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=fsm::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, fsm::Transition)

@given(instance=fsm::Region_strategy)
@settings(max_examples=50)
def test_fsm::region_instantiation(instance):
    assert isinstance(instance, fsm::Region)

@given(instance=fsm::AbstractState_strategy)
@settings(max_examples=50)
def test_fsm::abstractstate_instantiation(instance):
    assert isinstance(instance, fsm::AbstractState)

@given(instance=fsm::StateMachine_strategy)
@settings(max_examples=50)
def test_fsm::statemachine_instantiation(instance):
    assert isinstance(instance, fsm::StateMachine)
