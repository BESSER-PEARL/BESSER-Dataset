import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rpslPerceptionGraphMetaModel_InputPort,
    rpslPerceptionGraphMetaModel_Connection,
    rpslPerceptionGraphMetaModel_OutputPort,
    Element,
    rpslPerceptionGraphMetaModel_Node,
    rpslPerceptionGraphMetaModel_Leaf,
    rpslPerceptionGraphMetaModel_Component,
    rpslPerceptionGraphMetaModel_Prototype,
    rpslPerceptionGraphMetaModel_Element,
    rpslPerceptionGraphMetaModel_PerceptionGraph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rpslperceptiongraphmetamodel_inputport_is_not_abstract():
    assert not inspect.isabstract(rpslPerceptionGraphMetaModel_InputPort)


def test_rpslperceptiongraphmetamodel_inputport_constructor_exists():
    assert callable(rpslPerceptionGraphMetaModel_InputPort.__init__)


def test_rpslperceptiongraphmetamodel_inputport_constructor_args():
    sig = inspect.signature(rpslPerceptionGraphMetaModel_InputPort.__init__)
    params = list(sig.parameters.keys())



def test_rpslperceptiongraphmetamodel_connection_is_not_abstract():
    assert not inspect.isabstract(rpslPerceptionGraphMetaModel_Connection)


def test_rpslperceptiongraphmetamodel_connection_constructor_exists():
    assert callable(rpslPerceptionGraphMetaModel_Connection.__init__)


def test_rpslperceptiongraphmetamodel_connection_constructor_args():
    sig = inspect.signature(rpslPerceptionGraphMetaModel_Connection.__init__)
    params = list(sig.parameters.keys())



def test_rpslperceptiongraphmetamodel_outputport_is_not_abstract():
    assert not inspect.isabstract(rpslPerceptionGraphMetaModel_OutputPort)


def test_rpslperceptiongraphmetamodel_outputport_constructor_exists():
    assert callable(rpslPerceptionGraphMetaModel_OutputPort.__init__)


def test_rpslperceptiongraphmetamodel_outputport_constructor_args():
    sig = inspect.signature(rpslPerceptionGraphMetaModel_OutputPort.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_rpslperceptiongraphmetamodel_node_is_not_abstract():
    assert not inspect.isabstract(rpslPerceptionGraphMetaModel_Node)


def test_rpslperceptiongraphmetamodel_node_constructor_exists():
    assert callable(rpslPerceptionGraphMetaModel_Node.__init__)


def test_rpslperceptiongraphmetamodel_node_constructor_args():
    sig = inspect.signature(rpslPerceptionGraphMetaModel_Node.__init__)
    params = list(sig.parameters.keys())



def test_rpslperceptiongraphmetamodel_leaf_is_not_abstract():
    assert not inspect.isabstract(rpslPerceptionGraphMetaModel_Leaf)


def test_rpslperceptiongraphmetamodel_leaf_constructor_exists():
    assert callable(rpslPerceptionGraphMetaModel_Leaf.__init__)


def test_rpslperceptiongraphmetamodel_leaf_constructor_args():
    sig = inspect.signature(rpslPerceptionGraphMetaModel_Leaf.__init__)
    params = list(sig.parameters.keys())



def test_rpslperceptiongraphmetamodel_component_is_not_abstract():
    assert not inspect.isabstract(rpslPerceptionGraphMetaModel_Component)


def test_rpslperceptiongraphmetamodel_component_constructor_exists():
    assert callable(rpslPerceptionGraphMetaModel_Component.__init__)


def test_rpslperceptiongraphmetamodel_component_constructor_args():
    sig = inspect.signature(rpslPerceptionGraphMetaModel_Component.__init__)
    params = list(sig.parameters.keys())



def test_rpslperceptiongraphmetamodel_prototype_is_not_abstract():
    assert not inspect.isabstract(rpslPerceptionGraphMetaModel_Prototype)


def test_rpslperceptiongraphmetamodel_prototype_constructor_exists():
    assert callable(rpslPerceptionGraphMetaModel_Prototype.__init__)


def test_rpslperceptiongraphmetamodel_prototype_constructor_args():
    sig = inspect.signature(rpslPerceptionGraphMetaModel_Prototype.__init__)
    params = list(sig.parameters.keys())



def test_rpslperceptiongraphmetamodel_element_is_not_abstract():
    assert not inspect.isabstract(rpslPerceptionGraphMetaModel_Element)


def test_rpslperceptiongraphmetamodel_element_constructor_exists():
    assert callable(rpslPerceptionGraphMetaModel_Element.__init__)


def test_rpslperceptiongraphmetamodel_element_constructor_args():
    sig = inspect.signature(rpslPerceptionGraphMetaModel_Element.__init__)
    params = list(sig.parameters.keys())
    assert "doc" in params, "Missing parameter 'doc'"
    assert "name" in params, "Missing parameter 'name'"

def test_rpslperceptiongraphmetamodel_element_has_doc():
    assert hasattr(rpslPerceptionGraphMetaModel_Element, "doc")
    descriptor = None
    for klass in rpslPerceptionGraphMetaModel_Element.__mro__:
        if "doc" in klass.__dict__:
            descriptor = klass.__dict__["doc"]
            break
    assert isinstance(descriptor, property)

def test_rpslperceptiongraphmetamodel_element_has_name():
    assert hasattr(rpslPerceptionGraphMetaModel_Element, "name")
    descriptor = None
    for klass in rpslPerceptionGraphMetaModel_Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rpslperceptiongraphmetamodel_perceptiongraph_is_not_abstract():
    assert not inspect.isabstract(rpslPerceptionGraphMetaModel_PerceptionGraph)


def test_rpslperceptiongraphmetamodel_perceptiongraph_constructor_exists():
    assert callable(rpslPerceptionGraphMetaModel_PerceptionGraph.__init__)


def test_rpslperceptiongraphmetamodel_perceptiongraph_constructor_args():
    sig = inspect.signature(rpslPerceptionGraphMetaModel_PerceptionGraph.__init__)
    params = list(sig.parameters.keys())
    assert "doc" in params, "Missing parameter 'doc'"
    assert "uuid" in params, "Missing parameter 'uuid'"
    assert "name" in params, "Missing parameter 'name'"

def test_rpslperceptiongraphmetamodel_perceptiongraph_has_doc():
    assert hasattr(rpslPerceptionGraphMetaModel_PerceptionGraph, "doc")
    descriptor = None
    for klass in rpslPerceptionGraphMetaModel_PerceptionGraph.__mro__:
        if "doc" in klass.__dict__:
            descriptor = klass.__dict__["doc"]
            break
    assert isinstance(descriptor, property)

def test_rpslperceptiongraphmetamodel_perceptiongraph_has_uuid():
    assert hasattr(rpslPerceptionGraphMetaModel_PerceptionGraph, "uuid")
    descriptor = None
    for klass in rpslPerceptionGraphMetaModel_PerceptionGraph.__mro__:
        if "uuid" in klass.__dict__:
            descriptor = klass.__dict__["uuid"]
            break
    assert isinstance(descriptor, property)

def test_rpslperceptiongraphmetamodel_perceptiongraph_has_name():
    assert hasattr(rpslPerceptionGraphMetaModel_PerceptionGraph, "name")
    descriptor = None
    for klass in rpslPerceptionGraphMetaModel_PerceptionGraph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
rpslPerceptionGraphMetaModel_InputPort_strategy = st.builds(
    rpslPerceptionGraphMetaModel_InputPort,
)
rpslPerceptionGraphMetaModel_Connection_strategy = st.builds(
    rpslPerceptionGraphMetaModel_Connection,
)
rpslPerceptionGraphMetaModel_OutputPort_strategy = st.builds(
    rpslPerceptionGraphMetaModel_OutputPort,
)
Element_strategy = st.builds(
    Element,
)
rpslPerceptionGraphMetaModel_Node_strategy = st.builds(
    rpslPerceptionGraphMetaModel_Node,
)
rpslPerceptionGraphMetaModel_Leaf_strategy = st.builds(
    rpslPerceptionGraphMetaModel_Leaf,
)
rpslPerceptionGraphMetaModel_Component_strategy = st.builds(
    rpslPerceptionGraphMetaModel_Component,
)
rpslPerceptionGraphMetaModel_Prototype_strategy = st.builds(
    rpslPerceptionGraphMetaModel_Prototype,
)
rpslPerceptionGraphMetaModel_Element_strategy = st.builds(
    rpslPerceptionGraphMetaModel_Element,
    doc=
        safe_text,
    name=
        safe_text
)
rpslPerceptionGraphMetaModel_PerceptionGraph_strategy = st.builds(
    rpslPerceptionGraphMetaModel_PerceptionGraph,
    doc=
        safe_text,
    uuid=
        safe_text,
    name=
        safe_text
)

@given(instance=rpslPerceptionGraphMetaModel_InputPort_strategy)
@settings(max_examples=50)
def test_rpslperceptiongraphmetamodel_inputport_instantiation(instance):
    assert isinstance(instance, rpslPerceptionGraphMetaModel_InputPort)

@given(instance=rpslPerceptionGraphMetaModel_Connection_strategy)
@settings(max_examples=50)
def test_rpslperceptiongraphmetamodel_connection_instantiation(instance):
    assert isinstance(instance, rpslPerceptionGraphMetaModel_Connection)

@given(instance=rpslPerceptionGraphMetaModel_OutputPort_strategy)
@settings(max_examples=50)
def test_rpslperceptiongraphmetamodel_outputport_instantiation(instance):
    assert isinstance(instance, rpslPerceptionGraphMetaModel_OutputPort)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=rpslPerceptionGraphMetaModel_Node_strategy)
@settings(max_examples=50)
def test_rpslperceptiongraphmetamodel_node_instantiation(instance):
    assert isinstance(instance, rpslPerceptionGraphMetaModel_Node)

@given(instance=rpslPerceptionGraphMetaModel_Leaf_strategy)
@settings(max_examples=50)
def test_rpslperceptiongraphmetamodel_leaf_instantiation(instance):
    assert isinstance(instance, rpslPerceptionGraphMetaModel_Leaf)

@given(instance=rpslPerceptionGraphMetaModel_Component_strategy)
@settings(max_examples=50)
def test_rpslperceptiongraphmetamodel_component_instantiation(instance):
    assert isinstance(instance, rpslPerceptionGraphMetaModel_Component)

@given(instance=rpslPerceptionGraphMetaModel_Prototype_strategy)
@settings(max_examples=50)
def test_rpslperceptiongraphmetamodel_prototype_instantiation(instance):
    assert isinstance(instance, rpslPerceptionGraphMetaModel_Prototype)

@given(instance=rpslPerceptionGraphMetaModel_Element_strategy)
@settings(max_examples=50)
def test_rpslperceptiongraphmetamodel_element_instantiation(instance):
    assert isinstance(instance, rpslPerceptionGraphMetaModel_Element)



@given(instance=rpslPerceptionGraphMetaModel_Element_strategy)
def test_rpslperceptiongraphmetamodel_element_doc_setter(instance):
    original = instance.doc
    instance.doc = original
    assert instance.doc == original



@given(instance=rpslPerceptionGraphMetaModel_Element_strategy)
def test_rpslperceptiongraphmetamodel_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rpslPerceptionGraphMetaModel_PerceptionGraph_strategy)
@settings(max_examples=50)
def test_rpslperceptiongraphmetamodel_perceptiongraph_instantiation(instance):
    assert isinstance(instance, rpslPerceptionGraphMetaModel_PerceptionGraph)



@given(instance=rpslPerceptionGraphMetaModel_PerceptionGraph_strategy)
def test_rpslperceptiongraphmetamodel_perceptiongraph_doc_setter(instance):
    original = instance.doc
    instance.doc = original
    assert instance.doc == original



@given(instance=rpslPerceptionGraphMetaModel_PerceptionGraph_strategy)
def test_rpslperceptiongraphmetamodel_perceptiongraph_uuid_setter(instance):
    original = instance.uuid
    instance.uuid = original
    assert instance.uuid == original



@given(instance=rpslPerceptionGraphMetaModel_PerceptionGraph_strategy)
def test_rpslperceptiongraphmetamodel_perceptiongraph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
