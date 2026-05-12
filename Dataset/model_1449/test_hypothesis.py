import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model_BendPoint,
    Node,
    model_AssociationNode,
    model_TypeNode,
    model_Edge,
    model_Node,
    model_Diagram,
    EdgeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_bendpoint_is_not_abstract():
    assert not inspect.isabstract(model_BendPoint)


def test_model_bendpoint_constructor_exists():
    assert callable(model_BendPoint.__init__)


def test_model_bendpoint_constructor_args():
    sig = inspect.signature(model_BendPoint.__init__)
    params = list(sig.parameters.keys())
    assert "posX" in params, "Missing parameter 'posX'"
    assert "posY" in params, "Missing parameter 'posY'"

def test_model_bendpoint_has_posX():
    assert hasattr(model_BendPoint, "posX")
    descriptor = None
    for klass in model_BendPoint.__mro__:
        if "posX" in klass.__dict__:
            descriptor = klass.__dict__["posX"]
            break
    assert isinstance(descriptor, property)

def test_model_bendpoint_has_posY():
    assert hasattr(model_BendPoint, "posY")
    descriptor = None
    for klass in model_BendPoint.__mro__:
        if "posY" in klass.__dict__:
            descriptor = klass.__dict__["posY"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_model_associationnode_is_not_abstract():
    assert not inspect.isabstract(model_AssociationNode)


def test_model_associationnode_constructor_exists():
    assert callable(model_AssociationNode.__init__)


def test_model_associationnode_constructor_args():
    sig = inspect.signature(model_AssociationNode.__init__)
    params = list(sig.parameters.keys())
    assert "associationTypeConstraint" in params, "Missing parameter 'associationTypeConstraint'"

def test_model_associationnode_has_associationTypeConstraint():
    assert hasattr(model_AssociationNode, "associationTypeConstraint")
    descriptor = None
    for klass in model_AssociationNode.__mro__:
        if "associationTypeConstraint" in klass.__dict__:
            descriptor = klass.__dict__["associationTypeConstraint"]
            break
    assert isinstance(descriptor, property)



def test_model_typenode_is_not_abstract():
    assert not inspect.isabstract(model_TypeNode)


def test_model_typenode_constructor_exists():
    assert callable(model_TypeNode.__init__)


def test_model_typenode_constructor_args():
    sig = inspect.signature(model_TypeNode.__init__)
    params = list(sig.parameters.keys())
    assert "topicType" in params, "Missing parameter 'topicType'"

def test_model_typenode_has_topicType():
    assert hasattr(model_TypeNode, "topicType")
    descriptor = None
    for klass in model_TypeNode.__mro__:
        if "topicType" in klass.__dict__:
            descriptor = klass.__dict__["topicType"]
            break
    assert isinstance(descriptor, property)



def test_model_edge_is_not_abstract():
    assert not inspect.isabstract(model_Edge)


def test_model_edge_constructor_exists():
    assert callable(model_Edge.__init__)


def test_model_edge_constructor_args():
    sig = inspect.signature(model_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_model_edge_has_type():
    assert hasattr(model_Edge, "type")
    descriptor = None
    for klass in model_Edge.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_model_node_is_not_abstract():
    assert not inspect.isabstract(model_Node)


def test_model_node_constructor_exists():
    assert callable(model_Node.__init__)


def test_model_node_constructor_args():
    sig = inspect.signature(model_Node.__init__)
    params = list(sig.parameters.keys())
    assert "posY" in params, "Missing parameter 'posY'"
    assert "posX" in params, "Missing parameter 'posX'"

def test_model_node_has_posY():
    assert hasattr(model_Node, "posY")
    descriptor = None
    for klass in model_Node.__mro__:
        if "posY" in klass.__dict__:
            descriptor = klass.__dict__["posY"]
            break
    assert isinstance(descriptor, property)

def test_model_node_has_posX():
    assert hasattr(model_Node, "posX")
    descriptor = None
    for klass in model_Node.__mro__:
        if "posX" in klass.__dict__:
            descriptor = klass.__dict__["posX"]
            break
    assert isinstance(descriptor, property)



def test_model_diagram_is_not_abstract():
    assert not inspect.isabstract(model_Diagram)


def test_model_diagram_constructor_exists():
    assert callable(model_Diagram.__init__)


def test_model_diagram_constructor_args():
    sig = inspect.signature(model_Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "topicMapSchema" in params, "Missing parameter 'topicMapSchema'"

def test_model_diagram_has_topicMapSchema():
    assert hasattr(model_Diagram, "topicMapSchema")
    descriptor = None
    for klass in model_Diagram.__mro__:
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
model_BendPoint_strategy = st.builds(
    model_BendPoint,
    posX=
        st.integers(),
    posY=
        st.integers()
)
Node_strategy = st.builds(
    Node,
)
model_AssociationNode_strategy = st.builds(
    model_AssociationNode,
    associationTypeConstraint=
        safe_text
)
model_TypeNode_strategy = st.builds(
    model_TypeNode,
    topicType=
        safe_text
)
model_Edge_strategy = st.builds(
    model_Edge,
    type=
        safe_text
)
model_Node_strategy = st.builds(
    model_Node,
    posY=
        st.integers(),
    posX=
        st.integers()
)
model_Diagram_strategy = st.builds(
    model_Diagram,
    topicMapSchema=
        safe_text
)

@given(instance=model_BendPoint_strategy)
@settings(max_examples=50)
def test_model_bendpoint_instantiation(instance):
    assert isinstance(instance, model_BendPoint)



@given(instance=model_BendPoint_strategy)
def test_model_bendpoint_posX_setter(instance):
    original = instance.posX
    instance.posX = original
    assert instance.posX == original



@given(instance=model_BendPoint_strategy)
def test_model_bendpoint_posY_setter(instance):
    original = instance.posY
    instance.posY = original
    assert instance.posY == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=model_AssociationNode_strategy)
@settings(max_examples=50)
def test_model_associationnode_instantiation(instance):
    assert isinstance(instance, model_AssociationNode)



@given(instance=model_AssociationNode_strategy)
def test_model_associationnode_associationTypeConstraint_setter(instance):
    original = instance.associationTypeConstraint
    instance.associationTypeConstraint = original
    assert instance.associationTypeConstraint == original

@given(instance=model_TypeNode_strategy)
@settings(max_examples=50)
def test_model_typenode_instantiation(instance):
    assert isinstance(instance, model_TypeNode)



@given(instance=model_TypeNode_strategy)
def test_model_typenode_topicType_setter(instance):
    original = instance.topicType
    instance.topicType = original
    assert instance.topicType == original

@given(instance=model_Edge_strategy)
@settings(max_examples=50)
def test_model_edge_instantiation(instance):
    assert isinstance(instance, model_Edge)



@given(instance=model_Edge_strategy)
def test_model_edge_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model_Node_strategy)
@settings(max_examples=50)
def test_model_node_instantiation(instance):
    assert isinstance(instance, model_Node)



@given(instance=model_Node_strategy)
def test_model_node_posY_setter(instance):
    original = instance.posY
    instance.posY = original
    assert instance.posY == original



@given(instance=model_Node_strategy)
def test_model_node_posX_setter(instance):
    original = instance.posX
    instance.posX = original
    assert instance.posX == original

@given(instance=model_Diagram_strategy)
@settings(max_examples=50)
def test_model_diagram_instantiation(instance):
    assert isinstance(instance, model_Diagram)



@given(instance=model_Diagram_strategy)
def test_model_diagram_topicMapSchema_setter(instance):
    original = instance.topicMapSchema
    instance.topicMapSchema = original
    assert instance.topicMapSchema == original
