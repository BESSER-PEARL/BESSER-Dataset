import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    GraphMetaM::Model,
    GraphMetaM::Edge,
    GraphMetaM::Vertex,
    GraphMetaM::Graph,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graphmetam::model_is_not_abstract():
    assert not inspect.isabstract(GraphMetaM::Model)


def test_graphmetam::model_constructor_exists():
    assert callable(GraphMetaM::Model.__init__)


def test_graphmetam::model_constructor_args():
    sig = inspect.signature(GraphMetaM::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graphmetam::model_has_name():
    assert hasattr(GraphMetaM::Model, "name")
    descriptor = None
    for klass in GraphMetaM::Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graphmetam::edge_is_not_abstract():
    assert not inspect.isabstract(GraphMetaM::Edge)


def test_graphmetam::edge_constructor_exists():
    assert callable(GraphMetaM::Edge.__init__)


def test_graphmetam::edge_constructor_args():
    sig = inspect.signature(GraphMetaM::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "async_" in params, "Missing parameter 'async_'"
    assert "localPriority" in params, "Missing parameter 'localPriority'"
    assert "name" in params, "Missing parameter 'name'"
    assert "rName" in params, "Missing parameter 'rName'"

def test_graphmetam::edge_has_async_():
    assert hasattr(GraphMetaM::Edge, "async_")
    descriptor = None
    for klass in GraphMetaM::Edge.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_graphmetam::edge_has_localPriority():
    assert hasattr(GraphMetaM::Edge, "localPriority")
    descriptor = None
    for klass in GraphMetaM::Edge.__mro__:
        if "localPriority" in klass.__dict__:
            descriptor = klass.__dict__["localPriority"]
            break
    assert isinstance(descriptor, property)

def test_graphmetam::edge_has_name():
    assert hasattr(GraphMetaM::Edge, "name")
    descriptor = None
    for klass in GraphMetaM::Edge.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_graphmetam::edge_has_rName():
    assert hasattr(GraphMetaM::Edge, "rName")
    descriptor = None
    for klass in GraphMetaM::Edge.__mro__:
        if "rName" in klass.__dict__:
            descriptor = klass.__dict__["rName"]
            break
    assert isinstance(descriptor, property)



def test_graphmetam::vertex_is_not_abstract():
    assert not inspect.isabstract(GraphMetaM::Vertex)


def test_graphmetam::vertex_constructor_exists():
    assert callable(GraphMetaM::Vertex.__init__)


def test_graphmetam::vertex_constructor_args():
    sig = inspect.signature(GraphMetaM::Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "activity" in params, "Missing parameter 'activity'"
    assert "name" in params, "Missing parameter 'name'"
    assert "cycles" in params, "Missing parameter 'cycles'"
    assert "globalPriority" in params, "Missing parameter 'globalPriority'"
    assert "rName" in params, "Missing parameter 'rName'"
    assert "type" in params, "Missing parameter 'type'"

def test_graphmetam::vertex_has_activity():
    assert hasattr(GraphMetaM::Vertex, "activity")
    descriptor = None
    for klass in GraphMetaM::Vertex.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)

def test_graphmetam::vertex_has_name():
    assert hasattr(GraphMetaM::Vertex, "name")
    descriptor = None
    for klass in GraphMetaM::Vertex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_graphmetam::vertex_has_cycles():
    assert hasattr(GraphMetaM::Vertex, "cycles")
    descriptor = None
    for klass in GraphMetaM::Vertex.__mro__:
        if "cycles" in klass.__dict__:
            descriptor = klass.__dict__["cycles"]
            break
    assert isinstance(descriptor, property)

def test_graphmetam::vertex_has_globalPriority():
    assert hasattr(GraphMetaM::Vertex, "globalPriority")
    descriptor = None
    for klass in GraphMetaM::Vertex.__mro__:
        if "globalPriority" in klass.__dict__:
            descriptor = klass.__dict__["globalPriority"]
            break
    assert isinstance(descriptor, property)

def test_graphmetam::vertex_has_rName():
    assert hasattr(GraphMetaM::Vertex, "rName")
    descriptor = None
    for klass in GraphMetaM::Vertex.__mro__:
        if "rName" in klass.__dict__:
            descriptor = klass.__dict__["rName"]
            break
    assert isinstance(descriptor, property)

def test_graphmetam::vertex_has_type():
    assert hasattr(GraphMetaM::Vertex, "type")
    descriptor = None
    for klass in GraphMetaM::Vertex.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_graphmetam::graph_is_not_abstract():
    assert not inspect.isabstract(GraphMetaM::Graph)


def test_graphmetam::graph_constructor_exists():
    assert callable(GraphMetaM::Graph.__init__)


def test_graphmetam::graph_constructor_args():
    sig = inspect.signature(GraphMetaM::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "cycles" in params, "Missing parameter 'cycles'"
    assert "rName" in params, "Missing parameter 'rName'"
    assert "name" in params, "Missing parameter 'name'"

def test_graphmetam::graph_has_cycles():
    assert hasattr(GraphMetaM::Graph, "cycles")
    descriptor = None
    for klass in GraphMetaM::Graph.__mro__:
        if "cycles" in klass.__dict__:
            descriptor = klass.__dict__["cycles"]
            break
    assert isinstance(descriptor, property)

def test_graphmetam::graph_has_rName():
    assert hasattr(GraphMetaM::Graph, "rName")
    descriptor = None
    for klass in GraphMetaM::Graph.__mro__:
        if "rName" in klass.__dict__:
            descriptor = klass.__dict__["rName"]
            break
    assert isinstance(descriptor, property)

def test_graphmetam::graph_has_name():
    assert hasattr(GraphMetaM::Graph, "name")
    descriptor = None
    for klass in GraphMetaM::Graph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
GraphMetaM::Model_strategy = st.builds(
    GraphMetaM::Model,
    name=
        safe_text
)
GraphMetaM::Edge_strategy = st.builds(
    GraphMetaM::Edge,
    async_=
        st.booleans(),
    localPriority=
        st.integers(),
    name=
        safe_text,
    rName=
        safe_text
)
GraphMetaM::Vertex_strategy = st.builds(
    GraphMetaM::Vertex,
    activity=
        safe_text,
    name=
        safe_text,
    cycles=
        st.integers(),
    globalPriority=
        st.integers(),
    rName=
        safe_text,
    type=
        safe_text
)
GraphMetaM::Graph_strategy = st.builds(
    GraphMetaM::Graph,
    cycles=
        st.integers(),
    rName=
        safe_text,
    name=
        safe_text
)

@given(instance=GraphMetaM::Model_strategy)
@settings(max_examples=50)
def test_graphmetam::model_instantiation(instance):
    assert isinstance(instance, GraphMetaM::Model)

@given(instance=GraphMetaM::Model_strategy)
def test_graphmetam::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=GraphMetaM::Model_strategy)
def test_graphmetam::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=GraphMetaM::Edge_strategy)
@settings(max_examples=50)
def test_graphmetam::edge_instantiation(instance):
    assert isinstance(instance, GraphMetaM::Edge)

@given(instance=GraphMetaM::Edge_strategy)
def test_graphmetam::edge_async__type(instance):
    assert isinstance(instance.async_, bool)


@given(instance=GraphMetaM::Edge_strategy)
def test_graphmetam::edge_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original

@given(instance=GraphMetaM::Edge_strategy)
def test_graphmetam::edge_localPriority_type(instance):
    assert isinstance(instance.localPriority, int)


@given(instance=GraphMetaM::Edge_strategy)
def test_graphmetam::edge_localPriority_setter(instance):
    original = instance.localPriority
    instance.localPriority = original
    assert instance.localPriority == original

@given(instance=GraphMetaM::Edge_strategy)
def test_graphmetam::edge_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=GraphMetaM::Edge_strategy)
def test_graphmetam::edge_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=GraphMetaM::Edge_strategy)
def test_graphmetam::edge_rName_type(instance):
    assert isinstance(instance.rName, str)


@given(instance=GraphMetaM::Edge_strategy)
def test_graphmetam::edge_rName_setter(instance):
    original = instance.rName
    instance.rName = original
    assert instance.rName == original

@given(instance=GraphMetaM::Vertex_strategy)
@settings(max_examples=50)
def test_graphmetam::vertex_instantiation(instance):
    assert isinstance(instance, GraphMetaM::Vertex)

@given(instance=GraphMetaM::Vertex_strategy)
def test_graphmetam::vertex_activity_type(instance):
    assert isinstance(instance.activity, str)


@given(instance=GraphMetaM::Vertex_strategy)
def test_graphmetam::vertex_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original

@given(instance=GraphMetaM::Vertex_strategy)
def test_graphmetam::vertex_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=GraphMetaM::Vertex_strategy)
def test_graphmetam::vertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=GraphMetaM::Vertex_strategy)
def test_graphmetam::vertex_cycles_type(instance):
    assert isinstance(instance.cycles, int)


@given(instance=GraphMetaM::Vertex_strategy)
def test_graphmetam::vertex_cycles_setter(instance):
    original = instance.cycles
    instance.cycles = original
    assert instance.cycles == original

@given(instance=GraphMetaM::Vertex_strategy)
def test_graphmetam::vertex_globalPriority_type(instance):
    assert isinstance(instance.globalPriority, int)


@given(instance=GraphMetaM::Vertex_strategy)
def test_graphmetam::vertex_globalPriority_setter(instance):
    original = instance.globalPriority
    instance.globalPriority = original
    assert instance.globalPriority == original

@given(instance=GraphMetaM::Vertex_strategy)
def test_graphmetam::vertex_rName_type(instance):
    assert isinstance(instance.rName, str)


@given(instance=GraphMetaM::Vertex_strategy)
def test_graphmetam::vertex_rName_setter(instance):
    original = instance.rName
    instance.rName = original
    assert instance.rName == original

@given(instance=GraphMetaM::Vertex_strategy)
def test_graphmetam::vertex_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=GraphMetaM::Vertex_strategy)
def test_graphmetam::vertex_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=GraphMetaM::Graph_strategy)
@settings(max_examples=50)
def test_graphmetam::graph_instantiation(instance):
    assert isinstance(instance, GraphMetaM::Graph)

@given(instance=GraphMetaM::Graph_strategy)
def test_graphmetam::graph_cycles_type(instance):
    assert isinstance(instance.cycles, int)


@given(instance=GraphMetaM::Graph_strategy)
def test_graphmetam::graph_cycles_setter(instance):
    original = instance.cycles
    instance.cycles = original
    assert instance.cycles == original

@given(instance=GraphMetaM::Graph_strategy)
def test_graphmetam::graph_rName_type(instance):
    assert isinstance(instance.rName, str)


@given(instance=GraphMetaM::Graph_strategy)
def test_graphmetam::graph_rName_setter(instance):
    original = instance.rName
    instance.rName = original
    assert instance.rName == original

@given(instance=GraphMetaM::Graph_strategy)
def test_graphmetam::graph_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=GraphMetaM::Graph_strategy)
def test_graphmetam::graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
