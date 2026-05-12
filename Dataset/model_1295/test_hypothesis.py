import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Behavior,
    StateMachine_CodeBlock,
    StateMachine_Trigger,
    StateMachine_Behavior,
    StateMachine_Region,
    Vertex,
    StateMachine_State,
    State,
    StateMachine_FinalState,
    StateMachine_Transition,
    StateMachine_Vertex,
    StateMachine_PseudoState,
    StateMachine_StateMachine,
    StateMachine_Constraint,
    PseudoStateKind,
    TransitionKind,
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



def test_statemachine_codeblock_is_not_abstract():
    assert not inspect.isabstract(StateMachine_CodeBlock)


def test_statemachine_codeblock_constructor_exists():
    assert callable(StateMachine_CodeBlock.__init__)


def test_statemachine_codeblock_constructor_args():
    sig = inspect.signature(StateMachine_CodeBlock.__init__)
    params = list(sig.parameters.keys())
    assert "desc" in params, "Missing parameter 'desc'"

def test_statemachine_codeblock_has_desc():
    assert hasattr(StateMachine_CodeBlock, "desc")
    descriptor = None
    for klass in StateMachine_CodeBlock.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_trigger_is_not_abstract():
    assert not inspect.isabstract(StateMachine_Trigger)


def test_statemachine_trigger_constructor_exists():
    assert callable(StateMachine_Trigger.__init__)


def test_statemachine_trigger_constructor_args():
    sig = inspect.signature(StateMachine_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_statemachine_trigger_has_trigger():
    assert hasattr(StateMachine_Trigger, "trigger")
    descriptor = None
    for klass in StateMachine_Trigger.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_behavior_is_not_abstract():
    assert not inspect.isabstract(StateMachine_Behavior)


def test_statemachine_behavior_constructor_exists():
    assert callable(StateMachine_Behavior.__init__)


def test_statemachine_behavior_constructor_args():
    sig = inspect.signature(StateMachine_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_region_is_not_abstract():
    assert not inspect.isabstract(StateMachine_Region)


def test_statemachine_region_constructor_exists():
    assert callable(StateMachine_Region.__init__)


def test_statemachine_region_constructor_args():
    sig = inspect.signature(StateMachine_Region.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_region_has_name():
    assert hasattr(StateMachine_Region, "name")
    descriptor = None
    for klass in StateMachine_Region.__mro__:
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



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(StateMachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(StateMachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(StateMachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "isSubmachineState" in params, "Missing parameter 'isSubmachineState'"
    assert "isSimple" in params, "Missing parameter 'isSimple'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"

def test_statemachine_state_has_isSubmachineState():
    assert hasattr(StateMachine_State, "isSubmachineState")
    descriptor = None
    for klass in StateMachine_State.__mro__:
        if "isSubmachineState" in klass.__dict__:
            descriptor = klass.__dict__["isSubmachineState"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_state_has_isSimple():
    assert hasattr(StateMachine_State, "isSimple")
    descriptor = None
    for klass in StateMachine_State.__mro__:
        if "isSimple" in klass.__dict__:
            descriptor = klass.__dict__["isSimple"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_state_has_isComposite():
    assert hasattr(StateMachine_State, "isComposite")
    descriptor = None
    for klass in StateMachine_State.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_finalstate_is_not_abstract():
    assert not inspect.isabstract(StateMachine_FinalState)


def test_statemachine_finalstate_constructor_exists():
    assert callable(StateMachine_FinalState.__init__)


def test_statemachine_finalstate_constructor_args():
    sig = inspect.signature(StateMachine_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(StateMachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(StateMachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(StateMachine_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_transition_has_kind():
    assert hasattr(StateMachine_Transition, "kind")
    descriptor = None
    for klass in StateMachine_Transition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_transition_has_name():
    assert hasattr(StateMachine_Transition, "name")
    descriptor = None
    for klass in StateMachine_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_vertex_is_not_abstract():
    assert not inspect.isabstract(StateMachine_Vertex)


def test_statemachine_vertex_constructor_exists():
    assert callable(StateMachine_Vertex.__init__)


def test_statemachine_vertex_constructor_args():
    sig = inspect.signature(StateMachine_Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_vertex_has_name():
    assert hasattr(StateMachine_Vertex, "name")
    descriptor = None
    for klass in StateMachine_Vertex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_pseudostate_is_not_abstract():
    assert not inspect.isabstract(StateMachine_PseudoState)


def test_statemachine_pseudostate_constructor_exists():
    assert callable(StateMachine_PseudoState.__init__)


def test_statemachine_pseudostate_constructor_args():
    sig = inspect.signature(StateMachine_PseudoState.__init__)
    params = list(sig.parameters.keys())
    assert "pseudoStateKind" in params, "Missing parameter 'pseudoStateKind'"
    assert "returnValue" in params, "Missing parameter 'returnValue'"

def test_statemachine_pseudostate_has_pseudoStateKind():
    assert hasattr(StateMachine_PseudoState, "pseudoStateKind")
    descriptor = None
    for klass in StateMachine_PseudoState.__mro__:
        if "pseudoStateKind" in klass.__dict__:
            descriptor = klass.__dict__["pseudoStateKind"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_pseudostate_has_returnValue():
    assert hasattr(StateMachine_PseudoState, "returnValue")
    descriptor = None
    for klass in StateMachine_PseudoState.__mro__:
        if "returnValue" in klass.__dict__:
            descriptor = klass.__dict__["returnValue"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine_StateMachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(StateMachine_StateMachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(StateMachine_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_statemachine_has_name():
    assert hasattr(StateMachine_StateMachine, "name")
    descriptor = None
    for klass in StateMachine_StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_constraint_is_not_abstract():
    assert not inspect.isabstract(StateMachine_Constraint)


def test_statemachine_constraint_constructor_exists():
    assert callable(StateMachine_Constraint.__init__)


def test_statemachine_constraint_constructor_args():
    sig = inspect.signature(StateMachine_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "constraint" in params, "Missing parameter 'constraint'"

def test_statemachine_constraint_has_constraint():
    assert hasattr(StateMachine_Constraint, "constraint")
    descriptor = None
    for klass in StateMachine_Constraint.__mro__:
        if "constraint" in klass.__dict__:
            descriptor = klass.__dict__["constraint"]
            break
    assert isinstance(descriptor, property)

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudoStateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudoStateKind]
    expected_literals = [
        "initial",
        "entryPoint",
        "shallowHistory",
        "deepHistory",
        "exitPoint",
        "join",
        "choice",
        "fork",
        "terminate",
        "junction",
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
        "external",
        "local",
        "internal",
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
Behavior_strategy = st.builds(
    Behavior,
)
StateMachine_CodeBlock_strategy = st.builds(
    StateMachine_CodeBlock,
    desc=
        safe_text
)
StateMachine_Trigger_strategy = st.builds(
    StateMachine_Trigger,
    trigger=
        safe_text
)
StateMachine_Behavior_strategy = st.builds(
    StateMachine_Behavior,
)
StateMachine_Region_strategy = st.builds(
    StateMachine_Region,
    name=
        safe_text
)
Vertex_strategy = st.builds(
    Vertex,
)
StateMachine_State_strategy = st.builds(
    StateMachine_State,
    isSubmachineState=
        safe_text,
    isSimple=
        safe_text,
    isComposite=
        safe_text
)
State_strategy = st.builds(
    State,
)
StateMachine_FinalState_strategy = st.builds(
    StateMachine_FinalState,
)
StateMachine_Transition_strategy = st.builds(
    StateMachine_Transition,
    kind=
        safe_text,
    name=
        safe_text
)
StateMachine_Vertex_strategy = st.builds(
    StateMachine_Vertex,
    name=
        safe_text
)
StateMachine_PseudoState_strategy = st.builds(
    StateMachine_PseudoState,
    pseudoStateKind=
        safe_text,
    returnValue=
        safe_text
)
StateMachine_StateMachine_strategy = st.builds(
    StateMachine_StateMachine,
    name=
        safe_text
)
StateMachine_Constraint_strategy = st.builds(
    StateMachine_Constraint,
    constraint=
        safe_text
)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=StateMachine_CodeBlock_strategy)
@settings(max_examples=50)
def test_statemachine_codeblock_instantiation(instance):
    assert isinstance(instance, StateMachine_CodeBlock)



@given(instance=StateMachine_CodeBlock_strategy)
def test_statemachine_codeblock_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=StateMachine_Trigger_strategy)
@settings(max_examples=50)
def test_statemachine_trigger_instantiation(instance):
    assert isinstance(instance, StateMachine_Trigger)



@given(instance=StateMachine_Trigger_strategy)
def test_statemachine_trigger_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=StateMachine_Behavior_strategy)
@settings(max_examples=50)
def test_statemachine_behavior_instantiation(instance):
    assert isinstance(instance, StateMachine_Behavior)

@given(instance=StateMachine_Region_strategy)
@settings(max_examples=50)
def test_statemachine_region_instantiation(instance):
    assert isinstance(instance, StateMachine_Region)



@given(instance=StateMachine_Region_strategy)
def test_statemachine_region_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=StateMachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, StateMachine_State)



@given(instance=StateMachine_State_strategy)
def test_statemachine_state_isSubmachineState_setter(instance):
    original = instance.isSubmachineState
    instance.isSubmachineState = original
    assert instance.isSubmachineState == original



@given(instance=StateMachine_State_strategy)
def test_statemachine_state_isSimple_setter(instance):
    original = instance.isSimple
    instance.isSimple = original
    assert instance.isSimple == original



@given(instance=StateMachine_State_strategy)
def test_statemachine_state_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=StateMachine_FinalState_strategy)
@settings(max_examples=50)
def test_statemachine_finalstate_instantiation(instance):
    assert isinstance(instance, StateMachine_FinalState)

@given(instance=StateMachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, StateMachine_Transition)



@given(instance=StateMachine_Transition_strategy)
def test_statemachine_transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=StateMachine_Transition_strategy)
def test_statemachine_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachine_Vertex_strategy)
@settings(max_examples=50)
def test_statemachine_vertex_instantiation(instance):
    assert isinstance(instance, StateMachine_Vertex)



@given(instance=StateMachine_Vertex_strategy)
def test_statemachine_vertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachine_PseudoState_strategy)
@settings(max_examples=50)
def test_statemachine_pseudostate_instantiation(instance):
    assert isinstance(instance, StateMachine_PseudoState)



@given(instance=StateMachine_PseudoState_strategy)
def test_statemachine_pseudostate_pseudoStateKind_setter(instance):
    original = instance.pseudoStateKind
    instance.pseudoStateKind = original
    assert instance.pseudoStateKind == original



@given(instance=StateMachine_PseudoState_strategy)
def test_statemachine_pseudostate_returnValue_setter(instance):
    original = instance.returnValue
    instance.returnValue = original
    assert instance.returnValue == original

@given(instance=StateMachine_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine_StateMachine)



@given(instance=StateMachine_StateMachine_strategy)
def test_statemachine_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachine_Constraint_strategy)
@settings(max_examples=50)
def test_statemachine_constraint_instantiation(instance):
    assert isinstance(instance, StateMachine_Constraint)



@given(instance=StateMachine_Constraint_strategy)
def test_statemachine_constraint_constraint_setter(instance):
    original = instance.constraint
    instance.constraint = original
    assert instance.constraint == original
