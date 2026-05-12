import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mention_graph_Edge,
    mention_graph_Node,
    mention_graph_MentionGraph,
    Node,
    mention_graph_HashTag,
    mention_graph_User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mention_graph_edge_is_not_abstract():
    assert not inspect.isabstract(mention_graph_Edge)


def test_mention_graph_edge_constructor_exists():
    assert callable(mention_graph_Edge.__init__)


def test_mention_graph_edge_constructor_args():
    sig = inspect.signature(mention_graph_Edge.__init__)
    params = list(sig.parameters.keys())



def test_mention_graph_node_is_not_abstract():
    assert not inspect.isabstract(mention_graph_Node)


def test_mention_graph_node_constructor_exists():
    assert callable(mention_graph_Node.__init__)


def test_mention_graph_node_constructor_args():
    sig = inspect.signature(mention_graph_Node.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mention_graph_node_has_value():
    assert hasattr(mention_graph_Node, "value")
    descriptor = None
    for klass in mention_graph_Node.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mention_graph_mentiongraph_is_not_abstract():
    assert not inspect.isabstract(mention_graph_MentionGraph)


def test_mention_graph_mentiongraph_constructor_exists():
    assert callable(mention_graph_MentionGraph.__init__)


def test_mention_graph_mentiongraph_constructor_args():
    sig = inspect.signature(mention_graph_MentionGraph.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_mention_graph_hashtag_is_not_abstract():
    assert not inspect.isabstract(mention_graph_HashTag)


def test_mention_graph_hashtag_constructor_exists():
    assert callable(mention_graph_HashTag.__init__)


def test_mention_graph_hashtag_constructor_args():
    sig = inspect.signature(mention_graph_HashTag.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_mention_graph_hashtag_has_count():
    assert hasattr(mention_graph_HashTag, "count")
    descriptor = None
    for klass in mention_graph_HashTag.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_mention_graph_user_is_not_abstract():
    assert not inspect.isabstract(mention_graph_User)


def test_mention_graph_user_constructor_exists():
    assert callable(mention_graph_User.__init__)


def test_mention_graph_user_constructor_args():
    sig = inspect.signature(mention_graph_User.__init__)
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
mention_graph_Edge_strategy = st.builds(
    mention_graph_Edge,
)
mention_graph_Node_strategy = st.builds(
    mention_graph_Node,
    value=
        safe_text
)
mention_graph_MentionGraph_strategy = st.builds(
    mention_graph_MentionGraph,
)
Node_strategy = st.builds(
    Node,
)
mention_graph_HashTag_strategy = st.builds(
    mention_graph_HashTag,
    count=
        st.integers()
)
mention_graph_User_strategy = st.builds(
    mention_graph_User,
)

@given(instance=mention_graph_Edge_strategy)
@settings(max_examples=50)
def test_mention_graph_edge_instantiation(instance):
    assert isinstance(instance, mention_graph_Edge)

@given(instance=mention_graph_Node_strategy)
@settings(max_examples=50)
def test_mention_graph_node_instantiation(instance):
    assert isinstance(instance, mention_graph_Node)



@given(instance=mention_graph_Node_strategy)
def test_mention_graph_node_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mention_graph_MentionGraph_strategy)
@settings(max_examples=50)
def test_mention_graph_mentiongraph_instantiation(instance):
    assert isinstance(instance, mention_graph_MentionGraph)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=mention_graph_HashTag_strategy)
@settings(max_examples=50)
def test_mention_graph_hashtag_instantiation(instance):
    assert isinstance(instance, mention_graph_HashTag)



@given(instance=mention_graph_HashTag_strategy)
def test_mention_graph_hashtag_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=mention_graph_User_strategy)
@settings(max_examples=50)
def test_mention_graph_user_instantiation(instance):
    assert isinstance(instance, mention_graph_User)
