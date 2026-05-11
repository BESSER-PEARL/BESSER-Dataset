import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    cbmg::RequestParameter,
    cbmg::Transition,
    cbmg::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cbmg::requestparameter_is_not_abstract():
    assert not inspect.isabstract(cbmg::RequestParameter)


def test_cbmg::requestparameter_constructor_exists():
    assert callable(cbmg::RequestParameter.__init__)


def test_cbmg::requestparameter_constructor_args():
    sig = inspect.signature(cbmg::RequestParameter.__init__)
    params = list(sig.parameters.keys())
    assert "parameterValue" in params, "Missing parameter 'parameterValue'"
    assert "parameterName" in params, "Missing parameter 'parameterName'"

def test_cbmg::requestparameter_has_parameterValue():
    assert hasattr(cbmg::RequestParameter, "parameterValue")
    descriptor = None
    for klass in cbmg::RequestParameter.__mro__:
        if "parameterValue" in klass.__dict__:
            descriptor = klass.__dict__["parameterValue"]
            break
    assert isinstance(descriptor, property)

def test_cbmg::requestparameter_has_parameterName():
    assert hasattr(cbmg::RequestParameter, "parameterName")
    descriptor = None
    for klass in cbmg::RequestParameter.__mro__:
        if "parameterName" in klass.__dict__:
            descriptor = klass.__dict__["parameterName"]
            break
    assert isinstance(descriptor, property)



def test_cbmg::transition_is_not_abstract():
    assert not inspect.isabstract(cbmg::Transition)


def test_cbmg::transition_constructor_exists():
    assert callable(cbmg::Transition.__init__)


def test_cbmg::transition_constructor_args():
    sig = inspect.signature(cbmg::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "method" in params, "Missing parameter 'method'"
    assert "thinkTime" in params, "Missing parameter 'thinkTime'"
    assert "accept" in params, "Missing parameter 'accept'"
    assert "nbrOfTransitions" in params, "Missing parameter 'nbrOfTransitions'"
    assert "probability" in params, "Missing parameter 'probability'"
    assert "condition" in params, "Missing parameter 'condition'"

def test_cbmg::transition_has_method():
    assert hasattr(cbmg::Transition, "method")
    descriptor = None
    for klass in cbmg::Transition.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)

def test_cbmg::transition_has_thinkTime():
    assert hasattr(cbmg::Transition, "thinkTime")
    descriptor = None
    for klass in cbmg::Transition.__mro__:
        if "thinkTime" in klass.__dict__:
            descriptor = klass.__dict__["thinkTime"]
            break
    assert isinstance(descriptor, property)

def test_cbmg::transition_has_accept():
    assert hasattr(cbmg::Transition, "accept")
    descriptor = None
    for klass in cbmg::Transition.__mro__:
        if "accept" in klass.__dict__:
            descriptor = klass.__dict__["accept"]
            break
    assert isinstance(descriptor, property)

def test_cbmg::transition_has_nbrOfTransitions():
    assert hasattr(cbmg::Transition, "nbrOfTransitions")
    descriptor = None
    for klass in cbmg::Transition.__mro__:
        if "nbrOfTransitions" in klass.__dict__:
            descriptor = klass.__dict__["nbrOfTransitions"]
            break
    assert isinstance(descriptor, property)

def test_cbmg::transition_has_probability():
    assert hasattr(cbmg::Transition, "probability")
    descriptor = None
    for klass in cbmg::Transition.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)

def test_cbmg::transition_has_condition():
    assert hasattr(cbmg::Transition, "condition")
    descriptor = None
    for klass in cbmg::Transition.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_cbmg::state_is_not_abstract():
    assert not inspect.isabstract(cbmg::State)


def test_cbmg::state_constructor_exists():
    assert callable(cbmg::State.__init__)


def test_cbmg::state_constructor_args():
    sig = inspect.signature(cbmg::State.__init__)
    params = list(sig.parameters.keys())
    assert "localName" in params, "Missing parameter 'localName'"
    assert "isEndState" in params, "Missing parameter 'isEndState'"
    assert "localAddr" in params, "Missing parameter 'localAddr'"
    assert "isStartState" in params, "Missing parameter 'isStartState'"
    assert "port" in params, "Missing parameter 'port'"
    assert "requestURL" in params, "Missing parameter 'requestURL'"

def test_cbmg::state_has_localName():
    assert hasattr(cbmg::State, "localName")
    descriptor = None
    for klass in cbmg::State.__mro__:
        if "localName" in klass.__dict__:
            descriptor = klass.__dict__["localName"]
            break
    assert isinstance(descriptor, property)

def test_cbmg::state_has_isEndState():
    assert hasattr(cbmg::State, "isEndState")
    descriptor = None
    for klass in cbmg::State.__mro__:
        if "isEndState" in klass.__dict__:
            descriptor = klass.__dict__["isEndState"]
            break
    assert isinstance(descriptor, property)

def test_cbmg::state_has_localAddr():
    assert hasattr(cbmg::State, "localAddr")
    descriptor = None
    for klass in cbmg::State.__mro__:
        if "localAddr" in klass.__dict__:
            descriptor = klass.__dict__["localAddr"]
            break
    assert isinstance(descriptor, property)

def test_cbmg::state_has_isStartState():
    assert hasattr(cbmg::State, "isStartState")
    descriptor = None
    for klass in cbmg::State.__mro__:
        if "isStartState" in klass.__dict__:
            descriptor = klass.__dict__["isStartState"]
            break
    assert isinstance(descriptor, property)

def test_cbmg::state_has_port():
    assert hasattr(cbmg::State, "port")
    descriptor = None
    for klass in cbmg::State.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)

def test_cbmg::state_has_requestURL():
    assert hasattr(cbmg::State, "requestURL")
    descriptor = None
    for klass in cbmg::State.__mro__:
        if "requestURL" in klass.__dict__:
            descriptor = klass.__dict__["requestURL"]
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
cbmg::RequestParameter_strategy = st.builds(
    cbmg::RequestParameter,
    parameterValue=
        safe_text,
    parameterName=
        safe_text
)
cbmg::Transition_strategy = st.builds(
    cbmg::Transition,
    method=
        safe_text,
    thinkTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    accept=
        safe_text,
    nbrOfTransitions=
        st.integers(),
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    condition=
        safe_text
)
cbmg::State_strategy = st.builds(
    cbmg::State,
    localName=
        safe_text,
    isEndState=
        st.booleans(),
    localAddr=
        safe_text,
    isStartState=
        st.booleans(),
    port=
        st.integers(),
    requestURL=
        safe_text
)

@given(instance=cbmg::RequestParameter_strategy)
@settings(max_examples=50)
def test_cbmg::requestparameter_instantiation(instance):
    assert isinstance(instance, cbmg::RequestParameter)

@given(instance=cbmg::RequestParameter_strategy)
def test_cbmg::requestparameter_parameterValue_type(instance):
    assert isinstance(instance.parameterValue, str)


@given(instance=cbmg::RequestParameter_strategy)
def test_cbmg::requestparameter_parameterValue_setter(instance):
    original = instance.parameterValue
    instance.parameterValue = original
    assert instance.parameterValue == original

@given(instance=cbmg::RequestParameter_strategy)
def test_cbmg::requestparameter_parameterName_type(instance):
    assert isinstance(instance.parameterName, str)


@given(instance=cbmg::RequestParameter_strategy)
def test_cbmg::requestparameter_parameterName_setter(instance):
    original = instance.parameterName
    instance.parameterName = original
    assert instance.parameterName == original

@given(instance=cbmg::Transition_strategy)
@settings(max_examples=50)
def test_cbmg::transition_instantiation(instance):
    assert isinstance(instance, cbmg::Transition)

@given(instance=cbmg::Transition_strategy)
def test_cbmg::transition_method_type(instance):
    assert isinstance(instance.method, str)


@given(instance=cbmg::Transition_strategy)
def test_cbmg::transition_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=cbmg::Transition_strategy)
def test_cbmg::transition_thinkTime_type(instance):
    assert isinstance(instance.thinkTime, float)


@given(instance=cbmg::Transition_strategy)
def test_cbmg::transition_thinkTime_setter(instance):
    original = instance.thinkTime
    instance.thinkTime = original
    assert instance.thinkTime == original

@given(instance=cbmg::Transition_strategy)
def test_cbmg::transition_accept_type(instance):
    assert isinstance(instance.accept, str)


@given(instance=cbmg::Transition_strategy)
def test_cbmg::transition_accept_setter(instance):
    original = instance.accept
    instance.accept = original
    assert instance.accept == original

@given(instance=cbmg::Transition_strategy)
def test_cbmg::transition_nbrOfTransitions_type(instance):
    assert isinstance(instance.nbrOfTransitions, int)


@given(instance=cbmg::Transition_strategy)
def test_cbmg::transition_nbrOfTransitions_setter(instance):
    original = instance.nbrOfTransitions
    instance.nbrOfTransitions = original
    assert instance.nbrOfTransitions == original

@given(instance=cbmg::Transition_strategy)
def test_cbmg::transition_probability_type(instance):
    assert isinstance(instance.probability, float)


@given(instance=cbmg::Transition_strategy)
def test_cbmg::transition_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=cbmg::Transition_strategy)
def test_cbmg::transition_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=cbmg::Transition_strategy)
def test_cbmg::transition_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=cbmg::State_strategy)
@settings(max_examples=50)
def test_cbmg::state_instantiation(instance):
    assert isinstance(instance, cbmg::State)

@given(instance=cbmg::State_strategy)
def test_cbmg::state_localName_type(instance):
    assert isinstance(instance.localName, str)


@given(instance=cbmg::State_strategy)
def test_cbmg::state_localName_setter(instance):
    original = instance.localName
    instance.localName = original
    assert instance.localName == original

@given(instance=cbmg::State_strategy)
def test_cbmg::state_isEndState_type(instance):
    assert isinstance(instance.isEndState, bool)


@given(instance=cbmg::State_strategy)
def test_cbmg::state_isEndState_setter(instance):
    original = instance.isEndState
    instance.isEndState = original
    assert instance.isEndState == original

@given(instance=cbmg::State_strategy)
def test_cbmg::state_localAddr_type(instance):
    assert isinstance(instance.localAddr, str)


@given(instance=cbmg::State_strategy)
def test_cbmg::state_localAddr_setter(instance):
    original = instance.localAddr
    instance.localAddr = original
    assert instance.localAddr == original

@given(instance=cbmg::State_strategy)
def test_cbmg::state_isStartState_type(instance):
    assert isinstance(instance.isStartState, bool)


@given(instance=cbmg::State_strategy)
def test_cbmg::state_isStartState_setter(instance):
    original = instance.isStartState
    instance.isStartState = original
    assert instance.isStartState == original

@given(instance=cbmg::State_strategy)
def test_cbmg::state_port_type(instance):
    assert isinstance(instance.port, int)


@given(instance=cbmg::State_strategy)
def test_cbmg::state_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=cbmg::State_strategy)
def test_cbmg::state_requestURL_type(instance):
    assert isinstance(instance.requestURL, str)


@given(instance=cbmg::State_strategy)
def test_cbmg::state_requestURL_setter(instance):
    original = instance.requestURL
    instance.requestURL = original
    assert instance.requestURL == original
