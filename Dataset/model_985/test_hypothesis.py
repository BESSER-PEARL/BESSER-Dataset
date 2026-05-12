import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    node,
    cfg_endnode,
    cfg_startnode,
    cfg_edge,
    cfg_node,
    cfg_cfg,
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



def test_cfg_endnode_is_not_abstract():
    assert not inspect.isabstract(cfg_endnode)


def test_cfg_endnode_constructor_exists():
    assert callable(cfg_endnode.__init__)


def test_cfg_endnode_constructor_args():
    sig = inspect.signature(cfg_endnode.__init__)
    params = list(sig.parameters.keys())



def test_cfg_startnode_is_not_abstract():
    assert not inspect.isabstract(cfg_startnode)


def test_cfg_startnode_constructor_exists():
    assert callable(cfg_startnode.__init__)


def test_cfg_startnode_constructor_args():
    sig = inspect.signature(cfg_startnode.__init__)
    params = list(sig.parameters.keys())



def test_cfg_edge_is_not_abstract():
    assert not inspect.isabstract(cfg_edge)


def test_cfg_edge_constructor_exists():
    assert callable(cfg_edge.__init__)


def test_cfg_edge_constructor_args():
    sig = inspect.signature(cfg_edge.__init__)
    params = list(sig.parameters.keys())



def test_cfg_node_is_not_abstract():
    assert not inspect.isabstract(cfg_node)


def test_cfg_node_constructor_exists():
    assert callable(cfg_node.__init__)


def test_cfg_node_constructor_args():
    sig = inspect.signature(cfg_node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cfg_node_has_name():
    assert hasattr(cfg_node, "name")
    descriptor = None
    for klass in cfg_node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cfg_cfg_is_not_abstract():
    assert not inspect.isabstract(cfg_cfg)


def test_cfg_cfg_constructor_exists():
    assert callable(cfg_cfg.__init__)


def test_cfg_cfg_constructor_args():
    sig = inspect.signature(cfg_cfg.__init__)
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
cfg_endnode_strategy = st.builds(
    cfg_endnode,
)
cfg_startnode_strategy = st.builds(
    cfg_startnode,
)
cfg_edge_strategy = st.builds(
    cfg_edge,
)
cfg_node_strategy = st.builds(
    cfg_node,
    name=
        safe_text
)
cfg_cfg_strategy = st.builds(
    cfg_cfg,
)

@given(instance=node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, node)

@given(instance=cfg_endnode_strategy)
@settings(max_examples=50)
def test_cfg_endnode_instantiation(instance):
    assert isinstance(instance, cfg_endnode)

@given(instance=cfg_startnode_strategy)
@settings(max_examples=50)
def test_cfg_startnode_instantiation(instance):
    assert isinstance(instance, cfg_startnode)

@given(instance=cfg_edge_strategy)
@settings(max_examples=50)
def test_cfg_edge_instantiation(instance):
    assert isinstance(instance, cfg_edge)

@given(instance=cfg_node_strategy)
@settings(max_examples=50)
def test_cfg_node_instantiation(instance):
    assert isinstance(instance, cfg_node)



@given(instance=cfg_node_strategy)
def test_cfg_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cfg_cfg_strategy)
@settings(max_examples=50)
def test_cfg_cfg_instantiation(instance):
    assert isinstance(instance, cfg_cfg)
