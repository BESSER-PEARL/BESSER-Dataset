import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    shape_Point,
    shape_CommonLayout,
    shape_CompartmentPolygon,
    shape_CompartmentRoundedRectangle,
    CompartmentShape,
    shape_CompartmentEllipse,
    shape_CompartmentRectangle,
    shape_CompartmentShape,
    shape_Compartment,
    shape_CompartmentInfo,
    Shape,
    shape_Rectangle,
    shape_Polyline,
    shape_RoundedRectangle,
    shape_Polygon,
    shape_Text,
    shape_Ellipse,
    shape_Line,
    shape_TextLayout,
    shape_RoundedRectangleLayout,
    shape_RectangleEllipseLayout,
    shape_PolyLineLayout,
    shape_LineLayout,
    ShapeConnection,
    shape_CDRectangle,
    shape_CDPolygon,
    shape_CDEllipse,
    shape_CDRoundedRectangle,
    shape_CDPolyline,
    shape_CDText,
    shape_CDLine,
    AnchorPositionPos,
    shape_AnchorFixPointPosition,
    shape_AnchorRelativePosition,
    shape_AnchorPositionPos,
    shape_AnchorPosition,
    shape_TextBody,
    AnchorType,
    shape_AnchorManual,
    shape_AnchorPredefinied,
    shape_AnchorType,
    shape_ShapeConnection,
    shape_Anchor,
    shape_Description,
    shape_Shape,
    shape_ShapeLayout,
    shape_PlacingDefinition,
    shape_ShapestyleLayout,
    ShapeContainerElement,
    shape_ShapeDefinition,
    shape_ConnectionDefinition,
    shape_ShapeContainerElement,
    shape_ShapeContainer,
    ConnectionStyle,
    HAlign,
    TextType,
    VAlign,
    CompartmentLayout,
    AnchorPredefiniedEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_shape_point_is_not_abstract():
    assert not inspect.isabstract(shape_Point)


def test_shape_point_constructor_exists():
    assert callable(shape_Point.__init__)


def test_shape_point_constructor_args():
    sig = inspect.signature(shape_Point.__init__)
    params = list(sig.parameters.keys())
    assert "curveAfter" in params, "Missing parameter 'curveAfter'"
    assert "ycor" in params, "Missing parameter 'ycor'"
    assert "curveBefore" in params, "Missing parameter 'curveBefore'"
    assert "xcor" in params, "Missing parameter 'xcor'"

def test_shape_point_has_curveAfter():
    assert hasattr(shape_Point, "curveAfter")
    descriptor = None
    for klass in shape_Point.__mro__:
        if "curveAfter" in klass.__dict__:
            descriptor = klass.__dict__["curveAfter"]
            break
    assert isinstance(descriptor, property)

def test_shape_point_has_ycor():
    assert hasattr(shape_Point, "ycor")
    descriptor = None
    for klass in shape_Point.__mro__:
        if "ycor" in klass.__dict__:
            descriptor = klass.__dict__["ycor"]
            break
    assert isinstance(descriptor, property)

def test_shape_point_has_curveBefore():
    assert hasattr(shape_Point, "curveBefore")
    descriptor = None
    for klass in shape_Point.__mro__:
        if "curveBefore" in klass.__dict__:
            descriptor = klass.__dict__["curveBefore"]
            break
    assert isinstance(descriptor, property)

def test_shape_point_has_xcor():
    assert hasattr(shape_Point, "xcor")
    descriptor = None
    for klass in shape_Point.__mro__:
        if "xcor" in klass.__dict__:
            descriptor = klass.__dict__["xcor"]
            break
    assert isinstance(descriptor, property)



def test_shape_commonlayout_is_not_abstract():
    assert not inspect.isabstract(shape_CommonLayout)


def test_shape_commonlayout_constructor_exists():
    assert callable(shape_CommonLayout.__init__)


def test_shape_commonlayout_constructor_args():
    sig = inspect.signature(shape_CommonLayout.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "xcor" in params, "Missing parameter 'xcor'"
    assert "heigth" in params, "Missing parameter 'heigth'"
    assert "ycor" in params, "Missing parameter 'ycor'"

def test_shape_commonlayout_has_width():
    assert hasattr(shape_CommonLayout, "width")
    descriptor = None
    for klass in shape_CommonLayout.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_shape_commonlayout_has_xcor():
    assert hasattr(shape_CommonLayout, "xcor")
    descriptor = None
    for klass in shape_CommonLayout.__mro__:
        if "xcor" in klass.__dict__:
            descriptor = klass.__dict__["xcor"]
            break
    assert isinstance(descriptor, property)

def test_shape_commonlayout_has_heigth():
    assert hasattr(shape_CommonLayout, "heigth")
    descriptor = None
    for klass in shape_CommonLayout.__mro__:
        if "heigth" in klass.__dict__:
            descriptor = klass.__dict__["heigth"]
            break
    assert isinstance(descriptor, property)

def test_shape_commonlayout_has_ycor():
    assert hasattr(shape_CommonLayout, "ycor")
    descriptor = None
    for klass in shape_CommonLayout.__mro__:
        if "ycor" in klass.__dict__:
            descriptor = klass.__dict__["ycor"]
            break
    assert isinstance(descriptor, property)



def test_shape_compartmentpolygon_is_not_abstract():
    assert not inspect.isabstract(shape_CompartmentPolygon)


def test_shape_compartmentpolygon_constructor_exists():
    assert callable(shape_CompartmentPolygon.__init__)


def test_shape_compartmentpolygon_constructor_args():
    sig = inspect.signature(shape_CompartmentPolygon.__init__)
    params = list(sig.parameters.keys())



def test_shape_compartmentroundedrectangle_is_not_abstract():
    assert not inspect.isabstract(shape_CompartmentRoundedRectangle)


def test_shape_compartmentroundedrectangle_constructor_exists():
    assert callable(shape_CompartmentRoundedRectangle.__init__)


def test_shape_compartmentroundedrectangle_constructor_args():
    sig = inspect.signature(shape_CompartmentRoundedRectangle.__init__)
    params = list(sig.parameters.keys())



def test_compartmentshape_is_not_abstract():
    assert not inspect.isabstract(CompartmentShape)


def test_compartmentshape_constructor_exists():
    assert callable(CompartmentShape.__init__)


def test_compartmentshape_constructor_args():
    sig = inspect.signature(CompartmentShape.__init__)
    params = list(sig.parameters.keys())



def test_shape_compartmentellipse_is_not_abstract():
    assert not inspect.isabstract(shape_CompartmentEllipse)


def test_shape_compartmentellipse_constructor_exists():
    assert callable(shape_CompartmentEllipse.__init__)


def test_shape_compartmentellipse_constructor_args():
    sig = inspect.signature(shape_CompartmentEllipse.__init__)
    params = list(sig.parameters.keys())



def test_shape_compartmentrectangle_is_not_abstract():
    assert not inspect.isabstract(shape_CompartmentRectangle)


def test_shape_compartmentrectangle_constructor_exists():
    assert callable(shape_CompartmentRectangle.__init__)


def test_shape_compartmentrectangle_constructor_args():
    sig = inspect.signature(shape_CompartmentRectangle.__init__)
    params = list(sig.parameters.keys())



def test_shape_compartmentshape_is_not_abstract():
    assert not inspect.isabstract(shape_CompartmentShape)


def test_shape_compartmentshape_constructor_exists():
    assert callable(shape_CompartmentShape.__init__)


def test_shape_compartmentshape_constructor_args():
    sig = inspect.signature(shape_CompartmentShape.__init__)
    params = list(sig.parameters.keys())



def test_shape_compartment_is_not_abstract():
    assert not inspect.isabstract(shape_Compartment)


def test_shape_compartment_constructor_exists():
    assert callable(shape_Compartment.__init__)


def test_shape_compartment_constructor_args():
    sig = inspect.signature(shape_Compartment.__init__)
    params = list(sig.parameters.keys())
    assert "compartmentLayout" in params, "Missing parameter 'compartmentLayout'"

def test_shape_compartment_has_compartmentLayout():
    assert hasattr(shape_Compartment, "compartmentLayout")
    descriptor = None
    for klass in shape_Compartment.__mro__:
        if "compartmentLayout" in klass.__dict__:
            descriptor = klass.__dict__["compartmentLayout"]
            break
    assert isinstance(descriptor, property)



def test_shape_compartmentinfo_is_not_abstract():
    assert not inspect.isabstract(shape_CompartmentInfo)


def test_shape_compartmentinfo_constructor_exists():
    assert callable(shape_CompartmentInfo.__init__)


def test_shape_compartmentinfo_constructor_args():
    sig = inspect.signature(shape_CompartmentInfo.__init__)
    params = list(sig.parameters.keys())
    assert "stretchH" in params, "Missing parameter 'stretchH'"
    assert "spacing" in params, "Missing parameter 'spacing'"
    assert "margin" in params, "Missing parameter 'margin'"
    assert "compartmentLayout" in params, "Missing parameter 'compartmentLayout'"
    assert "invisible" in params, "Missing parameter 'invisible'"
    assert "stretchV" in params, "Missing parameter 'stretchV'"

def test_shape_compartmentinfo_has_stretchH():
    assert hasattr(shape_CompartmentInfo, "stretchH")
    descriptor = None
    for klass in shape_CompartmentInfo.__mro__:
        if "stretchH" in klass.__dict__:
            descriptor = klass.__dict__["stretchH"]
            break
    assert isinstance(descriptor, property)

def test_shape_compartmentinfo_has_spacing():
    assert hasattr(shape_CompartmentInfo, "spacing")
    descriptor = None
    for klass in shape_CompartmentInfo.__mro__:
        if "spacing" in klass.__dict__:
            descriptor = klass.__dict__["spacing"]
            break
    assert isinstance(descriptor, property)

def test_shape_compartmentinfo_has_margin():
    assert hasattr(shape_CompartmentInfo, "margin")
    descriptor = None
    for klass in shape_CompartmentInfo.__mro__:
        if "margin" in klass.__dict__:
            descriptor = klass.__dict__["margin"]
            break
    assert isinstance(descriptor, property)

def test_shape_compartmentinfo_has_compartmentLayout():
    assert hasattr(shape_CompartmentInfo, "compartmentLayout")
    descriptor = None
    for klass in shape_CompartmentInfo.__mro__:
        if "compartmentLayout" in klass.__dict__:
            descriptor = klass.__dict__["compartmentLayout"]
            break
    assert isinstance(descriptor, property)

def test_shape_compartmentinfo_has_invisible():
    assert hasattr(shape_CompartmentInfo, "invisible")
    descriptor = None
    for klass in shape_CompartmentInfo.__mro__:
        if "invisible" in klass.__dict__:
            descriptor = klass.__dict__["invisible"]
            break
    assert isinstance(descriptor, property)

def test_shape_compartmentinfo_has_stretchV():
    assert hasattr(shape_CompartmentInfo, "stretchV")
    descriptor = None
    for klass in shape_CompartmentInfo.__mro__:
        if "stretchV" in klass.__dict__:
            descriptor = klass.__dict__["stretchV"]
            break
    assert isinstance(descriptor, property)



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_shape_rectangle_is_not_abstract():
    assert not inspect.isabstract(shape_Rectangle)


def test_shape_rectangle_constructor_exists():
    assert callable(shape_Rectangle.__init__)


def test_shape_rectangle_constructor_args():
    sig = inspect.signature(shape_Rectangle.__init__)
    params = list(sig.parameters.keys())



def test_shape_polyline_is_not_abstract():
    assert not inspect.isabstract(shape_Polyline)


def test_shape_polyline_constructor_exists():
    assert callable(shape_Polyline.__init__)


def test_shape_polyline_constructor_args():
    sig = inspect.signature(shape_Polyline.__init__)
    params = list(sig.parameters.keys())



def test_shape_roundedrectangle_is_not_abstract():
    assert not inspect.isabstract(shape_RoundedRectangle)


def test_shape_roundedrectangle_constructor_exists():
    assert callable(shape_RoundedRectangle.__init__)


def test_shape_roundedrectangle_constructor_args():
    sig = inspect.signature(shape_RoundedRectangle.__init__)
    params = list(sig.parameters.keys())



def test_shape_polygon_is_not_abstract():
    assert not inspect.isabstract(shape_Polygon)


def test_shape_polygon_constructor_exists():
    assert callable(shape_Polygon.__init__)


def test_shape_polygon_constructor_args():
    sig = inspect.signature(shape_Polygon.__init__)
    params = list(sig.parameters.keys())



def test_shape_text_is_not_abstract():
    assert not inspect.isabstract(shape_Text)


def test_shape_text_constructor_exists():
    assert callable(shape_Text.__init__)


def test_shape_text_constructor_args():
    sig = inspect.signature(shape_Text.__init__)
    params = list(sig.parameters.keys())
    assert "texttype" in params, "Missing parameter 'texttype'"

def test_shape_text_has_texttype():
    assert hasattr(shape_Text, "texttype")
    descriptor = None
    for klass in shape_Text.__mro__:
        if "texttype" in klass.__dict__:
            descriptor = klass.__dict__["texttype"]
            break
    assert isinstance(descriptor, property)



def test_shape_ellipse_is_not_abstract():
    assert not inspect.isabstract(shape_Ellipse)


def test_shape_ellipse_constructor_exists():
    assert callable(shape_Ellipse.__init__)


def test_shape_ellipse_constructor_args():
    sig = inspect.signature(shape_Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_shape_line_is_not_abstract():
    assert not inspect.isabstract(shape_Line)


def test_shape_line_constructor_exists():
    assert callable(shape_Line.__init__)


def test_shape_line_constructor_args():
    sig = inspect.signature(shape_Line.__init__)
    params = list(sig.parameters.keys())



def test_shape_textlayout_is_not_abstract():
    assert not inspect.isabstract(shape_TextLayout)


def test_shape_textlayout_constructor_exists():
    assert callable(shape_TextLayout.__init__)


def test_shape_textlayout_constructor_args():
    sig = inspect.signature(shape_TextLayout.__init__)
    params = list(sig.parameters.keys())
    assert "hAlign" in params, "Missing parameter 'hAlign'"
    assert "vAlign" in params, "Missing parameter 'vAlign'"

def test_shape_textlayout_has_hAlign():
    assert hasattr(shape_TextLayout, "hAlign")
    descriptor = None
    for klass in shape_TextLayout.__mro__:
        if "hAlign" in klass.__dict__:
            descriptor = klass.__dict__["hAlign"]
            break
    assert isinstance(descriptor, property)

def test_shape_textlayout_has_vAlign():
    assert hasattr(shape_TextLayout, "vAlign")
    descriptor = None
    for klass in shape_TextLayout.__mro__:
        if "vAlign" in klass.__dict__:
            descriptor = klass.__dict__["vAlign"]
            break
    assert isinstance(descriptor, property)



def test_shape_roundedrectanglelayout_is_not_abstract():
    assert not inspect.isabstract(shape_RoundedRectangleLayout)


def test_shape_roundedrectanglelayout_constructor_exists():
    assert callable(shape_RoundedRectangleLayout.__init__)


def test_shape_roundedrectanglelayout_constructor_args():
    sig = inspect.signature(shape_RoundedRectangleLayout.__init__)
    params = list(sig.parameters.keys())
    assert "curveWidth" in params, "Missing parameter 'curveWidth'"
    assert "curveHeight" in params, "Missing parameter 'curveHeight'"

def test_shape_roundedrectanglelayout_has_curveWidth():
    assert hasattr(shape_RoundedRectangleLayout, "curveWidth")
    descriptor = None
    for klass in shape_RoundedRectangleLayout.__mro__:
        if "curveWidth" in klass.__dict__:
            descriptor = klass.__dict__["curveWidth"]
            break
    assert isinstance(descriptor, property)

def test_shape_roundedrectanglelayout_has_curveHeight():
    assert hasattr(shape_RoundedRectangleLayout, "curveHeight")
    descriptor = None
    for klass in shape_RoundedRectangleLayout.__mro__:
        if "curveHeight" in klass.__dict__:
            descriptor = klass.__dict__["curveHeight"]
            break
    assert isinstance(descriptor, property)



def test_shape_rectangleellipselayout_is_not_abstract():
    assert not inspect.isabstract(shape_RectangleEllipseLayout)


def test_shape_rectangleellipselayout_constructor_exists():
    assert callable(shape_RectangleEllipseLayout.__init__)


def test_shape_rectangleellipselayout_constructor_args():
    sig = inspect.signature(shape_RectangleEllipseLayout.__init__)
    params = list(sig.parameters.keys())



def test_shape_polylinelayout_is_not_abstract():
    assert not inspect.isabstract(shape_PolyLineLayout)


def test_shape_polylinelayout_constructor_exists():
    assert callable(shape_PolyLineLayout.__init__)


def test_shape_polylinelayout_constructor_args():
    sig = inspect.signature(shape_PolyLineLayout.__init__)
    params = list(sig.parameters.keys())



def test_shape_linelayout_is_not_abstract():
    assert not inspect.isabstract(shape_LineLayout)


def test_shape_linelayout_constructor_exists():
    assert callable(shape_LineLayout.__init__)


def test_shape_linelayout_constructor_args():
    sig = inspect.signature(shape_LineLayout.__init__)
    params = list(sig.parameters.keys())



def test_shapeconnection_is_not_abstract():
    assert not inspect.isabstract(ShapeConnection)


def test_shapeconnection_constructor_exists():
    assert callable(ShapeConnection.__init__)


def test_shapeconnection_constructor_args():
    sig = inspect.signature(ShapeConnection.__init__)
    params = list(sig.parameters.keys())



def test_shape_cdrectangle_is_not_abstract():
    assert not inspect.isabstract(shape_CDRectangle)


def test_shape_cdrectangle_constructor_exists():
    assert callable(shape_CDRectangle.__init__)


def test_shape_cdrectangle_constructor_args():
    sig = inspect.signature(shape_CDRectangle.__init__)
    params = list(sig.parameters.keys())



def test_shape_cdpolygon_is_not_abstract():
    assert not inspect.isabstract(shape_CDPolygon)


def test_shape_cdpolygon_constructor_exists():
    assert callable(shape_CDPolygon.__init__)


def test_shape_cdpolygon_constructor_args():
    sig = inspect.signature(shape_CDPolygon.__init__)
    params = list(sig.parameters.keys())



def test_shape_cdellipse_is_not_abstract():
    assert not inspect.isabstract(shape_CDEllipse)


def test_shape_cdellipse_constructor_exists():
    assert callable(shape_CDEllipse.__init__)


def test_shape_cdellipse_constructor_args():
    sig = inspect.signature(shape_CDEllipse.__init__)
    params = list(sig.parameters.keys())



def test_shape_cdroundedrectangle_is_not_abstract():
    assert not inspect.isabstract(shape_CDRoundedRectangle)


def test_shape_cdroundedrectangle_constructor_exists():
    assert callable(shape_CDRoundedRectangle.__init__)


def test_shape_cdroundedrectangle_constructor_args():
    sig = inspect.signature(shape_CDRoundedRectangle.__init__)
    params = list(sig.parameters.keys())



def test_shape_cdpolyline_is_not_abstract():
    assert not inspect.isabstract(shape_CDPolyline)


def test_shape_cdpolyline_constructor_exists():
    assert callable(shape_CDPolyline.__init__)


def test_shape_cdpolyline_constructor_args():
    sig = inspect.signature(shape_CDPolyline.__init__)
    params = list(sig.parameters.keys())



def test_shape_cdtext_is_not_abstract():
    assert not inspect.isabstract(shape_CDText)


def test_shape_cdtext_constructor_exists():
    assert callable(shape_CDText.__init__)


def test_shape_cdtext_constructor_args():
    sig = inspect.signature(shape_CDText.__init__)
    params = list(sig.parameters.keys())
    assert "texttype" in params, "Missing parameter 'texttype'"

def test_shape_cdtext_has_texttype():
    assert hasattr(shape_CDText, "texttype")
    descriptor = None
    for klass in shape_CDText.__mro__:
        if "texttype" in klass.__dict__:
            descriptor = klass.__dict__["texttype"]
            break
    assert isinstance(descriptor, property)



def test_shape_cdline_is_not_abstract():
    assert not inspect.isabstract(shape_CDLine)


def test_shape_cdline_constructor_exists():
    assert callable(shape_CDLine.__init__)


def test_shape_cdline_constructor_args():
    sig = inspect.signature(shape_CDLine.__init__)
    params = list(sig.parameters.keys())



def test_anchorpositionpos_is_not_abstract():
    assert not inspect.isabstract(AnchorPositionPos)


def test_anchorpositionpos_constructor_exists():
    assert callable(AnchorPositionPos.__init__)


def test_anchorpositionpos_constructor_args():
    sig = inspect.signature(AnchorPositionPos.__init__)
    params = list(sig.parameters.keys())



def test_shape_anchorfixpointposition_is_not_abstract():
    assert not inspect.isabstract(shape_AnchorFixPointPosition)


def test_shape_anchorfixpointposition_constructor_exists():
    assert callable(shape_AnchorFixPointPosition.__init__)


def test_shape_anchorfixpointposition_constructor_args():
    sig = inspect.signature(shape_AnchorFixPointPosition.__init__)
    params = list(sig.parameters.keys())
    assert "ycor" in params, "Missing parameter 'ycor'"
    assert "xcor" in params, "Missing parameter 'xcor'"

def test_shape_anchorfixpointposition_has_ycor():
    assert hasattr(shape_AnchorFixPointPosition, "ycor")
    descriptor = None
    for klass in shape_AnchorFixPointPosition.__mro__:
        if "ycor" in klass.__dict__:
            descriptor = klass.__dict__["ycor"]
            break
    assert isinstance(descriptor, property)

def test_shape_anchorfixpointposition_has_xcor():
    assert hasattr(shape_AnchorFixPointPosition, "xcor")
    descriptor = None
    for klass in shape_AnchorFixPointPosition.__mro__:
        if "xcor" in klass.__dict__:
            descriptor = klass.__dict__["xcor"]
            break
    assert isinstance(descriptor, property)



def test_shape_anchorrelativeposition_is_not_abstract():
    assert not inspect.isabstract(shape_AnchorRelativePosition)


def test_shape_anchorrelativeposition_constructor_exists():
    assert callable(shape_AnchorRelativePosition.__init__)


def test_shape_anchorrelativeposition_constructor_args():
    sig = inspect.signature(shape_AnchorRelativePosition.__init__)
    params = list(sig.parameters.keys())
    assert "xoffset" in params, "Missing parameter 'xoffset'"
    assert "yoffset" in params, "Missing parameter 'yoffset'"

def test_shape_anchorrelativeposition_has_xoffset():
    assert hasattr(shape_AnchorRelativePosition, "xoffset")
    descriptor = None
    for klass in shape_AnchorRelativePosition.__mro__:
        if "xoffset" in klass.__dict__:
            descriptor = klass.__dict__["xoffset"]
            break
    assert isinstance(descriptor, property)

def test_shape_anchorrelativeposition_has_yoffset():
    assert hasattr(shape_AnchorRelativePosition, "yoffset")
    descriptor = None
    for klass in shape_AnchorRelativePosition.__mro__:
        if "yoffset" in klass.__dict__:
            descriptor = klass.__dict__["yoffset"]
            break
    assert isinstance(descriptor, property)



def test_shape_anchorpositionpos_is_not_abstract():
    assert not inspect.isabstract(shape_AnchorPositionPos)


def test_shape_anchorpositionpos_constructor_exists():
    assert callable(shape_AnchorPositionPos.__init__)


def test_shape_anchorpositionpos_constructor_args():
    sig = inspect.signature(shape_AnchorPositionPos.__init__)
    params = list(sig.parameters.keys())



def test_shape_anchorposition_is_not_abstract():
    assert not inspect.isabstract(shape_AnchorPosition)


def test_shape_anchorposition_constructor_exists():
    assert callable(shape_AnchorPosition.__init__)


def test_shape_anchorposition_constructor_args():
    sig = inspect.signature(shape_AnchorPosition.__init__)
    params = list(sig.parameters.keys())



def test_shape_textbody_is_not_abstract():
    assert not inspect.isabstract(shape_TextBody)


def test_shape_textbody_constructor_exists():
    assert callable(shape_TextBody.__init__)


def test_shape_textbody_constructor_args():
    sig = inspect.signature(shape_TextBody.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_shape_textbody_has_value():
    assert hasattr(shape_TextBody, "value")
    descriptor = None
    for klass in shape_TextBody.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_anchortype_is_not_abstract():
    assert not inspect.isabstract(AnchorType)


def test_anchortype_constructor_exists():
    assert callable(AnchorType.__init__)


def test_anchortype_constructor_args():
    sig = inspect.signature(AnchorType.__init__)
    params = list(sig.parameters.keys())



def test_shape_anchormanual_is_not_abstract():
    assert not inspect.isabstract(shape_AnchorManual)


def test_shape_anchormanual_constructor_exists():
    assert callable(shape_AnchorManual.__init__)


def test_shape_anchormanual_constructor_args():
    sig = inspect.signature(shape_AnchorManual.__init__)
    params = list(sig.parameters.keys())



def test_shape_anchorpredefinied_is_not_abstract():
    assert not inspect.isabstract(shape_AnchorPredefinied)


def test_shape_anchorpredefinied_constructor_exists():
    assert callable(shape_AnchorPredefinied.__init__)


def test_shape_anchorpredefinied_constructor_args():
    sig = inspect.signature(shape_AnchorPredefinied.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_shape_anchorpredefinied_has_value():
    assert hasattr(shape_AnchorPredefinied, "value")
    descriptor = None
    for klass in shape_AnchorPredefinied.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_shape_anchortype_is_not_abstract():
    assert not inspect.isabstract(shape_AnchorType)


def test_shape_anchortype_constructor_exists():
    assert callable(shape_AnchorType.__init__)


def test_shape_anchortype_constructor_args():
    sig = inspect.signature(shape_AnchorType.__init__)
    params = list(sig.parameters.keys())



def test_shape_shapeconnection_is_not_abstract():
    assert not inspect.isabstract(shape_ShapeConnection)


def test_shape_shapeconnection_constructor_exists():
    assert callable(shape_ShapeConnection.__init__)


def test_shape_shapeconnection_constructor_args():
    sig = inspect.signature(shape_ShapeConnection.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"

def test_shape_shapeconnection_has_style():
    assert hasattr(shape_ShapeConnection, "style")
    descriptor = None
    for klass in shape_ShapeConnection.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_shape_anchor_is_not_abstract():
    assert not inspect.isabstract(shape_Anchor)


def test_shape_anchor_constructor_exists():
    assert callable(shape_Anchor.__init__)


def test_shape_anchor_constructor_args():
    sig = inspect.signature(shape_Anchor.__init__)
    params = list(sig.parameters.keys())



def test_shape_description_is_not_abstract():
    assert not inspect.isabstract(shape_Description)


def test_shape_description_constructor_exists():
    assert callable(shape_Description.__init__)


def test_shape_description_constructor_args():
    sig = inspect.signature(shape_Description.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "hAlign" in params, "Missing parameter 'hAlign'"
    assert "vAlign" in params, "Missing parameter 'vAlign'"

def test_shape_description_has_style():
    assert hasattr(shape_Description, "style")
    descriptor = None
    for klass in shape_Description.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_shape_description_has_hAlign():
    assert hasattr(shape_Description, "hAlign")
    descriptor = None
    for klass in shape_Description.__mro__:
        if "hAlign" in klass.__dict__:
            descriptor = klass.__dict__["hAlign"]
            break
    assert isinstance(descriptor, property)

def test_shape_description_has_vAlign():
    assert hasattr(shape_Description, "vAlign")
    descriptor = None
    for klass in shape_Description.__mro__:
        if "vAlign" in klass.__dict__:
            descriptor = klass.__dict__["vAlign"]
            break
    assert isinstance(descriptor, property)



def test_shape_shape_is_not_abstract():
    assert not inspect.isabstract(shape_Shape)


def test_shape_shape_constructor_exists():
    assert callable(shape_Shape.__init__)


def test_shape_shape_constructor_args():
    sig = inspect.signature(shape_Shape.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"

def test_shape_shape_has_style():
    assert hasattr(shape_Shape, "style")
    descriptor = None
    for klass in shape_Shape.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_shape_shapelayout_is_not_abstract():
    assert not inspect.isabstract(shape_ShapeLayout)


def test_shape_shapelayout_constructor_exists():
    assert callable(shape_ShapeLayout.__init__)


def test_shape_shapelayout_constructor_args():
    sig = inspect.signature(shape_ShapeLayout.__init__)
    params = list(sig.parameters.keys())
    assert "minheight" in params, "Missing parameter 'minheight'"
    assert "stretchV" in params, "Missing parameter 'stretchV'"
    assert "proportional" in params, "Missing parameter 'proportional'"
    assert "maxheight" in params, "Missing parameter 'maxheight'"
    assert "minwidth" in params, "Missing parameter 'minwidth'"
    assert "stretchH" in params, "Missing parameter 'stretchH'"
    assert "maxwidth" in params, "Missing parameter 'maxwidth'"

def test_shape_shapelayout_has_minheight():
    assert hasattr(shape_ShapeLayout, "minheight")
    descriptor = None
    for klass in shape_ShapeLayout.__mro__:
        if "minheight" in klass.__dict__:
            descriptor = klass.__dict__["minheight"]
            break
    assert isinstance(descriptor, property)

def test_shape_shapelayout_has_stretchV():
    assert hasattr(shape_ShapeLayout, "stretchV")
    descriptor = None
    for klass in shape_ShapeLayout.__mro__:
        if "stretchV" in klass.__dict__:
            descriptor = klass.__dict__["stretchV"]
            break
    assert isinstance(descriptor, property)

def test_shape_shapelayout_has_proportional():
    assert hasattr(shape_ShapeLayout, "proportional")
    descriptor = None
    for klass in shape_ShapeLayout.__mro__:
        if "proportional" in klass.__dict__:
            descriptor = klass.__dict__["proportional"]
            break
    assert isinstance(descriptor, property)

def test_shape_shapelayout_has_maxheight():
    assert hasattr(shape_ShapeLayout, "maxheight")
    descriptor = None
    for klass in shape_ShapeLayout.__mro__:
        if "maxheight" in klass.__dict__:
            descriptor = klass.__dict__["maxheight"]
            break
    assert isinstance(descriptor, property)

def test_shape_shapelayout_has_minwidth():
    assert hasattr(shape_ShapeLayout, "minwidth")
    descriptor = None
    for klass in shape_ShapeLayout.__mro__:
        if "minwidth" in klass.__dict__:
            descriptor = klass.__dict__["minwidth"]
            break
    assert isinstance(descriptor, property)

def test_shape_shapelayout_has_stretchH():
    assert hasattr(shape_ShapeLayout, "stretchH")
    descriptor = None
    for klass in shape_ShapeLayout.__mro__:
        if "stretchH" in klass.__dict__:
            descriptor = klass.__dict__["stretchH"]
            break
    assert isinstance(descriptor, property)

def test_shape_shapelayout_has_maxwidth():
    assert hasattr(shape_ShapeLayout, "maxwidth")
    descriptor = None
    for klass in shape_ShapeLayout.__mro__:
        if "maxwidth" in klass.__dict__:
            descriptor = klass.__dict__["maxwidth"]
            break
    assert isinstance(descriptor, property)



def test_shape_placingdefinition_is_not_abstract():
    assert not inspect.isabstract(shape_PlacingDefinition)


def test_shape_placingdefinition_constructor_exists():
    assert callable(shape_PlacingDefinition.__init__)


def test_shape_placingdefinition_constructor_args():
    sig = inspect.signature(shape_PlacingDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"
    assert "distance" in params, "Missing parameter 'distance'"
    assert "offset" in params, "Missing parameter 'offset'"

def test_shape_placingdefinition_has_angle():
    assert hasattr(shape_PlacingDefinition, "angle")
    descriptor = None
    for klass in shape_PlacingDefinition.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)

def test_shape_placingdefinition_has_distance():
    assert hasattr(shape_PlacingDefinition, "distance")
    descriptor = None
    for klass in shape_PlacingDefinition.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)

def test_shape_placingdefinition_has_offset():
    assert hasattr(shape_PlacingDefinition, "offset")
    descriptor = None
    for klass in shape_PlacingDefinition.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)



def test_shape_shapestylelayout_is_not_abstract():
    assert not inspect.isabstract(shape_ShapestyleLayout)


def test_shape_shapestylelayout_constructor_exists():
    assert callable(shape_ShapestyleLayout.__init__)


def test_shape_shapestylelayout_constructor_args():
    sig = inspect.signature(shape_ShapestyleLayout.__init__)
    params = list(sig.parameters.keys())



def test_shapecontainerelement_is_not_abstract():
    assert not inspect.isabstract(ShapeContainerElement)


def test_shapecontainerelement_constructor_exists():
    assert callable(ShapeContainerElement.__init__)


def test_shapecontainerelement_constructor_args():
    sig = inspect.signature(ShapeContainerElement.__init__)
    params = list(sig.parameters.keys())



def test_shape_shapedefinition_is_not_abstract():
    assert not inspect.isabstract(shape_ShapeDefinition)


def test_shape_shapedefinition_constructor_exists():
    assert callable(shape_ShapeDefinition.__init__)


def test_shape_shapedefinition_constructor_args():
    sig = inspect.signature(shape_ShapeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_shape_connectiondefinition_is_not_abstract():
    assert not inspect.isabstract(shape_ConnectionDefinition)


def test_shape_connectiondefinition_constructor_exists():
    assert callable(shape_ConnectionDefinition.__init__)


def test_shape_connectiondefinition_constructor_args():
    sig = inspect.signature(shape_ConnectionDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "connectionStyle" in params, "Missing parameter 'connectionStyle'"

def test_shape_connectiondefinition_has_connectionStyle():
    assert hasattr(shape_ConnectionDefinition, "connectionStyle")
    descriptor = None
    for klass in shape_ConnectionDefinition.__mro__:
        if "connectionStyle" in klass.__dict__:
            descriptor = klass.__dict__["connectionStyle"]
            break
    assert isinstance(descriptor, property)



def test_shape_shapecontainerelement_is_not_abstract():
    assert not inspect.isabstract(shape_ShapeContainerElement)


def test_shape_shapecontainerelement_constructor_exists():
    assert callable(shape_ShapeContainerElement.__init__)


def test_shape_shapecontainerelement_constructor_args():
    sig = inspect.signature(shape_ShapeContainerElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "style" in params, "Missing parameter 'style'"

def test_shape_shapecontainerelement_has_name():
    assert hasattr(shape_ShapeContainerElement, "name")
    descriptor = None
    for klass in shape_ShapeContainerElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_shape_shapecontainerelement_has_style():
    assert hasattr(shape_ShapeContainerElement, "style")
    descriptor = None
    for klass in shape_ShapeContainerElement.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_shape_shapecontainer_is_not_abstract():
    assert not inspect.isabstract(shape_ShapeContainer)


def test_shape_shapecontainer_constructor_exists():
    assert callable(shape_ShapeContainer.__init__)


def test_shape_shapecontainer_constructor_args():
    sig = inspect.signature(shape_ShapeContainer.__init__)
    params = list(sig.parameters.keys())

def test_connectionstyle_exists():
    # Check that the Enumeration exists
    assert ConnectionStyle is not None

def test_connectionstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConnectionStyle]
    expected_literals = [
        "freeform",
        "manhatten",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConnectionStyle"

def test_halign_exists():
    # Check that the Enumeration exists
    assert HAlign is not None

def test_halign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HAlign]
    expected_literals = [
        "CENTER",
        "RIGHT",
        "LEFT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HAlign"

def test_texttype_exists():
    # Check that the Enumeration exists
    assert TextType is not None

def test_texttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextType]
    expected_literals = [
        "multiline",
        "default",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextType"

def test_valign_exists():
    # Check that the Enumeration exists
    assert VAlign is not None

def test_valign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VAlign]
    expected_literals = [
        "BOTTOM",
        "TOP",
        "MIDDLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VAlign"

def test_compartmentlayout_exists():
    # Check that the Enumeration exists
    assert CompartmentLayout is not None

def test_compartmentlayout_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CompartmentLayout]
    expected_literals = [
        "FIXED",
        "VERTICAL",
        "FIT",
        "HORIZONTAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CompartmentLayout"

def test_anchorpredefiniedenum_exists():
    # Check that the Enumeration exists
    assert AnchorPredefiniedEnum is not None

def test_anchorpredefiniedenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AnchorPredefiniedEnum]
    expected_literals = [
        "center",
        "corners",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AnchorPredefiniedEnum"


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
shape_Point_strategy = st.builds(
    shape_Point,
    curveAfter=
        st.integers(),
    ycor=
        safe_text,
    curveBefore=
        st.integers(),
    xcor=
        safe_text
)
shape_CommonLayout_strategy = st.builds(
    shape_CommonLayout,
    width=
        st.integers(),
    xcor=
        st.integers(),
    heigth=
        st.integers(),
    ycor=
        st.integers()
)
shape_CompartmentPolygon_strategy = st.builds(
    shape_CompartmentPolygon,
)
shape_CompartmentRoundedRectangle_strategy = st.builds(
    shape_CompartmentRoundedRectangle,
)
CompartmentShape_strategy = st.builds(
    CompartmentShape,
)
shape_CompartmentEllipse_strategy = st.builds(
    shape_CompartmentEllipse,
)
shape_CompartmentRectangle_strategy = st.builds(
    shape_CompartmentRectangle,
)
shape_CompartmentShape_strategy = st.builds(
    shape_CompartmentShape,
)
shape_Compartment_strategy = st.builds(
    shape_Compartment,
    compartmentLayout=
        safe_text
)
shape_CompartmentInfo_strategy = st.builds(
    shape_CompartmentInfo,
    stretchH=
        safe_text,
    spacing=
        st.integers(),
    margin=
        st.integers(),
    compartmentLayout=
        safe_text,
    invisible=
        st.booleans(),
    stretchV=
        safe_text
)
Shape_strategy = st.builds(
    Shape,
)
shape_Rectangle_strategy = st.builds(
    shape_Rectangle,
)
shape_Polyline_strategy = st.builds(
    shape_Polyline,
)
shape_RoundedRectangle_strategy = st.builds(
    shape_RoundedRectangle,
)
shape_Polygon_strategy = st.builds(
    shape_Polygon,
)
shape_Text_strategy = st.builds(
    shape_Text,
    texttype=
        safe_text
)
shape_Ellipse_strategy = st.builds(
    shape_Ellipse,
)
shape_Line_strategy = st.builds(
    shape_Line,
)
shape_TextLayout_strategy = st.builds(
    shape_TextLayout,
    hAlign=
        safe_text,
    vAlign=
        safe_text
)
shape_RoundedRectangleLayout_strategy = st.builds(
    shape_RoundedRectangleLayout,
    curveWidth=
        st.integers(),
    curveHeight=
        st.integers()
)
shape_RectangleEllipseLayout_strategy = st.builds(
    shape_RectangleEllipseLayout,
)
shape_PolyLineLayout_strategy = st.builds(
    shape_PolyLineLayout,
)
shape_LineLayout_strategy = st.builds(
    shape_LineLayout,
)
ShapeConnection_strategy = st.builds(
    ShapeConnection,
)
shape_CDRectangle_strategy = st.builds(
    shape_CDRectangle,
)
shape_CDPolygon_strategy = st.builds(
    shape_CDPolygon,
)
shape_CDEllipse_strategy = st.builds(
    shape_CDEllipse,
)
shape_CDRoundedRectangle_strategy = st.builds(
    shape_CDRoundedRectangle,
)
shape_CDPolyline_strategy = st.builds(
    shape_CDPolyline,
)
shape_CDText_strategy = st.builds(
    shape_CDText,
    texttype=
        safe_text
)
shape_CDLine_strategy = st.builds(
    shape_CDLine,
)
AnchorPositionPos_strategy = st.builds(
    AnchorPositionPos,
)
shape_AnchorFixPointPosition_strategy = st.builds(
    shape_AnchorFixPointPosition,
    ycor=
        st.integers(),
    xcor=
        st.integers()
)
shape_AnchorRelativePosition_strategy = st.builds(
    shape_AnchorRelativePosition,
    xoffset=
        safe_text,
    yoffset=
        safe_text
)
shape_AnchorPositionPos_strategy = st.builds(
    shape_AnchorPositionPos,
)
shape_AnchorPosition_strategy = st.builds(
    shape_AnchorPosition,
)
shape_TextBody_strategy = st.builds(
    shape_TextBody,
    value=
        safe_text
)
AnchorType_strategy = st.builds(
    AnchorType,
)
shape_AnchorManual_strategy = st.builds(
    shape_AnchorManual,
)
shape_AnchorPredefinied_strategy = st.builds(
    shape_AnchorPredefinied,
    value=
        safe_text
)
shape_AnchorType_strategy = st.builds(
    shape_AnchorType,
)
shape_ShapeConnection_strategy = st.builds(
    shape_ShapeConnection,
    style=
        safe_text
)
shape_Anchor_strategy = st.builds(
    shape_Anchor,
)
shape_Description_strategy = st.builds(
    shape_Description,
    style=
        safe_text,
    hAlign=
        safe_text,
    vAlign=
        safe_text
)
shape_Shape_strategy = st.builds(
    shape_Shape,
    style=
        safe_text
)
shape_ShapeLayout_strategy = st.builds(
    shape_ShapeLayout,
    minheight=
        st.integers(),
    stretchV=
        safe_text,
    proportional=
        safe_text,
    maxheight=
        st.integers(),
    minwidth=
        st.integers(),
    stretchH=
        safe_text,
    maxwidth=
        st.integers()
)
shape_PlacingDefinition_strategy = st.builds(
    shape_PlacingDefinition,
    angle=
        st.integers(),
    distance=
        st.integers(),
    offset=
        safe_text
)
shape_ShapestyleLayout_strategy = st.builds(
    shape_ShapestyleLayout,
)
ShapeContainerElement_strategy = st.builds(
    ShapeContainerElement,
)
shape_ShapeDefinition_strategy = st.builds(
    shape_ShapeDefinition,
)
shape_ConnectionDefinition_strategy = st.builds(
    shape_ConnectionDefinition,
    connectionStyle=
        safe_text
)
shape_ShapeContainerElement_strategy = st.builds(
    shape_ShapeContainerElement,
    name=
        safe_text,
    style=
        safe_text
)
shape_ShapeContainer_strategy = st.builds(
    shape_ShapeContainer,
)

@given(instance=shape_Point_strategy)
@settings(max_examples=50)
def test_shape_point_instantiation(instance):
    assert isinstance(instance, shape_Point)



@given(instance=shape_Point_strategy)
def test_shape_point_curveAfter_setter(instance):
    original = instance.curveAfter
    instance.curveAfter = original
    assert instance.curveAfter == original



@given(instance=shape_Point_strategy)
def test_shape_point_ycor_setter(instance):
    original = instance.ycor
    instance.ycor = original
    assert instance.ycor == original



@given(instance=shape_Point_strategy)
def test_shape_point_curveBefore_setter(instance):
    original = instance.curveBefore
    instance.curveBefore = original
    assert instance.curveBefore == original



@given(instance=shape_Point_strategy)
def test_shape_point_xcor_setter(instance):
    original = instance.xcor
    instance.xcor = original
    assert instance.xcor == original

@given(instance=shape_CommonLayout_strategy)
@settings(max_examples=50)
def test_shape_commonlayout_instantiation(instance):
    assert isinstance(instance, shape_CommonLayout)



@given(instance=shape_CommonLayout_strategy)
def test_shape_commonlayout_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=shape_CommonLayout_strategy)
def test_shape_commonlayout_xcor_setter(instance):
    original = instance.xcor
    instance.xcor = original
    assert instance.xcor == original



@given(instance=shape_CommonLayout_strategy)
def test_shape_commonlayout_heigth_setter(instance):
    original = instance.heigth
    instance.heigth = original
    assert instance.heigth == original



@given(instance=shape_CommonLayout_strategy)
def test_shape_commonlayout_ycor_setter(instance):
    original = instance.ycor
    instance.ycor = original
    assert instance.ycor == original

@given(instance=shape_CompartmentPolygon_strategy)
@settings(max_examples=50)
def test_shape_compartmentpolygon_instantiation(instance):
    assert isinstance(instance, shape_CompartmentPolygon)

@given(instance=shape_CompartmentRoundedRectangle_strategy)
@settings(max_examples=50)
def test_shape_compartmentroundedrectangle_instantiation(instance):
    assert isinstance(instance, shape_CompartmentRoundedRectangle)

@given(instance=CompartmentShape_strategy)
@settings(max_examples=50)
def test_compartmentshape_instantiation(instance):
    assert isinstance(instance, CompartmentShape)

@given(instance=shape_CompartmentEllipse_strategy)
@settings(max_examples=50)
def test_shape_compartmentellipse_instantiation(instance):
    assert isinstance(instance, shape_CompartmentEllipse)

@given(instance=shape_CompartmentRectangle_strategy)
@settings(max_examples=50)
def test_shape_compartmentrectangle_instantiation(instance):
    assert isinstance(instance, shape_CompartmentRectangle)

@given(instance=shape_CompartmentShape_strategy)
@settings(max_examples=50)
def test_shape_compartmentshape_instantiation(instance):
    assert isinstance(instance, shape_CompartmentShape)

@given(instance=shape_Compartment_strategy)
@settings(max_examples=50)
def test_shape_compartment_instantiation(instance):
    assert isinstance(instance, shape_Compartment)



@given(instance=shape_Compartment_strategy)
def test_shape_compartment_compartmentLayout_setter(instance):
    original = instance.compartmentLayout
    instance.compartmentLayout = original
    assert instance.compartmentLayout == original

@given(instance=shape_CompartmentInfo_strategy)
@settings(max_examples=50)
def test_shape_compartmentinfo_instantiation(instance):
    assert isinstance(instance, shape_CompartmentInfo)



@given(instance=shape_CompartmentInfo_strategy)
def test_shape_compartmentinfo_stretchH_setter(instance):
    original = instance.stretchH
    instance.stretchH = original
    assert instance.stretchH == original



@given(instance=shape_CompartmentInfo_strategy)
def test_shape_compartmentinfo_spacing_setter(instance):
    original = instance.spacing
    instance.spacing = original
    assert instance.spacing == original



@given(instance=shape_CompartmentInfo_strategy)
def test_shape_compartmentinfo_margin_setter(instance):
    original = instance.margin
    instance.margin = original
    assert instance.margin == original



@given(instance=shape_CompartmentInfo_strategy)
def test_shape_compartmentinfo_compartmentLayout_setter(instance):
    original = instance.compartmentLayout
    instance.compartmentLayout = original
    assert instance.compartmentLayout == original



@given(instance=shape_CompartmentInfo_strategy)
def test_shape_compartmentinfo_invisible_setter(instance):
    original = instance.invisible
    instance.invisible = original
    assert instance.invisible == original



@given(instance=shape_CompartmentInfo_strategy)
def test_shape_compartmentinfo_stretchV_setter(instance):
    original = instance.stretchV
    instance.stretchV = original
    assert instance.stretchV == original

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=shape_Rectangle_strategy)
@settings(max_examples=50)
def test_shape_rectangle_instantiation(instance):
    assert isinstance(instance, shape_Rectangle)

@given(instance=shape_Polyline_strategy)
@settings(max_examples=50)
def test_shape_polyline_instantiation(instance):
    assert isinstance(instance, shape_Polyline)

@given(instance=shape_RoundedRectangle_strategy)
@settings(max_examples=50)
def test_shape_roundedrectangle_instantiation(instance):
    assert isinstance(instance, shape_RoundedRectangle)

@given(instance=shape_Polygon_strategy)
@settings(max_examples=50)
def test_shape_polygon_instantiation(instance):
    assert isinstance(instance, shape_Polygon)

@given(instance=shape_Text_strategy)
@settings(max_examples=50)
def test_shape_text_instantiation(instance):
    assert isinstance(instance, shape_Text)



@given(instance=shape_Text_strategy)
def test_shape_text_texttype_setter(instance):
    original = instance.texttype
    instance.texttype = original
    assert instance.texttype == original

@given(instance=shape_Ellipse_strategy)
@settings(max_examples=50)
def test_shape_ellipse_instantiation(instance):
    assert isinstance(instance, shape_Ellipse)

@given(instance=shape_Line_strategy)
@settings(max_examples=50)
def test_shape_line_instantiation(instance):
    assert isinstance(instance, shape_Line)

@given(instance=shape_TextLayout_strategy)
@settings(max_examples=50)
def test_shape_textlayout_instantiation(instance):
    assert isinstance(instance, shape_TextLayout)



@given(instance=shape_TextLayout_strategy)
def test_shape_textlayout_hAlign_setter(instance):
    original = instance.hAlign
    instance.hAlign = original
    assert instance.hAlign == original



@given(instance=shape_TextLayout_strategy)
def test_shape_textlayout_vAlign_setter(instance):
    original = instance.vAlign
    instance.vAlign = original
    assert instance.vAlign == original

@given(instance=shape_RoundedRectangleLayout_strategy)
@settings(max_examples=50)
def test_shape_roundedrectanglelayout_instantiation(instance):
    assert isinstance(instance, shape_RoundedRectangleLayout)



@given(instance=shape_RoundedRectangleLayout_strategy)
def test_shape_roundedrectanglelayout_curveWidth_setter(instance):
    original = instance.curveWidth
    instance.curveWidth = original
    assert instance.curveWidth == original



@given(instance=shape_RoundedRectangleLayout_strategy)
def test_shape_roundedrectanglelayout_curveHeight_setter(instance):
    original = instance.curveHeight
    instance.curveHeight = original
    assert instance.curveHeight == original

@given(instance=shape_RectangleEllipseLayout_strategy)
@settings(max_examples=50)
def test_shape_rectangleellipselayout_instantiation(instance):
    assert isinstance(instance, shape_RectangleEllipseLayout)

@given(instance=shape_PolyLineLayout_strategy)
@settings(max_examples=50)
def test_shape_polylinelayout_instantiation(instance):
    assert isinstance(instance, shape_PolyLineLayout)

@given(instance=shape_LineLayout_strategy)
@settings(max_examples=50)
def test_shape_linelayout_instantiation(instance):
    assert isinstance(instance, shape_LineLayout)

@given(instance=ShapeConnection_strategy)
@settings(max_examples=50)
def test_shapeconnection_instantiation(instance):
    assert isinstance(instance, ShapeConnection)

@given(instance=shape_CDRectangle_strategy)
@settings(max_examples=50)
def test_shape_cdrectangle_instantiation(instance):
    assert isinstance(instance, shape_CDRectangle)

@given(instance=shape_CDPolygon_strategy)
@settings(max_examples=50)
def test_shape_cdpolygon_instantiation(instance):
    assert isinstance(instance, shape_CDPolygon)

@given(instance=shape_CDEllipse_strategy)
@settings(max_examples=50)
def test_shape_cdellipse_instantiation(instance):
    assert isinstance(instance, shape_CDEllipse)

@given(instance=shape_CDRoundedRectangle_strategy)
@settings(max_examples=50)
def test_shape_cdroundedrectangle_instantiation(instance):
    assert isinstance(instance, shape_CDRoundedRectangle)

@given(instance=shape_CDPolyline_strategy)
@settings(max_examples=50)
def test_shape_cdpolyline_instantiation(instance):
    assert isinstance(instance, shape_CDPolyline)

@given(instance=shape_CDText_strategy)
@settings(max_examples=50)
def test_shape_cdtext_instantiation(instance):
    assert isinstance(instance, shape_CDText)



@given(instance=shape_CDText_strategy)
def test_shape_cdtext_texttype_setter(instance):
    original = instance.texttype
    instance.texttype = original
    assert instance.texttype == original

@given(instance=shape_CDLine_strategy)
@settings(max_examples=50)
def test_shape_cdline_instantiation(instance):
    assert isinstance(instance, shape_CDLine)

@given(instance=AnchorPositionPos_strategy)
@settings(max_examples=50)
def test_anchorpositionpos_instantiation(instance):
    assert isinstance(instance, AnchorPositionPos)

@given(instance=shape_AnchorFixPointPosition_strategy)
@settings(max_examples=50)
def test_shape_anchorfixpointposition_instantiation(instance):
    assert isinstance(instance, shape_AnchorFixPointPosition)



@given(instance=shape_AnchorFixPointPosition_strategy)
def test_shape_anchorfixpointposition_ycor_setter(instance):
    original = instance.ycor
    instance.ycor = original
    assert instance.ycor == original



@given(instance=shape_AnchorFixPointPosition_strategy)
def test_shape_anchorfixpointposition_xcor_setter(instance):
    original = instance.xcor
    instance.xcor = original
    assert instance.xcor == original

@given(instance=shape_AnchorRelativePosition_strategy)
@settings(max_examples=50)
def test_shape_anchorrelativeposition_instantiation(instance):
    assert isinstance(instance, shape_AnchorRelativePosition)



@given(instance=shape_AnchorRelativePosition_strategy)
def test_shape_anchorrelativeposition_xoffset_setter(instance):
    original = instance.xoffset
    instance.xoffset = original
    assert instance.xoffset == original



@given(instance=shape_AnchorRelativePosition_strategy)
def test_shape_anchorrelativeposition_yoffset_setter(instance):
    original = instance.yoffset
    instance.yoffset = original
    assert instance.yoffset == original

@given(instance=shape_AnchorPositionPos_strategy)
@settings(max_examples=50)
def test_shape_anchorpositionpos_instantiation(instance):
    assert isinstance(instance, shape_AnchorPositionPos)

@given(instance=shape_AnchorPosition_strategy)
@settings(max_examples=50)
def test_shape_anchorposition_instantiation(instance):
    assert isinstance(instance, shape_AnchorPosition)

@given(instance=shape_TextBody_strategy)
@settings(max_examples=50)
def test_shape_textbody_instantiation(instance):
    assert isinstance(instance, shape_TextBody)



@given(instance=shape_TextBody_strategy)
def test_shape_textbody_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=AnchorType_strategy)
@settings(max_examples=50)
def test_anchortype_instantiation(instance):
    assert isinstance(instance, AnchorType)

@given(instance=shape_AnchorManual_strategy)
@settings(max_examples=50)
def test_shape_anchormanual_instantiation(instance):
    assert isinstance(instance, shape_AnchorManual)

@given(instance=shape_AnchorPredefinied_strategy)
@settings(max_examples=50)
def test_shape_anchorpredefinied_instantiation(instance):
    assert isinstance(instance, shape_AnchorPredefinied)



@given(instance=shape_AnchorPredefinied_strategy)
def test_shape_anchorpredefinied_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=shape_AnchorType_strategy)
@settings(max_examples=50)
def test_shape_anchortype_instantiation(instance):
    assert isinstance(instance, shape_AnchorType)

@given(instance=shape_ShapeConnection_strategy)
@settings(max_examples=50)
def test_shape_shapeconnection_instantiation(instance):
    assert isinstance(instance, shape_ShapeConnection)



@given(instance=shape_ShapeConnection_strategy)
def test_shape_shapeconnection_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=shape_Anchor_strategy)
@settings(max_examples=50)
def test_shape_anchor_instantiation(instance):
    assert isinstance(instance, shape_Anchor)

@given(instance=shape_Description_strategy)
@settings(max_examples=50)
def test_shape_description_instantiation(instance):
    assert isinstance(instance, shape_Description)



@given(instance=shape_Description_strategy)
def test_shape_description_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=shape_Description_strategy)
def test_shape_description_hAlign_setter(instance):
    original = instance.hAlign
    instance.hAlign = original
    assert instance.hAlign == original



@given(instance=shape_Description_strategy)
def test_shape_description_vAlign_setter(instance):
    original = instance.vAlign
    instance.vAlign = original
    assert instance.vAlign == original

@given(instance=shape_Shape_strategy)
@settings(max_examples=50)
def test_shape_shape_instantiation(instance):
    assert isinstance(instance, shape_Shape)



@given(instance=shape_Shape_strategy)
def test_shape_shape_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=shape_ShapeLayout_strategy)
@settings(max_examples=50)
def test_shape_shapelayout_instantiation(instance):
    assert isinstance(instance, shape_ShapeLayout)



@given(instance=shape_ShapeLayout_strategy)
def test_shape_shapelayout_minheight_setter(instance):
    original = instance.minheight
    instance.minheight = original
    assert instance.minheight == original



@given(instance=shape_ShapeLayout_strategy)
def test_shape_shapelayout_stretchV_setter(instance):
    original = instance.stretchV
    instance.stretchV = original
    assert instance.stretchV == original



@given(instance=shape_ShapeLayout_strategy)
def test_shape_shapelayout_proportional_setter(instance):
    original = instance.proportional
    instance.proportional = original
    assert instance.proportional == original



@given(instance=shape_ShapeLayout_strategy)
def test_shape_shapelayout_maxheight_setter(instance):
    original = instance.maxheight
    instance.maxheight = original
    assert instance.maxheight == original



@given(instance=shape_ShapeLayout_strategy)
def test_shape_shapelayout_minwidth_setter(instance):
    original = instance.minwidth
    instance.minwidth = original
    assert instance.minwidth == original



@given(instance=shape_ShapeLayout_strategy)
def test_shape_shapelayout_stretchH_setter(instance):
    original = instance.stretchH
    instance.stretchH = original
    assert instance.stretchH == original



@given(instance=shape_ShapeLayout_strategy)
def test_shape_shapelayout_maxwidth_setter(instance):
    original = instance.maxwidth
    instance.maxwidth = original
    assert instance.maxwidth == original

@given(instance=shape_PlacingDefinition_strategy)
@settings(max_examples=50)
def test_shape_placingdefinition_instantiation(instance):
    assert isinstance(instance, shape_PlacingDefinition)



@given(instance=shape_PlacingDefinition_strategy)
def test_shape_placingdefinition_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original



@given(instance=shape_PlacingDefinition_strategy)
def test_shape_placingdefinition_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original



@given(instance=shape_PlacingDefinition_strategy)
def test_shape_placingdefinition_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=shape_ShapestyleLayout_strategy)
@settings(max_examples=50)
def test_shape_shapestylelayout_instantiation(instance):
    assert isinstance(instance, shape_ShapestyleLayout)

@given(instance=ShapeContainerElement_strategy)
@settings(max_examples=50)
def test_shapecontainerelement_instantiation(instance):
    assert isinstance(instance, ShapeContainerElement)

@given(instance=shape_ShapeDefinition_strategy)
@settings(max_examples=50)
def test_shape_shapedefinition_instantiation(instance):
    assert isinstance(instance, shape_ShapeDefinition)

@given(instance=shape_ConnectionDefinition_strategy)
@settings(max_examples=50)
def test_shape_connectiondefinition_instantiation(instance):
    assert isinstance(instance, shape_ConnectionDefinition)



@given(instance=shape_ConnectionDefinition_strategy)
def test_shape_connectiondefinition_connectionStyle_setter(instance):
    original = instance.connectionStyle
    instance.connectionStyle = original
    assert instance.connectionStyle == original

@given(instance=shape_ShapeContainerElement_strategy)
@settings(max_examples=50)
def test_shape_shapecontainerelement_instantiation(instance):
    assert isinstance(instance, shape_ShapeContainerElement)



@given(instance=shape_ShapeContainerElement_strategy)
def test_shape_shapecontainerelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=shape_ShapeContainerElement_strategy)
def test_shape_shapecontainerelement_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=shape_ShapeContainer_strategy)
@settings(max_examples=50)
def test_shape_shapecontainer_instantiation(instance):
    assert isinstance(instance, shape_ShapeContainer)
