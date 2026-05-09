import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    node,
    cfg::endnode,
    cfg::startnode,
    cfg::edge,
    cfg::node,
    cfg::cfg,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_node_is_not_abstract():
    assert not inspect.isabstract(node)


def test_node_constructor_exists():
    assert callable(node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(node.__init__)
    params = list(sig.parameters.keys())



def test_cfg::endnode_is_not_abstract():
    assert not inspect.isabstract(cfg::endnode)


def test_cfg::endnode_constructor_exists():
    assert callable(cfg::endnode.__init__)


def test_cfg::endnode_constructor_args():
    sig = inspect.signature(cfg::endnode.__init__)
    params = list(sig.parameters.keys())



def test_cfg::startnode_is_not_abstract():
    assert not inspect.isabstract(cfg::startnode)


def test_cfg::startnode_constructor_exists():
    assert callable(cfg::startnode.__init__)


def test_cfg::startnode_constructor_args():
    sig = inspect.signature(cfg::startnode.__init__)
    params = list(sig.parameters.keys())



def test_cfg::edge_is_not_abstract():
    assert not inspect.isabstract(cfg::edge)


def test_cfg::edge_constructor_exists():
    assert callable(cfg::edge.__init__)


def test_cfg::edge_constructor_args():
    sig = inspect.signature(cfg::edge.__init__)
    params = list(sig.parameters.keys())



def test_cfg::node_is_not_abstract():
    assert not inspect.isabstract(cfg::node)


def test_cfg::node_constructor_exists():
    assert callable(cfg::node.__init__)


def test_cfg::node_constructor_args():
    sig = inspect.signature(cfg::node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cfg::node_has_name():
    assert hasattr(cfg::node, "name")
    descriptor = None
    for klass in cfg::node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cfg::cfg_is_not_abstract():
    assert not inspect.isabstract(cfg::cfg)


def test_cfg::cfg_constructor_exists():
    assert callable(cfg::cfg.__init__)


def test_cfg::cfg_constructor_args():
    sig = inspect.signature(cfg::cfg.__init__)
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
node_strategy = st.builds(
    node,
)
cfg::endnode_strategy = st.builds(
    cfg::endnode,
)
cfg::startnode_strategy = st.builds(
    cfg::startnode,
)
cfg::edge_strategy = st.builds(
    cfg::edge,
)
cfg::node_strategy = st.builds(
    cfg::node,
    name=
        safe_text
)
cfg::cfg_strategy = st.builds(
    cfg::cfg,
)

@given(instance=node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, node)

@given(instance=cfg::endnode_strategy)
@settings(max_examples=50)
def test_cfg::endnode_instantiation(instance):
    assert isinstance(instance, cfg::endnode)

@given(instance=cfg::startnode_strategy)
@settings(max_examples=50)
def test_cfg::startnode_instantiation(instance):
    assert isinstance(instance, cfg::startnode)

@given(instance=cfg::edge_strategy)
@settings(max_examples=50)
def test_cfg::edge_instantiation(instance):
    assert isinstance(instance, cfg::edge)

@given(instance=cfg::node_strategy)
@settings(max_examples=50)
def test_cfg::node_instantiation(instance):
    assert isinstance(instance, cfg::node)

@given(instance=cfg::node_strategy)
def test_cfg::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cfg::node_strategy)
def test_cfg::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cfg::cfg_strategy)
@settings(max_examples=50)
def test_cfg::cfg_instantiation(instance):
    assert isinstance(instance, cfg::cfg)
