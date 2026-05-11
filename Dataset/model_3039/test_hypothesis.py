import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dataflownet::Token,
    dataflownet::Type,
    Node,
    dataflownet::StateMachine,
    dataflownet::DataflowNet,
    NamedElement,
    dataflownet::Channel,
    dataflownet::DataflowSystem,
    dataflownet::StateMachineState,
    dataflownet::FiringRule,
    dataflownet::Node,
    dataflownet::NamedElement,
    dataflownet::StateMachineTransition,
    dataflownet::Process,
    Protocol,
    Comparation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dataflownet::token_is_not_abstract():
    assert not inspect.isabstract(dataflownet::Token)


def test_dataflownet::token_constructor_exists():
    assert callable(dataflownet::Token.__init__)


def test_dataflownet::token_constructor_args():
    sig = inspect.signature(dataflownet::Token.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dataflownet::token_has_value():
    assert hasattr(dataflownet::Token, "value")
    descriptor = None
    for klass in dataflownet::Token.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dataflownet::type_is_not_abstract():
    assert not inspect.isabstract(dataflownet::Type)


def test_dataflownet::type_constructor_exists():
    assert callable(dataflownet::Type.__init__)


def test_dataflownet::type_constructor_args():
    sig = inspect.signature(dataflownet::Type.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_dataflownet::statemachine_is_not_abstract():
    assert not inspect.isabstract(dataflownet::StateMachine)


def test_dataflownet::statemachine_constructor_exists():
    assert callable(dataflownet::StateMachine.__init__)


def test_dataflownet::statemachine_constructor_args():
    sig = inspect.signature(dataflownet::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_dataflownet::dataflownet_is_not_abstract():
    assert not inspect.isabstract(dataflownet::DataflowNet)


def test_dataflownet::dataflownet_constructor_exists():
    assert callable(dataflownet::DataflowNet.__init__)


def test_dataflownet::dataflownet_constructor_args():
    sig = inspect.signature(dataflownet::DataflowNet.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_dataflownet::channel_is_not_abstract():
    assert not inspect.isabstract(dataflownet::Channel)


def test_dataflownet::channel_constructor_exists():
    assert callable(dataflownet::Channel.__init__)


def test_dataflownet::channel_constructor_args():
    sig = inspect.signature(dataflownet::Channel.__init__)
    params = list(sig.parameters.keys())



def test_dataflownet::dataflowsystem_is_not_abstract():
    assert not inspect.isabstract(dataflownet::DataflowSystem)


def test_dataflownet::dataflowsystem_constructor_exists():
    assert callable(dataflownet::DataflowSystem.__init__)


def test_dataflownet::dataflowsystem_constructor_args():
    sig = inspect.signature(dataflownet::DataflowSystem.__init__)
    params = list(sig.parameters.keys())
    assert "protocol" in params, "Missing parameter 'protocol'"

def test_dataflownet::dataflowsystem_has_protocol():
    assert hasattr(dataflownet::DataflowSystem, "protocol")
    descriptor = None
    for klass in dataflownet::DataflowSystem.__mro__:
        if "protocol" in klass.__dict__:
            descriptor = klass.__dict__["protocol"]
            break
    assert isinstance(descriptor, property)



def test_dataflownet::statemachinestate_is_not_abstract():
    assert not inspect.isabstract(dataflownet::StateMachineState)


def test_dataflownet::statemachinestate_constructor_exists():
    assert callable(dataflownet::StateMachineState.__init__)


def test_dataflownet::statemachinestate_constructor_args():
    sig = inspect.signature(dataflownet::StateMachineState.__init__)
    params = list(sig.parameters.keys())



def test_dataflownet::firingrule_is_not_abstract():
    assert not inspect.isabstract(dataflownet::FiringRule)


def test_dataflownet::firingrule_constructor_exists():
    assert callable(dataflownet::FiringRule.__init__)


def test_dataflownet::firingrule_constructor_args():
    sig = inspect.signature(dataflownet::FiringRule.__init__)
    params = list(sig.parameters.keys())
    assert "compType" in params, "Missing parameter 'compType'"

def test_dataflownet::firingrule_has_compType():
    assert hasattr(dataflownet::FiringRule, "compType")
    descriptor = None
    for klass in dataflownet::FiringRule.__mro__:
        if "compType" in klass.__dict__:
            descriptor = klass.__dict__["compType"]
            break
    assert isinstance(descriptor, property)



def test_dataflownet::node_is_not_abstract():
    assert not inspect.isabstract(dataflownet::Node)


def test_dataflownet::node_constructor_exists():
    assert callable(dataflownet::Node.__init__)


def test_dataflownet::node_constructor_args():
    sig = inspect.signature(dataflownet::Node.__init__)
    params = list(sig.parameters.keys())



def test_dataflownet::namedelement_is_not_abstract():
    assert not inspect.isabstract(dataflownet::NamedElement)


def test_dataflownet::namedelement_constructor_exists():
    assert callable(dataflownet::NamedElement.__init__)


def test_dataflownet::namedelement_constructor_args():
    sig = inspect.signature(dataflownet::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dataflownet::namedelement_has_name():
    assert hasattr(dataflownet::NamedElement, "name")
    descriptor = None
    for klass in dataflownet::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dataflownet::statemachinetransition_is_not_abstract():
    assert not inspect.isabstract(dataflownet::StateMachineTransition)


def test_dataflownet::statemachinetransition_constructor_exists():
    assert callable(dataflownet::StateMachineTransition.__init__)


def test_dataflownet::statemachinetransition_constructor_args():
    sig = inspect.signature(dataflownet::StateMachineTransition.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"

def test_dataflownet::statemachinetransition_has_priority():
    assert hasattr(dataflownet::StateMachineTransition, "priority")
    descriptor = None
    for klass in dataflownet::StateMachineTransition.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_dataflownet::process_is_not_abstract():
    assert not inspect.isabstract(dataflownet::Process)


def test_dataflownet::process_constructor_exists():
    assert callable(dataflownet::Process.__init__)


def test_dataflownet::process_constructor_args():
    sig = inspect.signature(dataflownet::Process.__init__)
    params = list(sig.parameters.keys())
    assert "host" in params, "Missing parameter 'host'"

def test_dataflownet::process_has_host():
    assert hasattr(dataflownet::Process, "host")
    descriptor = None
    for klass in dataflownet::Process.__mro__:
        if "host" in klass.__dict__:
            descriptor = klass.__dict__["host"]
            break
    assert isinstance(descriptor, property)

def test_protocol_exists():
    # Check that the Enumeration exists
    assert Protocol is not None

def test_protocol_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Protocol]
    expected_literals = [
        "Akka",
        "Paho",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Protocol"

def test_comparation_exists():
    # Check that the Enumeration exists
    assert Comparation is not None

def test_comparation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Comparation]
    expected_literals = [
        "Equal",
        "Less",
        "NotEqual",
        "Greater",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Comparation"


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
dataflownet::Token_strategy = st.builds(
    dataflownet::Token,
    value=
        safe_text
)
dataflownet::Type_strategy = st.builds(
    dataflownet::Type,
)
Node_strategy = st.builds(
    Node,
)
dataflownet::StateMachine_strategy = st.builds(
    dataflownet::StateMachine,
)
dataflownet::DataflowNet_strategy = st.builds(
    dataflownet::DataflowNet,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
dataflownet::Channel_strategy = st.builds(
    dataflownet::Channel,
)
dataflownet::DataflowSystem_strategy = st.builds(
    dataflownet::DataflowSystem,
    protocol=
        safe_text
)
dataflownet::StateMachineState_strategy = st.builds(
    dataflownet::StateMachineState,
)
dataflownet::FiringRule_strategy = st.builds(
    dataflownet::FiringRule,
    compType=
        safe_text
)
dataflownet::Node_strategy = st.builds(
    dataflownet::Node,
)
dataflownet::NamedElement_strategy = st.builds(
    dataflownet::NamedElement,
    name=
        safe_text
)
dataflownet::StateMachineTransition_strategy = st.builds(
    dataflownet::StateMachineTransition,
    priority=
        st.integers()
)
dataflownet::Process_strategy = st.builds(
    dataflownet::Process,
    host=
        safe_text
)

@given(instance=dataflownet::Token_strategy)
@settings(max_examples=50)
def test_dataflownet::token_instantiation(instance):
    assert isinstance(instance, dataflownet::Token)

@given(instance=dataflownet::Token_strategy)
def test_dataflownet::token_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=dataflownet::Token_strategy)
def test_dataflownet::token_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dataflownet::Type_strategy)
@settings(max_examples=50)
def test_dataflownet::type_instantiation(instance):
    assert isinstance(instance, dataflownet::Type)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=dataflownet::StateMachine_strategy)
@settings(max_examples=50)
def test_dataflownet::statemachine_instantiation(instance):
    assert isinstance(instance, dataflownet::StateMachine)

@given(instance=dataflownet::DataflowNet_strategy)
@settings(max_examples=50)
def test_dataflownet::dataflownet_instantiation(instance):
    assert isinstance(instance, dataflownet::DataflowNet)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=dataflownet::Channel_strategy)
@settings(max_examples=50)
def test_dataflownet::channel_instantiation(instance):
    assert isinstance(instance, dataflownet::Channel)

@given(instance=dataflownet::DataflowSystem_strategy)
@settings(max_examples=50)
def test_dataflownet::dataflowsystem_instantiation(instance):
    assert isinstance(instance, dataflownet::DataflowSystem)

@given(instance=dataflownet::DataflowSystem_strategy)
def test_dataflownet::dataflowsystem_protocol_type(instance):
    assert isinstance(instance.protocol, str)


@given(instance=dataflownet::DataflowSystem_strategy)
def test_dataflownet::dataflowsystem_protocol_setter(instance):
    original = instance.protocol
    instance.protocol = original
    assert instance.protocol == original

@given(instance=dataflownet::StateMachineState_strategy)
@settings(max_examples=50)
def test_dataflownet::statemachinestate_instantiation(instance):
    assert isinstance(instance, dataflownet::StateMachineState)

@given(instance=dataflownet::FiringRule_strategy)
@settings(max_examples=50)
def test_dataflownet::firingrule_instantiation(instance):
    assert isinstance(instance, dataflownet::FiringRule)

@given(instance=dataflownet::FiringRule_strategy)
def test_dataflownet::firingrule_compType_type(instance):
    assert isinstance(instance.compType, str)


@given(instance=dataflownet::FiringRule_strategy)
def test_dataflownet::firingrule_compType_setter(instance):
    original = instance.compType
    instance.compType = original
    assert instance.compType == original

@given(instance=dataflownet::Node_strategy)
@settings(max_examples=50)
def test_dataflownet::node_instantiation(instance):
    assert isinstance(instance, dataflownet::Node)

@given(instance=dataflownet::NamedElement_strategy)
@settings(max_examples=50)
def test_dataflownet::namedelement_instantiation(instance):
    assert isinstance(instance, dataflownet::NamedElement)

@given(instance=dataflownet::NamedElement_strategy)
def test_dataflownet::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dataflownet::NamedElement_strategy)
def test_dataflownet::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dataflownet::StateMachineTransition_strategy)
@settings(max_examples=50)
def test_dataflownet::statemachinetransition_instantiation(instance):
    assert isinstance(instance, dataflownet::StateMachineTransition)

@given(instance=dataflownet::StateMachineTransition_strategy)
def test_dataflownet::statemachinetransition_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=dataflownet::StateMachineTransition_strategy)
def test_dataflownet::statemachinetransition_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=dataflownet::Process_strategy)
@settings(max_examples=50)
def test_dataflownet::process_instantiation(instance):
    assert isinstance(instance, dataflownet::Process)

@given(instance=dataflownet::Process_strategy)
def test_dataflownet::process_host_type(instance):
    assert isinstance(instance.host, str)


@given(instance=dataflownet::Process_strategy)
def test_dataflownet::process_host_setter(instance):
    original = instance.host
    instance.host = original
    assert instance.host == original
