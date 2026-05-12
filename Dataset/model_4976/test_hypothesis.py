import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Port,
    ComponentLanguageShallow_OutPort,
    ComponentLanguageShallow_InPort,
    ComponentLanguageShallow_Connector,
    ComponentLanguageShallow_Port,
    ComponentLanguageShallow_Component,
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



def test_componentlanguageshallow_outport_is_not_abstract():
    assert not inspect.isabstract(ComponentLanguageShallow_OutPort)


def test_componentlanguageshallow_outport_constructor_exists():
    assert callable(ComponentLanguageShallow_OutPort.__init__)


def test_componentlanguageshallow_outport_constructor_args():
    sig = inspect.signature(ComponentLanguageShallow_OutPort.__init__)
    params = list(sig.parameters.keys())



def test_componentlanguageshallow_inport_is_not_abstract():
    assert not inspect.isabstract(ComponentLanguageShallow_InPort)


def test_componentlanguageshallow_inport_constructor_exists():
    assert callable(ComponentLanguageShallow_InPort.__init__)


def test_componentlanguageshallow_inport_constructor_args():
    sig = inspect.signature(ComponentLanguageShallow_InPort.__init__)
    params = list(sig.parameters.keys())



def test_componentlanguageshallow_connector_is_not_abstract():
    assert not inspect.isabstract(ComponentLanguageShallow_Connector)


def test_componentlanguageshallow_connector_constructor_exists():
    assert callable(ComponentLanguageShallow_Connector.__init__)


def test_componentlanguageshallow_connector_constructor_args():
    sig = inspect.signature(ComponentLanguageShallow_Connector.__init__)
    params = list(sig.parameters.keys())



def test_componentlanguageshallow_port_is_not_abstract():
    assert not inspect.isabstract(ComponentLanguageShallow_Port)


def test_componentlanguageshallow_port_constructor_exists():
    assert callable(ComponentLanguageShallow_Port.__init__)


def test_componentlanguageshallow_port_constructor_args():
    sig = inspect.signature(ComponentLanguageShallow_Port.__init__)
    params = list(sig.parameters.keys())



def test_componentlanguageshallow_component_is_not_abstract():
    assert not inspect.isabstract(ComponentLanguageShallow_Component)


def test_componentlanguageshallow_component_constructor_exists():
    assert callable(ComponentLanguageShallow_Component.__init__)


def test_componentlanguageshallow_component_constructor_args():
    sig = inspect.signature(ComponentLanguageShallow_Component.__init__)
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
ComponentLanguageShallow_OutPort_strategy = st.builds(
    ComponentLanguageShallow_OutPort,
)
ComponentLanguageShallow_InPort_strategy = st.builds(
    ComponentLanguageShallow_InPort,
)
ComponentLanguageShallow_Connector_strategy = st.builds(
    ComponentLanguageShallow_Connector,
)
ComponentLanguageShallow_Port_strategy = st.builds(
    ComponentLanguageShallow_Port,
)
ComponentLanguageShallow_Component_strategy = st.builds(
    ComponentLanguageShallow_Component,
)

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=ComponentLanguageShallow_OutPort_strategy)
@settings(max_examples=50)
def test_componentlanguageshallow_outport_instantiation(instance):
    assert isinstance(instance, ComponentLanguageShallow_OutPort)

@given(instance=ComponentLanguageShallow_InPort_strategy)
@settings(max_examples=50)
def test_componentlanguageshallow_inport_instantiation(instance):
    assert isinstance(instance, ComponentLanguageShallow_InPort)

@given(instance=ComponentLanguageShallow_Connector_strategy)
@settings(max_examples=50)
def test_componentlanguageshallow_connector_instantiation(instance):
    assert isinstance(instance, ComponentLanguageShallow_Connector)

@given(instance=ComponentLanguageShallow_Port_strategy)
@settings(max_examples=50)
def test_componentlanguageshallow_port_instantiation(instance):
    assert isinstance(instance, ComponentLanguageShallow_Port)

@given(instance=ComponentLanguageShallow_Component_strategy)
@settings(max_examples=50)
def test_componentlanguageshallow_component_instantiation(instance):
    assert isinstance(instance, ComponentLanguageShallow_Component)
