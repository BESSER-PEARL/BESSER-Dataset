import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Port,
    ComponentLanguageShallow::OutPort,
    ComponentLanguageShallow::InPort,
    ComponentLanguageShallow::Connector,
    ComponentLanguageShallow::Port,
    ComponentLanguageShallow::Component,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_componentlanguageshallow::outport_is_not_abstract():
    assert not inspect.isabstract(ComponentLanguageShallow::OutPort)


def test_componentlanguageshallow::outport_constructor_exists():
    assert callable(ComponentLanguageShallow::OutPort.__init__)


def test_componentlanguageshallow::outport_constructor_args():
    sig = inspect.signature(ComponentLanguageShallow::OutPort.__init__)
    params = list(sig.parameters.keys())



def test_componentlanguageshallow::inport_is_not_abstract():
    assert not inspect.isabstract(ComponentLanguageShallow::InPort)


def test_componentlanguageshallow::inport_constructor_exists():
    assert callable(ComponentLanguageShallow::InPort.__init__)


def test_componentlanguageshallow::inport_constructor_args():
    sig = inspect.signature(ComponentLanguageShallow::InPort.__init__)
    params = list(sig.parameters.keys())



def test_componentlanguageshallow::connector_is_not_abstract():
    assert not inspect.isabstract(ComponentLanguageShallow::Connector)


def test_componentlanguageshallow::connector_constructor_exists():
    assert callable(ComponentLanguageShallow::Connector.__init__)


def test_componentlanguageshallow::connector_constructor_args():
    sig = inspect.signature(ComponentLanguageShallow::Connector.__init__)
    params = list(sig.parameters.keys())



def test_componentlanguageshallow::port_is_not_abstract():
    assert not inspect.isabstract(ComponentLanguageShallow::Port)


def test_componentlanguageshallow::port_constructor_exists():
    assert callable(ComponentLanguageShallow::Port.__init__)


def test_componentlanguageshallow::port_constructor_args():
    sig = inspect.signature(ComponentLanguageShallow::Port.__init__)
    params = list(sig.parameters.keys())



def test_componentlanguageshallow::component_is_not_abstract():
    assert not inspect.isabstract(ComponentLanguageShallow::Component)


def test_componentlanguageshallow::component_constructor_exists():
    assert callable(ComponentLanguageShallow::Component.__init__)


def test_componentlanguageshallow::component_constructor_args():
    sig = inspect.signature(ComponentLanguageShallow::Component.__init__)
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
Port_strategy = st.builds(
    Port,
)
ComponentLanguageShallow::OutPort_strategy = st.builds(
    ComponentLanguageShallow::OutPort,
)
ComponentLanguageShallow::InPort_strategy = st.builds(
    ComponentLanguageShallow::InPort,
)
ComponentLanguageShallow::Connector_strategy = st.builds(
    ComponentLanguageShallow::Connector,
)
ComponentLanguageShallow::Port_strategy = st.builds(
    ComponentLanguageShallow::Port,
)
ComponentLanguageShallow::Component_strategy = st.builds(
    ComponentLanguageShallow::Component,
)

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=ComponentLanguageShallow::OutPort_strategy)
@settings(max_examples=50)
def test_componentlanguageshallow::outport_instantiation(instance):
    assert isinstance(instance, ComponentLanguageShallow::OutPort)

@given(instance=ComponentLanguageShallow::InPort_strategy)
@settings(max_examples=50)
def test_componentlanguageshallow::inport_instantiation(instance):
    assert isinstance(instance, ComponentLanguageShallow::InPort)

@given(instance=ComponentLanguageShallow::Connector_strategy)
@settings(max_examples=50)
def test_componentlanguageshallow::connector_instantiation(instance):
    assert isinstance(instance, ComponentLanguageShallow::Connector)

@given(instance=ComponentLanguageShallow::Port_strategy)
@settings(max_examples=50)
def test_componentlanguageshallow::port_instantiation(instance):
    assert isinstance(instance, ComponentLanguageShallow::Port)

@given(instance=ComponentLanguageShallow::Component_strategy)
@settings(max_examples=50)
def test_componentlanguageshallow::component_instantiation(instance):
    assert isinstance(instance, ComponentLanguageShallow::Component)
