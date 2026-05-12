import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    migrationmodeler_GaugeSection,
    NodeStyle,
    migrationmodeler_Ellipse,
    migrationmodeler_Lozenge,
    migrationmodeler_Square,
    migrationmodeler_GaugeCompositeStyle,
    migrationmodeler_Note,
    migrationmodeler_BundledImage,
    migrationmodeler_Dot,
    BasicLabelStyle,
    migrationmodeler_LabelStyle,
    ContainerStyle,
    migrationmodeler_WorkspaceImage,
    migrationmodeler_ShapeContainerStyle,
    migrationmodeler_FlatContainerStyle,
    LabelStyle,
    migrationmodeler_BorderedStyle,
    migrationmodeler_Representation,
    migrationmodeler_TestCase,
    BorderedStyle,
    migrationmodeler_BasicLabelStyle,
    migrationmodeler_Color,
    migrationmodeler_ContainerStyle,
    AbstractNodeRepresentation,
    migrationmodeler_NodeStyle,
    migrationmodeler_EdgeStyle,
    migrationmodeler_Point,
    AbstractRepresentation,
    migrationmodeler_AbstractNodeRepresentation,
    migrationmodeler_Layout,
    migrationmodeler_AbstractRepresentation,
    migrationmodeler_ContainerRepresentation,
    migrationmodeler_BorderedRepresentation,
    migrationmodeler_NodeRepresentation,
    AbstractNode,
    migrationmodeler_Bordered,
    GraphicalElement,
    migrationmodeler_AbstractNode,
    migrationmodeler_GraphicalElement,
    migrationmodeler_Layer,
    migrationmodeler_Filter,
    migrationmodeler_Edge,
    migrationmodeler_Node,
    migrationmodeler_Container,
    Representation,
    migrationmodeler_Diagram,
    migrationmodeler_EdgeRepresentation,
    AlignmentKind,
    RoutingStyle,
    ContainerShape,
    LabelAlignment,
    LabelPosition,
    FontFormat,
    BackgroundStyle,
    BundledImageShape,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_migrationmodeler_gaugesection_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_GaugeSection)


def test_migrationmodeler_gaugesection_constructor_exists():
    assert callable(migrationmodeler_GaugeSection.__init__)


def test_migrationmodeler_gaugesection_constructor_args():
    sig = inspect.signature(migrationmodeler_GaugeSection.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"
    assert "label" in params, "Missing parameter 'label'"

def test_migrationmodeler_gaugesection_has_value():
    assert hasattr(migrationmodeler_GaugeSection, "value")
    descriptor = None
    for klass in migrationmodeler_GaugeSection.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_migrationmodeler_gaugesection_has_min():
    assert hasattr(migrationmodeler_GaugeSection, "min")
    descriptor = None
    for klass in migrationmodeler_GaugeSection.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_migrationmodeler_gaugesection_has_max():
    assert hasattr(migrationmodeler_GaugeSection, "max")
    descriptor = None
    for klass in migrationmodeler_GaugeSection.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_migrationmodeler_gaugesection_has_label():
    assert hasattr(migrationmodeler_GaugeSection, "label")
    descriptor = None
    for klass in migrationmodeler_GaugeSection.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_nodestyle_is_not_abstract():
    assert not inspect.isabstract(NodeStyle)


def test_nodestyle_constructor_exists():
    assert callable(NodeStyle.__init__)


def test_nodestyle_constructor_args():
    sig = inspect.signature(NodeStyle.__init__)
    params = list(sig.parameters.keys())



def test_migrationmodeler_ellipse_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Ellipse)


def test_migrationmodeler_ellipse_constructor_exists():
    assert callable(migrationmodeler_Ellipse.__init__)


def test_migrationmodeler_ellipse_constructor_args():
    sig = inspect.signature(migrationmodeler_Ellipse.__init__)
    params = list(sig.parameters.keys())
    assert "verticalDiameter" in params, "Missing parameter 'verticalDiameter'"
    assert "horizontalDiameter" in params, "Missing parameter 'horizontalDiameter'"

def test_migrationmodeler_ellipse_has_verticalDiameter():
    assert hasattr(migrationmodeler_Ellipse, "verticalDiameter")
    descriptor = None
    for klass in migrationmodeler_Ellipse.__mro__:
        if "verticalDiameter" in klass.__dict__:
            descriptor = klass.__dict__["verticalDiameter"]
            break
    assert isinstance(descriptor, property)

def test_migrationmodeler_ellipse_has_horizontalDiameter():
    assert hasattr(migrationmodeler_Ellipse, "horizontalDiameter")
    descriptor = None
    for klass in migrationmodeler_Ellipse.__mro__:
        if "horizontalDiameter" in klass.__dict__:
            descriptor = klass.__dict__["horizontalDiameter"]
            break
    assert isinstance(descriptor, property)



def test_migrationmodeler_lozenge_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Lozenge)


def test_migrationmodeler_lozenge_constructor_exists():
    assert callable(migrationmodeler_Lozenge.__init__)


def test_migrationmodeler_lozenge_constructor_args():
    sig = inspect.signature(migrationmodeler_Lozenge.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_migrationmodeler_lozenge_has_height():
    assert hasattr(migrationmodeler_Lozenge, "height")
    descriptor = None
    for klass in migrationmodeler_Lozenge.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_migrationmodeler_lozenge_has_width():
    assert hasattr(migrationmodeler_Lozenge, "width")
    descriptor = None
    for klass in migrationmodeler_Lozenge.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_migrationmodeler_square_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Square)


def test_migrationmodeler_square_constructor_exists():
    assert callable(migrationmodeler_Square.__init__)


def test_migrationmodeler_square_constructor_args():
    sig = inspect.signature(migrationmodeler_Square.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_migrationmodeler_square_has_width():
    assert hasattr(migrationmodeler_Square, "width")
    descriptor = None
    for klass in migrationmodeler_Square.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_migrationmodeler_square_has_height():
    assert hasattr(migrationmodeler_Square, "height")
    descriptor = None
    for klass in migrationmodeler_Square.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_migrationmodeler_gaugecompositestyle_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_GaugeCompositeStyle)


def test_migrationmodeler_gaugecompositestyle_constructor_exists():
    assert callable(migrationmodeler_GaugeCompositeStyle.__init__)


def test_migrationmodeler_gaugecompositestyle_constructor_args():
    sig = inspect.signature(migrationmodeler_GaugeCompositeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"

def test_migrationmodeler_gaugecompositestyle_has_alignment():
    assert hasattr(migrationmodeler_GaugeCompositeStyle, "alignment")
    descriptor = None
    for klass in migrationmodeler_GaugeCompositeStyle.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)



def test_migrationmodeler_note_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Note)


def test_migrationmodeler_note_constructor_exists():
    assert callable(migrationmodeler_Note.__init__)


def test_migrationmodeler_note_constructor_args():
    sig = inspect.signature(migrationmodeler_Note.__init__)
    params = list(sig.parameters.keys())



def test_migrationmodeler_bundledimage_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_BundledImage)


def test_migrationmodeler_bundledimage_constructor_exists():
    assert callable(migrationmodeler_BundledImage.__init__)


def test_migrationmodeler_bundledimage_constructor_args():
    sig = inspect.signature(migrationmodeler_BundledImage.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"

def test_migrationmodeler_bundledimage_has_shape():
    assert hasattr(migrationmodeler_BundledImage, "shape")
    descriptor = None
    for klass in migrationmodeler_BundledImage.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_migrationmodeler_dot_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Dot)


def test_migrationmodeler_dot_constructor_exists():
    assert callable(migrationmodeler_Dot.__init__)


def test_migrationmodeler_dot_constructor_args():
    sig = inspect.signature(migrationmodeler_Dot.__init__)
    params = list(sig.parameters.keys())



def test_basiclabelstyle_is_not_abstract():
    assert not inspect.isabstract(BasicLabelStyle)


def test_basiclabelstyle_constructor_exists():
    assert callable(BasicLabelStyle.__init__)


def test_basiclabelstyle_constructor_args():
    sig = inspect.signature(BasicLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_migrationmodeler_labelstyle_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_LabelStyle)


def test_migrationmodeler_labelstyle_constructor_exists():
    assert callable(migrationmodeler_LabelStyle.__init__)


def test_migrationmodeler_labelstyle_constructor_args():
    sig = inspect.signature(migrationmodeler_LabelStyle.__init__)
    params = list(sig.parameters.keys())
    assert "labelAlignment" in params, "Missing parameter 'labelAlignment'"

def test_migrationmodeler_labelstyle_has_labelAlignment():
    assert hasattr(migrationmodeler_LabelStyle, "labelAlignment")
    descriptor = None
    for klass in migrationmodeler_LabelStyle.__mro__:
        if "labelAlignment" in klass.__dict__:
            descriptor = klass.__dict__["labelAlignment"]
            break
    assert isinstance(descriptor, property)



def test_containerstyle_is_not_abstract():
    assert not inspect.isabstract(ContainerStyle)


def test_containerstyle_constructor_exists():
    assert callable(ContainerStyle.__init__)


def test_containerstyle_constructor_args():
    sig = inspect.signature(ContainerStyle.__init__)
    params = list(sig.parameters.keys())



def test_migrationmodeler_workspaceimage_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_WorkspaceImage)


def test_migrationmodeler_workspaceimage_constructor_exists():
    assert callable(migrationmodeler_WorkspaceImage.__init__)


def test_migrationmodeler_workspaceimage_constructor_args():
    sig = inspect.signature(migrationmodeler_WorkspaceImage.__init__)
    params = list(sig.parameters.keys())
    assert "workspacePath" in params, "Missing parameter 'workspacePath'"

def test_migrationmodeler_workspaceimage_has_workspacePath():
    assert hasattr(migrationmodeler_WorkspaceImage, "workspacePath")
    descriptor = None
    for klass in migrationmodeler_WorkspaceImage.__mro__:
        if "workspacePath" in klass.__dict__:
            descriptor = klass.__dict__["workspacePath"]
            break
    assert isinstance(descriptor, property)



def test_migrationmodeler_shapecontainerstyle_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_ShapeContainerStyle)


def test_migrationmodeler_shapecontainerstyle_constructor_exists():
    assert callable(migrationmodeler_ShapeContainerStyle.__init__)


def test_migrationmodeler_shapecontainerstyle_constructor_args():
    sig = inspect.signature(migrationmodeler_ShapeContainerStyle.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"

def test_migrationmodeler_shapecontainerstyle_has_shape():
    assert hasattr(migrationmodeler_ShapeContainerStyle, "shape")
    descriptor = None
    for klass in migrationmodeler_ShapeContainerStyle.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_migrationmodeler_flatcontainerstyle_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_FlatContainerStyle)


def test_migrationmodeler_flatcontainerstyle_constructor_exists():
    assert callable(migrationmodeler_FlatContainerStyle.__init__)


def test_migrationmodeler_flatcontainerstyle_constructor_args():
    sig = inspect.signature(migrationmodeler_FlatContainerStyle.__init__)
    params = list(sig.parameters.keys())
    assert "backgroundStyle" in params, "Missing parameter 'backgroundStyle'"

def test_migrationmodeler_flatcontainerstyle_has_backgroundStyle():
    assert hasattr(migrationmodeler_FlatContainerStyle, "backgroundStyle")
    descriptor = None
    for klass in migrationmodeler_FlatContainerStyle.__mro__:
        if "backgroundStyle" in klass.__dict__:
            descriptor = klass.__dict__["backgroundStyle"]
            break
    assert isinstance(descriptor, property)



def test_labelstyle_is_not_abstract():
    assert not inspect.isabstract(LabelStyle)


def test_labelstyle_constructor_exists():
    assert callable(LabelStyle.__init__)


def test_labelstyle_constructor_args():
    sig = inspect.signature(LabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_migrationmodeler_borderedstyle_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_BorderedStyle)


def test_migrationmodeler_borderedstyle_constructor_exists():
    assert callable(migrationmodeler_BorderedStyle.__init__)


def test_migrationmodeler_borderedstyle_constructor_args():
    sig = inspect.signature(migrationmodeler_BorderedStyle.__init__)
    params = list(sig.parameters.keys())
    assert "borderSize" in params, "Missing parameter 'borderSize'"

def test_migrationmodeler_borderedstyle_has_borderSize():
    assert hasattr(migrationmodeler_BorderedStyle, "borderSize")
    descriptor = None
    for klass in migrationmodeler_BorderedStyle.__mro__:
        if "borderSize" in klass.__dict__:
            descriptor = klass.__dict__["borderSize"]
            break
    assert isinstance(descriptor, property)



def test_migrationmodeler_representation_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Representation)


def test_migrationmodeler_representation_constructor_exists():
    assert callable(migrationmodeler_Representation.__init__)


def test_migrationmodeler_representation_constructor_args():
    sig = inspect.signature(migrationmodeler_Representation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_migrationmodeler_representation_has_name():
    assert hasattr(migrationmodeler_Representation, "name")
    descriptor = None
    for klass in migrationmodeler_Representation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_migrationmodeler_testcase_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_TestCase)


def test_migrationmodeler_testcase_constructor_exists():
    assert callable(migrationmodeler_TestCase.__init__)


def test_migrationmodeler_testcase_constructor_args():
    sig = inspect.signature(migrationmodeler_TestCase.__init__)
    params = list(sig.parameters.keys())



def test_borderedstyle_is_not_abstract():
    assert not inspect.isabstract(BorderedStyle)


def test_borderedstyle_constructor_exists():
    assert callable(BorderedStyle.__init__)


def test_borderedstyle_constructor_args():
    sig = inspect.signature(BorderedStyle.__init__)
    params = list(sig.parameters.keys())



def test_migrationmodeler_basiclabelstyle_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_BasicLabelStyle)


def test_migrationmodeler_basiclabelstyle_constructor_exists():
    assert callable(migrationmodeler_BasicLabelStyle.__init__)


def test_migrationmodeler_basiclabelstyle_constructor_args():
    sig = inspect.signature(migrationmodeler_BasicLabelStyle.__init__)
    params = list(sig.parameters.keys())
    assert "labelFormat" in params, "Missing parameter 'labelFormat'"
    assert "labelSize" in params, "Missing parameter 'labelSize'"
    assert "showIcon" in params, "Missing parameter 'showIcon'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"

def test_migrationmodeler_basiclabelstyle_has_labelFormat():
    assert hasattr(migrationmodeler_BasicLabelStyle, "labelFormat")
    descriptor = None
    for klass in migrationmodeler_BasicLabelStyle.__mro__:
        if "labelFormat" in klass.__dict__:
            descriptor = klass.__dict__["labelFormat"]
            break
    assert isinstance(descriptor, property)

def test_migrationmodeler_basiclabelstyle_has_labelSize():
    assert hasattr(migrationmodeler_BasicLabelStyle, "labelSize")
    descriptor = None
    for klass in migrationmodeler_BasicLabelStyle.__mro__:
        if "labelSize" in klass.__dict__:
            descriptor = klass.__dict__["labelSize"]
            break
    assert isinstance(descriptor, property)

def test_migrationmodeler_basiclabelstyle_has_showIcon():
    assert hasattr(migrationmodeler_BasicLabelStyle, "showIcon")
    descriptor = None
    for klass in migrationmodeler_BasicLabelStyle.__mro__:
        if "showIcon" in klass.__dict__:
            descriptor = klass.__dict__["showIcon"]
            break
    assert isinstance(descriptor, property)

def test_migrationmodeler_basiclabelstyle_has_iconPath():
    assert hasattr(migrationmodeler_BasicLabelStyle, "iconPath")
    descriptor = None
    for klass in migrationmodeler_BasicLabelStyle.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)



def test_migrationmodeler_color_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Color)


def test_migrationmodeler_color_constructor_exists():
    assert callable(migrationmodeler_Color.__init__)


def test_migrationmodeler_color_constructor_args():
    sig = inspect.signature(migrationmodeler_Color.__init__)
    params = list(sig.parameters.keys())
    assert "blue" in params, "Missing parameter 'blue'"
    assert "red" in params, "Missing parameter 'red'"
    assert "green" in params, "Missing parameter 'green'"

def test_migrationmodeler_color_has_blue():
    assert hasattr(migrationmodeler_Color, "blue")
    descriptor = None
    for klass in migrationmodeler_Color.__mro__:
        if "blue" in klass.__dict__:
            descriptor = klass.__dict__["blue"]
            break
    assert isinstance(descriptor, property)

def test_migrationmodeler_color_has_red():
    assert hasattr(migrationmodeler_Color, "red")
    descriptor = None
    for klass in migrationmodeler_Color.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
            break
    assert isinstance(descriptor, property)

def test_migrationmodeler_color_has_green():
    assert hasattr(migrationmodeler_Color, "green")
    descriptor = None
    for klass in migrationmodeler_Color.__mro__:
        if "green" in klass.__dict__:
            descriptor = klass.__dict__["green"]
            break
    assert isinstance(descriptor, property)



def test_migrationmodeler_containerstyle_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_ContainerStyle)


def test_migrationmodeler_containerstyle_constructor_exists():
    assert callable(migrationmodeler_ContainerStyle.__init__)


def test_migrationmodeler_containerstyle_constructor_args():
    sig = inspect.signature(migrationmodeler_ContainerStyle.__init__)
    params = list(sig.parameters.keys())



def test_abstractnoderepresentation_is_not_abstract():
    assert not inspect.isabstract(AbstractNodeRepresentation)


def test_abstractnoderepresentation_constructor_exists():
    assert callable(AbstractNodeRepresentation.__init__)


def test_abstractnoderepresentation_constructor_args():
    sig = inspect.signature(AbstractNodeRepresentation.__init__)
    params = list(sig.parameters.keys())



def test_migrationmodeler_nodestyle_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_NodeStyle)


def test_migrationmodeler_nodestyle_constructor_exists():
    assert callable(migrationmodeler_NodeStyle.__init__)


def test_migrationmodeler_nodestyle_constructor_args():
    sig = inspect.signature(migrationmodeler_NodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "labelPosition" in params, "Missing parameter 'labelPosition'"
    assert "hideLabelByDefault" in params, "Missing parameter 'hideLabelByDefault'"

def test_migrationmodeler_nodestyle_has_labelPosition():
    assert hasattr(migrationmodeler_NodeStyle, "labelPosition")
    descriptor = None
    for klass in migrationmodeler_NodeStyle.__mro__:
        if "labelPosition" in klass.__dict__:
            descriptor = klass.__dict__["labelPosition"]
            break
    assert isinstance(descriptor, property)

def test_migrationmodeler_nodestyle_has_hideLabelByDefault():
    assert hasattr(migrationmodeler_NodeStyle, "hideLabelByDefault")
    descriptor = None
    for klass in migrationmodeler_NodeStyle.__mro__:
        if "hideLabelByDefault" in klass.__dict__:
            descriptor = klass.__dict__["hideLabelByDefault"]
            break
    assert isinstance(descriptor, property)



def test_migrationmodeler_edgestyle_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_EdgeStyle)


def test_migrationmodeler_edgestyle_constructor_exists():
    assert callable(migrationmodeler_EdgeStyle.__init__)


def test_migrationmodeler_edgestyle_constructor_args():
    sig = inspect.signature(migrationmodeler_EdgeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "routingStyle" in params, "Missing parameter 'routingStyle'"

def test_migrationmodeler_edgestyle_has_routingStyle():
    assert hasattr(migrationmodeler_EdgeStyle, "routingStyle")
    descriptor = None
    for klass in migrationmodeler_EdgeStyle.__mro__:
        if "routingStyle" in klass.__dict__:
            descriptor = klass.__dict__["routingStyle"]
            break
    assert isinstance(descriptor, property)



def test_migrationmodeler_point_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Point)


def test_migrationmodeler_point_constructor_exists():
    assert callable(migrationmodeler_Point.__init__)


def test_migrationmodeler_point_constructor_args():
    sig = inspect.signature(migrationmodeler_Point.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_migrationmodeler_point_has_y():
    assert hasattr(migrationmodeler_Point, "y")
    descriptor = None
    for klass in migrationmodeler_Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_migrationmodeler_point_has_x():
    assert hasattr(migrationmodeler_Point, "x")
    descriptor = None
    for klass in migrationmodeler_Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_abstractrepresentation_is_not_abstract():
    assert not inspect.isabstract(AbstractRepresentation)


def test_abstractrepresentation_constructor_exists():
    assert callable(AbstractRepresentation.__init__)


def test_abstractrepresentation_constructor_args():
    sig = inspect.signature(AbstractRepresentation.__init__)
    params = list(sig.parameters.keys())



def test_migrationmodeler_abstractnoderepresentation_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_AbstractNodeRepresentation)


def test_migrationmodeler_abstractnoderepresentation_constructor_exists():
    assert callable(migrationmodeler_AbstractNodeRepresentation.__init__)


def test_migrationmodeler_abstractnoderepresentation_constructor_args():
    sig = inspect.signature(migrationmodeler_AbstractNodeRepresentation.__init__)
    params = list(sig.parameters.keys())



def test_migrationmodeler_layout_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Layout)


def test_migrationmodeler_layout_constructor_exists():
    assert callable(migrationmodeler_Layout.__init__)


def test_migrationmodeler_layout_constructor_args():
    sig = inspect.signature(migrationmodeler_Layout.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"
    assert "y" in params, "Missing parameter 'y'"

def test_migrationmodeler_layout_has_x():
    assert hasattr(migrationmodeler_Layout, "x")
    descriptor = None
    for klass in migrationmodeler_Layout.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_migrationmodeler_layout_has_height():
    assert hasattr(migrationmodeler_Layout, "height")
    descriptor = None
    for klass in migrationmodeler_Layout.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_migrationmodeler_layout_has_width():
    assert hasattr(migrationmodeler_Layout, "width")
    descriptor = None
    for klass in migrationmodeler_Layout.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_migrationmodeler_layout_has_y():
    assert hasattr(migrationmodeler_Layout, "y")
    descriptor = None
    for klass in migrationmodeler_Layout.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_migrationmodeler_abstractrepresentation_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_AbstractRepresentation)


def test_migrationmodeler_abstractrepresentation_constructor_exists():
    assert callable(migrationmodeler_AbstractRepresentation.__init__)


def test_migrationmodeler_abstractrepresentation_constructor_args():
    sig = inspect.signature(migrationmodeler_AbstractRepresentation.__init__)
    params = list(sig.parameters.keys())
    assert "mappingId" in params, "Missing parameter 'mappingId'"
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "displayed" in params, "Missing parameter 'displayed'"
    assert "pinned" in params, "Missing parameter 'pinned'"

def test_migrationmodeler_abstractrepresentation_has_mappingId():
    assert hasattr(migrationmodeler_AbstractRepresentation, "mappingId")
    descriptor = None
    for klass in migrationmodeler_AbstractRepresentation.__mro__:
        if "mappingId" in klass.__dict__:
            descriptor = klass.__dict__["mappingId"]
            break
    assert isinstance(descriptor, property)

def test_migrationmodeler_abstractrepresentation_has_hidden():
    assert hasattr(migrationmodeler_AbstractRepresentation, "hidden")
    descriptor = None
    for klass in migrationmodeler_AbstractRepresentation.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)

def test_migrationmodeler_abstractrepresentation_has_displayed():
    assert hasattr(migrationmodeler_AbstractRepresentation, "displayed")
    descriptor = None
    for klass in migrationmodeler_AbstractRepresentation.__mro__:
        if "displayed" in klass.__dict__:
            descriptor = klass.__dict__["displayed"]
            break
    assert isinstance(descriptor, property)

def test_migrationmodeler_abstractrepresentation_has_pinned():
    assert hasattr(migrationmodeler_AbstractRepresentation, "pinned")
    descriptor = None
    for klass in migrationmodeler_AbstractRepresentation.__mro__:
        if "pinned" in klass.__dict__:
            descriptor = klass.__dict__["pinned"]
            break
    assert isinstance(descriptor, property)



def test_migrationmodeler_containerrepresentation_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_ContainerRepresentation)


def test_migrationmodeler_containerrepresentation_constructor_exists():
    assert callable(migrationmodeler_ContainerRepresentation.__init__)


def test_migrationmodeler_containerrepresentation_constructor_args():
    sig = inspect.signature(migrationmodeler_ContainerRepresentation.__init__)
    params = list(sig.parameters.keys())
    assert "autoSized" in params, "Missing parameter 'autoSized'"

def test_migrationmodeler_containerrepresentation_has_autoSized():
    assert hasattr(migrationmodeler_ContainerRepresentation, "autoSized")
    descriptor = None
    for klass in migrationmodeler_ContainerRepresentation.__mro__:
        if "autoSized" in klass.__dict__:
            descriptor = klass.__dict__["autoSized"]
            break
    assert isinstance(descriptor, property)



def test_migrationmodeler_borderedrepresentation_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_BorderedRepresentation)


def test_migrationmodeler_borderedrepresentation_constructor_exists():
    assert callable(migrationmodeler_BorderedRepresentation.__init__)


def test_migrationmodeler_borderedrepresentation_constructor_args():
    sig = inspect.signature(migrationmodeler_BorderedRepresentation.__init__)
    params = list(sig.parameters.keys())



def test_migrationmodeler_noderepresentation_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_NodeRepresentation)


def test_migrationmodeler_noderepresentation_constructor_exists():
    assert callable(migrationmodeler_NodeRepresentation.__init__)


def test_migrationmodeler_noderepresentation_constructor_args():
    sig = inspect.signature(migrationmodeler_NodeRepresentation.__init__)
    params = list(sig.parameters.keys())



def test_abstractnode_is_not_abstract():
    assert not inspect.isabstract(AbstractNode)


def test_abstractnode_constructor_exists():
    assert callable(AbstractNode.__init__)


def test_abstractnode_constructor_args():
    sig = inspect.signature(AbstractNode.__init__)
    params = list(sig.parameters.keys())



def test_migrationmodeler_bordered_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Bordered)


def test_migrationmodeler_bordered_constructor_exists():
    assert callable(migrationmodeler_Bordered.__init__)


def test_migrationmodeler_bordered_constructor_args():
    sig = inspect.signature(migrationmodeler_Bordered.__init__)
    params = list(sig.parameters.keys())



def test_graphicalelement_is_not_abstract():
    assert not inspect.isabstract(GraphicalElement)


def test_graphicalelement_constructor_exists():
    assert callable(GraphicalElement.__init__)


def test_graphicalelement_constructor_args():
    sig = inspect.signature(GraphicalElement.__init__)
    params = list(sig.parameters.keys())



def test_migrationmodeler_abstractnode_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_AbstractNode)


def test_migrationmodeler_abstractnode_constructor_exists():
    assert callable(migrationmodeler_AbstractNode.__init__)


def test_migrationmodeler_abstractnode_constructor_args():
    sig = inspect.signature(migrationmodeler_AbstractNode.__init__)
    params = list(sig.parameters.keys())



def test_migrationmodeler_graphicalelement_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_GraphicalElement)


def test_migrationmodeler_graphicalelement_constructor_exists():
    assert callable(migrationmodeler_GraphicalElement.__init__)


def test_migrationmodeler_graphicalelement_constructor_args():
    sig = inspect.signature(migrationmodeler_GraphicalElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_migrationmodeler_graphicalelement_has_id():
    assert hasattr(migrationmodeler_GraphicalElement, "id")
    descriptor = None
    for klass in migrationmodeler_GraphicalElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_migrationmodeler_layer_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Layer)


def test_migrationmodeler_layer_constructor_exists():
    assert callable(migrationmodeler_Layer.__init__)


def test_migrationmodeler_layer_constructor_args():
    sig = inspect.signature(migrationmodeler_Layer.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "activated" in params, "Missing parameter 'activated'"

def test_migrationmodeler_layer_has_id():
    assert hasattr(migrationmodeler_Layer, "id")
    descriptor = None
    for klass in migrationmodeler_Layer.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_migrationmodeler_layer_has_activated():
    assert hasattr(migrationmodeler_Layer, "activated")
    descriptor = None
    for klass in migrationmodeler_Layer.__mro__:
        if "activated" in klass.__dict__:
            descriptor = klass.__dict__["activated"]
            break
    assert isinstance(descriptor, property)



def test_migrationmodeler_filter_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Filter)


def test_migrationmodeler_filter_constructor_exists():
    assert callable(migrationmodeler_Filter.__init__)


def test_migrationmodeler_filter_constructor_args():
    sig = inspect.signature(migrationmodeler_Filter.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "activated" in params, "Missing parameter 'activated'"

def test_migrationmodeler_filter_has_id():
    assert hasattr(migrationmodeler_Filter, "id")
    descriptor = None
    for klass in migrationmodeler_Filter.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_migrationmodeler_filter_has_activated():
    assert hasattr(migrationmodeler_Filter, "activated")
    descriptor = None
    for klass in migrationmodeler_Filter.__mro__:
        if "activated" in klass.__dict__:
            descriptor = klass.__dict__["activated"]
            break
    assert isinstance(descriptor, property)



def test_migrationmodeler_edge_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Edge)


def test_migrationmodeler_edge_constructor_exists():
    assert callable(migrationmodeler_Edge.__init__)


def test_migrationmodeler_edge_constructor_args():
    sig = inspect.signature(migrationmodeler_Edge.__init__)
    params = list(sig.parameters.keys())



def test_migrationmodeler_node_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Node)


def test_migrationmodeler_node_constructor_exists():
    assert callable(migrationmodeler_Node.__init__)


def test_migrationmodeler_node_constructor_args():
    sig = inspect.signature(migrationmodeler_Node.__init__)
    params = list(sig.parameters.keys())



def test_migrationmodeler_container_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Container)


def test_migrationmodeler_container_constructor_exists():
    assert callable(migrationmodeler_Container.__init__)


def test_migrationmodeler_container_constructor_args():
    sig = inspect.signature(migrationmodeler_Container.__init__)
    params = list(sig.parameters.keys())



def test_representation_is_not_abstract():
    assert not inspect.isabstract(Representation)


def test_representation_constructor_exists():
    assert callable(Representation.__init__)


def test_representation_constructor_args():
    sig = inspect.signature(Representation.__init__)
    params = list(sig.parameters.keys())



def test_migrationmodeler_diagram_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Diagram)


def test_migrationmodeler_diagram_constructor_exists():
    assert callable(migrationmodeler_Diagram.__init__)


def test_migrationmodeler_diagram_constructor_args():
    sig = inspect.signature(migrationmodeler_Diagram.__init__)
    params = list(sig.parameters.keys())



def test_migrationmodeler_edgerepresentation_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_EdgeRepresentation)


def test_migrationmodeler_edgerepresentation_constructor_exists():
    assert callable(migrationmodeler_EdgeRepresentation.__init__)


def test_migrationmodeler_edgerepresentation_constructor_args():
    sig = inspect.signature(migrationmodeler_EdgeRepresentation.__init__)
    params = list(sig.parameters.keys())

def test_alignmentkind_exists():
    # Check that the Enumeration exists
    assert AlignmentKind is not None

def test_alignmentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AlignmentKind]
    expected_literals = [
        "SQUARE",
        "VERTICAL",
        "HORIZONTAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AlignmentKind"

def test_routingstyle_exists():
    # Check that the Enumeration exists
    assert RoutingStyle is not None

def test_routingstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RoutingStyle]
    expected_literals = [
        "Tree",
        "Manhattan",
        "Straight",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RoutingStyle"

def test_containershape_exists():
    # Check that the Enumeration exists
    assert ContainerShape is not None

def test_containershape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContainerShape]
    expected_literals = [
        "parallelogram",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContainerShape"

def test_labelalignment_exists():
    # Check that the Enumeration exists
    assert LabelAlignment is not None

def test_labelalignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LabelAlignment]
    expected_literals = [
        "LEFT",
        "CENTER",
        "RIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LabelAlignment"

def test_labelposition_exists():
    # Check that the Enumeration exists
    assert LabelPosition is not None

def test_labelposition_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LabelPosition]
    expected_literals = [
        "border",
        "node",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LabelPosition"

def test_fontformat_exists():
    # Check that the Enumeration exists
    assert FontFormat is not None

def test_fontformat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontFormat]
    expected_literals = [
        "italic",
        "bold_italic",
        "normal",
        "bold",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontFormat"

def test_backgroundstyle_exists():
    # Check that the Enumeration exists
    assert BackgroundStyle is not None

def test_backgroundstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BackgroundStyle]
    expected_literals = [
        "GradientLeftToRight",
        "GradientTopToBottom",
        "Liquid",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BackgroundStyle"

def test_bundledimageshape_exists():
    # Check that the Enumeration exists
    assert BundledImageShape is not None

def test_bundledimageshape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BundledImageShape]
    expected_literals = [
        "stroke",
        "triangle",
        "square",
        "dot",
        "ring",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BundledImageShape"


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
migrationmodeler_GaugeSection_strategy = st.builds(
    migrationmodeler_GaugeSection,
    value=
        safe_text,
    min=
        safe_text,
    max=
        safe_text,
    label=
        safe_text
)
NodeStyle_strategy = st.builds(
    NodeStyle,
)
migrationmodeler_Ellipse_strategy = st.builds(
    migrationmodeler_Ellipse,
    verticalDiameter=
        safe_text,
    horizontalDiameter=
        safe_text
)
migrationmodeler_Lozenge_strategy = st.builds(
    migrationmodeler_Lozenge,
    height=
        safe_text,
    width=
        safe_text
)
migrationmodeler_Square_strategy = st.builds(
    migrationmodeler_Square,
    width=
        safe_text,
    height=
        safe_text
)
migrationmodeler_GaugeCompositeStyle_strategy = st.builds(
    migrationmodeler_GaugeCompositeStyle,
    alignment=
        safe_text
)
migrationmodeler_Note_strategy = st.builds(
    migrationmodeler_Note,
)
migrationmodeler_BundledImage_strategy = st.builds(
    migrationmodeler_BundledImage,
    shape=
        safe_text
)
migrationmodeler_Dot_strategy = st.builds(
    migrationmodeler_Dot,
)
BasicLabelStyle_strategy = st.builds(
    BasicLabelStyle,
)
migrationmodeler_LabelStyle_strategy = st.builds(
    migrationmodeler_LabelStyle,
    labelAlignment=
        safe_text
)
ContainerStyle_strategy = st.builds(
    ContainerStyle,
)
migrationmodeler_WorkspaceImage_strategy = st.builds(
    migrationmodeler_WorkspaceImage,
    workspacePath=
        safe_text
)
migrationmodeler_ShapeContainerStyle_strategy = st.builds(
    migrationmodeler_ShapeContainerStyle,
    shape=
        safe_text
)
migrationmodeler_FlatContainerStyle_strategy = st.builds(
    migrationmodeler_FlatContainerStyle,
    backgroundStyle=
        safe_text
)
LabelStyle_strategy = st.builds(
    LabelStyle,
)
migrationmodeler_BorderedStyle_strategy = st.builds(
    migrationmodeler_BorderedStyle,
    borderSize=
        st.integers()
)
migrationmodeler_Representation_strategy = st.builds(
    migrationmodeler_Representation,
    name=
        safe_text
)
migrationmodeler_TestCase_strategy = st.builds(
    migrationmodeler_TestCase,
)
BorderedStyle_strategy = st.builds(
    BorderedStyle,
)
migrationmodeler_BasicLabelStyle_strategy = st.builds(
    migrationmodeler_BasicLabelStyle,
    labelFormat=
        safe_text,
    labelSize=
        st.integers(),
    showIcon=
        st.booleans(),
    iconPath=
        safe_text
)
migrationmodeler_Color_strategy = st.builds(
    migrationmodeler_Color,
    blue=
        st.integers(),
    red=
        st.integers(),
    green=
        st.integers()
)
migrationmodeler_ContainerStyle_strategy = st.builds(
    migrationmodeler_ContainerStyle,
)
AbstractNodeRepresentation_strategy = st.builds(
    AbstractNodeRepresentation,
)
migrationmodeler_NodeStyle_strategy = st.builds(
    migrationmodeler_NodeStyle,
    labelPosition=
        safe_text,
    hideLabelByDefault=
        st.booleans()
)
migrationmodeler_EdgeStyle_strategy = st.builds(
    migrationmodeler_EdgeStyle,
    routingStyle=
        safe_text
)
migrationmodeler_Point_strategy = st.builds(
    migrationmodeler_Point,
    y=
        st.integers(),
    x=
        st.integers()
)
AbstractRepresentation_strategy = st.builds(
    AbstractRepresentation,
)
migrationmodeler_AbstractNodeRepresentation_strategy = st.builds(
    migrationmodeler_AbstractNodeRepresentation,
)
migrationmodeler_Layout_strategy = st.builds(
    migrationmodeler_Layout,
    x=
        st.integers(),
    height=
        st.integers(),
    width=
        st.integers(),
    y=
        st.integers()
)
migrationmodeler_AbstractRepresentation_strategy = st.builds(
    migrationmodeler_AbstractRepresentation,
    mappingId=
        safe_text,
    hidden=
        st.booleans(),
    displayed=
        st.booleans(),
    pinned=
        st.booleans()
)
migrationmodeler_ContainerRepresentation_strategy = st.builds(
    migrationmodeler_ContainerRepresentation,
    autoSized=
        st.booleans()
)
migrationmodeler_BorderedRepresentation_strategy = st.builds(
    migrationmodeler_BorderedRepresentation,
)
migrationmodeler_NodeRepresentation_strategy = st.builds(
    migrationmodeler_NodeRepresentation,
)
AbstractNode_strategy = st.builds(
    AbstractNode,
)
migrationmodeler_Bordered_strategy = st.builds(
    migrationmodeler_Bordered,
)
GraphicalElement_strategy = st.builds(
    GraphicalElement,
)
migrationmodeler_AbstractNode_strategy = st.builds(
    migrationmodeler_AbstractNode,
)
migrationmodeler_GraphicalElement_strategy = st.builds(
    migrationmodeler_GraphicalElement,
    id=
        safe_text
)
migrationmodeler_Layer_strategy = st.builds(
    migrationmodeler_Layer,
    id=
        safe_text,
    activated=
        st.booleans()
)
migrationmodeler_Filter_strategy = st.builds(
    migrationmodeler_Filter,
    id=
        safe_text,
    activated=
        st.booleans()
)
migrationmodeler_Edge_strategy = st.builds(
    migrationmodeler_Edge,
)
migrationmodeler_Node_strategy = st.builds(
    migrationmodeler_Node,
)
migrationmodeler_Container_strategy = st.builds(
    migrationmodeler_Container,
)
Representation_strategy = st.builds(
    Representation,
)
migrationmodeler_Diagram_strategy = st.builds(
    migrationmodeler_Diagram,
)
migrationmodeler_EdgeRepresentation_strategy = st.builds(
    migrationmodeler_EdgeRepresentation,
)

@given(instance=migrationmodeler_GaugeSection_strategy)
@settings(max_examples=50)
def test_migrationmodeler_gaugesection_instantiation(instance):
    assert isinstance(instance, migrationmodeler_GaugeSection)



@given(instance=migrationmodeler_GaugeSection_strategy)
def test_migrationmodeler_gaugesection_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=migrationmodeler_GaugeSection_strategy)
def test_migrationmodeler_gaugesection_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=migrationmodeler_GaugeSection_strategy)
def test_migrationmodeler_gaugesection_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=migrationmodeler_GaugeSection_strategy)
def test_migrationmodeler_gaugesection_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=NodeStyle_strategy)
@settings(max_examples=50)
def test_nodestyle_instantiation(instance):
    assert isinstance(instance, NodeStyle)

@given(instance=migrationmodeler_Ellipse_strategy)
@settings(max_examples=50)
def test_migrationmodeler_ellipse_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Ellipse)



@given(instance=migrationmodeler_Ellipse_strategy)
def test_migrationmodeler_ellipse_verticalDiameter_setter(instance):
    original = instance.verticalDiameter
    instance.verticalDiameter = original
    assert instance.verticalDiameter == original



@given(instance=migrationmodeler_Ellipse_strategy)
def test_migrationmodeler_ellipse_horizontalDiameter_setter(instance):
    original = instance.horizontalDiameter
    instance.horizontalDiameter = original
    assert instance.horizontalDiameter == original

@given(instance=migrationmodeler_Lozenge_strategy)
@settings(max_examples=50)
def test_migrationmodeler_lozenge_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Lozenge)



@given(instance=migrationmodeler_Lozenge_strategy)
def test_migrationmodeler_lozenge_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=migrationmodeler_Lozenge_strategy)
def test_migrationmodeler_lozenge_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=migrationmodeler_Square_strategy)
@settings(max_examples=50)
def test_migrationmodeler_square_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Square)



@given(instance=migrationmodeler_Square_strategy)
def test_migrationmodeler_square_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=migrationmodeler_Square_strategy)
def test_migrationmodeler_square_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=migrationmodeler_GaugeCompositeStyle_strategy)
@settings(max_examples=50)
def test_migrationmodeler_gaugecompositestyle_instantiation(instance):
    assert isinstance(instance, migrationmodeler_GaugeCompositeStyle)



@given(instance=migrationmodeler_GaugeCompositeStyle_strategy)
def test_migrationmodeler_gaugecompositestyle_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=migrationmodeler_Note_strategy)
@settings(max_examples=50)
def test_migrationmodeler_note_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Note)

@given(instance=migrationmodeler_BundledImage_strategy)
@settings(max_examples=50)
def test_migrationmodeler_bundledimage_instantiation(instance):
    assert isinstance(instance, migrationmodeler_BundledImage)



@given(instance=migrationmodeler_BundledImage_strategy)
def test_migrationmodeler_bundledimage_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=migrationmodeler_Dot_strategy)
@settings(max_examples=50)
def test_migrationmodeler_dot_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Dot)

@given(instance=BasicLabelStyle_strategy)
@settings(max_examples=50)
def test_basiclabelstyle_instantiation(instance):
    assert isinstance(instance, BasicLabelStyle)

@given(instance=migrationmodeler_LabelStyle_strategy)
@settings(max_examples=50)
def test_migrationmodeler_labelstyle_instantiation(instance):
    assert isinstance(instance, migrationmodeler_LabelStyle)



@given(instance=migrationmodeler_LabelStyle_strategy)
def test_migrationmodeler_labelstyle_labelAlignment_setter(instance):
    original = instance.labelAlignment
    instance.labelAlignment = original
    assert instance.labelAlignment == original

@given(instance=ContainerStyle_strategy)
@settings(max_examples=50)
def test_containerstyle_instantiation(instance):
    assert isinstance(instance, ContainerStyle)

@given(instance=migrationmodeler_WorkspaceImage_strategy)
@settings(max_examples=50)
def test_migrationmodeler_workspaceimage_instantiation(instance):
    assert isinstance(instance, migrationmodeler_WorkspaceImage)



@given(instance=migrationmodeler_WorkspaceImage_strategy)
def test_migrationmodeler_workspaceimage_workspacePath_setter(instance):
    original = instance.workspacePath
    instance.workspacePath = original
    assert instance.workspacePath == original

@given(instance=migrationmodeler_ShapeContainerStyle_strategy)
@settings(max_examples=50)
def test_migrationmodeler_shapecontainerstyle_instantiation(instance):
    assert isinstance(instance, migrationmodeler_ShapeContainerStyle)



@given(instance=migrationmodeler_ShapeContainerStyle_strategy)
def test_migrationmodeler_shapecontainerstyle_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=migrationmodeler_FlatContainerStyle_strategy)
@settings(max_examples=50)
def test_migrationmodeler_flatcontainerstyle_instantiation(instance):
    assert isinstance(instance, migrationmodeler_FlatContainerStyle)



@given(instance=migrationmodeler_FlatContainerStyle_strategy)
def test_migrationmodeler_flatcontainerstyle_backgroundStyle_setter(instance):
    original = instance.backgroundStyle
    instance.backgroundStyle = original
    assert instance.backgroundStyle == original

@given(instance=LabelStyle_strategy)
@settings(max_examples=50)
def test_labelstyle_instantiation(instance):
    assert isinstance(instance, LabelStyle)

@given(instance=migrationmodeler_BorderedStyle_strategy)
@settings(max_examples=50)
def test_migrationmodeler_borderedstyle_instantiation(instance):
    assert isinstance(instance, migrationmodeler_BorderedStyle)



@given(instance=migrationmodeler_BorderedStyle_strategy)
def test_migrationmodeler_borderedstyle_borderSize_setter(instance):
    original = instance.borderSize
    instance.borderSize = original
    assert instance.borderSize == original

@given(instance=migrationmodeler_Representation_strategy)
@settings(max_examples=50)
def test_migrationmodeler_representation_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Representation)



@given(instance=migrationmodeler_Representation_strategy)
def test_migrationmodeler_representation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=migrationmodeler_TestCase_strategy)
@settings(max_examples=50)
def test_migrationmodeler_testcase_instantiation(instance):
    assert isinstance(instance, migrationmodeler_TestCase)

@given(instance=BorderedStyle_strategy)
@settings(max_examples=50)
def test_borderedstyle_instantiation(instance):
    assert isinstance(instance, BorderedStyle)

@given(instance=migrationmodeler_BasicLabelStyle_strategy)
@settings(max_examples=50)
def test_migrationmodeler_basiclabelstyle_instantiation(instance):
    assert isinstance(instance, migrationmodeler_BasicLabelStyle)



@given(instance=migrationmodeler_BasicLabelStyle_strategy)
def test_migrationmodeler_basiclabelstyle_labelFormat_setter(instance):
    original = instance.labelFormat
    instance.labelFormat = original
    assert instance.labelFormat == original



@given(instance=migrationmodeler_BasicLabelStyle_strategy)
def test_migrationmodeler_basiclabelstyle_labelSize_setter(instance):
    original = instance.labelSize
    instance.labelSize = original
    assert instance.labelSize == original



@given(instance=migrationmodeler_BasicLabelStyle_strategy)
def test_migrationmodeler_basiclabelstyle_showIcon_setter(instance):
    original = instance.showIcon
    instance.showIcon = original
    assert instance.showIcon == original



@given(instance=migrationmodeler_BasicLabelStyle_strategy)
def test_migrationmodeler_basiclabelstyle_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=migrationmodeler_Color_strategy)
@settings(max_examples=50)
def test_migrationmodeler_color_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Color)



@given(instance=migrationmodeler_Color_strategy)
def test_migrationmodeler_color_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original



@given(instance=migrationmodeler_Color_strategy)
def test_migrationmodeler_color_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original



@given(instance=migrationmodeler_Color_strategy)
def test_migrationmodeler_color_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original

@given(instance=migrationmodeler_ContainerStyle_strategy)
@settings(max_examples=50)
def test_migrationmodeler_containerstyle_instantiation(instance):
    assert isinstance(instance, migrationmodeler_ContainerStyle)

@given(instance=AbstractNodeRepresentation_strategy)
@settings(max_examples=50)
def test_abstractnoderepresentation_instantiation(instance):
    assert isinstance(instance, AbstractNodeRepresentation)

@given(instance=migrationmodeler_NodeStyle_strategy)
@settings(max_examples=50)
def test_migrationmodeler_nodestyle_instantiation(instance):
    assert isinstance(instance, migrationmodeler_NodeStyle)



@given(instance=migrationmodeler_NodeStyle_strategy)
def test_migrationmodeler_nodestyle_labelPosition_setter(instance):
    original = instance.labelPosition
    instance.labelPosition = original
    assert instance.labelPosition == original



@given(instance=migrationmodeler_NodeStyle_strategy)
def test_migrationmodeler_nodestyle_hideLabelByDefault_setter(instance):
    original = instance.hideLabelByDefault
    instance.hideLabelByDefault = original
    assert instance.hideLabelByDefault == original

@given(instance=migrationmodeler_EdgeStyle_strategy)
@settings(max_examples=50)
def test_migrationmodeler_edgestyle_instantiation(instance):
    assert isinstance(instance, migrationmodeler_EdgeStyle)



@given(instance=migrationmodeler_EdgeStyle_strategy)
def test_migrationmodeler_edgestyle_routingStyle_setter(instance):
    original = instance.routingStyle
    instance.routingStyle = original
    assert instance.routingStyle == original

@given(instance=migrationmodeler_Point_strategy)
@settings(max_examples=50)
def test_migrationmodeler_point_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Point)



@given(instance=migrationmodeler_Point_strategy)
def test_migrationmodeler_point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=migrationmodeler_Point_strategy)
def test_migrationmodeler_point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=AbstractRepresentation_strategy)
@settings(max_examples=50)
def test_abstractrepresentation_instantiation(instance):
    assert isinstance(instance, AbstractRepresentation)

@given(instance=migrationmodeler_AbstractNodeRepresentation_strategy)
@settings(max_examples=50)
def test_migrationmodeler_abstractnoderepresentation_instantiation(instance):
    assert isinstance(instance, migrationmodeler_AbstractNodeRepresentation)

@given(instance=migrationmodeler_Layout_strategy)
@settings(max_examples=50)
def test_migrationmodeler_layout_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Layout)



@given(instance=migrationmodeler_Layout_strategy)
def test_migrationmodeler_layout_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=migrationmodeler_Layout_strategy)
def test_migrationmodeler_layout_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=migrationmodeler_Layout_strategy)
def test_migrationmodeler_layout_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=migrationmodeler_Layout_strategy)
def test_migrationmodeler_layout_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=migrationmodeler_AbstractRepresentation_strategy)
@settings(max_examples=50)
def test_migrationmodeler_abstractrepresentation_instantiation(instance):
    assert isinstance(instance, migrationmodeler_AbstractRepresentation)



@given(instance=migrationmodeler_AbstractRepresentation_strategy)
def test_migrationmodeler_abstractrepresentation_mappingId_setter(instance):
    original = instance.mappingId
    instance.mappingId = original
    assert instance.mappingId == original



@given(instance=migrationmodeler_AbstractRepresentation_strategy)
def test_migrationmodeler_abstractrepresentation_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original



@given(instance=migrationmodeler_AbstractRepresentation_strategy)
def test_migrationmodeler_abstractrepresentation_displayed_setter(instance):
    original = instance.displayed
    instance.displayed = original
    assert instance.displayed == original



@given(instance=migrationmodeler_AbstractRepresentation_strategy)
def test_migrationmodeler_abstractrepresentation_pinned_setter(instance):
    original = instance.pinned
    instance.pinned = original
    assert instance.pinned == original

@given(instance=migrationmodeler_ContainerRepresentation_strategy)
@settings(max_examples=50)
def test_migrationmodeler_containerrepresentation_instantiation(instance):
    assert isinstance(instance, migrationmodeler_ContainerRepresentation)



@given(instance=migrationmodeler_ContainerRepresentation_strategy)
def test_migrationmodeler_containerrepresentation_autoSized_setter(instance):
    original = instance.autoSized
    instance.autoSized = original
    assert instance.autoSized == original

@given(instance=migrationmodeler_BorderedRepresentation_strategy)
@settings(max_examples=50)
def test_migrationmodeler_borderedrepresentation_instantiation(instance):
    assert isinstance(instance, migrationmodeler_BorderedRepresentation)

@given(instance=migrationmodeler_NodeRepresentation_strategy)
@settings(max_examples=50)
def test_migrationmodeler_noderepresentation_instantiation(instance):
    assert isinstance(instance, migrationmodeler_NodeRepresentation)

@given(instance=AbstractNode_strategy)
@settings(max_examples=50)
def test_abstractnode_instantiation(instance):
    assert isinstance(instance, AbstractNode)

@given(instance=migrationmodeler_Bordered_strategy)
@settings(max_examples=50)
def test_migrationmodeler_bordered_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Bordered)

@given(instance=GraphicalElement_strategy)
@settings(max_examples=50)
def test_graphicalelement_instantiation(instance):
    assert isinstance(instance, GraphicalElement)

@given(instance=migrationmodeler_AbstractNode_strategy)
@settings(max_examples=50)
def test_migrationmodeler_abstractnode_instantiation(instance):
    assert isinstance(instance, migrationmodeler_AbstractNode)

@given(instance=migrationmodeler_GraphicalElement_strategy)
@settings(max_examples=50)
def test_migrationmodeler_graphicalelement_instantiation(instance):
    assert isinstance(instance, migrationmodeler_GraphicalElement)



@given(instance=migrationmodeler_GraphicalElement_strategy)
def test_migrationmodeler_graphicalelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=migrationmodeler_Layer_strategy)
@settings(max_examples=50)
def test_migrationmodeler_layer_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Layer)



@given(instance=migrationmodeler_Layer_strategy)
def test_migrationmodeler_layer_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=migrationmodeler_Layer_strategy)
def test_migrationmodeler_layer_activated_setter(instance):
    original = instance.activated
    instance.activated = original
    assert instance.activated == original

@given(instance=migrationmodeler_Filter_strategy)
@settings(max_examples=50)
def test_migrationmodeler_filter_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Filter)



@given(instance=migrationmodeler_Filter_strategy)
def test_migrationmodeler_filter_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=migrationmodeler_Filter_strategy)
def test_migrationmodeler_filter_activated_setter(instance):
    original = instance.activated
    instance.activated = original
    assert instance.activated == original

@given(instance=migrationmodeler_Edge_strategy)
@settings(max_examples=50)
def test_migrationmodeler_edge_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Edge)

@given(instance=migrationmodeler_Node_strategy)
@settings(max_examples=50)
def test_migrationmodeler_node_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Node)

@given(instance=migrationmodeler_Container_strategy)
@settings(max_examples=50)
def test_migrationmodeler_container_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Container)

@given(instance=Representation_strategy)
@settings(max_examples=50)
def test_representation_instantiation(instance):
    assert isinstance(instance, Representation)

@given(instance=migrationmodeler_Diagram_strategy)
@settings(max_examples=50)
def test_migrationmodeler_diagram_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Diagram)

@given(instance=migrationmodeler_EdgeRepresentation_strategy)
@settings(max_examples=50)
def test_migrationmodeler_edgerepresentation_instantiation(instance):
    assert isinstance(instance, migrationmodeler_EdgeRepresentation)
