import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sm_Graph,
    Mark,
    sm_Observation,
    sm_Mark,
    sm_Edge,
    sm_Node,
    Graph,
    sm_StateMachine,
    Edge,
    sm_Transition,
    Node,
    sm_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sm_graph_is_not_abstract():
    assert not inspect.isabstract(sm_Graph)


def test_sm_graph_constructor_exists():
    assert callable(sm_Graph.__init__)


def test_sm_graph_constructor_args():
    sig = inspect.signature(sm_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sm_graph_has_name():
    assert hasattr(sm_Graph, "name")
    descriptor = None
    for klass in sm_Graph.__mro__:
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



def test_sm_observation_is_not_abstract():
    assert not inspect.isabstract(sm_Observation)


def test_sm_observation_constructor_exists():
    assert callable(sm_Observation.__init__)


def test_sm_observation_constructor_args():
    sig = inspect.signature(sm_Observation.__init__)
    params = list(sig.parameters.keys())



def test_sm_mark_is_not_abstract():
    assert not inspect.isabstract(sm_Mark)


def test_sm_mark_constructor_exists():
    assert callable(sm_Mark.__init__)


def test_sm_mark_constructor_args():
    sig = inspect.signature(sm_Mark.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_sm_mark_has_time():
    assert hasattr(sm_Mark, "time")
    descriptor = None
    for klass in sm_Mark.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_sm_edge_is_not_abstract():
    assert not inspect.isabstract(sm_Edge)


def test_sm_edge_constructor_exists():
    assert callable(sm_Edge.__init__)


def test_sm_edge_constructor_args():
    sig = inspect.signature(sm_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sm_edge_has_name():
    assert hasattr(sm_Edge, "name")
    descriptor = None
    for klass in sm_Edge.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sm_node_is_not_abstract():
    assert not inspect.isabstract(sm_Node)


def test_sm_node_constructor_exists():
    assert callable(sm_Node.__init__)


def test_sm_node_constructor_args():
    sig = inspect.signature(sm_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sm_node_has_name():
    assert hasattr(sm_Node, "name")
    descriptor = None
    for klass in sm_Node.__mro__:
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



def test_sm_statemachine_is_not_abstract():
    assert not inspect.isabstract(sm_StateMachine)


def test_sm_statemachine_constructor_exists():
    assert callable(sm_StateMachine.__init__)


def test_sm_statemachine_constructor_args():
    sig = inspect.signature(sm_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_sm_transition_is_not_abstract():
    assert not inspect.isabstract(sm_Transition)


def test_sm_transition_constructor_exists():
    assert callable(sm_Transition.__init__)


def test_sm_transition_constructor_args():
    sig = inspect.signature(sm_Transition.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_sm_state_is_not_abstract():
    assert not inspect.isabstract(sm_State)


def test_sm_state_constructor_exists():
    assert callable(sm_State.__init__)


def test_sm_state_constructor_args():
    sig = inspect.signature(sm_State.__init__)
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
sm_Graph_strategy = st.builds(
    sm_Graph,
    name=
        safe_text
)
Mark_strategy = st.builds(
    Mark,
)
sm_Observation_strategy = st.builds(
    sm_Observation,
)
sm_Mark_strategy = st.builds(
    sm_Mark,
    time=
        safe_text
)
sm_Edge_strategy = st.builds(
    sm_Edge,
    name=
        safe_text
)
sm_Node_strategy = st.builds(
    sm_Node,
    name=
        safe_text
)
Graph_strategy = st.builds(
    Graph,
)
sm_StateMachine_strategy = st.builds(
    sm_StateMachine,
)
Edge_strategy = st.builds(
    Edge,
)
sm_Transition_strategy = st.builds(
    sm_Transition,
)
Node_strategy = st.builds(
    Node,
)
sm_State_strategy = st.builds(
    sm_State,
)

@given(instance=sm_Graph_strategy)
@settings(max_examples=50)
def test_sm_graph_instantiation(instance):
    assert isinstance(instance, sm_Graph)



@given(instance=sm_Graph_strategy)
def test_sm_graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Mark_strategy)
@settings(max_examples=50)
def test_mark_instantiation(instance):
    assert isinstance(instance, Mark)

@given(instance=sm_Observation_strategy)
@settings(max_examples=50)
def test_sm_observation_instantiation(instance):
    assert isinstance(instance, sm_Observation)

@given(instance=sm_Mark_strategy)
@settings(max_examples=50)
def test_sm_mark_instantiation(instance):
    assert isinstance(instance, sm_Mark)



@given(instance=sm_Mark_strategy)
def test_sm_mark_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=sm_Edge_strategy)
@settings(max_examples=50)
def test_sm_edge_instantiation(instance):
    assert isinstance(instance, sm_Edge)



@given(instance=sm_Edge_strategy)
def test_sm_edge_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sm_Node_strategy)
@settings(max_examples=50)
def test_sm_node_instantiation(instance):
    assert isinstance(instance, sm_Node)



@given(instance=sm_Node_strategy)
def test_sm_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Graph_strategy)
@settings(max_examples=50)
def test_graph_instantiation(instance):
    assert isinstance(instance, Graph)

@given(instance=sm_StateMachine_strategy)
@settings(max_examples=50)
def test_sm_statemachine_instantiation(instance):
    assert isinstance(instance, sm_StateMachine)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=sm_Transition_strategy)
@settings(max_examples=50)
def test_sm_transition_instantiation(instance):
    assert isinstance(instance, sm_Transition)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=sm_State_strategy)
@settings(max_examples=50)
def test_sm_state_instantiation(instance):
    assert isinstance(instance, sm_State)
