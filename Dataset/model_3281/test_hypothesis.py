import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sm::Graph,
    Mark,
    sm::Observation,
    sm::Mark,
    sm::Edge,
    sm::Node,
    Graph,
    sm::StateMachine,
    Edge,
    sm::Transition,
    Node,
    sm::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sm::graph_is_not_abstract():
    assert not inspect.isabstract(sm::Graph)


def test_sm::graph_constructor_exists():
    assert callable(sm::Graph.__init__)


def test_sm::graph_constructor_args():
    sig = inspect.signature(sm::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sm::graph_has_name():
    assert hasattr(sm::Graph, "name")
    descriptor = None
    for klass in sm::Graph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mark_is_not_abstract():
    assert not inspect.isabstract(Mark)


def test_mark_constructor_exists():
    assert callable(Mark.__init__)


def test_mark_constructor_args():
    sig = inspect.signature(Mark.__init__)
    params = list(sig.parameters.keys())



def test_sm::observation_is_not_abstract():
    assert not inspect.isabstract(sm::Observation)


def test_sm::observation_constructor_exists():
    assert callable(sm::Observation.__init__)


def test_sm::observation_constructor_args():
    sig = inspect.signature(sm::Observation.__init__)
    params = list(sig.parameters.keys())



def test_sm::mark_is_not_abstract():
    assert not inspect.isabstract(sm::Mark)


def test_sm::mark_constructor_exists():
    assert callable(sm::Mark.__init__)


def test_sm::mark_constructor_args():
    sig = inspect.signature(sm::Mark.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_sm::mark_has_time():
    assert hasattr(sm::Mark, "time")
    descriptor = None
    for klass in sm::Mark.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_sm::edge_is_not_abstract():
    assert not inspect.isabstract(sm::Edge)


def test_sm::edge_constructor_exists():
    assert callable(sm::Edge.__init__)


def test_sm::edge_constructor_args():
    sig = inspect.signature(sm::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sm::edge_has_name():
    assert hasattr(sm::Edge, "name")
    descriptor = None
    for klass in sm::Edge.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sm::node_is_not_abstract():
    assert not inspect.isabstract(sm::Node)


def test_sm::node_constructor_exists():
    assert callable(sm::Node.__init__)


def test_sm::node_constructor_args():
    sig = inspect.signature(sm::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sm::node_has_name():
    assert hasattr(sm::Node, "name")
    descriptor = None
    for klass in sm::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph_is_not_abstract():
    assert not inspect.isabstract(Graph)


def test_graph_constructor_exists():
    assert callable(Graph.__init__)


def test_graph_constructor_args():
    sig = inspect.signature(Graph.__init__)
    params = list(sig.parameters.keys())



def test_sm::statemachine_is_not_abstract():
    assert not inspect.isabstract(sm::StateMachine)


def test_sm::statemachine_constructor_exists():
    assert callable(sm::StateMachine.__init__)


def test_sm::statemachine_constructor_args():
    sig = inspect.signature(sm::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_sm::transition_is_not_abstract():
    assert not inspect.isabstract(sm::Transition)


def test_sm::transition_constructor_exists():
    assert callable(sm::Transition.__init__)


def test_sm::transition_constructor_args():
    sig = inspect.signature(sm::Transition.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_sm::state_is_not_abstract():
    assert not inspect.isabstract(sm::State)


def test_sm::state_constructor_exists():
    assert callable(sm::State.__init__)


def test_sm::state_constructor_args():
    sig = inspect.signature(sm::State.__init__)
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
sm::Graph_strategy = st.builds(
    sm::Graph,
    name=
        safe_text
)
Mark_strategy = st.builds(
    Mark,
)
sm::Observation_strategy = st.builds(
    sm::Observation,
)
sm::Mark_strategy = st.builds(
    sm::Mark,
    time=
        safe_text
)
sm::Edge_strategy = st.builds(
    sm::Edge,
    name=
        safe_text
)
sm::Node_strategy = st.builds(
    sm::Node,
    name=
        safe_text
)
Graph_strategy = st.builds(
    Graph,
)
sm::StateMachine_strategy = st.builds(
    sm::StateMachine,
)
Edge_strategy = st.builds(
    Edge,
)
sm::Transition_strategy = st.builds(
    sm::Transition,
)
Node_strategy = st.builds(
    Node,
)
sm::State_strategy = st.builds(
    sm::State,
)

@given(instance=sm::Graph_strategy)
@settings(max_examples=50)
def test_sm::graph_instantiation(instance):
    assert isinstance(instance, sm::Graph)

@given(instance=sm::Graph_strategy)
def test_sm::graph_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sm::Graph_strategy)
def test_sm::graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Mark_strategy)
@settings(max_examples=50)
def test_mark_instantiation(instance):
    assert isinstance(instance, Mark)

@given(instance=sm::Observation_strategy)
@settings(max_examples=50)
def test_sm::observation_instantiation(instance):
    assert isinstance(instance, sm::Observation)

@given(instance=sm::Mark_strategy)
@settings(max_examples=50)
def test_sm::mark_instantiation(instance):
    assert isinstance(instance, sm::Mark)

@given(instance=sm::Mark_strategy)
def test_sm::mark_time_type(instance):
    assert isinstance(instance.time, str)


@given(instance=sm::Mark_strategy)
def test_sm::mark_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=sm::Edge_strategy)
@settings(max_examples=50)
def test_sm::edge_instantiation(instance):
    assert isinstance(instance, sm::Edge)

@given(instance=sm::Edge_strategy)
def test_sm::edge_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sm::Edge_strategy)
def test_sm::edge_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sm::Node_strategy)
@settings(max_examples=50)
def test_sm::node_instantiation(instance):
    assert isinstance(instance, sm::Node)

@given(instance=sm::Node_strategy)
def test_sm::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sm::Node_strategy)
def test_sm::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Graph_strategy)
@settings(max_examples=50)
def test_graph_instantiation(instance):
    assert isinstance(instance, Graph)

@given(instance=sm::StateMachine_strategy)
@settings(max_examples=50)
def test_sm::statemachine_instantiation(instance):
    assert isinstance(instance, sm::StateMachine)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=sm::Transition_strategy)
@settings(max_examples=50)
def test_sm::transition_instantiation(instance):
    assert isinstance(instance, sm::Transition)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=sm::State_strategy)
@settings(max_examples=50)
def test_sm::state_instantiation(instance):
    assert isinstance(instance, sm::State)
