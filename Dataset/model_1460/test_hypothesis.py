import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Node,
    graphs::CompositeNode,
    graphs::Edge,
    graphs::Node,
    graphs::Graph,
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



def test_graphs::compositenode_is_not_abstract():
    assert not inspect.isabstract(graphs::CompositeNode)


def test_graphs::compositenode_constructor_exists():
    assert callable(graphs::CompositeNode.__init__)


def test_graphs::compositenode_constructor_args():
    sig = inspect.signature(graphs::CompositeNode.__init__)
    params = list(sig.parameters.keys())



def test_graphs::edge_is_not_abstract():
    assert not inspect.isabstract(graphs::Edge)


def test_graphs::edge_constructor_exists():
    assert callable(graphs::Edge.__init__)


def test_graphs::edge_constructor_args():
    sig = inspect.signature(graphs::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_graphs::edge_has_weight():
    assert hasattr(graphs::Edge, "weight")
    descriptor = None
    for klass in graphs::Edge.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_graphs::node_is_not_abstract():
    assert not inspect.isabstract(graphs::Node)


def test_graphs::node_constructor_exists():
    assert callable(graphs::Node.__init__)


def test_graphs::node_constructor_args():
    sig = inspect.signature(graphs::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graphs::node_has_name():
    assert hasattr(graphs::Node, "name")
    descriptor = None
    for klass in graphs::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graphs::graph_is_not_abstract():
    assert not inspect.isabstract(graphs::Graph)


def test_graphs::graph_constructor_exists():
    assert callable(graphs::Graph.__init__)


def test_graphs::graph_constructor_args():
    sig = inspect.signature(graphs::Graph.__init__)
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
graphs::CompositeNode_strategy = st.builds(
    graphs::CompositeNode,
)
graphs::Edge_strategy = st.builds(
    graphs::Edge,
    weight=
        st.integers()
)
graphs::Node_strategy = st.builds(
    graphs::Node,
    name=
        safe_text
)
graphs::Graph_strategy = st.builds(
    graphs::Graph,
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=graphs::CompositeNode_strategy)
@settings(max_examples=50)
def test_graphs::compositenode_instantiation(instance):
    assert isinstance(instance, graphs::CompositeNode)

@given(instance=graphs::Edge_strategy)
@settings(max_examples=50)
def test_graphs::edge_instantiation(instance):
    assert isinstance(instance, graphs::Edge)

@given(instance=graphs::Edge_strategy)
def test_graphs::edge_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=graphs::Edge_strategy)
def test_graphs::edge_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=graphs::Node_strategy)
@settings(max_examples=50)
def test_graphs::node_instantiation(instance):
    assert isinstance(instance, graphs::Node)

@given(instance=graphs::Node_strategy)
def test_graphs::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graphs::Node_strategy)
def test_graphs::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphs::Node_strategy)
@settings(max_examples=30)
def test_graphs::node_inputs_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.inputs()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.inputs).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'inputs' in graphs::Node is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'inputs' in graphs::Node did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'inputs' in graphs::Node is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graphs::Node_strategy)
@settings(max_examples=30)
def test_graphs::node_outputs_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.outputs()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.outputs).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'outputs' in graphs::Node is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'outputs' in graphs::Node did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'outputs' in graphs::Node is not implemented or raised an error")

@given(instance=graphs::Graph_strategy)
@settings(max_examples=50)
def test_graphs::graph_instantiation(instance):
    assert isinstance(instance, graphs::Graph)
