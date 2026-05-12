import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    di_EStringToStringMapEntry,
    Shape,
    di_LabeledShape,
    Edge,
    di_LabeledEdge,
    di_Bounds,
    di_DocumentRoot,
    di_Style,
    DiagramElement,
    di_Node,
    di_Edge,
    di_ExtensionType,
    di_DiagramElement,
    Node,
    di_Plane,
    di_Shape,
    di_Label,
    di_Point,
    di_Diagram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_di_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(di_EStringToStringMapEntry)


def test_di_estringtostringmapentry_constructor_exists():
    assert callable(di_EStringToStringMapEntry.__init__)


def test_di_estringtostringmapentry_constructor_args():
    sig = inspect.signature(di_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_di_labeledshape_is_not_abstract():
    assert not inspect.isabstract(di_LabeledShape)


def test_di_labeledshape_constructor_exists():
    assert callable(di_LabeledShape.__init__)


def test_di_labeledshape_constructor_args():
    sig = inspect.signature(di_LabeledShape.__init__)
    params = list(sig.parameters.keys())



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_di_labelededge_is_not_abstract():
    assert not inspect.isabstract(di_LabeledEdge)


def test_di_labelededge_constructor_exists():
    assert callable(di_LabeledEdge.__init__)


def test_di_labelededge_constructor_args():
    sig = inspect.signature(di_LabeledEdge.__init__)
    params = list(sig.parameters.keys())



def test_di_bounds_is_not_abstract():
    assert not inspect.isabstract(di_Bounds)


def test_di_bounds_constructor_exists():
    assert callable(di_Bounds.__init__)


def test_di_bounds_constructor_args():
    sig = inspect.signature(di_Bounds.__init__)
    params = list(sig.parameters.keys())



def test_di_documentroot_is_not_abstract():
    assert not inspect.isabstract(di_DocumentRoot)


def test_di_documentroot_constructor_exists():
    assert callable(di_DocumentRoot.__init__)


def test_di_documentroot_constructor_args():
    sig = inspect.signature(di_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_di_documentroot_has_mixed():
    assert hasattr(di_DocumentRoot, "mixed")
    descriptor = None
    for klass in di_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_di_style_is_not_abstract():
    assert not inspect.isabstract(di_Style)


def test_di_style_constructor_exists():
    assert callable(di_Style.__init__)


def test_di_style_constructor_args():
    sig = inspect.signature(di_Style.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_di_style_has_id():
    assert hasattr(di_Style, "id")
    descriptor = None
    for klass in di_Style.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_diagramelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElement)


def test_diagramelement_constructor_exists():
    assert callable(DiagramElement.__init__)


def test_diagramelement_constructor_args():
    sig = inspect.signature(DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_di_node_is_not_abstract():
    assert not inspect.isabstract(di_Node)


def test_di_node_constructor_exists():
    assert callable(di_Node.__init__)


def test_di_node_constructor_args():
    sig = inspect.signature(di_Node.__init__)
    params = list(sig.parameters.keys())



def test_di_edge_is_not_abstract():
    assert not inspect.isabstract(di_Edge)


def test_di_edge_constructor_exists():
    assert callable(di_Edge.__init__)


def test_di_edge_constructor_args():
    sig = inspect.signature(di_Edge.__init__)
    params = list(sig.parameters.keys())



def test_di_extensiontype_is_not_abstract():
    assert not inspect.isabstract(di_ExtensionType)


def test_di_extensiontype_constructor_exists():
    assert callable(di_ExtensionType.__init__)


def test_di_extensiontype_constructor_args():
    sig = inspect.signature(di_ExtensionType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"

def test_di_extensiontype_has_any():
    assert hasattr(di_ExtensionType, "any")
    descriptor = None
    for klass in di_ExtensionType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_di_diagramelement_is_not_abstract():
    assert not inspect.isabstract(di_DiagramElement)


def test_di_diagramelement_constructor_exists():
    assert callable(di_DiagramElement.__init__)


def test_di_diagramelement_constructor_args():
    sig = inspect.signature(di_DiagramElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_di_diagramelement_has_id():
    assert hasattr(di_DiagramElement, "id")
    descriptor = None
    for klass in di_DiagramElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_di_diagramelement_has_anyAttribute():
    assert hasattr(di_DiagramElement, "anyAttribute")
    descriptor = None
    for klass in di_DiagramElement.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_di_plane_is_not_abstract():
    assert not inspect.isabstract(di_Plane)


def test_di_plane_constructor_exists():
    assert callable(di_Plane.__init__)


def test_di_plane_constructor_args():
    sig = inspect.signature(di_Plane.__init__)
    params = list(sig.parameters.keys())
    assert "diagramElementGroup" in params, "Missing parameter 'diagramElementGroup'"

def test_di_plane_has_diagramElementGroup():
    assert hasattr(di_Plane, "diagramElementGroup")
    descriptor = None
    for klass in di_Plane.__mro__:
        if "diagramElementGroup" in klass.__dict__:
            descriptor = klass.__dict__["diagramElementGroup"]
            break
    assert isinstance(descriptor, property)



def test_di_shape_is_not_abstract():
    assert not inspect.isabstract(di_Shape)


def test_di_shape_constructor_exists():
    assert callable(di_Shape.__init__)


def test_di_shape_constructor_args():
    sig = inspect.signature(di_Shape.__init__)
    params = list(sig.parameters.keys())



def test_di_label_is_not_abstract():
    assert not inspect.isabstract(di_Label)


def test_di_label_constructor_exists():
    assert callable(di_Label.__init__)


def test_di_label_constructor_args():
    sig = inspect.signature(di_Label.__init__)
    params = list(sig.parameters.keys())



def test_di_point_is_not_abstract():
    assert not inspect.isabstract(di_Point)


def test_di_point_constructor_exists():
    assert callable(di_Point.__init__)


def test_di_point_constructor_args():
    sig = inspect.signature(di_Point.__init__)
    params = list(sig.parameters.keys())



def test_di_diagram_is_not_abstract():
    assert not inspect.isabstract(di_Diagram)


def test_di_diagram_constructor_exists():
    assert callable(di_Diagram.__init__)


def test_di_diagram_constructor_args():
    sig = inspect.signature(di_Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "resolution" in params, "Missing parameter 'resolution'"
    assert "name" in params, "Missing parameter 'name'"

def test_di_diagram_has_id():
    assert hasattr(di_Diagram, "id")
    descriptor = None
    for klass in di_Diagram.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_di_diagram_has_documentation():
    assert hasattr(di_Diagram, "documentation")
    descriptor = None
    for klass in di_Diagram.__mro__:
        if "documentation" in klass.__dict__:
            descriptor = klass.__dict__["documentation"]
            break
    assert isinstance(descriptor, property)

def test_di_diagram_has_resolution():
    assert hasattr(di_Diagram, "resolution")
    descriptor = None
    for klass in di_Diagram.__mro__:
        if "resolution" in klass.__dict__:
            descriptor = klass.__dict__["resolution"]
            break
    assert isinstance(descriptor, property)

def test_di_diagram_has_name():
    assert hasattr(di_Diagram, "name")
    descriptor = None
    for klass in di_Diagram.__mro__:
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
di_EStringToStringMapEntry_strategy = st.builds(
    di_EStringToStringMapEntry,
)
Shape_strategy = st.builds(
    Shape,
)
di_LabeledShape_strategy = st.builds(
    di_LabeledShape,
)
Edge_strategy = st.builds(
    Edge,
)
di_LabeledEdge_strategy = st.builds(
    di_LabeledEdge,
)
di_Bounds_strategy = st.builds(
    di_Bounds,
)
di_DocumentRoot_strategy = st.builds(
    di_DocumentRoot,
    mixed=
        safe_text
)
di_Style_strategy = st.builds(
    di_Style,
    id=
        safe_text
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
di_Node_strategy = st.builds(
    di_Node,
)
di_Edge_strategy = st.builds(
    di_Edge,
)
di_ExtensionType_strategy = st.builds(
    di_ExtensionType,
    any=
        safe_text
)
di_DiagramElement_strategy = st.builds(
    di_DiagramElement,
    id=
        safe_text,
    anyAttribute=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
di_Plane_strategy = st.builds(
    di_Plane,
    diagramElementGroup=
        safe_text
)
di_Shape_strategy = st.builds(
    di_Shape,
)
di_Label_strategy = st.builds(
    di_Label,
)
di_Point_strategy = st.builds(
    di_Point,
)
di_Diagram_strategy = st.builds(
    di_Diagram,
    id=
        safe_text,
    documentation=
        safe_text,
    resolution=
        safe_text,
    name=
        safe_text
)

@given(instance=di_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_di_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, di_EStringToStringMapEntry)

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=di_LabeledShape_strategy)
@settings(max_examples=50)
def test_di_labeledshape_instantiation(instance):
    assert isinstance(instance, di_LabeledShape)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=di_LabeledEdge_strategy)
@settings(max_examples=50)
def test_di_labelededge_instantiation(instance):
    assert isinstance(instance, di_LabeledEdge)

@given(instance=di_Bounds_strategy)
@settings(max_examples=50)
def test_di_bounds_instantiation(instance):
    assert isinstance(instance, di_Bounds)

@given(instance=di_DocumentRoot_strategy)
@settings(max_examples=50)
def test_di_documentroot_instantiation(instance):
    assert isinstance(instance, di_DocumentRoot)



@given(instance=di_DocumentRoot_strategy)
def test_di_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=di_Style_strategy)
@settings(max_examples=50)
def test_di_style_instantiation(instance):
    assert isinstance(instance, di_Style)



@given(instance=di_Style_strategy)
def test_di_style_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=DiagramElement_strategy)
@settings(max_examples=50)
def test_diagramelement_instantiation(instance):
    assert isinstance(instance, DiagramElement)

@given(instance=di_Node_strategy)
@settings(max_examples=50)
def test_di_node_instantiation(instance):
    assert isinstance(instance, di_Node)

@given(instance=di_Edge_strategy)
@settings(max_examples=50)
def test_di_edge_instantiation(instance):
    assert isinstance(instance, di_Edge)

@given(instance=di_ExtensionType_strategy)
@settings(max_examples=50)
def test_di_extensiontype_instantiation(instance):
    assert isinstance(instance, di_ExtensionType)



@given(instance=di_ExtensionType_strategy)
def test_di_extensiontype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=di_DiagramElement_strategy)
@settings(max_examples=50)
def test_di_diagramelement_instantiation(instance):
    assert isinstance(instance, di_DiagramElement)



@given(instance=di_DiagramElement_strategy)
def test_di_diagramelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=di_DiagramElement_strategy)
def test_di_diagramelement_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=di_Plane_strategy)
@settings(max_examples=50)
def test_di_plane_instantiation(instance):
    assert isinstance(instance, di_Plane)



@given(instance=di_Plane_strategy)
def test_di_plane_diagramElementGroup_setter(instance):
    original = instance.diagramElementGroup
    instance.diagramElementGroup = original
    assert instance.diagramElementGroup == original

@given(instance=di_Shape_strategy)
@settings(max_examples=50)
def test_di_shape_instantiation(instance):
    assert isinstance(instance, di_Shape)

@given(instance=di_Label_strategy)
@settings(max_examples=50)
def test_di_label_instantiation(instance):
    assert isinstance(instance, di_Label)

@given(instance=di_Point_strategy)
@settings(max_examples=50)
def test_di_point_instantiation(instance):
    assert isinstance(instance, di_Point)

@given(instance=di_Diagram_strategy)
@settings(max_examples=50)
def test_di_diagram_instantiation(instance):
    assert isinstance(instance, di_Diagram)



@given(instance=di_Diagram_strategy)
def test_di_diagram_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=di_Diagram_strategy)
def test_di_diagram_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original



@given(instance=di_Diagram_strategy)
def test_di_diagram_resolution_setter(instance):
    original = instance.resolution
    instance.resolution = original
    assert instance.resolution == original



@given(instance=di_Diagram_strategy)
def test_di_diagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
