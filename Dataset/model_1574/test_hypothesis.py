import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    graph_Named,
    graph_Entry,
    GraphElement,
    Typed,
    graph_GraphElement,
    graph_Vertex,
    graph_Edge,
    Named,
    graph_Label,
    graph_Typed,
    graph_Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_graph_entry_is_not_abstract():
    assert not inspect.isabstract(graph_Entry)


def test_graph_entry_constructor_exists():
    assert callable(graph_Entry.__init__)


def test_graph_entry_constructor_args():
    sig = inspect.signature(graph_Entry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_graph_entry_has_key():
    assert hasattr(graph_Entry, "key")
    descriptor = None
    for klass in graph_Entry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_graph_entry_has_value():
    assert hasattr(graph_Entry, "value")
    descriptor = None
    for klass in graph_Entry.__mro__:
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



def test_graph_graphelement_is_not_abstract():
    assert not inspect.isabstract(graph_GraphElement)


def test_graph_graphelement_constructor_exists():
    assert callable(graph_GraphElement.__init__)


def test_graph_graphelement_constructor_args():
    sig = inspect.signature(graph_GraphElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_graph_graphelement_has_id():
    assert hasattr(graph_GraphElement, "id")
    descriptor = None
    for klass in graph_GraphElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_graph_vertex_is_not_abstract():
    assert not inspect.isabstract(graph_Vertex)


def test_graph_vertex_constructor_exists():
    assert callable(graph_Vertex.__init__)


def test_graph_vertex_constructor_args():
    sig = inspect.signature(graph_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_graph_edge_is_not_abstract():
    assert not inspect.isabstract(graph_Edge)


def test_graph_edge_constructor_exists():
    assert callable(graph_Edge.__init__)


def test_graph_edge_constructor_args():
    sig = inspect.signature(graph_Edge.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_graph_label_is_not_abstract():
    assert not inspect.isabstract(graph_Label)


def test_graph_label_constructor_exists():
    assert callable(graph_Label.__init__)


def test_graph_label_constructor_args():
    sig = inspect.signature(graph_Label.__init__)
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
    assert "direct" in params, "Missing parameter 'direct'"

def test_graph_graph_has_direct():
    assert hasattr(graph_Graph, "direct")
    descriptor = None
    for klass in graph_Graph.__mro__:
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
graph_Named_strategy = st.builds(
    graph_Named,
    name=
        safe_text
)
graph_Entry_strategy = st.builds(
    graph_Entry,
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
graph_GraphElement_strategy = st.builds(
    graph_GraphElement,
    id=
        st.integers()
)
graph_Vertex_strategy = st.builds(
    graph_Vertex,
)
graph_Edge_strategy = st.builds(
    graph_Edge,
)
Named_strategy = st.builds(
    Named,
)
graph_Label_strategy = st.builds(
    graph_Label,
)
graph_Typed_strategy = st.builds(
    graph_Typed,
    type=
        safe_text
)
graph_Graph_strategy = st.builds(
    graph_Graph,
    direct=
        st.booleans()
)

@given(instance=graph_Named_strategy)
@settings(max_examples=50)
def test_graph_named_instantiation(instance):
    assert isinstance(instance, graph_Named)



@given(instance=graph_Named_strategy)
def test_graph_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph_Entry_strategy)
@settings(max_examples=50)
def test_graph_entry_instantiation(instance):
    assert isinstance(instance, graph_Entry)



@given(instance=graph_Entry_strategy)
def test_graph_entry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=graph_Entry_strategy)
def test_graph_entry_value_setter(instance):
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

@given(instance=graph_GraphElement_strategy)
@settings(max_examples=50)
def test_graph_graphelement_instantiation(instance):
    assert isinstance(instance, graph_GraphElement)



@given(instance=graph_GraphElement_strategy)
def test_graph_graphelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=graph_Vertex_strategy)
@settings(max_examples=50)
def test_graph_vertex_instantiation(instance):
    assert isinstance(instance, graph_Vertex)

@given(instance=graph_Edge_strategy)
@settings(max_examples=50)
def test_graph_edge_instantiation(instance):
    assert isinstance(instance, graph_Edge)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=graph_Label_strategy)
@settings(max_examples=50)
def test_graph_label_instantiation(instance):
    assert isinstance(instance, graph_Label)

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



@given(instance=graph_Graph_strategy)
def test_graph_graph_direct_setter(instance):
    original = instance.direct
    instance.direct = original
    assert instance.direct == original
