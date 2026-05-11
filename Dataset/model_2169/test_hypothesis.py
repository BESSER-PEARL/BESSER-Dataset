import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rpslPerceptionGraphMetaModel::InputPort,
    rpslPerceptionGraphMetaModel::Connection,
    rpslPerceptionGraphMetaModel::OutputPort,
    Element,
    rpslPerceptionGraphMetaModel::Node,
    rpslPerceptionGraphMetaModel::Leaf,
    rpslPerceptionGraphMetaModel::Component,
    rpslPerceptionGraphMetaModel::Prototype,
    rpslPerceptionGraphMetaModel::Element,
    rpslPerceptionGraphMetaModel::PerceptionGraph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rpslperceptiongraphmetamodel::inputport_is_not_abstract():
    assert not inspect.isabstract(rpslPerceptionGraphMetaModel::InputPort)


def test_rpslperceptiongraphmetamodel::inputport_constructor_exists():
    assert callable(rpslPerceptionGraphMetaModel::InputPort.__init__)


def test_rpslperceptiongraphmetamodel::inputport_constructor_args():
    sig = inspect.signature(rpslPerceptionGraphMetaModel::InputPort.__init__)
    params = list(sig.parameters.keys())



def test_rpslperceptiongraphmetamodel::connection_is_not_abstract():
    assert not inspect.isabstract(rpslPerceptionGraphMetaModel::Connection)


def test_rpslperceptiongraphmetamodel::connection_constructor_exists():
    assert callable(rpslPerceptionGraphMetaModel::Connection.__init__)


def test_rpslperceptiongraphmetamodel::connection_constructor_args():
    sig = inspect.signature(rpslPerceptionGraphMetaModel::Connection.__init__)
    params = list(sig.parameters.keys())



def test_rpslperceptiongraphmetamodel::outputport_is_not_abstract():
    assert not inspect.isabstract(rpslPerceptionGraphMetaModel::OutputPort)


def test_rpslperceptiongraphmetamodel::outputport_constructor_exists():
    assert callable(rpslPerceptionGraphMetaModel::OutputPort.__init__)


def test_rpslperceptiongraphmetamodel::outputport_constructor_args():
    sig = inspect.signature(rpslPerceptionGraphMetaModel::OutputPort.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_rpslperceptiongraphmetamodel::node_is_not_abstract():
    assert not inspect.isabstract(rpslPerceptionGraphMetaModel::Node)


def test_rpslperceptiongraphmetamodel::node_constructor_exists():
    assert callable(rpslPerceptionGraphMetaModel::Node.__init__)


def test_rpslperceptiongraphmetamodel::node_constructor_args():
    sig = inspect.signature(rpslPerceptionGraphMetaModel::Node.__init__)
    params = list(sig.parameters.keys())



def test_rpslperceptiongraphmetamodel::leaf_is_not_abstract():
    assert not inspect.isabstract(rpslPerceptionGraphMetaModel::Leaf)


def test_rpslperceptiongraphmetamodel::leaf_constructor_exists():
    assert callable(rpslPerceptionGraphMetaModel::Leaf.__init__)


def test_rpslperceptiongraphmetamodel::leaf_constructor_args():
    sig = inspect.signature(rpslPerceptionGraphMetaModel::Leaf.__init__)
    params = list(sig.parameters.keys())



def test_rpslperceptiongraphmetamodel::component_is_not_abstract():
    assert not inspect.isabstract(rpslPerceptionGraphMetaModel::Component)


def test_rpslperceptiongraphmetamodel::component_constructor_exists():
    assert callable(rpslPerceptionGraphMetaModel::Component.__init__)


def test_rpslperceptiongraphmetamodel::component_constructor_args():
    sig = inspect.signature(rpslPerceptionGraphMetaModel::Component.__init__)
    params = list(sig.parameters.keys())



def test_rpslperceptiongraphmetamodel::prototype_is_not_abstract():
    assert not inspect.isabstract(rpslPerceptionGraphMetaModel::Prototype)


def test_rpslperceptiongraphmetamodel::prototype_constructor_exists():
    assert callable(rpslPerceptionGraphMetaModel::Prototype.__init__)


def test_rpslperceptiongraphmetamodel::prototype_constructor_args():
    sig = inspect.signature(rpslPerceptionGraphMetaModel::Prototype.__init__)
    params = list(sig.parameters.keys())



def test_rpslperceptiongraphmetamodel::element_is_not_abstract():
    assert not inspect.isabstract(rpslPerceptionGraphMetaModel::Element)


def test_rpslperceptiongraphmetamodel::element_constructor_exists():
    assert callable(rpslPerceptionGraphMetaModel::Element.__init__)


def test_rpslperceptiongraphmetamodel::element_constructor_args():
    sig = inspect.signature(rpslPerceptionGraphMetaModel::Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "doc" in params, "Missing parameter 'doc'"

def test_rpslperceptiongraphmetamodel::element_has_name():
    assert hasattr(rpslPerceptionGraphMetaModel::Element, "name")
    descriptor = None
    for klass in rpslPerceptionGraphMetaModel::Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rpslperceptiongraphmetamodel::element_has_doc():
    assert hasattr(rpslPerceptionGraphMetaModel::Element, "doc")
    descriptor = None
    for klass in rpslPerceptionGraphMetaModel::Element.__mro__:
        if "doc" in klass.__dict__:
            descriptor = klass.__dict__["doc"]
            break
    assert isinstance(descriptor, property)



def test_rpslperceptiongraphmetamodel::perceptiongraph_is_not_abstract():
    assert not inspect.isabstract(rpslPerceptionGraphMetaModel::PerceptionGraph)


def test_rpslperceptiongraphmetamodel::perceptiongraph_constructor_exists():
    assert callable(rpslPerceptionGraphMetaModel::PerceptionGraph.__init__)


def test_rpslperceptiongraphmetamodel::perceptiongraph_constructor_args():
    sig = inspect.signature(rpslPerceptionGraphMetaModel::PerceptionGraph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "doc" in params, "Missing parameter 'doc'"
    assert "uuid" in params, "Missing parameter 'uuid'"

def test_rpslperceptiongraphmetamodel::perceptiongraph_has_name():
    assert hasattr(rpslPerceptionGraphMetaModel::PerceptionGraph, "name")
    descriptor = None
    for klass in rpslPerceptionGraphMetaModel::PerceptionGraph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rpslperceptiongraphmetamodel::perceptiongraph_has_doc():
    assert hasattr(rpslPerceptionGraphMetaModel::PerceptionGraph, "doc")
    descriptor = None
    for klass in rpslPerceptionGraphMetaModel::PerceptionGraph.__mro__:
        if "doc" in klass.__dict__:
            descriptor = klass.__dict__["doc"]
            break
    assert isinstance(descriptor, property)

def test_rpslperceptiongraphmetamodel::perceptiongraph_has_uuid():
    assert hasattr(rpslPerceptionGraphMetaModel::PerceptionGraph, "uuid")
    descriptor = None
    for klass in rpslPerceptionGraphMetaModel::PerceptionGraph.__mro__:
        if "uuid" in klass.__dict__:
            descriptor = klass.__dict__["uuid"]
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
rpslPerceptionGraphMetaModel::InputPort_strategy = st.builds(
    rpslPerceptionGraphMetaModel::InputPort,
)
rpslPerceptionGraphMetaModel::Connection_strategy = st.builds(
    rpslPerceptionGraphMetaModel::Connection,
)
rpslPerceptionGraphMetaModel::OutputPort_strategy = st.builds(
    rpslPerceptionGraphMetaModel::OutputPort,
)
Element_strategy = st.builds(
    Element,
)
rpslPerceptionGraphMetaModel::Node_strategy = st.builds(
    rpslPerceptionGraphMetaModel::Node,
)
rpslPerceptionGraphMetaModel::Leaf_strategy = st.builds(
    rpslPerceptionGraphMetaModel::Leaf,
)
rpslPerceptionGraphMetaModel::Component_strategy = st.builds(
    rpslPerceptionGraphMetaModel::Component,
)
rpslPerceptionGraphMetaModel::Prototype_strategy = st.builds(
    rpslPerceptionGraphMetaModel::Prototype,
)
rpslPerceptionGraphMetaModel::Element_strategy = st.builds(
    rpslPerceptionGraphMetaModel::Element,
    name=
        safe_text,
    doc=
        safe_text
)
rpslPerceptionGraphMetaModel::PerceptionGraph_strategy = st.builds(
    rpslPerceptionGraphMetaModel::PerceptionGraph,
    name=
        safe_text,
    doc=
        safe_text,
    uuid=
        safe_text
)

@given(instance=rpslPerceptionGraphMetaModel::InputPort_strategy)
@settings(max_examples=50)
def test_rpslperceptiongraphmetamodel::inputport_instantiation(instance):
    assert isinstance(instance, rpslPerceptionGraphMetaModel::InputPort)

@given(instance=rpslPerceptionGraphMetaModel::Connection_strategy)
@settings(max_examples=50)
def test_rpslperceptiongraphmetamodel::connection_instantiation(instance):
    assert isinstance(instance, rpslPerceptionGraphMetaModel::Connection)

@given(instance=rpslPerceptionGraphMetaModel::OutputPort_strategy)
@settings(max_examples=50)
def test_rpslperceptiongraphmetamodel::outputport_instantiation(instance):
    assert isinstance(instance, rpslPerceptionGraphMetaModel::OutputPort)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=rpslPerceptionGraphMetaModel::Node_strategy)
@settings(max_examples=50)
def test_rpslperceptiongraphmetamodel::node_instantiation(instance):
    assert isinstance(instance, rpslPerceptionGraphMetaModel::Node)

@given(instance=rpslPerceptionGraphMetaModel::Leaf_strategy)
@settings(max_examples=50)
def test_rpslperceptiongraphmetamodel::leaf_instantiation(instance):
    assert isinstance(instance, rpslPerceptionGraphMetaModel::Leaf)

@given(instance=rpslPerceptionGraphMetaModel::Component_strategy)
@settings(max_examples=50)
def test_rpslperceptiongraphmetamodel::component_instantiation(instance):
    assert isinstance(instance, rpslPerceptionGraphMetaModel::Component)

@given(instance=rpslPerceptionGraphMetaModel::Prototype_strategy)
@settings(max_examples=50)
def test_rpslperceptiongraphmetamodel::prototype_instantiation(instance):
    assert isinstance(instance, rpslPerceptionGraphMetaModel::Prototype)

@given(instance=rpslPerceptionGraphMetaModel::Element_strategy)
@settings(max_examples=50)
def test_rpslperceptiongraphmetamodel::element_instantiation(instance):
    assert isinstance(instance, rpslPerceptionGraphMetaModel::Element)

@given(instance=rpslPerceptionGraphMetaModel::Element_strategy)
def test_rpslperceptiongraphmetamodel::element_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rpslPerceptionGraphMetaModel::Element_strategy)
def test_rpslperceptiongraphmetamodel::element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rpslPerceptionGraphMetaModel::Element_strategy)
def test_rpslperceptiongraphmetamodel::element_doc_type(instance):
    assert isinstance(instance.doc, str)


@given(instance=rpslPerceptionGraphMetaModel::Element_strategy)
def test_rpslperceptiongraphmetamodel::element_doc_setter(instance):
    original = instance.doc
    instance.doc = original
    assert instance.doc == original

@given(instance=rpslPerceptionGraphMetaModel::PerceptionGraph_strategy)
@settings(max_examples=50)
def test_rpslperceptiongraphmetamodel::perceptiongraph_instantiation(instance):
    assert isinstance(instance, rpslPerceptionGraphMetaModel::PerceptionGraph)

@given(instance=rpslPerceptionGraphMetaModel::PerceptionGraph_strategy)
def test_rpslperceptiongraphmetamodel::perceptiongraph_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rpslPerceptionGraphMetaModel::PerceptionGraph_strategy)
def test_rpslperceptiongraphmetamodel::perceptiongraph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rpslPerceptionGraphMetaModel::PerceptionGraph_strategy)
def test_rpslperceptiongraphmetamodel::perceptiongraph_doc_type(instance):
    assert isinstance(instance.doc, str)


@given(instance=rpslPerceptionGraphMetaModel::PerceptionGraph_strategy)
def test_rpslperceptiongraphmetamodel::perceptiongraph_doc_setter(instance):
    original = instance.doc
    instance.doc = original
    assert instance.doc == original

@given(instance=rpslPerceptionGraphMetaModel::PerceptionGraph_strategy)
def test_rpslperceptiongraphmetamodel::perceptiongraph_uuid_type(instance):
    assert isinstance(instance.uuid, str)


@given(instance=rpslPerceptionGraphMetaModel::PerceptionGraph_strategy)
def test_rpslperceptiongraphmetamodel::perceptiongraph_uuid_setter(instance):
    original = instance.uuid
    instance.uuid = original
    assert instance.uuid == original
