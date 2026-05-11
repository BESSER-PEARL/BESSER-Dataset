import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Behaviour::TransitionFunction,
    Transition,
    Behaviour::StochasticTransition,
    Behaviour::ConditionalTransition,
    Place,
    Behaviour::StartPlace,
    Behaviour::Server,
    Behaviour::WaitingLine,
    Behaviour::QueuePlace,
    Behaviour::DefaultPlace,
    Connection,
    Behaviour::PreTransitionConnection,
    Behaviour::PostTransitionConnection,
    Identifier,
    Behaviour::Connection,
    Behaviour::Transition,
    Behaviour::Description,
    Behaviour::Colour,
    Behaviour::Token,
    Behaviour::Place,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_behaviour::transitionfunction_is_not_abstract():
    assert not inspect.isabstract(Behaviour::TransitionFunction)


def test_behaviour::transitionfunction_constructor_exists():
    assert callable(Behaviour::TransitionFunction.__init__)


def test_behaviour::transitionfunction_constructor_args():
    sig = inspect.signature(Behaviour::TransitionFunction.__init__)
    params = list(sig.parameters.keys())
    assert "transitionFunction" in params, "Missing parameter 'transitionFunction'"

def test_behaviour::transitionfunction_has_transitionFunction():
    assert hasattr(Behaviour::TransitionFunction, "transitionFunction")
    descriptor = None
    for klass in Behaviour::TransitionFunction.__mro__:
        if "transitionFunction" in klass.__dict__:
            descriptor = klass.__dict__["transitionFunction"]
            break
    assert isinstance(descriptor, property)



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::stochastictransition_is_not_abstract():
    assert not inspect.isabstract(Behaviour::StochasticTransition)


def test_behaviour::stochastictransition_constructor_exists():
    assert callable(Behaviour::StochasticTransition.__init__)


def test_behaviour::stochastictransition_constructor_args():
    sig = inspect.signature(Behaviour::StochasticTransition.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::conditionaltransition_is_not_abstract():
    assert not inspect.isabstract(Behaviour::ConditionalTransition)


def test_behaviour::conditionaltransition_constructor_exists():
    assert callable(Behaviour::ConditionalTransition.__init__)


def test_behaviour::conditionaltransition_constructor_args():
    sig = inspect.signature(Behaviour::ConditionalTransition.__init__)
    params = list(sig.parameters.keys())



def test_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_place_constructor_exists():
    assert callable(Place.__init__)


def test_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::startplace_is_not_abstract():
    assert not inspect.isabstract(Behaviour::StartPlace)


def test_behaviour::startplace_constructor_exists():
    assert callable(Behaviour::StartPlace.__init__)


def test_behaviour::startplace_constructor_args():
    sig = inspect.signature(Behaviour::StartPlace.__init__)
    params = list(sig.parameters.keys())
    assert "spawnPolicy" in params, "Missing parameter 'spawnPolicy'"

def test_behaviour::startplace_has_spawnPolicy():
    assert hasattr(Behaviour::StartPlace, "spawnPolicy")
    descriptor = None
    for klass in Behaviour::StartPlace.__mro__:
        if "spawnPolicy" in klass.__dict__:
            descriptor = klass.__dict__["spawnPolicy"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::server_is_not_abstract():
    assert not inspect.isabstract(Behaviour::Server)


def test_behaviour::server_constructor_exists():
    assert callable(Behaviour::Server.__init__)


def test_behaviour::server_constructor_args():
    sig = inspect.signature(Behaviour::Server.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_behaviour::server_has_capacity():
    assert hasattr(Behaviour::Server, "capacity")
    descriptor = None
    for klass in Behaviour::Server.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::waitingline_is_not_abstract():
    assert not inspect.isabstract(Behaviour::WaitingLine)


def test_behaviour::waitingline_constructor_exists():
    assert callable(Behaviour::WaitingLine.__init__)


def test_behaviour::waitingline_constructor_args():
    sig = inspect.signature(Behaviour::WaitingLine.__init__)
    params = list(sig.parameters.keys())
    assert "schedulingPolicy" in params, "Missing parameter 'schedulingPolicy'"

def test_behaviour::waitingline_has_schedulingPolicy():
    assert hasattr(Behaviour::WaitingLine, "schedulingPolicy")
    descriptor = None
    for klass in Behaviour::WaitingLine.__mro__:
        if "schedulingPolicy" in klass.__dict__:
            descriptor = klass.__dict__["schedulingPolicy"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::queueplace_is_not_abstract():
    assert not inspect.isabstract(Behaviour::QueuePlace)


def test_behaviour::queueplace_constructor_exists():
    assert callable(Behaviour::QueuePlace.__init__)


def test_behaviour::queueplace_constructor_args():
    sig = inspect.signature(Behaviour::QueuePlace.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::defaultplace_is_not_abstract():
    assert not inspect.isabstract(Behaviour::DefaultPlace)


def test_behaviour::defaultplace_constructor_exists():
    assert callable(Behaviour::DefaultPlace.__init__)


def test_behaviour::defaultplace_constructor_args():
    sig = inspect.signature(Behaviour::DefaultPlace.__init__)
    params = list(sig.parameters.keys())



def test_connection_is_not_abstract():
    assert not inspect.isabstract(Connection)


def test_connection_constructor_exists():
    assert callable(Connection.__init__)


def test_connection_constructor_args():
    sig = inspect.signature(Connection.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::pretransitionconnection_is_not_abstract():
    assert not inspect.isabstract(Behaviour::PreTransitionConnection)


def test_behaviour::pretransitionconnection_constructor_exists():
    assert callable(Behaviour::PreTransitionConnection.__init__)


def test_behaviour::pretransitionconnection_constructor_args():
    sig = inspect.signature(Behaviour::PreTransitionConnection.__init__)
    params = list(sig.parameters.keys())
    assert "requiredTokenAmount" in params, "Missing parameter 'requiredTokenAmount'"

def test_behaviour::pretransitionconnection_has_requiredTokenAmount():
    assert hasattr(Behaviour::PreTransitionConnection, "requiredTokenAmount")
    descriptor = None
    for klass in Behaviour::PreTransitionConnection.__mro__:
        if "requiredTokenAmount" in klass.__dict__:
            descriptor = klass.__dict__["requiredTokenAmount"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::posttransitionconnection_is_not_abstract():
    assert not inspect.isabstract(Behaviour::PostTransitionConnection)


def test_behaviour::posttransitionconnection_constructor_exists():
    assert callable(Behaviour::PostTransitionConnection.__init__)


def test_behaviour::posttransitionconnection_constructor_args():
    sig = inspect.signature(Behaviour::PostTransitionConnection.__init__)
    params = list(sig.parameters.keys())



def test_identifier_is_not_abstract():
    assert not inspect.isabstract(Identifier)


def test_identifier_constructor_exists():
    assert callable(Identifier.__init__)


def test_identifier_constructor_args():
    sig = inspect.signature(Identifier.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::connection_is_not_abstract():
    assert not inspect.isabstract(Behaviour::Connection)


def test_behaviour::connection_constructor_exists():
    assert callable(Behaviour::Connection.__init__)


def test_behaviour::connection_constructor_args():
    sig = inspect.signature(Behaviour::Connection.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::transition_is_not_abstract():
    assert not inspect.isabstract(Behaviour::Transition)


def test_behaviour::transition_constructor_exists():
    assert callable(Behaviour::Transition.__init__)


def test_behaviour::transition_constructor_args():
    sig = inspect.signature(Behaviour::Transition.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::description_is_not_abstract():
    assert not inspect.isabstract(Behaviour::Description)


def test_behaviour::description_constructor_exists():
    assert callable(Behaviour::Description.__init__)


def test_behaviour::description_constructor_args():
    sig = inspect.signature(Behaviour::Description.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::colour_is_not_abstract():
    assert not inspect.isabstract(Behaviour::Colour)


def test_behaviour::colour_constructor_exists():
    assert callable(Behaviour::Colour.__init__)


def test_behaviour::colour_constructor_args():
    sig = inspect.signature(Behaviour::Colour.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_behaviour::colour_has_attribute():
    assert hasattr(Behaviour::Colour, "attribute")
    descriptor = None
    for klass in Behaviour::Colour.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::token_is_not_abstract():
    assert not inspect.isabstract(Behaviour::Token)


def test_behaviour::token_constructor_exists():
    assert callable(Behaviour::Token.__init__)


def test_behaviour::token_constructor_args():
    sig = inspect.signature(Behaviour::Token.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::place_is_not_abstract():
    assert not inspect.isabstract(Behaviour::Place)


def test_behaviour::place_constructor_exists():
    assert callable(Behaviour::Place.__init__)


def test_behaviour::place_constructor_args():
    sig = inspect.signature(Behaviour::Place.__init__)
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
Behaviour::TransitionFunction_strategy = st.builds(
    Behaviour::TransitionFunction,
    transitionFunction=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
Behaviour::StochasticTransition_strategy = st.builds(
    Behaviour::StochasticTransition,
)
Behaviour::ConditionalTransition_strategy = st.builds(
    Behaviour::ConditionalTransition,
)
Place_strategy = st.builds(
    Place,
)
Behaviour::StartPlace_strategy = st.builds(
    Behaviour::StartPlace,
    spawnPolicy=
        safe_text
)
Behaviour::Server_strategy = st.builds(
    Behaviour::Server,
    capacity=
        st.integers()
)
Behaviour::WaitingLine_strategy = st.builds(
    Behaviour::WaitingLine,
    schedulingPolicy=
        safe_text
)
Behaviour::QueuePlace_strategy = st.builds(
    Behaviour::QueuePlace,
)
Behaviour::DefaultPlace_strategy = st.builds(
    Behaviour::DefaultPlace,
)
Connection_strategy = st.builds(
    Connection,
)
Behaviour::PreTransitionConnection_strategy = st.builds(
    Behaviour::PreTransitionConnection,
    requiredTokenAmount=
        st.integers()
)
Behaviour::PostTransitionConnection_strategy = st.builds(
    Behaviour::PostTransitionConnection,
)
Identifier_strategy = st.builds(
    Identifier,
)
Behaviour::Connection_strategy = st.builds(
    Behaviour::Connection,
)
Behaviour::Transition_strategy = st.builds(
    Behaviour::Transition,
)
Behaviour::Description_strategy = st.builds(
    Behaviour::Description,
)
Behaviour::Colour_strategy = st.builds(
    Behaviour::Colour,
    attribute=
        safe_text
)
Behaviour::Token_strategy = st.builds(
    Behaviour::Token,
)
Behaviour::Place_strategy = st.builds(
    Behaviour::Place,
)

@given(instance=Behaviour::TransitionFunction_strategy)
@settings(max_examples=50)
def test_behaviour::transitionfunction_instantiation(instance):
    assert isinstance(instance, Behaviour::TransitionFunction)

@given(instance=Behaviour::TransitionFunction_strategy)
def test_behaviour::transitionfunction_transitionFunction_type(instance):
    assert isinstance(instance.transitionFunction, str)


@given(instance=Behaviour::TransitionFunction_strategy)
def test_behaviour::transitionfunction_transitionFunction_setter(instance):
    original = instance.transitionFunction
    instance.transitionFunction = original
    assert instance.transitionFunction == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=Behaviour::StochasticTransition_strategy)
@settings(max_examples=50)
def test_behaviour::stochastictransition_instantiation(instance):
    assert isinstance(instance, Behaviour::StochasticTransition)

@given(instance=Behaviour::ConditionalTransition_strategy)
@settings(max_examples=50)
def test_behaviour::conditionaltransition_instantiation(instance):
    assert isinstance(instance, Behaviour::ConditionalTransition)

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=Behaviour::StartPlace_strategy)
@settings(max_examples=50)
def test_behaviour::startplace_instantiation(instance):
    assert isinstance(instance, Behaviour::StartPlace)

@given(instance=Behaviour::StartPlace_strategy)
def test_behaviour::startplace_spawnPolicy_type(instance):
    assert isinstance(instance.spawnPolicy, str)


@given(instance=Behaviour::StartPlace_strategy)
def test_behaviour::startplace_spawnPolicy_setter(instance):
    original = instance.spawnPolicy
    instance.spawnPolicy = original
    assert instance.spawnPolicy == original

@given(instance=Behaviour::Server_strategy)
@settings(max_examples=50)
def test_behaviour::server_instantiation(instance):
    assert isinstance(instance, Behaviour::Server)

@given(instance=Behaviour::Server_strategy)
def test_behaviour::server_capacity_type(instance):
    assert isinstance(instance.capacity, int)


@given(instance=Behaviour::Server_strategy)
def test_behaviour::server_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=Behaviour::WaitingLine_strategy)
@settings(max_examples=50)
def test_behaviour::waitingline_instantiation(instance):
    assert isinstance(instance, Behaviour::WaitingLine)

@given(instance=Behaviour::WaitingLine_strategy)
def test_behaviour::waitingline_schedulingPolicy_type(instance):
    assert isinstance(instance.schedulingPolicy, str)


@given(instance=Behaviour::WaitingLine_strategy)
def test_behaviour::waitingline_schedulingPolicy_setter(instance):
    original = instance.schedulingPolicy
    instance.schedulingPolicy = original
    assert instance.schedulingPolicy == original

@given(instance=Behaviour::QueuePlace_strategy)
@settings(max_examples=50)
def test_behaviour::queueplace_instantiation(instance):
    assert isinstance(instance, Behaviour::QueuePlace)

@given(instance=Behaviour::DefaultPlace_strategy)
@settings(max_examples=50)
def test_behaviour::defaultplace_instantiation(instance):
    assert isinstance(instance, Behaviour::DefaultPlace)

@given(instance=Connection_strategy)
@settings(max_examples=50)
def test_connection_instantiation(instance):
    assert isinstance(instance, Connection)

@given(instance=Behaviour::PreTransitionConnection_strategy)
@settings(max_examples=50)
def test_behaviour::pretransitionconnection_instantiation(instance):
    assert isinstance(instance, Behaviour::PreTransitionConnection)

@given(instance=Behaviour::PreTransitionConnection_strategy)
def test_behaviour::pretransitionconnection_requiredTokenAmount_type(instance):
    assert isinstance(instance.requiredTokenAmount, int)


@given(instance=Behaviour::PreTransitionConnection_strategy)
def test_behaviour::pretransitionconnection_requiredTokenAmount_setter(instance):
    original = instance.requiredTokenAmount
    instance.requiredTokenAmount = original
    assert instance.requiredTokenAmount == original

@given(instance=Behaviour::PostTransitionConnection_strategy)
@settings(max_examples=50)
def test_behaviour::posttransitionconnection_instantiation(instance):
    assert isinstance(instance, Behaviour::PostTransitionConnection)

@given(instance=Identifier_strategy)
@settings(max_examples=50)
def test_identifier_instantiation(instance):
    assert isinstance(instance, Identifier)

@given(instance=Behaviour::Connection_strategy)
@settings(max_examples=50)
def test_behaviour::connection_instantiation(instance):
    assert isinstance(instance, Behaviour::Connection)

@given(instance=Behaviour::Transition_strategy)
@settings(max_examples=50)
def test_behaviour::transition_instantiation(instance):
    assert isinstance(instance, Behaviour::Transition)

@given(instance=Behaviour::Description_strategy)
@settings(max_examples=50)
def test_behaviour::description_instantiation(instance):
    assert isinstance(instance, Behaviour::Description)

@given(instance=Behaviour::Colour_strategy)
@settings(max_examples=50)
def test_behaviour::colour_instantiation(instance):
    assert isinstance(instance, Behaviour::Colour)

@given(instance=Behaviour::Colour_strategy)
def test_behaviour::colour_attribute_type(instance):
    assert isinstance(instance.attribute, str)


@given(instance=Behaviour::Colour_strategy)
def test_behaviour::colour_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=Behaviour::Token_strategy)
@settings(max_examples=50)
def test_behaviour::token_instantiation(instance):
    assert isinstance(instance, Behaviour::Token)

@given(instance=Behaviour::Place_strategy)
@settings(max_examples=50)
def test_behaviour::place_instantiation(instance):
    assert isinstance(instance, Behaviour::Place)
