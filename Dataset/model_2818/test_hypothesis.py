import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Value,
    model_BooleanValue,
    model_EnumValue,
    model_StringValue,
    model_DoubleValue,
    model_IntValue,
    model_CustomColor,
    Feature,
    model_Anchor,
    ConnectableElement,
    model_Rectangle,
    model_Label,
    model_Image,
    model_Invisible,
    model_Custom,
    model_Color,
    model_Contains,
    model_EClass,
    model_ImportStatement,
    model_CustomFigure,
    model_DiagramElement,
    model_Colors,
    model_Decorator,
    model_EReference,
    FeatureContainer,
    model_Arrow,
    model_ConnectableElement,
    DiagramElement,
    model_Link,
    model_Node,
    model_Value,
    model_EAttribute,
    model_FeatureContainer,
    model_FeatureConditional,
    model_Feature,
    model_Diagram,
    model_MetaModel,
    model_XDiagram,
    model_LineWidth,
    model_Position,
    model_Point,
    model_Size,
    model_Transparency,
    model_LineStyle,
    model_TextAlign,
    model_FontProperties,
    model_TextPart,
    model_TextValue,
    model_Visible,
    model_Layout,
    model_Corner,
    model_Line,
    model_Triangle,
    model_Polyline,
    model_Ellipse,
    model_Rhombus,
    model_ColorFeature,
    AnchorDirection,
    Operator,
    BooleanLiteral,
    DefaultColor,
    TextAlignValue,
    LineType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_model_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(model_BooleanValue)


def test_model_booleanvalue_constructor_exists():
    assert callable(model_BooleanValue.__init__)


def test_model_booleanvalue_constructor_args():
    sig = inspect.signature(model_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model_booleanvalue_has_value():
    assert hasattr(model_BooleanValue, "value")
    descriptor = None
    for klass in model_BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model_enumvalue_is_not_abstract():
    assert not inspect.isabstract(model_EnumValue)


def test_model_enumvalue_constructor_exists():
    assert callable(model_EnumValue.__init__)


def test_model_enumvalue_constructor_args():
    sig = inspect.signature(model_EnumValue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_enumvalue_has_name():
    assert hasattr(model_EnumValue, "name")
    descriptor = None
    for klass in model_EnumValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_stringvalue_is_not_abstract():
    assert not inspect.isabstract(model_StringValue)


def test_model_stringvalue_constructor_exists():
    assert callable(model_StringValue.__init__)


def test_model_stringvalue_constructor_args():
    sig = inspect.signature(model_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "null" in params, "Missing parameter 'null'"
    assert "value" in params, "Missing parameter 'value'"

def test_model_stringvalue_has_null():
    assert hasattr(model_StringValue, "null")
    descriptor = None
    for klass in model_StringValue.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)

def test_model_stringvalue_has_value():
    assert hasattr(model_StringValue, "value")
    descriptor = None
    for klass in model_StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model_doublevalue_is_not_abstract():
    assert not inspect.isabstract(model_DoubleValue)


def test_model_doublevalue_constructor_exists():
    assert callable(model_DoubleValue.__init__)


def test_model_doublevalue_constructor_args():
    sig = inspect.signature(model_DoubleValue.__init__)
    params = list(sig.parameters.keys())
    assert "valueInt" in params, "Missing parameter 'valueInt'"
    assert "valueDecimal" in params, "Missing parameter 'valueDecimal'"

def test_model_doublevalue_has_valueInt():
    assert hasattr(model_DoubleValue, "valueInt")
    descriptor = None
    for klass in model_DoubleValue.__mro__:
        if "valueInt" in klass.__dict__:
            descriptor = klass.__dict__["valueInt"]
            break
    assert isinstance(descriptor, property)

def test_model_doublevalue_has_valueDecimal():
    assert hasattr(model_DoubleValue, "valueDecimal")
    descriptor = None
    for klass in model_DoubleValue.__mro__:
        if "valueDecimal" in klass.__dict__:
            descriptor = klass.__dict__["valueDecimal"]
            break
    assert isinstance(descriptor, property)



def test_model_intvalue_is_not_abstract():
    assert not inspect.isabstract(model_IntValue)


def test_model_intvalue_constructor_exists():
    assert callable(model_IntValue.__init__)


def test_model_intvalue_constructor_args():
    sig = inspect.signature(model_IntValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model_intvalue_has_value():
    assert hasattr(model_IntValue, "value")
    descriptor = None
    for klass in model_IntValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model_customcolor_is_not_abstract():
    assert not inspect.isabstract(model_CustomColor)


def test_model_customcolor_constructor_exists():
    assert callable(model_CustomColor.__init__)


def test_model_customcolor_constructor_args():
    sig = inspect.signature(model_CustomColor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "G" in params, "Missing parameter 'G'"
    assert "B" in params, "Missing parameter 'B'"
    assert "R" in params, "Missing parameter 'R'"

def test_model_customcolor_has_name():
    assert hasattr(model_CustomColor, "name")
    descriptor = None
    for klass in model_CustomColor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_customcolor_has_G():
    assert hasattr(model_CustomColor, "G")
    descriptor = None
    for klass in model_CustomColor.__mro__:
        if "G" in klass.__dict__:
            descriptor = klass.__dict__["G"]
            break
    assert isinstance(descriptor, property)

def test_model_customcolor_has_B():
    assert hasattr(model_CustomColor, "B")
    descriptor = None
    for klass in model_CustomColor.__mro__:
        if "B" in klass.__dict__:
            descriptor = klass.__dict__["B"]
            break
    assert isinstance(descriptor, property)

def test_model_customcolor_has_R():
    assert hasattr(model_CustomColor, "R")
    descriptor = None
    for klass in model_CustomColor.__mro__:
        if "R" in klass.__dict__:
            descriptor = klass.__dict__["R"]
            break
    assert isinstance(descriptor, property)



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_model_anchor_is_not_abstract():
    assert not inspect.isabstract(model_Anchor)


def test_model_anchor_constructor_exists():
    assert callable(model_Anchor.__init__)


def test_model_anchor_constructor_args():
    sig = inspect.signature(model_Anchor.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "max" in params, "Missing parameter 'max'"

def test_model_anchor_has_direction():
    assert hasattr(model_Anchor, "direction")
    descriptor = None
    for klass in model_Anchor.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_model_anchor_has_max():
    assert hasattr(model_Anchor, "max")
    descriptor = None
    for klass in model_Anchor.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_connectableelement_is_not_abstract():
    assert not inspect.isabstract(ConnectableElement)


def test_connectableelement_constructor_exists():
    assert callable(ConnectableElement.__init__)


def test_connectableelement_constructor_args():
    sig = inspect.signature(ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_model_rectangle_is_not_abstract():
    assert not inspect.isabstract(model_Rectangle)


def test_model_rectangle_constructor_exists():
    assert callable(model_Rectangle.__init__)


def test_model_rectangle_constructor_args():
    sig = inspect.signature(model_Rectangle.__init__)
    params = list(sig.parameters.keys())
    assert "rectangle" in params, "Missing parameter 'rectangle'"
    assert "square" in params, "Missing parameter 'square'"

def test_model_rectangle_has_rectangle():
    assert hasattr(model_Rectangle, "rectangle")
    descriptor = None
    for klass in model_Rectangle.__mro__:
        if "rectangle" in klass.__dict__:
            descriptor = klass.__dict__["rectangle"]
            break
    assert isinstance(descriptor, property)

def test_model_rectangle_has_square():
    assert hasattr(model_Rectangle, "square")
    descriptor = None
    for klass in model_Rectangle.__mro__:
        if "square" in klass.__dict__:
            descriptor = klass.__dict__["square"]
            break
    assert isinstance(descriptor, property)



def test_model_label_is_not_abstract():
    assert not inspect.isabstract(model_Label)


def test_model_label_constructor_exists():
    assert callable(model_Label.__init__)


def test_model_label_constructor_args():
    sig = inspect.signature(model_Label.__init__)
    params = list(sig.parameters.keys())



def test_model_image_is_not_abstract():
    assert not inspect.isabstract(model_Image)


def test_model_image_constructor_exists():
    assert callable(model_Image.__init__)


def test_model_image_constructor_args():
    sig = inspect.signature(model_Image.__init__)
    params = list(sig.parameters.keys())
    assert "imageId" in params, "Missing parameter 'imageId'"

def test_model_image_has_imageId():
    assert hasattr(model_Image, "imageId")
    descriptor = None
    for klass in model_Image.__mro__:
        if "imageId" in klass.__dict__:
            descriptor = klass.__dict__["imageId"]
            break
    assert isinstance(descriptor, property)



def test_model_invisible_is_not_abstract():
    assert not inspect.isabstract(model_Invisible)


def test_model_invisible_constructor_exists():
    assert callable(model_Invisible.__init__)


def test_model_invisible_constructor_args():
    sig = inspect.signature(model_Invisible.__init__)
    params = list(sig.parameters.keys())



def test_model_custom_is_not_abstract():
    assert not inspect.isabstract(model_Custom)


def test_model_custom_constructor_exists():
    assert callable(model_Custom.__init__)


def test_model_custom_constructor_args():
    sig = inspect.signature(model_Custom.__init__)
    params = list(sig.parameters.keys())



def test_model_color_is_not_abstract():
    assert not inspect.isabstract(model_Color)


def test_model_color_constructor_exists():
    assert callable(model_Color.__init__)


def test_model_color_constructor_args():
    sig = inspect.signature(model_Color.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_model_color_has_default():
    assert hasattr(model_Color, "default")
    descriptor = None
    for klass in model_Color.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_model_contains_is_not_abstract():
    assert not inspect.isabstract(model_Contains)


def test_model_contains_constructor_exists():
    assert callable(model_Contains.__init__)


def test_model_contains_constructor_args():
    sig = inspect.signature(model_Contains.__init__)
    params = list(sig.parameters.keys())



def test_model_eclass_is_not_abstract():
    assert not inspect.isabstract(model_EClass)


def test_model_eclass_constructor_exists():
    assert callable(model_EClass.__init__)


def test_model_eclass_constructor_args():
    sig = inspect.signature(model_EClass.__init__)
    params = list(sig.parameters.keys())



def test_model_importstatement_is_not_abstract():
    assert not inspect.isabstract(model_ImportStatement)


def test_model_importstatement_constructor_exists():
    assert callable(model_ImportStatement.__init__)


def test_model_importstatement_constructor_args():
    sig = inspect.signature(model_ImportStatement.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_model_importstatement_has_importedNamespace():
    assert hasattr(model_ImportStatement, "importedNamespace")
    descriptor = None
    for klass in model_ImportStatement.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_model_customfigure_is_not_abstract():
    assert not inspect.isabstract(model_CustomFigure)


def test_model_customfigure_constructor_exists():
    assert callable(model_CustomFigure.__init__)


def test_model_customfigure_constructor_args():
    sig = inspect.signature(model_CustomFigure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_customfigure_has_name():
    assert hasattr(model_CustomFigure, "name")
    descriptor = None
    for klass in model_CustomFigure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_diagramelement_is_not_abstract():
    assert not inspect.isabstract(model_DiagramElement)


def test_model_diagramelement_constructor_exists():
    assert callable(model_DiagramElement.__init__)


def test_model_diagramelement_constructor_args():
    sig = inspect.signature(model_DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_model_colors_is_not_abstract():
    assert not inspect.isabstract(model_Colors)


def test_model_colors_constructor_exists():
    assert callable(model_Colors.__init__)


def test_model_colors_constructor_args():
    sig = inspect.signature(model_Colors.__init__)
    params = list(sig.parameters.keys())



def test_model_decorator_is_not_abstract():
    assert not inspect.isabstract(model_Decorator)


def test_model_decorator_constructor_exists():
    assert callable(model_Decorator.__init__)


def test_model_decorator_constructor_args():
    sig = inspect.signature(model_Decorator.__init__)
    params = list(sig.parameters.keys())



def test_model_ereference_is_not_abstract():
    assert not inspect.isabstract(model_EReference)


def test_model_ereference_constructor_exists():
    assert callable(model_EReference.__init__)


def test_model_ereference_constructor_args():
    sig = inspect.signature(model_EReference.__init__)
    params = list(sig.parameters.keys())



def test_featurecontainer_is_not_abstract():
    assert not inspect.isabstract(FeatureContainer)


def test_featurecontainer_constructor_exists():
    assert callable(FeatureContainer.__init__)


def test_featurecontainer_constructor_args():
    sig = inspect.signature(FeatureContainer.__init__)
    params = list(sig.parameters.keys())



def test_model_arrow_is_not_abstract():
    assert not inspect.isabstract(model_Arrow)


def test_model_arrow_constructor_exists():
    assert callable(model_Arrow.__init__)


def test_model_arrow_constructor_args():
    sig = inspect.signature(model_Arrow.__init__)
    params = list(sig.parameters.keys())



def test_model_connectableelement_is_not_abstract():
    assert not inspect.isabstract(model_ConnectableElement)


def test_model_connectableelement_constructor_exists():
    assert callable(model_ConnectableElement.__init__)


def test_model_connectableelement_constructor_args():
    sig = inspect.signature(model_ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_diagramelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElement)


def test_diagramelement_constructor_exists():
    assert callable(DiagramElement.__init__)


def test_diagramelement_constructor_args():
    sig = inspect.signature(DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_model_link_is_not_abstract():
    assert not inspect.isabstract(model_Link)


def test_model_link_constructor_exists():
    assert callable(model_Link.__init__)


def test_model_link_constructor_args():
    sig = inspect.signature(model_Link.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"
    assert "complex" in params, "Missing parameter 'complex'"

def test_model_link_has_reference():
    assert hasattr(model_Link, "reference")
    descriptor = None
    for klass in model_Link.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_model_link_has_complex():
    assert hasattr(model_Link, "complex")
    descriptor = None
    for klass in model_Link.__mro__:
        if "complex" in klass.__dict__:
            descriptor = klass.__dict__["complex"]
            break
    assert isinstance(descriptor, property)



def test_model_node_is_not_abstract():
    assert not inspect.isabstract(model_Node)


def test_model_node_constructor_exists():
    assert callable(model_Node.__init__)


def test_model_node_constructor_args():
    sig = inspect.signature(model_Node.__init__)
    params = list(sig.parameters.keys())



def test_model_value_is_not_abstract():
    assert not inspect.isabstract(model_Value)


def test_model_value_constructor_exists():
    assert callable(model_Value.__init__)


def test_model_value_constructor_args():
    sig = inspect.signature(model_Value.__init__)
    params = list(sig.parameters.keys())



def test_model_eattribute_is_not_abstract():
    assert not inspect.isabstract(model_EAttribute)


def test_model_eattribute_constructor_exists():
    assert callable(model_EAttribute.__init__)


def test_model_eattribute_constructor_args():
    sig = inspect.signature(model_EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_model_featurecontainer_is_not_abstract():
    assert not inspect.isabstract(model_FeatureContainer)


def test_model_featurecontainer_constructor_exists():
    assert callable(model_FeatureContainer.__init__)


def test_model_featurecontainer_constructor_args():
    sig = inspect.signature(model_FeatureContainer.__init__)
    params = list(sig.parameters.keys())



def test_model_featureconditional_is_not_abstract():
    assert not inspect.isabstract(model_FeatureConditional)


def test_model_featureconditional_constructor_exists():
    assert callable(model_FeatureConditional.__init__)


def test_model_featureconditional_constructor_args():
    sig = inspect.signature(model_FeatureConditional.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_model_featureconditional_has_operator():
    assert hasattr(model_FeatureConditional, "operator")
    descriptor = None
    for klass in model_FeatureConditional.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_model_feature_is_not_abstract():
    assert not inspect.isabstract(model_Feature)


def test_model_feature_constructor_exists():
    assert callable(model_Feature.__init__)


def test_model_feature_constructor_args():
    sig = inspect.signature(model_Feature.__init__)
    params = list(sig.parameters.keys())



def test_model_diagram_is_not_abstract():
    assert not inspect.isabstract(model_Diagram)


def test_model_diagram_constructor_exists():
    assert callable(model_Diagram.__init__)


def test_model_diagram_constructor_args():
    sig = inspect.signature(model_Diagram.__init__)
    params = list(sig.parameters.keys())



def test_model_metamodel_is_not_abstract():
    assert not inspect.isabstract(model_MetaModel)


def test_model_metamodel_constructor_exists():
    assert callable(model_MetaModel.__init__)


def test_model_metamodel_constructor_args():
    sig = inspect.signature(model_MetaModel.__init__)
    params = list(sig.parameters.keys())
    assert "plugin" in params, "Missing parameter 'plugin'"
    assert "ecorePath" in params, "Missing parameter 'ecorePath'"

def test_model_metamodel_has_plugin():
    assert hasattr(model_MetaModel, "plugin")
    descriptor = None
    for klass in model_MetaModel.__mro__:
        if "plugin" in klass.__dict__:
            descriptor = klass.__dict__["plugin"]
            break
    assert isinstance(descriptor, property)

def test_model_metamodel_has_ecorePath():
    assert hasattr(model_MetaModel, "ecorePath")
    descriptor = None
    for klass in model_MetaModel.__mro__:
        if "ecorePath" in klass.__dict__:
            descriptor = klass.__dict__["ecorePath"]
            break
    assert isinstance(descriptor, property)



def test_model_xdiagram_is_not_abstract():
    assert not inspect.isabstract(model_XDiagram)


def test_model_xdiagram_constructor_exists():
    assert callable(model_XDiagram.__init__)


def test_model_xdiagram_constructor_args():
    sig = inspect.signature(model_XDiagram.__init__)
    params = list(sig.parameters.keys())



def test_model_linewidth_is_not_abstract():
    assert not inspect.isabstract(model_LineWidth)


def test_model_linewidth_constructor_exists():
    assert callable(model_LineWidth.__init__)


def test_model_linewidth_constructor_args():
    sig = inspect.signature(model_LineWidth.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"

def test_model_linewidth_has_width():
    assert hasattr(model_LineWidth, "width")
    descriptor = None
    for klass in model_LineWidth.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_model_position_is_not_abstract():
    assert not inspect.isabstract(model_Position)


def test_model_position_constructor_exists():
    assert callable(model_Position.__init__)


def test_model_position_constructor_args():
    sig = inspect.signature(model_Position.__init__)
    params = list(sig.parameters.keys())
    assert "xRelative" in params, "Missing parameter 'xRelative'"
    assert "yRelative" in params, "Missing parameter 'yRelative'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_model_position_has_xRelative():
    assert hasattr(model_Position, "xRelative")
    descriptor = None
    for klass in model_Position.__mro__:
        if "xRelative" in klass.__dict__:
            descriptor = klass.__dict__["xRelative"]
            break
    assert isinstance(descriptor, property)

def test_model_position_has_yRelative():
    assert hasattr(model_Position, "yRelative")
    descriptor = None
    for klass in model_Position.__mro__:
        if "yRelative" in klass.__dict__:
            descriptor = klass.__dict__["yRelative"]
            break
    assert isinstance(descriptor, property)

def test_model_position_has_y():
    assert hasattr(model_Position, "y")
    descriptor = None
    for klass in model_Position.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_model_position_has_x():
    assert hasattr(model_Position, "x")
    descriptor = None
    for klass in model_Position.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_model_point_is_not_abstract():
    assert not inspect.isabstract(model_Point)


def test_model_point_constructor_exists():
    assert callable(model_Point.__init__)


def test_model_point_constructor_args():
    sig = inspect.signature(model_Point.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_model_point_has_y():
    assert hasattr(model_Point, "y")
    descriptor = None
    for klass in model_Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_model_point_has_x():
    assert hasattr(model_Point, "x")
    descriptor = None
    for klass in model_Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_model_size_is_not_abstract():
    assert not inspect.isabstract(model_Size)


def test_model_size_constructor_exists():
    assert callable(model_Size.__init__)


def test_model_size_constructor_args():
    sig = inspect.signature(model_Size.__init__)
    params = list(sig.parameters.keys())
    assert "widthRelative" in params, "Missing parameter 'widthRelative'"
    assert "heightRelative" in params, "Missing parameter 'heightRelative'"
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"
    assert "resizable" in params, "Missing parameter 'resizable'"

def test_model_size_has_widthRelative():
    assert hasattr(model_Size, "widthRelative")
    descriptor = None
    for klass in model_Size.__mro__:
        if "widthRelative" in klass.__dict__:
            descriptor = klass.__dict__["widthRelative"]
            break
    assert isinstance(descriptor, property)

def test_model_size_has_heightRelative():
    assert hasattr(model_Size, "heightRelative")
    descriptor = None
    for klass in model_Size.__mro__:
        if "heightRelative" in klass.__dict__:
            descriptor = klass.__dict__["heightRelative"]
            break
    assert isinstance(descriptor, property)

def test_model_size_has_width():
    assert hasattr(model_Size, "width")
    descriptor = None
    for klass in model_Size.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_model_size_has_height():
    assert hasattr(model_Size, "height")
    descriptor = None
    for klass in model_Size.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_model_size_has_resizable():
    assert hasattr(model_Size, "resizable")
    descriptor = None
    for klass in model_Size.__mro__:
        if "resizable" in klass.__dict__:
            descriptor = klass.__dict__["resizable"]
            break
    assert isinstance(descriptor, property)



def test_model_transparency_is_not_abstract():
    assert not inspect.isabstract(model_Transparency)


def test_model_transparency_constructor_exists():
    assert callable(model_Transparency.__init__)


def test_model_transparency_constructor_args():
    sig = inspect.signature(model_Transparency.__init__)
    params = list(sig.parameters.keys())
    assert "percent" in params, "Missing parameter 'percent'"

def test_model_transparency_has_percent():
    assert hasattr(model_Transparency, "percent")
    descriptor = None
    for klass in model_Transparency.__mro__:
        if "percent" in klass.__dict__:
            descriptor = klass.__dict__["percent"]
            break
    assert isinstance(descriptor, property)



def test_model_linestyle_is_not_abstract():
    assert not inspect.isabstract(model_LineStyle)


def test_model_linestyle_constructor_exists():
    assert callable(model_LineStyle.__init__)


def test_model_linestyle_constructor_args():
    sig = inspect.signature(model_LineStyle.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "manhattan" in params, "Missing parameter 'manhattan'"

def test_model_linestyle_has_style():
    assert hasattr(model_LineStyle, "style")
    descriptor = None
    for klass in model_LineStyle.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_model_linestyle_has_manhattan():
    assert hasattr(model_LineStyle, "manhattan")
    descriptor = None
    for klass in model_LineStyle.__mro__:
        if "manhattan" in klass.__dict__:
            descriptor = klass.__dict__["manhattan"]
            break
    assert isinstance(descriptor, property)



def test_model_textalign_is_not_abstract():
    assert not inspect.isabstract(model_TextAlign)


def test_model_textalign_constructor_exists():
    assert callable(model_TextAlign.__init__)


def test_model_textalign_constructor_args():
    sig = inspect.signature(model_TextAlign.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model_textalign_has_value():
    assert hasattr(model_TextAlign, "value")
    descriptor = None
    for klass in model_TextAlign.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model_fontproperties_is_not_abstract():
    assert not inspect.isabstract(model_FontProperties)


def test_model_fontproperties_constructor_exists():
    assert callable(model_FontProperties.__init__)


def test_model_fontproperties_constructor_args():
    sig = inspect.signature(model_FontProperties.__init__)
    params = list(sig.parameters.keys())
    assert "face" in params, "Missing parameter 'face'"
    assert "bold" in params, "Missing parameter 'bold'"
    assert "italics" in params, "Missing parameter 'italics'"
    assert "size" in params, "Missing parameter 'size'"

def test_model_fontproperties_has_face():
    assert hasattr(model_FontProperties, "face")
    descriptor = None
    for klass in model_FontProperties.__mro__:
        if "face" in klass.__dict__:
            descriptor = klass.__dict__["face"]
            break
    assert isinstance(descriptor, property)

def test_model_fontproperties_has_bold():
    assert hasattr(model_FontProperties, "bold")
    descriptor = None
    for klass in model_FontProperties.__mro__:
        if "bold" in klass.__dict__:
            descriptor = klass.__dict__["bold"]
            break
    assert isinstance(descriptor, property)

def test_model_fontproperties_has_italics():
    assert hasattr(model_FontProperties, "italics")
    descriptor = None
    for klass in model_FontProperties.__mro__:
        if "italics" in klass.__dict__:
            descriptor = klass.__dict__["italics"]
            break
    assert isinstance(descriptor, property)

def test_model_fontproperties_has_size():
    assert hasattr(model_FontProperties, "size")
    descriptor = None
    for klass in model_FontProperties.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_model_textpart_is_not_abstract():
    assert not inspect.isabstract(model_TextPart)


def test_model_textpart_constructor_exists():
    assert callable(model_TextPart.__init__)


def test_model_textpart_constructor_args():
    sig = inspect.signature(model_TextPart.__init__)
    params = list(sig.parameters.keys())
    assert "editable" in params, "Missing parameter 'editable'"
    assert "text" in params, "Missing parameter 'text'"

def test_model_textpart_has_editable():
    assert hasattr(model_TextPart, "editable")
    descriptor = None
    for klass in model_TextPart.__mro__:
        if "editable" in klass.__dict__:
            descriptor = klass.__dict__["editable"]
            break
    assert isinstance(descriptor, property)

def test_model_textpart_has_text():
    assert hasattr(model_TextPart, "text")
    descriptor = None
    for klass in model_TextPart.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_model_textvalue_is_not_abstract():
    assert not inspect.isabstract(model_TextValue)


def test_model_textvalue_constructor_exists():
    assert callable(model_TextValue.__init__)


def test_model_textvalue_constructor_args():
    sig = inspect.signature(model_TextValue.__init__)
    params = list(sig.parameters.keys())



def test_model_visible_is_not_abstract():
    assert not inspect.isabstract(model_Visible)


def test_model_visible_constructor_exists():
    assert callable(model_Visible.__init__)


def test_model_visible_constructor_args():
    sig = inspect.signature(model_Visible.__init__)
    params = list(sig.parameters.keys())



def test_model_layout_is_not_abstract():
    assert not inspect.isabstract(model_Layout)


def test_model_layout_constructor_exists():
    assert callable(model_Layout.__init__)


def test_model_layout_constructor_args():
    sig = inspect.signature(model_Layout.__init__)
    params = list(sig.parameters.keys())
    assert "vertical" in params, "Missing parameter 'vertical'"
    assert "horizontal" in params, "Missing parameter 'horizontal'"
    assert "margin" in params, "Missing parameter 'margin'"

def test_model_layout_has_vertical():
    assert hasattr(model_Layout, "vertical")
    descriptor = None
    for klass in model_Layout.__mro__:
        if "vertical" in klass.__dict__:
            descriptor = klass.__dict__["vertical"]
            break
    assert isinstance(descriptor, property)

def test_model_layout_has_horizontal():
    assert hasattr(model_Layout, "horizontal")
    descriptor = None
    for klass in model_Layout.__mro__:
        if "horizontal" in klass.__dict__:
            descriptor = klass.__dict__["horizontal"]
            break
    assert isinstance(descriptor, property)

def test_model_layout_has_margin():
    assert hasattr(model_Layout, "margin")
    descriptor = None
    for klass in model_Layout.__mro__:
        if "margin" in klass.__dict__:
            descriptor = klass.__dict__["margin"]
            break
    assert isinstance(descriptor, property)



def test_model_corner_is_not_abstract():
    assert not inspect.isabstract(model_Corner)


def test_model_corner_constructor_exists():
    assert callable(model_Corner.__init__)


def test_model_corner_constructor_args():
    sig = inspect.signature(model_Corner.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_model_corner_has_angle():
    assert hasattr(model_Corner, "angle")
    descriptor = None
    for klass in model_Corner.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_model_line_is_not_abstract():
    assert not inspect.isabstract(model_Line)


def test_model_line_constructor_exists():
    assert callable(model_Line.__init__)


def test_model_line_constructor_args():
    sig = inspect.signature(model_Line.__init__)
    params = list(sig.parameters.keys())
    assert "horizontal" in params, "Missing parameter 'horizontal'"
    assert "vertical" in params, "Missing parameter 'vertical'"

def test_model_line_has_horizontal():
    assert hasattr(model_Line, "horizontal")
    descriptor = None
    for klass in model_Line.__mro__:
        if "horizontal" in klass.__dict__:
            descriptor = klass.__dict__["horizontal"]
            break
    assert isinstance(descriptor, property)

def test_model_line_has_vertical():
    assert hasattr(model_Line, "vertical")
    descriptor = None
    for klass in model_Line.__mro__:
        if "vertical" in klass.__dict__:
            descriptor = klass.__dict__["vertical"]
            break
    assert isinstance(descriptor, property)



def test_model_triangle_is_not_abstract():
    assert not inspect.isabstract(model_Triangle)


def test_model_triangle_constructor_exists():
    assert callable(model_Triangle.__init__)


def test_model_triangle_constructor_args():
    sig = inspect.signature(model_Triangle.__init__)
    params = list(sig.parameters.keys())



def test_model_polyline_is_not_abstract():
    assert not inspect.isabstract(model_Polyline)


def test_model_polyline_constructor_exists():
    assert callable(model_Polyline.__init__)


def test_model_polyline_constructor_args():
    sig = inspect.signature(model_Polyline.__init__)
    params = list(sig.parameters.keys())
    assert "polygon" in params, "Missing parameter 'polygon'"
    assert "polyline" in params, "Missing parameter 'polyline'"

def test_model_polyline_has_polygon():
    assert hasattr(model_Polyline, "polygon")
    descriptor = None
    for klass in model_Polyline.__mro__:
        if "polygon" in klass.__dict__:
            descriptor = klass.__dict__["polygon"]
            break
    assert isinstance(descriptor, property)

def test_model_polyline_has_polyline():
    assert hasattr(model_Polyline, "polyline")
    descriptor = None
    for klass in model_Polyline.__mro__:
        if "polyline" in klass.__dict__:
            descriptor = klass.__dict__["polyline"]
            break
    assert isinstance(descriptor, property)



def test_model_ellipse_is_not_abstract():
    assert not inspect.isabstract(model_Ellipse)


def test_model_ellipse_constructor_exists():
    assert callable(model_Ellipse.__init__)


def test_model_ellipse_constructor_args():
    sig = inspect.signature(model_Ellipse.__init__)
    params = list(sig.parameters.keys())
    assert "circle" in params, "Missing parameter 'circle'"
    assert "ellipse" in params, "Missing parameter 'ellipse'"

def test_model_ellipse_has_circle():
    assert hasattr(model_Ellipse, "circle")
    descriptor = None
    for klass in model_Ellipse.__mro__:
        if "circle" in klass.__dict__:
            descriptor = klass.__dict__["circle"]
            break
    assert isinstance(descriptor, property)

def test_model_ellipse_has_ellipse():
    assert hasattr(model_Ellipse, "ellipse")
    descriptor = None
    for klass in model_Ellipse.__mro__:
        if "ellipse" in klass.__dict__:
            descriptor = klass.__dict__["ellipse"]
            break
    assert isinstance(descriptor, property)



def test_model_rhombus_is_not_abstract():
    assert not inspect.isabstract(model_Rhombus)


def test_model_rhombus_constructor_exists():
    assert callable(model_Rhombus.__init__)


def test_model_rhombus_constructor_args():
    sig = inspect.signature(model_Rhombus.__init__)
    params = list(sig.parameters.keys())



def test_model_colorfeature_is_not_abstract():
    assert not inspect.isabstract(model_ColorFeature)


def test_model_colorfeature_constructor_exists():
    assert callable(model_ColorFeature.__init__)


def test_model_colorfeature_constructor_args():
    sig = inspect.signature(model_ColorFeature.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_model_colorfeature_has_type():
    assert hasattr(model_ColorFeature, "type")
    descriptor = None
    for klass in model_ColorFeature.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_anchordirection_exists():
    # Check that the Enumeration exists
    assert AnchorDirection is not None

def test_anchordirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AnchorDirection]
    expected_literals = [
        "OUTGOING",
        "INCOMING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AnchorDirection"

def test_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "DIFFERENT",
        "EQUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"

def test_booleanliteral_exists():
    # Check that the Enumeration exists
    assert BooleanLiteral is not None

def test_booleanliteral_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanLiteral]
    expected_literals = [
        "FALSE",
        "TRUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanLiteral"

def test_defaultcolor_exists():
    # Check that the Enumeration exists
    assert DefaultColor is not None

def test_defaultcolor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DefaultColor]
    expected_literals = [
        "GRAY",
        "MAROON",
        "NAVY",
        "PURPLE",
        "BLUE",
        "YELLOW",
        "OLIVE",
        "FUCHSIA",
        "WHITE",
        "TEAL",
        "RED",
        "SILVER",
        "BLACK",
        "LIME",
        "GREEN",
        "AQUA",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DefaultColor"

def test_textalignvalue_exists():
    # Check that the Enumeration exists
    assert TextAlignValue is not None

def test_textalignvalue_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextAlignValue]
    expected_literals = [
        "RIGHT",
        "LEFT",
        "CENTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextAlignValue"

def test_linetype_exists():
    # Check that the Enumeration exists
    assert LineType is not None

def test_linetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineType]
    expected_literals = [
        "DASH",
        "SOLID",
        "DOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineType"


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
Value_strategy = st.builds(
    Value,
)
model_BooleanValue_strategy = st.builds(
    model_BooleanValue,
    value=
        safe_text
)
model_EnumValue_strategy = st.builds(
    model_EnumValue,
    name=
        safe_text
)
model_StringValue_strategy = st.builds(
    model_StringValue,
    null=
        st.booleans(),
    value=
        safe_text
)
model_DoubleValue_strategy = st.builds(
    model_DoubleValue,
    valueInt=
        st.integers(),
    valueDecimal=
        st.integers()
)
model_IntValue_strategy = st.builds(
    model_IntValue,
    value=
        st.integers()
)
model_CustomColor_strategy = st.builds(
    model_CustomColor,
    name=
        safe_text,
    G=
        st.integers(),
    B=
        st.integers(),
    R=
        st.integers()
)
Feature_strategy = st.builds(
    Feature,
)
model_Anchor_strategy = st.builds(
    model_Anchor,
    direction=
        safe_text,
    max=
        st.integers()
)
ConnectableElement_strategy = st.builds(
    ConnectableElement,
)
model_Rectangle_strategy = st.builds(
    model_Rectangle,
    rectangle=
        st.booleans(),
    square=
        st.booleans()
)
model_Label_strategy = st.builds(
    model_Label,
)
model_Image_strategy = st.builds(
    model_Image,
    imageId=
        safe_text
)
model_Invisible_strategy = st.builds(
    model_Invisible,
)
model_Custom_strategy = st.builds(
    model_Custom,
)
model_Color_strategy = st.builds(
    model_Color,
    default=
        safe_text
)
model_Contains_strategy = st.builds(
    model_Contains,
)
model_EClass_strategy = st.builds(
    model_EClass,
)
model_ImportStatement_strategy = st.builds(
    model_ImportStatement,
    importedNamespace=
        safe_text
)
model_CustomFigure_strategy = st.builds(
    model_CustomFigure,
    name=
        safe_text
)
model_DiagramElement_strategy = st.builds(
    model_DiagramElement,
)
model_Colors_strategy = st.builds(
    model_Colors,
)
model_Decorator_strategy = st.builds(
    model_Decorator,
)
model_EReference_strategy = st.builds(
    model_EReference,
)
FeatureContainer_strategy = st.builds(
    FeatureContainer,
)
model_Arrow_strategy = st.builds(
    model_Arrow,
)
model_ConnectableElement_strategy = st.builds(
    model_ConnectableElement,
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
model_Link_strategy = st.builds(
    model_Link,
    reference=
        st.booleans(),
    complex=
        st.booleans()
)
model_Node_strategy = st.builds(
    model_Node,
)
model_Value_strategy = st.builds(
    model_Value,
)
model_EAttribute_strategy = st.builds(
    model_EAttribute,
)
model_FeatureContainer_strategy = st.builds(
    model_FeatureContainer,
)
model_FeatureConditional_strategy = st.builds(
    model_FeatureConditional,
    operator=
        safe_text
)
model_Feature_strategy = st.builds(
    model_Feature,
)
model_Diagram_strategy = st.builds(
    model_Diagram,
)
model_MetaModel_strategy = st.builds(
    model_MetaModel,
    plugin=
        safe_text,
    ecorePath=
        safe_text
)
model_XDiagram_strategy = st.builds(
    model_XDiagram,
)
model_LineWidth_strategy = st.builds(
    model_LineWidth,
    width=
        st.integers()
)
model_Position_strategy = st.builds(
    model_Position,
    xRelative=
        st.booleans(),
    yRelative=
        st.booleans(),
    y=
        st.integers(),
    x=
        st.integers()
)
model_Point_strategy = st.builds(
    model_Point,
    y=
        st.integers(),
    x=
        st.integers()
)
model_Size_strategy = st.builds(
    model_Size,
    widthRelative=
        st.booleans(),
    heightRelative=
        st.booleans(),
    width=
        st.integers(),
    height=
        st.integers(),
    resizable=
        st.booleans()
)
model_Transparency_strategy = st.builds(
    model_Transparency,
    percent=
        st.integers()
)
model_LineStyle_strategy = st.builds(
    model_LineStyle,
    style=
        safe_text,
    manhattan=
        st.booleans()
)
model_TextAlign_strategy = st.builds(
    model_TextAlign,
    value=
        safe_text
)
model_FontProperties_strategy = st.builds(
    model_FontProperties,
    face=
        safe_text,
    bold=
        st.booleans(),
    italics=
        st.booleans(),
    size=
        st.integers()
)
model_TextPart_strategy = st.builds(
    model_TextPart,
    editable=
        st.booleans(),
    text=
        safe_text
)
model_TextValue_strategy = st.builds(
    model_TextValue,
)
model_Visible_strategy = st.builds(
    model_Visible,
)
model_Layout_strategy = st.builds(
    model_Layout,
    vertical=
        st.booleans(),
    horizontal=
        st.booleans(),
    margin=
        st.integers()
)
model_Corner_strategy = st.builds(
    model_Corner,
    angle=
        st.integers()
)
model_Line_strategy = st.builds(
    model_Line,
    horizontal=
        st.booleans(),
    vertical=
        st.booleans()
)
model_Triangle_strategy = st.builds(
    model_Triangle,
)
model_Polyline_strategy = st.builds(
    model_Polyline,
    polygon=
        st.booleans(),
    polyline=
        st.booleans()
)
model_Ellipse_strategy = st.builds(
    model_Ellipse,
    circle=
        st.booleans(),
    ellipse=
        st.booleans()
)
model_Rhombus_strategy = st.builds(
    model_Rhombus,
)
model_ColorFeature_strategy = st.builds(
    model_ColorFeature,
    type=
        safe_text
)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=model_BooleanValue_strategy)
@settings(max_examples=50)
def test_model_booleanvalue_instantiation(instance):
    assert isinstance(instance, model_BooleanValue)



@given(instance=model_BooleanValue_strategy)
def test_model_booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model_EnumValue_strategy)
@settings(max_examples=50)
def test_model_enumvalue_instantiation(instance):
    assert isinstance(instance, model_EnumValue)



@given(instance=model_EnumValue_strategy)
def test_model_enumvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_StringValue_strategy)
@settings(max_examples=50)
def test_model_stringvalue_instantiation(instance):
    assert isinstance(instance, model_StringValue)



@given(instance=model_StringValue_strategy)
def test_model_stringvalue_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original



@given(instance=model_StringValue_strategy)
def test_model_stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model_DoubleValue_strategy)
@settings(max_examples=50)
def test_model_doublevalue_instantiation(instance):
    assert isinstance(instance, model_DoubleValue)



@given(instance=model_DoubleValue_strategy)
def test_model_doublevalue_valueInt_setter(instance):
    original = instance.valueInt
    instance.valueInt = original
    assert instance.valueInt == original



@given(instance=model_DoubleValue_strategy)
def test_model_doublevalue_valueDecimal_setter(instance):
    original = instance.valueDecimal
    instance.valueDecimal = original
    assert instance.valueDecimal == original

@given(instance=model_IntValue_strategy)
@settings(max_examples=50)
def test_model_intvalue_instantiation(instance):
    assert isinstance(instance, model_IntValue)



@given(instance=model_IntValue_strategy)
def test_model_intvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model_CustomColor_strategy)
@settings(max_examples=50)
def test_model_customcolor_instantiation(instance):
    assert isinstance(instance, model_CustomColor)



@given(instance=model_CustomColor_strategy)
def test_model_customcolor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_CustomColor_strategy)
def test_model_customcolor_G_setter(instance):
    original = instance.G
    instance.G = original
    assert instance.G == original



@given(instance=model_CustomColor_strategy)
def test_model_customcolor_B_setter(instance):
    original = instance.B
    instance.B = original
    assert instance.B == original



@given(instance=model_CustomColor_strategy)
def test_model_customcolor_R_setter(instance):
    original = instance.R
    instance.R = original
    assert instance.R == original

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=model_Anchor_strategy)
@settings(max_examples=50)
def test_model_anchor_instantiation(instance):
    assert isinstance(instance, model_Anchor)



@given(instance=model_Anchor_strategy)
def test_model_anchor_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=model_Anchor_strategy)
def test_model_anchor_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=ConnectableElement_strategy)
@settings(max_examples=50)
def test_connectableelement_instantiation(instance):
    assert isinstance(instance, ConnectableElement)

@given(instance=model_Rectangle_strategy)
@settings(max_examples=50)
def test_model_rectangle_instantiation(instance):
    assert isinstance(instance, model_Rectangle)



@given(instance=model_Rectangle_strategy)
def test_model_rectangle_rectangle_setter(instance):
    original = instance.rectangle
    instance.rectangle = original
    assert instance.rectangle == original



@given(instance=model_Rectangle_strategy)
def test_model_rectangle_square_setter(instance):
    original = instance.square
    instance.square = original
    assert instance.square == original

@given(instance=model_Label_strategy)
@settings(max_examples=50)
def test_model_label_instantiation(instance):
    assert isinstance(instance, model_Label)

@given(instance=model_Image_strategy)
@settings(max_examples=50)
def test_model_image_instantiation(instance):
    assert isinstance(instance, model_Image)



@given(instance=model_Image_strategy)
def test_model_image_imageId_setter(instance):
    original = instance.imageId
    instance.imageId = original
    assert instance.imageId == original

@given(instance=model_Invisible_strategy)
@settings(max_examples=50)
def test_model_invisible_instantiation(instance):
    assert isinstance(instance, model_Invisible)

@given(instance=model_Custom_strategy)
@settings(max_examples=50)
def test_model_custom_instantiation(instance):
    assert isinstance(instance, model_Custom)

@given(instance=model_Color_strategy)
@settings(max_examples=50)
def test_model_color_instantiation(instance):
    assert isinstance(instance, model_Color)



@given(instance=model_Color_strategy)
def test_model_color_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=model_Contains_strategy)
@settings(max_examples=50)
def test_model_contains_instantiation(instance):
    assert isinstance(instance, model_Contains)

@given(instance=model_EClass_strategy)
@settings(max_examples=50)
def test_model_eclass_instantiation(instance):
    assert isinstance(instance, model_EClass)

@given(instance=model_ImportStatement_strategy)
@settings(max_examples=50)
def test_model_importstatement_instantiation(instance):
    assert isinstance(instance, model_ImportStatement)



@given(instance=model_ImportStatement_strategy)
def test_model_importstatement_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=model_CustomFigure_strategy)
@settings(max_examples=50)
def test_model_customfigure_instantiation(instance):
    assert isinstance(instance, model_CustomFigure)



@given(instance=model_CustomFigure_strategy)
def test_model_customfigure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_DiagramElement_strategy)
@settings(max_examples=50)
def test_model_diagramelement_instantiation(instance):
    assert isinstance(instance, model_DiagramElement)

@given(instance=model_Colors_strategy)
@settings(max_examples=50)
def test_model_colors_instantiation(instance):
    assert isinstance(instance, model_Colors)

@given(instance=model_Decorator_strategy)
@settings(max_examples=50)
def test_model_decorator_instantiation(instance):
    assert isinstance(instance, model_Decorator)

@given(instance=model_EReference_strategy)
@settings(max_examples=50)
def test_model_ereference_instantiation(instance):
    assert isinstance(instance, model_EReference)

@given(instance=FeatureContainer_strategy)
@settings(max_examples=50)
def test_featurecontainer_instantiation(instance):
    assert isinstance(instance, FeatureContainer)

@given(instance=model_Arrow_strategy)
@settings(max_examples=50)
def test_model_arrow_instantiation(instance):
    assert isinstance(instance, model_Arrow)

@given(instance=model_ConnectableElement_strategy)
@settings(max_examples=50)
def test_model_connectableelement_instantiation(instance):
    assert isinstance(instance, model_ConnectableElement)

@given(instance=DiagramElement_strategy)
@settings(max_examples=50)
def test_diagramelement_instantiation(instance):
    assert isinstance(instance, DiagramElement)

@given(instance=model_Link_strategy)
@settings(max_examples=50)
def test_model_link_instantiation(instance):
    assert isinstance(instance, model_Link)



@given(instance=model_Link_strategy)
def test_model_link_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original



@given(instance=model_Link_strategy)
def test_model_link_complex_setter(instance):
    original = instance.complex
    instance.complex = original
    assert instance.complex == original

@given(instance=model_Node_strategy)
@settings(max_examples=50)
def test_model_node_instantiation(instance):
    assert isinstance(instance, model_Node)

@given(instance=model_Value_strategy)
@settings(max_examples=50)
def test_model_value_instantiation(instance):
    assert isinstance(instance, model_Value)

@given(instance=model_EAttribute_strategy)
@settings(max_examples=50)
def test_model_eattribute_instantiation(instance):
    assert isinstance(instance, model_EAttribute)

@given(instance=model_FeatureContainer_strategy)
@settings(max_examples=50)
def test_model_featurecontainer_instantiation(instance):
    assert isinstance(instance, model_FeatureContainer)

@given(instance=model_FeatureConditional_strategy)
@settings(max_examples=50)
def test_model_featureconditional_instantiation(instance):
    assert isinstance(instance, model_FeatureConditional)



@given(instance=model_FeatureConditional_strategy)
def test_model_featureconditional_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=model_Feature_strategy)
@settings(max_examples=50)
def test_model_feature_instantiation(instance):
    assert isinstance(instance, model_Feature)

@given(instance=model_Diagram_strategy)
@settings(max_examples=50)
def test_model_diagram_instantiation(instance):
    assert isinstance(instance, model_Diagram)

@given(instance=model_MetaModel_strategy)
@settings(max_examples=50)
def test_model_metamodel_instantiation(instance):
    assert isinstance(instance, model_MetaModel)



@given(instance=model_MetaModel_strategy)
def test_model_metamodel_plugin_setter(instance):
    original = instance.plugin
    instance.plugin = original
    assert instance.plugin == original



@given(instance=model_MetaModel_strategy)
def test_model_metamodel_ecorePath_setter(instance):
    original = instance.ecorePath
    instance.ecorePath = original
    assert instance.ecorePath == original

@given(instance=model_XDiagram_strategy)
@settings(max_examples=50)
def test_model_xdiagram_instantiation(instance):
    assert isinstance(instance, model_XDiagram)

@given(instance=model_LineWidth_strategy)
@settings(max_examples=50)
def test_model_linewidth_instantiation(instance):
    assert isinstance(instance, model_LineWidth)



@given(instance=model_LineWidth_strategy)
def test_model_linewidth_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=model_Position_strategy)
@settings(max_examples=50)
def test_model_position_instantiation(instance):
    assert isinstance(instance, model_Position)



@given(instance=model_Position_strategy)
def test_model_position_xRelative_setter(instance):
    original = instance.xRelative
    instance.xRelative = original
    assert instance.xRelative == original



@given(instance=model_Position_strategy)
def test_model_position_yRelative_setter(instance):
    original = instance.yRelative
    instance.yRelative = original
    assert instance.yRelative == original



@given(instance=model_Position_strategy)
def test_model_position_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=model_Position_strategy)
def test_model_position_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=model_Point_strategy)
@settings(max_examples=50)
def test_model_point_instantiation(instance):
    assert isinstance(instance, model_Point)



@given(instance=model_Point_strategy)
def test_model_point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=model_Point_strategy)
def test_model_point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=model_Size_strategy)
@settings(max_examples=50)
def test_model_size_instantiation(instance):
    assert isinstance(instance, model_Size)



@given(instance=model_Size_strategy)
def test_model_size_widthRelative_setter(instance):
    original = instance.widthRelative
    instance.widthRelative = original
    assert instance.widthRelative == original



@given(instance=model_Size_strategy)
def test_model_size_heightRelative_setter(instance):
    original = instance.heightRelative
    instance.heightRelative = original
    assert instance.heightRelative == original



@given(instance=model_Size_strategy)
def test_model_size_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=model_Size_strategy)
def test_model_size_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=model_Size_strategy)
def test_model_size_resizable_setter(instance):
    original = instance.resizable
    instance.resizable = original
    assert instance.resizable == original

@given(instance=model_Transparency_strategy)
@settings(max_examples=50)
def test_model_transparency_instantiation(instance):
    assert isinstance(instance, model_Transparency)



@given(instance=model_Transparency_strategy)
def test_model_transparency_percent_setter(instance):
    original = instance.percent
    instance.percent = original
    assert instance.percent == original

@given(instance=model_LineStyle_strategy)
@settings(max_examples=50)
def test_model_linestyle_instantiation(instance):
    assert isinstance(instance, model_LineStyle)



@given(instance=model_LineStyle_strategy)
def test_model_linestyle_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=model_LineStyle_strategy)
def test_model_linestyle_manhattan_setter(instance):
    original = instance.manhattan
    instance.manhattan = original
    assert instance.manhattan == original

@given(instance=model_TextAlign_strategy)
@settings(max_examples=50)
def test_model_textalign_instantiation(instance):
    assert isinstance(instance, model_TextAlign)



@given(instance=model_TextAlign_strategy)
def test_model_textalign_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model_FontProperties_strategy)
@settings(max_examples=50)
def test_model_fontproperties_instantiation(instance):
    assert isinstance(instance, model_FontProperties)



@given(instance=model_FontProperties_strategy)
def test_model_fontproperties_face_setter(instance):
    original = instance.face
    instance.face = original
    assert instance.face == original



@given(instance=model_FontProperties_strategy)
def test_model_fontproperties_bold_setter(instance):
    original = instance.bold
    instance.bold = original
    assert instance.bold == original



@given(instance=model_FontProperties_strategy)
def test_model_fontproperties_italics_setter(instance):
    original = instance.italics
    instance.italics = original
    assert instance.italics == original



@given(instance=model_FontProperties_strategy)
def test_model_fontproperties_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=model_TextPart_strategy)
@settings(max_examples=50)
def test_model_textpart_instantiation(instance):
    assert isinstance(instance, model_TextPart)



@given(instance=model_TextPart_strategy)
def test_model_textpart_editable_setter(instance):
    original = instance.editable
    instance.editable = original
    assert instance.editable == original



@given(instance=model_TextPart_strategy)
def test_model_textpart_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=model_TextValue_strategy)
@settings(max_examples=50)
def test_model_textvalue_instantiation(instance):
    assert isinstance(instance, model_TextValue)

@given(instance=model_Visible_strategy)
@settings(max_examples=50)
def test_model_visible_instantiation(instance):
    assert isinstance(instance, model_Visible)

@given(instance=model_Layout_strategy)
@settings(max_examples=50)
def test_model_layout_instantiation(instance):
    assert isinstance(instance, model_Layout)



@given(instance=model_Layout_strategy)
def test_model_layout_vertical_setter(instance):
    original = instance.vertical
    instance.vertical = original
    assert instance.vertical == original



@given(instance=model_Layout_strategy)
def test_model_layout_horizontal_setter(instance):
    original = instance.horizontal
    instance.horizontal = original
    assert instance.horizontal == original



@given(instance=model_Layout_strategy)
def test_model_layout_margin_setter(instance):
    original = instance.margin
    instance.margin = original
    assert instance.margin == original

@given(instance=model_Corner_strategy)
@settings(max_examples=50)
def test_model_corner_instantiation(instance):
    assert isinstance(instance, model_Corner)



@given(instance=model_Corner_strategy)
def test_model_corner_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=model_Line_strategy)
@settings(max_examples=50)
def test_model_line_instantiation(instance):
    assert isinstance(instance, model_Line)



@given(instance=model_Line_strategy)
def test_model_line_horizontal_setter(instance):
    original = instance.horizontal
    instance.horizontal = original
    assert instance.horizontal == original



@given(instance=model_Line_strategy)
def test_model_line_vertical_setter(instance):
    original = instance.vertical
    instance.vertical = original
    assert instance.vertical == original

@given(instance=model_Triangle_strategy)
@settings(max_examples=50)
def test_model_triangle_instantiation(instance):
    assert isinstance(instance, model_Triangle)

@given(instance=model_Polyline_strategy)
@settings(max_examples=50)
def test_model_polyline_instantiation(instance):
    assert isinstance(instance, model_Polyline)



@given(instance=model_Polyline_strategy)
def test_model_polyline_polygon_setter(instance):
    original = instance.polygon
    instance.polygon = original
    assert instance.polygon == original



@given(instance=model_Polyline_strategy)
def test_model_polyline_polyline_setter(instance):
    original = instance.polyline
    instance.polyline = original
    assert instance.polyline == original

@given(instance=model_Ellipse_strategy)
@settings(max_examples=50)
def test_model_ellipse_instantiation(instance):
    assert isinstance(instance, model_Ellipse)



@given(instance=model_Ellipse_strategy)
def test_model_ellipse_circle_setter(instance):
    original = instance.circle
    instance.circle = original
    assert instance.circle == original



@given(instance=model_Ellipse_strategy)
def test_model_ellipse_ellipse_setter(instance):
    original = instance.ellipse
    instance.ellipse = original
    assert instance.ellipse == original

@given(instance=model_Rhombus_strategy)
@settings(max_examples=50)
def test_model_rhombus_instantiation(instance):
    assert isinstance(instance, model_Rhombus)

@given(instance=model_ColorFeature_strategy)
@settings(max_examples=50)
def test_model_colorfeature_instantiation(instance):
    assert isinstance(instance, model_ColorFeature)



@given(instance=model_ColorFeature_strategy)
def test_model_colorfeature_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
