import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Node,
    notation_BendPoint,
    notation_Anchor,
    BendPoint,
    notation_AbsoluteBendPoint,
    notation_RelativeBendPoint,
    notation_EObject,
    Identifier,
    notation_DiagramElement,
    notation_HierarchicalNode,
    DiagramElement,
    notation_Edge,
    notation_Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_notation_bendpoint_is_not_abstract():
    assert not inspect.isabstract(notation_BendPoint)


def test_notation_bendpoint_constructor_exists():
    assert callable(notation_BendPoint.__init__)


def test_notation_bendpoint_constructor_args():
    sig = inspect.signature(notation_BendPoint.__init__)
    params = list(sig.parameters.keys())



def test_notation_anchor_is_not_abstract():
    assert not inspect.isabstract(notation_Anchor)


def test_notation_anchor_constructor_exists():
    assert callable(notation_Anchor.__init__)


def test_notation_anchor_constructor_args():
    sig = inspect.signature(notation_Anchor.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_notation_anchor_has_x():
    assert hasattr(notation_Anchor, "x")
    descriptor = None
    for klass in notation_Anchor.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_notation_anchor_has_y():
    assert hasattr(notation_Anchor, "y")
    descriptor = None
    for klass in notation_Anchor.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_bendpoint_is_not_abstract():
    assert not inspect.isabstract(BendPoint)


def test_bendpoint_constructor_exists():
    assert callable(BendPoint.__init__)


def test_bendpoint_constructor_args():
    sig = inspect.signature(BendPoint.__init__)
    params = list(sig.parameters.keys())



def test_notation_absolutebendpoint_is_not_abstract():
    assert not inspect.isabstract(notation_AbsoluteBendPoint)


def test_notation_absolutebendpoint_constructor_exists():
    assert callable(notation_AbsoluteBendPoint.__init__)


def test_notation_absolutebendpoint_constructor_args():
    sig = inspect.signature(notation_AbsoluteBendPoint.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_notation_absolutebendpoint_has_x():
    assert hasattr(notation_AbsoluteBendPoint, "x")
    descriptor = None
    for klass in notation_AbsoluteBendPoint.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_notation_absolutebendpoint_has_y():
    assert hasattr(notation_AbsoluteBendPoint, "y")
    descriptor = None
    for klass in notation_AbsoluteBendPoint.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_notation_relativebendpoint_is_not_abstract():
    assert not inspect.isabstract(notation_RelativeBendPoint)


def test_notation_relativebendpoint_constructor_exists():
    assert callable(notation_RelativeBendPoint.__init__)


def test_notation_relativebendpoint_constructor_args():
    sig = inspect.signature(notation_RelativeBendPoint.__init__)
    params = list(sig.parameters.keys())
    assert "sourceX" in params, "Missing parameter 'sourceX'"
    assert "targetY" in params, "Missing parameter 'targetY'"
    assert "sourceY" in params, "Missing parameter 'sourceY'"
    assert "targetX" in params, "Missing parameter 'targetX'"

def test_notation_relativebendpoint_has_sourceX():
    assert hasattr(notation_RelativeBendPoint, "sourceX")
    descriptor = None
    for klass in notation_RelativeBendPoint.__mro__:
        if "sourceX" in klass.__dict__:
            descriptor = klass.__dict__["sourceX"]
            break
    assert isinstance(descriptor, property)

def test_notation_relativebendpoint_has_targetY():
    assert hasattr(notation_RelativeBendPoint, "targetY")
    descriptor = None
    for klass in notation_RelativeBendPoint.__mro__:
        if "targetY" in klass.__dict__:
            descriptor = klass.__dict__["targetY"]
            break
    assert isinstance(descriptor, property)

def test_notation_relativebendpoint_has_sourceY():
    assert hasattr(notation_RelativeBendPoint, "sourceY")
    descriptor = None
    for klass in notation_RelativeBendPoint.__mro__:
        if "sourceY" in klass.__dict__:
            descriptor = klass.__dict__["sourceY"]
            break
    assert isinstance(descriptor, property)

def test_notation_relativebendpoint_has_targetX():
    assert hasattr(notation_RelativeBendPoint, "targetX")
    descriptor = None
    for klass in notation_RelativeBendPoint.__mro__:
        if "targetX" in klass.__dict__:
            descriptor = klass.__dict__["targetX"]
            break
    assert isinstance(descriptor, property)



def test_notation_eobject_is_not_abstract():
    assert not inspect.isabstract(notation_EObject)


def test_notation_eobject_constructor_exists():
    assert callable(notation_EObject.__init__)


def test_notation_eobject_constructor_args():
    sig = inspect.signature(notation_EObject.__init__)
    params = list(sig.parameters.keys())



def test_identifier_is_not_abstract():
    assert not inspect.isabstract(Identifier)


def test_identifier_constructor_exists():
    assert callable(Identifier.__init__)


def test_identifier_constructor_args():
    sig = inspect.signature(Identifier.__init__)
    params = list(sig.parameters.keys())



def test_notation_diagramelement_is_not_abstract():
    assert not inspect.isabstract(notation_DiagramElement)


def test_notation_diagramelement_constructor_exists():
    assert callable(notation_DiagramElement.__init__)


def test_notation_diagramelement_constructor_args():
    sig = inspect.signature(notation_DiagramElement.__init__)
    params = list(sig.parameters.keys())
    assert "persistent" in params, "Missing parameter 'persistent'"
    assert "visible" in params, "Missing parameter 'visible'"

def test_notation_diagramelement_has_persistent():
    assert hasattr(notation_DiagramElement, "persistent")
    descriptor = None
    for klass in notation_DiagramElement.__mro__:
        if "persistent" in klass.__dict__:
            descriptor = klass.__dict__["persistent"]
            break
    assert isinstance(descriptor, property)

def test_notation_diagramelement_has_visible():
    assert hasattr(notation_DiagramElement, "visible")
    descriptor = None
    for klass in notation_DiagramElement.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)



def test_notation_hierarchicalnode_is_not_abstract():
    assert not inspect.isabstract(notation_HierarchicalNode)


def test_notation_hierarchicalnode_constructor_exists():
    assert callable(notation_HierarchicalNode.__init__)


def test_notation_hierarchicalnode_constructor_args():
    sig = inspect.signature(notation_HierarchicalNode.__init__)
    params = list(sig.parameters.keys())



def test_diagramelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElement)


def test_diagramelement_constructor_exists():
    assert callable(DiagramElement.__init__)


def test_diagramelement_constructor_args():
    sig = inspect.signature(DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_notation_edge_is_not_abstract():
    assert not inspect.isabstract(notation_Edge)


def test_notation_edge_constructor_exists():
    assert callable(notation_Edge.__init__)


def test_notation_edge_constructor_args():
    sig = inspect.signature(notation_Edge.__init__)
    params = list(sig.parameters.keys())



def test_notation_node_is_not_abstract():
    assert not inspect.isabstract(notation_Node)


def test_notation_node_constructor_exists():
    assert callable(notation_Node.__init__)


def test_notation_node_constructor_args():
    sig = inspect.signature(notation_Node.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "height" in params, "Missing parameter 'height'"
    assert "y" in params, "Missing parameter 'y'"
    assert "width" in params, "Missing parameter 'width'"

def test_notation_node_has_x():
    assert hasattr(notation_Node, "x")
    descriptor = None
    for klass in notation_Node.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_notation_node_has_height():
    assert hasattr(notation_Node, "height")
    descriptor = None
    for klass in notation_Node.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_notation_node_has_y():
    assert hasattr(notation_Node, "y")
    descriptor = None
    for klass in notation_Node.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_notation_node_has_width():
    assert hasattr(notation_Node, "width")
    descriptor = None
    for klass in notation_Node.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
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
Node_strategy = st.builds(
    Node,
)
notation_BendPoint_strategy = st.builds(
    notation_BendPoint,
)
notation_Anchor_strategy = st.builds(
    notation_Anchor,
    x=
        st.integers(),
    y=
        st.integers()
)
BendPoint_strategy = st.builds(
    BendPoint,
)
notation_AbsoluteBendPoint_strategy = st.builds(
    notation_AbsoluteBendPoint,
    x=
        st.integers(),
    y=
        st.integers()
)
notation_RelativeBendPoint_strategy = st.builds(
    notation_RelativeBendPoint,
    sourceX=
        st.integers(),
    targetY=
        st.integers(),
    sourceY=
        st.integers(),
    targetX=
        st.integers()
)
notation_EObject_strategy = st.builds(
    notation_EObject,
)
Identifier_strategy = st.builds(
    Identifier,
)
notation_DiagramElement_strategy = st.builds(
    notation_DiagramElement,
    persistent=
        st.booleans(),
    visible=
        st.booleans()
)
notation_HierarchicalNode_strategy = st.builds(
    notation_HierarchicalNode,
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
notation_Edge_strategy = st.builds(
    notation_Edge,
)
notation_Node_strategy = st.builds(
    notation_Node,
    x=
        st.integers(),
    height=
        st.integers(),
    y=
        st.integers(),
    width=
        st.integers()
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=notation_BendPoint_strategy)
@settings(max_examples=50)
def test_notation_bendpoint_instantiation(instance):
    assert isinstance(instance, notation_BendPoint)

@given(instance=notation_Anchor_strategy)
@settings(max_examples=50)
def test_notation_anchor_instantiation(instance):
    assert isinstance(instance, notation_Anchor)



@given(instance=notation_Anchor_strategy)
def test_notation_anchor_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=notation_Anchor_strategy)
def test_notation_anchor_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=BendPoint_strategy)
@settings(max_examples=50)
def test_bendpoint_instantiation(instance):
    assert isinstance(instance, BendPoint)

@given(instance=notation_AbsoluteBendPoint_strategy)
@settings(max_examples=50)
def test_notation_absolutebendpoint_instantiation(instance):
    assert isinstance(instance, notation_AbsoluteBendPoint)



@given(instance=notation_AbsoluteBendPoint_strategy)
def test_notation_absolutebendpoint_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=notation_AbsoluteBendPoint_strategy)
def test_notation_absolutebendpoint_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=notation_RelativeBendPoint_strategy)
@settings(max_examples=50)
def test_notation_relativebendpoint_instantiation(instance):
    assert isinstance(instance, notation_RelativeBendPoint)



@given(instance=notation_RelativeBendPoint_strategy)
def test_notation_relativebendpoint_sourceX_setter(instance):
    original = instance.sourceX
    instance.sourceX = original
    assert instance.sourceX == original



@given(instance=notation_RelativeBendPoint_strategy)
def test_notation_relativebendpoint_targetY_setter(instance):
    original = instance.targetY
    instance.targetY = original
    assert instance.targetY == original



@given(instance=notation_RelativeBendPoint_strategy)
def test_notation_relativebendpoint_sourceY_setter(instance):
    original = instance.sourceY
    instance.sourceY = original
    assert instance.sourceY == original



@given(instance=notation_RelativeBendPoint_strategy)
def test_notation_relativebendpoint_targetX_setter(instance):
    original = instance.targetX
    instance.targetX = original
    assert instance.targetX == original

@given(instance=notation_EObject_strategy)
@settings(max_examples=50)
def test_notation_eobject_instantiation(instance):
    assert isinstance(instance, notation_EObject)

@given(instance=Identifier_strategy)
@settings(max_examples=50)
def test_identifier_instantiation(instance):
    assert isinstance(instance, Identifier)

@given(instance=notation_DiagramElement_strategy)
@settings(max_examples=50)
def test_notation_diagramelement_instantiation(instance):
    assert isinstance(instance, notation_DiagramElement)



@given(instance=notation_DiagramElement_strategy)
def test_notation_diagramelement_persistent_setter(instance):
    original = instance.persistent
    instance.persistent = original
    assert instance.persistent == original



@given(instance=notation_DiagramElement_strategy)
def test_notation_diagramelement_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=notation_HierarchicalNode_strategy)
@settings(max_examples=50)
def test_notation_hierarchicalnode_instantiation(instance):
    assert isinstance(instance, notation_HierarchicalNode)

@given(instance=DiagramElement_strategy)
@settings(max_examples=50)
def test_diagramelement_instantiation(instance):
    assert isinstance(instance, DiagramElement)

@given(instance=notation_Edge_strategy)
@settings(max_examples=50)
def test_notation_edge_instantiation(instance):
    assert isinstance(instance, notation_Edge)

@given(instance=notation_Node_strategy)
@settings(max_examples=50)
def test_notation_node_instantiation(instance):
    assert isinstance(instance, notation_Node)



@given(instance=notation_Node_strategy)
def test_notation_node_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=notation_Node_strategy)
def test_notation_node_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=notation_Node_strategy)
def test_notation_node_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=notation_Node_strategy)
def test_notation_node_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original
