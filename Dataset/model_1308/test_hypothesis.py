import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PseudoState,
    SimplStateMachineDC::InitialState,
    State,
    SimplStateMachineDC::PseudoState,
    SimplStateMachineDC::CompositeState,
    SimplStateMachineDC::State,
    SimplStateMachineDC::Transition,
    SimplStateMachineDC::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pseudostate_is_not_abstract():
    assert not inspect.isabstract(PseudoState)


def test_pseudostate_constructor_exists():
    assert callable(PseudoState.__init__)


def test_pseudostate_constructor_args():
    sig = inspect.signature(PseudoState.__init__)
    params = list(sig.parameters.keys())



def test_simplstatemachinedc::initialstate_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachineDC::InitialState)


def test_simplstatemachinedc::initialstate_constructor_exists():
    assert callable(SimplStateMachineDC::InitialState.__init__)


def test_simplstatemachinedc::initialstate_constructor_args():
    sig = inspect.signature(SimplStateMachineDC::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_simplstatemachinedc::pseudostate_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachineDC::PseudoState)


def test_simplstatemachinedc::pseudostate_constructor_exists():
    assert callable(SimplStateMachineDC::PseudoState.__init__)


def test_simplstatemachinedc::pseudostate_constructor_args():
    sig = inspect.signature(SimplStateMachineDC::PseudoState.__init__)
    params = list(sig.parameters.keys())



def test_simplstatemachinedc::compositestate_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachineDC::CompositeState)


def test_simplstatemachinedc::compositestate_constructor_exists():
    assert callable(SimplStateMachineDC::CompositeState.__init__)


def test_simplstatemachinedc::compositestate_constructor_args():
    sig = inspect.signature(SimplStateMachineDC::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_simplstatemachinedc::state_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachineDC::State)


def test_simplstatemachinedc::state_constructor_exists():
    assert callable(SimplStateMachineDC::State.__init__)


def test_simplstatemachinedc::state_constructor_args():
    sig = inspect.signature(SimplStateMachineDC::State.__init__)
    params = list(sig.parameters.keys())
    assert "Ord" in params, "Missing parameter 'Ord'"
    assert "name" in params, "Missing parameter 'name'"
    assert "Inh" in params, "Missing parameter 'Inh'"
    assert "isActive" in params, "Missing parameter 'isActive'"
    assert "OrdIf" in params, "Missing parameter 'OrdIf'"
    assert "InhIf" in params, "Missing parameter 'InhIf'"

def test_simplstatemachinedc::state_has_Ord():
    assert hasattr(SimplStateMachineDC::State, "Ord")
    descriptor = None
    for klass in SimplStateMachineDC::State.__mro__:
        if "Ord" in klass.__dict__:
            descriptor = klass.__dict__["Ord"]
            break
    assert isinstance(descriptor, property)

def test_simplstatemachinedc::state_has_name():
    assert hasattr(SimplStateMachineDC::State, "name")
    descriptor = None
    for klass in SimplStateMachineDC::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplstatemachinedc::state_has_Inh():
    assert hasattr(SimplStateMachineDC::State, "Inh")
    descriptor = None
    for klass in SimplStateMachineDC::State.__mro__:
        if "Inh" in klass.__dict__:
            descriptor = klass.__dict__["Inh"]
            break
    assert isinstance(descriptor, property)

def test_simplstatemachinedc::state_has_isActive():
    assert hasattr(SimplStateMachineDC::State, "isActive")
    descriptor = None
    for klass in SimplStateMachineDC::State.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)

def test_simplstatemachinedc::state_has_OrdIf():
    assert hasattr(SimplStateMachineDC::State, "OrdIf")
    descriptor = None
    for klass in SimplStateMachineDC::State.__mro__:
        if "OrdIf" in klass.__dict__:
            descriptor = klass.__dict__["OrdIf"]
            break
    assert isinstance(descriptor, property)

def test_simplstatemachinedc::state_has_InhIf():
    assert hasattr(SimplStateMachineDC::State, "InhIf")
    descriptor = None
    for klass in SimplStateMachineDC::State.__mro__:
        if "InhIf" in klass.__dict__:
            descriptor = klass.__dict__["InhIf"]
            break
    assert isinstance(descriptor, property)



def test_simplstatemachinedc::transition_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachineDC::Transition)


def test_simplstatemachinedc::transition_constructor_exists():
    assert callable(SimplStateMachineDC::Transition.__init__)


def test_simplstatemachinedc::transition_constructor_args():
    sig = inspect.signature(SimplStateMachineDC::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_simplstatemachinedc::transition_has_event():
    assert hasattr(SimplStateMachineDC::Transition, "event")
    descriptor = None
    for klass in SimplStateMachineDC::Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_simplstatemachinedc::statemachine_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachineDC::StateMachine)


def test_simplstatemachinedc::statemachine_constructor_exists():
    assert callable(SimplStateMachineDC::StateMachine.__init__)


def test_simplstatemachinedc::statemachine_constructor_args():
    sig = inspect.signature(SimplStateMachineDC::StateMachine.__init__)
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
PseudoState_strategy = st.builds(
    PseudoState,
)
SimplStateMachineDC::InitialState_strategy = st.builds(
    SimplStateMachineDC::InitialState,
)
State_strategy = st.builds(
    State,
)
SimplStateMachineDC::PseudoState_strategy = st.builds(
    SimplStateMachineDC::PseudoState,
)
SimplStateMachineDC::CompositeState_strategy = st.builds(
    SimplStateMachineDC::CompositeState,
)
SimplStateMachineDC::State_strategy = st.builds(
    SimplStateMachineDC::State,
    Ord=
        safe_text,
    name=
        safe_text,
    Inh=
        safe_text,
    isActive=
        st.booleans(),
    OrdIf=
        safe_text,
    InhIf=
        safe_text
)
SimplStateMachineDC::Transition_strategy = st.builds(
    SimplStateMachineDC::Transition,
    event=
        safe_text
)
SimplStateMachineDC::StateMachine_strategy = st.builds(
    SimplStateMachineDC::StateMachine,
)

@given(instance=PseudoState_strategy)
@settings(max_examples=50)
def test_pseudostate_instantiation(instance):
    assert isinstance(instance, PseudoState)

@given(instance=SimplStateMachineDC::InitialState_strategy)
@settings(max_examples=50)
def test_simplstatemachinedc::initialstate_instantiation(instance):
    assert isinstance(instance, SimplStateMachineDC::InitialState)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=SimplStateMachineDC::PseudoState_strategy)
@settings(max_examples=50)
def test_simplstatemachinedc::pseudostate_instantiation(instance):
    assert isinstance(instance, SimplStateMachineDC::PseudoState)

@given(instance=SimplStateMachineDC::CompositeState_strategy)
@settings(max_examples=50)
def test_simplstatemachinedc::compositestate_instantiation(instance):
    assert isinstance(instance, SimplStateMachineDC::CompositeState)

@given(instance=SimplStateMachineDC::State_strategy)
@settings(max_examples=50)
def test_simplstatemachinedc::state_instantiation(instance):
    assert isinstance(instance, SimplStateMachineDC::State)

@given(instance=SimplStateMachineDC::State_strategy)
def test_simplstatemachinedc::state_Ord_type(instance):
    assert isinstance(instance.Ord, str)


@given(instance=SimplStateMachineDC::State_strategy)
def test_simplstatemachinedc::state_Ord_setter(instance):
    original = instance.Ord
    instance.Ord = original
    assert instance.Ord == original

@given(instance=SimplStateMachineDC::State_strategy)
def test_simplstatemachinedc::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimplStateMachineDC::State_strategy)
def test_simplstatemachinedc::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimplStateMachineDC::State_strategy)
def test_simplstatemachinedc::state_Inh_type(instance):
    assert isinstance(instance.Inh, str)


@given(instance=SimplStateMachineDC::State_strategy)
def test_simplstatemachinedc::state_Inh_setter(instance):
    original = instance.Inh
    instance.Inh = original
    assert instance.Inh == original

@given(instance=SimplStateMachineDC::State_strategy)
def test_simplstatemachinedc::state_isActive_type(instance):
    assert isinstance(instance.isActive, bool)


@given(instance=SimplStateMachineDC::State_strategy)
def test_simplstatemachinedc::state_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=SimplStateMachineDC::State_strategy)
def test_simplstatemachinedc::state_OrdIf_type(instance):
    assert isinstance(instance.OrdIf, str)


@given(instance=SimplStateMachineDC::State_strategy)
def test_simplstatemachinedc::state_OrdIf_setter(instance):
    original = instance.OrdIf
    instance.OrdIf = original
    assert instance.OrdIf == original

@given(instance=SimplStateMachineDC::State_strategy)
def test_simplstatemachinedc::state_InhIf_type(instance):
    assert isinstance(instance.InhIf, str)


@given(instance=SimplStateMachineDC::State_strategy)
def test_simplstatemachinedc::state_InhIf_setter(instance):
    original = instance.InhIf
    instance.InhIf = original
    assert instance.InhIf == original

@given(instance=SimplStateMachineDC::Transition_strategy)
@settings(max_examples=50)
def test_simplstatemachinedc::transition_instantiation(instance):
    assert isinstance(instance, SimplStateMachineDC::Transition)

@given(instance=SimplStateMachineDC::Transition_strategy)
def test_simplstatemachinedc::transition_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=SimplStateMachineDC::Transition_strategy)
def test_simplstatemachinedc::transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=SimplStateMachineDC::StateMachine_strategy)
@settings(max_examples=50)
def test_simplstatemachinedc::statemachine_instantiation(instance):
    assert isinstance(instance, SimplStateMachineDC::StateMachine)
