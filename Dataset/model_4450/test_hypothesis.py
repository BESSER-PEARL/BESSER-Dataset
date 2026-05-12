import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Message,
    iot_Request,
    iot_Dispatch,
    iot_Event,
    iot_Message,
    iot_BrokerSpec,
    iot_IotSystemSpec,
    iot_IotSystem,
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



def test_iot_request_is_not_abstract():
    assert not inspect.isabstract(iot_Request)


def test_iot_request_constructor_exists():
    assert callable(iot_Request.__init__)


def test_iot_request_constructor_args():
    sig = inspect.signature(iot_Request.__init__)
    params = list(sig.parameters.keys())



def test_iot_dispatch_is_not_abstract():
    assert not inspect.isabstract(iot_Dispatch)


def test_iot_dispatch_constructor_exists():
    assert callable(iot_Dispatch.__init__)


def test_iot_dispatch_constructor_args():
    sig = inspect.signature(iot_Dispatch.__init__)
    params = list(sig.parameters.keys())



def test_iot_event_is_not_abstract():
    assert not inspect.isabstract(iot_Event)


def test_iot_event_constructor_exists():
    assert callable(iot_Event.__init__)


def test_iot_event_constructor_args():
    sig = inspect.signature(iot_Event.__init__)
    params = list(sig.parameters.keys())



def test_iot_message_is_not_abstract():
    assert not inspect.isabstract(iot_Message)


def test_iot_message_constructor_exists():
    assert callable(iot_Message.__init__)


def test_iot_message_constructor_args():
    sig = inspect.signature(iot_Message.__init__)
    params = list(sig.parameters.keys())
    assert "msg" in params, "Missing parameter 'msg'"
    assert "name" in params, "Missing parameter 'name'"

def test_iot_message_has_msg():
    assert hasattr(iot_Message, "msg")
    descriptor = None
    for klass in iot_Message.__mro__:
        if "msg" in klass.__dict__:
            descriptor = klass.__dict__["msg"]
            break
    assert isinstance(descriptor, property)

def test_iot_message_has_name():
    assert hasattr(iot_Message, "name")
    descriptor = None
    for klass in iot_Message.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot_brokerspec_is_not_abstract():
    assert not inspect.isabstract(iot_BrokerSpec)


def test_iot_brokerspec_constructor_exists():
    assert callable(iot_BrokerSpec.__init__)


def test_iot_brokerspec_constructor_args():
    sig = inspect.signature(iot_BrokerSpec.__init__)
    params = list(sig.parameters.keys())
    assert "brokerPort" in params, "Missing parameter 'brokerPort'"
    assert "brokerHost" in params, "Missing parameter 'brokerHost'"

def test_iot_brokerspec_has_brokerPort():
    assert hasattr(iot_BrokerSpec, "brokerPort")
    descriptor = None
    for klass in iot_BrokerSpec.__mro__:
        if "brokerPort" in klass.__dict__:
            descriptor = klass.__dict__["brokerPort"]
            break
    assert isinstance(descriptor, property)

def test_iot_brokerspec_has_brokerHost():
    assert hasattr(iot_BrokerSpec, "brokerHost")
    descriptor = None
    for klass in iot_BrokerSpec.__mro__:
        if "brokerHost" in klass.__dict__:
            descriptor = klass.__dict__["brokerHost"]
            break
    assert isinstance(descriptor, property)



def test_iot_iotsystemspec_is_not_abstract():
    assert not inspect.isabstract(iot_IotSystemSpec)


def test_iot_iotsystemspec_constructor_exists():
    assert callable(iot_IotSystemSpec.__init__)


def test_iot_iotsystemspec_constructor_args():
    sig = inspect.signature(iot_IotSystemSpec.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot_iotsystemspec_has_name():
    assert hasattr(iot_IotSystemSpec, "name")
    descriptor = None
    for klass in iot_IotSystemSpec.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot_iotsystem_is_not_abstract():
    assert not inspect.isabstract(iot_IotSystem)


def test_iot_iotsystem_constructor_exists():
    assert callable(iot_IotSystem.__init__)


def test_iot_iotsystem_constructor_args():
    sig = inspect.signature(iot_IotSystem.__init__)
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
iot_Request_strategy = st.builds(
    iot_Request,
)
iot_Dispatch_strategy = st.builds(
    iot_Dispatch,
)
iot_Event_strategy = st.builds(
    iot_Event,
)
iot_Message_strategy = st.builds(
    iot_Message,
    msg=
        safe_text,
    name=
        safe_text
)
iot_BrokerSpec_strategy = st.builds(
    iot_BrokerSpec,
    brokerPort=
        st.integers(),
    brokerHost=
        safe_text
)
iot_IotSystemSpec_strategy = st.builds(
    iot_IotSystemSpec,
    name=
        safe_text
)
iot_IotSystem_strategy = st.builds(
    iot_IotSystem,
)

@given(instance=Message_strategy)
@settings(max_examples=50)
def test_message_instantiation(instance):
    assert isinstance(instance, Message)

@given(instance=iot_Request_strategy)
@settings(max_examples=50)
def test_iot_request_instantiation(instance):
    assert isinstance(instance, iot_Request)

@given(instance=iot_Dispatch_strategy)
@settings(max_examples=50)
def test_iot_dispatch_instantiation(instance):
    assert isinstance(instance, iot_Dispatch)

@given(instance=iot_Event_strategy)
@settings(max_examples=50)
def test_iot_event_instantiation(instance):
    assert isinstance(instance, iot_Event)

@given(instance=iot_Message_strategy)
@settings(max_examples=50)
def test_iot_message_instantiation(instance):
    assert isinstance(instance, iot_Message)



@given(instance=iot_Message_strategy)
def test_iot_message_msg_setter(instance):
    original = instance.msg
    instance.msg = original
    assert instance.msg == original



@given(instance=iot_Message_strategy)
def test_iot_message_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iot_BrokerSpec_strategy)
@settings(max_examples=50)
def test_iot_brokerspec_instantiation(instance):
    assert isinstance(instance, iot_BrokerSpec)



@given(instance=iot_BrokerSpec_strategy)
def test_iot_brokerspec_brokerPort_setter(instance):
    original = instance.brokerPort
    instance.brokerPort = original
    assert instance.brokerPort == original



@given(instance=iot_BrokerSpec_strategy)
def test_iot_brokerspec_brokerHost_setter(instance):
    original = instance.brokerHost
    instance.brokerHost = original
    assert instance.brokerHost == original

@given(instance=iot_IotSystemSpec_strategy)
@settings(max_examples=50)
def test_iot_iotsystemspec_instantiation(instance):
    assert isinstance(instance, iot_IotSystemSpec)



@given(instance=iot_IotSystemSpec_strategy)
def test_iot_iotsystemspec_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iot_IotSystem_strategy)
@settings(max_examples=50)
def test_iot_iotsystem_instantiation(instance):
    assert isinstance(instance, iot_IotSystem)
