import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    GraphMetaM_Model,
    GraphMetaM_Edge,
    GraphMetaM_Vertex,
    GraphMetaM_Graph,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graphmetam_model_is_not_abstract():
    assert not inspect.isabstract(GraphMetaM_Model)


def test_graphmetam_model_constructor_exists():
    assert callable(GraphMetaM_Model.__init__)


def test_graphmetam_model_constructor_args():
    sig = inspect.signature(GraphMetaM_Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graphmetam_model_has_name():
    assert hasattr(GraphMetaM_Model, "name")
    descriptor = None
    for klass in GraphMetaM_Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graphmetam_edge_is_not_abstract():
    assert not inspect.isabstract(GraphMetaM_Edge)


def test_graphmetam_edge_constructor_exists():
    assert callable(GraphMetaM_Edge.__init__)


def test_graphmetam_edge_constructor_args():
    sig = inspect.signature(GraphMetaM_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "localPriority" in params, "Missing parameter 'localPriority'"
    assert "rName" in params, "Missing parameter 'rName'"
    assert "async_" in params, "Missing parameter 'async_'"
    assert "name" in params, "Missing parameter 'name'"

def test_graphmetam_edge_has_localPriority():
    assert hasattr(GraphMetaM_Edge, "localPriority")
    descriptor = None
    for klass in GraphMetaM_Edge.__mro__:
        if "localPriority" in klass.__dict__:
            descriptor = klass.__dict__["localPriority"]
            break
    assert isinstance(descriptor, property)

def test_graphmetam_edge_has_rName():
    assert hasattr(GraphMetaM_Edge, "rName")
    descriptor = None
    for klass in GraphMetaM_Edge.__mro__:
        if "rName" in klass.__dict__:
            descriptor = klass.__dict__["rName"]
            break
    assert isinstance(descriptor, property)

def test_graphmetam_edge_has_async_():
    assert hasattr(GraphMetaM_Edge, "async_")
    descriptor = None
    for klass in GraphMetaM_Edge.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_graphmetam_edge_has_name():
    assert hasattr(GraphMetaM_Edge, "name")
    descriptor = None
    for klass in GraphMetaM_Edge.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graphmetam_vertex_is_not_abstract():
    assert not inspect.isabstract(GraphMetaM_Vertex)


def test_graphmetam_vertex_constructor_exists():
    assert callable(GraphMetaM_Vertex.__init__)


def test_graphmetam_vertex_constructor_args():
    sig = inspect.signature(GraphMetaM_Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "globalPriority" in params, "Missing parameter 'globalPriority'"
    assert "activity" in params, "Missing parameter 'activity'"
    assert "cycles" in params, "Missing parameter 'cycles'"
    assert "name" in params, "Missing parameter 'name'"
    assert "rName" in params, "Missing parameter 'rName'"
    assert "type" in params, "Missing parameter 'type'"

def test_graphmetam_vertex_has_globalPriority():
    assert hasattr(GraphMetaM_Vertex, "globalPriority")
    descriptor = None
    for klass in GraphMetaM_Vertex.__mro__:
        if "globalPriority" in klass.__dict__:
            descriptor = klass.__dict__["globalPriority"]
            break
    assert isinstance(descriptor, property)

def test_graphmetam_vertex_has_activity():
    assert hasattr(GraphMetaM_Vertex, "activity")
    descriptor = None
    for klass in GraphMetaM_Vertex.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)

def test_graphmetam_vertex_has_cycles():
    assert hasattr(GraphMetaM_Vertex, "cycles")
    descriptor = None
    for klass in GraphMetaM_Vertex.__mro__:
        if "cycles" in klass.__dict__:
            descriptor = klass.__dict__["cycles"]
            break
    assert isinstance(descriptor, property)

def test_graphmetam_vertex_has_name():
    assert hasattr(GraphMetaM_Vertex, "name")
    descriptor = None
    for klass in GraphMetaM_Vertex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_graphmetam_vertex_has_rName():
    assert hasattr(GraphMetaM_Vertex, "rName")
    descriptor = None
    for klass in GraphMetaM_Vertex.__mro__:
        if "rName" in klass.__dict__:
            descriptor = klass.__dict__["rName"]
            break
    assert isinstance(descriptor, property)

def test_graphmetam_vertex_has_type():
    assert hasattr(GraphMetaM_Vertex, "type")
    descriptor = None
    for klass in GraphMetaM_Vertex.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_graphmetam_graph_is_not_abstract():
    assert not inspect.isabstract(GraphMetaM_Graph)


def test_graphmetam_graph_constructor_exists():
    assert callable(GraphMetaM_Graph.__init__)


def test_graphmetam_graph_constructor_args():
    sig = inspect.signature(GraphMetaM_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "rName" in params, "Missing parameter 'rName'"
    assert "cycles" in params, "Missing parameter 'cycles'"

def test_graphmetam_graph_has_name():
    assert hasattr(GraphMetaM_Graph, "name")
    descriptor = None
    for klass in GraphMetaM_Graph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_graphmetam_graph_has_rName():
    assert hasattr(GraphMetaM_Graph, "rName")
    descriptor = None
    for klass in GraphMetaM_Graph.__mro__:
        if "rName" in klass.__dict__:
            descriptor = klass.__dict__["rName"]
            break
    assert isinstance(descriptor, property)

def test_graphmetam_graph_has_cycles():
    assert hasattr(GraphMetaM_Graph, "cycles")
    descriptor = None
    for klass in GraphMetaM_Graph.__mro__:
        if "cycles" in klass.__dict__:
            descriptor = klass.__dict__["cycles"]
            break
    assert isinstance(descriptor, property)

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "or_",
        "and_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"


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
GraphMetaM_Model_strategy = st.builds(
    GraphMetaM_Model,
    name=
        safe_text
)
GraphMetaM_Edge_strategy = st.builds(
    GraphMetaM_Edge,
    localPriority=
        st.integers(),
    rName=
        safe_text,
    async_=
        st.booleans(),
    name=
        safe_text
)
GraphMetaM_Vertex_strategy = st.builds(
    GraphMetaM_Vertex,
    globalPriority=
        st.integers(),
    activity=
        safe_text,
    cycles=
        st.integers(),
    name=
        safe_text,
    rName=
        safe_text,
    type=
        safe_text
)
GraphMetaM_Graph_strategy = st.builds(
    GraphMetaM_Graph,
    name=
        safe_text,
    rName=
        safe_text,
    cycles=
        st.integers()
)

@given(instance=GraphMetaM_Model_strategy)
@settings(max_examples=50)
def test_graphmetam_model_instantiation(instance):
    assert isinstance(instance, GraphMetaM_Model)



@given(instance=GraphMetaM_Model_strategy)
def test_graphmetam_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=GraphMetaM_Edge_strategy)
@settings(max_examples=50)
def test_graphmetam_edge_instantiation(instance):
    assert isinstance(instance, GraphMetaM_Edge)



@given(instance=GraphMetaM_Edge_strategy)
def test_graphmetam_edge_localPriority_setter(instance):
    original = instance.localPriority
    instance.localPriority = original
    assert instance.localPriority == original



@given(instance=GraphMetaM_Edge_strategy)
def test_graphmetam_edge_rName_setter(instance):
    original = instance.rName
    instance.rName = original
    assert instance.rName == original



@given(instance=GraphMetaM_Edge_strategy)
def test_graphmetam_edge_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original



@given(instance=GraphMetaM_Edge_strategy)
def test_graphmetam_edge_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=GraphMetaM_Vertex_strategy)
@settings(max_examples=50)
def test_graphmetam_vertex_instantiation(instance):
    assert isinstance(instance, GraphMetaM_Vertex)



@given(instance=GraphMetaM_Vertex_strategy)
def test_graphmetam_vertex_globalPriority_setter(instance):
    original = instance.globalPriority
    instance.globalPriority = original
    assert instance.globalPriority == original



@given(instance=GraphMetaM_Vertex_strategy)
def test_graphmetam_vertex_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original



@given(instance=GraphMetaM_Vertex_strategy)
def test_graphmetam_vertex_cycles_setter(instance):
    original = instance.cycles
    instance.cycles = original
    assert instance.cycles == original



@given(instance=GraphMetaM_Vertex_strategy)
def test_graphmetam_vertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=GraphMetaM_Vertex_strategy)
def test_graphmetam_vertex_rName_setter(instance):
    original = instance.rName
    instance.rName = original
    assert instance.rName == original



@given(instance=GraphMetaM_Vertex_strategy)
def test_graphmetam_vertex_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=GraphMetaM_Graph_strategy)
@settings(max_examples=50)
def test_graphmetam_graph_instantiation(instance):
    assert isinstance(instance, GraphMetaM_Graph)



@given(instance=GraphMetaM_Graph_strategy)
def test_graphmetam_graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=GraphMetaM_Graph_strategy)
def test_graphmetam_graph_rName_setter(instance):
    original = instance.rName
    instance.rName = original
    assert instance.rName == original



@given(instance=GraphMetaM_Graph_strategy)
def test_graphmetam_graph_cycles_setter(instance):
    original = instance.cycles
    instance.cycles = original
    assert instance.cycles == original
