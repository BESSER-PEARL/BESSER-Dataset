import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petrinetv3Trace::petrinetv3::TracedTransition,
    petrinetv3Trace::petrinetv3::TracedToken,
    petrinetv3::petrinetv3Trace::Token,
    petrinetv3::petrinetv3Trace::Place,
    petrinetv3Trace::petrinetv3::TracedPlace,
    petrinetv3Trace::States::Transition::clock::Value,
    petrinetv3::petrinetv3Trace::Net,
    petrinetv3::petrinetv3Trace::Transition,
    petrinetv3Trace::States::Place::tokens::Value,
    MSEOccurrence,
    petrinetv3Trace::Steps::Step,
    SmallStep,
    petrinetv3Trace::Steps::RootImplicitStep,
    Transition::clock::Value,
    Place::tokens::Value,
    petrinetv3Trace::States::State,
    BigStep,
    petrinetv3Trace::Steps::Petrinetv3::Net::Run,
    Steps::SmallStep,
    Steps::Petrinetv3::Net::Run::AbstractSubStep,
    petrinetv3Trace::Steps::Petrinetv3::Net::Initialize,
    State,
    Step,
    petrinetv3Trace::Steps::SmallStep,
    petrinetv3Trace::Steps::BigStep,
    petrinetv3::TracedTransition,
    petrinetv3::TracedToken,
    petrinetv3Trace::Steps::Petrinetv3::Transition::Fire,
    petrinetv3Trace::Steps::Petrinetv3::Net::TickEnabledTransitions,
    petrinetv3Trace::Steps::Petrinetv3::Net::Run::ImplicitStep,
    petrinetv3Trace::Steps::Petrinetv3::Net::Run::AbstractSubStep,
    Petrinetv3::Net::Run::AbstractSubStep,
    Petrinetv3::Transition::Fire,
    Petrinetv3::Net::TickEnabledTransitions,
    Petrinetv3::Net::Run,
    Petrinetv3::Net::Initialize,
    petrinetv3Trace::Trace,
    petrinetv3::TracedPlace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinetv3trace::petrinetv3::tracedtransition_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace::petrinetv3::TracedTransition)


def test_petrinetv3trace::petrinetv3::tracedtransition_constructor_exists():
    assert callable(petrinetv3Trace::petrinetv3::TracedTransition.__init__)


def test_petrinetv3trace::petrinetv3::tracedtransition_constructor_args():
    sig = inspect.signature(petrinetv3Trace::petrinetv3::TracedTransition.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace::petrinetv3::tracedtoken_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace::petrinetv3::TracedToken)


def test_petrinetv3trace::petrinetv3::tracedtoken_constructor_exists():
    assert callable(petrinetv3Trace::petrinetv3::TracedToken.__init__)


def test_petrinetv3trace::petrinetv3::tracedtoken_constructor_args():
    sig = inspect.signature(petrinetv3Trace::petrinetv3::TracedToken.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3::petrinetv3trace::token_is_not_abstract():
    assert not inspect.isabstract(petrinetv3::petrinetv3Trace::Token)


def test_petrinetv3::petrinetv3trace::token_constructor_exists():
    assert callable(petrinetv3::petrinetv3Trace::Token.__init__)


def test_petrinetv3::petrinetv3trace::token_constructor_args():
    sig = inspect.signature(petrinetv3::petrinetv3Trace::Token.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3::petrinetv3trace::place_is_not_abstract():
    assert not inspect.isabstract(petrinetv3::petrinetv3Trace::Place)


def test_petrinetv3::petrinetv3trace::place_constructor_exists():
    assert callable(petrinetv3::petrinetv3Trace::Place.__init__)


def test_petrinetv3::petrinetv3trace::place_constructor_args():
    sig = inspect.signature(petrinetv3::petrinetv3Trace::Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace::petrinetv3::tracedplace_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace::petrinetv3::TracedPlace)


def test_petrinetv3trace::petrinetv3::tracedplace_constructor_exists():
    assert callable(petrinetv3Trace::petrinetv3::TracedPlace.__init__)


def test_petrinetv3trace::petrinetv3::tracedplace_constructor_args():
    sig = inspect.signature(petrinetv3Trace::petrinetv3::TracedPlace.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace::states::transition::clock::value_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace::States::Transition::clock::Value)


def test_petrinetv3trace::states::transition::clock::value_constructor_exists():
    assert callable(petrinetv3Trace::States::Transition::clock::Value.__init__)


def test_petrinetv3trace::states::transition::clock::value_constructor_args():
    sig = inspect.signature(petrinetv3Trace::States::Transition::clock::Value.__init__)
    params = list(sig.parameters.keys())
    assert "clock" in params, "Missing parameter 'clock'"

def test_petrinetv3trace::states::transition::clock::value_has_clock():
    assert hasattr(petrinetv3Trace::States::Transition::clock::Value, "clock")
    descriptor = None
    for klass in petrinetv3Trace::States::Transition::clock::Value.__mro__:
        if "clock" in klass.__dict__:
            descriptor = klass.__dict__["clock"]
            break
    assert isinstance(descriptor, property)



def test_petrinetv3::petrinetv3trace::net_is_not_abstract():
    assert not inspect.isabstract(petrinetv3::petrinetv3Trace::Net)


def test_petrinetv3::petrinetv3trace::net_constructor_exists():
    assert callable(petrinetv3::petrinetv3Trace::Net.__init__)


def test_petrinetv3::petrinetv3trace::net_constructor_args():
    sig = inspect.signature(petrinetv3::petrinetv3Trace::Net.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3::petrinetv3trace::transition_is_not_abstract():
    assert not inspect.isabstract(petrinetv3::petrinetv3Trace::Transition)


def test_petrinetv3::petrinetv3trace::transition_constructor_exists():
    assert callable(petrinetv3::petrinetv3Trace::Transition.__init__)


def test_petrinetv3::petrinetv3trace::transition_constructor_args():
    sig = inspect.signature(petrinetv3::petrinetv3Trace::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace::states::place::tokens::value_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace::States::Place::tokens::Value)


def test_petrinetv3trace::states::place::tokens::value_constructor_exists():
    assert callable(petrinetv3Trace::States::Place::tokens::Value.__init__)


def test_petrinetv3trace::states::place::tokens::value_constructor_args():
    sig = inspect.signature(petrinetv3Trace::States::Place::tokens::Value.__init__)
    params = list(sig.parameters.keys())



def test_mseoccurrence_is_not_abstract():
    assert not inspect.isabstract(MSEOccurrence)


def test_mseoccurrence_constructor_exists():
    assert callable(MSEOccurrence.__init__)


def test_mseoccurrence_constructor_args():
    sig = inspect.signature(MSEOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace::steps::step_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace::Steps::Step)


def test_petrinetv3trace::steps::step_constructor_exists():
    assert callable(petrinetv3Trace::Steps::Step.__init__)


def test_petrinetv3trace::steps::step_constructor_args():
    sig = inspect.signature(petrinetv3Trace::Steps::Step.__init__)
    params = list(sig.parameters.keys())



def test_smallstep_is_not_abstract():
    assert not inspect.isabstract(SmallStep)


def test_smallstep_constructor_exists():
    assert callable(SmallStep.__init__)


def test_smallstep_constructor_args():
    sig = inspect.signature(SmallStep.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace::steps::rootimplicitstep_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace::Steps::RootImplicitStep)


def test_petrinetv3trace::steps::rootimplicitstep_constructor_exists():
    assert callable(petrinetv3Trace::Steps::RootImplicitStep.__init__)


def test_petrinetv3trace::steps::rootimplicitstep_constructor_args():
    sig = inspect.signature(petrinetv3Trace::Steps::RootImplicitStep.__init__)
    params = list(sig.parameters.keys())



def test_transition::clock::value_is_not_abstract():
    assert not inspect.isabstract(Transition::clock::Value)


def test_transition::clock::value_constructor_exists():
    assert callable(Transition::clock::Value.__init__)


def test_transition::clock::value_constructor_args():
    sig = inspect.signature(Transition::clock::Value.__init__)
    params = list(sig.parameters.keys())



def test_place::tokens::value_is_not_abstract():
    assert not inspect.isabstract(Place::tokens::Value)


def test_place::tokens::value_constructor_exists():
    assert callable(Place::tokens::Value.__init__)


def test_place::tokens::value_constructor_args():
    sig = inspect.signature(Place::tokens::Value.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace::states::state_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace::States::State)


def test_petrinetv3trace::states::state_constructor_exists():
    assert callable(petrinetv3Trace::States::State.__init__)


def test_petrinetv3trace::states::state_constructor_args():
    sig = inspect.signature(petrinetv3Trace::States::State.__init__)
    params = list(sig.parameters.keys())



def test_bigstep_is_not_abstract():
    assert not inspect.isabstract(BigStep)


def test_bigstep_constructor_exists():
    assert callable(BigStep.__init__)


def test_bigstep_constructor_args():
    sig = inspect.signature(BigStep.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace::steps::petrinetv3::net::run_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace::Steps::Petrinetv3::Net::Run)


def test_petrinetv3trace::steps::petrinetv3::net::run_constructor_exists():
    assert callable(petrinetv3Trace::Steps::Petrinetv3::Net::Run.__init__)


def test_petrinetv3trace::steps::petrinetv3::net::run_constructor_args():
    sig = inspect.signature(petrinetv3Trace::Steps::Petrinetv3::Net::Run.__init__)
    params = list(sig.parameters.keys())



def test_steps::smallstep_is_not_abstract():
    assert not inspect.isabstract(Steps::SmallStep)


def test_steps::smallstep_constructor_exists():
    assert callable(Steps::SmallStep.__init__)


def test_steps::smallstep_constructor_args():
    sig = inspect.signature(Steps::SmallStep.__init__)
    params = list(sig.parameters.keys())



def test_steps::petrinetv3::net::run::abstractsubstep_is_not_abstract():
    assert not inspect.isabstract(Steps::Petrinetv3::Net::Run::AbstractSubStep)


def test_steps::petrinetv3::net::run::abstractsubstep_constructor_exists():
    assert callable(Steps::Petrinetv3::Net::Run::AbstractSubStep.__init__)


def test_steps::petrinetv3::net::run::abstractsubstep_constructor_args():
    sig = inspect.signature(Steps::Petrinetv3::Net::Run::AbstractSubStep.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace::steps::petrinetv3::net::initialize_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace::Steps::Petrinetv3::Net::Initialize)


def test_petrinetv3trace::steps::petrinetv3::net::initialize_constructor_exists():
    assert callable(petrinetv3Trace::Steps::Petrinetv3::Net::Initialize.__init__)


def test_petrinetv3trace::steps::petrinetv3::net::initialize_constructor_args():
    sig = inspect.signature(petrinetv3Trace::Steps::Petrinetv3::Net::Initialize.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_step_is_not_abstract():
    assert not inspect.isabstract(Step)


def test_step_constructor_exists():
    assert callable(Step.__init__)


def test_step_constructor_args():
    sig = inspect.signature(Step.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace::steps::smallstep_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace::Steps::SmallStep)


def test_petrinetv3trace::steps::smallstep_constructor_exists():
    assert callable(petrinetv3Trace::Steps::SmallStep.__init__)


def test_petrinetv3trace::steps::smallstep_constructor_args():
    sig = inspect.signature(petrinetv3Trace::Steps::SmallStep.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace::steps::bigstep_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace::Steps::BigStep)


def test_petrinetv3trace::steps::bigstep_constructor_exists():
    assert callable(petrinetv3Trace::Steps::BigStep.__init__)


def test_petrinetv3trace::steps::bigstep_constructor_args():
    sig = inspect.signature(petrinetv3Trace::Steps::BigStep.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3::tracedtransition_is_not_abstract():
    assert not inspect.isabstract(petrinetv3::TracedTransition)


def test_petrinetv3::tracedtransition_constructor_exists():
    assert callable(petrinetv3::TracedTransition.__init__)


def test_petrinetv3::tracedtransition_constructor_args():
    sig = inspect.signature(petrinetv3::TracedTransition.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3::tracedtoken_is_not_abstract():
    assert not inspect.isabstract(petrinetv3::TracedToken)


def test_petrinetv3::tracedtoken_constructor_exists():
    assert callable(petrinetv3::TracedToken.__init__)


def test_petrinetv3::tracedtoken_constructor_args():
    sig = inspect.signature(petrinetv3::TracedToken.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace::steps::petrinetv3::transition::fire_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace::Steps::Petrinetv3::Transition::Fire)


def test_petrinetv3trace::steps::petrinetv3::transition::fire_constructor_exists():
    assert callable(petrinetv3Trace::Steps::Petrinetv3::Transition::Fire.__init__)


def test_petrinetv3trace::steps::petrinetv3::transition::fire_constructor_args():
    sig = inspect.signature(petrinetv3Trace::Steps::Petrinetv3::Transition::Fire.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace::steps::petrinetv3::net::tickenabledtransitions_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace::Steps::Petrinetv3::Net::TickEnabledTransitions)


def test_petrinetv3trace::steps::petrinetv3::net::tickenabledtransitions_constructor_exists():
    assert callable(petrinetv3Trace::Steps::Petrinetv3::Net::TickEnabledTransitions.__init__)


def test_petrinetv3trace::steps::petrinetv3::net::tickenabledtransitions_constructor_args():
    sig = inspect.signature(petrinetv3Trace::Steps::Petrinetv3::Net::TickEnabledTransitions.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace::steps::petrinetv3::net::run::implicitstep_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace::Steps::Petrinetv3::Net::Run::ImplicitStep)


def test_petrinetv3trace::steps::petrinetv3::net::run::implicitstep_constructor_exists():
    assert callable(petrinetv3Trace::Steps::Petrinetv3::Net::Run::ImplicitStep.__init__)


def test_petrinetv3trace::steps::petrinetv3::net::run::implicitstep_constructor_args():
    sig = inspect.signature(petrinetv3Trace::Steps::Petrinetv3::Net::Run::ImplicitStep.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace::steps::petrinetv3::net::run::abstractsubstep_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace::Steps::Petrinetv3::Net::Run::AbstractSubStep)


def test_petrinetv3trace::steps::petrinetv3::net::run::abstractsubstep_constructor_exists():
    assert callable(petrinetv3Trace::Steps::Petrinetv3::Net::Run::AbstractSubStep.__init__)


def test_petrinetv3trace::steps::petrinetv3::net::run::abstractsubstep_constructor_args():
    sig = inspect.signature(petrinetv3Trace::Steps::Petrinetv3::Net::Run::AbstractSubStep.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3::net::run::abstractsubstep_is_not_abstract():
    assert not inspect.isabstract(Petrinetv3::Net::Run::AbstractSubStep)


def test_petrinetv3::net::run::abstractsubstep_constructor_exists():
    assert callable(Petrinetv3::Net::Run::AbstractSubStep.__init__)


def test_petrinetv3::net::run::abstractsubstep_constructor_args():
    sig = inspect.signature(Petrinetv3::Net::Run::AbstractSubStep.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3::transition::fire_is_not_abstract():
    assert not inspect.isabstract(Petrinetv3::Transition::Fire)


def test_petrinetv3::transition::fire_constructor_exists():
    assert callable(Petrinetv3::Transition::Fire.__init__)


def test_petrinetv3::transition::fire_constructor_args():
    sig = inspect.signature(Petrinetv3::Transition::Fire.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3::net::tickenabledtransitions_is_not_abstract():
    assert not inspect.isabstract(Petrinetv3::Net::TickEnabledTransitions)


def test_petrinetv3::net::tickenabledtransitions_constructor_exists():
    assert callable(Petrinetv3::Net::TickEnabledTransitions.__init__)


def test_petrinetv3::net::tickenabledtransitions_constructor_args():
    sig = inspect.signature(Petrinetv3::Net::TickEnabledTransitions.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3::net::run_is_not_abstract():
    assert not inspect.isabstract(Petrinetv3::Net::Run)


def test_petrinetv3::net::run_constructor_exists():
    assert callable(Petrinetv3::Net::Run.__init__)


def test_petrinetv3::net::run_constructor_args():
    sig = inspect.signature(Petrinetv3::Net::Run.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3::net::initialize_is_not_abstract():
    assert not inspect.isabstract(Petrinetv3::Net::Initialize)


def test_petrinetv3::net::initialize_constructor_exists():
    assert callable(Petrinetv3::Net::Initialize.__init__)


def test_petrinetv3::net::initialize_constructor_args():
    sig = inspect.signature(Petrinetv3::Net::Initialize.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace::trace_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace::Trace)


def test_petrinetv3trace::trace_constructor_exists():
    assert callable(petrinetv3Trace::Trace.__init__)


def test_petrinetv3trace::trace_constructor_args():
    sig = inspect.signature(petrinetv3Trace::Trace.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3::tracedplace_is_not_abstract():
    assert not inspect.isabstract(petrinetv3::TracedPlace)


def test_petrinetv3::tracedplace_constructor_exists():
    assert callable(petrinetv3::TracedPlace.__init__)


def test_petrinetv3::tracedplace_constructor_args():
    sig = inspect.signature(petrinetv3::TracedPlace.__init__)
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
petrinetv3Trace::petrinetv3::TracedTransition_strategy = st.builds(
    petrinetv3Trace::petrinetv3::TracedTransition,
)
petrinetv3Trace::petrinetv3::TracedToken_strategy = st.builds(
    petrinetv3Trace::petrinetv3::TracedToken,
)
petrinetv3::petrinetv3Trace::Token_strategy = st.builds(
    petrinetv3::petrinetv3Trace::Token,
)
petrinetv3::petrinetv3Trace::Place_strategy = st.builds(
    petrinetv3::petrinetv3Trace::Place,
)
petrinetv3Trace::petrinetv3::TracedPlace_strategy = st.builds(
    petrinetv3Trace::petrinetv3::TracedPlace,
)
petrinetv3Trace::States::Transition::clock::Value_strategy = st.builds(
    petrinetv3Trace::States::Transition::clock::Value,
    clock=
        st.integers()
)
petrinetv3::petrinetv3Trace::Net_strategy = st.builds(
    petrinetv3::petrinetv3Trace::Net,
)
petrinetv3::petrinetv3Trace::Transition_strategy = st.builds(
    petrinetv3::petrinetv3Trace::Transition,
)
petrinetv3Trace::States::Place::tokens::Value_strategy = st.builds(
    petrinetv3Trace::States::Place::tokens::Value,
)
MSEOccurrence_strategy = st.builds(
    MSEOccurrence,
)
petrinetv3Trace::Steps::Step_strategy = st.builds(
    petrinetv3Trace::Steps::Step,
)
SmallStep_strategy = st.builds(
    SmallStep,
)
petrinetv3Trace::Steps::RootImplicitStep_strategy = st.builds(
    petrinetv3Trace::Steps::RootImplicitStep,
)
Transition::clock::Value_strategy = st.builds(
    Transition::clock::Value,
)
Place::tokens::Value_strategy = st.builds(
    Place::tokens::Value,
)
petrinetv3Trace::States::State_strategy = st.builds(
    petrinetv3Trace::States::State,
)
BigStep_strategy = st.builds(
    BigStep,
)
petrinetv3Trace::Steps::Petrinetv3::Net::Run_strategy = st.builds(
    petrinetv3Trace::Steps::Petrinetv3::Net::Run,
)
Steps::SmallStep_strategy = st.builds(
    Steps::SmallStep,
)
Steps::Petrinetv3::Net::Run::AbstractSubStep_strategy = st.builds(
    Steps::Petrinetv3::Net::Run::AbstractSubStep,
)
petrinetv3Trace::Steps::Petrinetv3::Net::Initialize_strategy = st.builds(
    petrinetv3Trace::Steps::Petrinetv3::Net::Initialize,
)
State_strategy = st.builds(
    State,
)
Step_strategy = st.builds(
    Step,
)
petrinetv3Trace::Steps::SmallStep_strategy = st.builds(
    petrinetv3Trace::Steps::SmallStep,
)
petrinetv3Trace::Steps::BigStep_strategy = st.builds(
    petrinetv3Trace::Steps::BigStep,
)
petrinetv3::TracedTransition_strategy = st.builds(
    petrinetv3::TracedTransition,
)
petrinetv3::TracedToken_strategy = st.builds(
    petrinetv3::TracedToken,
)
petrinetv3Trace::Steps::Petrinetv3::Transition::Fire_strategy = st.builds(
    petrinetv3Trace::Steps::Petrinetv3::Transition::Fire,
)
petrinetv3Trace::Steps::Petrinetv3::Net::TickEnabledTransitions_strategy = st.builds(
    petrinetv3Trace::Steps::Petrinetv3::Net::TickEnabledTransitions,
)
petrinetv3Trace::Steps::Petrinetv3::Net::Run::ImplicitStep_strategy = st.builds(
    petrinetv3Trace::Steps::Petrinetv3::Net::Run::ImplicitStep,
)
petrinetv3Trace::Steps::Petrinetv3::Net::Run::AbstractSubStep_strategy = st.builds(
    petrinetv3Trace::Steps::Petrinetv3::Net::Run::AbstractSubStep,
)
Petrinetv3::Net::Run::AbstractSubStep_strategy = st.builds(
    Petrinetv3::Net::Run::AbstractSubStep,
)
Petrinetv3::Transition::Fire_strategy = st.builds(
    Petrinetv3::Transition::Fire,
)
Petrinetv3::Net::TickEnabledTransitions_strategy = st.builds(
    Petrinetv3::Net::TickEnabledTransitions,
)
Petrinetv3::Net::Run_strategy = st.builds(
    Petrinetv3::Net::Run,
)
Petrinetv3::Net::Initialize_strategy = st.builds(
    Petrinetv3::Net::Initialize,
)
petrinetv3Trace::Trace_strategy = st.builds(
    petrinetv3Trace::Trace,
)
petrinetv3::TracedPlace_strategy = st.builds(
    petrinetv3::TracedPlace,
)

@given(instance=petrinetv3Trace::petrinetv3::TracedTransition_strategy)
@settings(max_examples=50)
def test_petrinetv3trace::petrinetv3::tracedtransition_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace::petrinetv3::TracedTransition)

@given(instance=petrinetv3Trace::petrinetv3::TracedToken_strategy)
@settings(max_examples=50)
def test_petrinetv3trace::petrinetv3::tracedtoken_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace::petrinetv3::TracedToken)

@given(instance=petrinetv3::petrinetv3Trace::Token_strategy)
@settings(max_examples=50)
def test_petrinetv3::petrinetv3trace::token_instantiation(instance):
    assert isinstance(instance, petrinetv3::petrinetv3Trace::Token)

@given(instance=petrinetv3::petrinetv3Trace::Place_strategy)
@settings(max_examples=50)
def test_petrinetv3::petrinetv3trace::place_instantiation(instance):
    assert isinstance(instance, petrinetv3::petrinetv3Trace::Place)

@given(instance=petrinetv3Trace::petrinetv3::TracedPlace_strategy)
@settings(max_examples=50)
def test_petrinetv3trace::petrinetv3::tracedplace_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace::petrinetv3::TracedPlace)

@given(instance=petrinetv3Trace::States::Transition::clock::Value_strategy)
@settings(max_examples=50)
def test_petrinetv3trace::states::transition::clock::value_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace::States::Transition::clock::Value)

@given(instance=petrinetv3Trace::States::Transition::clock::Value_strategy)
def test_petrinetv3trace::states::transition::clock::value_clock_type(instance):
    assert isinstance(instance.clock, int)


@given(instance=petrinetv3Trace::States::Transition::clock::Value_strategy)
def test_petrinetv3trace::states::transition::clock::value_clock_setter(instance):
    original = instance.clock
    instance.clock = original
    assert instance.clock == original

@given(instance=petrinetv3::petrinetv3Trace::Net_strategy)
@settings(max_examples=50)
def test_petrinetv3::petrinetv3trace::net_instantiation(instance):
    assert isinstance(instance, petrinetv3::petrinetv3Trace::Net)

@given(instance=petrinetv3::petrinetv3Trace::Transition_strategy)
@settings(max_examples=50)
def test_petrinetv3::petrinetv3trace::transition_instantiation(instance):
    assert isinstance(instance, petrinetv3::petrinetv3Trace::Transition)

@given(instance=petrinetv3Trace::States::Place::tokens::Value_strategy)
@settings(max_examples=50)
def test_petrinetv3trace::states::place::tokens::value_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace::States::Place::tokens::Value)

@given(instance=MSEOccurrence_strategy)
@settings(max_examples=50)
def test_mseoccurrence_instantiation(instance):
    assert isinstance(instance, MSEOccurrence)

@given(instance=petrinetv3Trace::Steps::Step_strategy)
@settings(max_examples=50)
def test_petrinetv3trace::steps::step_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace::Steps::Step)

@given(instance=SmallStep_strategy)
@settings(max_examples=50)
def test_smallstep_instantiation(instance):
    assert isinstance(instance, SmallStep)

@given(instance=petrinetv3Trace::Steps::RootImplicitStep_strategy)
@settings(max_examples=50)
def test_petrinetv3trace::steps::rootimplicitstep_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace::Steps::RootImplicitStep)

@given(instance=Transition::clock::Value_strategy)
@settings(max_examples=50)
def test_transition::clock::value_instantiation(instance):
    assert isinstance(instance, Transition::clock::Value)

@given(instance=Place::tokens::Value_strategy)
@settings(max_examples=50)
def test_place::tokens::value_instantiation(instance):
    assert isinstance(instance, Place::tokens::Value)

@given(instance=petrinetv3Trace::States::State_strategy)
@settings(max_examples=50)
def test_petrinetv3trace::states::state_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace::States::State)

@given(instance=BigStep_strategy)
@settings(max_examples=50)
def test_bigstep_instantiation(instance):
    assert isinstance(instance, BigStep)

@given(instance=petrinetv3Trace::Steps::Petrinetv3::Net::Run_strategy)
@settings(max_examples=50)
def test_petrinetv3trace::steps::petrinetv3::net::run_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace::Steps::Petrinetv3::Net::Run)

@given(instance=Steps::SmallStep_strategy)
@settings(max_examples=50)
def test_steps::smallstep_instantiation(instance):
    assert isinstance(instance, Steps::SmallStep)

@given(instance=Steps::Petrinetv3::Net::Run::AbstractSubStep_strategy)
@settings(max_examples=50)
def test_steps::petrinetv3::net::run::abstractsubstep_instantiation(instance):
    assert isinstance(instance, Steps::Petrinetv3::Net::Run::AbstractSubStep)

@given(instance=petrinetv3Trace::Steps::Petrinetv3::Net::Initialize_strategy)
@settings(max_examples=50)
def test_petrinetv3trace::steps::petrinetv3::net::initialize_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace::Steps::Petrinetv3::Net::Initialize)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=Step_strategy)
@settings(max_examples=50)
def test_step_instantiation(instance):
    assert isinstance(instance, Step)

@given(instance=petrinetv3Trace::Steps::SmallStep_strategy)
@settings(max_examples=50)
def test_petrinetv3trace::steps::smallstep_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace::Steps::SmallStep)

@given(instance=petrinetv3Trace::Steps::BigStep_strategy)
@settings(max_examples=50)
def test_petrinetv3trace::steps::bigstep_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace::Steps::BigStep)

@given(instance=petrinetv3::TracedTransition_strategy)
@settings(max_examples=50)
def test_petrinetv3::tracedtransition_instantiation(instance):
    assert isinstance(instance, petrinetv3::TracedTransition)

@given(instance=petrinetv3::TracedToken_strategy)
@settings(max_examples=50)
def test_petrinetv3::tracedtoken_instantiation(instance):
    assert isinstance(instance, petrinetv3::TracedToken)

@given(instance=petrinetv3Trace::Steps::Petrinetv3::Transition::Fire_strategy)
@settings(max_examples=50)
def test_petrinetv3trace::steps::petrinetv3::transition::fire_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace::Steps::Petrinetv3::Transition::Fire)

@given(instance=petrinetv3Trace::Steps::Petrinetv3::Net::TickEnabledTransitions_strategy)
@settings(max_examples=50)
def test_petrinetv3trace::steps::petrinetv3::net::tickenabledtransitions_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace::Steps::Petrinetv3::Net::TickEnabledTransitions)

@given(instance=petrinetv3Trace::Steps::Petrinetv3::Net::Run::ImplicitStep_strategy)
@settings(max_examples=50)
def test_petrinetv3trace::steps::petrinetv3::net::run::implicitstep_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace::Steps::Petrinetv3::Net::Run::ImplicitStep)

@given(instance=petrinetv3Trace::Steps::Petrinetv3::Net::Run::AbstractSubStep_strategy)
@settings(max_examples=50)
def test_petrinetv3trace::steps::petrinetv3::net::run::abstractsubstep_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace::Steps::Petrinetv3::Net::Run::AbstractSubStep)

@given(instance=Petrinetv3::Net::Run::AbstractSubStep_strategy)
@settings(max_examples=50)
def test_petrinetv3::net::run::abstractsubstep_instantiation(instance):
    assert isinstance(instance, Petrinetv3::Net::Run::AbstractSubStep)

@given(instance=Petrinetv3::Transition::Fire_strategy)
@settings(max_examples=50)
def test_petrinetv3::transition::fire_instantiation(instance):
    assert isinstance(instance, Petrinetv3::Transition::Fire)

@given(instance=Petrinetv3::Net::TickEnabledTransitions_strategy)
@settings(max_examples=50)
def test_petrinetv3::net::tickenabledtransitions_instantiation(instance):
    assert isinstance(instance, Petrinetv3::Net::TickEnabledTransitions)

@given(instance=Petrinetv3::Net::Run_strategy)
@settings(max_examples=50)
def test_petrinetv3::net::run_instantiation(instance):
    assert isinstance(instance, Petrinetv3::Net::Run)

@given(instance=Petrinetv3::Net::Initialize_strategy)
@settings(max_examples=50)
def test_petrinetv3::net::initialize_instantiation(instance):
    assert isinstance(instance, Petrinetv3::Net::Initialize)

@given(instance=petrinetv3Trace::Trace_strategy)
@settings(max_examples=50)
def test_petrinetv3trace::trace_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace::Trace)

@given(instance=petrinetv3::TracedPlace_strategy)
@settings(max_examples=50)
def test_petrinetv3::tracedplace_instantiation(instance):
    assert isinstance(instance, petrinetv3::TracedPlace)
