import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    capellacommon::Constraint,
    StateEvent,
    capellacommon::TimeEvent,
    capellacommon::ChangeEvent,
    AbstractEvent,
    Pseudostate,
    capellacommon::JoinPseudoState,
    capellacommon::ForkPseudoState,
    capellacommon::ShallowHistoryPseudoState,
    capellacommon::ChoicePseudoState,
    capellacommon::DeepHistoryPseudoState,
    capellacommon::EntryPointPseudoState,
    capellacommon::ExitPointPseudoState,
    capellacommon::TerminatePseudoState,
    capellacommon::InitialPseudoState,
    capellacommon::TraceableElement,
    ModelElement,
    TraceableElement,
    CapellaElement,
    capellacommon::GenericTrace,
    Structure,
    IState,
    State,
    capellacommon::FinalState,
    capellacommon::Mode,
    capellacommon::AbstractEvent,
    capellacommon::AbstractCapability,
    capellacommon::FunctionalChain,
    capellacommon::AbstractFunction,
    AbstractState,
    capellacommon::Pseudostate,
    capellacommon::State,
    NamedElement,
    capellacommon::StateEvent,
    capellacommon::AbstractState,
    capellacommon::StateTransition,
    capellacommon::Region,
    AbstractBehavior,
    capellacommon::StateMachine,
    capellacommon::AbstractCapabilityPkg,
    ChangeEventKind,
    TransitionKind,
    TimeEventKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_capellacommon::constraint_is_not_abstract():
    assert not inspect.isabstract(capellacommon::Constraint)


def test_capellacommon::constraint_constructor_exists():
    assert callable(capellacommon::Constraint.__init__)


def test_capellacommon::constraint_constructor_args():
    sig = inspect.signature(capellacommon::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_stateevent_is_not_abstract():
    assert not inspect.isabstract(StateEvent)


def test_stateevent_constructor_exists():
    assert callable(StateEvent.__init__)


def test_stateevent_constructor_args():
    sig = inspect.signature(StateEvent.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::timeevent_is_not_abstract():
    assert not inspect.isabstract(capellacommon::TimeEvent)


def test_capellacommon::timeevent_constructor_exists():
    assert callable(capellacommon::TimeEvent.__init__)


def test_capellacommon::timeevent_constructor_args():
    sig = inspect.signature(capellacommon::TimeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_capellacommon::timeevent_has_time():
    assert hasattr(capellacommon::TimeEvent, "time")
    descriptor = None
    for klass in capellacommon::TimeEvent.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_capellacommon::timeevent_has_kind():
    assert hasattr(capellacommon::TimeEvent, "kind")
    descriptor = None
    for klass in capellacommon::TimeEvent.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_capellacommon::changeevent_is_not_abstract():
    assert not inspect.isabstract(capellacommon::ChangeEvent)


def test_capellacommon::changeevent_constructor_exists():
    assert callable(capellacommon::ChangeEvent.__init__)


def test_capellacommon::changeevent_constructor_args():
    sig = inspect.signature(capellacommon::ChangeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_capellacommon::changeevent_has_kind():
    assert hasattr(capellacommon::ChangeEvent, "kind")
    descriptor = None
    for klass in capellacommon::ChangeEvent.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_abstractevent_is_not_abstract():
    assert not inspect.isabstract(AbstractEvent)


def test_abstractevent_constructor_exists():
    assert callable(AbstractEvent.__init__)


def test_abstractevent_constructor_args():
    sig = inspect.signature(AbstractEvent.__init__)
    params = list(sig.parameters.keys())



def test_pseudostate_is_not_abstract():
    assert not inspect.isabstract(Pseudostate)


def test_pseudostate_constructor_exists():
    assert callable(Pseudostate.__init__)


def test_pseudostate_constructor_args():
    sig = inspect.signature(Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::joinpseudostate_is_not_abstract():
    assert not inspect.isabstract(capellacommon::JoinPseudoState)


def test_capellacommon::joinpseudostate_constructor_exists():
    assert callable(capellacommon::JoinPseudoState.__init__)


def test_capellacommon::joinpseudostate_constructor_args():
    sig = inspect.signature(capellacommon::JoinPseudoState.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::forkpseudostate_is_not_abstract():
    assert not inspect.isabstract(capellacommon::ForkPseudoState)


def test_capellacommon::forkpseudostate_constructor_exists():
    assert callable(capellacommon::ForkPseudoState.__init__)


def test_capellacommon::forkpseudostate_constructor_args():
    sig = inspect.signature(capellacommon::ForkPseudoState.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::shallowhistorypseudostate_is_not_abstract():
    assert not inspect.isabstract(capellacommon::ShallowHistoryPseudoState)


def test_capellacommon::shallowhistorypseudostate_constructor_exists():
    assert callable(capellacommon::ShallowHistoryPseudoState.__init__)


def test_capellacommon::shallowhistorypseudostate_constructor_args():
    sig = inspect.signature(capellacommon::ShallowHistoryPseudoState.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::choicepseudostate_is_not_abstract():
    assert not inspect.isabstract(capellacommon::ChoicePseudoState)


def test_capellacommon::choicepseudostate_constructor_exists():
    assert callable(capellacommon::ChoicePseudoState.__init__)


def test_capellacommon::choicepseudostate_constructor_args():
    sig = inspect.signature(capellacommon::ChoicePseudoState.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::deephistorypseudostate_is_not_abstract():
    assert not inspect.isabstract(capellacommon::DeepHistoryPseudoState)


def test_capellacommon::deephistorypseudostate_constructor_exists():
    assert callable(capellacommon::DeepHistoryPseudoState.__init__)


def test_capellacommon::deephistorypseudostate_constructor_args():
    sig = inspect.signature(capellacommon::DeepHistoryPseudoState.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::entrypointpseudostate_is_not_abstract():
    assert not inspect.isabstract(capellacommon::EntryPointPseudoState)


def test_capellacommon::entrypointpseudostate_constructor_exists():
    assert callable(capellacommon::EntryPointPseudoState.__init__)


def test_capellacommon::entrypointpseudostate_constructor_args():
    sig = inspect.signature(capellacommon::EntryPointPseudoState.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::exitpointpseudostate_is_not_abstract():
    assert not inspect.isabstract(capellacommon::ExitPointPseudoState)


def test_capellacommon::exitpointpseudostate_constructor_exists():
    assert callable(capellacommon::ExitPointPseudoState.__init__)


def test_capellacommon::exitpointpseudostate_constructor_args():
    sig = inspect.signature(capellacommon::ExitPointPseudoState.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::terminatepseudostate_is_not_abstract():
    assert not inspect.isabstract(capellacommon::TerminatePseudoState)


def test_capellacommon::terminatepseudostate_constructor_exists():
    assert callable(capellacommon::TerminatePseudoState.__init__)


def test_capellacommon::terminatepseudostate_constructor_args():
    sig = inspect.signature(capellacommon::TerminatePseudoState.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::initialpseudostate_is_not_abstract():
    assert not inspect.isabstract(capellacommon::InitialPseudoState)


def test_capellacommon::initialpseudostate_constructor_exists():
    assert callable(capellacommon::InitialPseudoState.__init__)


def test_capellacommon::initialpseudostate_constructor_args():
    sig = inspect.signature(capellacommon::InitialPseudoState.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::traceableelement_is_not_abstract():
    assert not inspect.isabstract(capellacommon::TraceableElement)


def test_capellacommon::traceableelement_constructor_exists():
    assert callable(capellacommon::TraceableElement.__init__)


def test_capellacommon::traceableelement_constructor_args():
    sig = inspect.signature(capellacommon::TraceableElement.__init__)
    params = list(sig.parameters.keys())



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_traceableelement_is_not_abstract():
    assert not inspect.isabstract(TraceableElement)


def test_traceableelement_constructor_exists():
    assert callable(TraceableElement.__init__)


def test_traceableelement_constructor_args():
    sig = inspect.signature(TraceableElement.__init__)
    params = list(sig.parameters.keys())



def test_capellaelement_is_not_abstract():
    assert not inspect.isabstract(CapellaElement)


def test_capellaelement_constructor_exists():
    assert callable(CapellaElement.__init__)


def test_capellaelement_constructor_args():
    sig = inspect.signature(CapellaElement.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::generictrace_is_not_abstract():
    assert not inspect.isabstract(capellacommon::GenericTrace)


def test_capellacommon::generictrace_constructor_exists():
    assert callable(capellacommon::GenericTrace.__init__)


def test_capellacommon::generictrace_constructor_args():
    sig = inspect.signature(capellacommon::GenericTrace.__init__)
    params = list(sig.parameters.keys())



def test_structure_is_not_abstract():
    assert not inspect.isabstract(Structure)


def test_structure_constructor_exists():
    assert callable(Structure.__init__)


def test_structure_constructor_args():
    sig = inspect.signature(Structure.__init__)
    params = list(sig.parameters.keys())



def test_istate_is_not_abstract():
    assert not inspect.isabstract(IState)


def test_istate_constructor_exists():
    assert callable(IState.__init__)


def test_istate_constructor_args():
    sig = inspect.signature(IState.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::finalstate_is_not_abstract():
    assert not inspect.isabstract(capellacommon::FinalState)


def test_capellacommon::finalstate_constructor_exists():
    assert callable(capellacommon::FinalState.__init__)


def test_capellacommon::finalstate_constructor_args():
    sig = inspect.signature(capellacommon::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::mode_is_not_abstract():
    assert not inspect.isabstract(capellacommon::Mode)


def test_capellacommon::mode_constructor_exists():
    assert callable(capellacommon::Mode.__init__)


def test_capellacommon::mode_constructor_args():
    sig = inspect.signature(capellacommon::Mode.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::abstractevent_is_not_abstract():
    assert not inspect.isabstract(capellacommon::AbstractEvent)


def test_capellacommon::abstractevent_constructor_exists():
    assert callable(capellacommon::AbstractEvent.__init__)


def test_capellacommon::abstractevent_constructor_args():
    sig = inspect.signature(capellacommon::AbstractEvent.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::abstractcapability_is_not_abstract():
    assert not inspect.isabstract(capellacommon::AbstractCapability)


def test_capellacommon::abstractcapability_constructor_exists():
    assert callable(capellacommon::AbstractCapability.__init__)


def test_capellacommon::abstractcapability_constructor_args():
    sig = inspect.signature(capellacommon::AbstractCapability.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::functionalchain_is_not_abstract():
    assert not inspect.isabstract(capellacommon::FunctionalChain)


def test_capellacommon::functionalchain_constructor_exists():
    assert callable(capellacommon::FunctionalChain.__init__)


def test_capellacommon::functionalchain_constructor_args():
    sig = inspect.signature(capellacommon::FunctionalChain.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::abstractfunction_is_not_abstract():
    assert not inspect.isabstract(capellacommon::AbstractFunction)


def test_capellacommon::abstractfunction_constructor_exists():
    assert callable(capellacommon::AbstractFunction.__init__)


def test_capellacommon::abstractfunction_constructor_args():
    sig = inspect.signature(capellacommon::AbstractFunction.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::pseudostate_is_not_abstract():
    assert not inspect.isabstract(capellacommon::Pseudostate)


def test_capellacommon::pseudostate_constructor_exists():
    assert callable(capellacommon::Pseudostate.__init__)


def test_capellacommon::pseudostate_constructor_args():
    sig = inspect.signature(capellacommon::Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::state_is_not_abstract():
    assert not inspect.isabstract(capellacommon::State)


def test_capellacommon::state_constructor_exists():
    assert callable(capellacommon::State.__init__)


def test_capellacommon::state_constructor_args():
    sig = inspect.signature(capellacommon::State.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::stateevent_is_not_abstract():
    assert not inspect.isabstract(capellacommon::StateEvent)


def test_capellacommon::stateevent_constructor_exists():
    assert callable(capellacommon::StateEvent.__init__)


def test_capellacommon::stateevent_constructor_args():
    sig = inspect.signature(capellacommon::StateEvent.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::abstractstate_is_not_abstract():
    assert not inspect.isabstract(capellacommon::AbstractState)


def test_capellacommon::abstractstate_constructor_exists():
    assert callable(capellacommon::AbstractState.__init__)


def test_capellacommon::abstractstate_constructor_args():
    sig = inspect.signature(capellacommon::AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::statetransition_is_not_abstract():
    assert not inspect.isabstract(capellacommon::StateTransition)


def test_capellacommon::statetransition_constructor_exists():
    assert callable(capellacommon::StateTransition.__init__)


def test_capellacommon::statetransition_constructor_args():
    sig = inspect.signature(capellacommon::StateTransition.__init__)
    params = list(sig.parameters.keys())
    assert "triggerDescription" in params, "Missing parameter 'triggerDescription'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_capellacommon::statetransition_has_triggerDescription():
    assert hasattr(capellacommon::StateTransition, "triggerDescription")
    descriptor = None
    for klass in capellacommon::StateTransition.__mro__:
        if "triggerDescription" in klass.__dict__:
            descriptor = klass.__dict__["triggerDescription"]
            break
    assert isinstance(descriptor, property)

def test_capellacommon::statetransition_has_kind():
    assert hasattr(capellacommon::StateTransition, "kind")
    descriptor = None
    for klass in capellacommon::StateTransition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_capellacommon::region_is_not_abstract():
    assert not inspect.isabstract(capellacommon::Region)


def test_capellacommon::region_constructor_exists():
    assert callable(capellacommon::Region.__init__)


def test_capellacommon::region_constructor_args():
    sig = inspect.signature(capellacommon::Region.__init__)
    params = list(sig.parameters.keys())



def test_abstractbehavior_is_not_abstract():
    assert not inspect.isabstract(AbstractBehavior)


def test_abstractbehavior_constructor_exists():
    assert callable(AbstractBehavior.__init__)


def test_abstractbehavior_constructor_args():
    sig = inspect.signature(AbstractBehavior.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::statemachine_is_not_abstract():
    assert not inspect.isabstract(capellacommon::StateMachine)


def test_capellacommon::statemachine_constructor_exists():
    assert callable(capellacommon::StateMachine.__init__)


def test_capellacommon::statemachine_constructor_args():
    sig = inspect.signature(capellacommon::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_capellacommon::abstractcapabilitypkg_is_not_abstract():
    assert not inspect.isabstract(capellacommon::AbstractCapabilityPkg)


def test_capellacommon::abstractcapabilitypkg_constructor_exists():
    assert callable(capellacommon::AbstractCapabilityPkg.__init__)


def test_capellacommon::abstractcapabilitypkg_constructor_args():
    sig = inspect.signature(capellacommon::AbstractCapabilityPkg.__init__)
    params = list(sig.parameters.keys())

def test_changeeventkind_exists():
    # Check that the Enumeration exists
    assert ChangeEventKind is not None

def test_changeeventkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ChangeEventKind]
    expected_literals = [
        "WHEN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ChangeEventKind"

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

def test_timeeventkind_exists():
    # Check that the Enumeration exists
    assert TimeEventKind is not None

def test_timeeventkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeEventKind]
    expected_literals = [
        "AT",
        "AFTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeEventKind"


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
capellacommon::Constraint_strategy = st.builds(
    capellacommon::Constraint,
)
StateEvent_strategy = st.builds(
    StateEvent,
)
capellacommon::TimeEvent_strategy = st.builds(
    capellacommon::TimeEvent,
    time=
        safe_text,
    kind=
        safe_text
)
capellacommon::ChangeEvent_strategy = st.builds(
    capellacommon::ChangeEvent,
    kind=
        safe_text
)
AbstractEvent_strategy = st.builds(
    AbstractEvent,
)
Pseudostate_strategy = st.builds(
    Pseudostate,
)
capellacommon::JoinPseudoState_strategy = st.builds(
    capellacommon::JoinPseudoState,
)
capellacommon::ForkPseudoState_strategy = st.builds(
    capellacommon::ForkPseudoState,
)
capellacommon::ShallowHistoryPseudoState_strategy = st.builds(
    capellacommon::ShallowHistoryPseudoState,
)
capellacommon::ChoicePseudoState_strategy = st.builds(
    capellacommon::ChoicePseudoState,
)
capellacommon::DeepHistoryPseudoState_strategy = st.builds(
    capellacommon::DeepHistoryPseudoState,
)
capellacommon::EntryPointPseudoState_strategy = st.builds(
    capellacommon::EntryPointPseudoState,
)
capellacommon::ExitPointPseudoState_strategy = st.builds(
    capellacommon::ExitPointPseudoState,
)
capellacommon::TerminatePseudoState_strategy = st.builds(
    capellacommon::TerminatePseudoState,
)
capellacommon::InitialPseudoState_strategy = st.builds(
    capellacommon::InitialPseudoState,
)
capellacommon::TraceableElement_strategy = st.builds(
    capellacommon::TraceableElement,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
TraceableElement_strategy = st.builds(
    TraceableElement,
)
CapellaElement_strategy = st.builds(
    CapellaElement,
)
capellacommon::GenericTrace_strategy = st.builds(
    capellacommon::GenericTrace,
)
Structure_strategy = st.builds(
    Structure,
)
IState_strategy = st.builds(
    IState,
)
State_strategy = st.builds(
    State,
)
capellacommon::FinalState_strategy = st.builds(
    capellacommon::FinalState,
)
capellacommon::Mode_strategy = st.builds(
    capellacommon::Mode,
)
capellacommon::AbstractEvent_strategy = st.builds(
    capellacommon::AbstractEvent,
)
capellacommon::AbstractCapability_strategy = st.builds(
    capellacommon::AbstractCapability,
)
capellacommon::FunctionalChain_strategy = st.builds(
    capellacommon::FunctionalChain,
)
capellacommon::AbstractFunction_strategy = st.builds(
    capellacommon::AbstractFunction,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
capellacommon::Pseudostate_strategy = st.builds(
    capellacommon::Pseudostate,
)
capellacommon::State_strategy = st.builds(
    capellacommon::State,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
capellacommon::StateEvent_strategy = st.builds(
    capellacommon::StateEvent,
)
capellacommon::AbstractState_strategy = st.builds(
    capellacommon::AbstractState,
)
capellacommon::StateTransition_strategy = st.builds(
    capellacommon::StateTransition,
    triggerDescription=
        safe_text,
    kind=
        safe_text
)
capellacommon::Region_strategy = st.builds(
    capellacommon::Region,
)
AbstractBehavior_strategy = st.builds(
    AbstractBehavior,
)
capellacommon::StateMachine_strategy = st.builds(
    capellacommon::StateMachine,
)
capellacommon::AbstractCapabilityPkg_strategy = st.builds(
    capellacommon::AbstractCapabilityPkg,
)

@given(instance=capellacommon::Constraint_strategy)
@settings(max_examples=50)
def test_capellacommon::constraint_instantiation(instance):
    assert isinstance(instance, capellacommon::Constraint)

@given(instance=StateEvent_strategy)
@settings(max_examples=50)
def test_stateevent_instantiation(instance):
    assert isinstance(instance, StateEvent)

@given(instance=capellacommon::TimeEvent_strategy)
@settings(max_examples=50)
def test_capellacommon::timeevent_instantiation(instance):
    assert isinstance(instance, capellacommon::TimeEvent)

@given(instance=capellacommon::TimeEvent_strategy)
def test_capellacommon::timeevent_time_type(instance):
    assert isinstance(instance.time, str)


@given(instance=capellacommon::TimeEvent_strategy)
def test_capellacommon::timeevent_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=capellacommon::TimeEvent_strategy)
def test_capellacommon::timeevent_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=capellacommon::TimeEvent_strategy)
def test_capellacommon::timeevent_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=capellacommon::ChangeEvent_strategy)
@settings(max_examples=50)
def test_capellacommon::changeevent_instantiation(instance):
    assert isinstance(instance, capellacommon::ChangeEvent)

@given(instance=capellacommon::ChangeEvent_strategy)
def test_capellacommon::changeevent_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=capellacommon::ChangeEvent_strategy)
def test_capellacommon::changeevent_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=AbstractEvent_strategy)
@settings(max_examples=50)
def test_abstractevent_instantiation(instance):
    assert isinstance(instance, AbstractEvent)

@given(instance=Pseudostate_strategy)
@settings(max_examples=50)
def test_pseudostate_instantiation(instance):
    assert isinstance(instance, Pseudostate)

@given(instance=capellacommon::JoinPseudoState_strategy)
@settings(max_examples=50)
def test_capellacommon::joinpseudostate_instantiation(instance):
    assert isinstance(instance, capellacommon::JoinPseudoState)

@given(instance=capellacommon::ForkPseudoState_strategy)
@settings(max_examples=50)
def test_capellacommon::forkpseudostate_instantiation(instance):
    assert isinstance(instance, capellacommon::ForkPseudoState)

@given(instance=capellacommon::ShallowHistoryPseudoState_strategy)
@settings(max_examples=50)
def test_capellacommon::shallowhistorypseudostate_instantiation(instance):
    assert isinstance(instance, capellacommon::ShallowHistoryPseudoState)

@given(instance=capellacommon::ChoicePseudoState_strategy)
@settings(max_examples=50)
def test_capellacommon::choicepseudostate_instantiation(instance):
    assert isinstance(instance, capellacommon::ChoicePseudoState)

@given(instance=capellacommon::DeepHistoryPseudoState_strategy)
@settings(max_examples=50)
def test_capellacommon::deephistorypseudostate_instantiation(instance):
    assert isinstance(instance, capellacommon::DeepHistoryPseudoState)

@given(instance=capellacommon::EntryPointPseudoState_strategy)
@settings(max_examples=50)
def test_capellacommon::entrypointpseudostate_instantiation(instance):
    assert isinstance(instance, capellacommon::EntryPointPseudoState)

@given(instance=capellacommon::ExitPointPseudoState_strategy)
@settings(max_examples=50)
def test_capellacommon::exitpointpseudostate_instantiation(instance):
    assert isinstance(instance, capellacommon::ExitPointPseudoState)

@given(instance=capellacommon::TerminatePseudoState_strategy)
@settings(max_examples=50)
def test_capellacommon::terminatepseudostate_instantiation(instance):
    assert isinstance(instance, capellacommon::TerminatePseudoState)

@given(instance=capellacommon::InitialPseudoState_strategy)
@settings(max_examples=50)
def test_capellacommon::initialpseudostate_instantiation(instance):
    assert isinstance(instance, capellacommon::InitialPseudoState)

@given(instance=capellacommon::TraceableElement_strategy)
@settings(max_examples=50)
def test_capellacommon::traceableelement_instantiation(instance):
    assert isinstance(instance, capellacommon::TraceableElement)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=TraceableElement_strategy)
@settings(max_examples=50)
def test_traceableelement_instantiation(instance):
    assert isinstance(instance, TraceableElement)

@given(instance=CapellaElement_strategy)
@settings(max_examples=50)
def test_capellaelement_instantiation(instance):
    assert isinstance(instance, CapellaElement)

@given(instance=capellacommon::GenericTrace_strategy)
@settings(max_examples=50)
def test_capellacommon::generictrace_instantiation(instance):
    assert isinstance(instance, capellacommon::GenericTrace)

@given(instance=Structure_strategy)
@settings(max_examples=50)
def test_structure_instantiation(instance):
    assert isinstance(instance, Structure)

@given(instance=IState_strategy)
@settings(max_examples=50)
def test_istate_instantiation(instance):
    assert isinstance(instance, IState)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=capellacommon::FinalState_strategy)
@settings(max_examples=50)
def test_capellacommon::finalstate_instantiation(instance):
    assert isinstance(instance, capellacommon::FinalState)

@given(instance=capellacommon::Mode_strategy)
@settings(max_examples=50)
def test_capellacommon::mode_instantiation(instance):
    assert isinstance(instance, capellacommon::Mode)

@given(instance=capellacommon::AbstractEvent_strategy)
@settings(max_examples=50)
def test_capellacommon::abstractevent_instantiation(instance):
    assert isinstance(instance, capellacommon::AbstractEvent)

@given(instance=capellacommon::AbstractCapability_strategy)
@settings(max_examples=50)
def test_capellacommon::abstractcapability_instantiation(instance):
    assert isinstance(instance, capellacommon::AbstractCapability)

@given(instance=capellacommon::FunctionalChain_strategy)
@settings(max_examples=50)
def test_capellacommon::functionalchain_instantiation(instance):
    assert isinstance(instance, capellacommon::FunctionalChain)

@given(instance=capellacommon::AbstractFunction_strategy)
@settings(max_examples=50)
def test_capellacommon::abstractfunction_instantiation(instance):
    assert isinstance(instance, capellacommon::AbstractFunction)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=capellacommon::Pseudostate_strategy)
@settings(max_examples=50)
def test_capellacommon::pseudostate_instantiation(instance):
    assert isinstance(instance, capellacommon::Pseudostate)

@given(instance=capellacommon::State_strategy)
@settings(max_examples=50)
def test_capellacommon::state_instantiation(instance):
    assert isinstance(instance, capellacommon::State)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=capellacommon::StateEvent_strategy)
@settings(max_examples=50)
def test_capellacommon::stateevent_instantiation(instance):
    assert isinstance(instance, capellacommon::StateEvent)

@given(instance=capellacommon::AbstractState_strategy)
@settings(max_examples=50)
def test_capellacommon::abstractstate_instantiation(instance):
    assert isinstance(instance, capellacommon::AbstractState)

@given(instance=capellacommon::StateTransition_strategy)
@settings(max_examples=50)
def test_capellacommon::statetransition_instantiation(instance):
    assert isinstance(instance, capellacommon::StateTransition)

@given(instance=capellacommon::StateTransition_strategy)
def test_capellacommon::statetransition_triggerDescription_type(instance):
    assert isinstance(instance.triggerDescription, str)


@given(instance=capellacommon::StateTransition_strategy)
def test_capellacommon::statetransition_triggerDescription_setter(instance):
    original = instance.triggerDescription
    instance.triggerDescription = original
    assert instance.triggerDescription == original

@given(instance=capellacommon::StateTransition_strategy)
def test_capellacommon::statetransition_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=capellacommon::StateTransition_strategy)
def test_capellacommon::statetransition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=capellacommon::Region_strategy)
@settings(max_examples=50)
def test_capellacommon::region_instantiation(instance):
    assert isinstance(instance, capellacommon::Region)

@given(instance=AbstractBehavior_strategy)
@settings(max_examples=50)
def test_abstractbehavior_instantiation(instance):
    assert isinstance(instance, AbstractBehavior)

@given(instance=capellacommon::StateMachine_strategy)
@settings(max_examples=50)
def test_capellacommon::statemachine_instantiation(instance):
    assert isinstance(instance, capellacommon::StateMachine)

@given(instance=capellacommon::AbstractCapabilityPkg_strategy)
@settings(max_examples=50)
def test_capellacommon::abstractcapabilitypkg_instantiation(instance):
    assert isinstance(instance, capellacommon::AbstractCapabilityPkg)
