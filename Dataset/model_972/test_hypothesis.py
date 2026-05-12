import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Typed,
    graph_Named,
    graph_Edge,
    graph_Node,
    Named,
    graph_Typed,
    graph_Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typed_is_not_abstract():
    assert not inspect.isabstract(Typed)


def test_typed_constructor_exists():
    assert callable(Typed.__init__)


def test_typed_constructor_args():
    sig = inspect.signature(Typed.__init__)
    params = list(sig.parameters.keys())



def test_graph_named_is_not_abstract():
    assert not inspect.isabstract(graph_Named)


def test_graph_named_constructor_exists():
    assert callable(graph_Named.__init__)


def test_graph_named_constructor_args():
    sig = inspect.signature(graph_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph_named_has_name():
    assert hasattr(graph_Named, "name")
    descriptor = None
    for klass in graph_Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph_edge_is_not_abstract():
    assert not inspect.isabstract(graph_Edge)


def test_graph_edge_constructor_exists():
    assert callable(graph_Edge.__init__)


def test_graph_edge_constructor_args():
    sig = inspect.signature(graph_Edge.__init__)
    params = list(sig.parameters.keys())



def test_graph_node_is_not_abstract():
    assert not inspect.isabstract(graph_Node)


def test_graph_node_constructor_exists():
    assert callable(graph_Node.__init__)


def test_graph_node_constructor_args():
    sig = inspect.signature(graph_Node.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_graph_typed_is_not_abstract():
    assert not inspect.isabstract(graph_Typed)


def test_graph_typed_constructor_exists():
    assert callable(graph_Typed.__init__)


def test_graph_typed_constructor_args():
    sig = inspect.signature(graph_Typed.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_graph_typed_has_type():
    assert hasattr(graph_Typed, "type")
    descriptor = None
    for klass in graph_Typed.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_graph_graph_is_not_abstract():
    assert not inspect.isabstract(graph_Graph)


def test_graph_graph_constructor_exists():
    assert callable(graph_Graph.__init__)


def test_graph_graph_constructor_args():
    sig = inspect.signature(graph_Graph.__init__)
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
Typed_strategy = st.builds(
    Typed,
)
graph_Named_strategy = st.builds(
    graph_Named,
    name=
        safe_text
)
graph_Edge_strategy = st.builds(
    graph_Edge,
)
graph_Node_strategy = st.builds(
    graph_Node,
)
Named_strategy = st.builds(
    Named,
)
graph_Typed_strategy = st.builds(
    graph_Typed,
    type=
        safe_text
)
graph_Graph_strategy = st.builds(
    graph_Graph,
)

@given(instance=Typed_strategy)
@settings(max_examples=50)
def test_typed_instantiation(instance):
    assert isinstance(instance, Typed)

@given(instance=graph_Named_strategy)
@settings(max_examples=50)
def test_graph_named_instantiation(instance):
    assert isinstance(instance, graph_Named)



@given(instance=graph_Named_strategy)
def test_graph_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph_Edge_strategy)
@settings(max_examples=50)
def test_graph_edge_instantiation(instance):
    assert isinstance(instance, graph_Edge)

@given(instance=graph_Node_strategy)
@settings(max_examples=50)
def test_graph_node_instantiation(instance):
    assert isinstance(instance, graph_Node)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=graph_Typed_strategy)
@settings(max_examples=50)
def test_graph_typed_instantiation(instance):
    assert isinstance(instance, graph_Typed)



@given(instance=graph_Typed_strategy)
def test_graph_typed_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=graph_Graph_strategy)
@settings(max_examples=50)
def test_graph_graph_instantiation(instance):
    assert isinstance(instance, graph_Graph)
