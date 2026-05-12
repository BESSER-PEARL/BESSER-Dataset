import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NameBase,
    Action,
    StateAction,
    statechart_ENTRY,
    statechart_EXIT,
    statechart_DO,
    State,
    statechart_CompositeState,
    statechart_StateAction,
    statechart_TransitionAction,
    StateVertex,
    statechart_State,
    IDBase,
    statechart_Event,
    statechart_Label,
    statechart_Transition,
    statechart_StateVertex,
    statechart_Action,
    statechart_Guard,
    statechart_StateMachine,
    statechart_StateMachineRoot,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_stateaction_is_not_abstract():
    assert not inspect.isabstract(StateAction)


def test_stateaction_constructor_exists():
    assert callable(StateAction.__init__)


def test_stateaction_constructor_args():
    sig = inspect.signature(StateAction.__init__)
    params = list(sig.parameters.keys())



def test_statechart_entry_is_not_abstract():
    assert not inspect.isabstract(statechart_ENTRY)


def test_statechart_entry_constructor_exists():
    assert callable(statechart_ENTRY.__init__)


def test_statechart_entry_constructor_args():
    sig = inspect.signature(statechart_ENTRY.__init__)
    params = list(sig.parameters.keys())



def test_statechart_exit_is_not_abstract():
    assert not inspect.isabstract(statechart_EXIT)


def test_statechart_exit_constructor_exists():
    assert callable(statechart_EXIT.__init__)


def test_statechart_exit_constructor_args():
    sig = inspect.signature(statechart_EXIT.__init__)
    params = list(sig.parameters.keys())



def test_statechart_do_is_not_abstract():
    assert not inspect.isabstract(statechart_DO)


def test_statechart_do_constructor_exists():
    assert callable(statechart_DO.__init__)


def test_statechart_do_constructor_args():
    sig = inspect.signature(statechart_DO.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statechart_compositestate_is_not_abstract():
    assert not inspect.isabstract(statechart_CompositeState)


def test_statechart_compositestate_constructor_exists():
    assert callable(statechart_CompositeState.__init__)


def test_statechart_compositestate_constructor_args():
    sig = inspect.signature(statechart_CompositeState.__init__)
    params = list(sig.parameters.keys())
    assert "isConcurrent" in params, "Missing parameter 'isConcurrent'"

def test_statechart_compositestate_has_isConcurrent():
    assert hasattr(statechart_CompositeState, "isConcurrent")
    descriptor = None
    for klass in statechart_CompositeState.__mro__:
        if "isConcurrent" in klass.__dict__:
            descriptor = klass.__dict__["isConcurrent"]
            break
    assert isinstance(descriptor, property)



def test_statechart_stateaction_is_not_abstract():
    assert not inspect.isabstract(statechart_StateAction)


def test_statechart_stateaction_constructor_exists():
    assert callable(statechart_StateAction.__init__)


def test_statechart_stateaction_constructor_args():
    sig = inspect.signature(statechart_StateAction.__init__)
    params = list(sig.parameters.keys())



def test_statechart_transitionaction_is_not_abstract():
    assert not inspect.isabstract(statechart_TransitionAction)


def test_statechart_transitionaction_constructor_exists():
    assert callable(statechart_TransitionAction.__init__)


def test_statechart_transitionaction_constructor_args():
    sig = inspect.signature(statechart_TransitionAction.__init__)
    params = list(sig.parameters.keys())



def test_statevertex_is_not_abstract():
    assert not inspect.isabstract(StateVertex)


def test_statevertex_constructor_exists():
    assert callable(StateVertex.__init__)


def test_statevertex_constructor_args():
    sig = inspect.signature(StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_statechart_state_is_not_abstract():
    assert not inspect.isabstract(statechart_State)


def test_statechart_state_constructor_exists():
    assert callable(statechart_State.__init__)


def test_statechart_state_constructor_args():
    sig = inspect.signature(statechart_State.__init__)
    params = list(sig.parameters.keys())



def test_idbase_is_not_abstract():
    assert not inspect.isabstract(IDBase)


def test_idbase_constructor_exists():
    assert callable(IDBase.__init__)


def test_idbase_constructor_args():
    sig = inspect.signature(IDBase.__init__)
    params = list(sig.parameters.keys())



def test_statechart_event_is_not_abstract():
    assert not inspect.isabstract(statechart_Event)


def test_statechart_event_constructor_exists():
    assert callable(statechart_Event.__init__)


def test_statechart_event_constructor_args():
    sig = inspect.signature(statechart_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statechart_event_has_name():
    assert hasattr(statechart_Event, "name")
    descriptor = None
    for klass in statechart_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statechart_label_is_not_abstract():
    assert not inspect.isabstract(statechart_Label)


def test_statechart_label_constructor_exists():
    assert callable(statechart_Label.__init__)


def test_statechart_label_constructor_args():
    sig = inspect.signature(statechart_Label.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statechart_label_has_name():
    assert hasattr(statechart_Label, "name")
    descriptor = None
    for klass in statechart_Label.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statechart_transition_is_not_abstract():
    assert not inspect.isabstract(statechart_Transition)


def test_statechart_transition_constructor_exists():
    assert callable(statechart_Transition.__init__)


def test_statechart_transition_constructor_args():
    sig = inspect.signature(statechart_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_statechart_transition_has_description():
    assert hasattr(statechart_Transition, "description")
    descriptor = None
    for klass in statechart_Transition.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_statechart_statevertex_is_not_abstract():
    assert not inspect.isabstract(statechart_StateVertex)


def test_statechart_statevertex_constructor_exists():
    assert callable(statechart_StateVertex.__init__)


def test_statechart_statevertex_constructor_args():
    sig = inspect.signature(statechart_StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_statechart_action_is_not_abstract():
    assert not inspect.isabstract(statechart_Action)


def test_statechart_action_constructor_exists():
    assert callable(statechart_Action.__init__)


def test_statechart_action_constructor_args():
    sig = inspect.signature(statechart_Action.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statechart_action_has_value():
    assert hasattr(statechart_Action, "value")
    descriptor = None
    for klass in statechart_Action.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statechart_guard_is_not_abstract():
    assert not inspect.isabstract(statechart_Guard)


def test_statechart_guard_constructor_exists():
    assert callable(statechart_Guard.__init__)


def test_statechart_guard_constructor_args():
    sig = inspect.signature(statechart_Guard.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_statechart_guard_has_expression():
    assert hasattr(statechart_Guard, "expression")
    descriptor = None
    for klass in statechart_Guard.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_statechart_statemachine_is_not_abstract():
    assert not inspect.isabstract(statechart_StateMachine)


def test_statechart_statemachine_constructor_exists():
    assert callable(statechart_StateMachine.__init__)


def test_statechart_statemachine_constructor_args():
    sig = inspect.signature(statechart_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statechart_statemachine_has_name():
    assert hasattr(statechart_StateMachine, "name")
    descriptor = None
    for klass in statechart_StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statechart_statemachineroot_is_not_abstract():
    assert not inspect.isabstract(statechart_StateMachineRoot)


def test_statechart_statemachineroot_constructor_exists():
    assert callable(statechart_StateMachineRoot.__init__)


def test_statechart_statemachineroot_constructor_args():
    sig = inspect.signature(statechart_StateMachineRoot.__init__)
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
NameBase_strategy = st.builds(
    NameBase,
)
Action_strategy = st.builds(
    Action,
)
StateAction_strategy = st.builds(
    StateAction,
)
statechart_ENTRY_strategy = st.builds(
    statechart_ENTRY,
)
statechart_EXIT_strategy = st.builds(
    statechart_EXIT,
)
statechart_DO_strategy = st.builds(
    statechart_DO,
)
State_strategy = st.builds(
    State,
)
statechart_CompositeState_strategy = st.builds(
    statechart_CompositeState,
    isConcurrent=
        st.booleans()
)
statechart_StateAction_strategy = st.builds(
    statechart_StateAction,
)
statechart_TransitionAction_strategy = st.builds(
    statechart_TransitionAction,
)
StateVertex_strategy = st.builds(
    StateVertex,
)
statechart_State_strategy = st.builds(
    statechart_State,
)
IDBase_strategy = st.builds(
    IDBase,
)
statechart_Event_strategy = st.builds(
    statechart_Event,
    name=
        safe_text
)
statechart_Label_strategy = st.builds(
    statechart_Label,
    name=
        safe_text
)
statechart_Transition_strategy = st.builds(
    statechart_Transition,
    description=
        safe_text
)
statechart_StateVertex_strategy = st.builds(
    statechart_StateVertex,
)
statechart_Action_strategy = st.builds(
    statechart_Action,
    value=
        safe_text
)
statechart_Guard_strategy = st.builds(
    statechart_Guard,
    expression=
        safe_text
)
statechart_StateMachine_strategy = st.builds(
    statechart_StateMachine,
    name=
        safe_text
)
statechart_StateMachineRoot_strategy = st.builds(
    statechart_StateMachineRoot,
)

@given(instance=NameBase_strategy)
@settings(max_examples=50)
def test_namebase_instantiation(instance):
    assert isinstance(instance, NameBase)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=StateAction_strategy)
@settings(max_examples=50)
def test_stateaction_instantiation(instance):
    assert isinstance(instance, StateAction)

@given(instance=statechart_ENTRY_strategy)
@settings(max_examples=50)
def test_statechart_entry_instantiation(instance):
    assert isinstance(instance, statechart_ENTRY)

@given(instance=statechart_EXIT_strategy)
@settings(max_examples=50)
def test_statechart_exit_instantiation(instance):
    assert isinstance(instance, statechart_EXIT)

@given(instance=statechart_DO_strategy)
@settings(max_examples=50)
def test_statechart_do_instantiation(instance):
    assert isinstance(instance, statechart_DO)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statechart_CompositeState_strategy)
@settings(max_examples=50)
def test_statechart_compositestate_instantiation(instance):
    assert isinstance(instance, statechart_CompositeState)



@given(instance=statechart_CompositeState_strategy)
def test_statechart_compositestate_isConcurrent_setter(instance):
    original = instance.isConcurrent
    instance.isConcurrent = original
    assert instance.isConcurrent == original

@given(instance=statechart_StateAction_strategy)
@settings(max_examples=50)
def test_statechart_stateaction_instantiation(instance):
    assert isinstance(instance, statechart_StateAction)

@given(instance=statechart_TransitionAction_strategy)
@settings(max_examples=50)
def test_statechart_transitionaction_instantiation(instance):
    assert isinstance(instance, statechart_TransitionAction)

@given(instance=StateVertex_strategy)
@settings(max_examples=50)
def test_statevertex_instantiation(instance):
    assert isinstance(instance, StateVertex)

@given(instance=statechart_State_strategy)
@settings(max_examples=50)
def test_statechart_state_instantiation(instance):
    assert isinstance(instance, statechart_State)

@given(instance=IDBase_strategy)
@settings(max_examples=50)
def test_idbase_instantiation(instance):
    assert isinstance(instance, IDBase)

@given(instance=statechart_Event_strategy)
@settings(max_examples=50)
def test_statechart_event_instantiation(instance):
    assert isinstance(instance, statechart_Event)



@given(instance=statechart_Event_strategy)
def test_statechart_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statechart_Label_strategy)
@settings(max_examples=50)
def test_statechart_label_instantiation(instance):
    assert isinstance(instance, statechart_Label)



@given(instance=statechart_Label_strategy)
def test_statechart_label_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statechart_Transition_strategy)
@settings(max_examples=50)
def test_statechart_transition_instantiation(instance):
    assert isinstance(instance, statechart_Transition)



@given(instance=statechart_Transition_strategy)
def test_statechart_transition_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=statechart_StateVertex_strategy)
@settings(max_examples=50)
def test_statechart_statevertex_instantiation(instance):
    assert isinstance(instance, statechart_StateVertex)

@given(instance=statechart_Action_strategy)
@settings(max_examples=50)
def test_statechart_action_instantiation(instance):
    assert isinstance(instance, statechart_Action)



@given(instance=statechart_Action_strategy)
def test_statechart_action_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=statechart_Guard_strategy)
@settings(max_examples=50)
def test_statechart_guard_instantiation(instance):
    assert isinstance(instance, statechart_Guard)



@given(instance=statechart_Guard_strategy)
def test_statechart_guard_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=statechart_StateMachine_strategy)
@settings(max_examples=50)
def test_statechart_statemachine_instantiation(instance):
    assert isinstance(instance, statechart_StateMachine)



@given(instance=statechart_StateMachine_strategy)
def test_statechart_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statechart_StateMachineRoot_strategy)
@settings(max_examples=50)
def test_statechart_statemachineroot_instantiation(instance):
    assert isinstance(instance, statechart_StateMachineRoot)
