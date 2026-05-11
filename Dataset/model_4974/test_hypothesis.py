import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ComponentLanguageDeep::ConnectorInstance,
    ComponentLanguageDeep::PortInstance,
    ComponentLanguageDeep::ComponentInstance,
    ComponentLanguageDeep::Port,
    ComponentLanguageDeep::Component,
    PortInstance,
    ComponentLanguageDeep::OutPortInstance,
    ComponentLanguageDeep::InPortInstance,
    Port,
    ComponentLanguageDeep::OutPort,
    ComponentLanguageDeep::InPort,
    ComponentLanguageDeep::Connector,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_componentlanguagedeep::connectorinstance_is_not_abstract():
    assert not inspect.isabstract(ComponentLanguageDeep::ConnectorInstance)


def test_componentlanguagedeep::connectorinstance_constructor_exists():
    assert callable(ComponentLanguageDeep::ConnectorInstance.__init__)


def test_componentlanguagedeep::connectorinstance_constructor_args():
    sig = inspect.signature(ComponentLanguageDeep::ConnectorInstance.__init__)
    params = list(sig.parameters.keys())



def test_componentlanguagedeep::portinstance_is_not_abstract():
    assert not inspect.isabstract(ComponentLanguageDeep::PortInstance)


def test_componentlanguagedeep::portinstance_constructor_exists():
    assert callable(ComponentLanguageDeep::PortInstance.__init__)


def test_componentlanguagedeep::portinstance_constructor_args():
    sig = inspect.signature(ComponentLanguageDeep::PortInstance.__init__)
    params = list(sig.parameters.keys())



def test_componentlanguagedeep::componentinstance_is_not_abstract():
    assert not inspect.isabstract(ComponentLanguageDeep::ComponentInstance)


def test_componentlanguagedeep::componentinstance_constructor_exists():
    assert callable(ComponentLanguageDeep::ComponentInstance.__init__)


def test_componentlanguagedeep::componentinstance_constructor_args():
    sig = inspect.signature(ComponentLanguageDeep::ComponentInstance.__init__)
    params = list(sig.parameters.keys())



def test_componentlanguagedeep::port_is_not_abstract():
    assert not inspect.isabstract(ComponentLanguageDeep::Port)


def test_componentlanguagedeep::port_constructor_exists():
    assert callable(ComponentLanguageDeep::Port.__init__)


def test_componentlanguagedeep::port_constructor_args():
    sig = inspect.signature(ComponentLanguageDeep::Port.__init__)
    params = list(sig.parameters.keys())



def test_componentlanguagedeep::component_is_not_abstract():
    assert not inspect.isabstract(ComponentLanguageDeep::Component)


def test_componentlanguagedeep::component_constructor_exists():
    assert callable(ComponentLanguageDeep::Component.__init__)


def test_componentlanguagedeep::component_constructor_args():
    sig = inspect.signature(ComponentLanguageDeep::Component.__init__)
    params = list(sig.parameters.keys())



def test_portinstance_is_not_abstract():
    assert not inspect.isabstract(PortInstance)


def test_portinstance_constructor_exists():
    assert callable(PortInstance.__init__)


def test_portinstance_constructor_args():
    sig = inspect.signature(PortInstance.__init__)
    params = list(sig.parameters.keys())



def test_componentlanguagedeep::outportinstance_is_not_abstract():
    assert not inspect.isabstract(ComponentLanguageDeep::OutPortInstance)


def test_componentlanguagedeep::outportinstance_constructor_exists():
    assert callable(ComponentLanguageDeep::OutPortInstance.__init__)


def test_componentlanguagedeep::outportinstance_constructor_args():
    sig = inspect.signature(ComponentLanguageDeep::OutPortInstance.__init__)
    params = list(sig.parameters.keys())



def test_componentlanguagedeep::inportinstance_is_not_abstract():
    assert not inspect.isabstract(ComponentLanguageDeep::InPortInstance)


def test_componentlanguagedeep::inportinstance_constructor_exists():
    assert callable(ComponentLanguageDeep::InPortInstance.__init__)


def test_componentlanguagedeep::inportinstance_constructor_args():
    sig = inspect.signature(ComponentLanguageDeep::InPortInstance.__init__)
    params = list(sig.parameters.keys())



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_componentlanguagedeep::outport_is_not_abstract():
    assert not inspect.isabstract(ComponentLanguageDeep::OutPort)


def test_componentlanguagedeep::outport_constructor_exists():
    assert callable(ComponentLanguageDeep::OutPort.__init__)


def test_componentlanguagedeep::outport_constructor_args():
    sig = inspect.signature(ComponentLanguageDeep::OutPort.__init__)
    params = list(sig.parameters.keys())



def test_componentlanguagedeep::inport_is_not_abstract():
    assert not inspect.isabstract(ComponentLanguageDeep::InPort)


def test_componentlanguagedeep::inport_constructor_exists():
    assert callable(ComponentLanguageDeep::InPort.__init__)


def test_componentlanguagedeep::inport_constructor_args():
    sig = inspect.signature(ComponentLanguageDeep::InPort.__init__)
    params = list(sig.parameters.keys())



def test_componentlanguagedeep::connector_is_not_abstract():
    assert not inspect.isabstract(ComponentLanguageDeep::Connector)


def test_componentlanguagedeep::connector_constructor_exists():
    assert callable(ComponentLanguageDeep::Connector.__init__)


def test_componentlanguagedeep::connector_constructor_args():
    sig = inspect.signature(ComponentLanguageDeep::Connector.__init__)
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
ComponentLanguageDeep::ConnectorInstance_strategy = st.builds(
    ComponentLanguageDeep::ConnectorInstance,
)
ComponentLanguageDeep::PortInstance_strategy = st.builds(
    ComponentLanguageDeep::PortInstance,
)
ComponentLanguageDeep::ComponentInstance_strategy = st.builds(
    ComponentLanguageDeep::ComponentInstance,
)
ComponentLanguageDeep::Port_strategy = st.builds(
    ComponentLanguageDeep::Port,
)
ComponentLanguageDeep::Component_strategy = st.builds(
    ComponentLanguageDeep::Component,
)
PortInstance_strategy = st.builds(
    PortInstance,
)
ComponentLanguageDeep::OutPortInstance_strategy = st.builds(
    ComponentLanguageDeep::OutPortInstance,
)
ComponentLanguageDeep::InPortInstance_strategy = st.builds(
    ComponentLanguageDeep::InPortInstance,
)
Port_strategy = st.builds(
    Port,
)
ComponentLanguageDeep::OutPort_strategy = st.builds(
    ComponentLanguageDeep::OutPort,
)
ComponentLanguageDeep::InPort_strategy = st.builds(
    ComponentLanguageDeep::InPort,
)
ComponentLanguageDeep::Connector_strategy = st.builds(
    ComponentLanguageDeep::Connector,
)

@given(instance=ComponentLanguageDeep::ConnectorInstance_strategy)
@settings(max_examples=50)
def test_componentlanguagedeep::connectorinstance_instantiation(instance):
    assert isinstance(instance, ComponentLanguageDeep::ConnectorInstance)

@given(instance=ComponentLanguageDeep::PortInstance_strategy)
@settings(max_examples=50)
def test_componentlanguagedeep::portinstance_instantiation(instance):
    assert isinstance(instance, ComponentLanguageDeep::PortInstance)

@given(instance=ComponentLanguageDeep::ComponentInstance_strategy)
@settings(max_examples=50)
def test_componentlanguagedeep::componentinstance_instantiation(instance):
    assert isinstance(instance, ComponentLanguageDeep::ComponentInstance)

@given(instance=ComponentLanguageDeep::Port_strategy)
@settings(max_examples=50)
def test_componentlanguagedeep::port_instantiation(instance):
    assert isinstance(instance, ComponentLanguageDeep::Port)

@given(instance=ComponentLanguageDeep::Component_strategy)
@settings(max_examples=50)
def test_componentlanguagedeep::component_instantiation(instance):
    assert isinstance(instance, ComponentLanguageDeep::Component)

@given(instance=PortInstance_strategy)
@settings(max_examples=50)
def test_portinstance_instantiation(instance):
    assert isinstance(instance, PortInstance)

@given(instance=ComponentLanguageDeep::OutPortInstance_strategy)
@settings(max_examples=50)
def test_componentlanguagedeep::outportinstance_instantiation(instance):
    assert isinstance(instance, ComponentLanguageDeep::OutPortInstance)

@given(instance=ComponentLanguageDeep::InPortInstance_strategy)
@settings(max_examples=50)
def test_componentlanguagedeep::inportinstance_instantiation(instance):
    assert isinstance(instance, ComponentLanguageDeep::InPortInstance)

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=ComponentLanguageDeep::OutPort_strategy)
@settings(max_examples=50)
def test_componentlanguagedeep::outport_instantiation(instance):
    assert isinstance(instance, ComponentLanguageDeep::OutPort)

@given(instance=ComponentLanguageDeep::InPort_strategy)
@settings(max_examples=50)
def test_componentlanguagedeep::inport_instantiation(instance):
    assert isinstance(instance, ComponentLanguageDeep::InPort)

@given(instance=ComponentLanguageDeep::Connector_strategy)
@settings(max_examples=50)
def test_componentlanguagedeep::connector_instantiation(instance):
    assert isinstance(instance, ComponentLanguageDeep::Connector)
