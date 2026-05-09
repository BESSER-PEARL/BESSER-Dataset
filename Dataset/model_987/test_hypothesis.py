import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    qVTcDataDependencyGraph::Graph,
    qVTcDataDependencyGraph::Element,
    Element,
    qVTcDataDependencyGraph::Node,
    qVTcDataDependencyGraph::Edge,
    Edge,
    qVTcDataDependencyGraph::ContainmentEdge,
    qVTcDataDependencyGraph::ReferenceEdge,
    qVTcDataDependencyGraph::DependencyEdge,
    qVTcDataDependencyGraph::EObject,
    Node,
    qVTcDataDependencyGraph::DataTypeNode,
    qVTcDataDependencyGraph::MappingNode,
    qVTcDataDependencyGraph::ClassNode,
    Model,
    DependencyDirection,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_qvtcdatadependencygraph::graph_is_not_abstract():
    assert not inspect.isabstract(qVTcDataDependencyGraph::Graph)


def test_qvtcdatadependencygraph::graph_constructor_exists():
    assert callable(qVTcDataDependencyGraph::Graph.__init__)


def test_qvtcdatadependencygraph::graph_constructor_args():
    sig = inspect.signature(qVTcDataDependencyGraph::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qvtcdatadependencygraph::graph_has_name():
    assert hasattr(qVTcDataDependencyGraph::Graph, "name")
    descriptor = None
    for klass in qVTcDataDependencyGraph::Graph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qvtcdatadependencygraph::element_is_not_abstract():
    assert not inspect.isabstract(qVTcDataDependencyGraph::Element)


def test_qvtcdatadependencygraph::element_constructor_exists():
    assert callable(qVTcDataDependencyGraph::Element.__init__)


def test_qvtcdatadependencygraph::element_constructor_args():
    sig = inspect.signature(qVTcDataDependencyGraph::Element.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_qvtcdatadependencygraph::node_is_not_abstract():
    assert not inspect.isabstract(qVTcDataDependencyGraph::Node)


def test_qvtcdatadependencygraph::node_constructor_exists():
    assert callable(qVTcDataDependencyGraph::Node.__init__)


def test_qvtcdatadependencygraph::node_constructor_args():
    sig = inspect.signature(qVTcDataDependencyGraph::Node.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_qvtcdatadependencygraph::node_has_label():
    assert hasattr(qVTcDataDependencyGraph::Node, "label")
    descriptor = None
    for klass in qVTcDataDependencyGraph::Node.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_qvtcdatadependencygraph::edge_is_not_abstract():
    assert not inspect.isabstract(qVTcDataDependencyGraph::Edge)


def test_qvtcdatadependencygraph::edge_constructor_exists():
    assert callable(qVTcDataDependencyGraph::Edge.__init__)


def test_qvtcdatadependencygraph::edge_constructor_args():
    sig = inspect.signature(qVTcDataDependencyGraph::Edge.__init__)
    params = list(sig.parameters.keys())



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_qvtcdatadependencygraph::containmentedge_is_not_abstract():
    assert not inspect.isabstract(qVTcDataDependencyGraph::ContainmentEdge)


def test_qvtcdatadependencygraph::containmentedge_constructor_exists():
    assert callable(qVTcDataDependencyGraph::ContainmentEdge.__init__)


def test_qvtcdatadependencygraph::containmentedge_constructor_args():
    sig = inspect.signature(qVTcDataDependencyGraph::ContainmentEdge.__init__)
    params = list(sig.parameters.keys())
    assert "model" in params, "Missing parameter 'model'"

def test_qvtcdatadependencygraph::containmentedge_has_model():
    assert hasattr(qVTcDataDependencyGraph::ContainmentEdge, "model")
    descriptor = None
    for klass in qVTcDataDependencyGraph::ContainmentEdge.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)



def test_qvtcdatadependencygraph::referenceedge_is_not_abstract():
    assert not inspect.isabstract(qVTcDataDependencyGraph::ReferenceEdge)


def test_qvtcdatadependencygraph::referenceedge_constructor_exists():
    assert callable(qVTcDataDependencyGraph::ReferenceEdge.__init__)


def test_qvtcdatadependencygraph::referenceedge_constructor_args():
    sig = inspect.signature(qVTcDataDependencyGraph::ReferenceEdge.__init__)
    params = list(sig.parameters.keys())



def test_qvtcdatadependencygraph::dependencyedge_is_not_abstract():
    assert not inspect.isabstract(qVTcDataDependencyGraph::DependencyEdge)


def test_qvtcdatadependencygraph::dependencyedge_constructor_exists():
    assert callable(qVTcDataDependencyGraph::DependencyEdge.__init__)


def test_qvtcdatadependencygraph::dependencyedge_constructor_args():
    sig = inspect.signature(qVTcDataDependencyGraph::DependencyEdge.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "multiple" in params, "Missing parameter 'multiple'"
    assert "derived" in params, "Missing parameter 'derived'"

def test_qvtcdatadependencygraph::dependencyedge_has_direction():
    assert hasattr(qVTcDataDependencyGraph::DependencyEdge, "direction")
    descriptor = None
    for klass in qVTcDataDependencyGraph::DependencyEdge.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_qvtcdatadependencygraph::dependencyedge_has_multiple():
    assert hasattr(qVTcDataDependencyGraph::DependencyEdge, "multiple")
    descriptor = None
    for klass in qVTcDataDependencyGraph::DependencyEdge.__mro__:
        if "multiple" in klass.__dict__:
            descriptor = klass.__dict__["multiple"]
            break
    assert isinstance(descriptor, property)

def test_qvtcdatadependencygraph::dependencyedge_has_derived():
    assert hasattr(qVTcDataDependencyGraph::DependencyEdge, "derived")
    descriptor = None
    for klass in qVTcDataDependencyGraph::DependencyEdge.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)



def test_qvtcdatadependencygraph::eobject_is_not_abstract():
    assert not inspect.isabstract(qVTcDataDependencyGraph::EObject)


def test_qvtcdatadependencygraph::eobject_constructor_exists():
    assert callable(qVTcDataDependencyGraph::EObject.__init__)


def test_qvtcdatadependencygraph::eobject_constructor_args():
    sig = inspect.signature(qVTcDataDependencyGraph::EObject.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_qvtcdatadependencygraph::datatypenode_is_not_abstract():
    assert not inspect.isabstract(qVTcDataDependencyGraph::DataTypeNode)


def test_qvtcdatadependencygraph::datatypenode_constructor_exists():
    assert callable(qVTcDataDependencyGraph::DataTypeNode.__init__)


def test_qvtcdatadependencygraph::datatypenode_constructor_args():
    sig = inspect.signature(qVTcDataDependencyGraph::DataTypeNode.__init__)
    params = list(sig.parameters.keys())



def test_qvtcdatadependencygraph::mappingnode_is_not_abstract():
    assert not inspect.isabstract(qVTcDataDependencyGraph::MappingNode)


def test_qvtcdatadependencygraph::mappingnode_constructor_exists():
    assert callable(qVTcDataDependencyGraph::MappingNode.__init__)


def test_qvtcdatadependencygraph::mappingnode_constructor_args():
    sig = inspect.signature(qVTcDataDependencyGraph::MappingNode.__init__)
    params = list(sig.parameters.keys())



def test_qvtcdatadependencygraph::classnode_is_not_abstract():
    assert not inspect.isabstract(qVTcDataDependencyGraph::ClassNode)


def test_qvtcdatadependencygraph::classnode_constructor_exists():
    assert callable(qVTcDataDependencyGraph::ClassNode.__init__)


def test_qvtcdatadependencygraph::classnode_constructor_args():
    sig = inspect.signature(qVTcDataDependencyGraph::ClassNode.__init__)
    params = list(sig.parameters.keys())
    assert "model" in params, "Missing parameter 'model'"
    assert "superTypes" in params, "Missing parameter 'superTypes'"

def test_qvtcdatadependencygraph::classnode_has_model():
    assert hasattr(qVTcDataDependencyGraph::ClassNode, "model")
    descriptor = None
    for klass in qVTcDataDependencyGraph::ClassNode.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)

def test_qvtcdatadependencygraph::classnode_has_superTypes():
    assert hasattr(qVTcDataDependencyGraph::ClassNode, "superTypes")
    descriptor = None
    for klass in qVTcDataDependencyGraph::ClassNode.__mro__:
        if "superTypes" in klass.__dict__:
            descriptor = klass.__dict__["superTypes"]
            break
    assert isinstance(descriptor, property)

def test_model_exists():
    # Check that the Enumeration exists
    assert Model is not None

def test_model_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Model]
    expected_literals = [
        "middle",
        "output",
        "input",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Model"

def test_dependencydirection_exists():
    # Check that the Enumeration exists
    assert DependencyDirection is not None

def test_dependencydirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DependencyDirection]
    expected_literals = [
        "input",
        "output",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DependencyDirection"


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
qVTcDataDependencyGraph::Graph_strategy = st.builds(
    qVTcDataDependencyGraph::Graph,
    name=
        safe_text
)
qVTcDataDependencyGraph::Element_strategy = st.builds(
    qVTcDataDependencyGraph::Element,
)
Element_strategy = st.builds(
    Element,
)
qVTcDataDependencyGraph::Node_strategy = st.builds(
    qVTcDataDependencyGraph::Node,
    label=
        safe_text
)
qVTcDataDependencyGraph::Edge_strategy = st.builds(
    qVTcDataDependencyGraph::Edge,
)
Edge_strategy = st.builds(
    Edge,
)
qVTcDataDependencyGraph::ContainmentEdge_strategy = st.builds(
    qVTcDataDependencyGraph::ContainmentEdge,
    model=
        safe_text
)
qVTcDataDependencyGraph::ReferenceEdge_strategy = st.builds(
    qVTcDataDependencyGraph::ReferenceEdge,
)
qVTcDataDependencyGraph::DependencyEdge_strategy = st.builds(
    qVTcDataDependencyGraph::DependencyEdge,
    direction=
        safe_text,
    multiple=
        st.booleans(),
    derived=
        st.booleans()
)
qVTcDataDependencyGraph::EObject_strategy = st.builds(
    qVTcDataDependencyGraph::EObject,
)
Node_strategy = st.builds(
    Node,
)
qVTcDataDependencyGraph::DataTypeNode_strategy = st.builds(
    qVTcDataDependencyGraph::DataTypeNode,
)
qVTcDataDependencyGraph::MappingNode_strategy = st.builds(
    qVTcDataDependencyGraph::MappingNode,
)
qVTcDataDependencyGraph::ClassNode_strategy = st.builds(
    qVTcDataDependencyGraph::ClassNode,
    model=
        safe_text,
    superTypes=
        safe_text
)

@given(instance=qVTcDataDependencyGraph::Graph_strategy)
@settings(max_examples=50)
def test_qvtcdatadependencygraph::graph_instantiation(instance):
    assert isinstance(instance, qVTcDataDependencyGraph::Graph)

@given(instance=qVTcDataDependencyGraph::Graph_strategy)
def test_qvtcdatadependencygraph::graph_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=qVTcDataDependencyGraph::Graph_strategy)
def test_qvtcdatadependencygraph::graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=qVTcDataDependencyGraph::Element_strategy)
@settings(max_examples=50)
def test_qvtcdatadependencygraph::element_instantiation(instance):
    assert isinstance(instance, qVTcDataDependencyGraph::Element)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=qVTcDataDependencyGraph::Node_strategy)
@settings(max_examples=50)
def test_qvtcdatadependencygraph::node_instantiation(instance):
    assert isinstance(instance, qVTcDataDependencyGraph::Node)

@given(instance=qVTcDataDependencyGraph::Node_strategy)
def test_qvtcdatadependencygraph::node_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=qVTcDataDependencyGraph::Node_strategy)
def test_qvtcdatadependencygraph::node_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=qVTcDataDependencyGraph::Edge_strategy)
@settings(max_examples=50)
def test_qvtcdatadependencygraph::edge_instantiation(instance):
    assert isinstance(instance, qVTcDataDependencyGraph::Edge)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=qVTcDataDependencyGraph::ContainmentEdge_strategy)
@settings(max_examples=50)
def test_qvtcdatadependencygraph::containmentedge_instantiation(instance):
    assert isinstance(instance, qVTcDataDependencyGraph::ContainmentEdge)

@given(instance=qVTcDataDependencyGraph::ContainmentEdge_strategy)
def test_qvtcdatadependencygraph::containmentedge_model_type(instance):
    assert isinstance(instance.model, str)


@given(instance=qVTcDataDependencyGraph::ContainmentEdge_strategy)
def test_qvtcdatadependencygraph::containmentedge_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original

@given(instance=qVTcDataDependencyGraph::ReferenceEdge_strategy)
@settings(max_examples=50)
def test_qvtcdatadependencygraph::referenceedge_instantiation(instance):
    assert isinstance(instance, qVTcDataDependencyGraph::ReferenceEdge)

@given(instance=qVTcDataDependencyGraph::DependencyEdge_strategy)
@settings(max_examples=50)
def test_qvtcdatadependencygraph::dependencyedge_instantiation(instance):
    assert isinstance(instance, qVTcDataDependencyGraph::DependencyEdge)

@given(instance=qVTcDataDependencyGraph::DependencyEdge_strategy)
def test_qvtcdatadependencygraph::dependencyedge_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=qVTcDataDependencyGraph::DependencyEdge_strategy)
def test_qvtcdatadependencygraph::dependencyedge_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=qVTcDataDependencyGraph::DependencyEdge_strategy)
def test_qvtcdatadependencygraph::dependencyedge_multiple_type(instance):
    assert isinstance(instance.multiple, bool)


@given(instance=qVTcDataDependencyGraph::DependencyEdge_strategy)
def test_qvtcdatadependencygraph::dependencyedge_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original

@given(instance=qVTcDataDependencyGraph::DependencyEdge_strategy)
def test_qvtcdatadependencygraph::dependencyedge_derived_type(instance):
    assert isinstance(instance.derived, bool)


@given(instance=qVTcDataDependencyGraph::DependencyEdge_strategy)
def test_qvtcdatadependencygraph::dependencyedge_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=qVTcDataDependencyGraph::EObject_strategy)
@settings(max_examples=50)
def test_qvtcdatadependencygraph::eobject_instantiation(instance):
    assert isinstance(instance, qVTcDataDependencyGraph::EObject)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=qVTcDataDependencyGraph::DataTypeNode_strategy)
@settings(max_examples=50)
def test_qvtcdatadependencygraph::datatypenode_instantiation(instance):
    assert isinstance(instance, qVTcDataDependencyGraph::DataTypeNode)

@given(instance=qVTcDataDependencyGraph::MappingNode_strategy)
@settings(max_examples=50)
def test_qvtcdatadependencygraph::mappingnode_instantiation(instance):
    assert isinstance(instance, qVTcDataDependencyGraph::MappingNode)

@given(instance=qVTcDataDependencyGraph::ClassNode_strategy)
@settings(max_examples=50)
def test_qvtcdatadependencygraph::classnode_instantiation(instance):
    assert isinstance(instance, qVTcDataDependencyGraph::ClassNode)

@given(instance=qVTcDataDependencyGraph::ClassNode_strategy)
def test_qvtcdatadependencygraph::classnode_model_type(instance):
    assert isinstance(instance.model, str)


@given(instance=qVTcDataDependencyGraph::ClassNode_strategy)
def test_qvtcdatadependencygraph::classnode_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original

@given(instance=qVTcDataDependencyGraph::ClassNode_strategy)
def test_qvtcdatadependencygraph::classnode_superTypes_type(instance):
    assert isinstance(instance.superTypes, str)


@given(instance=qVTcDataDependencyGraph::ClassNode_strategy)
def test_qvtcdatadependencygraph::classnode_superTypes_setter(instance):
    original = instance.superTypes
    instance.superTypes = original
    assert instance.superTypes == original
