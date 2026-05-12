import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    SimplStateMachineDC_CompositeState,
    SimplStateMachineDC_State,
    PseudoState,
    SimplStateMachineDC_InitialState,
    SimplStateMachineDC_PseudoState,
    SimplStateMachineDC_Transition,
    SimplStateMachineDC_StateMachine,
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



def test_simplstatemachinedc_compositestate_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachineDC_CompositeState)


def test_simplstatemachinedc_compositestate_constructor_exists():
    assert callable(SimplStateMachineDC_CompositeState.__init__)


def test_simplstatemachinedc_compositestate_constructor_args():
    sig = inspect.signature(SimplStateMachineDC_CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_simplstatemachinedc_state_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachineDC_State)


def test_simplstatemachinedc_state_constructor_exists():
    assert callable(SimplStateMachineDC_State.__init__)


def test_simplstatemachinedc_state_constructor_args():
    sig = inspect.signature(SimplStateMachineDC_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isActive" in params, "Missing parameter 'isActive'"
    assert "OrdIf" in params, "Missing parameter 'OrdIf'"
    assert "Ord" in params, "Missing parameter 'Ord'"
    assert "Inh" in params, "Missing parameter 'Inh'"
    assert "InhIf" in params, "Missing parameter 'InhIf'"

def test_simplstatemachinedc_state_has_name():
    assert hasattr(SimplStateMachineDC_State, "name")
    descriptor = None
    for klass in SimplStateMachineDC_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplstatemachinedc_state_has_isActive():
    assert hasattr(SimplStateMachineDC_State, "isActive")
    descriptor = None
    for klass in SimplStateMachineDC_State.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)

def test_simplstatemachinedc_state_has_OrdIf():
    assert hasattr(SimplStateMachineDC_State, "OrdIf")
    descriptor = None
    for klass in SimplStateMachineDC_State.__mro__:
        if "OrdIf" in klass.__dict__:
            descriptor = klass.__dict__["OrdIf"]
            break
    assert isinstance(descriptor, property)

def test_simplstatemachinedc_state_has_Ord():
    assert hasattr(SimplStateMachineDC_State, "Ord")
    descriptor = None
    for klass in SimplStateMachineDC_State.__mro__:
        if "Ord" in klass.__dict__:
            descriptor = klass.__dict__["Ord"]
            break
    assert isinstance(descriptor, property)

def test_simplstatemachinedc_state_has_Inh():
    assert hasattr(SimplStateMachineDC_State, "Inh")
    descriptor = None
    for klass in SimplStateMachineDC_State.__mro__:
        if "Inh" in klass.__dict__:
            descriptor = klass.__dict__["Inh"]
            break
    assert isinstance(descriptor, property)

def test_simplstatemachinedc_state_has_InhIf():
    assert hasattr(SimplStateMachineDC_State, "InhIf")
    descriptor = None
    for klass in SimplStateMachineDC_State.__mro__:
        if "InhIf" in klass.__dict__:
            descriptor = klass.__dict__["InhIf"]
            break
    assert isinstance(descriptor, property)



def test_pseudostate_is_not_abstract():
    assert not inspect.isabstract(PseudoState)


def test_pseudostate_constructor_exists():
    assert callable(PseudoState.__init__)


def test_pseudostate_constructor_args():
    sig = inspect.signature(PseudoState.__init__)
    params = list(sig.parameters.keys())



def test_simplstatemachinedc_initialstate_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachineDC_InitialState)


def test_simplstatemachinedc_initialstate_constructor_exists():
    assert callable(SimplStateMachineDC_InitialState.__init__)


def test_simplstatemachinedc_initialstate_constructor_args():
    sig = inspect.signature(SimplStateMachineDC_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_simplstatemachinedc_pseudostate_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachineDC_PseudoState)


def test_simplstatemachinedc_pseudostate_constructor_exists():
    assert callable(SimplStateMachineDC_PseudoState.__init__)


def test_simplstatemachinedc_pseudostate_constructor_args():
    sig = inspect.signature(SimplStateMachineDC_PseudoState.__init__)
    params = list(sig.parameters.keys())



def test_simplstatemachinedc_transition_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachineDC_Transition)


def test_simplstatemachinedc_transition_constructor_exists():
    assert callable(SimplStateMachineDC_Transition.__init__)


def test_simplstatemachinedc_transition_constructor_args():
    sig = inspect.signature(SimplStateMachineDC_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_simplstatemachinedc_transition_has_event():
    assert hasattr(SimplStateMachineDC_Transition, "event")
    descriptor = None
    for klass in SimplStateMachineDC_Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_simplstatemachinedc_statemachine_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachineDC_StateMachine)


def test_simplstatemachinedc_statemachine_constructor_exists():
    assert callable(SimplStateMachineDC_StateMachine.__init__)


def test_simplstatemachinedc_statemachine_constructor_args():
    sig = inspect.signature(SimplStateMachineDC_StateMachine.__init__)
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
State_strategy = st.builds(
    State,
)
SimplStateMachineDC_CompositeState_strategy = st.builds(
    SimplStateMachineDC_CompositeState,
)
SimplStateMachineDC_State_strategy = st.builds(
    SimplStateMachineDC_State,
    name=
        safe_text,
    isActive=
        st.booleans(),
    OrdIf=
        safe_text,
    Ord=
        safe_text,
    Inh=
        safe_text,
    InhIf=
        safe_text
)
PseudoState_strategy = st.builds(
    PseudoState,
)
SimplStateMachineDC_InitialState_strategy = st.builds(
    SimplStateMachineDC_InitialState,
)
SimplStateMachineDC_PseudoState_strategy = st.builds(
    SimplStateMachineDC_PseudoState,
)
SimplStateMachineDC_Transition_strategy = st.builds(
    SimplStateMachineDC_Transition,
    event=
        safe_text
)
SimplStateMachineDC_StateMachine_strategy = st.builds(
    SimplStateMachineDC_StateMachine,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=SimplStateMachineDC_CompositeState_strategy)
@settings(max_examples=50)
def test_simplstatemachinedc_compositestate_instantiation(instance):
    assert isinstance(instance, SimplStateMachineDC_CompositeState)

@given(instance=SimplStateMachineDC_State_strategy)
@settings(max_examples=50)
def test_simplstatemachinedc_state_instantiation(instance):
    assert isinstance(instance, SimplStateMachineDC_State)



@given(instance=SimplStateMachineDC_State_strategy)
def test_simplstatemachinedc_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SimplStateMachineDC_State_strategy)
def test_simplstatemachinedc_state_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original



@given(instance=SimplStateMachineDC_State_strategy)
def test_simplstatemachinedc_state_OrdIf_setter(instance):
    original = instance.OrdIf
    instance.OrdIf = original
    assert instance.OrdIf == original



@given(instance=SimplStateMachineDC_State_strategy)
def test_simplstatemachinedc_state_Ord_setter(instance):
    original = instance.Ord
    instance.Ord = original
    assert instance.Ord == original



@given(instance=SimplStateMachineDC_State_strategy)
def test_simplstatemachinedc_state_Inh_setter(instance):
    original = instance.Inh
    instance.Inh = original
    assert instance.Inh == original



@given(instance=SimplStateMachineDC_State_strategy)
def test_simplstatemachinedc_state_InhIf_setter(instance):
    original = instance.InhIf
    instance.InhIf = original
    assert instance.InhIf == original

@given(instance=PseudoState_strategy)
@settings(max_examples=50)
def test_pseudostate_instantiation(instance):
    assert isinstance(instance, PseudoState)

@given(instance=SimplStateMachineDC_InitialState_strategy)
@settings(max_examples=50)
def test_simplstatemachinedc_initialstate_instantiation(instance):
    assert isinstance(instance, SimplStateMachineDC_InitialState)

@given(instance=SimplStateMachineDC_PseudoState_strategy)
@settings(max_examples=50)
def test_simplstatemachinedc_pseudostate_instantiation(instance):
    assert isinstance(instance, SimplStateMachineDC_PseudoState)

@given(instance=SimplStateMachineDC_Transition_strategy)
@settings(max_examples=50)
def test_simplstatemachinedc_transition_instantiation(instance):
    assert isinstance(instance, SimplStateMachineDC_Transition)



@given(instance=SimplStateMachineDC_Transition_strategy)
def test_simplstatemachinedc_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=SimplStateMachineDC_StateMachine_strategy)
@settings(max_examples=50)
def test_simplstatemachinedc_statemachine_instantiation(instance):
    assert isinstance(instance, SimplStateMachineDC_StateMachine)
