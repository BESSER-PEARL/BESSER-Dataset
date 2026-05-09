import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Behavior,
    StateMachine::CodeBlock,
    StateMachine::Trigger,
    StateMachine::Behavior,
    StateMachine::Region,
    Vertex,
    StateMachine::State,
    State,
    StateMachine::FinalState,
    StateMachine::Transition,
    StateMachine::Vertex,
    StateMachine::PseudoState,
    StateMachine::StateMachine,
    StateMachine::Constraint,
    TransitionKind,
    PseudoStateKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::codeblock_is_not_abstract():
    assert not inspect.isabstract(StateMachine::CodeBlock)


def test_statemachine::codeblock_constructor_exists():
    assert callable(StateMachine::CodeBlock.__init__)


def test_statemachine::codeblock_constructor_args():
    sig = inspect.signature(StateMachine::CodeBlock.__init__)
    params = list(sig.parameters.keys())
    assert "desc" in params, "Missing parameter 'desc'"

def test_statemachine::codeblock_has_desc():
    assert hasattr(StateMachine::CodeBlock, "desc")
    descriptor = None
    for klass in StateMachine::CodeBlock.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::trigger_is_not_abstract():
    assert not inspect.isabstract(StateMachine::Trigger)


def test_statemachine::trigger_constructor_exists():
    assert callable(StateMachine::Trigger.__init__)


def test_statemachine::trigger_constructor_args():
    sig = inspect.signature(StateMachine::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_statemachine::trigger_has_trigger():
    assert hasattr(StateMachine::Trigger, "trigger")
    descriptor = None
    for klass in StateMachine::Trigger.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::behavior_is_not_abstract():
    assert not inspect.isabstract(StateMachine::Behavior)


def test_statemachine::behavior_constructor_exists():
    assert callable(StateMachine::Behavior.__init__)


def test_statemachine::behavior_constructor_args():
    sig = inspect.signature(StateMachine::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::region_is_not_abstract():
    assert not inspect.isabstract(StateMachine::Region)


def test_statemachine::region_constructor_exists():
    assert callable(StateMachine::Region.__init__)


def test_statemachine::region_constructor_args():
    sig = inspect.signature(StateMachine::Region.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::region_has_name():
    assert hasattr(StateMachine::Region, "name")
    descriptor = None
    for klass in StateMachine::Region.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(StateMachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(StateMachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(StateMachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isSubmachineState" in params, "Missing parameter 'isSubmachineState'"
    assert "isSimple" in params, "Missing parameter 'isSimple'"

def test_statemachine::state_has_isComposite():
    assert hasattr(StateMachine::State, "isComposite")
    descriptor = None
    for klass in StateMachine::State.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::state_has_isSubmachineState():
    assert hasattr(StateMachine::State, "isSubmachineState")
    descriptor = None
    for klass in StateMachine::State.__mro__:
        if "isSubmachineState" in klass.__dict__:
            descriptor = klass.__dict__["isSubmachineState"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::state_has_isSimple():
    assert hasattr(StateMachine::State, "isSimple")
    descriptor = None
    for klass in StateMachine::State.__mro__:
        if "isSimple" in klass.__dict__:
            descriptor = klass.__dict__["isSimple"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::finalstate_is_not_abstract():
    assert not inspect.isabstract(StateMachine::FinalState)


def test_statemachine::finalstate_constructor_exists():
    assert callable(StateMachine::FinalState.__init__)


def test_statemachine::finalstate_constructor_args():
    sig = inspect.signature(StateMachine::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(StateMachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(StateMachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(StateMachine::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::transition_has_kind():
    assert hasattr(StateMachine::Transition, "kind")
    descriptor = None
    for klass in StateMachine::Transition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::transition_has_name():
    assert hasattr(StateMachine::Transition, "name")
    descriptor = None
    for klass in StateMachine::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::vertex_is_not_abstract():
    assert not inspect.isabstract(StateMachine::Vertex)


def test_statemachine::vertex_constructor_exists():
    assert callable(StateMachine::Vertex.__init__)


def test_statemachine::vertex_constructor_args():
    sig = inspect.signature(StateMachine::Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::vertex_has_name():
    assert hasattr(StateMachine::Vertex, "name")
    descriptor = None
    for klass in StateMachine::Vertex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::pseudostate_is_not_abstract():
    assert not inspect.isabstract(StateMachine::PseudoState)


def test_statemachine::pseudostate_constructor_exists():
    assert callable(StateMachine::PseudoState.__init__)


def test_statemachine::pseudostate_constructor_args():
    sig = inspect.signature(StateMachine::PseudoState.__init__)
    params = list(sig.parameters.keys())
    assert "pseudoStateKind" in params, "Missing parameter 'pseudoStateKind'"
    assert "returnValue" in params, "Missing parameter 'returnValue'"

def test_statemachine::pseudostate_has_pseudoStateKind():
    assert hasattr(StateMachine::PseudoState, "pseudoStateKind")
    descriptor = None
    for klass in StateMachine::PseudoState.__mro__:
        if "pseudoStateKind" in klass.__dict__:
            descriptor = klass.__dict__["pseudoStateKind"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::pseudostate_has_returnValue():
    assert hasattr(StateMachine::PseudoState, "returnValue")
    descriptor = None
    for klass in StateMachine::PseudoState.__mro__:
        if "returnValue" in klass.__dict__:
            descriptor = klass.__dict__["returnValue"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine::StateMachine)


def test_statemachine::statemachine_constructor_exists():
    assert callable(StateMachine::StateMachine.__init__)


def test_statemachine::statemachine_constructor_args():
    sig = inspect.signature(StateMachine::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::statemachine_has_name():
    assert hasattr(StateMachine::StateMachine, "name")
    descriptor = None
    for klass in StateMachine::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::constraint_is_not_abstract():
    assert not inspect.isabstract(StateMachine::Constraint)


def test_statemachine::constraint_constructor_exists():
    assert callable(StateMachine::Constraint.__init__)


def test_statemachine::constraint_constructor_args():
    sig = inspect.signature(StateMachine::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "constraint" in params, "Missing parameter 'constraint'"

def test_statemachine::constraint_has_constraint():
    assert hasattr(StateMachine::Constraint, "constraint")
    descriptor = None
    for klass in StateMachine::Constraint.__mro__:
        if "constraint" in klass.__dict__:
            descriptor = klass.__dict__["constraint"]
            break
    assert isinstance(descriptor, property)

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
        "exitPoint",
        "shallowHistory",
        "junction",
        "entryPoint",
        "deepHistory",
        "join",
        "fork",
        "choice",
        "terminate",
        "initial",
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
Behavior_strategy = st.builds(
    Behavior,
)
StateMachine::CodeBlock_strategy = st.builds(
    StateMachine::CodeBlock,
    desc=
        safe_text
)
StateMachine::Trigger_strategy = st.builds(
    StateMachine::Trigger,
    trigger=
        safe_text
)
StateMachine::Behavior_strategy = st.builds(
    StateMachine::Behavior,
)
StateMachine::Region_strategy = st.builds(
    StateMachine::Region,
    name=
        safe_text
)
Vertex_strategy = st.builds(
    Vertex,
)
StateMachine::State_strategy = st.builds(
    StateMachine::State,
    isComposite=
        safe_text,
    isSubmachineState=
        safe_text,
    isSimple=
        safe_text
)
State_strategy = st.builds(
    State,
)
StateMachine::FinalState_strategy = st.builds(
    StateMachine::FinalState,
)
StateMachine::Transition_strategy = st.builds(
    StateMachine::Transition,
    kind=
        safe_text,
    name=
        safe_text
)
StateMachine::Vertex_strategy = st.builds(
    StateMachine::Vertex,
    name=
        safe_text
)
StateMachine::PseudoState_strategy = st.builds(
    StateMachine::PseudoState,
    pseudoStateKind=
        safe_text,
    returnValue=
        safe_text
)
StateMachine::StateMachine_strategy = st.builds(
    StateMachine::StateMachine,
    name=
        safe_text
)
StateMachine::Constraint_strategy = st.builds(
    StateMachine::Constraint,
    constraint=
        safe_text
)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=StateMachine::CodeBlock_strategy)
@settings(max_examples=50)
def test_statemachine::codeblock_instantiation(instance):
    assert isinstance(instance, StateMachine::CodeBlock)

@given(instance=StateMachine::CodeBlock_strategy)
def test_statemachine::codeblock_desc_type(instance):
    assert isinstance(instance.desc, str)


@given(instance=StateMachine::CodeBlock_strategy)
def test_statemachine::codeblock_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=StateMachine::Trigger_strategy)
@settings(max_examples=50)
def test_statemachine::trigger_instantiation(instance):
    assert isinstance(instance, StateMachine::Trigger)

@given(instance=StateMachine::Trigger_strategy)
def test_statemachine::trigger_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=StateMachine::Trigger_strategy)
def test_statemachine::trigger_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=StateMachine::Behavior_strategy)
@settings(max_examples=50)
def test_statemachine::behavior_instantiation(instance):
    assert isinstance(instance, StateMachine::Behavior)

@given(instance=StateMachine::Region_strategy)
@settings(max_examples=50)
def test_statemachine::region_instantiation(instance):
    assert isinstance(instance, StateMachine::Region)

@given(instance=StateMachine::Region_strategy)
def test_statemachine::region_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachine::Region_strategy)
def test_statemachine::region_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=StateMachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, StateMachine::State)

@given(instance=StateMachine::State_strategy)
def test_statemachine::state_isComposite_type(instance):
    assert isinstance(instance.isComposite, str)


@given(instance=StateMachine::State_strategy)
def test_statemachine::state_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=StateMachine::State_strategy)
def test_statemachine::state_isSubmachineState_type(instance):
    assert isinstance(instance.isSubmachineState, str)


@given(instance=StateMachine::State_strategy)
def test_statemachine::state_isSubmachineState_setter(instance):
    original = instance.isSubmachineState
    instance.isSubmachineState = original
    assert instance.isSubmachineState == original

@given(instance=StateMachine::State_strategy)
def test_statemachine::state_isSimple_type(instance):
    assert isinstance(instance.isSimple, str)


@given(instance=StateMachine::State_strategy)
def test_statemachine::state_isSimple_setter(instance):
    original = instance.isSimple
    instance.isSimple = original
    assert instance.isSimple == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=StateMachine::FinalState_strategy)
@settings(max_examples=50)
def test_statemachine::finalstate_instantiation(instance):
    assert isinstance(instance, StateMachine::FinalState)

@given(instance=StateMachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, StateMachine::Transition)

@given(instance=StateMachine::Transition_strategy)
def test_statemachine::transition_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=StateMachine::Transition_strategy)
def test_statemachine::transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=StateMachine::Transition_strategy)
def test_statemachine::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachine::Transition_strategy)
def test_statemachine::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachine::Vertex_strategy)
@settings(max_examples=50)
def test_statemachine::vertex_instantiation(instance):
    assert isinstance(instance, StateMachine::Vertex)

@given(instance=StateMachine::Vertex_strategy)
def test_statemachine::vertex_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachine::Vertex_strategy)
def test_statemachine::vertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachine::PseudoState_strategy)
@settings(max_examples=50)
def test_statemachine::pseudostate_instantiation(instance):
    assert isinstance(instance, StateMachine::PseudoState)

@given(instance=StateMachine::PseudoState_strategy)
def test_statemachine::pseudostate_pseudoStateKind_type(instance):
    assert isinstance(instance.pseudoStateKind, str)


@given(instance=StateMachine::PseudoState_strategy)
def test_statemachine::pseudostate_pseudoStateKind_setter(instance):
    original = instance.pseudoStateKind
    instance.pseudoStateKind = original
    assert instance.pseudoStateKind == original

@given(instance=StateMachine::PseudoState_strategy)
def test_statemachine::pseudostate_returnValue_type(instance):
    assert isinstance(instance.returnValue, str)


@given(instance=StateMachine::PseudoState_strategy)
def test_statemachine::pseudostate_returnValue_setter(instance):
    original = instance.returnValue
    instance.returnValue = original
    assert instance.returnValue == original

@given(instance=StateMachine::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine::StateMachine)

@given(instance=StateMachine::StateMachine_strategy)
def test_statemachine::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachine::StateMachine_strategy)
def test_statemachine::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachine::Constraint_strategy)
@settings(max_examples=50)
def test_statemachine::constraint_instantiation(instance):
    assert isinstance(instance, StateMachine::Constraint)

@given(instance=StateMachine::Constraint_strategy)
def test_statemachine::constraint_constraint_type(instance):
    assert isinstance(instance.constraint, str)


@given(instance=StateMachine::Constraint_strategy)
def test_statemachine::constraint_constraint_setter(instance):
    original = instance.constraint
    instance.constraint = original
    assert instance.constraint == original
