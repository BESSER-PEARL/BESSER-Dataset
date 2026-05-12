import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mtm_di_EStringToStringMapEntry,
    mtm_di_DocumentRoot,
    mtm_di_Style,
    Shape,
    mtm_di_LabeledShape,
    Edge,
    mtm_di_LabeledEdge,
    mtm_di_Bounds,
    Node,
    mtm_di_Plane,
    mtm_di_Shape,
    mtm_di_Label,
    mtm_di_Point,
    DiagramElement,
    mtm_di_Edge,
    mtm_di_Node,
    mtm_di_ExtensionType,
    mtm_di_DiagramElement,
    mtm_di_Diagram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mtm_di_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(mtm_di_EStringToStringMapEntry)


def test_mtm_di_estringtostringmapentry_constructor_exists():
    assert callable(mtm_di_EStringToStringMapEntry.__init__)


def test_mtm_di_estringtostringmapentry_constructor_args():
    sig = inspect.signature(mtm_di_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_mtm_di_documentroot_is_not_abstract():
    assert not inspect.isabstract(mtm_di_DocumentRoot)


def test_mtm_di_documentroot_constructor_exists():
    assert callable(mtm_di_DocumentRoot.__init__)


def test_mtm_di_documentroot_constructor_args():
    sig = inspect.signature(mtm_di_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_mtm_di_documentroot_has_mixed():
    assert hasattr(mtm_di_DocumentRoot, "mixed")
    descriptor = None
    for klass in mtm_di_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_mtm_di_style_is_not_abstract():
    assert not inspect.isabstract(mtm_di_Style)


def test_mtm_di_style_constructor_exists():
    assert callable(mtm_di_Style.__init__)


def test_mtm_di_style_constructor_args():
    sig = inspect.signature(mtm_di_Style.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mtm_di_style_has_id():
    assert hasattr(mtm_di_Style, "id")
    descriptor = None
    for klass in mtm_di_Style.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_mtm_di_labeledshape_is_not_abstract():
    assert not inspect.isabstract(mtm_di_LabeledShape)


def test_mtm_di_labeledshape_constructor_exists():
    assert callable(mtm_di_LabeledShape.__init__)


def test_mtm_di_labeledshape_constructor_args():
    sig = inspect.signature(mtm_di_LabeledShape.__init__)
    params = list(sig.parameters.keys())



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_mtm_di_labelededge_is_not_abstract():
    assert not inspect.isabstract(mtm_di_LabeledEdge)


def test_mtm_di_labelededge_constructor_exists():
    assert callable(mtm_di_LabeledEdge.__init__)


def test_mtm_di_labelededge_constructor_args():
    sig = inspect.signature(mtm_di_LabeledEdge.__init__)
    params = list(sig.parameters.keys())



def test_mtm_di_bounds_is_not_abstract():
    assert not inspect.isabstract(mtm_di_Bounds)


def test_mtm_di_bounds_constructor_exists():
    assert callable(mtm_di_Bounds.__init__)


def test_mtm_di_bounds_constructor_args():
    sig = inspect.signature(mtm_di_Bounds.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_mtm_di_plane_is_not_abstract():
    assert not inspect.isabstract(mtm_di_Plane)


def test_mtm_di_plane_constructor_exists():
    assert callable(mtm_di_Plane.__init__)


def test_mtm_di_plane_constructor_args():
    sig = inspect.signature(mtm_di_Plane.__init__)
    params = list(sig.parameters.keys())
    assert "diagramElementGroup" in params, "Missing parameter 'diagramElementGroup'"

def test_mtm_di_plane_has_diagramElementGroup():
    assert hasattr(mtm_di_Plane, "diagramElementGroup")
    descriptor = None
    for klass in mtm_di_Plane.__mro__:
        if "diagramElementGroup" in klass.__dict__:
            descriptor = klass.__dict__["diagramElementGroup"]
            break
    assert isinstance(descriptor, property)



def test_mtm_di_shape_is_not_abstract():
    assert not inspect.isabstract(mtm_di_Shape)


def test_mtm_di_shape_constructor_exists():
    assert callable(mtm_di_Shape.__init__)


def test_mtm_di_shape_constructor_args():
    sig = inspect.signature(mtm_di_Shape.__init__)
    params = list(sig.parameters.keys())



def test_mtm_di_label_is_not_abstract():
    assert not inspect.isabstract(mtm_di_Label)


def test_mtm_di_label_constructor_exists():
    assert callable(mtm_di_Label.__init__)


def test_mtm_di_label_constructor_args():
    sig = inspect.signature(mtm_di_Label.__init__)
    params = list(sig.parameters.keys())



def test_mtm_di_point_is_not_abstract():
    assert not inspect.isabstract(mtm_di_Point)


def test_mtm_di_point_constructor_exists():
    assert callable(mtm_di_Point.__init__)


def test_mtm_di_point_constructor_args():
    sig = inspect.signature(mtm_di_Point.__init__)
    params = list(sig.parameters.keys())



def test_diagramelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElement)


def test_diagramelement_constructor_exists():
    assert callable(DiagramElement.__init__)


def test_diagramelement_constructor_args():
    sig = inspect.signature(DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_mtm_di_edge_is_not_abstract():
    assert not inspect.isabstract(mtm_di_Edge)


def test_mtm_di_edge_constructor_exists():
    assert callable(mtm_di_Edge.__init__)


def test_mtm_di_edge_constructor_args():
    sig = inspect.signature(mtm_di_Edge.__init__)
    params = list(sig.parameters.keys())



def test_mtm_di_node_is_not_abstract():
    assert not inspect.isabstract(mtm_di_Node)


def test_mtm_di_node_constructor_exists():
    assert callable(mtm_di_Node.__init__)


def test_mtm_di_node_constructor_args():
    sig = inspect.signature(mtm_di_Node.__init__)
    params = list(sig.parameters.keys())



def test_mtm_di_extensiontype_is_not_abstract():
    assert not inspect.isabstract(mtm_di_ExtensionType)


def test_mtm_di_extensiontype_constructor_exists():
    assert callable(mtm_di_ExtensionType.__init__)


def test_mtm_di_extensiontype_constructor_args():
    sig = inspect.signature(mtm_di_ExtensionType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"

def test_mtm_di_extensiontype_has_any():
    assert hasattr(mtm_di_ExtensionType, "any")
    descriptor = None
    for klass in mtm_di_ExtensionType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_mtm_di_diagramelement_is_not_abstract():
    assert not inspect.isabstract(mtm_di_DiagramElement)


def test_mtm_di_diagramelement_constructor_exists():
    assert callable(mtm_di_DiagramElement.__init__)


def test_mtm_di_diagramelement_constructor_args():
    sig = inspect.signature(mtm_di_DiagramElement.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "id" in params, "Missing parameter 'id'"

def test_mtm_di_diagramelement_has_anyAttribute():
    assert hasattr(mtm_di_DiagramElement, "anyAttribute")
    descriptor = None
    for klass in mtm_di_DiagramElement.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_mtm_di_diagramelement_has_id():
    assert hasattr(mtm_di_DiagramElement, "id")
    descriptor = None
    for klass in mtm_di_DiagramElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mtm_di_diagram_is_not_abstract():
    assert not inspect.isabstract(mtm_di_Diagram)


def test_mtm_di_diagram_constructor_exists():
    assert callable(mtm_di_Diagram.__init__)


def test_mtm_di_diagram_constructor_args():
    sig = inspect.signature(mtm_di_Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "name" in params, "Missing parameter 'name'"
    assert "resolution" in params, "Missing parameter 'resolution'"
    assert "id" in params, "Missing parameter 'id'"

def test_mtm_di_diagram_has_documentation():
    assert hasattr(mtm_di_Diagram, "documentation")
    descriptor = None
    for klass in mtm_di_Diagram.__mro__:
        if "documentation" in klass.__dict__:
            descriptor = klass.__dict__["documentation"]
            break
    assert isinstance(descriptor, property)

def test_mtm_di_diagram_has_name():
    assert hasattr(mtm_di_Diagram, "name")
    descriptor = None
    for klass in mtm_di_Diagram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mtm_di_diagram_has_resolution():
    assert hasattr(mtm_di_Diagram, "resolution")
    descriptor = None
    for klass in mtm_di_Diagram.__mro__:
        if "resolution" in klass.__dict__:
            descriptor = klass.__dict__["resolution"]
            break
    assert isinstance(descriptor, property)

def test_mtm_di_diagram_has_id():
    assert hasattr(mtm_di_Diagram, "id")
    descriptor = None
    for klass in mtm_di_Diagram.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
mtm_di_EStringToStringMapEntry_strategy = st.builds(
    mtm_di_EStringToStringMapEntry,
)
mtm_di_DocumentRoot_strategy = st.builds(
    mtm_di_DocumentRoot,
    mixed=
        safe_text
)
mtm_di_Style_strategy = st.builds(
    mtm_di_Style,
    id=
        safe_text
)
Shape_strategy = st.builds(
    Shape,
)
mtm_di_LabeledShape_strategy = st.builds(
    mtm_di_LabeledShape,
)
Edge_strategy = st.builds(
    Edge,
)
mtm_di_LabeledEdge_strategy = st.builds(
    mtm_di_LabeledEdge,
)
mtm_di_Bounds_strategy = st.builds(
    mtm_di_Bounds,
)
Node_strategy = st.builds(
    Node,
)
mtm_di_Plane_strategy = st.builds(
    mtm_di_Plane,
    diagramElementGroup=
        safe_text
)
mtm_di_Shape_strategy = st.builds(
    mtm_di_Shape,
)
mtm_di_Label_strategy = st.builds(
    mtm_di_Label,
)
mtm_di_Point_strategy = st.builds(
    mtm_di_Point,
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
mtm_di_Edge_strategy = st.builds(
    mtm_di_Edge,
)
mtm_di_Node_strategy = st.builds(
    mtm_di_Node,
)
mtm_di_ExtensionType_strategy = st.builds(
    mtm_di_ExtensionType,
    any=
        safe_text
)
mtm_di_DiagramElement_strategy = st.builds(
    mtm_di_DiagramElement,
    anyAttribute=
        safe_text,
    id=
        safe_text
)
mtm_di_Diagram_strategy = st.builds(
    mtm_di_Diagram,
    documentation=
        safe_text,
    name=
        safe_text,
    resolution=
        safe_text,
    id=
        safe_text
)

@given(instance=mtm_di_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_mtm_di_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, mtm_di_EStringToStringMapEntry)

@given(instance=mtm_di_DocumentRoot_strategy)
@settings(max_examples=50)
def test_mtm_di_documentroot_instantiation(instance):
    assert isinstance(instance, mtm_di_DocumentRoot)



@given(instance=mtm_di_DocumentRoot_strategy)
def test_mtm_di_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=mtm_di_Style_strategy)
@settings(max_examples=50)
def test_mtm_di_style_instantiation(instance):
    assert isinstance(instance, mtm_di_Style)



@given(instance=mtm_di_Style_strategy)
def test_mtm_di_style_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=mtm_di_LabeledShape_strategy)
@settings(max_examples=50)
def test_mtm_di_labeledshape_instantiation(instance):
    assert isinstance(instance, mtm_di_LabeledShape)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=mtm_di_LabeledEdge_strategy)
@settings(max_examples=50)
def test_mtm_di_labelededge_instantiation(instance):
    assert isinstance(instance, mtm_di_LabeledEdge)

@given(instance=mtm_di_Bounds_strategy)
@settings(max_examples=50)
def test_mtm_di_bounds_instantiation(instance):
    assert isinstance(instance, mtm_di_Bounds)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=mtm_di_Plane_strategy)
@settings(max_examples=50)
def test_mtm_di_plane_instantiation(instance):
    assert isinstance(instance, mtm_di_Plane)



@given(instance=mtm_di_Plane_strategy)
def test_mtm_di_plane_diagramElementGroup_setter(instance):
    original = instance.diagramElementGroup
    instance.diagramElementGroup = original
    assert instance.diagramElementGroup == original

@given(instance=mtm_di_Shape_strategy)
@settings(max_examples=50)
def test_mtm_di_shape_instantiation(instance):
    assert isinstance(instance, mtm_di_Shape)

@given(instance=mtm_di_Label_strategy)
@settings(max_examples=50)
def test_mtm_di_label_instantiation(instance):
    assert isinstance(instance, mtm_di_Label)

@given(instance=mtm_di_Point_strategy)
@settings(max_examples=50)
def test_mtm_di_point_instantiation(instance):
    assert isinstance(instance, mtm_di_Point)

@given(instance=DiagramElement_strategy)
@settings(max_examples=50)
def test_diagramelement_instantiation(instance):
    assert isinstance(instance, DiagramElement)

@given(instance=mtm_di_Edge_strategy)
@settings(max_examples=50)
def test_mtm_di_edge_instantiation(instance):
    assert isinstance(instance, mtm_di_Edge)

@given(instance=mtm_di_Node_strategy)
@settings(max_examples=50)
def test_mtm_di_node_instantiation(instance):
    assert isinstance(instance, mtm_di_Node)

@given(instance=mtm_di_ExtensionType_strategy)
@settings(max_examples=50)
def test_mtm_di_extensiontype_instantiation(instance):
    assert isinstance(instance, mtm_di_ExtensionType)



@given(instance=mtm_di_ExtensionType_strategy)
def test_mtm_di_extensiontype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=mtm_di_DiagramElement_strategy)
@settings(max_examples=50)
def test_mtm_di_diagramelement_instantiation(instance):
    assert isinstance(instance, mtm_di_DiagramElement)



@given(instance=mtm_di_DiagramElement_strategy)
def test_mtm_di_diagramelement_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=mtm_di_DiagramElement_strategy)
def test_mtm_di_diagramelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=mtm_di_Diagram_strategy)
@settings(max_examples=50)
def test_mtm_di_diagram_instantiation(instance):
    assert isinstance(instance, mtm_di_Diagram)



@given(instance=mtm_di_Diagram_strategy)
def test_mtm_di_diagram_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original



@given(instance=mtm_di_Diagram_strategy)
def test_mtm_di_diagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mtm_di_Diagram_strategy)
def test_mtm_di_diagram_resolution_setter(instance):
    original = instance.resolution
    instance.resolution = original
    assert instance.resolution == original



@given(instance=mtm_di_Diagram_strategy)
def test_mtm_di_diagram_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
