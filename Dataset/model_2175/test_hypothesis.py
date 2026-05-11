import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Node,
    controlflow::Branch,
    controlflow::Command,
    controlflow::Graph,
    controlflow::Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_controlflow::branch_is_not_abstract():
    assert not inspect.isabstract(controlflow::Branch)


def test_controlflow::branch_constructor_exists():
    assert callable(controlflow::Branch.__init__)


def test_controlflow::branch_constructor_args():
    sig = inspect.signature(controlflow::Branch.__init__)
    params = list(sig.parameters.keys())



def test_controlflow::command_is_not_abstract():
    assert not inspect.isabstract(controlflow::Command)


def test_controlflow::command_constructor_exists():
    assert callable(controlflow::Command.__init__)


def test_controlflow::command_constructor_args():
    sig = inspect.signature(controlflow::Command.__init__)
    params = list(sig.parameters.keys())



def test_controlflow::graph_is_not_abstract():
    assert not inspect.isabstract(controlflow::Graph)


def test_controlflow::graph_constructor_exists():
    assert callable(controlflow::Graph.__init__)


def test_controlflow::graph_constructor_args():
    sig = inspect.signature(controlflow::Graph.__init__)
    params = list(sig.parameters.keys())



def test_controlflow::node_is_not_abstract():
    assert not inspect.isabstract(controlflow::Node)


def test_controlflow::node_constructor_exists():
    assert callable(controlflow::Node.__init__)


def test_controlflow::node_constructor_args():
    sig = inspect.signature(controlflow::Node.__init__)
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
Node_strategy = st.builds(
    Node,
)
controlflow::Branch_strategy = st.builds(
    controlflow::Branch,
)
controlflow::Command_strategy = st.builds(
    controlflow::Command,
)
controlflow::Graph_strategy = st.builds(
    controlflow::Graph,
)
controlflow::Node_strategy = st.builds(
    controlflow::Node,
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=controlflow::Branch_strategy)
@settings(max_examples=50)
def test_controlflow::branch_instantiation(instance):
    assert isinstance(instance, controlflow::Branch)

@given(instance=controlflow::Command_strategy)
@settings(max_examples=50)
def test_controlflow::command_instantiation(instance):
    assert isinstance(instance, controlflow::Command)

@given(instance=controlflow::Graph_strategy)
@settings(max_examples=50)
def test_controlflow::graph_instantiation(instance):
    assert isinstance(instance, controlflow::Graph)

@given(instance=controlflow::Node_strategy)
@settings(max_examples=50)
def test_controlflow::node_instantiation(instance):
    assert isinstance(instance, controlflow::Node)
