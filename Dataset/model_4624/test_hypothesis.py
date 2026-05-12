import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    notation_Point,
    Figure,
    notation_Roundtangle,
    notation_Square,
    notation_Triangle,
    notation_Circle,
    notation_Cube,
    notation_Diamond,
    notation_Cylinder,
    notation_Polyline,
    notation_Rectangle,
    Style,
    notation_Style,
    Value,
    notation_ReferenceValue,
    notation_AttributeValue,
    TextualElement,
    notation_Value,
    notation_Keyword,
    notation_Token,
    notation_TextualContainment,
    notation_TextStyle,
    notation_IconStyle,
    notation_FigureContainment,
    GraphicalElement,
    notation_Composite,
    notation_Icon,
    notation_Image,
    notation_Label,
    notation_SyntaxOf,
    notation_BorderStyle,
    notation_FigureStyle,
    notation_Figure,
    notation_LineStyle,
    notation_Line,
    DiagramElement,
    notation_Node,
    IDElement,
    notation_GraphicalElement,
    notation_TextualElement,
    notation_IDElement,
    notation_DiagramElement,
    notation_DiagramDefinition,
    Relation,
    notation_Link,
    notation_Compartment,
    notation_Relation,
    notation_NotationDefinition,
    Layout,
    DefinitionType,
    Orientation,
    AudienceType,
    FillTextureType,
    LineTextureType,
    IconType,
    Color,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_notation_point_is_not_abstract():
    assert not inspect.isabstract(notation_Point)


def test_notation_point_constructor_exists():
    assert callable(notation_Point.__init__)


def test_notation_point_constructor_args():
    sig = inspect.signature(notation_Point.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_notation_point_has_x():
    assert hasattr(notation_Point, "x")
    descriptor = None
    for klass in notation_Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_notation_point_has_y():
    assert hasattr(notation_Point, "y")
    descriptor = None
    for klass in notation_Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_figure_is_not_abstract():
    assert not inspect.isabstract(Figure)


def test_figure_constructor_exists():
    assert callable(Figure.__init__)


def test_figure_constructor_args():
    sig = inspect.signature(Figure.__init__)
    params = list(sig.parameters.keys())



def test_notation_roundtangle_is_not_abstract():
    assert not inspect.isabstract(notation_Roundtangle)


def test_notation_roundtangle_constructor_exists():
    assert callable(notation_Roundtangle.__init__)


def test_notation_roundtangle_constructor_args():
    sig = inspect.signature(notation_Roundtangle.__init__)
    params = list(sig.parameters.keys())



def test_notation_square_is_not_abstract():
    assert not inspect.isabstract(notation_Square)


def test_notation_square_constructor_exists():
    assert callable(notation_Square.__init__)


def test_notation_square_constructor_args():
    sig = inspect.signature(notation_Square.__init__)
    params = list(sig.parameters.keys())



def test_notation_triangle_is_not_abstract():
    assert not inspect.isabstract(notation_Triangle)


def test_notation_triangle_constructor_exists():
    assert callable(notation_Triangle.__init__)


def test_notation_triangle_constructor_args():
    sig = inspect.signature(notation_Triangle.__init__)
    params = list(sig.parameters.keys())



def test_notation_circle_is_not_abstract():
    assert not inspect.isabstract(notation_Circle)


def test_notation_circle_constructor_exists():
    assert callable(notation_Circle.__init__)


def test_notation_circle_constructor_args():
    sig = inspect.signature(notation_Circle.__init__)
    params = list(sig.parameters.keys())



def test_notation_cube_is_not_abstract():
    assert not inspect.isabstract(notation_Cube)


def test_notation_cube_constructor_exists():
    assert callable(notation_Cube.__init__)


def test_notation_cube_constructor_args():
    sig = inspect.signature(notation_Cube.__init__)
    params = list(sig.parameters.keys())



def test_notation_diamond_is_not_abstract():
    assert not inspect.isabstract(notation_Diamond)


def test_notation_diamond_constructor_exists():
    assert callable(notation_Diamond.__init__)


def test_notation_diamond_constructor_args():
    sig = inspect.signature(notation_Diamond.__init__)
    params = list(sig.parameters.keys())



def test_notation_cylinder_is_not_abstract():
    assert not inspect.isabstract(notation_Cylinder)


def test_notation_cylinder_constructor_exists():
    assert callable(notation_Cylinder.__init__)


def test_notation_cylinder_constructor_args():
    sig = inspect.signature(notation_Cylinder.__init__)
    params = list(sig.parameters.keys())



def test_notation_polyline_is_not_abstract():
    assert not inspect.isabstract(notation_Polyline)


def test_notation_polyline_constructor_exists():
    assert callable(notation_Polyline.__init__)


def test_notation_polyline_constructor_args():
    sig = inspect.signature(notation_Polyline.__init__)
    params = list(sig.parameters.keys())



def test_notation_rectangle_is_not_abstract():
    assert not inspect.isabstract(notation_Rectangle)


def test_notation_rectangle_constructor_exists():
    assert callable(notation_Rectangle.__init__)


def test_notation_rectangle_constructor_args():
    sig = inspect.signature(notation_Rectangle.__init__)
    params = list(sig.parameters.keys())



def test_style_is_not_abstract():
    assert not inspect.isabstract(Style)


def test_style_constructor_exists():
    assert callable(Style.__init__)


def test_style_constructor_args():
    sig = inspect.signature(Style.__init__)
    params = list(sig.parameters.keys())



def test_notation_style_is_not_abstract():
    assert not inspect.isabstract(notation_Style)


def test_notation_style_constructor_exists():
    assert callable(notation_Style.__init__)


def test_notation_style_constructor_args():
    sig = inspect.signature(notation_Style.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_notation_referencevalue_is_not_abstract():
    assert not inspect.isabstract(notation_ReferenceValue)


def test_notation_referencevalue_constructor_exists():
    assert callable(notation_ReferenceValue.__init__)


def test_notation_referencevalue_constructor_args():
    sig = inspect.signature(notation_ReferenceValue.__init__)
    params = list(sig.parameters.keys())



def test_notation_attributevalue_is_not_abstract():
    assert not inspect.isabstract(notation_AttributeValue)


def test_notation_attributevalue_constructor_exists():
    assert callable(notation_AttributeValue.__init__)


def test_notation_attributevalue_constructor_args():
    sig = inspect.signature(notation_AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_textualelement_is_not_abstract():
    assert not inspect.isabstract(TextualElement)


def test_textualelement_constructor_exists():
    assert callable(TextualElement.__init__)


def test_textualelement_constructor_args():
    sig = inspect.signature(TextualElement.__init__)
    params = list(sig.parameters.keys())



def test_notation_value_is_not_abstract():
    assert not inspect.isabstract(notation_Value)


def test_notation_value_constructor_exists():
    assert callable(notation_Value.__init__)


def test_notation_value_constructor_args():
    sig = inspect.signature(notation_Value.__init__)
    params = list(sig.parameters.keys())



def test_notation_keyword_is_not_abstract():
    assert not inspect.isabstract(notation_Keyword)


def test_notation_keyword_constructor_exists():
    assert callable(notation_Keyword.__init__)


def test_notation_keyword_constructor_args():
    sig = inspect.signature(notation_Keyword.__init__)
    params = list(sig.parameters.keys())



def test_notation_token_is_not_abstract():
    assert not inspect.isabstract(notation_Token)


def test_notation_token_constructor_exists():
    assert callable(notation_Token.__init__)


def test_notation_token_constructor_args():
    sig = inspect.signature(notation_Token.__init__)
    params = list(sig.parameters.keys())



def test_notation_textualcontainment_is_not_abstract():
    assert not inspect.isabstract(notation_TextualContainment)


def test_notation_textualcontainment_constructor_exists():
    assert callable(notation_TextualContainment.__init__)


def test_notation_textualcontainment_constructor_args():
    sig = inspect.signature(notation_TextualContainment.__init__)
    params = list(sig.parameters.keys())
    assert "layout" in params, "Missing parameter 'layout'"

def test_notation_textualcontainment_has_layout():
    assert hasattr(notation_TextualContainment, "layout")
    descriptor = None
    for klass in notation_TextualContainment.__mro__:
        if "layout" in klass.__dict__:
            descriptor = klass.__dict__["layout"]
            break
    assert isinstance(descriptor, property)



def test_notation_textstyle_is_not_abstract():
    assert not inspect.isabstract(notation_TextStyle)


def test_notation_textstyle_constructor_exists():
    assert callable(notation_TextStyle.__init__)


def test_notation_textstyle_constructor_args():
    sig = inspect.signature(notation_TextStyle.__init__)
    params = list(sig.parameters.keys())
    assert "bold" in params, "Missing parameter 'bold'"
    assert "underlined" in params, "Missing parameter 'underlined'"
    assert "fontColor" in params, "Missing parameter 'fontColor'"
    assert "fontName" in params, "Missing parameter 'fontName'"
    assert "fontSize" in params, "Missing parameter 'fontSize'"
    assert "italic" in params, "Missing parameter 'italic'"

def test_notation_textstyle_has_bold():
    assert hasattr(notation_TextStyle, "bold")
    descriptor = None
    for klass in notation_TextStyle.__mro__:
        if "bold" in klass.__dict__:
            descriptor = klass.__dict__["bold"]
            break
    assert isinstance(descriptor, property)

def test_notation_textstyle_has_underlined():
    assert hasattr(notation_TextStyle, "underlined")
    descriptor = None
    for klass in notation_TextStyle.__mro__:
        if "underlined" in klass.__dict__:
            descriptor = klass.__dict__["underlined"]
            break
    assert isinstance(descriptor, property)

def test_notation_textstyle_has_fontColor():
    assert hasattr(notation_TextStyle, "fontColor")
    descriptor = None
    for klass in notation_TextStyle.__mro__:
        if "fontColor" in klass.__dict__:
            descriptor = klass.__dict__["fontColor"]
            break
    assert isinstance(descriptor, property)

def test_notation_textstyle_has_fontName():
    assert hasattr(notation_TextStyle, "fontName")
    descriptor = None
    for klass in notation_TextStyle.__mro__:
        if "fontName" in klass.__dict__:
            descriptor = klass.__dict__["fontName"]
            break
    assert isinstance(descriptor, property)

def test_notation_textstyle_has_fontSize():
    assert hasattr(notation_TextStyle, "fontSize")
    descriptor = None
    for klass in notation_TextStyle.__mro__:
        if "fontSize" in klass.__dict__:
            descriptor = klass.__dict__["fontSize"]
            break
    assert isinstance(descriptor, property)

def test_notation_textstyle_has_italic():
    assert hasattr(notation_TextStyle, "italic")
    descriptor = None
    for klass in notation_TextStyle.__mro__:
        if "italic" in klass.__dict__:
            descriptor = klass.__dict__["italic"]
            break
    assert isinstance(descriptor, property)



def test_notation_iconstyle_is_not_abstract():
    assert not inspect.isabstract(notation_IconStyle)


def test_notation_iconstyle_constructor_exists():
    assert callable(notation_IconStyle.__init__)


def test_notation_iconstyle_constructor_args():
    sig = inspect.signature(notation_IconStyle.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "color" in params, "Missing parameter 'color'"
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "width" in params, "Missing parameter 'width'"
    assert "brightness" in params, "Missing parameter 'brightness'"

def test_notation_iconstyle_has_height():
    assert hasattr(notation_IconStyle, "height")
    descriptor = None
    for klass in notation_IconStyle.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_notation_iconstyle_has_color():
    assert hasattr(notation_IconStyle, "color")
    descriptor = None
    for klass in notation_IconStyle.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_notation_iconstyle_has_orientation():
    assert hasattr(notation_IconStyle, "orientation")
    descriptor = None
    for klass in notation_IconStyle.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)

def test_notation_iconstyle_has_width():
    assert hasattr(notation_IconStyle, "width")
    descriptor = None
    for klass in notation_IconStyle.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_notation_iconstyle_has_brightness():
    assert hasattr(notation_IconStyle, "brightness")
    descriptor = None
    for klass in notation_IconStyle.__mro__:
        if "brightness" in klass.__dict__:
            descriptor = klass.__dict__["brightness"]
            break
    assert isinstance(descriptor, property)



def test_notation_figurecontainment_is_not_abstract():
    assert not inspect.isabstract(notation_FigureContainment)


def test_notation_figurecontainment_constructor_exists():
    assert callable(notation_FigureContainment.__init__)


def test_notation_figurecontainment_constructor_args():
    sig = inspect.signature(notation_FigureContainment.__init__)
    params = list(sig.parameters.keys())
    assert "layout" in params, "Missing parameter 'layout'"

def test_notation_figurecontainment_has_layout():
    assert hasattr(notation_FigureContainment, "layout")
    descriptor = None
    for klass in notation_FigureContainment.__mro__:
        if "layout" in klass.__dict__:
            descriptor = klass.__dict__["layout"]
            break
    assert isinstance(descriptor, property)



def test_graphicalelement_is_not_abstract():
    assert not inspect.isabstract(GraphicalElement)


def test_graphicalelement_constructor_exists():
    assert callable(GraphicalElement.__init__)


def test_graphicalelement_constructor_args():
    sig = inspect.signature(GraphicalElement.__init__)
    params = list(sig.parameters.keys())



def test_notation_composite_is_not_abstract():
    assert not inspect.isabstract(notation_Composite)


def test_notation_composite_constructor_exists():
    assert callable(notation_Composite.__init__)


def test_notation_composite_constructor_args():
    sig = inspect.signature(notation_Composite.__init__)
    params = list(sig.parameters.keys())
    assert "layout" in params, "Missing parameter 'layout'"

def test_notation_composite_has_layout():
    assert hasattr(notation_Composite, "layout")
    descriptor = None
    for klass in notation_Composite.__mro__:
        if "layout" in klass.__dict__:
            descriptor = klass.__dict__["layout"]
            break
    assert isinstance(descriptor, property)



def test_notation_icon_is_not_abstract():
    assert not inspect.isabstract(notation_Icon)


def test_notation_icon_constructor_exists():
    assert callable(notation_Icon.__init__)


def test_notation_icon_constructor_args():
    sig = inspect.signature(notation_Icon.__init__)
    params = list(sig.parameters.keys())
    assert "iconType" in params, "Missing parameter 'iconType'"

def test_notation_icon_has_iconType():
    assert hasattr(notation_Icon, "iconType")
    descriptor = None
    for klass in notation_Icon.__mro__:
        if "iconType" in klass.__dict__:
            descriptor = klass.__dict__["iconType"]
            break
    assert isinstance(descriptor, property)



def test_notation_image_is_not_abstract():
    assert not inspect.isabstract(notation_Image)


def test_notation_image_constructor_exists():
    assert callable(notation_Image.__init__)


def test_notation_image_constructor_args():
    sig = inspect.signature(notation_Image.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"

def test_notation_image_has_path():
    assert hasattr(notation_Image, "path")
    descriptor = None
    for klass in notation_Image.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_notation_label_is_not_abstract():
    assert not inspect.isabstract(notation_Label)


def test_notation_label_constructor_exists():
    assert callable(notation_Label.__init__)


def test_notation_label_constructor_args():
    sig = inspect.signature(notation_Label.__init__)
    params = list(sig.parameters.keys())



def test_notation_syntaxof_is_not_abstract():
    assert not inspect.isabstract(notation_SyntaxOf)


def test_notation_syntaxof_constructor_exists():
    assert callable(notation_SyntaxOf.__init__)


def test_notation_syntaxof_constructor_args():
    sig = inspect.signature(notation_SyntaxOf.__init__)
    params = list(sig.parameters.keys())



def test_notation_borderstyle_is_not_abstract():
    assert not inspect.isabstract(notation_BorderStyle)


def test_notation_borderstyle_constructor_exists():
    assert callable(notation_BorderStyle.__init__)


def test_notation_borderstyle_constructor_args():
    sig = inspect.signature(notation_BorderStyle.__init__)
    params = list(sig.parameters.keys())
    assert "thickness" in params, "Missing parameter 'thickness'"
    assert "color" in params, "Missing parameter 'color'"
    assert "texture" in params, "Missing parameter 'texture'"

def test_notation_borderstyle_has_thickness():
    assert hasattr(notation_BorderStyle, "thickness")
    descriptor = None
    for klass in notation_BorderStyle.__mro__:
        if "thickness" in klass.__dict__:
            descriptor = klass.__dict__["thickness"]
            break
    assert isinstance(descriptor, property)

def test_notation_borderstyle_has_color():
    assert hasattr(notation_BorderStyle, "color")
    descriptor = None
    for klass in notation_BorderStyle.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_notation_borderstyle_has_texture():
    assert hasattr(notation_BorderStyle, "texture")
    descriptor = None
    for klass in notation_BorderStyle.__mro__:
        if "texture" in klass.__dict__:
            descriptor = klass.__dict__["texture"]
            break
    assert isinstance(descriptor, property)



def test_notation_figurestyle_is_not_abstract():
    assert not inspect.isabstract(notation_FigureStyle)


def test_notation_figurestyle_constructor_exists():
    assert callable(notation_FigureStyle.__init__)


def test_notation_figurestyle_constructor_args():
    sig = inspect.signature(notation_FigureStyle.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "width" in params, "Missing parameter 'width'"
    assert "fillTexture" in params, "Missing parameter 'fillTexture'"
    assert "brightness" in params, "Missing parameter 'brightness'"
    assert "fillColor" in params, "Missing parameter 'fillColor'"
    assert "height" in params, "Missing parameter 'height'"
    assert "fillOrientation" in params, "Missing parameter 'fillOrientation'"
    assert "fillTextureColor" in params, "Missing parameter 'fillTextureColor'"

def test_notation_figurestyle_has_orientation():
    assert hasattr(notation_FigureStyle, "orientation")
    descriptor = None
    for klass in notation_FigureStyle.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)

def test_notation_figurestyle_has_width():
    assert hasattr(notation_FigureStyle, "width")
    descriptor = None
    for klass in notation_FigureStyle.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_notation_figurestyle_has_fillTexture():
    assert hasattr(notation_FigureStyle, "fillTexture")
    descriptor = None
    for klass in notation_FigureStyle.__mro__:
        if "fillTexture" in klass.__dict__:
            descriptor = klass.__dict__["fillTexture"]
            break
    assert isinstance(descriptor, property)

def test_notation_figurestyle_has_brightness():
    assert hasattr(notation_FigureStyle, "brightness")
    descriptor = None
    for klass in notation_FigureStyle.__mro__:
        if "brightness" in klass.__dict__:
            descriptor = klass.__dict__["brightness"]
            break
    assert isinstance(descriptor, property)

def test_notation_figurestyle_has_fillColor():
    assert hasattr(notation_FigureStyle, "fillColor")
    descriptor = None
    for klass in notation_FigureStyle.__mro__:
        if "fillColor" in klass.__dict__:
            descriptor = klass.__dict__["fillColor"]
            break
    assert isinstance(descriptor, property)

def test_notation_figurestyle_has_height():
    assert hasattr(notation_FigureStyle, "height")
    descriptor = None
    for klass in notation_FigureStyle.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_notation_figurestyle_has_fillOrientation():
    assert hasattr(notation_FigureStyle, "fillOrientation")
    descriptor = None
    for klass in notation_FigureStyle.__mro__:
        if "fillOrientation" in klass.__dict__:
            descriptor = klass.__dict__["fillOrientation"]
            break
    assert isinstance(descriptor, property)

def test_notation_figurestyle_has_fillTextureColor():
    assert hasattr(notation_FigureStyle, "fillTextureColor")
    descriptor = None
    for klass in notation_FigureStyle.__mro__:
        if "fillTextureColor" in klass.__dict__:
            descriptor = klass.__dict__["fillTextureColor"]
            break
    assert isinstance(descriptor, property)



def test_notation_figure_is_not_abstract():
    assert not inspect.isabstract(notation_Figure)


def test_notation_figure_constructor_exists():
    assert callable(notation_Figure.__init__)


def test_notation_figure_constructor_args():
    sig = inspect.signature(notation_Figure.__init__)
    params = list(sig.parameters.keys())



def test_notation_linestyle_is_not_abstract():
    assert not inspect.isabstract(notation_LineStyle)


def test_notation_linestyle_constructor_exists():
    assert callable(notation_LineStyle.__init__)


def test_notation_linestyle_constructor_args():
    sig = inspect.signature(notation_LineStyle.__init__)
    params = list(sig.parameters.keys())
    assert "texture" in params, "Missing parameter 'texture'"
    assert "length" in params, "Missing parameter 'length'"
    assert "color" in params, "Missing parameter 'color'"
    assert "thickness" in params, "Missing parameter 'thickness'"
    assert "brightness" in params, "Missing parameter 'brightness'"
    assert "orientation" in params, "Missing parameter 'orientation'"

def test_notation_linestyle_has_texture():
    assert hasattr(notation_LineStyle, "texture")
    descriptor = None
    for klass in notation_LineStyle.__mro__:
        if "texture" in klass.__dict__:
            descriptor = klass.__dict__["texture"]
            break
    assert isinstance(descriptor, property)

def test_notation_linestyle_has_length():
    assert hasattr(notation_LineStyle, "length")
    descriptor = None
    for klass in notation_LineStyle.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_notation_linestyle_has_color():
    assert hasattr(notation_LineStyle, "color")
    descriptor = None
    for klass in notation_LineStyle.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_notation_linestyle_has_thickness():
    assert hasattr(notation_LineStyle, "thickness")
    descriptor = None
    for klass in notation_LineStyle.__mro__:
        if "thickness" in klass.__dict__:
            descriptor = klass.__dict__["thickness"]
            break
    assert isinstance(descriptor, property)

def test_notation_linestyle_has_brightness():
    assert hasattr(notation_LineStyle, "brightness")
    descriptor = None
    for klass in notation_LineStyle.__mro__:
        if "brightness" in klass.__dict__:
            descriptor = klass.__dict__["brightness"]
            break
    assert isinstance(descriptor, property)

def test_notation_linestyle_has_orientation():
    assert hasattr(notation_LineStyle, "orientation")
    descriptor = None
    for klass in notation_LineStyle.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)



def test_notation_line_is_not_abstract():
    assert not inspect.isabstract(notation_Line)


def test_notation_line_constructor_exists():
    assert callable(notation_Line.__init__)


def test_notation_line_constructor_args():
    sig = inspect.signature(notation_Line.__init__)
    params = list(sig.parameters.keys())



def test_diagramelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElement)


def test_diagramelement_constructor_exists():
    assert callable(DiagramElement.__init__)


def test_diagramelement_constructor_args():
    sig = inspect.signature(DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_notation_node_is_not_abstract():
    assert not inspect.isabstract(notation_Node)


def test_notation_node_constructor_exists():
    assert callable(notation_Node.__init__)


def test_notation_node_constructor_args():
    sig = inspect.signature(notation_Node.__init__)
    params = list(sig.parameters.keys())



def test_idelement_is_not_abstract():
    assert not inspect.isabstract(IDElement)


def test_idelement_constructor_exists():
    assert callable(IDElement.__init__)


def test_idelement_constructor_args():
    sig = inspect.signature(IDElement.__init__)
    params = list(sig.parameters.keys())



def test_notation_graphicalelement_is_not_abstract():
    assert not inspect.isabstract(notation_GraphicalElement)


def test_notation_graphicalelement_constructor_exists():
    assert callable(notation_GraphicalElement.__init__)


def test_notation_graphicalelement_constructor_args():
    sig = inspect.signature(notation_GraphicalElement.__init__)
    params = list(sig.parameters.keys())



def test_notation_textualelement_is_not_abstract():
    assert not inspect.isabstract(notation_TextualElement)


def test_notation_textualelement_constructor_exists():
    assert callable(notation_TextualElement.__init__)


def test_notation_textualelement_constructor_args():
    sig = inspect.signature(notation_TextualElement.__init__)
    params = list(sig.parameters.keys())



def test_notation_idelement_is_not_abstract():
    assert not inspect.isabstract(notation_IDElement)


def test_notation_idelement_constructor_exists():
    assert callable(notation_IDElement.__init__)


def test_notation_idelement_constructor_args():
    sig = inspect.signature(notation_IDElement.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_notation_idelement_has_ID():
    assert hasattr(notation_IDElement, "ID")
    descriptor = None
    for klass in notation_IDElement.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_notation_diagramelement_is_not_abstract():
    assert not inspect.isabstract(notation_DiagramElement)


def test_notation_diagramelement_constructor_exists():
    assert callable(notation_DiagramElement.__init__)


def test_notation_diagramelement_constructor_args():
    sig = inspect.signature(notation_DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_notation_diagramdefinition_is_not_abstract():
    assert not inspect.isabstract(notation_DiagramDefinition)


def test_notation_diagramdefinition_constructor_exists():
    assert callable(notation_DiagramDefinition.__init__)


def test_notation_diagramdefinition_constructor_args():
    sig = inspect.signature(notation_DiagramDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "targetedAudience" in params, "Missing parameter 'targetedAudience'"
    assert "Legend" in params, "Missing parameter 'Legend'"
    assert "allowChunks" in params, "Missing parameter 'allowChunks'"
    assert "Level" in params, "Missing parameter 'Level'"

def test_notation_diagramdefinition_has_targetedAudience():
    assert hasattr(notation_DiagramDefinition, "targetedAudience")
    descriptor = None
    for klass in notation_DiagramDefinition.__mro__:
        if "targetedAudience" in klass.__dict__:
            descriptor = klass.__dict__["targetedAudience"]
            break
    assert isinstance(descriptor, property)

def test_notation_diagramdefinition_has_Legend():
    assert hasattr(notation_DiagramDefinition, "Legend")
    descriptor = None
    for klass in notation_DiagramDefinition.__mro__:
        if "Legend" in klass.__dict__:
            descriptor = klass.__dict__["Legend"]
            break
    assert isinstance(descriptor, property)

def test_notation_diagramdefinition_has_allowChunks():
    assert hasattr(notation_DiagramDefinition, "allowChunks")
    descriptor = None
    for klass in notation_DiagramDefinition.__mro__:
        if "allowChunks" in klass.__dict__:
            descriptor = klass.__dict__["allowChunks"]
            break
    assert isinstance(descriptor, property)

def test_notation_diagramdefinition_has_Level():
    assert hasattr(notation_DiagramDefinition, "Level")
    descriptor = None
    for klass in notation_DiagramDefinition.__mro__:
        if "Level" in klass.__dict__:
            descriptor = klass.__dict__["Level"]
            break
    assert isinstance(descriptor, property)



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_notation_link_is_not_abstract():
    assert not inspect.isabstract(notation_Link)


def test_notation_link_constructor_exists():
    assert callable(notation_Link.__init__)


def test_notation_link_constructor_args():
    sig = inspect.signature(notation_Link.__init__)
    params = list(sig.parameters.keys())



def test_notation_compartment_is_not_abstract():
    assert not inspect.isabstract(notation_Compartment)


def test_notation_compartment_constructor_exists():
    assert callable(notation_Compartment.__init__)


def test_notation_compartment_constructor_args():
    sig = inspect.signature(notation_Compartment.__init__)
    params = list(sig.parameters.keys())
    assert "layout" in params, "Missing parameter 'layout'"

def test_notation_compartment_has_layout():
    assert hasattr(notation_Compartment, "layout")
    descriptor = None
    for klass in notation_Compartment.__mro__:
        if "layout" in klass.__dict__:
            descriptor = klass.__dict__["layout"]
            break
    assert isinstance(descriptor, property)



def test_notation_relation_is_not_abstract():
    assert not inspect.isabstract(notation_Relation)


def test_notation_relation_constructor_exists():
    assert callable(notation_Relation.__init__)


def test_notation_relation_constructor_args():
    sig = inspect.signature(notation_Relation.__init__)
    params = list(sig.parameters.keys())



def test_notation_notationdefinition_is_not_abstract():
    assert not inspect.isabstract(notation_NotationDefinition)


def test_notation_notationdefinition_constructor_exists():
    assert callable(notation_NotationDefinition.__init__)


def test_notation_notationdefinition_constructor_args():
    sig = inspect.signature(notation_NotationDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"

def test_notation_notationdefinition_has_Type():
    assert hasattr(notation_NotationDefinition, "Type")
    descriptor = None
    for klass in notation_NotationDefinition.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_layout_exists():
    # Check that the Enumeration exists
    assert Layout is not None

def test_layout_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Layout]
    expected_literals = [
        "UNKNOWN",
        "HORIZONTAL",
        "VERTICAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Layout"

def test_definitiontype_exists():
    # Check that the Enumeration exists
    assert DefinitionType is not None

def test_definitiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DefinitionType]
    expected_literals = [
        "GRAPHICAL",
        "HYBRID",
        "TEXTUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DefinitionType"

def test_orientation_exists():
    # Check that the Enumeration exists
    assert Orientation is not None

def test_orientation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Orientation]
    expected_literals = [
        "RIGHT_DIAGONAL",
        "LEFT_DIAGONAL",
        "HORIZONTAL",
        "VERTICAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Orientation"

def test_audiencetype_exists():
    # Check that the Enumeration exists
    assert AudienceType is not None

def test_audiencetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AudienceType]
    expected_literals = [
        "BOTH",
        "EXPERT",
        "BEGINNER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AudienceType"

def test_filltexturetype_exists():
    # Check that the Enumeration exists
    assert FillTextureType is not None

def test_filltexturetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FillTextureType]
    expected_literals = [
        "STRIP",
        "DASHDOTDOT",
        "NONE",
        "DASHDOT",
        "DOT",
        "DASH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FillTextureType"

def test_linetexturetype_exists():
    # Check that the Enumeration exists
    assert LineTextureType is not None

def test_linetexturetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineTextureType]
    expected_literals = [
        "SOLID",
        "DASH",
        "DASHDOTDOT",
        "DOUBLE",
        "DASHDOT",
        "DOT",
        "INVISIBLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineTextureType"

def test_icontype_exists():
    # Check that the Enumeration exists
    assert IconType is not None

def test_icontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IconType]
    expected_literals = [
        "LETTER",
        "ARROW",
        "CROSS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IconType"

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "LIGHT_GREEN",
        "GREEN",
        "BLACK",
        "GRAY",
        "ORANGE",
        "LIGHT_BLUE",
        "RED",
        "DARK_GREEN",
        "WHITE",
        "YELLOW",
        "CYAN",
        "DARK_GRAY",
        "DARK_BLUE",
        "LIGHT_GRAY",
        "BLUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"


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
notation_Point_strategy = st.builds(
    notation_Point,
    x=
        st.integers(),
    y=
        st.integers()
)
Figure_strategy = st.builds(
    Figure,
)
notation_Roundtangle_strategy = st.builds(
    notation_Roundtangle,
)
notation_Square_strategy = st.builds(
    notation_Square,
)
notation_Triangle_strategy = st.builds(
    notation_Triangle,
)
notation_Circle_strategy = st.builds(
    notation_Circle,
)
notation_Cube_strategy = st.builds(
    notation_Cube,
)
notation_Diamond_strategy = st.builds(
    notation_Diamond,
)
notation_Cylinder_strategy = st.builds(
    notation_Cylinder,
)
notation_Polyline_strategy = st.builds(
    notation_Polyline,
)
notation_Rectangle_strategy = st.builds(
    notation_Rectangle,
)
Style_strategy = st.builds(
    Style,
)
notation_Style_strategy = st.builds(
    notation_Style,
)
Value_strategy = st.builds(
    Value,
)
notation_ReferenceValue_strategy = st.builds(
    notation_ReferenceValue,
)
notation_AttributeValue_strategy = st.builds(
    notation_AttributeValue,
)
TextualElement_strategy = st.builds(
    TextualElement,
)
notation_Value_strategy = st.builds(
    notation_Value,
)
notation_Keyword_strategy = st.builds(
    notation_Keyword,
)
notation_Token_strategy = st.builds(
    notation_Token,
)
notation_TextualContainment_strategy = st.builds(
    notation_TextualContainment,
    layout=
        safe_text
)
notation_TextStyle_strategy = st.builds(
    notation_TextStyle,
    bold=
        st.booleans(),
    underlined=
        st.booleans(),
    fontColor=
        safe_text,
    fontName=
        safe_text,
    fontSize=
        st.integers(),
    italic=
        st.booleans()
)
notation_IconStyle_strategy = st.builds(
    notation_IconStyle,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    color=
        safe_text,
    orientation=
        safe_text,
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    brightness=
        st.integers()
)
notation_FigureContainment_strategy = st.builds(
    notation_FigureContainment,
    layout=
        safe_text
)
GraphicalElement_strategy = st.builds(
    GraphicalElement,
)
notation_Composite_strategy = st.builds(
    notation_Composite,
    layout=
        safe_text
)
notation_Icon_strategy = st.builds(
    notation_Icon,
    iconType=
        safe_text
)
notation_Image_strategy = st.builds(
    notation_Image,
    path=
        safe_text
)
notation_Label_strategy = st.builds(
    notation_Label,
)
notation_SyntaxOf_strategy = st.builds(
    notation_SyntaxOf,
)
notation_BorderStyle_strategy = st.builds(
    notation_BorderStyle,
    thickness=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    color=
        safe_text,
    texture=
        safe_text
)
notation_FigureStyle_strategy = st.builds(
    notation_FigureStyle,
    orientation=
        safe_text,
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    fillTexture=
        safe_text,
    brightness=
        st.integers(),
    fillColor=
        safe_text,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    fillOrientation=
        safe_text,
    fillTextureColor=
        safe_text
)
notation_Figure_strategy = st.builds(
    notation_Figure,
)
notation_LineStyle_strategy = st.builds(
    notation_LineStyle,
    texture=
        safe_text,
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    color=
        safe_text,
    thickness=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    brightness=
        st.integers(),
    orientation=
        safe_text
)
notation_Line_strategy = st.builds(
    notation_Line,
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
notation_Node_strategy = st.builds(
    notation_Node,
)
IDElement_strategy = st.builds(
    IDElement,
)
notation_GraphicalElement_strategy = st.builds(
    notation_GraphicalElement,
)
notation_TextualElement_strategy = st.builds(
    notation_TextualElement,
)
notation_IDElement_strategy = st.builds(
    notation_IDElement,
    ID=
        safe_text
)
notation_DiagramElement_strategy = st.builds(
    notation_DiagramElement,
)
notation_DiagramDefinition_strategy = st.builds(
    notation_DiagramDefinition,
    targetedAudience=
        safe_text,
    Legend=
        safe_text,
    allowChunks=
        st.booleans(),
    Level=
        st.integers()
)
Relation_strategy = st.builds(
    Relation,
)
notation_Link_strategy = st.builds(
    notation_Link,
)
notation_Compartment_strategy = st.builds(
    notation_Compartment,
    layout=
        safe_text
)
notation_Relation_strategy = st.builds(
    notation_Relation,
)
notation_NotationDefinition_strategy = st.builds(
    notation_NotationDefinition,
    Type=
        safe_text
)

@given(instance=notation_Point_strategy)
@settings(max_examples=50)
def test_notation_point_instantiation(instance):
    assert isinstance(instance, notation_Point)



@given(instance=notation_Point_strategy)
def test_notation_point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=notation_Point_strategy)
def test_notation_point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=Figure_strategy)
@settings(max_examples=50)
def test_figure_instantiation(instance):
    assert isinstance(instance, Figure)

@given(instance=notation_Roundtangle_strategy)
@settings(max_examples=50)
def test_notation_roundtangle_instantiation(instance):
    assert isinstance(instance, notation_Roundtangle)

@given(instance=notation_Square_strategy)
@settings(max_examples=50)
def test_notation_square_instantiation(instance):
    assert isinstance(instance, notation_Square)

@given(instance=notation_Triangle_strategy)
@settings(max_examples=50)
def test_notation_triangle_instantiation(instance):
    assert isinstance(instance, notation_Triangle)

@given(instance=notation_Circle_strategy)
@settings(max_examples=50)
def test_notation_circle_instantiation(instance):
    assert isinstance(instance, notation_Circle)

@given(instance=notation_Cube_strategy)
@settings(max_examples=50)
def test_notation_cube_instantiation(instance):
    assert isinstance(instance, notation_Cube)

@given(instance=notation_Diamond_strategy)
@settings(max_examples=50)
def test_notation_diamond_instantiation(instance):
    assert isinstance(instance, notation_Diamond)

@given(instance=notation_Cylinder_strategy)
@settings(max_examples=50)
def test_notation_cylinder_instantiation(instance):
    assert isinstance(instance, notation_Cylinder)

@given(instance=notation_Polyline_strategy)
@settings(max_examples=50)
def test_notation_polyline_instantiation(instance):
    assert isinstance(instance, notation_Polyline)

@given(instance=notation_Rectangle_strategy)
@settings(max_examples=50)
def test_notation_rectangle_instantiation(instance):
    assert isinstance(instance, notation_Rectangle)

@given(instance=Style_strategy)
@settings(max_examples=50)
def test_style_instantiation(instance):
    assert isinstance(instance, Style)

@given(instance=notation_Style_strategy)
@settings(max_examples=50)
def test_notation_style_instantiation(instance):
    assert isinstance(instance, notation_Style)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=notation_ReferenceValue_strategy)
@settings(max_examples=50)
def test_notation_referencevalue_instantiation(instance):
    assert isinstance(instance, notation_ReferenceValue)

@given(instance=notation_AttributeValue_strategy)
@settings(max_examples=50)
def test_notation_attributevalue_instantiation(instance):
    assert isinstance(instance, notation_AttributeValue)

@given(instance=TextualElement_strategy)
@settings(max_examples=50)
def test_textualelement_instantiation(instance):
    assert isinstance(instance, TextualElement)

@given(instance=notation_Value_strategy)
@settings(max_examples=50)
def test_notation_value_instantiation(instance):
    assert isinstance(instance, notation_Value)

@given(instance=notation_Keyword_strategy)
@settings(max_examples=50)
def test_notation_keyword_instantiation(instance):
    assert isinstance(instance, notation_Keyword)

@given(instance=notation_Token_strategy)
@settings(max_examples=50)
def test_notation_token_instantiation(instance):
    assert isinstance(instance, notation_Token)

@given(instance=notation_TextualContainment_strategy)
@settings(max_examples=50)
def test_notation_textualcontainment_instantiation(instance):
    assert isinstance(instance, notation_TextualContainment)



@given(instance=notation_TextualContainment_strategy)
def test_notation_textualcontainment_layout_setter(instance):
    original = instance.layout
    instance.layout = original
    assert instance.layout == original

@given(instance=notation_TextStyle_strategy)
@settings(max_examples=50)
def test_notation_textstyle_instantiation(instance):
    assert isinstance(instance, notation_TextStyle)



@given(instance=notation_TextStyle_strategy)
def test_notation_textstyle_bold_setter(instance):
    original = instance.bold
    instance.bold = original
    assert instance.bold == original



@given(instance=notation_TextStyle_strategy)
def test_notation_textstyle_underlined_setter(instance):
    original = instance.underlined
    instance.underlined = original
    assert instance.underlined == original



@given(instance=notation_TextStyle_strategy)
def test_notation_textstyle_fontColor_setter(instance):
    original = instance.fontColor
    instance.fontColor = original
    assert instance.fontColor == original



@given(instance=notation_TextStyle_strategy)
def test_notation_textstyle_fontName_setter(instance):
    original = instance.fontName
    instance.fontName = original
    assert instance.fontName == original



@given(instance=notation_TextStyle_strategy)
def test_notation_textstyle_fontSize_setter(instance):
    original = instance.fontSize
    instance.fontSize = original
    assert instance.fontSize == original



@given(instance=notation_TextStyle_strategy)
def test_notation_textstyle_italic_setter(instance):
    original = instance.italic
    instance.italic = original
    assert instance.italic == original

@given(instance=notation_IconStyle_strategy)
@settings(max_examples=50)
def test_notation_iconstyle_instantiation(instance):
    assert isinstance(instance, notation_IconStyle)



@given(instance=notation_IconStyle_strategy)
def test_notation_iconstyle_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=notation_IconStyle_strategy)
def test_notation_iconstyle_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=notation_IconStyle_strategy)
def test_notation_iconstyle_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original



@given(instance=notation_IconStyle_strategy)
def test_notation_iconstyle_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=notation_IconStyle_strategy)
def test_notation_iconstyle_brightness_setter(instance):
    original = instance.brightness
    instance.brightness = original
    assert instance.brightness == original

@given(instance=notation_FigureContainment_strategy)
@settings(max_examples=50)
def test_notation_figurecontainment_instantiation(instance):
    assert isinstance(instance, notation_FigureContainment)



@given(instance=notation_FigureContainment_strategy)
def test_notation_figurecontainment_layout_setter(instance):
    original = instance.layout
    instance.layout = original
    assert instance.layout == original

@given(instance=GraphicalElement_strategy)
@settings(max_examples=50)
def test_graphicalelement_instantiation(instance):
    assert isinstance(instance, GraphicalElement)

@given(instance=notation_Composite_strategy)
@settings(max_examples=50)
def test_notation_composite_instantiation(instance):
    assert isinstance(instance, notation_Composite)



@given(instance=notation_Composite_strategy)
def test_notation_composite_layout_setter(instance):
    original = instance.layout
    instance.layout = original
    assert instance.layout == original

@given(instance=notation_Icon_strategy)
@settings(max_examples=50)
def test_notation_icon_instantiation(instance):
    assert isinstance(instance, notation_Icon)



@given(instance=notation_Icon_strategy)
def test_notation_icon_iconType_setter(instance):
    original = instance.iconType
    instance.iconType = original
    assert instance.iconType == original

@given(instance=notation_Image_strategy)
@settings(max_examples=50)
def test_notation_image_instantiation(instance):
    assert isinstance(instance, notation_Image)



@given(instance=notation_Image_strategy)
def test_notation_image_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=notation_Label_strategy)
@settings(max_examples=50)
def test_notation_label_instantiation(instance):
    assert isinstance(instance, notation_Label)

@given(instance=notation_SyntaxOf_strategy)
@settings(max_examples=50)
def test_notation_syntaxof_instantiation(instance):
    assert isinstance(instance, notation_SyntaxOf)

@given(instance=notation_BorderStyle_strategy)
@settings(max_examples=50)
def test_notation_borderstyle_instantiation(instance):
    assert isinstance(instance, notation_BorderStyle)



@given(instance=notation_BorderStyle_strategy)
def test_notation_borderstyle_thickness_setter(instance):
    original = instance.thickness
    instance.thickness = original
    assert instance.thickness == original



@given(instance=notation_BorderStyle_strategy)
def test_notation_borderstyle_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=notation_BorderStyle_strategy)
def test_notation_borderstyle_texture_setter(instance):
    original = instance.texture
    instance.texture = original
    assert instance.texture == original

@given(instance=notation_FigureStyle_strategy)
@settings(max_examples=50)
def test_notation_figurestyle_instantiation(instance):
    assert isinstance(instance, notation_FigureStyle)



@given(instance=notation_FigureStyle_strategy)
def test_notation_figurestyle_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original



@given(instance=notation_FigureStyle_strategy)
def test_notation_figurestyle_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=notation_FigureStyle_strategy)
def test_notation_figurestyle_fillTexture_setter(instance):
    original = instance.fillTexture
    instance.fillTexture = original
    assert instance.fillTexture == original



@given(instance=notation_FigureStyle_strategy)
def test_notation_figurestyle_brightness_setter(instance):
    original = instance.brightness
    instance.brightness = original
    assert instance.brightness == original



@given(instance=notation_FigureStyle_strategy)
def test_notation_figurestyle_fillColor_setter(instance):
    original = instance.fillColor
    instance.fillColor = original
    assert instance.fillColor == original



@given(instance=notation_FigureStyle_strategy)
def test_notation_figurestyle_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=notation_FigureStyle_strategy)
def test_notation_figurestyle_fillOrientation_setter(instance):
    original = instance.fillOrientation
    instance.fillOrientation = original
    assert instance.fillOrientation == original



@given(instance=notation_FigureStyle_strategy)
def test_notation_figurestyle_fillTextureColor_setter(instance):
    original = instance.fillTextureColor
    instance.fillTextureColor = original
    assert instance.fillTextureColor == original

@given(instance=notation_Figure_strategy)
@settings(max_examples=50)
def test_notation_figure_instantiation(instance):
    assert isinstance(instance, notation_Figure)

@given(instance=notation_LineStyle_strategy)
@settings(max_examples=50)
def test_notation_linestyle_instantiation(instance):
    assert isinstance(instance, notation_LineStyle)



@given(instance=notation_LineStyle_strategy)
def test_notation_linestyle_texture_setter(instance):
    original = instance.texture
    instance.texture = original
    assert instance.texture == original



@given(instance=notation_LineStyle_strategy)
def test_notation_linestyle_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=notation_LineStyle_strategy)
def test_notation_linestyle_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=notation_LineStyle_strategy)
def test_notation_linestyle_thickness_setter(instance):
    original = instance.thickness
    instance.thickness = original
    assert instance.thickness == original



@given(instance=notation_LineStyle_strategy)
def test_notation_linestyle_brightness_setter(instance):
    original = instance.brightness
    instance.brightness = original
    assert instance.brightness == original



@given(instance=notation_LineStyle_strategy)
def test_notation_linestyle_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=notation_Line_strategy)
@settings(max_examples=50)
def test_notation_line_instantiation(instance):
    assert isinstance(instance, notation_Line)

@given(instance=DiagramElement_strategy)
@settings(max_examples=50)
def test_diagramelement_instantiation(instance):
    assert isinstance(instance, DiagramElement)

@given(instance=notation_Node_strategy)
@settings(max_examples=50)
def test_notation_node_instantiation(instance):
    assert isinstance(instance, notation_Node)

@given(instance=IDElement_strategy)
@settings(max_examples=50)
def test_idelement_instantiation(instance):
    assert isinstance(instance, IDElement)

@given(instance=notation_GraphicalElement_strategy)
@settings(max_examples=50)
def test_notation_graphicalelement_instantiation(instance):
    assert isinstance(instance, notation_GraphicalElement)

@given(instance=notation_TextualElement_strategy)
@settings(max_examples=50)
def test_notation_textualelement_instantiation(instance):
    assert isinstance(instance, notation_TextualElement)

@given(instance=notation_IDElement_strategy)
@settings(max_examples=50)
def test_notation_idelement_instantiation(instance):
    assert isinstance(instance, notation_IDElement)



@given(instance=notation_IDElement_strategy)
def test_notation_idelement_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=notation_DiagramElement_strategy)
@settings(max_examples=50)
def test_notation_diagramelement_instantiation(instance):
    assert isinstance(instance, notation_DiagramElement)

@given(instance=notation_DiagramDefinition_strategy)
@settings(max_examples=50)
def test_notation_diagramdefinition_instantiation(instance):
    assert isinstance(instance, notation_DiagramDefinition)



@given(instance=notation_DiagramDefinition_strategy)
def test_notation_diagramdefinition_targetedAudience_setter(instance):
    original = instance.targetedAudience
    instance.targetedAudience = original
    assert instance.targetedAudience == original



@given(instance=notation_DiagramDefinition_strategy)
def test_notation_diagramdefinition_Legend_setter(instance):
    original = instance.Legend
    instance.Legend = original
    assert instance.Legend == original



@given(instance=notation_DiagramDefinition_strategy)
def test_notation_diagramdefinition_allowChunks_setter(instance):
    original = instance.allowChunks
    instance.allowChunks = original
    assert instance.allowChunks == original



@given(instance=notation_DiagramDefinition_strategy)
def test_notation_diagramdefinition_Level_setter(instance):
    original = instance.Level
    instance.Level = original
    assert instance.Level == original

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=notation_Link_strategy)
@settings(max_examples=50)
def test_notation_link_instantiation(instance):
    assert isinstance(instance, notation_Link)

@given(instance=notation_Compartment_strategy)
@settings(max_examples=50)
def test_notation_compartment_instantiation(instance):
    assert isinstance(instance, notation_Compartment)



@given(instance=notation_Compartment_strategy)
def test_notation_compartment_layout_setter(instance):
    original = instance.layout
    instance.layout = original
    assert instance.layout == original

@given(instance=notation_Relation_strategy)
@settings(max_examples=50)
def test_notation_relation_instantiation(instance):
    assert isinstance(instance, notation_Relation)

@given(instance=notation_NotationDefinition_strategy)
@settings(max_examples=50)
def test_notation_notationdefinition_instantiation(instance):
    assert isinstance(instance, notation_NotationDefinition)



@given(instance=notation_NotationDefinition_strategy)
def test_notation_notationdefinition_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original
