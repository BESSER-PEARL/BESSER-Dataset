import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Node,
    notation::BendPoint,
    notation::Anchor,
    BendPoint,
    notation::AbsoluteBendPoint,
    notation::RelativeBendPoint,
    notation::EObject,
    Identifier,
    notation::DiagramElement,
    notation::HierarchicalNode,
    DiagramElement,
    notation::Edge,
    notation::Node,
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



def test_notation::bendpoint_is_not_abstract():
    assert not inspect.isabstract(notation::BendPoint)


def test_notation::bendpoint_constructor_exists():
    assert callable(notation::BendPoint.__init__)


def test_notation::bendpoint_constructor_args():
    sig = inspect.signature(notation::BendPoint.__init__)
    params = list(sig.parameters.keys())



def test_notation::anchor_is_not_abstract():
    assert not inspect.isabstract(notation::Anchor)


def test_notation::anchor_constructor_exists():
    assert callable(notation::Anchor.__init__)


def test_notation::anchor_constructor_args():
    sig = inspect.signature(notation::Anchor.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_notation::anchor_has_y():
    assert hasattr(notation::Anchor, "y")
    descriptor = None
    for klass in notation::Anchor.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_notation::anchor_has_x():
    assert hasattr(notation::Anchor, "x")
    descriptor = None
    for klass in notation::Anchor.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_bendpoint_is_not_abstract():
    assert not inspect.isabstract(BendPoint)


def test_bendpoint_constructor_exists():
    assert callable(BendPoint.__init__)


def test_bendpoint_constructor_args():
    sig = inspect.signature(BendPoint.__init__)
    params = list(sig.parameters.keys())



def test_notation::absolutebendpoint_is_not_abstract():
    assert not inspect.isabstract(notation::AbsoluteBendPoint)


def test_notation::absolutebendpoint_constructor_exists():
    assert callable(notation::AbsoluteBendPoint.__init__)


def test_notation::absolutebendpoint_constructor_args():
    sig = inspect.signature(notation::AbsoluteBendPoint.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_notation::absolutebendpoint_has_x():
    assert hasattr(notation::AbsoluteBendPoint, "x")
    descriptor = None
    for klass in notation::AbsoluteBendPoint.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_notation::absolutebendpoint_has_y():
    assert hasattr(notation::AbsoluteBendPoint, "y")
    descriptor = None
    for klass in notation::AbsoluteBendPoint.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_notation::relativebendpoint_is_not_abstract():
    assert not inspect.isabstract(notation::RelativeBendPoint)


def test_notation::relativebendpoint_constructor_exists():
    assert callable(notation::RelativeBendPoint.__init__)


def test_notation::relativebendpoint_constructor_args():
    sig = inspect.signature(notation::RelativeBendPoint.__init__)
    params = list(sig.parameters.keys())
    assert "targetY" in params, "Missing parameter 'targetY'"
    assert "sourceY" in params, "Missing parameter 'sourceY'"
    assert "targetX" in params, "Missing parameter 'targetX'"
    assert "sourceX" in params, "Missing parameter 'sourceX'"

def test_notation::relativebendpoint_has_targetY():
    assert hasattr(notation::RelativeBendPoint, "targetY")
    descriptor = None
    for klass in notation::RelativeBendPoint.__mro__:
        if "targetY" in klass.__dict__:
            descriptor = klass.__dict__["targetY"]
            break
    assert isinstance(descriptor, property)

def test_notation::relativebendpoint_has_sourceY():
    assert hasattr(notation::RelativeBendPoint, "sourceY")
    descriptor = None
    for klass in notation::RelativeBendPoint.__mro__:
        if "sourceY" in klass.__dict__:
            descriptor = klass.__dict__["sourceY"]
            break
    assert isinstance(descriptor, property)

def test_notation::relativebendpoint_has_targetX():
    assert hasattr(notation::RelativeBendPoint, "targetX")
    descriptor = None
    for klass in notation::RelativeBendPoint.__mro__:
        if "targetX" in klass.__dict__:
            descriptor = klass.__dict__["targetX"]
            break
    assert isinstance(descriptor, property)

def test_notation::relativebendpoint_has_sourceX():
    assert hasattr(notation::RelativeBendPoint, "sourceX")
    descriptor = None
    for klass in notation::RelativeBendPoint.__mro__:
        if "sourceX" in klass.__dict__:
            descriptor = klass.__dict__["sourceX"]
            break
    assert isinstance(descriptor, property)



def test_notation::eobject_is_not_abstract():
    assert not inspect.isabstract(notation::EObject)


def test_notation::eobject_constructor_exists():
    assert callable(notation::EObject.__init__)


def test_notation::eobject_constructor_args():
    sig = inspect.signature(notation::EObject.__init__)
    params = list(sig.parameters.keys())



def test_identifier_is_not_abstract():
    assert not inspect.isabstract(Identifier)


def test_identifier_constructor_exists():
    assert callable(Identifier.__init__)


def test_identifier_constructor_args():
    sig = inspect.signature(Identifier.__init__)
    params = list(sig.parameters.keys())



def test_notation::diagramelement_is_not_abstract():
    assert not inspect.isabstract(notation::DiagramElement)


def test_notation::diagramelement_constructor_exists():
    assert callable(notation::DiagramElement.__init__)


def test_notation::diagramelement_constructor_args():
    sig = inspect.signature(notation::DiagramElement.__init__)
    params = list(sig.parameters.keys())
    assert "persistent" in params, "Missing parameter 'persistent'"
    assert "visible" in params, "Missing parameter 'visible'"

def test_notation::diagramelement_has_persistent():
    assert hasattr(notation::DiagramElement, "persistent")
    descriptor = None
    for klass in notation::DiagramElement.__mro__:
        if "persistent" in klass.__dict__:
            descriptor = klass.__dict__["persistent"]
            break
    assert isinstance(descriptor, property)

def test_notation::diagramelement_has_visible():
    assert hasattr(notation::DiagramElement, "visible")
    descriptor = None
    for klass in notation::DiagramElement.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)



def test_notation::hierarchicalnode_is_not_abstract():
    assert not inspect.isabstract(notation::HierarchicalNode)


def test_notation::hierarchicalnode_constructor_exists():
    assert callable(notation::HierarchicalNode.__init__)


def test_notation::hierarchicalnode_constructor_args():
    sig = inspect.signature(notation::HierarchicalNode.__init__)
    params = list(sig.parameters.keys())



def test_diagramelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElement)


def test_diagramelement_constructor_exists():
    assert callable(DiagramElement.__init__)


def test_diagramelement_constructor_args():
    sig = inspect.signature(DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_notation::edge_is_not_abstract():
    assert not inspect.isabstract(notation::Edge)


def test_notation::edge_constructor_exists():
    assert callable(notation::Edge.__init__)


def test_notation::edge_constructor_args():
    sig = inspect.signature(notation::Edge.__init__)
    params = list(sig.parameters.keys())



def test_notation::node_is_not_abstract():
    assert not inspect.isabstract(notation::Node)


def test_notation::node_constructor_exists():
    assert callable(notation::Node.__init__)


def test_notation::node_constructor_args():
    sig = inspect.signature(notation::Node.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"
    assert "y" in params, "Missing parameter 'y'"

def test_notation::node_has_x():
    assert hasattr(notation::Node, "x")
    descriptor = None
    for klass in notation::Node.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_notation::node_has_height():
    assert hasattr(notation::Node, "height")
    descriptor = None
    for klass in notation::Node.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_notation::node_has_width():
    assert hasattr(notation::Node, "width")
    descriptor = None
    for klass in notation::Node.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_notation::node_has_y():
    assert hasattr(notation::Node, "y")
    descriptor = None
    for klass in notation::Node.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
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
notation::BendPoint_strategy = st.builds(
    notation::BendPoint,
)
notation::Anchor_strategy = st.builds(
    notation::Anchor,
    y=
        st.integers(),
    x=
        st.integers()
)
BendPoint_strategy = st.builds(
    BendPoint,
)
notation::AbsoluteBendPoint_strategy = st.builds(
    notation::AbsoluteBendPoint,
    x=
        st.integers(),
    y=
        st.integers()
)
notation::RelativeBendPoint_strategy = st.builds(
    notation::RelativeBendPoint,
    targetY=
        st.integers(),
    sourceY=
        st.integers(),
    targetX=
        st.integers(),
    sourceX=
        st.integers()
)
notation::EObject_strategy = st.builds(
    notation::EObject,
)
Identifier_strategy = st.builds(
    Identifier,
)
notation::DiagramElement_strategy = st.builds(
    notation::DiagramElement,
    persistent=
        st.booleans(),
    visible=
        st.booleans()
)
notation::HierarchicalNode_strategy = st.builds(
    notation::HierarchicalNode,
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
notation::Edge_strategy = st.builds(
    notation::Edge,
)
notation::Node_strategy = st.builds(
    notation::Node,
    x=
        st.integers(),
    height=
        st.integers(),
    width=
        st.integers(),
    y=
        st.integers()
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=notation::BendPoint_strategy)
@settings(max_examples=50)
def test_notation::bendpoint_instantiation(instance):
    assert isinstance(instance, notation::BendPoint)

@given(instance=notation::Anchor_strategy)
@settings(max_examples=50)
def test_notation::anchor_instantiation(instance):
    assert isinstance(instance, notation::Anchor)

@given(instance=notation::Anchor_strategy)
def test_notation::anchor_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=notation::Anchor_strategy)
def test_notation::anchor_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=notation::Anchor_strategy)
def test_notation::anchor_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=notation::Anchor_strategy)
def test_notation::anchor_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=BendPoint_strategy)
@settings(max_examples=50)
def test_bendpoint_instantiation(instance):
    assert isinstance(instance, BendPoint)

@given(instance=notation::AbsoluteBendPoint_strategy)
@settings(max_examples=50)
def test_notation::absolutebendpoint_instantiation(instance):
    assert isinstance(instance, notation::AbsoluteBendPoint)

@given(instance=notation::AbsoluteBendPoint_strategy)
def test_notation::absolutebendpoint_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=notation::AbsoluteBendPoint_strategy)
def test_notation::absolutebendpoint_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=notation::AbsoluteBendPoint_strategy)
def test_notation::absolutebendpoint_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=notation::AbsoluteBendPoint_strategy)
def test_notation::absolutebendpoint_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=notation::RelativeBendPoint_strategy)
@settings(max_examples=50)
def test_notation::relativebendpoint_instantiation(instance):
    assert isinstance(instance, notation::RelativeBendPoint)

@given(instance=notation::RelativeBendPoint_strategy)
def test_notation::relativebendpoint_targetY_type(instance):
    assert isinstance(instance.targetY, int)


@given(instance=notation::RelativeBendPoint_strategy)
def test_notation::relativebendpoint_targetY_setter(instance):
    original = instance.targetY
    instance.targetY = original
    assert instance.targetY == original

@given(instance=notation::RelativeBendPoint_strategy)
def test_notation::relativebendpoint_sourceY_type(instance):
    assert isinstance(instance.sourceY, int)


@given(instance=notation::RelativeBendPoint_strategy)
def test_notation::relativebendpoint_sourceY_setter(instance):
    original = instance.sourceY
    instance.sourceY = original
    assert instance.sourceY == original

@given(instance=notation::RelativeBendPoint_strategy)
def test_notation::relativebendpoint_targetX_type(instance):
    assert isinstance(instance.targetX, int)


@given(instance=notation::RelativeBendPoint_strategy)
def test_notation::relativebendpoint_targetX_setter(instance):
    original = instance.targetX
    instance.targetX = original
    assert instance.targetX == original

@given(instance=notation::RelativeBendPoint_strategy)
def test_notation::relativebendpoint_sourceX_type(instance):
    assert isinstance(instance.sourceX, int)


@given(instance=notation::RelativeBendPoint_strategy)
def test_notation::relativebendpoint_sourceX_setter(instance):
    original = instance.sourceX
    instance.sourceX = original
    assert instance.sourceX == original

@given(instance=notation::EObject_strategy)
@settings(max_examples=50)
def test_notation::eobject_instantiation(instance):
    assert isinstance(instance, notation::EObject)

@given(instance=Identifier_strategy)
@settings(max_examples=50)
def test_identifier_instantiation(instance):
    assert isinstance(instance, Identifier)

@given(instance=notation::DiagramElement_strategy)
@settings(max_examples=50)
def test_notation::diagramelement_instantiation(instance):
    assert isinstance(instance, notation::DiagramElement)

@given(instance=notation::DiagramElement_strategy)
def test_notation::diagramelement_persistent_type(instance):
    assert isinstance(instance.persistent, bool)


@given(instance=notation::DiagramElement_strategy)
def test_notation::diagramelement_persistent_setter(instance):
    original = instance.persistent
    instance.persistent = original
    assert instance.persistent == original

@given(instance=notation::DiagramElement_strategy)
def test_notation::diagramelement_visible_type(instance):
    assert isinstance(instance.visible, bool)


@given(instance=notation::DiagramElement_strategy)
def test_notation::diagramelement_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=notation::HierarchicalNode_strategy)
@settings(max_examples=50)
def test_notation::hierarchicalnode_instantiation(instance):
    assert isinstance(instance, notation::HierarchicalNode)

@given(instance=DiagramElement_strategy)
@settings(max_examples=50)
def test_diagramelement_instantiation(instance):
    assert isinstance(instance, DiagramElement)

@given(instance=notation::Edge_strategy)
@settings(max_examples=50)
def test_notation::edge_instantiation(instance):
    assert isinstance(instance, notation::Edge)

@given(instance=notation::Node_strategy)
@settings(max_examples=50)
def test_notation::node_instantiation(instance):
    assert isinstance(instance, notation::Node)

@given(instance=notation::Node_strategy)
def test_notation::node_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=notation::Node_strategy)
def test_notation::node_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=notation::Node_strategy)
def test_notation::node_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=notation::Node_strategy)
def test_notation::node_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=notation::Node_strategy)
def test_notation::node_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=notation::Node_strategy)
def test_notation::node_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=notation::Node_strategy)
def test_notation::node_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=notation::Node_strategy)
def test_notation::node_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original
