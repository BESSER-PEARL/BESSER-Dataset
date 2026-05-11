import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Message,
    iot::Request,
    iot::Dispatch,
    iot::Event,
    iot::Message,
    iot::BrokerSpec,
    iot::IotSystemSpec,
    iot::IotSystem,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_message_is_not_abstract():
    assert not inspect.isabstract(Message)


def test_message_constructor_exists():
    assert callable(Message.__init__)


def test_message_constructor_args():
    sig = inspect.signature(Message.__init__)
    params = list(sig.parameters.keys())



def test_iot::request_is_not_abstract():
    assert not inspect.isabstract(iot::Request)


def test_iot::request_constructor_exists():
    assert callable(iot::Request.__init__)


def test_iot::request_constructor_args():
    sig = inspect.signature(iot::Request.__init__)
    params = list(sig.parameters.keys())



def test_iot::dispatch_is_not_abstract():
    assert not inspect.isabstract(iot::Dispatch)


def test_iot::dispatch_constructor_exists():
    assert callable(iot::Dispatch.__init__)


def test_iot::dispatch_constructor_args():
    sig = inspect.signature(iot::Dispatch.__init__)
    params = list(sig.parameters.keys())



def test_iot::event_is_not_abstract():
    assert not inspect.isabstract(iot::Event)


def test_iot::event_constructor_exists():
    assert callable(iot::Event.__init__)


def test_iot::event_constructor_args():
    sig = inspect.signature(iot::Event.__init__)
    params = list(sig.parameters.keys())



def test_iot::message_is_not_abstract():
    assert not inspect.isabstract(iot::Message)


def test_iot::message_constructor_exists():
    assert callable(iot::Message.__init__)


def test_iot::message_constructor_args():
    sig = inspect.signature(iot::Message.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "msg" in params, "Missing parameter 'msg'"

def test_iot::message_has_name():
    assert hasattr(iot::Message, "name")
    descriptor = None
    for klass in iot::Message.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_iot::message_has_msg():
    assert hasattr(iot::Message, "msg")
    descriptor = None
    for klass in iot::Message.__mro__:
        if "msg" in klass.__dict__:
            descriptor = klass.__dict__["msg"]
            break
    assert isinstance(descriptor, property)



def test_iot::brokerspec_is_not_abstract():
    assert not inspect.isabstract(iot::BrokerSpec)


def test_iot::brokerspec_constructor_exists():
    assert callable(iot::BrokerSpec.__init__)


def test_iot::brokerspec_constructor_args():
    sig = inspect.signature(iot::BrokerSpec.__init__)
    params = list(sig.parameters.keys())
    assert "brokerPort" in params, "Missing parameter 'brokerPort'"
    assert "brokerHost" in params, "Missing parameter 'brokerHost'"

def test_iot::brokerspec_has_brokerPort():
    assert hasattr(iot::BrokerSpec, "brokerPort")
    descriptor = None
    for klass in iot::BrokerSpec.__mro__:
        if "brokerPort" in klass.__dict__:
            descriptor = klass.__dict__["brokerPort"]
            break
    assert isinstance(descriptor, property)

def test_iot::brokerspec_has_brokerHost():
    assert hasattr(iot::BrokerSpec, "brokerHost")
    descriptor = None
    for klass in iot::BrokerSpec.__mro__:
        if "brokerHost" in klass.__dict__:
            descriptor = klass.__dict__["brokerHost"]
            break
    assert isinstance(descriptor, property)



def test_iot::iotsystemspec_is_not_abstract():
    assert not inspect.isabstract(iot::IotSystemSpec)


def test_iot::iotsystemspec_constructor_exists():
    assert callable(iot::IotSystemSpec.__init__)


def test_iot::iotsystemspec_constructor_args():
    sig = inspect.signature(iot::IotSystemSpec.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot::iotsystemspec_has_name():
    assert hasattr(iot::IotSystemSpec, "name")
    descriptor = None
    for klass in iot::IotSystemSpec.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot::iotsystem_is_not_abstract():
    assert not inspect.isabstract(iot::IotSystem)


def test_iot::iotsystem_constructor_exists():
    assert callable(iot::IotSystem.__init__)


def test_iot::iotsystem_constructor_args():
    sig = inspect.signature(iot::IotSystem.__init__)
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
Message_strategy = st.builds(
    Message,
)
iot::Request_strategy = st.builds(
    iot::Request,
)
iot::Dispatch_strategy = st.builds(
    iot::Dispatch,
)
iot::Event_strategy = st.builds(
    iot::Event,
)
iot::Message_strategy = st.builds(
    iot::Message,
    name=
        safe_text,
    msg=
        safe_text
)
iot::BrokerSpec_strategy = st.builds(
    iot::BrokerSpec,
    brokerPort=
        st.integers(),
    brokerHost=
        safe_text
)
iot::IotSystemSpec_strategy = st.builds(
    iot::IotSystemSpec,
    name=
        safe_text
)
iot::IotSystem_strategy = st.builds(
    iot::IotSystem,
)

@given(instance=Message_strategy)
@settings(max_examples=50)
def test_message_instantiation(instance):
    assert isinstance(instance, Message)

@given(instance=iot::Request_strategy)
@settings(max_examples=50)
def test_iot::request_instantiation(instance):
    assert isinstance(instance, iot::Request)

@given(instance=iot::Dispatch_strategy)
@settings(max_examples=50)
def test_iot::dispatch_instantiation(instance):
    assert isinstance(instance, iot::Dispatch)

@given(instance=iot::Event_strategy)
@settings(max_examples=50)
def test_iot::event_instantiation(instance):
    assert isinstance(instance, iot::Event)

@given(instance=iot::Message_strategy)
@settings(max_examples=50)
def test_iot::message_instantiation(instance):
    assert isinstance(instance, iot::Message)

@given(instance=iot::Message_strategy)
def test_iot::message_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iot::Message_strategy)
def test_iot::message_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iot::Message_strategy)
def test_iot::message_msg_type(instance):
    assert isinstance(instance.msg, str)


@given(instance=iot::Message_strategy)
def test_iot::message_msg_setter(instance):
    original = instance.msg
    instance.msg = original
    assert instance.msg == original

@given(instance=iot::BrokerSpec_strategy)
@settings(max_examples=50)
def test_iot::brokerspec_instantiation(instance):
    assert isinstance(instance, iot::BrokerSpec)

@given(instance=iot::BrokerSpec_strategy)
def test_iot::brokerspec_brokerPort_type(instance):
    assert isinstance(instance.brokerPort, int)


@given(instance=iot::BrokerSpec_strategy)
def test_iot::brokerspec_brokerPort_setter(instance):
    original = instance.brokerPort
    instance.brokerPort = original
    assert instance.brokerPort == original

@given(instance=iot::BrokerSpec_strategy)
def test_iot::brokerspec_brokerHost_type(instance):
    assert isinstance(instance.brokerHost, str)


@given(instance=iot::BrokerSpec_strategy)
def test_iot::brokerspec_brokerHost_setter(instance):
    original = instance.brokerHost
    instance.brokerHost = original
    assert instance.brokerHost == original

@given(instance=iot::IotSystemSpec_strategy)
@settings(max_examples=50)
def test_iot::iotsystemspec_instantiation(instance):
    assert isinstance(instance, iot::IotSystemSpec)

@given(instance=iot::IotSystemSpec_strategy)
def test_iot::iotsystemspec_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iot::IotSystemSpec_strategy)
def test_iot::iotsystemspec_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iot::IotSystem_strategy)
@settings(max_examples=50)
def test_iot::iotsystem_instantiation(instance):
    assert isinstance(instance, iot::IotSystem)
