import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    graph::Named,
    graph::Entry,
    GraphElement,
    Typed,
    graph::GraphElement,
    graph::Vertex,
    graph::Edge,
    Named,
    graph::Typed,
    graph::Label,
    graph::Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph::named_is_not_abstract():
    assert not inspect.isabstract(graph::Named)


def test_graph::named_constructor_exists():
    assert callable(graph::Named.__init__)


def test_graph::named_constructor_args():
    sig = inspect.signature(graph::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph::named_has_name():
    assert hasattr(graph::Named, "name")
    descriptor = None
    for klass in graph::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph::entry_is_not_abstract():
    assert not inspect.isabstract(graph::Entry)


def test_graph::entry_constructor_exists():
    assert callable(graph::Entry.__init__)


def test_graph::entry_constructor_args():
    sig = inspect.signature(graph::Entry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_graph::entry_has_key():
    assert hasattr(graph::Entry, "key")
    descriptor = None
    for klass in graph::Entry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_graph::entry_has_value():
    assert hasattr(graph::Entry, "value")
    descriptor = None
    for klass in graph::Entry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_graphelement_is_not_abstract():
    assert not inspect.isabstract(GraphElement)


def test_graphelement_constructor_exists():
    assert callable(GraphElement.__init__)


def test_graphelement_constructor_args():
    sig = inspect.signature(GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_typed_is_not_abstract():
    assert not inspect.isabstract(Typed)


def test_typed_constructor_exists():
    assert callable(Typed.__init__)


def test_typed_constructor_args():
    sig = inspect.signature(Typed.__init__)
    params = list(sig.parameters.keys())



def test_graph::graphelement_is_not_abstract():
    assert not inspect.isabstract(graph::GraphElement)


def test_graph::graphelement_constructor_exists():
    assert callable(graph::GraphElement.__init__)


def test_graph::graphelement_constructor_args():
    sig = inspect.signature(graph::GraphElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_graph::graphelement_has_id():
    assert hasattr(graph::GraphElement, "id")
    descriptor = None
    for klass in graph::GraphElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_graph::vertex_is_not_abstract():
    assert not inspect.isabstract(graph::Vertex)


def test_graph::vertex_constructor_exists():
    assert callable(graph::Vertex.__init__)


def test_graph::vertex_constructor_args():
    sig = inspect.signature(graph::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_graph::edge_is_not_abstract():
    assert not inspect.isabstract(graph::Edge)


def test_graph::edge_constructor_exists():
    assert callable(graph::Edge.__init__)


def test_graph::edge_constructor_args():
    sig = inspect.signature(graph::Edge.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_graph::typed_is_not_abstract():
    assert not inspect.isabstract(graph::Typed)


def test_graph::typed_constructor_exists():
    assert callable(graph::Typed.__init__)


def test_graph::typed_constructor_args():
    sig = inspect.signature(graph::Typed.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_graph::typed_has_type():
    assert hasattr(graph::Typed, "type")
    descriptor = None
    for klass in graph::Typed.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_graph::label_is_not_abstract():
    assert not inspect.isabstract(graph::Label)


def test_graph::label_constructor_exists():
    assert callable(graph::Label.__init__)


def test_graph::label_constructor_args():
    sig = inspect.signature(graph::Label.__init__)
    params = list(sig.parameters.keys())



def test_graph::graph_is_not_abstract():
    assert not inspect.isabstract(graph::Graph)


def test_graph::graph_constructor_exists():
    assert callable(graph::Graph.__init__)


def test_graph::graph_constructor_args():
    sig = inspect.signature(graph::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "direct" in params, "Missing parameter 'direct'"

def test_graph::graph_has_direct():
    assert hasattr(graph::Graph, "direct")
    descriptor = None
    for klass in graph::Graph.__mro__:
        if "direct" in klass.__dict__:
            descriptor = klass.__dict__["direct"]
            break
    assert isinstance(descriptor, property)


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
graph::Named_strategy = st.builds(
    graph::Named,
    name=
        safe_text
)
graph::Entry_strategy = st.builds(
    graph::Entry,
    key=
        safe_text,
    value=
        safe_text
)
GraphElement_strategy = st.builds(
    GraphElement,
)
Typed_strategy = st.builds(
    Typed,
)
graph::GraphElement_strategy = st.builds(
    graph::GraphElement,
    id=
        st.integers()
)
graph::Vertex_strategy = st.builds(
    graph::Vertex,
)
graph::Edge_strategy = st.builds(
    graph::Edge,
)
Named_strategy = st.builds(
    Named,
)
graph::Typed_strategy = st.builds(
    graph::Typed,
    type=
        safe_text
)
graph::Label_strategy = st.builds(
    graph::Label,
)
graph::Graph_strategy = st.builds(
    graph::Graph,
    direct=
        st.booleans()
)

@given(instance=graph::Named_strategy)
@settings(max_examples=50)
def test_graph::named_instantiation(instance):
    assert isinstance(instance, graph::Named)

@given(instance=graph::Named_strategy)
def test_graph::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graph::Named_strategy)
def test_graph::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph::Entry_strategy)
@settings(max_examples=50)
def test_graph::entry_instantiation(instance):
    assert isinstance(instance, graph::Entry)

@given(instance=graph::Entry_strategy)
def test_graph::entry_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=graph::Entry_strategy)
def test_graph::entry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=graph::Entry_strategy)
def test_graph::entry_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=graph::Entry_strategy)
def test_graph::entry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=GraphElement_strategy)
@settings(max_examples=50)
def test_graphelement_instantiation(instance):
    assert isinstance(instance, GraphElement)

@given(instance=Typed_strategy)
@settings(max_examples=50)
def test_typed_instantiation(instance):
    assert isinstance(instance, Typed)

@given(instance=graph::GraphElement_strategy)
@settings(max_examples=50)
def test_graph::graphelement_instantiation(instance):
    assert isinstance(instance, graph::GraphElement)

@given(instance=graph::GraphElement_strategy)
def test_graph::graphelement_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=graph::GraphElement_strategy)
def test_graph::graphelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=graph::Vertex_strategy)
@settings(max_examples=50)
def test_graph::vertex_instantiation(instance):
    assert isinstance(instance, graph::Vertex)

@given(instance=graph::Edge_strategy)
@settings(max_examples=50)
def test_graph::edge_instantiation(instance):
    assert isinstance(instance, graph::Edge)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=graph::Typed_strategy)
@settings(max_examples=50)
def test_graph::typed_instantiation(instance):
    assert isinstance(instance, graph::Typed)

@given(instance=graph::Typed_strategy)
def test_graph::typed_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=graph::Typed_strategy)
def test_graph::typed_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=graph::Label_strategy)
@settings(max_examples=50)
def test_graph::label_instantiation(instance):
    assert isinstance(instance, graph::Label)

@given(instance=graph::Graph_strategy)
@settings(max_examples=50)
def test_graph::graph_instantiation(instance):
    assert isinstance(instance, graph::Graph)

@given(instance=graph::Graph_strategy)
def test_graph::graph_direct_type(instance):
    assert isinstance(instance.direct, bool)


@given(instance=graph::Graph_strategy)
def test_graph::graph_direct_setter(instance):
    original = instance.direct
    instance.direct = original
    assert instance.direct == original
