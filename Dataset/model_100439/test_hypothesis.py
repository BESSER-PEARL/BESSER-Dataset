import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    StateAction,
    statechart::ENTRY,
    statechart::EXIT,
    statechart::DO,
    NameBase,
    Action,
    statechart::TransitionAction,
    statechart::StateAction,
    State,
    statechart::CompositeState,
    StateVertex,
    statechart::State,
    IDBase,
    statechart::Guard,
    statechart::StateMachine,
    statechart::Label,
    statechart::StateVertex,
    statechart::Event,
    statechart::Transition,
    statechart::Action,
    statechart::StateMachineRoot,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_stateaction_is_not_abstract():
    assert not inspect.isabstract(StateAction)


def test_stateaction_constructor_exists():
    assert callable(StateAction.__init__)


def test_stateaction_constructor_args():
    sig = inspect.signature(StateAction.__init__)
    params = list(sig.parameters.keys())



def test_statechart::entry_is_not_abstract():
    assert not inspect.isabstract(statechart::ENTRY)


def test_statechart::entry_constructor_exists():
    assert callable(statechart::ENTRY.__init__)


def test_statechart::entry_constructor_args():
    sig = inspect.signature(statechart::ENTRY.__init__)
    params = list(sig.parameters.keys())



def test_statechart::exit_is_not_abstract():
    assert not inspect.isabstract(statechart::EXIT)


def test_statechart::exit_constructor_exists():
    assert callable(statechart::EXIT.__init__)


def test_statechart::exit_constructor_args():
    sig = inspect.signature(statechart::EXIT.__init__)
    params = list(sig.parameters.keys())



def test_statechart::do_is_not_abstract():
    assert not inspect.isabstract(statechart::DO)


def test_statechart::do_constructor_exists():
    assert callable(statechart::DO.__init__)


def test_statechart::do_constructor_args():
    sig = inspect.signature(statechart::DO.__init__)
    params = list(sig.parameters.keys())



def test_namebase_is_not_abstract():
    assert not inspect.isabstract(NameBase)


def test_namebase_constructor_exists():
    assert callable(NameBase.__init__)


def test_namebase_constructor_args():
    sig = inspect.signature(NameBase.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_statechart::transitionaction_is_not_abstract():
    assert not inspect.isabstract(statechart::TransitionAction)


def test_statechart::transitionaction_constructor_exists():
    assert callable(statechart::TransitionAction.__init__)


def test_statechart::transitionaction_constructor_args():
    sig = inspect.signature(statechart::TransitionAction.__init__)
    params = list(sig.parameters.keys())



def test_statechart::stateaction_is_not_abstract():
    assert not inspect.isabstract(statechart::StateAction)


def test_statechart::stateaction_constructor_exists():
    assert callable(statechart::StateAction.__init__)


def test_statechart::stateaction_constructor_args():
    sig = inspect.signature(statechart::StateAction.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statechart::compositestate_is_not_abstract():
    assert not inspect.isabstract(statechart::CompositeState)


def test_statechart::compositestate_constructor_exists():
    assert callable(statechart::CompositeState.__init__)


def test_statechart::compositestate_constructor_args():
    sig = inspect.signature(statechart::CompositeState.__init__)
    params = list(sig.parameters.keys())
    assert "isConcurrent" in params, "Missing parameter 'isConcurrent'"

def test_statechart::compositestate_has_isConcurrent():
    assert hasattr(statechart::CompositeState, "isConcurrent")
    descriptor = None
    for klass in statechart::CompositeState.__mro__:
        if "isConcurrent" in klass.__dict__:
            descriptor = klass.__dict__["isConcurrent"]
            break
    assert isinstance(descriptor, property)



def test_statevertex_is_not_abstract():
    assert not inspect.isabstract(StateVertex)


def test_statevertex_constructor_exists():
    assert callable(StateVertex.__init__)


def test_statevertex_constructor_args():
    sig = inspect.signature(StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_statechart::state_is_not_abstract():
    assert not inspect.isabstract(statechart::State)


def test_statechart::state_constructor_exists():
    assert callable(statechart::State.__init__)


def test_statechart::state_constructor_args():
    sig = inspect.signature(statechart::State.__init__)
    params = list(sig.parameters.keys())



def test_idbase_is_not_abstract():
    assert not inspect.isabstract(IDBase)


def test_idbase_constructor_exists():
    assert callable(IDBase.__init__)


def test_idbase_constructor_args():
    sig = inspect.signature(IDBase.__init__)
    params = list(sig.parameters.keys())



def test_statechart::guard_is_not_abstract():
    assert not inspect.isabstract(statechart::Guard)


def test_statechart::guard_constructor_exists():
    assert callable(statechart::Guard.__init__)


def test_statechart::guard_constructor_args():
    sig = inspect.signature(statechart::Guard.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_statechart::guard_has_expression():
    assert hasattr(statechart::Guard, "expression")
    descriptor = None
    for klass in statechart::Guard.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_statechart::statemachine_is_not_abstract():
    assert not inspect.isabstract(statechart::StateMachine)


def test_statechart::statemachine_constructor_exists():
    assert callable(statechart::StateMachine.__init__)


def test_statechart::statemachine_constructor_args():
    sig = inspect.signature(statechart::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statechart::statemachine_has_name():
    assert hasattr(statechart::StateMachine, "name")
    descriptor = None
    for klass in statechart::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statechart::label_is_not_abstract():
    assert not inspect.isabstract(statechart::Label)


def test_statechart::label_constructor_exists():
    assert callable(statechart::Label.__init__)


def test_statechart::label_constructor_args():
    sig = inspect.signature(statechart::Label.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statechart::label_has_name():
    assert hasattr(statechart::Label, "name")
    descriptor = None
    for klass in statechart::Label.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statechart::statevertex_is_not_abstract():
    assert not inspect.isabstract(statechart::StateVertex)


def test_statechart::statevertex_constructor_exists():
    assert callable(statechart::StateVertex.__init__)


def test_statechart::statevertex_constructor_args():
    sig = inspect.signature(statechart::StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_statechart::event_is_not_abstract():
    assert not inspect.isabstract(statechart::Event)


def test_statechart::event_constructor_exists():
    assert callable(statechart::Event.__init__)


def test_statechart::event_constructor_args():
    sig = inspect.signature(statechart::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statechart::event_has_name():
    assert hasattr(statechart::Event, "name")
    descriptor = None
    for klass in statechart::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statechart::transition_is_not_abstract():
    assert not inspect.isabstract(statechart::Transition)


def test_statechart::transition_constructor_exists():
    assert callable(statechart::Transition.__init__)


def test_statechart::transition_constructor_args():
    sig = inspect.signature(statechart::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_statechart::transition_has_description():
    assert hasattr(statechart::Transition, "description")
    descriptor = None
    for klass in statechart::Transition.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_statechart::action_is_not_abstract():
    assert not inspect.isabstract(statechart::Action)


def test_statechart::action_constructor_exists():
    assert callable(statechart::Action.__init__)


def test_statechart::action_constructor_args():
    sig = inspect.signature(statechart::Action.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statechart::action_has_value():
    assert hasattr(statechart::Action, "value")
    descriptor = None
    for klass in statechart::Action.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statechart::statemachineroot_is_not_abstract():
    assert not inspect.isabstract(statechart::StateMachineRoot)


def test_statechart::statemachineroot_constructor_exists():
    assert callable(statechart::StateMachineRoot.__init__)


def test_statechart::statemachineroot_constructor_args():
    sig = inspect.signature(statechart::StateMachineRoot.__init__)
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
StateAction_strategy = st.builds(
    StateAction,
)
statechart::ENTRY_strategy = st.builds(
    statechart::ENTRY,
)
statechart::EXIT_strategy = st.builds(
    statechart::EXIT,
)
statechart::DO_strategy = st.builds(
    statechart::DO,
)
NameBase_strategy = st.builds(
    NameBase,
)
Action_strategy = st.builds(
    Action,
)
statechart::TransitionAction_strategy = st.builds(
    statechart::TransitionAction,
)
statechart::StateAction_strategy = st.builds(
    statechart::StateAction,
)
State_strategy = st.builds(
    State,
)
statechart::CompositeState_strategy = st.builds(
    statechart::CompositeState,
    isConcurrent=
        st.booleans()
)
StateVertex_strategy = st.builds(
    StateVertex,
)
statechart::State_strategy = st.builds(
    statechart::State,
)
IDBase_strategy = st.builds(
    IDBase,
)
statechart::Guard_strategy = st.builds(
    statechart::Guard,
    expression=
        safe_text
)
statechart::StateMachine_strategy = st.builds(
    statechart::StateMachine,
    name=
        safe_text
)
statechart::Label_strategy = st.builds(
    statechart::Label,
    name=
        safe_text
)
statechart::StateVertex_strategy = st.builds(
    statechart::StateVertex,
)
statechart::Event_strategy = st.builds(
    statechart::Event,
    name=
        safe_text
)
statechart::Transition_strategy = st.builds(
    statechart::Transition,
    description=
        safe_text
)
statechart::Action_strategy = st.builds(
    statechart::Action,
    value=
        safe_text
)
statechart::StateMachineRoot_strategy = st.builds(
    statechart::StateMachineRoot,
)

@given(instance=StateAction_strategy)
@settings(max_examples=50)
def test_stateaction_instantiation(instance):
    assert isinstance(instance, StateAction)

@given(instance=statechart::ENTRY_strategy)
@settings(max_examples=50)
def test_statechart::entry_instantiation(instance):
    assert isinstance(instance, statechart::ENTRY)

@given(instance=statechart::EXIT_strategy)
@settings(max_examples=50)
def test_statechart::exit_instantiation(instance):
    assert isinstance(instance, statechart::EXIT)

@given(instance=statechart::DO_strategy)
@settings(max_examples=50)
def test_statechart::do_instantiation(instance):
    assert isinstance(instance, statechart::DO)

@given(instance=NameBase_strategy)
@settings(max_examples=50)
def test_namebase_instantiation(instance):
    assert isinstance(instance, NameBase)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=statechart::TransitionAction_strategy)
@settings(max_examples=50)
def test_statechart::transitionaction_instantiation(instance):
    assert isinstance(instance, statechart::TransitionAction)

@given(instance=statechart::StateAction_strategy)
@settings(max_examples=50)
def test_statechart::stateaction_instantiation(instance):
    assert isinstance(instance, statechart::StateAction)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statechart::CompositeState_strategy)
@settings(max_examples=50)
def test_statechart::compositestate_instantiation(instance):
    assert isinstance(instance, statechart::CompositeState)

@given(instance=statechart::CompositeState_strategy)
def test_statechart::compositestate_isConcurrent_type(instance):
    assert isinstance(instance.isConcurrent, bool)


@given(instance=statechart::CompositeState_strategy)
def test_statechart::compositestate_isConcurrent_setter(instance):
    original = instance.isConcurrent
    instance.isConcurrent = original
    assert instance.isConcurrent == original

@given(instance=StateVertex_strategy)
@settings(max_examples=50)
def test_statevertex_instantiation(instance):
    assert isinstance(instance, StateVertex)

@given(instance=statechart::State_strategy)
@settings(max_examples=50)
def test_statechart::state_instantiation(instance):
    assert isinstance(instance, statechart::State)

@given(instance=IDBase_strategy)
@settings(max_examples=50)
def test_idbase_instantiation(instance):
    assert isinstance(instance, IDBase)

@given(instance=statechart::Guard_strategy)
@settings(max_examples=50)
def test_statechart::guard_instantiation(instance):
    assert isinstance(instance, statechart::Guard)

@given(instance=statechart::Guard_strategy)
def test_statechart::guard_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=statechart::Guard_strategy)
def test_statechart::guard_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=statechart::StateMachine_strategy)
@settings(max_examples=50)
def test_statechart::statemachine_instantiation(instance):
    assert isinstance(instance, statechart::StateMachine)

@given(instance=statechart::StateMachine_strategy)
def test_statechart::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statechart::StateMachine_strategy)
def test_statechart::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statechart::Label_strategy)
@settings(max_examples=50)
def test_statechart::label_instantiation(instance):
    assert isinstance(instance, statechart::Label)

@given(instance=statechart::Label_strategy)
def test_statechart::label_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statechart::Label_strategy)
def test_statechart::label_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statechart::StateVertex_strategy)
@settings(max_examples=50)
def test_statechart::statevertex_instantiation(instance):
    assert isinstance(instance, statechart::StateVertex)

@given(instance=statechart::Event_strategy)
@settings(max_examples=50)
def test_statechart::event_instantiation(instance):
    assert isinstance(instance, statechart::Event)

@given(instance=statechart::Event_strategy)
def test_statechart::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statechart::Event_strategy)
def test_statechart::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statechart::Transition_strategy)
@settings(max_examples=50)
def test_statechart::transition_instantiation(instance):
    assert isinstance(instance, statechart::Transition)

@given(instance=statechart::Transition_strategy)
def test_statechart::transition_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=statechart::Transition_strategy)
def test_statechart::transition_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=statechart::Action_strategy)
@settings(max_examples=50)
def test_statechart::action_instantiation(instance):
    assert isinstance(instance, statechart::Action)

@given(instance=statechart::Action_strategy)
def test_statechart::action_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=statechart::Action_strategy)
def test_statechart::action_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=statechart::StateMachineRoot_strategy)
@settings(max_examples=50)
def test_statechart::statemachineroot_instantiation(instance):
    assert isinstance(instance, statechart::StateMachineRoot)
