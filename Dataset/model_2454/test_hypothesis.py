import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    cbmg_RequestParameter,
    cbmg_Transition,
    cbmg_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cbmg_requestparameter_is_not_abstract():
    assert not inspect.isabstract(cbmg_RequestParameter)


def test_cbmg_requestparameter_constructor_exists():
    assert callable(cbmg_RequestParameter.__init__)


def test_cbmg_requestparameter_constructor_args():
    sig = inspect.signature(cbmg_RequestParameter.__init__)
    params = list(sig.parameters.keys())
    assert "parameterName" in params, "Missing parameter 'parameterName'"
    assert "parameterValue" in params, "Missing parameter 'parameterValue'"

def test_cbmg_requestparameter_has_parameterName():
    assert hasattr(cbmg_RequestParameter, "parameterName")
    descriptor = None
    for klass in cbmg_RequestParameter.__mro__:
        if "parameterName" in klass.__dict__:
            descriptor = klass.__dict__["parameterName"]
            break
    assert isinstance(descriptor, property)

def test_cbmg_requestparameter_has_parameterValue():
    assert hasattr(cbmg_RequestParameter, "parameterValue")
    descriptor = None
    for klass in cbmg_RequestParameter.__mro__:
        if "parameterValue" in klass.__dict__:
            descriptor = klass.__dict__["parameterValue"]
            break
    assert isinstance(descriptor, property)



def test_cbmg_transition_is_not_abstract():
    assert not inspect.isabstract(cbmg_Transition)


def test_cbmg_transition_constructor_exists():
    assert callable(cbmg_Transition.__init__)


def test_cbmg_transition_constructor_args():
    sig = inspect.signature(cbmg_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "method" in params, "Missing parameter 'method'"
    assert "accept" in params, "Missing parameter 'accept'"
    assert "probability" in params, "Missing parameter 'probability'"
    assert "thinkTime" in params, "Missing parameter 'thinkTime'"
    assert "nbrOfTransitions" in params, "Missing parameter 'nbrOfTransitions'"
    assert "condition" in params, "Missing parameter 'condition'"

def test_cbmg_transition_has_method():
    assert hasattr(cbmg_Transition, "method")
    descriptor = None
    for klass in cbmg_Transition.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)

def test_cbmg_transition_has_accept():
    assert hasattr(cbmg_Transition, "accept")
    descriptor = None
    for klass in cbmg_Transition.__mro__:
        if "accept" in klass.__dict__:
            descriptor = klass.__dict__["accept"]
            break
    assert isinstance(descriptor, property)

def test_cbmg_transition_has_probability():
    assert hasattr(cbmg_Transition, "probability")
    descriptor = None
    for klass in cbmg_Transition.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)

def test_cbmg_transition_has_thinkTime():
    assert hasattr(cbmg_Transition, "thinkTime")
    descriptor = None
    for klass in cbmg_Transition.__mro__:
        if "thinkTime" in klass.__dict__:
            descriptor = klass.__dict__["thinkTime"]
            break
    assert isinstance(descriptor, property)

def test_cbmg_transition_has_nbrOfTransitions():
    assert hasattr(cbmg_Transition, "nbrOfTransitions")
    descriptor = None
    for klass in cbmg_Transition.__mro__:
        if "nbrOfTransitions" in klass.__dict__:
            descriptor = klass.__dict__["nbrOfTransitions"]
            break
    assert isinstance(descriptor, property)

def test_cbmg_transition_has_condition():
    assert hasattr(cbmg_Transition, "condition")
    descriptor = None
    for klass in cbmg_Transition.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_cbmg_state_is_not_abstract():
    assert not inspect.isabstract(cbmg_State)


def test_cbmg_state_constructor_exists():
    assert callable(cbmg_State.__init__)


def test_cbmg_state_constructor_args():
    sig = inspect.signature(cbmg_State.__init__)
    params = list(sig.parameters.keys())
    assert "isStartState" in params, "Missing parameter 'isStartState'"
    assert "localName" in params, "Missing parameter 'localName'"
    assert "isEndState" in params, "Missing parameter 'isEndState'"
    assert "requestURL" in params, "Missing parameter 'requestURL'"
    assert "port" in params, "Missing parameter 'port'"
    assert "localAddr" in params, "Missing parameter 'localAddr'"

def test_cbmg_state_has_isStartState():
    assert hasattr(cbmg_State, "isStartState")
    descriptor = None
    for klass in cbmg_State.__mro__:
        if "isStartState" in klass.__dict__:
            descriptor = klass.__dict__["isStartState"]
            break
    assert isinstance(descriptor, property)

def test_cbmg_state_has_localName():
    assert hasattr(cbmg_State, "localName")
    descriptor = None
    for klass in cbmg_State.__mro__:
        if "localName" in klass.__dict__:
            descriptor = klass.__dict__["localName"]
            break
    assert isinstance(descriptor, property)

def test_cbmg_state_has_isEndState():
    assert hasattr(cbmg_State, "isEndState")
    descriptor = None
    for klass in cbmg_State.__mro__:
        if "isEndState" in klass.__dict__:
            descriptor = klass.__dict__["isEndState"]
            break
    assert isinstance(descriptor, property)

def test_cbmg_state_has_requestURL():
    assert hasattr(cbmg_State, "requestURL")
    descriptor = None
    for klass in cbmg_State.__mro__:
        if "requestURL" in klass.__dict__:
            descriptor = klass.__dict__["requestURL"]
            break
    assert isinstance(descriptor, property)

def test_cbmg_state_has_port():
    assert hasattr(cbmg_State, "port")
    descriptor = None
    for klass in cbmg_State.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)

def test_cbmg_state_has_localAddr():
    assert hasattr(cbmg_State, "localAddr")
    descriptor = None
    for klass in cbmg_State.__mro__:
        if "localAddr" in klass.__dict__:
            descriptor = klass.__dict__["localAddr"]
            break
    assert isinstance(descriptor, property)


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
cbmg_RequestParameter_strategy = st.builds(
    cbmg_RequestParameter,
    parameterName=
        safe_text,
    parameterValue=
        safe_text
)
cbmg_Transition_strategy = st.builds(
    cbmg_Transition,
    method=
        safe_text,
    accept=
        safe_text,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    thinkTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    nbrOfTransitions=
        st.integers(),
    condition=
        safe_text
)
cbmg_State_strategy = st.builds(
    cbmg_State,
    isStartState=
        st.booleans(),
    localName=
        safe_text,
    isEndState=
        st.booleans(),
    requestURL=
        safe_text,
    port=
        st.integers(),
    localAddr=
        safe_text
)

@given(instance=cbmg_RequestParameter_strategy)
@settings(max_examples=50)
def test_cbmg_requestparameter_instantiation(instance):
    assert isinstance(instance, cbmg_RequestParameter)



@given(instance=cbmg_RequestParameter_strategy)
def test_cbmg_requestparameter_parameterName_setter(instance):
    original = instance.parameterName
    instance.parameterName = original
    assert instance.parameterName == original



@given(instance=cbmg_RequestParameter_strategy)
def test_cbmg_requestparameter_parameterValue_setter(instance):
    original = instance.parameterValue
    instance.parameterValue = original
    assert instance.parameterValue == original

@given(instance=cbmg_Transition_strategy)
@settings(max_examples=50)
def test_cbmg_transition_instantiation(instance):
    assert isinstance(instance, cbmg_Transition)



@given(instance=cbmg_Transition_strategy)
def test_cbmg_transition_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original



@given(instance=cbmg_Transition_strategy)
def test_cbmg_transition_accept_setter(instance):
    original = instance.accept
    instance.accept = original
    assert instance.accept == original



@given(instance=cbmg_Transition_strategy)
def test_cbmg_transition_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original



@given(instance=cbmg_Transition_strategy)
def test_cbmg_transition_thinkTime_setter(instance):
    original = instance.thinkTime
    instance.thinkTime = original
    assert instance.thinkTime == original



@given(instance=cbmg_Transition_strategy)
def test_cbmg_transition_nbrOfTransitions_setter(instance):
    original = instance.nbrOfTransitions
    instance.nbrOfTransitions = original
    assert instance.nbrOfTransitions == original



@given(instance=cbmg_Transition_strategy)
def test_cbmg_transition_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=cbmg_State_strategy)
@settings(max_examples=50)
def test_cbmg_state_instantiation(instance):
    assert isinstance(instance, cbmg_State)



@given(instance=cbmg_State_strategy)
def test_cbmg_state_isStartState_setter(instance):
    original = instance.isStartState
    instance.isStartState = original
    assert instance.isStartState == original



@given(instance=cbmg_State_strategy)
def test_cbmg_state_localName_setter(instance):
    original = instance.localName
    instance.localName = original
    assert instance.localName == original



@given(instance=cbmg_State_strategy)
def test_cbmg_state_isEndState_setter(instance):
    original = instance.isEndState
    instance.isEndState = original
    assert instance.isEndState == original



@given(instance=cbmg_State_strategy)
def test_cbmg_state_requestURL_setter(instance):
    original = instance.requestURL
    instance.requestURL = original
    assert instance.requestURL == original



@given(instance=cbmg_State_strategy)
def test_cbmg_state_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original



@given(instance=cbmg_State_strategy)
def test_cbmg_state_localAddr_setter(instance):
    original = instance.localAddr
    instance.localAddr = original
    assert instance.localAddr == original
