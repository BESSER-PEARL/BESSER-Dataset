import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    petrinetv3Trace_petrinetv3_TracedTransition,
    petrinetv3Trace_petrinetv3_TracedToken,
    petrinetv3_petrinetv3Trace_Token,
    petrinetv3_petrinetv3Trace_Place,
    petrinetv3Trace_petrinetv3_TracedPlace,
    petrinetv3Trace_States_Transition_clock_Value,
    petrinetv3_petrinetv3Trace_Net,
    petrinetv3_petrinetv3Trace_Transition,
    petrinetv3Trace_States_Place_tokens_Value,
    MSEOccurrence,
    petrinetv3Trace_Steps_Step,
    SmallStep,
    petrinetv3Trace_Steps_RootImplicitStep,
    Transition_clock_Value,
    Place_tokens_Value,
    petrinetv3Trace_States_State,
    BigStep,
    petrinetv3Trace_Steps_Petrinetv3_Net_Run,
    Steps_SmallStep,
    Steps_Petrinetv3_Net_Run_AbstractSubStep,
    petrinetv3Trace_Steps_Petrinetv3_Net_Initialize,
    State,
    Step,
    petrinetv3Trace_Steps_BigStep,
    petrinetv3Trace_Steps_SmallStep,
    petrinetv3_TracedTransition,
    petrinetv3_TracedToken,
    petrinetv3Trace_Steps_Petrinetv3_Transition_Fire,
    petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions,
    petrinetv3Trace_Steps_Petrinetv3_Net_Run_ImplicitStep,
    petrinetv3Trace_Steps_Petrinetv3_Net_Run_AbstractSubStep,
    Petrinetv3_Net_Run_AbstractSubStep,
    Petrinetv3_Transition_Fire,
    Petrinetv3_Net_TickEnabledTransitions,
    Petrinetv3_Net_Run,
    Petrinetv3_Net_Initialize,
    petrinetv3Trace_Trace,
    petrinetv3_TracedPlace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinetv3trace_petrinetv3_tracedtransition_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace_petrinetv3_TracedTransition)


def test_petrinetv3trace_petrinetv3_tracedtransition_constructor_exists():
    assert callable(petrinetv3Trace_petrinetv3_TracedTransition.__init__)


def test_petrinetv3trace_petrinetv3_tracedtransition_constructor_args():
    sig = inspect.signature(petrinetv3Trace_petrinetv3_TracedTransition.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace_petrinetv3_tracedtoken_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace_petrinetv3_TracedToken)


def test_petrinetv3trace_petrinetv3_tracedtoken_constructor_exists():
    assert callable(petrinetv3Trace_petrinetv3_TracedToken.__init__)


def test_petrinetv3trace_petrinetv3_tracedtoken_constructor_args():
    sig = inspect.signature(petrinetv3Trace_petrinetv3_TracedToken.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3_petrinetv3trace_token_is_not_abstract():
    assert not inspect.isabstract(petrinetv3_petrinetv3Trace_Token)


def test_petrinetv3_petrinetv3trace_token_constructor_exists():
    assert callable(petrinetv3_petrinetv3Trace_Token.__init__)


def test_petrinetv3_petrinetv3trace_token_constructor_args():
    sig = inspect.signature(petrinetv3_petrinetv3Trace_Token.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3_petrinetv3trace_place_is_not_abstract():
    assert not inspect.isabstract(petrinetv3_petrinetv3Trace_Place)


def test_petrinetv3_petrinetv3trace_place_constructor_exists():
    assert callable(petrinetv3_petrinetv3Trace_Place.__init__)


def test_petrinetv3_petrinetv3trace_place_constructor_args():
    sig = inspect.signature(petrinetv3_petrinetv3Trace_Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace_petrinetv3_tracedplace_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace_petrinetv3_TracedPlace)


def test_petrinetv3trace_petrinetv3_tracedplace_constructor_exists():
    assert callable(petrinetv3Trace_petrinetv3_TracedPlace.__init__)


def test_petrinetv3trace_petrinetv3_tracedplace_constructor_args():
    sig = inspect.signature(petrinetv3Trace_petrinetv3_TracedPlace.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace_states_transition_clock_value_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace_States_Transition_clock_Value)


def test_petrinetv3trace_states_transition_clock_value_constructor_exists():
    assert callable(petrinetv3Trace_States_Transition_clock_Value.__init__)


def test_petrinetv3trace_states_transition_clock_value_constructor_args():
    sig = inspect.signature(petrinetv3Trace_States_Transition_clock_Value.__init__)
    params = list(sig.parameters.keys())
    assert "clock" in params, "Missing parameter 'clock'"

def test_petrinetv3trace_states_transition_clock_value_has_clock():
    assert hasattr(petrinetv3Trace_States_Transition_clock_Value, "clock")
    descriptor = None
    for klass in petrinetv3Trace_States_Transition_clock_Value.__mro__:
        if "clock" in klass.__dict__:
            descriptor = klass.__dict__["clock"]
            break
    assert isinstance(descriptor, property)



def test_petrinetv3_petrinetv3trace_net_is_not_abstract():
    assert not inspect.isabstract(petrinetv3_petrinetv3Trace_Net)


def test_petrinetv3_petrinetv3trace_net_constructor_exists():
    assert callable(petrinetv3_petrinetv3Trace_Net.__init__)


def test_petrinetv3_petrinetv3trace_net_constructor_args():
    sig = inspect.signature(petrinetv3_petrinetv3Trace_Net.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3_petrinetv3trace_transition_is_not_abstract():
    assert not inspect.isabstract(petrinetv3_petrinetv3Trace_Transition)


def test_petrinetv3_petrinetv3trace_transition_constructor_exists():
    assert callable(petrinetv3_petrinetv3Trace_Transition.__init__)


def test_petrinetv3_petrinetv3trace_transition_constructor_args():
    sig = inspect.signature(petrinetv3_petrinetv3Trace_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace_states_place_tokens_value_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace_States_Place_tokens_Value)


def test_petrinetv3trace_states_place_tokens_value_constructor_exists():
    assert callable(petrinetv3Trace_States_Place_tokens_Value.__init__)


def test_petrinetv3trace_states_place_tokens_value_constructor_args():
    sig = inspect.signature(petrinetv3Trace_States_Place_tokens_Value.__init__)
    params = list(sig.parameters.keys())



def test_mseoccurrence_is_not_abstract():
    assert not inspect.isabstract(MSEOccurrence)


def test_mseoccurrence_constructor_exists():
    assert callable(MSEOccurrence.__init__)


def test_mseoccurrence_constructor_args():
    sig = inspect.signature(MSEOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace_steps_step_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace_Steps_Step)


def test_petrinetv3trace_steps_step_constructor_exists():
    assert callable(petrinetv3Trace_Steps_Step.__init__)


def test_petrinetv3trace_steps_step_constructor_args():
    sig = inspect.signature(petrinetv3Trace_Steps_Step.__init__)
    params = list(sig.parameters.keys())



def test_smallstep_is_not_abstract():
    assert not inspect.isabstract(SmallStep)


def test_smallstep_constructor_exists():
    assert callable(SmallStep.__init__)


def test_smallstep_constructor_args():
    sig = inspect.signature(SmallStep.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace_steps_rootimplicitstep_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace_Steps_RootImplicitStep)


def test_petrinetv3trace_steps_rootimplicitstep_constructor_exists():
    assert callable(petrinetv3Trace_Steps_RootImplicitStep.__init__)


def test_petrinetv3trace_steps_rootimplicitstep_constructor_args():
    sig = inspect.signature(petrinetv3Trace_Steps_RootImplicitStep.__init__)
    params = list(sig.parameters.keys())



def test_transition_clock_value_is_not_abstract():
    assert not inspect.isabstract(Transition_clock_Value)


def test_transition_clock_value_constructor_exists():
    assert callable(Transition_clock_Value.__init__)


def test_transition_clock_value_constructor_args():
    sig = inspect.signature(Transition_clock_Value.__init__)
    params = list(sig.parameters.keys())



def test_place_tokens_value_is_not_abstract():
    assert not inspect.isabstract(Place_tokens_Value)


def test_place_tokens_value_constructor_exists():
    assert callable(Place_tokens_Value.__init__)


def test_place_tokens_value_constructor_args():
    sig = inspect.signature(Place_tokens_Value.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace_states_state_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace_States_State)


def test_petrinetv3trace_states_state_constructor_exists():
    assert callable(petrinetv3Trace_States_State.__init__)


def test_petrinetv3trace_states_state_constructor_args():
    sig = inspect.signature(petrinetv3Trace_States_State.__init__)
    params = list(sig.parameters.keys())



def test_bigstep_is_not_abstract():
    assert not inspect.isabstract(BigStep)


def test_bigstep_constructor_exists():
    assert callable(BigStep.__init__)


def test_bigstep_constructor_args():
    sig = inspect.signature(BigStep.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace_steps_petrinetv3_net_run_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace_Steps_Petrinetv3_Net_Run)


def test_petrinetv3trace_steps_petrinetv3_net_run_constructor_exists():
    assert callable(petrinetv3Trace_Steps_Petrinetv3_Net_Run.__init__)


def test_petrinetv3trace_steps_petrinetv3_net_run_constructor_args():
    sig = inspect.signature(petrinetv3Trace_Steps_Petrinetv3_Net_Run.__init__)
    params = list(sig.parameters.keys())



def test_steps_smallstep_is_not_abstract():
    assert not inspect.isabstract(Steps_SmallStep)


def test_steps_smallstep_constructor_exists():
    assert callable(Steps_SmallStep.__init__)


def test_steps_smallstep_constructor_args():
    sig = inspect.signature(Steps_SmallStep.__init__)
    params = list(sig.parameters.keys())



def test_steps_petrinetv3_net_run_abstractsubstep_is_not_abstract():
    assert not inspect.isabstract(Steps_Petrinetv3_Net_Run_AbstractSubStep)


def test_steps_petrinetv3_net_run_abstractsubstep_constructor_exists():
    assert callable(Steps_Petrinetv3_Net_Run_AbstractSubStep.__init__)


def test_steps_petrinetv3_net_run_abstractsubstep_constructor_args():
    sig = inspect.signature(Steps_Petrinetv3_Net_Run_AbstractSubStep.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace_steps_petrinetv3_net_initialize_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace_Steps_Petrinetv3_Net_Initialize)


def test_petrinetv3trace_steps_petrinetv3_net_initialize_constructor_exists():
    assert callable(petrinetv3Trace_Steps_Petrinetv3_Net_Initialize.__init__)


def test_petrinetv3trace_steps_petrinetv3_net_initialize_constructor_args():
    sig = inspect.signature(petrinetv3Trace_Steps_Petrinetv3_Net_Initialize.__init__)
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



def test_petrinetv3trace_steps_bigstep_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace_Steps_BigStep)


def test_petrinetv3trace_steps_bigstep_constructor_exists():
    assert callable(petrinetv3Trace_Steps_BigStep.__init__)


def test_petrinetv3trace_steps_bigstep_constructor_args():
    sig = inspect.signature(petrinetv3Trace_Steps_BigStep.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace_steps_smallstep_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace_Steps_SmallStep)


def test_petrinetv3trace_steps_smallstep_constructor_exists():
    assert callable(petrinetv3Trace_Steps_SmallStep.__init__)


def test_petrinetv3trace_steps_smallstep_constructor_args():
    sig = inspect.signature(petrinetv3Trace_Steps_SmallStep.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3_tracedtransition_is_not_abstract():
    assert not inspect.isabstract(petrinetv3_TracedTransition)


def test_petrinetv3_tracedtransition_constructor_exists():
    assert callable(petrinetv3_TracedTransition.__init__)


def test_petrinetv3_tracedtransition_constructor_args():
    sig = inspect.signature(petrinetv3_TracedTransition.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3_tracedtoken_is_not_abstract():
    assert not inspect.isabstract(petrinetv3_TracedToken)


def test_petrinetv3_tracedtoken_constructor_exists():
    assert callable(petrinetv3_TracedToken.__init__)


def test_petrinetv3_tracedtoken_constructor_args():
    sig = inspect.signature(petrinetv3_TracedToken.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace_steps_petrinetv3_transition_fire_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace_Steps_Petrinetv3_Transition_Fire)


def test_petrinetv3trace_steps_petrinetv3_transition_fire_constructor_exists():
    assert callable(petrinetv3Trace_Steps_Petrinetv3_Transition_Fire.__init__)


def test_petrinetv3trace_steps_petrinetv3_transition_fire_constructor_args():
    sig = inspect.signature(petrinetv3Trace_Steps_Petrinetv3_Transition_Fire.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace_steps_petrinetv3_net_tickenabledtransitions_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions)


def test_petrinetv3trace_steps_petrinetv3_net_tickenabledtransitions_constructor_exists():
    assert callable(petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions.__init__)


def test_petrinetv3trace_steps_petrinetv3_net_tickenabledtransitions_constructor_args():
    sig = inspect.signature(petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace_steps_petrinetv3_net_run_implicitstep_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace_Steps_Petrinetv3_Net_Run_ImplicitStep)


def test_petrinetv3trace_steps_petrinetv3_net_run_implicitstep_constructor_exists():
    assert callable(petrinetv3Trace_Steps_Petrinetv3_Net_Run_ImplicitStep.__init__)


def test_petrinetv3trace_steps_petrinetv3_net_run_implicitstep_constructor_args():
    sig = inspect.signature(petrinetv3Trace_Steps_Petrinetv3_Net_Run_ImplicitStep.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace_steps_petrinetv3_net_run_abstractsubstep_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace_Steps_Petrinetv3_Net_Run_AbstractSubStep)


def test_petrinetv3trace_steps_petrinetv3_net_run_abstractsubstep_constructor_exists():
    assert callable(petrinetv3Trace_Steps_Petrinetv3_Net_Run_AbstractSubStep.__init__)


def test_petrinetv3trace_steps_petrinetv3_net_run_abstractsubstep_constructor_args():
    sig = inspect.signature(petrinetv3Trace_Steps_Petrinetv3_Net_Run_AbstractSubStep.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3_net_run_abstractsubstep_is_not_abstract():
    assert not inspect.isabstract(Petrinetv3_Net_Run_AbstractSubStep)


def test_petrinetv3_net_run_abstractsubstep_constructor_exists():
    assert callable(Petrinetv3_Net_Run_AbstractSubStep.__init__)


def test_petrinetv3_net_run_abstractsubstep_constructor_args():
    sig = inspect.signature(Petrinetv3_Net_Run_AbstractSubStep.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3_transition_fire_is_not_abstract():
    assert not inspect.isabstract(Petrinetv3_Transition_Fire)


def test_petrinetv3_transition_fire_constructor_exists():
    assert callable(Petrinetv3_Transition_Fire.__init__)


def test_petrinetv3_transition_fire_constructor_args():
    sig = inspect.signature(Petrinetv3_Transition_Fire.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3_net_tickenabledtransitions_is_not_abstract():
    assert not inspect.isabstract(Petrinetv3_Net_TickEnabledTransitions)


def test_petrinetv3_net_tickenabledtransitions_constructor_exists():
    assert callable(Petrinetv3_Net_TickEnabledTransitions.__init__)


def test_petrinetv3_net_tickenabledtransitions_constructor_args():
    sig = inspect.signature(Petrinetv3_Net_TickEnabledTransitions.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3_net_run_is_not_abstract():
    assert not inspect.isabstract(Petrinetv3_Net_Run)


def test_petrinetv3_net_run_constructor_exists():
    assert callable(Petrinetv3_Net_Run.__init__)


def test_petrinetv3_net_run_constructor_args():
    sig = inspect.signature(Petrinetv3_Net_Run.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3_net_initialize_is_not_abstract():
    assert not inspect.isabstract(Petrinetv3_Net_Initialize)


def test_petrinetv3_net_initialize_constructor_exists():
    assert callable(Petrinetv3_Net_Initialize.__init__)


def test_petrinetv3_net_initialize_constructor_args():
    sig = inspect.signature(Petrinetv3_Net_Initialize.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3trace_trace_is_not_abstract():
    assert not inspect.isabstract(petrinetv3Trace_Trace)


def test_petrinetv3trace_trace_constructor_exists():
    assert callable(petrinetv3Trace_Trace.__init__)


def test_petrinetv3trace_trace_constructor_args():
    sig = inspect.signature(petrinetv3Trace_Trace.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3_tracedplace_is_not_abstract():
    assert not inspect.isabstract(petrinetv3_TracedPlace)


def test_petrinetv3_tracedplace_constructor_exists():
    assert callable(petrinetv3_TracedPlace.__init__)


def test_petrinetv3_tracedplace_constructor_args():
    sig = inspect.signature(petrinetv3_TracedPlace.__init__)
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
petrinetv3Trace_petrinetv3_TracedTransition_strategy = st.builds(
    petrinetv3Trace_petrinetv3_TracedTransition,
)
petrinetv3Trace_petrinetv3_TracedToken_strategy = st.builds(
    petrinetv3Trace_petrinetv3_TracedToken,
)
petrinetv3_petrinetv3Trace_Token_strategy = st.builds(
    petrinetv3_petrinetv3Trace_Token,
)
petrinetv3_petrinetv3Trace_Place_strategy = st.builds(
    petrinetv3_petrinetv3Trace_Place,
)
petrinetv3Trace_petrinetv3_TracedPlace_strategy = st.builds(
    petrinetv3Trace_petrinetv3_TracedPlace,
)
petrinetv3Trace_States_Transition_clock_Value_strategy = st.builds(
    petrinetv3Trace_States_Transition_clock_Value,
    clock=
        st.integers()
)
petrinetv3_petrinetv3Trace_Net_strategy = st.builds(
    petrinetv3_petrinetv3Trace_Net,
)
petrinetv3_petrinetv3Trace_Transition_strategy = st.builds(
    petrinetv3_petrinetv3Trace_Transition,
)
petrinetv3Trace_States_Place_tokens_Value_strategy = st.builds(
    petrinetv3Trace_States_Place_tokens_Value,
)
MSEOccurrence_strategy = st.builds(
    MSEOccurrence,
)
petrinetv3Trace_Steps_Step_strategy = st.builds(
    petrinetv3Trace_Steps_Step,
)
SmallStep_strategy = st.builds(
    SmallStep,
)
petrinetv3Trace_Steps_RootImplicitStep_strategy = st.builds(
    petrinetv3Trace_Steps_RootImplicitStep,
)
Transition_clock_Value_strategy = st.builds(
    Transition_clock_Value,
)
Place_tokens_Value_strategy = st.builds(
    Place_tokens_Value,
)
petrinetv3Trace_States_State_strategy = st.builds(
    petrinetv3Trace_States_State,
)
BigStep_strategy = st.builds(
    BigStep,
)
petrinetv3Trace_Steps_Petrinetv3_Net_Run_strategy = st.builds(
    petrinetv3Trace_Steps_Petrinetv3_Net_Run,
)
Steps_SmallStep_strategy = st.builds(
    Steps_SmallStep,
)
Steps_Petrinetv3_Net_Run_AbstractSubStep_strategy = st.builds(
    Steps_Petrinetv3_Net_Run_AbstractSubStep,
)
petrinetv3Trace_Steps_Petrinetv3_Net_Initialize_strategy = st.builds(
    petrinetv3Trace_Steps_Petrinetv3_Net_Initialize,
)
State_strategy = st.builds(
    State,
)
Step_strategy = st.builds(
    Step,
)
petrinetv3Trace_Steps_BigStep_strategy = st.builds(
    petrinetv3Trace_Steps_BigStep,
)
petrinetv3Trace_Steps_SmallStep_strategy = st.builds(
    petrinetv3Trace_Steps_SmallStep,
)
petrinetv3_TracedTransition_strategy = st.builds(
    petrinetv3_TracedTransition,
)
petrinetv3_TracedToken_strategy = st.builds(
    petrinetv3_TracedToken,
)
petrinetv3Trace_Steps_Petrinetv3_Transition_Fire_strategy = st.builds(
    petrinetv3Trace_Steps_Petrinetv3_Transition_Fire,
)
petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions_strategy = st.builds(
    petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions,
)
petrinetv3Trace_Steps_Petrinetv3_Net_Run_ImplicitStep_strategy = st.builds(
    petrinetv3Trace_Steps_Petrinetv3_Net_Run_ImplicitStep,
)
petrinetv3Trace_Steps_Petrinetv3_Net_Run_AbstractSubStep_strategy = st.builds(
    petrinetv3Trace_Steps_Petrinetv3_Net_Run_AbstractSubStep,
)
Petrinetv3_Net_Run_AbstractSubStep_strategy = st.builds(
    Petrinetv3_Net_Run_AbstractSubStep,
)
Petrinetv3_Transition_Fire_strategy = st.builds(
    Petrinetv3_Transition_Fire,
)
Petrinetv3_Net_TickEnabledTransitions_strategy = st.builds(
    Petrinetv3_Net_TickEnabledTransitions,
)
Petrinetv3_Net_Run_strategy = st.builds(
    Petrinetv3_Net_Run,
)
Petrinetv3_Net_Initialize_strategy = st.builds(
    Petrinetv3_Net_Initialize,
)
petrinetv3Trace_Trace_strategy = st.builds(
    petrinetv3Trace_Trace,
)
petrinetv3_TracedPlace_strategy = st.builds(
    petrinetv3_TracedPlace,
)

@given(instance=petrinetv3Trace_petrinetv3_TracedTransition_strategy)
@settings(max_examples=50)
def test_petrinetv3trace_petrinetv3_tracedtransition_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace_petrinetv3_TracedTransition)

@given(instance=petrinetv3Trace_petrinetv3_TracedToken_strategy)
@settings(max_examples=50)
def test_petrinetv3trace_petrinetv3_tracedtoken_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace_petrinetv3_TracedToken)

@given(instance=petrinetv3_petrinetv3Trace_Token_strategy)
@settings(max_examples=50)
def test_petrinetv3_petrinetv3trace_token_instantiation(instance):
    assert isinstance(instance, petrinetv3_petrinetv3Trace_Token)

@given(instance=petrinetv3_petrinetv3Trace_Place_strategy)
@settings(max_examples=50)
def test_petrinetv3_petrinetv3trace_place_instantiation(instance):
    assert isinstance(instance, petrinetv3_petrinetv3Trace_Place)

@given(instance=petrinetv3Trace_petrinetv3_TracedPlace_strategy)
@settings(max_examples=50)
def test_petrinetv3trace_petrinetv3_tracedplace_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace_petrinetv3_TracedPlace)

@given(instance=petrinetv3Trace_States_Transition_clock_Value_strategy)
@settings(max_examples=50)
def test_petrinetv3trace_states_transition_clock_value_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace_States_Transition_clock_Value)



@given(instance=petrinetv3Trace_States_Transition_clock_Value_strategy)
def test_petrinetv3trace_states_transition_clock_value_clock_setter(instance):
    original = instance.clock
    instance.clock = original
    assert instance.clock == original

@given(instance=petrinetv3_petrinetv3Trace_Net_strategy)
@settings(max_examples=50)
def test_petrinetv3_petrinetv3trace_net_instantiation(instance):
    assert isinstance(instance, petrinetv3_petrinetv3Trace_Net)

@given(instance=petrinetv3_petrinetv3Trace_Transition_strategy)
@settings(max_examples=50)
def test_petrinetv3_petrinetv3trace_transition_instantiation(instance):
    assert isinstance(instance, petrinetv3_petrinetv3Trace_Transition)

@given(instance=petrinetv3Trace_States_Place_tokens_Value_strategy)
@settings(max_examples=50)
def test_petrinetv3trace_states_place_tokens_value_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace_States_Place_tokens_Value)

@given(instance=MSEOccurrence_strategy)
@settings(max_examples=50)
def test_mseoccurrence_instantiation(instance):
    assert isinstance(instance, MSEOccurrence)

@given(instance=petrinetv3Trace_Steps_Step_strategy)
@settings(max_examples=50)
def test_petrinetv3trace_steps_step_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace_Steps_Step)

@given(instance=SmallStep_strategy)
@settings(max_examples=50)
def test_smallstep_instantiation(instance):
    assert isinstance(instance, SmallStep)

@given(instance=petrinetv3Trace_Steps_RootImplicitStep_strategy)
@settings(max_examples=50)
def test_petrinetv3trace_steps_rootimplicitstep_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace_Steps_RootImplicitStep)

@given(instance=Transition_clock_Value_strategy)
@settings(max_examples=50)
def test_transition_clock_value_instantiation(instance):
    assert isinstance(instance, Transition_clock_Value)

@given(instance=Place_tokens_Value_strategy)
@settings(max_examples=50)
def test_place_tokens_value_instantiation(instance):
    assert isinstance(instance, Place_tokens_Value)

@given(instance=petrinetv3Trace_States_State_strategy)
@settings(max_examples=50)
def test_petrinetv3trace_states_state_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace_States_State)

@given(instance=BigStep_strategy)
@settings(max_examples=50)
def test_bigstep_instantiation(instance):
    assert isinstance(instance, BigStep)

@given(instance=petrinetv3Trace_Steps_Petrinetv3_Net_Run_strategy)
@settings(max_examples=50)
def test_petrinetv3trace_steps_petrinetv3_net_run_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace_Steps_Petrinetv3_Net_Run)

@given(instance=Steps_SmallStep_strategy)
@settings(max_examples=50)
def test_steps_smallstep_instantiation(instance):
    assert isinstance(instance, Steps_SmallStep)

@given(instance=Steps_Petrinetv3_Net_Run_AbstractSubStep_strategy)
@settings(max_examples=50)
def test_steps_petrinetv3_net_run_abstractsubstep_instantiation(instance):
    assert isinstance(instance, Steps_Petrinetv3_Net_Run_AbstractSubStep)

@given(instance=petrinetv3Trace_Steps_Petrinetv3_Net_Initialize_strategy)
@settings(max_examples=50)
def test_petrinetv3trace_steps_petrinetv3_net_initialize_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace_Steps_Petrinetv3_Net_Initialize)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=Step_strategy)
@settings(max_examples=50)
def test_step_instantiation(instance):
    assert isinstance(instance, Step)

@given(instance=petrinetv3Trace_Steps_BigStep_strategy)
@settings(max_examples=50)
def test_petrinetv3trace_steps_bigstep_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace_Steps_BigStep)

@given(instance=petrinetv3Trace_Steps_SmallStep_strategy)
@settings(max_examples=50)
def test_petrinetv3trace_steps_smallstep_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace_Steps_SmallStep)

@given(instance=petrinetv3_TracedTransition_strategy)
@settings(max_examples=50)
def test_petrinetv3_tracedtransition_instantiation(instance):
    assert isinstance(instance, petrinetv3_TracedTransition)

@given(instance=petrinetv3_TracedToken_strategy)
@settings(max_examples=50)
def test_petrinetv3_tracedtoken_instantiation(instance):
    assert isinstance(instance, petrinetv3_TracedToken)

@given(instance=petrinetv3Trace_Steps_Petrinetv3_Transition_Fire_strategy)
@settings(max_examples=50)
def test_petrinetv3trace_steps_petrinetv3_transition_fire_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace_Steps_Petrinetv3_Transition_Fire)

@given(instance=petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions_strategy)
@settings(max_examples=50)
def test_petrinetv3trace_steps_petrinetv3_net_tickenabledtransitions_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions)

@given(instance=petrinetv3Trace_Steps_Petrinetv3_Net_Run_ImplicitStep_strategy)
@settings(max_examples=50)
def test_petrinetv3trace_steps_petrinetv3_net_run_implicitstep_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace_Steps_Petrinetv3_Net_Run_ImplicitStep)

@given(instance=petrinetv3Trace_Steps_Petrinetv3_Net_Run_AbstractSubStep_strategy)
@settings(max_examples=50)
def test_petrinetv3trace_steps_petrinetv3_net_run_abstractsubstep_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace_Steps_Petrinetv3_Net_Run_AbstractSubStep)

@given(instance=Petrinetv3_Net_Run_AbstractSubStep_strategy)
@settings(max_examples=50)
def test_petrinetv3_net_run_abstractsubstep_instantiation(instance):
    assert isinstance(instance, Petrinetv3_Net_Run_AbstractSubStep)

@given(instance=Petrinetv3_Transition_Fire_strategy)
@settings(max_examples=50)
def test_petrinetv3_transition_fire_instantiation(instance):
    assert isinstance(instance, Petrinetv3_Transition_Fire)

@given(instance=Petrinetv3_Net_TickEnabledTransitions_strategy)
@settings(max_examples=50)
def test_petrinetv3_net_tickenabledtransitions_instantiation(instance):
    assert isinstance(instance, Petrinetv3_Net_TickEnabledTransitions)

@given(instance=Petrinetv3_Net_Run_strategy)
@settings(max_examples=50)
def test_petrinetv3_net_run_instantiation(instance):
    assert isinstance(instance, Petrinetv3_Net_Run)

@given(instance=Petrinetv3_Net_Initialize_strategy)
@settings(max_examples=50)
def test_petrinetv3_net_initialize_instantiation(instance):
    assert isinstance(instance, Petrinetv3_Net_Initialize)

@given(instance=petrinetv3Trace_Trace_strategy)
@settings(max_examples=50)
def test_petrinetv3trace_trace_instantiation(instance):
    assert isinstance(instance, petrinetv3Trace_Trace)

@given(instance=petrinetv3_TracedPlace_strategy)
@settings(max_examples=50)
def test_petrinetv3_tracedplace_instantiation(instance):
    assert isinstance(instance, petrinetv3_TracedPlace)
