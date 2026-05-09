import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model::BendPoint,
    Node,
    model::AssociationNode,
    model::TypeNode,
    model::Edge,
    model::Node,
    model::Diagram,
    EdgeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model::bendpoint_is_not_abstract():
    assert not inspect.isabstract(model::BendPoint)


def test_model::bendpoint_constructor_exists():
    assert callable(model::BendPoint.__init__)


def test_model::bendpoint_constructor_args():
    sig = inspect.signature(model::BendPoint.__init__)
    params = list(sig.parameters.keys())
    assert "posY" in params, "Missing parameter 'posY'"
    assert "posX" in params, "Missing parameter 'posX'"

def test_model::bendpoint_has_posY():
    assert hasattr(model::BendPoint, "posY")
    descriptor = None
    for klass in model::BendPoint.__mro__:
        if "posY" in klass.__dict__:
            descriptor = klass.__dict__["posY"]
            break
    assert isinstance(descriptor, property)

def test_model::bendpoint_has_posX():
    assert hasattr(model::BendPoint, "posX")
    descriptor = None
    for klass in model::BendPoint.__mro__:
        if "posX" in klass.__dict__:
            descriptor = klass.__dict__["posX"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_model::associationnode_is_not_abstract():
    assert not inspect.isabstract(model::AssociationNode)


def test_model::associationnode_constructor_exists():
    assert callable(model::AssociationNode.__init__)


def test_model::associationnode_constructor_args():
    sig = inspect.signature(model::AssociationNode.__init__)
    params = list(sig.parameters.keys())
    assert "associationTypeConstraint" in params, "Missing parameter 'associationTypeConstraint'"

def test_model::associationnode_has_associationTypeConstraint():
    assert hasattr(model::AssociationNode, "associationTypeConstraint")
    descriptor = None
    for klass in model::AssociationNode.__mro__:
        if "associationTypeConstraint" in klass.__dict__:
            descriptor = klass.__dict__["associationTypeConstraint"]
            break
    assert isinstance(descriptor, property)



def test_model::typenode_is_not_abstract():
    assert not inspect.isabstract(model::TypeNode)


def test_model::typenode_constructor_exists():
    assert callable(model::TypeNode.__init__)


def test_model::typenode_constructor_args():
    sig = inspect.signature(model::TypeNode.__init__)
    params = list(sig.parameters.keys())
    assert "topicType" in params, "Missing parameter 'topicType'"

def test_model::typenode_has_topicType():
    assert hasattr(model::TypeNode, "topicType")
    descriptor = None
    for klass in model::TypeNode.__mro__:
        if "topicType" in klass.__dict__:
            descriptor = klass.__dict__["topicType"]
            break
    assert isinstance(descriptor, property)



def test_model::edge_is_not_abstract():
    assert not inspect.isabstract(model::Edge)


def test_model::edge_constructor_exists():
    assert callable(model::Edge.__init__)


def test_model::edge_constructor_args():
    sig = inspect.signature(model::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_model::edge_has_type():
    assert hasattr(model::Edge, "type")
    descriptor = None
    for klass in model::Edge.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_model::node_is_not_abstract():
    assert not inspect.isabstract(model::Node)


def test_model::node_constructor_exists():
    assert callable(model::Node.__init__)


def test_model::node_constructor_args():
    sig = inspect.signature(model::Node.__init__)
    params = list(sig.parameters.keys())
    assert "posX" in params, "Missing parameter 'posX'"
    assert "posY" in params, "Missing parameter 'posY'"

def test_model::node_has_posX():
    assert hasattr(model::Node, "posX")
    descriptor = None
    for klass in model::Node.__mro__:
        if "posX" in klass.__dict__:
            descriptor = klass.__dict__["posX"]
            break
    assert isinstance(descriptor, property)

def test_model::node_has_posY():
    assert hasattr(model::Node, "posY")
    descriptor = None
    for klass in model::Node.__mro__:
        if "posY" in klass.__dict__:
            descriptor = klass.__dict__["posY"]
            break
    assert isinstance(descriptor, property)



def test_model::diagram_is_not_abstract():
    assert not inspect.isabstract(model::Diagram)


def test_model::diagram_constructor_exists():
    assert callable(model::Diagram.__init__)


def test_model::diagram_constructor_args():
    sig = inspect.signature(model::Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "topicMapSchema" in params, "Missing parameter 'topicMapSchema'"

def test_model::diagram_has_topicMapSchema():
    assert hasattr(model::Diagram, "topicMapSchema")
    descriptor = None
    for klass in model::Diagram.__mro__:
        if "topicMapSchema" in klass.__dict__:
            descriptor = klass.__dict__["topicMapSchema"]
            break
    assert isinstance(descriptor, property)

def test_edgetype_exists():
    # Check that the Enumeration exists
    assert EdgeType is not None

def test_edgetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeType]
    expected_literals = [
        "AKO_TYPE",
        "ROLE_CONSTRAINT_TYPE",
        "IS_A_TYPE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeType"


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
model::BendPoint_strategy = st.builds(
    model::BendPoint,
    posY=
        st.integers(),
    posX=
        st.integers()
)
Node_strategy = st.builds(
    Node,
)
model::AssociationNode_strategy = st.builds(
    model::AssociationNode,
    associationTypeConstraint=
        safe_text
)
model::TypeNode_strategy = st.builds(
    model::TypeNode,
    topicType=
        safe_text
)
model::Edge_strategy = st.builds(
    model::Edge,
    type=
        safe_text
)
model::Node_strategy = st.builds(
    model::Node,
    posX=
        st.integers(),
    posY=
        st.integers()
)
model::Diagram_strategy = st.builds(
    model::Diagram,
    topicMapSchema=
        safe_text
)

@given(instance=model::BendPoint_strategy)
@settings(max_examples=50)
def test_model::bendpoint_instantiation(instance):
    assert isinstance(instance, model::BendPoint)

@given(instance=model::BendPoint_strategy)
def test_model::bendpoint_posY_type(instance):
    assert isinstance(instance.posY, int)


@given(instance=model::BendPoint_strategy)
def test_model::bendpoint_posY_setter(instance):
    original = instance.posY
    instance.posY = original
    assert instance.posY == original

@given(instance=model::BendPoint_strategy)
def test_model::bendpoint_posX_type(instance):
    assert isinstance(instance.posX, int)


@given(instance=model::BendPoint_strategy)
def test_model::bendpoint_posX_setter(instance):
    original = instance.posX
    instance.posX = original
    assert instance.posX == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=model::AssociationNode_strategy)
@settings(max_examples=50)
def test_model::associationnode_instantiation(instance):
    assert isinstance(instance, model::AssociationNode)

@given(instance=model::AssociationNode_strategy)
def test_model::associationnode_associationTypeConstraint_type(instance):
    assert isinstance(instance.associationTypeConstraint, str)


@given(instance=model::AssociationNode_strategy)
def test_model::associationnode_associationTypeConstraint_setter(instance):
    original = instance.associationTypeConstraint
    instance.associationTypeConstraint = original
    assert instance.associationTypeConstraint == original

@given(instance=model::TypeNode_strategy)
@settings(max_examples=50)
def test_model::typenode_instantiation(instance):
    assert isinstance(instance, model::TypeNode)

@given(instance=model::TypeNode_strategy)
def test_model::typenode_topicType_type(instance):
    assert isinstance(instance.topicType, str)


@given(instance=model::TypeNode_strategy)
def test_model::typenode_topicType_setter(instance):
    original = instance.topicType
    instance.topicType = original
    assert instance.topicType == original

@given(instance=model::Edge_strategy)
@settings(max_examples=50)
def test_model::edge_instantiation(instance):
    assert isinstance(instance, model::Edge)

@given(instance=model::Edge_strategy)
def test_model::edge_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=model::Edge_strategy)
def test_model::edge_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model::Node_strategy)
@settings(max_examples=50)
def test_model::node_instantiation(instance):
    assert isinstance(instance, model::Node)

@given(instance=model::Node_strategy)
def test_model::node_posX_type(instance):
    assert isinstance(instance.posX, int)


@given(instance=model::Node_strategy)
def test_model::node_posX_setter(instance):
    original = instance.posX
    instance.posX = original
    assert instance.posX == original

@given(instance=model::Node_strategy)
def test_model::node_posY_type(instance):
    assert isinstance(instance.posY, int)


@given(instance=model::Node_strategy)
def test_model::node_posY_setter(instance):
    original = instance.posY
    instance.posY = original
    assert instance.posY == original

@given(instance=model::Diagram_strategy)
@settings(max_examples=50)
def test_model::diagram_instantiation(instance):
    assert isinstance(instance, model::Diagram)

@given(instance=model::Diagram_strategy)
def test_model::diagram_topicMapSchema_type(instance):
    assert isinstance(instance.topicMapSchema, str)


@given(instance=model::Diagram_strategy)
def test_model::diagram_topicMapSchema_setter(instance):
    original = instance.topicMapSchema
    instance.topicMapSchema = original
    assert instance.topicMapSchema == original
