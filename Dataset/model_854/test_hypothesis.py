import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsm::Region,
    Pseudostate,
    fsm::Choice,
    fsm::Join,
    fsm::Fork,
    fsm::Trigger,
    State,
    fsm::Pseudostate,
    fsm::InitialState,
    fsm::FinalState,
    fsm::CompositeState,
    fsm::Variable,
    Transition,
    fsm::TimedTransition,
    fsm::Action,
    fsm::Guard,
    NamedElement,
    fsm::Transition,
    fsm::State,
    fsm::StateMachine,
    fsm::NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::region_is_not_abstract():
    assert not inspect.isabstract(fsm::Region)


def test_fsm::region_constructor_exists():
    assert callable(fsm::Region.__init__)


def test_fsm::region_constructor_args():
    sig = inspect.signature(fsm::Region.__init__)
    params = list(sig.parameters.keys())



def test_pseudostate_is_not_abstract():
    assert not inspect.isabstract(Pseudostate)


def test_pseudostate_constructor_exists():
    assert callable(Pseudostate.__init__)


def test_pseudostate_constructor_args():
    sig = inspect.signature(Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_fsm::choice_is_not_abstract():
    assert not inspect.isabstract(fsm::Choice)


def test_fsm::choice_constructor_exists():
    assert callable(fsm::Choice.__init__)


def test_fsm::choice_constructor_args():
    sig = inspect.signature(fsm::Choice.__init__)
    params = list(sig.parameters.keys())



def test_fsm::join_is_not_abstract():
    assert not inspect.isabstract(fsm::Join)


def test_fsm::join_constructor_exists():
    assert callable(fsm::Join.__init__)


def test_fsm::join_constructor_args():
    sig = inspect.signature(fsm::Join.__init__)
    params = list(sig.parameters.keys())



def test_fsm::fork_is_not_abstract():
    assert not inspect.isabstract(fsm::Fork)


def test_fsm::fork_constructor_exists():
    assert callable(fsm::Fork.__init__)


def test_fsm::fork_constructor_args():
    sig = inspect.signature(fsm::Fork.__init__)
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



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_fsm::pseudostate_is_not_abstract():
    assert not inspect.isabstract(fsm::Pseudostate)


def test_fsm::pseudostate_constructor_exists():
    assert callable(fsm::Pseudostate.__init__)


def test_fsm::pseudostate_constructor_args():
    sig = inspect.signature(fsm::Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_fsm::initialstate_is_not_abstract():
    assert not inspect.isabstract(fsm::InitialState)


def test_fsm::initialstate_constructor_exists():
    assert callable(fsm::InitialState.__init__)


def test_fsm::initialstate_constructor_args():
    sig = inspect.signature(fsm::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::finalstate_is_not_abstract():
    assert not inspect.isabstract(fsm::FinalState)


def test_fsm::finalstate_constructor_exists():
    assert callable(fsm::FinalState.__init__)


def test_fsm::finalstate_constructor_args():
    sig = inspect.signature(fsm::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::compositestate_is_not_abstract():
    assert not inspect.isabstract(fsm::CompositeState)


def test_fsm::compositestate_constructor_exists():
    assert callable(fsm::CompositeState.__init__)


def test_fsm::compositestate_constructor_args():
    sig = inspect.signature(fsm::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::variable_is_not_abstract():
    assert not inspect.isabstract(fsm::Variable)


def test_fsm::variable_constructor_exists():
    assert callable(fsm::Variable.__init__)


def test_fsm::variable_constructor_args():
    sig = inspect.signature(fsm::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fsm::variable_has_name():
    assert hasattr(fsm::Variable, "name")
    descriptor = None
    for klass in fsm::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fsm::variable_has_value():
    assert hasattr(fsm::Variable, "value")
    descriptor = None
    for klass in fsm::Variable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsm::timedtransition_is_not_abstract():
    assert not inspect.isabstract(fsm::TimedTransition)


def test_fsm::timedtransition_constructor_exists():
    assert callable(fsm::TimedTransition.__init__)


def test_fsm::timedtransition_constructor_args():
    sig = inspect.signature(fsm::TimedTransition.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"

def test_fsm::timedtransition_has_duration():
    assert hasattr(fsm::TimedTransition, "duration")
    descriptor = None
    for klass in fsm::TimedTransition.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_fsm::action_is_not_abstract():
    assert not inspect.isabstract(fsm::Action)


def test_fsm::action_constructor_exists():
    assert callable(fsm::Action.__init__)


def test_fsm::action_constructor_args():
    sig = inspect.signature(fsm::Action.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"
    assert "value" in params, "Missing parameter 'value'"

def test_fsm::action_has_variable():
    assert hasattr(fsm::Action, "variable")
    descriptor = None
    for klass in fsm::Action.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)

def test_fsm::action_has_value():
    assert hasattr(fsm::Action, "value")
    descriptor = None
    for klass in fsm::Action.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fsm::guard_is_not_abstract():
    assert not inspect.isabstract(fsm::Guard)


def test_fsm::guard_constructor_exists():
    assert callable(fsm::Guard.__init__)


def test_fsm::guard_constructor_args():
    sig = inspect.signature(fsm::Guard.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_fsm::guard_has_expression():
    assert hasattr(fsm::Guard, "expression")
    descriptor = None
    for klass in fsm::Guard.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



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
    assert "initialTime" in params, "Missing parameter 'initialTime'"
    assert "finalTime" in params, "Missing parameter 'finalTime'"

def test_fsm::transition_has_initialTime():
    assert hasattr(fsm::Transition, "initialTime")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "initialTime" in klass.__dict__:
            descriptor = klass.__dict__["initialTime"]
            break
    assert isinstance(descriptor, property)

def test_fsm::transition_has_finalTime():
    assert hasattr(fsm::Transition, "finalTime")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "finalTime" in klass.__dict__:
            descriptor = klass.__dict__["finalTime"]
            break
    assert isinstance(descriptor, property)



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(fsm::State)


def test_fsm::state_constructor_exists():
    assert callable(fsm::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(fsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "initialTime" in params, "Missing parameter 'initialTime'"
    assert "finalTime" in params, "Missing parameter 'finalTime'"

def test_fsm::state_has_initialTime():
    assert hasattr(fsm::State, "initialTime")
    descriptor = None
    for klass in fsm::State.__mro__:
        if "initialTime" in klass.__dict__:
            descriptor = klass.__dict__["initialTime"]
            break
    assert isinstance(descriptor, property)

def test_fsm::state_has_finalTime():
    assert hasattr(fsm::State, "finalTime")
    descriptor = None
    for klass in fsm::State.__mro__:
        if "finalTime" in klass.__dict__:
            descriptor = klass.__dict__["finalTime"]
            break
    assert isinstance(descriptor, property)



def test_fsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(fsm::StateMachine)


def test_fsm::statemachine_constructor_exists():
    assert callable(fsm::StateMachine.__init__)


def test_fsm::statemachine_constructor_args():
    sig = inspect.signature(fsm::StateMachine.__init__)
    params = list(sig.parameters.keys())



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
fsm::Region_strategy = st.builds(
    fsm::Region,
)
Pseudostate_strategy = st.builds(
    Pseudostate,
)
fsm::Choice_strategy = st.builds(
    fsm::Choice,
)
fsm::Join_strategy = st.builds(
    fsm::Join,
)
fsm::Fork_strategy = st.builds(
    fsm::Fork,
)
fsm::Trigger_strategy = st.builds(
    fsm::Trigger,
    expression=
        safe_text
)
State_strategy = st.builds(
    State,
)
fsm::Pseudostate_strategy = st.builds(
    fsm::Pseudostate,
)
fsm::InitialState_strategy = st.builds(
    fsm::InitialState,
)
fsm::FinalState_strategy = st.builds(
    fsm::FinalState,
)
fsm::CompositeState_strategy = st.builds(
    fsm::CompositeState,
)
fsm::Variable_strategy = st.builds(
    fsm::Variable,
    name=
        safe_text,
    value=
        st.booleans()
)
Transition_strategy = st.builds(
    Transition,
)
fsm::TimedTransition_strategy = st.builds(
    fsm::TimedTransition,
    duration=
        st.integers()
)
fsm::Action_strategy = st.builds(
    fsm::Action,
    variable=
        safe_text,
    value=
        st.booleans()
)
fsm::Guard_strategy = st.builds(
    fsm::Guard,
    expression=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
fsm::Transition_strategy = st.builds(
    fsm::Transition,
    initialTime=
        st.integers(),
    finalTime=
        st.integers()
)
fsm::State_strategy = st.builds(
    fsm::State,
    initialTime=
        st.integers(),
    finalTime=
        st.integers()
)
fsm::StateMachine_strategy = st.builds(
    fsm::StateMachine,
)
fsm::NamedElement_strategy = st.builds(
    fsm::NamedElement,
    name=
        safe_text
)

@given(instance=fsm::Region_strategy)
@settings(max_examples=50)
def test_fsm::region_instantiation(instance):
    assert isinstance(instance, fsm::Region)

@given(instance=Pseudostate_strategy)
@settings(max_examples=50)
def test_pseudostate_instantiation(instance):
    assert isinstance(instance, Pseudostate)

@given(instance=fsm::Choice_strategy)
@settings(max_examples=50)
def test_fsm::choice_instantiation(instance):
    assert isinstance(instance, fsm::Choice)

@given(instance=fsm::Join_strategy)
@settings(max_examples=50)
def test_fsm::join_instantiation(instance):
    assert isinstance(instance, fsm::Join)

@given(instance=fsm::Fork_strategy)
@settings(max_examples=50)
def test_fsm::fork_instantiation(instance):
    assert isinstance(instance, fsm::Fork)

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

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=fsm::Pseudostate_strategy)
@settings(max_examples=50)
def test_fsm::pseudostate_instantiation(instance):
    assert isinstance(instance, fsm::Pseudostate)

@given(instance=fsm::InitialState_strategy)
@settings(max_examples=50)
def test_fsm::initialstate_instantiation(instance):
    assert isinstance(instance, fsm::InitialState)

@given(instance=fsm::FinalState_strategy)
@settings(max_examples=50)
def test_fsm::finalstate_instantiation(instance):
    assert isinstance(instance, fsm::FinalState)

@given(instance=fsm::CompositeState_strategy)
@settings(max_examples=50)
def test_fsm::compositestate_instantiation(instance):
    assert isinstance(instance, fsm::CompositeState)

@given(instance=fsm::Variable_strategy)
@settings(max_examples=50)
def test_fsm::variable_instantiation(instance):
    assert isinstance(instance, fsm::Variable)

@given(instance=fsm::Variable_strategy)
def test_fsm::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::Variable_strategy)
def test_fsm::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::Variable_strategy)
def test_fsm::variable_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fsm::Variable_strategy)
def test_fsm::variable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=fsm::TimedTransition_strategy)
@settings(max_examples=50)
def test_fsm::timedtransition_instantiation(instance):
    assert isinstance(instance, fsm::TimedTransition)

@given(instance=fsm::TimedTransition_strategy)
def test_fsm::timedtransition_duration_type(instance):
    assert isinstance(instance.duration, int)


@given(instance=fsm::TimedTransition_strategy)
def test_fsm::timedtransition_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=fsm::Action_strategy)
@settings(max_examples=50)
def test_fsm::action_instantiation(instance):
    assert isinstance(instance, fsm::Action)

@given(instance=fsm::Action_strategy)
def test_fsm::action_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=fsm::Action_strategy)
def test_fsm::action_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=fsm::Action_strategy)
def test_fsm::action_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fsm::Action_strategy)
def test_fsm::action_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fsm::Guard_strategy)
@settings(max_examples=50)
def test_fsm::guard_instantiation(instance):
    assert isinstance(instance, fsm::Guard)

@given(instance=fsm::Guard_strategy)
def test_fsm::guard_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=fsm::Guard_strategy)
def test_fsm::guard_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=fsm::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, fsm::Transition)

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_initialTime_type(instance):
    assert isinstance(instance.initialTime, int)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_initialTime_setter(instance):
    original = instance.initialTime
    instance.initialTime = original
    assert instance.initialTime == original

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_finalTime_type(instance):
    assert isinstance(instance.finalTime, int)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_finalTime_setter(instance):
    original = instance.finalTime
    instance.finalTime = original
    assert instance.finalTime == original

@given(instance=fsm::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, fsm::State)

@given(instance=fsm::State_strategy)
def test_fsm::state_initialTime_type(instance):
    assert isinstance(instance.initialTime, int)


@given(instance=fsm::State_strategy)
def test_fsm::state_initialTime_setter(instance):
    original = instance.initialTime
    instance.initialTime = original
    assert instance.initialTime == original

@given(instance=fsm::State_strategy)
def test_fsm::state_finalTime_type(instance):
    assert isinstance(instance.finalTime, int)


@given(instance=fsm::State_strategy)
def test_fsm::state_finalTime_setter(instance):
    original = instance.finalTime
    instance.finalTime = original
    assert instance.finalTime == original

@given(instance=fsm::StateMachine_strategy)
@settings(max_examples=50)
def test_fsm::statemachine_instantiation(instance):
    assert isinstance(instance, fsm::StateMachine)

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
