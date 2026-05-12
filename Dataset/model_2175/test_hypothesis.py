import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Node,
    controlflow_Branch,
    controlflow_Command,
    controlflow_Graph,
    controlflow_Node,
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



def test_controlflow_branch_is_not_abstract():
    assert not inspect.isabstract(controlflow_Branch)


def test_controlflow_branch_constructor_exists():
    assert callable(controlflow_Branch.__init__)


def test_controlflow_branch_constructor_args():
    sig = inspect.signature(controlflow_Branch.__init__)
    params = list(sig.parameters.keys())



def test_controlflow_command_is_not_abstract():
    assert not inspect.isabstract(controlflow_Command)


def test_controlflow_command_constructor_exists():
    assert callable(controlflow_Command.__init__)


def test_controlflow_command_constructor_args():
    sig = inspect.signature(controlflow_Command.__init__)
    params = list(sig.parameters.keys())



def test_controlflow_graph_is_not_abstract():
    assert not inspect.isabstract(controlflow_Graph)


def test_controlflow_graph_constructor_exists():
    assert callable(controlflow_Graph.__init__)


def test_controlflow_graph_constructor_args():
    sig = inspect.signature(controlflow_Graph.__init__)
    params = list(sig.parameters.keys())



def test_controlflow_node_is_not_abstract():
    assert not inspect.isabstract(controlflow_Node)


def test_controlflow_node_constructor_exists():
    assert callable(controlflow_Node.__init__)


def test_controlflow_node_constructor_args():
    sig = inspect.signature(controlflow_Node.__init__)
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
controlflow_Branch_strategy = st.builds(
    controlflow_Branch,
)
controlflow_Command_strategy = st.builds(
    controlflow_Command,
)
controlflow_Graph_strategy = st.builds(
    controlflow_Graph,
)
controlflow_Node_strategy = st.builds(
    controlflow_Node,
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=controlflow_Branch_strategy)
@settings(max_examples=50)
def test_controlflow_branch_instantiation(instance):
    assert isinstance(instance, controlflow_Branch)

@given(instance=controlflow_Command_strategy)
@settings(max_examples=50)
def test_controlflow_command_instantiation(instance):
    assert isinstance(instance, controlflow_Command)

@given(instance=controlflow_Graph_strategy)
@settings(max_examples=50)
def test_controlflow_graph_instantiation(instance):
    assert isinstance(instance, controlflow_Graph)

@given(instance=controlflow_Node_strategy)
@settings(max_examples=50)
def test_controlflow_node_instantiation(instance):
    assert isinstance(instance, controlflow_Node)
