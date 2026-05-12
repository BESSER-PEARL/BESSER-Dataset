import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    VisualModel,
    editormodel_NodeVisualModel,
    editormodel_EStringToEObjectMapEntry,
    editormodel_ConnectionBendpoint,
    editormodel_Adapter,
    editormodel_Color,
    editormodel_Dimension,
    editormodel_Point,
    editormodel_EObject,
    Adapter,
    NodeVisualModel,
    editormodel_VisualDiagramJump,
    editormodel_ConnectionVisualModel,
    ExtensibleElement,
    editormodel_FlabotFileModel,
    editormodel_Folder,
    editormodel_VisualModel,
    editormodel_Note,
    editormodel_CoreModel,
    NamedElementModel,
    editormodel_Diagram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_visualmodel_is_not_abstract():
    assert not inspect.isabstract(VisualModel)


def test_visualmodel_constructor_exists():
    assert callable(VisualModel.__init__)


def test_visualmodel_constructor_args():
    sig = inspect.signature(VisualModel.__init__)
    params = list(sig.parameters.keys())



def test_editormodel_nodevisualmodel_is_not_abstract():
    assert not inspect.isabstract(editormodel_NodeVisualModel)


def test_editormodel_nodevisualmodel_constructor_exists():
    assert callable(editormodel_NodeVisualModel.__init__)


def test_editormodel_nodevisualmodel_constructor_args():
    sig = inspect.signature(editormodel_NodeVisualModel.__init__)
    params = list(sig.parameters.keys())
    assert "rotation" in params, "Missing parameter 'rotation'"

def test_editormodel_nodevisualmodel_has_rotation():
    assert hasattr(editormodel_NodeVisualModel, "rotation")
    descriptor = None
    for klass in editormodel_NodeVisualModel.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)



def test_editormodel_estringtoeobjectmapentry_is_not_abstract():
    assert not inspect.isabstract(editormodel_EStringToEObjectMapEntry)


def test_editormodel_estringtoeobjectmapentry_constructor_exists():
    assert callable(editormodel_EStringToEObjectMapEntry.__init__)


def test_editormodel_estringtoeobjectmapentry_constructor_args():
    sig = inspect.signature(editormodel_EStringToEObjectMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_editormodel_estringtoeobjectmapentry_has_key():
    assert hasattr(editormodel_EStringToEObjectMapEntry, "key")
    descriptor = None
    for klass in editormodel_EStringToEObjectMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_editormodel_connectionbendpoint_is_not_abstract():
    assert not inspect.isabstract(editormodel_ConnectionBendpoint)


def test_editormodel_connectionbendpoint_constructor_exists():
    assert callable(editormodel_ConnectionBendpoint.__init__)


def test_editormodel_connectionbendpoint_constructor_args():
    sig = inspect.signature(editormodel_ConnectionBendpoint.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_editormodel_connectionbendpoint_has_weight():
    assert hasattr(editormodel_ConnectionBendpoint, "weight")
    descriptor = None
    for klass in editormodel_ConnectionBendpoint.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_editormodel_adapter_is_not_abstract():
    assert not inspect.isabstract(editormodel_Adapter)


def test_editormodel_adapter_constructor_exists():
    assert callable(editormodel_Adapter.__init__)


def test_editormodel_adapter_constructor_args():
    sig = inspect.signature(editormodel_Adapter.__init__)
    params = list(sig.parameters.keys())



def test_editormodel_color_is_not_abstract():
    assert not inspect.isabstract(editormodel_Color)


def test_editormodel_color_constructor_exists():
    assert callable(editormodel_Color.__init__)


def test_editormodel_color_constructor_args():
    sig = inspect.signature(editormodel_Color.__init__)
    params = list(sig.parameters.keys())
    assert "green" in params, "Missing parameter 'green'"
    assert "blue" in params, "Missing parameter 'blue'"
    assert "red" in params, "Missing parameter 'red'"

def test_editormodel_color_has_green():
    assert hasattr(editormodel_Color, "green")
    descriptor = None
    for klass in editormodel_Color.__mro__:
        if "green" in klass.__dict__:
            descriptor = klass.__dict__["green"]
            break
    assert isinstance(descriptor, property)

def test_editormodel_color_has_blue():
    assert hasattr(editormodel_Color, "blue")
    descriptor = None
    for klass in editormodel_Color.__mro__:
        if "blue" in klass.__dict__:
            descriptor = klass.__dict__["blue"]
            break
    assert isinstance(descriptor, property)

def test_editormodel_color_has_red():
    assert hasattr(editormodel_Color, "red")
    descriptor = None
    for klass in editormodel_Color.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
            break
    assert isinstance(descriptor, property)



def test_editormodel_dimension_is_not_abstract():
    assert not inspect.isabstract(editormodel_Dimension)


def test_editormodel_dimension_constructor_exists():
    assert callable(editormodel_Dimension.__init__)


def test_editormodel_dimension_constructor_args():
    sig = inspect.signature(editormodel_Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_editormodel_dimension_has_width():
    assert hasattr(editormodel_Dimension, "width")
    descriptor = None
    for klass in editormodel_Dimension.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_editormodel_dimension_has_height():
    assert hasattr(editormodel_Dimension, "height")
    descriptor = None
    for klass in editormodel_Dimension.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_editormodel_point_is_not_abstract():
    assert not inspect.isabstract(editormodel_Point)


def test_editormodel_point_constructor_exists():
    assert callable(editormodel_Point.__init__)


def test_editormodel_point_constructor_args():
    sig = inspect.signature(editormodel_Point.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_editormodel_point_has_y():
    assert hasattr(editormodel_Point, "y")
    descriptor = None
    for klass in editormodel_Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_editormodel_point_has_x():
    assert hasattr(editormodel_Point, "x")
    descriptor = None
    for klass in editormodel_Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_editormodel_eobject_is_not_abstract():
    assert not inspect.isabstract(editormodel_EObject)


def test_editormodel_eobject_constructor_exists():
    assert callable(editormodel_EObject.__init__)


def test_editormodel_eobject_constructor_args():
    sig = inspect.signature(editormodel_EObject.__init__)
    params = list(sig.parameters.keys())



def test_adapter_is_not_abstract():
    assert not inspect.isabstract(Adapter)


def test_adapter_constructor_exists():
    assert callable(Adapter.__init__)


def test_adapter_constructor_args():
    sig = inspect.signature(Adapter.__init__)
    params = list(sig.parameters.keys())



def test_nodevisualmodel_is_not_abstract():
    assert not inspect.isabstract(NodeVisualModel)


def test_nodevisualmodel_constructor_exists():
    assert callable(NodeVisualModel.__init__)


def test_nodevisualmodel_constructor_args():
    sig = inspect.signature(NodeVisualModel.__init__)
    params = list(sig.parameters.keys())



def test_editormodel_visualdiagramjump_is_not_abstract():
    assert not inspect.isabstract(editormodel_VisualDiagramJump)


def test_editormodel_visualdiagramjump_constructor_exists():
    assert callable(editormodel_VisualDiagramJump.__init__)


def test_editormodel_visualdiagramjump_constructor_args():
    sig = inspect.signature(editormodel_VisualDiagramJump.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"

def test_editormodel_visualdiagramjump_has_to():
    assert hasattr(editormodel_VisualDiagramJump, "to")
    descriptor = None
    for klass in editormodel_VisualDiagramJump.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_editormodel_connectionvisualmodel_is_not_abstract():
    assert not inspect.isabstract(editormodel_ConnectionVisualModel)


def test_editormodel_connectionvisualmodel_constructor_exists():
    assert callable(editormodel_ConnectionVisualModel.__init__)


def test_editormodel_connectionvisualmodel_constructor_args():
    sig = inspect.signature(editormodel_ConnectionVisualModel.__init__)
    params = list(sig.parameters.keys())
    assert "targetTerminal" in params, "Missing parameter 'targetTerminal'"
    assert "sourceTerminal" in params, "Missing parameter 'sourceTerminal'"

def test_editormodel_connectionvisualmodel_has_targetTerminal():
    assert hasattr(editormodel_ConnectionVisualModel, "targetTerminal")
    descriptor = None
    for klass in editormodel_ConnectionVisualModel.__mro__:
        if "targetTerminal" in klass.__dict__:
            descriptor = klass.__dict__["targetTerminal"]
            break
    assert isinstance(descriptor, property)

def test_editormodel_connectionvisualmodel_has_sourceTerminal():
    assert hasattr(editormodel_ConnectionVisualModel, "sourceTerminal")
    descriptor = None
    for klass in editormodel_ConnectionVisualModel.__mro__:
        if "sourceTerminal" in klass.__dict__:
            descriptor = klass.__dict__["sourceTerminal"]
            break
    assert isinstance(descriptor, property)



def test_extensibleelement_is_not_abstract():
    assert not inspect.isabstract(ExtensibleElement)


def test_extensibleelement_constructor_exists():
    assert callable(ExtensibleElement.__init__)


def test_extensibleelement_constructor_args():
    sig = inspect.signature(ExtensibleElement.__init__)
    params = list(sig.parameters.keys())



def test_editormodel_flabotfilemodel_is_not_abstract():
    assert not inspect.isabstract(editormodel_FlabotFileModel)


def test_editormodel_flabotfilemodel_constructor_exists():
    assert callable(editormodel_FlabotFileModel.__init__)


def test_editormodel_flabotfilemodel_constructor_args():
    sig = inspect.signature(editormodel_FlabotFileModel.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "provider" in params, "Missing parameter 'provider'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_editormodel_flabotfilemodel_has_version():
    assert hasattr(editormodel_FlabotFileModel, "version")
    descriptor = None
    for klass in editormodel_FlabotFileModel.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_editormodel_flabotfilemodel_has_provider():
    assert hasattr(editormodel_FlabotFileModel, "provider")
    descriptor = None
    for klass in editormodel_FlabotFileModel.__mro__:
        if "provider" in klass.__dict__:
            descriptor = klass.__dict__["provider"]
            break
    assert isinstance(descriptor, property)

def test_editormodel_flabotfilemodel_has_name():
    assert hasattr(editormodel_FlabotFileModel, "name")
    descriptor = None
    for klass in editormodel_FlabotFileModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_editormodel_flabotfilemodel_has_id():
    assert hasattr(editormodel_FlabotFileModel, "id")
    descriptor = None
    for klass in editormodel_FlabotFileModel.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_editormodel_folder_is_not_abstract():
    assert not inspect.isabstract(editormodel_Folder)


def test_editormodel_folder_constructor_exists():
    assert callable(editormodel_Folder.__init__)


def test_editormodel_folder_constructor_args():
    sig = inspect.signature(editormodel_Folder.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_editormodel_folder_has_name():
    assert hasattr(editormodel_Folder, "name")
    descriptor = None
    for klass in editormodel_Folder.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_editormodel_visualmodel_is_not_abstract():
    assert not inspect.isabstract(editormodel_VisualModel)


def test_editormodel_visualmodel_constructor_exists():
    assert callable(editormodel_VisualModel.__init__)


def test_editormodel_visualmodel_constructor_args():
    sig = inspect.signature(editormodel_VisualModel.__init__)
    params = list(sig.parameters.keys())
    assert "detailLevel" in params, "Missing parameter 'detailLevel'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"

def test_editormodel_visualmodel_has_detailLevel():
    assert hasattr(editormodel_VisualModel, "detailLevel")
    descriptor = None
    for klass in editormodel_VisualModel.__mro__:
        if "detailLevel" in klass.__dict__:
            descriptor = klass.__dict__["detailLevel"]
            break
    assert isinstance(descriptor, property)

def test_editormodel_visualmodel_has_lineStyle():
    assert hasattr(editormodel_VisualModel, "lineStyle")
    descriptor = None
    for klass in editormodel_VisualModel.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_editormodel_visualmodel_has_lineWidth():
    assert hasattr(editormodel_VisualModel, "lineWidth")
    descriptor = None
    for klass in editormodel_VisualModel.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)



def test_editormodel_note_is_not_abstract():
    assert not inspect.isabstract(editormodel_Note)


def test_editormodel_note_constructor_exists():
    assert callable(editormodel_Note.__init__)


def test_editormodel_note_constructor_args():
    sig = inspect.signature(editormodel_Note.__init__)
    params = list(sig.parameters.keys())



def test_editormodel_coremodel_is_not_abstract():
    assert not inspect.isabstract(editormodel_CoreModel)


def test_editormodel_coremodel_constructor_exists():
    assert callable(editormodel_CoreModel.__init__)


def test_editormodel_coremodel_constructor_args():
    sig = inspect.signature(editormodel_CoreModel.__init__)
    params = list(sig.parameters.keys())



def test_namedelementmodel_is_not_abstract():
    assert not inspect.isabstract(NamedElementModel)


def test_namedelementmodel_constructor_exists():
    assert callable(NamedElementModel.__init__)


def test_namedelementmodel_constructor_args():
    sig = inspect.signature(NamedElementModel.__init__)
    params = list(sig.parameters.keys())



def test_editormodel_diagram_is_not_abstract():
    assert not inspect.isabstract(editormodel_Diagram)


def test_editormodel_diagram_constructor_exists():
    assert callable(editormodel_Diagram.__init__)


def test_editormodel_diagram_constructor_args():
    sig = inspect.signature(editormodel_Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "snapToGeometryEnabled" in params, "Missing parameter 'snapToGeometryEnabled'"
    assert "gridEnabled" in params, "Missing parameter 'gridEnabled'"

def test_editormodel_diagram_has_snapToGeometryEnabled():
    assert hasattr(editormodel_Diagram, "snapToGeometryEnabled")
    descriptor = None
    for klass in editormodel_Diagram.__mro__:
        if "snapToGeometryEnabled" in klass.__dict__:
            descriptor = klass.__dict__["snapToGeometryEnabled"]
            break
    assert isinstance(descriptor, property)

def test_editormodel_diagram_has_gridEnabled():
    assert hasattr(editormodel_Diagram, "gridEnabled")
    descriptor = None
    for klass in editormodel_Diagram.__mro__:
        if "gridEnabled" in klass.__dict__:
            descriptor = klass.__dict__["gridEnabled"]
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
VisualModel_strategy = st.builds(
    VisualModel,
)
editormodel_NodeVisualModel_strategy = st.builds(
    editormodel_NodeVisualModel,
    rotation=
        safe_text
)
editormodel_EStringToEObjectMapEntry_strategy = st.builds(
    editormodel_EStringToEObjectMapEntry,
    key=
        safe_text
)
editormodel_ConnectionBendpoint_strategy = st.builds(
    editormodel_ConnectionBendpoint,
    weight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
editormodel_Adapter_strategy = st.builds(
    editormodel_Adapter,
)
editormodel_Color_strategy = st.builds(
    editormodel_Color,
    green=
        st.integers(),
    blue=
        st.integers(),
    red=
        st.integers()
)
editormodel_Dimension_strategy = st.builds(
    editormodel_Dimension,
    width=
        st.integers(),
    height=
        st.integers()
)
editormodel_Point_strategy = st.builds(
    editormodel_Point,
    y=
        st.integers(),
    x=
        st.integers()
)
editormodel_EObject_strategy = st.builds(
    editormodel_EObject,
)
Adapter_strategy = st.builds(
    Adapter,
)
NodeVisualModel_strategy = st.builds(
    NodeVisualModel,
)
editormodel_VisualDiagramJump_strategy = st.builds(
    editormodel_VisualDiagramJump,
    to=
        safe_text
)
editormodel_ConnectionVisualModel_strategy = st.builds(
    editormodel_ConnectionVisualModel,
    targetTerminal=
        safe_text,
    sourceTerminal=
        safe_text
)
ExtensibleElement_strategy = st.builds(
    ExtensibleElement,
)
editormodel_FlabotFileModel_strategy = st.builds(
    editormodel_FlabotFileModel,
    version=
        safe_text,
    provider=
        safe_text,
    name=
        safe_text,
    id=
        safe_text
)
editormodel_Folder_strategy = st.builds(
    editormodel_Folder,
    name=
        safe_text
)
editormodel_VisualModel_strategy = st.builds(
    editormodel_VisualModel,
    detailLevel=
        st.integers(),
    lineStyle=
        st.integers(),
    lineWidth=
        st.integers()
)
editormodel_Note_strategy = st.builds(
    editormodel_Note,
)
editormodel_CoreModel_strategy = st.builds(
    editormodel_CoreModel,
)
NamedElementModel_strategy = st.builds(
    NamedElementModel,
)
editormodel_Diagram_strategy = st.builds(
    editormodel_Diagram,
    snapToGeometryEnabled=
        safe_text,
    gridEnabled=
        safe_text
)

@given(instance=VisualModel_strategy)
@settings(max_examples=50)
def test_visualmodel_instantiation(instance):
    assert isinstance(instance, VisualModel)

@given(instance=editormodel_NodeVisualModel_strategy)
@settings(max_examples=50)
def test_editormodel_nodevisualmodel_instantiation(instance):
    assert isinstance(instance, editormodel_NodeVisualModel)



@given(instance=editormodel_NodeVisualModel_strategy)
def test_editormodel_nodevisualmodel_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original

@given(instance=editormodel_EStringToEObjectMapEntry_strategy)
@settings(max_examples=50)
def test_editormodel_estringtoeobjectmapentry_instantiation(instance):
    assert isinstance(instance, editormodel_EStringToEObjectMapEntry)



@given(instance=editormodel_EStringToEObjectMapEntry_strategy)
def test_editormodel_estringtoeobjectmapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=editormodel_ConnectionBendpoint_strategy)
@settings(max_examples=50)
def test_editormodel_connectionbendpoint_instantiation(instance):
    assert isinstance(instance, editormodel_ConnectionBendpoint)



@given(instance=editormodel_ConnectionBendpoint_strategy)
def test_editormodel_connectionbendpoint_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=editormodel_Adapter_strategy)
@settings(max_examples=50)
def test_editormodel_adapter_instantiation(instance):
    assert isinstance(instance, editormodel_Adapter)

@given(instance=editormodel_Color_strategy)
@settings(max_examples=50)
def test_editormodel_color_instantiation(instance):
    assert isinstance(instance, editormodel_Color)



@given(instance=editormodel_Color_strategy)
def test_editormodel_color_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original



@given(instance=editormodel_Color_strategy)
def test_editormodel_color_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original



@given(instance=editormodel_Color_strategy)
def test_editormodel_color_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original

@given(instance=editormodel_Dimension_strategy)
@settings(max_examples=50)
def test_editormodel_dimension_instantiation(instance):
    assert isinstance(instance, editormodel_Dimension)



@given(instance=editormodel_Dimension_strategy)
def test_editormodel_dimension_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=editormodel_Dimension_strategy)
def test_editormodel_dimension_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=editormodel_Point_strategy)
@settings(max_examples=50)
def test_editormodel_point_instantiation(instance):
    assert isinstance(instance, editormodel_Point)



@given(instance=editormodel_Point_strategy)
def test_editormodel_point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=editormodel_Point_strategy)
def test_editormodel_point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=editormodel_EObject_strategy)
@settings(max_examples=50)
def test_editormodel_eobject_instantiation(instance):
    assert isinstance(instance, editormodel_EObject)

@given(instance=Adapter_strategy)
@settings(max_examples=50)
def test_adapter_instantiation(instance):
    assert isinstance(instance, Adapter)

@given(instance=NodeVisualModel_strategy)
@settings(max_examples=50)
def test_nodevisualmodel_instantiation(instance):
    assert isinstance(instance, NodeVisualModel)

@given(instance=editormodel_VisualDiagramJump_strategy)
@settings(max_examples=50)
def test_editormodel_visualdiagramjump_instantiation(instance):
    assert isinstance(instance, editormodel_VisualDiagramJump)



@given(instance=editormodel_VisualDiagramJump_strategy)
def test_editormodel_visualdiagramjump_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=editormodel_ConnectionVisualModel_strategy)
@settings(max_examples=50)
def test_editormodel_connectionvisualmodel_instantiation(instance):
    assert isinstance(instance, editormodel_ConnectionVisualModel)



@given(instance=editormodel_ConnectionVisualModel_strategy)
def test_editormodel_connectionvisualmodel_targetTerminal_setter(instance):
    original = instance.targetTerminal
    instance.targetTerminal = original
    assert instance.targetTerminal == original



@given(instance=editormodel_ConnectionVisualModel_strategy)
def test_editormodel_connectionvisualmodel_sourceTerminal_setter(instance):
    original = instance.sourceTerminal
    instance.sourceTerminal = original
    assert instance.sourceTerminal == original

@given(instance=ExtensibleElement_strategy)
@settings(max_examples=50)
def test_extensibleelement_instantiation(instance):
    assert isinstance(instance, ExtensibleElement)

@given(instance=editormodel_FlabotFileModel_strategy)
@settings(max_examples=50)
def test_editormodel_flabotfilemodel_instantiation(instance):
    assert isinstance(instance, editormodel_FlabotFileModel)



@given(instance=editormodel_FlabotFileModel_strategy)
def test_editormodel_flabotfilemodel_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=editormodel_FlabotFileModel_strategy)
def test_editormodel_flabotfilemodel_provider_setter(instance):
    original = instance.provider
    instance.provider = original
    assert instance.provider == original



@given(instance=editormodel_FlabotFileModel_strategy)
def test_editormodel_flabotfilemodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=editormodel_FlabotFileModel_strategy)
def test_editormodel_flabotfilemodel_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=editormodel_Folder_strategy)
@settings(max_examples=50)
def test_editormodel_folder_instantiation(instance):
    assert isinstance(instance, editormodel_Folder)



@given(instance=editormodel_Folder_strategy)
def test_editormodel_folder_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=editormodel_VisualModel_strategy)
@settings(max_examples=50)
def test_editormodel_visualmodel_instantiation(instance):
    assert isinstance(instance, editormodel_VisualModel)



@given(instance=editormodel_VisualModel_strategy)
def test_editormodel_visualmodel_detailLevel_setter(instance):
    original = instance.detailLevel
    instance.detailLevel = original
    assert instance.detailLevel == original



@given(instance=editormodel_VisualModel_strategy)
def test_editormodel_visualmodel_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original



@given(instance=editormodel_VisualModel_strategy)
def test_editormodel_visualmodel_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original

@given(instance=editormodel_Note_strategy)
@settings(max_examples=50)
def test_editormodel_note_instantiation(instance):
    assert isinstance(instance, editormodel_Note)

@given(instance=editormodel_CoreModel_strategy)
@settings(max_examples=50)
def test_editormodel_coremodel_instantiation(instance):
    assert isinstance(instance, editormodel_CoreModel)

@given(instance=NamedElementModel_strategy)
@settings(max_examples=50)
def test_namedelementmodel_instantiation(instance):
    assert isinstance(instance, NamedElementModel)

@given(instance=editormodel_Diagram_strategy)
@settings(max_examples=50)
def test_editormodel_diagram_instantiation(instance):
    assert isinstance(instance, editormodel_Diagram)



@given(instance=editormodel_Diagram_strategy)
def test_editormodel_diagram_snapToGeometryEnabled_setter(instance):
    original = instance.snapToGeometryEnabled
    instance.snapToGeometryEnabled = original
    assert instance.snapToGeometryEnabled == original



@given(instance=editormodel_Diagram_strategy)
def test_editormodel_diagram_gridEnabled_setter(instance):
    original = instance.gridEnabled
    instance.gridEnabled = original
    assert instance.gridEnabled == original
