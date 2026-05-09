import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mention::graph::Edge,
    mention::graph::Node,
    mention::graph::MentionGraph,
    Node,
    mention::graph::HashTag,
    mention::graph::User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mention::graph::edge_is_not_abstract():
    assert not inspect.isabstract(mention::graph::Edge)


def test_mention::graph::edge_constructor_exists():
    assert callable(mention::graph::Edge.__init__)


def test_mention::graph::edge_constructor_args():
    sig = inspect.signature(mention::graph::Edge.__init__)
    params = list(sig.parameters.keys())



def test_mention::graph::node_is_not_abstract():
    assert not inspect.isabstract(mention::graph::Node)


def test_mention::graph::node_constructor_exists():
    assert callable(mention::graph::Node.__init__)


def test_mention::graph::node_constructor_args():
    sig = inspect.signature(mention::graph::Node.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mention::graph::node_has_value():
    assert hasattr(mention::graph::Node, "value")
    descriptor = None
    for klass in mention::graph::Node.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mention::graph::mentiongraph_is_not_abstract():
    assert not inspect.isabstract(mention::graph::MentionGraph)


def test_mention::graph::mentiongraph_constructor_exists():
    assert callable(mention::graph::MentionGraph.__init__)


def test_mention::graph::mentiongraph_constructor_args():
    sig = inspect.signature(mention::graph::MentionGraph.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_mention::graph::hashtag_is_not_abstract():
    assert not inspect.isabstract(mention::graph::HashTag)


def test_mention::graph::hashtag_constructor_exists():
    assert callable(mention::graph::HashTag.__init__)


def test_mention::graph::hashtag_constructor_args():
    sig = inspect.signature(mention::graph::HashTag.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_mention::graph::hashtag_has_count():
    assert hasattr(mention::graph::HashTag, "count")
    descriptor = None
    for klass in mention::graph::HashTag.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_mention::graph::user_is_not_abstract():
    assert not inspect.isabstract(mention::graph::User)


def test_mention::graph::user_constructor_exists():
    assert callable(mention::graph::User.__init__)


def test_mention::graph::user_constructor_args():
    sig = inspect.signature(mention::graph::User.__init__)
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
mention::graph::Edge_strategy = st.builds(
    mention::graph::Edge,
)
mention::graph::Node_strategy = st.builds(
    mention::graph::Node,
    value=
        safe_text
)
mention::graph::MentionGraph_strategy = st.builds(
    mention::graph::MentionGraph,
)
Node_strategy = st.builds(
    Node,
)
mention::graph::HashTag_strategy = st.builds(
    mention::graph::HashTag,
    count=
        st.integers()
)
mention::graph::User_strategy = st.builds(
    mention::graph::User,
)

@given(instance=mention::graph::Edge_strategy)
@settings(max_examples=50)
def test_mention::graph::edge_instantiation(instance):
    assert isinstance(instance, mention::graph::Edge)

@given(instance=mention::graph::Node_strategy)
@settings(max_examples=50)
def test_mention::graph::node_instantiation(instance):
    assert isinstance(instance, mention::graph::Node)

@given(instance=mention::graph::Node_strategy)
def test_mention::graph::node_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=mention::graph::Node_strategy)
def test_mention::graph::node_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mention::graph::MentionGraph_strategy)
@settings(max_examples=50)
def test_mention::graph::mentiongraph_instantiation(instance):
    assert isinstance(instance, mention::graph::MentionGraph)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=mention::graph::HashTag_strategy)
@settings(max_examples=50)
def test_mention::graph::hashtag_instantiation(instance):
    assert isinstance(instance, mention::graph::HashTag)

@given(instance=mention::graph::HashTag_strategy)
def test_mention::graph::hashtag_count_type(instance):
    assert isinstance(instance.count, int)


@given(instance=mention::graph::HashTag_strategy)
def test_mention::graph::hashtag_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=mention::graph::User_strategy)
@settings(max_examples=50)
def test_mention::graph::user_instantiation(instance):
    assert isinstance(instance, mention::graph::User)
