import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    VisualModel,
    editormodel::NodeVisualModel,
    editormodel::EStringToEObjectMapEntry,
    editormodel::ConnectionBendpoint,
    editormodel::Adapter,
    editormodel::Color,
    editormodel::Dimension,
    editormodel::Point,
    editormodel::EObject,
    Adapter,
    NodeVisualModel,
    editormodel::VisualDiagramJump,
    editormodel::ConnectionVisualModel,
    ExtensibleElement,
    editormodel::FlabotFileModel,
    editormodel::Folder,
    editormodel::VisualModel,
    editormodel::Note,
    editormodel::CoreModel,
    NamedElementModel,
    editormodel::Diagram,
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



def test_editormodel::nodevisualmodel_is_not_abstract():
    assert not inspect.isabstract(editormodel::NodeVisualModel)


def test_editormodel::nodevisualmodel_constructor_exists():
    assert callable(editormodel::NodeVisualModel.__init__)


def test_editormodel::nodevisualmodel_constructor_args():
    sig = inspect.signature(editormodel::NodeVisualModel.__init__)
    params = list(sig.parameters.keys())
    assert "rotation" in params, "Missing parameter 'rotation'"

def test_editormodel::nodevisualmodel_has_rotation():
    assert hasattr(editormodel::NodeVisualModel, "rotation")
    descriptor = None
    for klass in editormodel::NodeVisualModel.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)



def test_editormodel::estringtoeobjectmapentry_is_not_abstract():
    assert not inspect.isabstract(editormodel::EStringToEObjectMapEntry)


def test_editormodel::estringtoeobjectmapentry_constructor_exists():
    assert callable(editormodel::EStringToEObjectMapEntry.__init__)


def test_editormodel::estringtoeobjectmapentry_constructor_args():
    sig = inspect.signature(editormodel::EStringToEObjectMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_editormodel::estringtoeobjectmapentry_has_key():
    assert hasattr(editormodel::EStringToEObjectMapEntry, "key")
    descriptor = None
    for klass in editormodel::EStringToEObjectMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_editormodel::connectionbendpoint_is_not_abstract():
    assert not inspect.isabstract(editormodel::ConnectionBendpoint)


def test_editormodel::connectionbendpoint_constructor_exists():
    assert callable(editormodel::ConnectionBendpoint.__init__)


def test_editormodel::connectionbendpoint_constructor_args():
    sig = inspect.signature(editormodel::ConnectionBendpoint.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_editormodel::connectionbendpoint_has_weight():
    assert hasattr(editormodel::ConnectionBendpoint, "weight")
    descriptor = None
    for klass in editormodel::ConnectionBendpoint.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_editormodel::adapter_is_not_abstract():
    assert not inspect.isabstract(editormodel::Adapter)


def test_editormodel::adapter_constructor_exists():
    assert callable(editormodel::Adapter.__init__)


def test_editormodel::adapter_constructor_args():
    sig = inspect.signature(editormodel::Adapter.__init__)
    params = list(sig.parameters.keys())



def test_editormodel::color_is_not_abstract():
    assert not inspect.isabstract(editormodel::Color)


def test_editormodel::color_constructor_exists():
    assert callable(editormodel::Color.__init__)


def test_editormodel::color_constructor_args():
    sig = inspect.signature(editormodel::Color.__init__)
    params = list(sig.parameters.keys())
    assert "green" in params, "Missing parameter 'green'"
    assert "blue" in params, "Missing parameter 'blue'"
    assert "red" in params, "Missing parameter 'red'"

def test_editormodel::color_has_green():
    assert hasattr(editormodel::Color, "green")
    descriptor = None
    for klass in editormodel::Color.__mro__:
        if "green" in klass.__dict__:
            descriptor = klass.__dict__["green"]
            break
    assert isinstance(descriptor, property)

def test_editormodel::color_has_blue():
    assert hasattr(editormodel::Color, "blue")
    descriptor = None
    for klass in editormodel::Color.__mro__:
        if "blue" in klass.__dict__:
            descriptor = klass.__dict__["blue"]
            break
    assert isinstance(descriptor, property)

def test_editormodel::color_has_red():
    assert hasattr(editormodel::Color, "red")
    descriptor = None
    for klass in editormodel::Color.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
            break
    assert isinstance(descriptor, property)



def test_editormodel::dimension_is_not_abstract():
    assert not inspect.isabstract(editormodel::Dimension)


def test_editormodel::dimension_constructor_exists():
    assert callable(editormodel::Dimension.__init__)


def test_editormodel::dimension_constructor_args():
    sig = inspect.signature(editormodel::Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_editormodel::dimension_has_height():
    assert hasattr(editormodel::Dimension, "height")
    descriptor = None
    for klass in editormodel::Dimension.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_editormodel::dimension_has_width():
    assert hasattr(editormodel::Dimension, "width")
    descriptor = None
    for klass in editormodel::Dimension.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_editormodel::point_is_not_abstract():
    assert not inspect.isabstract(editormodel::Point)


def test_editormodel::point_constructor_exists():
    assert callable(editormodel::Point.__init__)


def test_editormodel::point_constructor_args():
    sig = inspect.signature(editormodel::Point.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_editormodel::point_has_x():
    assert hasattr(editormodel::Point, "x")
    descriptor = None
    for klass in editormodel::Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_editormodel::point_has_y():
    assert hasattr(editormodel::Point, "y")
    descriptor = None
    for klass in editormodel::Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_editormodel::eobject_is_not_abstract():
    assert not inspect.isabstract(editormodel::EObject)


def test_editormodel::eobject_constructor_exists():
    assert callable(editormodel::EObject.__init__)


def test_editormodel::eobject_constructor_args():
    sig = inspect.signature(editormodel::EObject.__init__)
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



def test_editormodel::visualdiagramjump_is_not_abstract():
    assert not inspect.isabstract(editormodel::VisualDiagramJump)


def test_editormodel::visualdiagramjump_constructor_exists():
    assert callable(editormodel::VisualDiagramJump.__init__)


def test_editormodel::visualdiagramjump_constructor_args():
    sig = inspect.signature(editormodel::VisualDiagramJump.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"

def test_editormodel::visualdiagramjump_has_to():
    assert hasattr(editormodel::VisualDiagramJump, "to")
    descriptor = None
    for klass in editormodel::VisualDiagramJump.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_editormodel::connectionvisualmodel_is_not_abstract():
    assert not inspect.isabstract(editormodel::ConnectionVisualModel)


def test_editormodel::connectionvisualmodel_constructor_exists():
    assert callable(editormodel::ConnectionVisualModel.__init__)


def test_editormodel::connectionvisualmodel_constructor_args():
    sig = inspect.signature(editormodel::ConnectionVisualModel.__init__)
    params = list(sig.parameters.keys())
    assert "sourceTerminal" in params, "Missing parameter 'sourceTerminal'"
    assert "targetTerminal" in params, "Missing parameter 'targetTerminal'"

def test_editormodel::connectionvisualmodel_has_sourceTerminal():
    assert hasattr(editormodel::ConnectionVisualModel, "sourceTerminal")
    descriptor = None
    for klass in editormodel::ConnectionVisualModel.__mro__:
        if "sourceTerminal" in klass.__dict__:
            descriptor = klass.__dict__["sourceTerminal"]
            break
    assert isinstance(descriptor, property)

def test_editormodel::connectionvisualmodel_has_targetTerminal():
    assert hasattr(editormodel::ConnectionVisualModel, "targetTerminal")
    descriptor = None
    for klass in editormodel::ConnectionVisualModel.__mro__:
        if "targetTerminal" in klass.__dict__:
            descriptor = klass.__dict__["targetTerminal"]
            break
    assert isinstance(descriptor, property)



def test_extensibleelement_is_not_abstract():
    assert not inspect.isabstract(ExtensibleElement)


def test_extensibleelement_constructor_exists():
    assert callable(ExtensibleElement.__init__)


def test_extensibleelement_constructor_args():
    sig = inspect.signature(ExtensibleElement.__init__)
    params = list(sig.parameters.keys())



def test_editormodel::flabotfilemodel_is_not_abstract():
    assert not inspect.isabstract(editormodel::FlabotFileModel)


def test_editormodel::flabotfilemodel_constructor_exists():
    assert callable(editormodel::FlabotFileModel.__init__)


def test_editormodel::flabotfilemodel_constructor_args():
    sig = inspect.signature(editormodel::FlabotFileModel.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "provider" in params, "Missing parameter 'provider'"
    assert "version" in params, "Missing parameter 'version'"

def test_editormodel::flabotfilemodel_has_id():
    assert hasattr(editormodel::FlabotFileModel, "id")
    descriptor = None
    for klass in editormodel::FlabotFileModel.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_editormodel::flabotfilemodel_has_name():
    assert hasattr(editormodel::FlabotFileModel, "name")
    descriptor = None
    for klass in editormodel::FlabotFileModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_editormodel::flabotfilemodel_has_provider():
    assert hasattr(editormodel::FlabotFileModel, "provider")
    descriptor = None
    for klass in editormodel::FlabotFileModel.__mro__:
        if "provider" in klass.__dict__:
            descriptor = klass.__dict__["provider"]
            break
    assert isinstance(descriptor, property)

def test_editormodel::flabotfilemodel_has_version():
    assert hasattr(editormodel::FlabotFileModel, "version")
    descriptor = None
    for klass in editormodel::FlabotFileModel.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_editormodel::folder_is_not_abstract():
    assert not inspect.isabstract(editormodel::Folder)


def test_editormodel::folder_constructor_exists():
    assert callable(editormodel::Folder.__init__)


def test_editormodel::folder_constructor_args():
    sig = inspect.signature(editormodel::Folder.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_editormodel::folder_has_name():
    assert hasattr(editormodel::Folder, "name")
    descriptor = None
    for klass in editormodel::Folder.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_editormodel::visualmodel_is_not_abstract():
    assert not inspect.isabstract(editormodel::VisualModel)


def test_editormodel::visualmodel_constructor_exists():
    assert callable(editormodel::VisualModel.__init__)


def test_editormodel::visualmodel_constructor_args():
    sig = inspect.signature(editormodel::VisualModel.__init__)
    params = list(sig.parameters.keys())
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "detailLevel" in params, "Missing parameter 'detailLevel'"
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"

def test_editormodel::visualmodel_has_lineStyle():
    assert hasattr(editormodel::VisualModel, "lineStyle")
    descriptor = None
    for klass in editormodel::VisualModel.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_editormodel::visualmodel_has_detailLevel():
    assert hasattr(editormodel::VisualModel, "detailLevel")
    descriptor = None
    for klass in editormodel::VisualModel.__mro__:
        if "detailLevel" in klass.__dict__:
            descriptor = klass.__dict__["detailLevel"]
            break
    assert isinstance(descriptor, property)

def test_editormodel::visualmodel_has_lineWidth():
    assert hasattr(editormodel::VisualModel, "lineWidth")
    descriptor = None
    for klass in editormodel::VisualModel.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)



def test_editormodel::note_is_not_abstract():
    assert not inspect.isabstract(editormodel::Note)


def test_editormodel::note_constructor_exists():
    assert callable(editormodel::Note.__init__)


def test_editormodel::note_constructor_args():
    sig = inspect.signature(editormodel::Note.__init__)
    params = list(sig.parameters.keys())



def test_editormodel::coremodel_is_not_abstract():
    assert not inspect.isabstract(editormodel::CoreModel)


def test_editormodel::coremodel_constructor_exists():
    assert callable(editormodel::CoreModel.__init__)


def test_editormodel::coremodel_constructor_args():
    sig = inspect.signature(editormodel::CoreModel.__init__)
    params = list(sig.parameters.keys())



def test_namedelementmodel_is_not_abstract():
    assert not inspect.isabstract(NamedElementModel)


def test_namedelementmodel_constructor_exists():
    assert callable(NamedElementModel.__init__)


def test_namedelementmodel_constructor_args():
    sig = inspect.signature(NamedElementModel.__init__)
    params = list(sig.parameters.keys())



def test_editormodel::diagram_is_not_abstract():
    assert not inspect.isabstract(editormodel::Diagram)


def test_editormodel::diagram_constructor_exists():
    assert callable(editormodel::Diagram.__init__)


def test_editormodel::diagram_constructor_args():
    sig = inspect.signature(editormodel::Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "snapToGeometryEnabled" in params, "Missing parameter 'snapToGeometryEnabled'"
    assert "gridEnabled" in params, "Missing parameter 'gridEnabled'"

def test_editormodel::diagram_has_snapToGeometryEnabled():
    assert hasattr(editormodel::Diagram, "snapToGeometryEnabled")
    descriptor = None
    for klass in editormodel::Diagram.__mro__:
        if "snapToGeometryEnabled" in klass.__dict__:
            descriptor = klass.__dict__["snapToGeometryEnabled"]
            break
    assert isinstance(descriptor, property)

def test_editormodel::diagram_has_gridEnabled():
    assert hasattr(editormodel::Diagram, "gridEnabled")
    descriptor = None
    for klass in editormodel::Diagram.__mro__:
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
editormodel::NodeVisualModel_strategy = st.builds(
    editormodel::NodeVisualModel,
    rotation=
        safe_text
)
editormodel::EStringToEObjectMapEntry_strategy = st.builds(
    editormodel::EStringToEObjectMapEntry,
    key=
        safe_text
)
editormodel::ConnectionBendpoint_strategy = st.builds(
    editormodel::ConnectionBendpoint,
    weight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
editormodel::Adapter_strategy = st.builds(
    editormodel::Adapter,
)
editormodel::Color_strategy = st.builds(
    editormodel::Color,
    green=
        st.integers(),
    blue=
        st.integers(),
    red=
        st.integers()
)
editormodel::Dimension_strategy = st.builds(
    editormodel::Dimension,
    height=
        st.integers(),
    width=
        st.integers()
)
editormodel::Point_strategy = st.builds(
    editormodel::Point,
    x=
        st.integers(),
    y=
        st.integers()
)
editormodel::EObject_strategy = st.builds(
    editormodel::EObject,
)
Adapter_strategy = st.builds(
    Adapter,
)
NodeVisualModel_strategy = st.builds(
    NodeVisualModel,
)
editormodel::VisualDiagramJump_strategy = st.builds(
    editormodel::VisualDiagramJump,
    to=
        safe_text
)
editormodel::ConnectionVisualModel_strategy = st.builds(
    editormodel::ConnectionVisualModel,
    sourceTerminal=
        safe_text,
    targetTerminal=
        safe_text
)
ExtensibleElement_strategy = st.builds(
    ExtensibleElement,
)
editormodel::FlabotFileModel_strategy = st.builds(
    editormodel::FlabotFileModel,
    id=
        safe_text,
    name=
        safe_text,
    provider=
        safe_text,
    version=
        safe_text
)
editormodel::Folder_strategy = st.builds(
    editormodel::Folder,
    name=
        safe_text
)
editormodel::VisualModel_strategy = st.builds(
    editormodel::VisualModel,
    lineStyle=
        st.integers(),
    detailLevel=
        st.integers(),
    lineWidth=
        st.integers()
)
editormodel::Note_strategy = st.builds(
    editormodel::Note,
)
editormodel::CoreModel_strategy = st.builds(
    editormodel::CoreModel,
)
NamedElementModel_strategy = st.builds(
    NamedElementModel,
)
editormodel::Diagram_strategy = st.builds(
    editormodel::Diagram,
    snapToGeometryEnabled=
        safe_text,
    gridEnabled=
        safe_text
)

@given(instance=VisualModel_strategy)
@settings(max_examples=50)
def test_visualmodel_instantiation(instance):
    assert isinstance(instance, VisualModel)

@given(instance=editormodel::NodeVisualModel_strategy)
@settings(max_examples=50)
def test_editormodel::nodevisualmodel_instantiation(instance):
    assert isinstance(instance, editormodel::NodeVisualModel)

@given(instance=editormodel::NodeVisualModel_strategy)
def test_editormodel::nodevisualmodel_rotation_type(instance):
    assert isinstance(instance.rotation, str)


@given(instance=editormodel::NodeVisualModel_strategy)
def test_editormodel::nodevisualmodel_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original

@given(instance=editormodel::EStringToEObjectMapEntry_strategy)
@settings(max_examples=50)
def test_editormodel::estringtoeobjectmapentry_instantiation(instance):
    assert isinstance(instance, editormodel::EStringToEObjectMapEntry)

@given(instance=editormodel::EStringToEObjectMapEntry_strategy)
def test_editormodel::estringtoeobjectmapentry_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=editormodel::EStringToEObjectMapEntry_strategy)
def test_editormodel::estringtoeobjectmapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=editormodel::ConnectionBendpoint_strategy)
@settings(max_examples=50)
def test_editormodel::connectionbendpoint_instantiation(instance):
    assert isinstance(instance, editormodel::ConnectionBendpoint)

@given(instance=editormodel::ConnectionBendpoint_strategy)
def test_editormodel::connectionbendpoint_weight_type(instance):
    assert isinstance(instance.weight, float)


@given(instance=editormodel::ConnectionBendpoint_strategy)
def test_editormodel::connectionbendpoint_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=editormodel::Adapter_strategy)
@settings(max_examples=50)
def test_editormodel::adapter_instantiation(instance):
    assert isinstance(instance, editormodel::Adapter)

@given(instance=editormodel::Color_strategy)
@settings(max_examples=50)
def test_editormodel::color_instantiation(instance):
    assert isinstance(instance, editormodel::Color)

@given(instance=editormodel::Color_strategy)
def test_editormodel::color_green_type(instance):
    assert isinstance(instance.green, int)


@given(instance=editormodel::Color_strategy)
def test_editormodel::color_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original

@given(instance=editormodel::Color_strategy)
def test_editormodel::color_blue_type(instance):
    assert isinstance(instance.blue, int)


@given(instance=editormodel::Color_strategy)
def test_editormodel::color_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original

@given(instance=editormodel::Color_strategy)
def test_editormodel::color_red_type(instance):
    assert isinstance(instance.red, int)


@given(instance=editormodel::Color_strategy)
def test_editormodel::color_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original

@given(instance=editormodel::Dimension_strategy)
@settings(max_examples=50)
def test_editormodel::dimension_instantiation(instance):
    assert isinstance(instance, editormodel::Dimension)

@given(instance=editormodel::Dimension_strategy)
def test_editormodel::dimension_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=editormodel::Dimension_strategy)
def test_editormodel::dimension_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=editormodel::Dimension_strategy)
def test_editormodel::dimension_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=editormodel::Dimension_strategy)
def test_editormodel::dimension_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=editormodel::Point_strategy)
@settings(max_examples=50)
def test_editormodel::point_instantiation(instance):
    assert isinstance(instance, editormodel::Point)

@given(instance=editormodel::Point_strategy)
def test_editormodel::point_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=editormodel::Point_strategy)
def test_editormodel::point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=editormodel::Point_strategy)
def test_editormodel::point_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=editormodel::Point_strategy)
def test_editormodel::point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=editormodel::EObject_strategy)
@settings(max_examples=50)
def test_editormodel::eobject_instantiation(instance):
    assert isinstance(instance, editormodel::EObject)

@given(instance=Adapter_strategy)
@settings(max_examples=50)
def test_adapter_instantiation(instance):
    assert isinstance(instance, Adapter)

@given(instance=NodeVisualModel_strategy)
@settings(max_examples=50)
def test_nodevisualmodel_instantiation(instance):
    assert isinstance(instance, NodeVisualModel)

@given(instance=editormodel::VisualDiagramJump_strategy)
@settings(max_examples=50)
def test_editormodel::visualdiagramjump_instantiation(instance):
    assert isinstance(instance, editormodel::VisualDiagramJump)

@given(instance=editormodel::VisualDiagramJump_strategy)
def test_editormodel::visualdiagramjump_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=editormodel::VisualDiagramJump_strategy)
def test_editormodel::visualdiagramjump_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=editormodel::ConnectionVisualModel_strategy)
@settings(max_examples=50)
def test_editormodel::connectionvisualmodel_instantiation(instance):
    assert isinstance(instance, editormodel::ConnectionVisualModel)

@given(instance=editormodel::ConnectionVisualModel_strategy)
def test_editormodel::connectionvisualmodel_sourceTerminal_type(instance):
    assert isinstance(instance.sourceTerminal, str)


@given(instance=editormodel::ConnectionVisualModel_strategy)
def test_editormodel::connectionvisualmodel_sourceTerminal_setter(instance):
    original = instance.sourceTerminal
    instance.sourceTerminal = original
    assert instance.sourceTerminal == original

@given(instance=editormodel::ConnectionVisualModel_strategy)
def test_editormodel::connectionvisualmodel_targetTerminal_type(instance):
    assert isinstance(instance.targetTerminal, str)


@given(instance=editormodel::ConnectionVisualModel_strategy)
def test_editormodel::connectionvisualmodel_targetTerminal_setter(instance):
    original = instance.targetTerminal
    instance.targetTerminal = original
    assert instance.targetTerminal == original

@given(instance=ExtensibleElement_strategy)
@settings(max_examples=50)
def test_extensibleelement_instantiation(instance):
    assert isinstance(instance, ExtensibleElement)

@given(instance=editormodel::FlabotFileModel_strategy)
@settings(max_examples=50)
def test_editormodel::flabotfilemodel_instantiation(instance):
    assert isinstance(instance, editormodel::FlabotFileModel)

@given(instance=editormodel::FlabotFileModel_strategy)
def test_editormodel::flabotfilemodel_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=editormodel::FlabotFileModel_strategy)
def test_editormodel::flabotfilemodel_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=editormodel::FlabotFileModel_strategy)
def test_editormodel::flabotfilemodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=editormodel::FlabotFileModel_strategy)
def test_editormodel::flabotfilemodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=editormodel::FlabotFileModel_strategy)
def test_editormodel::flabotfilemodel_provider_type(instance):
    assert isinstance(instance.provider, str)


@given(instance=editormodel::FlabotFileModel_strategy)
def test_editormodel::flabotfilemodel_provider_setter(instance):
    original = instance.provider
    instance.provider = original
    assert instance.provider == original

@given(instance=editormodel::FlabotFileModel_strategy)
def test_editormodel::flabotfilemodel_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=editormodel::FlabotFileModel_strategy)
def test_editormodel::flabotfilemodel_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=editormodel::Folder_strategy)
@settings(max_examples=50)
def test_editormodel::folder_instantiation(instance):
    assert isinstance(instance, editormodel::Folder)

@given(instance=editormodel::Folder_strategy)
def test_editormodel::folder_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=editormodel::Folder_strategy)
def test_editormodel::folder_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=editormodel::VisualModel_strategy)
@settings(max_examples=50)
def test_editormodel::visualmodel_instantiation(instance):
    assert isinstance(instance, editormodel::VisualModel)

@given(instance=editormodel::VisualModel_strategy)
def test_editormodel::visualmodel_lineStyle_type(instance):
    assert isinstance(instance.lineStyle, int)


@given(instance=editormodel::VisualModel_strategy)
def test_editormodel::visualmodel_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original

@given(instance=editormodel::VisualModel_strategy)
def test_editormodel::visualmodel_detailLevel_type(instance):
    assert isinstance(instance.detailLevel, int)


@given(instance=editormodel::VisualModel_strategy)
def test_editormodel::visualmodel_detailLevel_setter(instance):
    original = instance.detailLevel
    instance.detailLevel = original
    assert instance.detailLevel == original

@given(instance=editormodel::VisualModel_strategy)
def test_editormodel::visualmodel_lineWidth_type(instance):
    assert isinstance(instance.lineWidth, int)


@given(instance=editormodel::VisualModel_strategy)
def test_editormodel::visualmodel_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original

@given(instance=editormodel::Note_strategy)
@settings(max_examples=50)
def test_editormodel::note_instantiation(instance):
    assert isinstance(instance, editormodel::Note)

@given(instance=editormodel::CoreModel_strategy)
@settings(max_examples=50)
def test_editormodel::coremodel_instantiation(instance):
    assert isinstance(instance, editormodel::CoreModel)

@given(instance=NamedElementModel_strategy)
@settings(max_examples=50)
def test_namedelementmodel_instantiation(instance):
    assert isinstance(instance, NamedElementModel)

@given(instance=editormodel::Diagram_strategy)
@settings(max_examples=50)
def test_editormodel::diagram_instantiation(instance):
    assert isinstance(instance, editormodel::Diagram)

@given(instance=editormodel::Diagram_strategy)
def test_editormodel::diagram_snapToGeometryEnabled_type(instance):
    assert isinstance(instance.snapToGeometryEnabled, str)


@given(instance=editormodel::Diagram_strategy)
def test_editormodel::diagram_snapToGeometryEnabled_setter(instance):
    original = instance.snapToGeometryEnabled
    instance.snapToGeometryEnabled = original
    assert instance.snapToGeometryEnabled == original

@given(instance=editormodel::Diagram_strategy)
def test_editormodel::diagram_gridEnabled_type(instance):
    assert isinstance(instance.gridEnabled, str)


@given(instance=editormodel::Diagram_strategy)
def test_editormodel::diagram_gridEnabled_setter(instance):
    original = instance.gridEnabled
    instance.gridEnabled = original
    assert instance.gridEnabled == original
