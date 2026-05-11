import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ParameterizedActionstep,
    actionpak1::ScheduleSaflet,
    actionpak1::InvokeSaflet2,
    call::CallSource1,
    actionstep::ParameterizedInitiator,
    actionpak1::IncomingCall2,
    ParameterizedInitiator,
    actionpak1::CustomInitiator,
    DynamicValue,
    ActionStep,
    actionpak1::UnscheduleSaflet,
    actionpak1::ActionstepTest,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_parameterizedactionstep_is_not_abstract():
    assert not inspect.isabstract(ParameterizedActionstep)


def test_parameterizedactionstep_constructor_exists():
    assert callable(ParameterizedActionstep.__init__)


def test_parameterizedactionstep_constructor_args():
    sig = inspect.signature(ParameterizedActionstep.__init__)
    params = list(sig.parameters.keys())



def test_actionpak1::schedulesaflet_is_not_abstract():
    assert not inspect.isabstract(actionpak1::ScheduleSaflet)


def test_actionpak1::schedulesaflet_constructor_exists():
    assert callable(actionpak1::ScheduleSaflet.__init__)


def test_actionpak1::schedulesaflet_constructor_args():
    sig = inspect.signature(actionpak1::ScheduleSaflet.__init__)
    params = list(sig.parameters.keys())



def test_actionpak1::invokesaflet2_is_not_abstract():
    assert not inspect.isabstract(actionpak1::InvokeSaflet2)


def test_actionpak1::invokesaflet2_constructor_exists():
    assert callable(actionpak1::InvokeSaflet2.__init__)


def test_actionpak1::invokesaflet2_constructor_args():
    sig = inspect.signature(actionpak1::InvokeSaflet2.__init__)
    params = list(sig.parameters.keys())
    assert "labelText" in params, "Missing parameter 'labelText'"

def test_actionpak1::invokesaflet2_has_labelText():
    assert hasattr(actionpak1::InvokeSaflet2, "labelText")
    descriptor = None
    for klass in actionpak1::InvokeSaflet2.__mro__:
        if "labelText" in klass.__dict__:
            descriptor = klass.__dict__["labelText"]
            break
    assert isinstance(descriptor, property)



def test_call::callsource1_is_not_abstract():
    assert not inspect.isabstract(call::CallSource1)


def test_call::callsource1_constructor_exists():
    assert callable(call::CallSource1.__init__)


def test_call::callsource1_constructor_args():
    sig = inspect.signature(call::CallSource1.__init__)
    params = list(sig.parameters.keys())



def test_actionstep::parameterizedinitiator_is_not_abstract():
    assert not inspect.isabstract(actionstep::ParameterizedInitiator)


def test_actionstep::parameterizedinitiator_constructor_exists():
    assert callable(actionstep::ParameterizedInitiator.__init__)


def test_actionstep::parameterizedinitiator_constructor_args():
    sig = inspect.signature(actionstep::ParameterizedInitiator.__init__)
    params = list(sig.parameters.keys())



def test_actionpak1::incomingcall2_is_not_abstract():
    assert not inspect.isabstract(actionpak1::IncomingCall2)


def test_actionpak1::incomingcall2_constructor_exists():
    assert callable(actionpak1::IncomingCall2.__init__)


def test_actionpak1::incomingcall2_constructor_args():
    sig = inspect.signature(actionpak1::IncomingCall2.__init__)
    params = list(sig.parameters.keys())
    assert "callName" in params, "Missing parameter 'callName'"

def test_actionpak1::incomingcall2_has_callName():
    assert hasattr(actionpak1::IncomingCall2, "callName")
    descriptor = None
    for klass in actionpak1::IncomingCall2.__mro__:
        if "callName" in klass.__dict__:
            descriptor = klass.__dict__["callName"]
            break
    assert isinstance(descriptor, property)



def test_parameterizedinitiator_is_not_abstract():
    assert not inspect.isabstract(ParameterizedInitiator)


def test_parameterizedinitiator_constructor_exists():
    assert callable(ParameterizedInitiator.__init__)


def test_parameterizedinitiator_constructor_args():
    sig = inspect.signature(ParameterizedInitiator.__init__)
    params = list(sig.parameters.keys())



def test_actionpak1::custominitiator_is_not_abstract():
    assert not inspect.isabstract(actionpak1::CustomInitiator)


def test_actionpak1::custominitiator_constructor_exists():
    assert callable(actionpak1::CustomInitiator.__init__)


def test_actionpak1::custominitiator_constructor_args():
    sig = inspect.signature(actionpak1::CustomInitiator.__init__)
    params = list(sig.parameters.keys())



def test_dynamicvalue_is_not_abstract():
    assert not inspect.isabstract(DynamicValue)


def test_dynamicvalue_constructor_exists():
    assert callable(DynamicValue.__init__)


def test_dynamicvalue_constructor_args():
    sig = inspect.signature(DynamicValue.__init__)
    params = list(sig.parameters.keys())



def test_actionstep_is_not_abstract():
    assert not inspect.isabstract(ActionStep)


def test_actionstep_constructor_exists():
    assert callable(ActionStep.__init__)


def test_actionstep_constructor_args():
    sig = inspect.signature(ActionStep.__init__)
    params = list(sig.parameters.keys())



def test_actionpak1::unschedulesaflet_is_not_abstract():
    assert not inspect.isabstract(actionpak1::UnscheduleSaflet)


def test_actionpak1::unschedulesaflet_constructor_exists():
    assert callable(actionpak1::UnscheduleSaflet.__init__)


def test_actionpak1::unschedulesaflet_constructor_args():
    sig = inspect.signature(actionpak1::UnscheduleSaflet.__init__)
    params = list(sig.parameters.keys())



def test_actionpak1::actionsteptest_is_not_abstract():
    assert not inspect.isabstract(actionpak1::ActionstepTest)


def test_actionpak1::actionsteptest_constructor_exists():
    assert callable(actionpak1::ActionstepTest.__init__)


def test_actionpak1::actionsteptest_constructor_args():
    sig = inspect.signature(actionpak1::ActionstepTest.__init__)
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
ParameterizedActionstep_strategy = st.builds(
    ParameterizedActionstep,
)
actionpak1::ScheduleSaflet_strategy = st.builds(
    actionpak1::ScheduleSaflet,
)
actionpak1::InvokeSaflet2_strategy = st.builds(
    actionpak1::InvokeSaflet2,
    labelText=
        safe_text
)
call::CallSource1_strategy = st.builds(
    call::CallSource1,
)
actionstep::ParameterizedInitiator_strategy = st.builds(
    actionstep::ParameterizedInitiator,
)
actionpak1::IncomingCall2_strategy = st.builds(
    actionpak1::IncomingCall2,
    callName=
        safe_text
)
ParameterizedInitiator_strategy = st.builds(
    ParameterizedInitiator,
)
actionpak1::CustomInitiator_strategy = st.builds(
    actionpak1::CustomInitiator,
)
DynamicValue_strategy = st.builds(
    DynamicValue,
)
ActionStep_strategy = st.builds(
    ActionStep,
)
actionpak1::UnscheduleSaflet_strategy = st.builds(
    actionpak1::UnscheduleSaflet,
)
actionpak1::ActionstepTest_strategy = st.builds(
    actionpak1::ActionstepTest,
)

@given(instance=ParameterizedActionstep_strategy)
@settings(max_examples=50)
def test_parameterizedactionstep_instantiation(instance):
    assert isinstance(instance, ParameterizedActionstep)

@given(instance=actionpak1::ScheduleSaflet_strategy)
@settings(max_examples=50)
def test_actionpak1::schedulesaflet_instantiation(instance):
    assert isinstance(instance, actionpak1::ScheduleSaflet)

@given(instance=actionpak1::InvokeSaflet2_strategy)
@settings(max_examples=50)
def test_actionpak1::invokesaflet2_instantiation(instance):
    assert isinstance(instance, actionpak1::InvokeSaflet2)

@given(instance=actionpak1::InvokeSaflet2_strategy)
def test_actionpak1::invokesaflet2_labelText_type(instance):
    assert isinstance(instance.labelText, str)


@given(instance=actionpak1::InvokeSaflet2_strategy)
def test_actionpak1::invokesaflet2_labelText_setter(instance):
    original = instance.labelText
    instance.labelText = original
    assert instance.labelText == original

@given(instance=call::CallSource1_strategy)
@settings(max_examples=50)
def test_call::callsource1_instantiation(instance):
    assert isinstance(instance, call::CallSource1)

@given(instance=actionstep::ParameterizedInitiator_strategy)
@settings(max_examples=50)
def test_actionstep::parameterizedinitiator_instantiation(instance):
    assert isinstance(instance, actionstep::ParameterizedInitiator)

@given(instance=actionpak1::IncomingCall2_strategy)
@settings(max_examples=50)
def test_actionpak1::incomingcall2_instantiation(instance):
    assert isinstance(instance, actionpak1::IncomingCall2)

@given(instance=actionpak1::IncomingCall2_strategy)
def test_actionpak1::incomingcall2_callName_type(instance):
    assert isinstance(instance.callName, str)


@given(instance=actionpak1::IncomingCall2_strategy)
def test_actionpak1::incomingcall2_callName_setter(instance):
    original = instance.callName
    instance.callName = original
    assert instance.callName == original

@given(instance=ParameterizedInitiator_strategy)
@settings(max_examples=50)
def test_parameterizedinitiator_instantiation(instance):
    assert isinstance(instance, ParameterizedInitiator)

@given(instance=actionpak1::CustomInitiator_strategy)
@settings(max_examples=50)
def test_actionpak1::custominitiator_instantiation(instance):
    assert isinstance(instance, actionpak1::CustomInitiator)

@given(instance=DynamicValue_strategy)
@settings(max_examples=50)
def test_dynamicvalue_instantiation(instance):
    assert isinstance(instance, DynamicValue)

@given(instance=ActionStep_strategy)
@settings(max_examples=50)
def test_actionstep_instantiation(instance):
    assert isinstance(instance, ActionStep)

@given(instance=actionpak1::UnscheduleSaflet_strategy)
@settings(max_examples=50)
def test_actionpak1::unschedulesaflet_instantiation(instance):
    assert isinstance(instance, actionpak1::UnscheduleSaflet)

@given(instance=actionpak1::ActionstepTest_strategy)
@settings(max_examples=50)
def test_actionpak1::actionsteptest_instantiation(instance):
    assert isinstance(instance, actionpak1::ActionstepTest)
