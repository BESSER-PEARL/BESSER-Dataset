import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    shape::Point,
    shape::CommonLayout,
    shape::CompartmentPolygon,
    shape::CompartmentRoundedRectangle,
    CompartmentShape,
    shape::CompartmentEllipse,
    shape::CompartmentRectangle,
    shape::CompartmentShape,
    shape::Compartment,
    shape::CompartmentInfo,
    Shape,
    shape::Polyline,
    shape::Polygon,
    shape::RoundedRectangle,
    shape::Text,
    shape::Rectangle,
    shape::Ellipse,
    shape::Line,
    shape::TextLayout,
    shape::RoundedRectangleLayout,
    shape::RectangleEllipseLayout,
    shape::PolyLineLayout,
    shape::LineLayout,
    ShapeConnection,
    shape::CDRectangle,
    shape::CDPolyline,
    shape::CDText,
    shape::CDPolygon,
    shape::CDEllipse,
    shape::CDRoundedRectangle,
    shape::CDLine,
    AnchorPositionPos,
    shape::AnchorFixPointPosition,
    shape::AnchorRelativePosition,
    shape::AnchorPositionPos,
    shape::AnchorPosition,
    shape::TextBody,
    AnchorType,
    shape::AnchorManual,
    shape::AnchorPredefinied,
    shape::AnchorType,
    shape::ShapeConnection,
    shape::Anchor,
    shape::Description,
    shape::Shape,
    shape::ShapeLayout,
    shape::PlacingDefinition,
    shape::ShapestyleLayout,
    ShapeContainerElement,
    shape::ShapeDefinition,
    shape::ConnectionDefinition,
    shape::ShapeContainerElement,
    shape::ShapeContainer,
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



def test_shape::point_is_not_abstract():
    assert not inspect.isabstract(shape::Point)


def test_shape::point_constructor_exists():
    assert callable(shape::Point.__init__)


def test_shape::point_constructor_args():
    sig = inspect.signature(shape::Point.__init__)
    params = list(sig.parameters.keys())
    assert "curveAfter" in params, "Missing parameter 'curveAfter'"
    assert "curveBefore" in params, "Missing parameter 'curveBefore'"
    assert "xcor" in params, "Missing parameter 'xcor'"
    assert "ycor" in params, "Missing parameter 'ycor'"

def test_shape::point_has_curveAfter():
    assert hasattr(shape::Point, "curveAfter")
    descriptor = None
    for klass in shape::Point.__mro__:
        if "curveAfter" in klass.__dict__:
            descriptor = klass.__dict__["curveAfter"]
            break
    assert isinstance(descriptor, property)

def test_shape::point_has_curveBefore():
    assert hasattr(shape::Point, "curveBefore")
    descriptor = None
    for klass in shape::Point.__mro__:
        if "curveBefore" in klass.__dict__:
            descriptor = klass.__dict__["curveBefore"]
            break
    assert isinstance(descriptor, property)

def test_shape::point_has_xcor():
    assert hasattr(shape::Point, "xcor")
    descriptor = None
    for klass in shape::Point.__mro__:
        if "xcor" in klass.__dict__:
            descriptor = klass.__dict__["xcor"]
            break
    assert isinstance(descriptor, property)

def test_shape::point_has_ycor():
    assert hasattr(shape::Point, "ycor")
    descriptor = None
    for klass in shape::Point.__mro__:
        if "ycor" in klass.__dict__:
            descriptor = klass.__dict__["ycor"]
            break
    assert isinstance(descriptor, property)



def test_shape::commonlayout_is_not_abstract():
    assert not inspect.isabstract(shape::CommonLayout)


def test_shape::commonlayout_constructor_exists():
    assert callable(shape::CommonLayout.__init__)


def test_shape::commonlayout_constructor_args():
    sig = inspect.signature(shape::CommonLayout.__init__)
    params = list(sig.parameters.keys())
    assert "ycor" in params, "Missing parameter 'ycor'"
    assert "xcor" in params, "Missing parameter 'xcor'"
    assert "width" in params, "Missing parameter 'width'"
    assert "heigth" in params, "Missing parameter 'heigth'"

def test_shape::commonlayout_has_ycor():
    assert hasattr(shape::CommonLayout, "ycor")
    descriptor = None
    for klass in shape::CommonLayout.__mro__:
        if "ycor" in klass.__dict__:
            descriptor = klass.__dict__["ycor"]
            break
    assert isinstance(descriptor, property)

def test_shape::commonlayout_has_xcor():
    assert hasattr(shape::CommonLayout, "xcor")
    descriptor = None
    for klass in shape::CommonLayout.__mro__:
        if "xcor" in klass.__dict__:
            descriptor = klass.__dict__["xcor"]
            break
    assert isinstance(descriptor, property)

def test_shape::commonlayout_has_width():
    assert hasattr(shape::CommonLayout, "width")
    descriptor = None
    for klass in shape::CommonLayout.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_shape::commonlayout_has_heigth():
    assert hasattr(shape::CommonLayout, "heigth")
    descriptor = None
    for klass in shape::CommonLayout.__mro__:
        if "heigth" in klass.__dict__:
            descriptor = klass.__dict__["heigth"]
            break
    assert isinstance(descriptor, property)



def test_shape::compartmentpolygon_is_not_abstract():
    assert not inspect.isabstract(shape::CompartmentPolygon)


def test_shape::compartmentpolygon_constructor_exists():
    assert callable(shape::CompartmentPolygon.__init__)


def test_shape::compartmentpolygon_constructor_args():
    sig = inspect.signature(shape::CompartmentPolygon.__init__)
    params = list(sig.parameters.keys())



def test_shape::compartmentroundedrectangle_is_not_abstract():
    assert not inspect.isabstract(shape::CompartmentRoundedRectangle)


def test_shape::compartmentroundedrectangle_constructor_exists():
    assert callable(shape::CompartmentRoundedRectangle.__init__)


def test_shape::compartmentroundedrectangle_constructor_args():
    sig = inspect.signature(shape::CompartmentRoundedRectangle.__init__)
    params = list(sig.parameters.keys())



def test_compartmentshape_is_not_abstract():
    assert not inspect.isabstract(CompartmentShape)


def test_compartmentshape_constructor_exists():
    assert callable(CompartmentShape.__init__)


def test_compartmentshape_constructor_args():
    sig = inspect.signature(CompartmentShape.__init__)
    params = list(sig.parameters.keys())



def test_shape::compartmentellipse_is_not_abstract():
    assert not inspect.isabstract(shape::CompartmentEllipse)


def test_shape::compartmentellipse_constructor_exists():
    assert callable(shape::CompartmentEllipse.__init__)


def test_shape::compartmentellipse_constructor_args():
    sig = inspect.signature(shape::CompartmentEllipse.__init__)
    params = list(sig.parameters.keys())



def test_shape::compartmentrectangle_is_not_abstract():
    assert not inspect.isabstract(shape::CompartmentRectangle)


def test_shape::compartmentrectangle_constructor_exists():
    assert callable(shape::CompartmentRectangle.__init__)


def test_shape::compartmentrectangle_constructor_args():
    sig = inspect.signature(shape::CompartmentRectangle.__init__)
    params = list(sig.parameters.keys())



def test_shape::compartmentshape_is_not_abstract():
    assert not inspect.isabstract(shape::CompartmentShape)


def test_shape::compartmentshape_constructor_exists():
    assert callable(shape::CompartmentShape.__init__)


def test_shape::compartmentshape_constructor_args():
    sig = inspect.signature(shape::CompartmentShape.__init__)
    params = list(sig.parameters.keys())



def test_shape::compartment_is_not_abstract():
    assert not inspect.isabstract(shape::Compartment)


def test_shape::compartment_constructor_exists():
    assert callable(shape::Compartment.__init__)


def test_shape::compartment_constructor_args():
    sig = inspect.signature(shape::Compartment.__init__)
    params = list(sig.parameters.keys())
    assert "compartmentLayout" in params, "Missing parameter 'compartmentLayout'"

def test_shape::compartment_has_compartmentLayout():
    assert hasattr(shape::Compartment, "compartmentLayout")
    descriptor = None
    for klass in shape::Compartment.__mro__:
        if "compartmentLayout" in klass.__dict__:
            descriptor = klass.__dict__["compartmentLayout"]
            break
    assert isinstance(descriptor, property)



def test_shape::compartmentinfo_is_not_abstract():
    assert not inspect.isabstract(shape::CompartmentInfo)


def test_shape::compartmentinfo_constructor_exists():
    assert callable(shape::CompartmentInfo.__init__)


def test_shape::compartmentinfo_constructor_args():
    sig = inspect.signature(shape::CompartmentInfo.__init__)
    params = list(sig.parameters.keys())
    assert "compartmentLayout" in params, "Missing parameter 'compartmentLayout'"
    assert "margin" in params, "Missing parameter 'margin'"
    assert "stretchV" in params, "Missing parameter 'stretchV'"
    assert "stretchH" in params, "Missing parameter 'stretchH'"
    assert "spacing" in params, "Missing parameter 'spacing'"
    assert "invisible" in params, "Missing parameter 'invisible'"

def test_shape::compartmentinfo_has_compartmentLayout():
    assert hasattr(shape::CompartmentInfo, "compartmentLayout")
    descriptor = None
    for klass in shape::CompartmentInfo.__mro__:
        if "compartmentLayout" in klass.__dict__:
            descriptor = klass.__dict__["compartmentLayout"]
            break
    assert isinstance(descriptor, property)

def test_shape::compartmentinfo_has_margin():
    assert hasattr(shape::CompartmentInfo, "margin")
    descriptor = None
    for klass in shape::CompartmentInfo.__mro__:
        if "margin" in klass.__dict__:
            descriptor = klass.__dict__["margin"]
            break
    assert isinstance(descriptor, property)

def test_shape::compartmentinfo_has_stretchV():
    assert hasattr(shape::CompartmentInfo, "stretchV")
    descriptor = None
    for klass in shape::CompartmentInfo.__mro__:
        if "stretchV" in klass.__dict__:
            descriptor = klass.__dict__["stretchV"]
            break
    assert isinstance(descriptor, property)

def test_shape::compartmentinfo_has_stretchH():
    assert hasattr(shape::CompartmentInfo, "stretchH")
    descriptor = None
    for klass in shape::CompartmentInfo.__mro__:
        if "stretchH" in klass.__dict__:
            descriptor = klass.__dict__["stretchH"]
            break
    assert isinstance(descriptor, property)

def test_shape::compartmentinfo_has_spacing():
    assert hasattr(shape::CompartmentInfo, "spacing")
    descriptor = None
    for klass in shape::CompartmentInfo.__mro__:
        if "spacing" in klass.__dict__:
            descriptor = klass.__dict__["spacing"]
            break
    assert isinstance(descriptor, property)

def test_shape::compartmentinfo_has_invisible():
    assert hasattr(shape::CompartmentInfo, "invisible")
    descriptor = None
    for klass in shape::CompartmentInfo.__mro__:
        if "invisible" in klass.__dict__:
            descriptor = klass.__dict__["invisible"]
            break
    assert isinstance(descriptor, property)



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_shape::polyline_is_not_abstract():
    assert not inspect.isabstract(shape::Polyline)


def test_shape::polyline_constructor_exists():
    assert callable(shape::Polyline.__init__)


def test_shape::polyline_constructor_args():
    sig = inspect.signature(shape::Polyline.__init__)
    params = list(sig.parameters.keys())



def test_shape::polygon_is_not_abstract():
    assert not inspect.isabstract(shape::Polygon)


def test_shape::polygon_constructor_exists():
    assert callable(shape::Polygon.__init__)


def test_shape::polygon_constructor_args():
    sig = inspect.signature(shape::Polygon.__init__)
    params = list(sig.parameters.keys())



def test_shape::roundedrectangle_is_not_abstract():
    assert not inspect.isabstract(shape::RoundedRectangle)


def test_shape::roundedrectangle_constructor_exists():
    assert callable(shape::RoundedRectangle.__init__)


def test_shape::roundedrectangle_constructor_args():
    sig = inspect.signature(shape::RoundedRectangle.__init__)
    params = list(sig.parameters.keys())



def test_shape::text_is_not_abstract():
    assert not inspect.isabstract(shape::Text)


def test_shape::text_constructor_exists():
    assert callable(shape::Text.__init__)


def test_shape::text_constructor_args():
    sig = inspect.signature(shape::Text.__init__)
    params = list(sig.parameters.keys())
    assert "texttype" in params, "Missing parameter 'texttype'"

def test_shape::text_has_texttype():
    assert hasattr(shape::Text, "texttype")
    descriptor = None
    for klass in shape::Text.__mro__:
        if "texttype" in klass.__dict__:
            descriptor = klass.__dict__["texttype"]
            break
    assert isinstance(descriptor, property)



def test_shape::rectangle_is_not_abstract():
    assert not inspect.isabstract(shape::Rectangle)


def test_shape::rectangle_constructor_exists():
    assert callable(shape::Rectangle.__init__)


def test_shape::rectangle_constructor_args():
    sig = inspect.signature(shape::Rectangle.__init__)
    params = list(sig.parameters.keys())



def test_shape::ellipse_is_not_abstract():
    assert not inspect.isabstract(shape::Ellipse)


def test_shape::ellipse_constructor_exists():
    assert callable(shape::Ellipse.__init__)


def test_shape::ellipse_constructor_args():
    sig = inspect.signature(shape::Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_shape::line_is_not_abstract():
    assert not inspect.isabstract(shape::Line)


def test_shape::line_constructor_exists():
    assert callable(shape::Line.__init__)


def test_shape::line_constructor_args():
    sig = inspect.signature(shape::Line.__init__)
    params = list(sig.parameters.keys())



def test_shape::textlayout_is_not_abstract():
    assert not inspect.isabstract(shape::TextLayout)


def test_shape::textlayout_constructor_exists():
    assert callable(shape::TextLayout.__init__)


def test_shape::textlayout_constructor_args():
    sig = inspect.signature(shape::TextLayout.__init__)
    params = list(sig.parameters.keys())
    assert "hAlign" in params, "Missing parameter 'hAlign'"
    assert "vAlign" in params, "Missing parameter 'vAlign'"

def test_shape::textlayout_has_hAlign():
    assert hasattr(shape::TextLayout, "hAlign")
    descriptor = None
    for klass in shape::TextLayout.__mro__:
        if "hAlign" in klass.__dict__:
            descriptor = klass.__dict__["hAlign"]
            break
    assert isinstance(descriptor, property)

def test_shape::textlayout_has_vAlign():
    assert hasattr(shape::TextLayout, "vAlign")
    descriptor = None
    for klass in shape::TextLayout.__mro__:
        if "vAlign" in klass.__dict__:
            descriptor = klass.__dict__["vAlign"]
            break
    assert isinstance(descriptor, property)



def test_shape::roundedrectanglelayout_is_not_abstract():
    assert not inspect.isabstract(shape::RoundedRectangleLayout)


def test_shape::roundedrectanglelayout_constructor_exists():
    assert callable(shape::RoundedRectangleLayout.__init__)


def test_shape::roundedrectanglelayout_constructor_args():
    sig = inspect.signature(shape::RoundedRectangleLayout.__init__)
    params = list(sig.parameters.keys())
    assert "curveHeight" in params, "Missing parameter 'curveHeight'"
    assert "curveWidth" in params, "Missing parameter 'curveWidth'"

def test_shape::roundedrectanglelayout_has_curveHeight():
    assert hasattr(shape::RoundedRectangleLayout, "curveHeight")
    descriptor = None
    for klass in shape::RoundedRectangleLayout.__mro__:
        if "curveHeight" in klass.__dict__:
            descriptor = klass.__dict__["curveHeight"]
            break
    assert isinstance(descriptor, property)

def test_shape::roundedrectanglelayout_has_curveWidth():
    assert hasattr(shape::RoundedRectangleLayout, "curveWidth")
    descriptor = None
    for klass in shape::RoundedRectangleLayout.__mro__:
        if "curveWidth" in klass.__dict__:
            descriptor = klass.__dict__["curveWidth"]
            break
    assert isinstance(descriptor, property)



def test_shape::rectangleellipselayout_is_not_abstract():
    assert not inspect.isabstract(shape::RectangleEllipseLayout)


def test_shape::rectangleellipselayout_constructor_exists():
    assert callable(shape::RectangleEllipseLayout.__init__)


def test_shape::rectangleellipselayout_constructor_args():
    sig = inspect.signature(shape::RectangleEllipseLayout.__init__)
    params = list(sig.parameters.keys())



def test_shape::polylinelayout_is_not_abstract():
    assert not inspect.isabstract(shape::PolyLineLayout)


def test_shape::polylinelayout_constructor_exists():
    assert callable(shape::PolyLineLayout.__init__)


def test_shape::polylinelayout_constructor_args():
    sig = inspect.signature(shape::PolyLineLayout.__init__)
    params = list(sig.parameters.keys())



def test_shape::linelayout_is_not_abstract():
    assert not inspect.isabstract(shape::LineLayout)


def test_shape::linelayout_constructor_exists():
    assert callable(shape::LineLayout.__init__)


def test_shape::linelayout_constructor_args():
    sig = inspect.signature(shape::LineLayout.__init__)
    params = list(sig.parameters.keys())



def test_shapeconnection_is_not_abstract():
    assert not inspect.isabstract(ShapeConnection)


def test_shapeconnection_constructor_exists():
    assert callable(ShapeConnection.__init__)


def test_shapeconnection_constructor_args():
    sig = inspect.signature(ShapeConnection.__init__)
    params = list(sig.parameters.keys())



def test_shape::cdrectangle_is_not_abstract():
    assert not inspect.isabstract(shape::CDRectangle)


def test_shape::cdrectangle_constructor_exists():
    assert callable(shape::CDRectangle.__init__)


def test_shape::cdrectangle_constructor_args():
    sig = inspect.signature(shape::CDRectangle.__init__)
    params = list(sig.parameters.keys())



def test_shape::cdpolyline_is_not_abstract():
    assert not inspect.isabstract(shape::CDPolyline)


def test_shape::cdpolyline_constructor_exists():
    assert callable(shape::CDPolyline.__init__)


def test_shape::cdpolyline_constructor_args():
    sig = inspect.signature(shape::CDPolyline.__init__)
    params = list(sig.parameters.keys())



def test_shape::cdtext_is_not_abstract():
    assert not inspect.isabstract(shape::CDText)


def test_shape::cdtext_constructor_exists():
    assert callable(shape::CDText.__init__)


def test_shape::cdtext_constructor_args():
    sig = inspect.signature(shape::CDText.__init__)
    params = list(sig.parameters.keys())
    assert "texttype" in params, "Missing parameter 'texttype'"

def test_shape::cdtext_has_texttype():
    assert hasattr(shape::CDText, "texttype")
    descriptor = None
    for klass in shape::CDText.__mro__:
        if "texttype" in klass.__dict__:
            descriptor = klass.__dict__["texttype"]
            break
    assert isinstance(descriptor, property)



def test_shape::cdpolygon_is_not_abstract():
    assert not inspect.isabstract(shape::CDPolygon)


def test_shape::cdpolygon_constructor_exists():
    assert callable(shape::CDPolygon.__init__)


def test_shape::cdpolygon_constructor_args():
    sig = inspect.signature(shape::CDPolygon.__init__)
    params = list(sig.parameters.keys())



def test_shape::cdellipse_is_not_abstract():
    assert not inspect.isabstract(shape::CDEllipse)


def test_shape::cdellipse_constructor_exists():
    assert callable(shape::CDEllipse.__init__)


def test_shape::cdellipse_constructor_args():
    sig = inspect.signature(shape::CDEllipse.__init__)
    params = list(sig.parameters.keys())



def test_shape::cdroundedrectangle_is_not_abstract():
    assert not inspect.isabstract(shape::CDRoundedRectangle)


def test_shape::cdroundedrectangle_constructor_exists():
    assert callable(shape::CDRoundedRectangle.__init__)


def test_shape::cdroundedrectangle_constructor_args():
    sig = inspect.signature(shape::CDRoundedRectangle.__init__)
    params = list(sig.parameters.keys())



def test_shape::cdline_is_not_abstract():
    assert not inspect.isabstract(shape::CDLine)


def test_shape::cdline_constructor_exists():
    assert callable(shape::CDLine.__init__)


def test_shape::cdline_constructor_args():
    sig = inspect.signature(shape::CDLine.__init__)
    params = list(sig.parameters.keys())



def test_anchorpositionpos_is_not_abstract():
    assert not inspect.isabstract(AnchorPositionPos)


def test_anchorpositionpos_constructor_exists():
    assert callable(AnchorPositionPos.__init__)


def test_anchorpositionpos_constructor_args():
    sig = inspect.signature(AnchorPositionPos.__init__)
    params = list(sig.parameters.keys())



def test_shape::anchorfixpointposition_is_not_abstract():
    assert not inspect.isabstract(shape::AnchorFixPointPosition)


def test_shape::anchorfixpointposition_constructor_exists():
    assert callable(shape::AnchorFixPointPosition.__init__)


def test_shape::anchorfixpointposition_constructor_args():
    sig = inspect.signature(shape::AnchorFixPointPosition.__init__)
    params = list(sig.parameters.keys())
    assert "ycor" in params, "Missing parameter 'ycor'"
    assert "xcor" in params, "Missing parameter 'xcor'"

def test_shape::anchorfixpointposition_has_ycor():
    assert hasattr(shape::AnchorFixPointPosition, "ycor")
    descriptor = None
    for klass in shape::AnchorFixPointPosition.__mro__:
        if "ycor" in klass.__dict__:
            descriptor = klass.__dict__["ycor"]
            break
    assert isinstance(descriptor, property)

def test_shape::anchorfixpointposition_has_xcor():
    assert hasattr(shape::AnchorFixPointPosition, "xcor")
    descriptor = None
    for klass in shape::AnchorFixPointPosition.__mro__:
        if "xcor" in klass.__dict__:
            descriptor = klass.__dict__["xcor"]
            break
    assert isinstance(descriptor, property)



def test_shape::anchorrelativeposition_is_not_abstract():
    assert not inspect.isabstract(shape::AnchorRelativePosition)


def test_shape::anchorrelativeposition_constructor_exists():
    assert callable(shape::AnchorRelativePosition.__init__)


def test_shape::anchorrelativeposition_constructor_args():
    sig = inspect.signature(shape::AnchorRelativePosition.__init__)
    params = list(sig.parameters.keys())
    assert "xoffset" in params, "Missing parameter 'xoffset'"
    assert "yoffset" in params, "Missing parameter 'yoffset'"

def test_shape::anchorrelativeposition_has_xoffset():
    assert hasattr(shape::AnchorRelativePosition, "xoffset")
    descriptor = None
    for klass in shape::AnchorRelativePosition.__mro__:
        if "xoffset" in klass.__dict__:
            descriptor = klass.__dict__["xoffset"]
            break
    assert isinstance(descriptor, property)

def test_shape::anchorrelativeposition_has_yoffset():
    assert hasattr(shape::AnchorRelativePosition, "yoffset")
    descriptor = None
    for klass in shape::AnchorRelativePosition.__mro__:
        if "yoffset" in klass.__dict__:
            descriptor = klass.__dict__["yoffset"]
            break
    assert isinstance(descriptor, property)



def test_shape::anchorpositionpos_is_not_abstract():
    assert not inspect.isabstract(shape::AnchorPositionPos)


def test_shape::anchorpositionpos_constructor_exists():
    assert callable(shape::AnchorPositionPos.__init__)


def test_shape::anchorpositionpos_constructor_args():
    sig = inspect.signature(shape::AnchorPositionPos.__init__)
    params = list(sig.parameters.keys())



def test_shape::anchorposition_is_not_abstract():
    assert not inspect.isabstract(shape::AnchorPosition)


def test_shape::anchorposition_constructor_exists():
    assert callable(shape::AnchorPosition.__init__)


def test_shape::anchorposition_constructor_args():
    sig = inspect.signature(shape::AnchorPosition.__init__)
    params = list(sig.parameters.keys())



def test_shape::textbody_is_not_abstract():
    assert not inspect.isabstract(shape::TextBody)


def test_shape::textbody_constructor_exists():
    assert callable(shape::TextBody.__init__)


def test_shape::textbody_constructor_args():
    sig = inspect.signature(shape::TextBody.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_shape::textbody_has_value():
    assert hasattr(shape::TextBody, "value")
    descriptor = None
    for klass in shape::TextBody.__mro__:
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



def test_shape::anchormanual_is_not_abstract():
    assert not inspect.isabstract(shape::AnchorManual)


def test_shape::anchormanual_constructor_exists():
    assert callable(shape::AnchorManual.__init__)


def test_shape::anchormanual_constructor_args():
    sig = inspect.signature(shape::AnchorManual.__init__)
    params = list(sig.parameters.keys())



def test_shape::anchorpredefinied_is_not_abstract():
    assert not inspect.isabstract(shape::AnchorPredefinied)


def test_shape::anchorpredefinied_constructor_exists():
    assert callable(shape::AnchorPredefinied.__init__)


def test_shape::anchorpredefinied_constructor_args():
    sig = inspect.signature(shape::AnchorPredefinied.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_shape::anchorpredefinied_has_value():
    assert hasattr(shape::AnchorPredefinied, "value")
    descriptor = None
    for klass in shape::AnchorPredefinied.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_shape::anchortype_is_not_abstract():
    assert not inspect.isabstract(shape::AnchorType)


def test_shape::anchortype_constructor_exists():
    assert callable(shape::AnchorType.__init__)


def test_shape::anchortype_constructor_args():
    sig = inspect.signature(shape::AnchorType.__init__)
    params = list(sig.parameters.keys())



def test_shape::shapeconnection_is_not_abstract():
    assert not inspect.isabstract(shape::ShapeConnection)


def test_shape::shapeconnection_constructor_exists():
    assert callable(shape::ShapeConnection.__init__)


def test_shape::shapeconnection_constructor_args():
    sig = inspect.signature(shape::ShapeConnection.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"

def test_shape::shapeconnection_has_style():
    assert hasattr(shape::ShapeConnection, "style")
    descriptor = None
    for klass in shape::ShapeConnection.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_shape::anchor_is_not_abstract():
    assert not inspect.isabstract(shape::Anchor)


def test_shape::anchor_constructor_exists():
    assert callable(shape::Anchor.__init__)


def test_shape::anchor_constructor_args():
    sig = inspect.signature(shape::Anchor.__init__)
    params = list(sig.parameters.keys())



def test_shape::description_is_not_abstract():
    assert not inspect.isabstract(shape::Description)


def test_shape::description_constructor_exists():
    assert callable(shape::Description.__init__)


def test_shape::description_constructor_args():
    sig = inspect.signature(shape::Description.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "vAlign" in params, "Missing parameter 'vAlign'"
    assert "hAlign" in params, "Missing parameter 'hAlign'"

def test_shape::description_has_style():
    assert hasattr(shape::Description, "style")
    descriptor = None
    for klass in shape::Description.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_shape::description_has_vAlign():
    assert hasattr(shape::Description, "vAlign")
    descriptor = None
    for klass in shape::Description.__mro__:
        if "vAlign" in klass.__dict__:
            descriptor = klass.__dict__["vAlign"]
            break
    assert isinstance(descriptor, property)

def test_shape::description_has_hAlign():
    assert hasattr(shape::Description, "hAlign")
    descriptor = None
    for klass in shape::Description.__mro__:
        if "hAlign" in klass.__dict__:
            descriptor = klass.__dict__["hAlign"]
            break
    assert isinstance(descriptor, property)



def test_shape::shape_is_not_abstract():
    assert not inspect.isabstract(shape::Shape)


def test_shape::shape_constructor_exists():
    assert callable(shape::Shape.__init__)


def test_shape::shape_constructor_args():
    sig = inspect.signature(shape::Shape.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"

def test_shape::shape_has_style():
    assert hasattr(shape::Shape, "style")
    descriptor = None
    for klass in shape::Shape.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_shape::shapelayout_is_not_abstract():
    assert not inspect.isabstract(shape::ShapeLayout)


def test_shape::shapelayout_constructor_exists():
    assert callable(shape::ShapeLayout.__init__)


def test_shape::shapelayout_constructor_args():
    sig = inspect.signature(shape::ShapeLayout.__init__)
    params = list(sig.parameters.keys())
    assert "stretchV" in params, "Missing parameter 'stretchV'"
    assert "maxwidth" in params, "Missing parameter 'maxwidth'"
    assert "proportional" in params, "Missing parameter 'proportional'"
    assert "minwidth" in params, "Missing parameter 'minwidth'"
    assert "stretchH" in params, "Missing parameter 'stretchH'"
    assert "minheight" in params, "Missing parameter 'minheight'"
    assert "maxheight" in params, "Missing parameter 'maxheight'"

def test_shape::shapelayout_has_stretchV():
    assert hasattr(shape::ShapeLayout, "stretchV")
    descriptor = None
    for klass in shape::ShapeLayout.__mro__:
        if "stretchV" in klass.__dict__:
            descriptor = klass.__dict__["stretchV"]
            break
    assert isinstance(descriptor, property)

def test_shape::shapelayout_has_maxwidth():
    assert hasattr(shape::ShapeLayout, "maxwidth")
    descriptor = None
    for klass in shape::ShapeLayout.__mro__:
        if "maxwidth" in klass.__dict__:
            descriptor = klass.__dict__["maxwidth"]
            break
    assert isinstance(descriptor, property)

def test_shape::shapelayout_has_proportional():
    assert hasattr(shape::ShapeLayout, "proportional")
    descriptor = None
    for klass in shape::ShapeLayout.__mro__:
        if "proportional" in klass.__dict__:
            descriptor = klass.__dict__["proportional"]
            break
    assert isinstance(descriptor, property)

def test_shape::shapelayout_has_minwidth():
    assert hasattr(shape::ShapeLayout, "minwidth")
    descriptor = None
    for klass in shape::ShapeLayout.__mro__:
        if "minwidth" in klass.__dict__:
            descriptor = klass.__dict__["minwidth"]
            break
    assert isinstance(descriptor, property)

def test_shape::shapelayout_has_stretchH():
    assert hasattr(shape::ShapeLayout, "stretchH")
    descriptor = None
    for klass in shape::ShapeLayout.__mro__:
        if "stretchH" in klass.__dict__:
            descriptor = klass.__dict__["stretchH"]
            break
    assert isinstance(descriptor, property)

def test_shape::shapelayout_has_minheight():
    assert hasattr(shape::ShapeLayout, "minheight")
    descriptor = None
    for klass in shape::ShapeLayout.__mro__:
        if "minheight" in klass.__dict__:
            descriptor = klass.__dict__["minheight"]
            break
    assert isinstance(descriptor, property)

def test_shape::shapelayout_has_maxheight():
    assert hasattr(shape::ShapeLayout, "maxheight")
    descriptor = None
    for klass in shape::ShapeLayout.__mro__:
        if "maxheight" in klass.__dict__:
            descriptor = klass.__dict__["maxheight"]
            break
    assert isinstance(descriptor, property)



def test_shape::placingdefinition_is_not_abstract():
    assert not inspect.isabstract(shape::PlacingDefinition)


def test_shape::placingdefinition_constructor_exists():
    assert callable(shape::PlacingDefinition.__init__)


def test_shape::placingdefinition_constructor_args():
    sig = inspect.signature(shape::PlacingDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "offset" in params, "Missing parameter 'offset'"
    assert "distance" in params, "Missing parameter 'distance'"
    assert "angle" in params, "Missing parameter 'angle'"

def test_shape::placingdefinition_has_offset():
    assert hasattr(shape::PlacingDefinition, "offset")
    descriptor = None
    for klass in shape::PlacingDefinition.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)

def test_shape::placingdefinition_has_distance():
    assert hasattr(shape::PlacingDefinition, "distance")
    descriptor = None
    for klass in shape::PlacingDefinition.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)

def test_shape::placingdefinition_has_angle():
    assert hasattr(shape::PlacingDefinition, "angle")
    descriptor = None
    for klass in shape::PlacingDefinition.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_shape::shapestylelayout_is_not_abstract():
    assert not inspect.isabstract(shape::ShapestyleLayout)


def test_shape::shapestylelayout_constructor_exists():
    assert callable(shape::ShapestyleLayout.__init__)


def test_shape::shapestylelayout_constructor_args():
    sig = inspect.signature(shape::ShapestyleLayout.__init__)
    params = list(sig.parameters.keys())



def test_shapecontainerelement_is_not_abstract():
    assert not inspect.isabstract(ShapeContainerElement)


def test_shapecontainerelement_constructor_exists():
    assert callable(ShapeContainerElement.__init__)


def test_shapecontainerelement_constructor_args():
    sig = inspect.signature(ShapeContainerElement.__init__)
    params = list(sig.parameters.keys())



def test_shape::shapedefinition_is_not_abstract():
    assert not inspect.isabstract(shape::ShapeDefinition)


def test_shape::shapedefinition_constructor_exists():
    assert callable(shape::ShapeDefinition.__init__)


def test_shape::shapedefinition_constructor_args():
    sig = inspect.signature(shape::ShapeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_shape::connectiondefinition_is_not_abstract():
    assert not inspect.isabstract(shape::ConnectionDefinition)


def test_shape::connectiondefinition_constructor_exists():
    assert callable(shape::ConnectionDefinition.__init__)


def test_shape::connectiondefinition_constructor_args():
    sig = inspect.signature(shape::ConnectionDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "connectionStyle" in params, "Missing parameter 'connectionStyle'"

def test_shape::connectiondefinition_has_connectionStyle():
    assert hasattr(shape::ConnectionDefinition, "connectionStyle")
    descriptor = None
    for klass in shape::ConnectionDefinition.__mro__:
        if "connectionStyle" in klass.__dict__:
            descriptor = klass.__dict__["connectionStyle"]
            break
    assert isinstance(descriptor, property)



def test_shape::shapecontainerelement_is_not_abstract():
    assert not inspect.isabstract(shape::ShapeContainerElement)


def test_shape::shapecontainerelement_constructor_exists():
    assert callable(shape::ShapeContainerElement.__init__)


def test_shape::shapecontainerelement_constructor_args():
    sig = inspect.signature(shape::ShapeContainerElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "style" in params, "Missing parameter 'style'"

def test_shape::shapecontainerelement_has_name():
    assert hasattr(shape::ShapeContainerElement, "name")
    descriptor = None
    for klass in shape::ShapeContainerElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_shape::shapecontainerelement_has_style():
    assert hasattr(shape::ShapeContainerElement, "style")
    descriptor = None
    for klass in shape::ShapeContainerElement.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_shape::shapecontainer_is_not_abstract():
    assert not inspect.isabstract(shape::ShapeContainer)


def test_shape::shapecontainer_constructor_exists():
    assert callable(shape::ShapeContainer.__init__)


def test_shape::shapecontainer_constructor_args():
    sig = inspect.signature(shape::ShapeContainer.__init__)
    params = list(sig.parameters.keys())

def test_connectionstyle_exists():
    # Check that the Enumeration exists
    assert ConnectionStyle is not None

def test_connectionstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConnectionStyle]
    expected_literals = [
        "manhatten",
        "freeform",
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
        "LEFT",
        "RIGHT",
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
        "default",
        "multiline",
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
        "TOP",
        "BOTTOM",
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
        "FIT",
        "FIXED",
        "VERTICAL",
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
        "corners",
        "center",
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
shape::Point_strategy = st.builds(
    shape::Point,
    curveAfter=
        st.integers(),
    curveBefore=
        st.integers(),
    xcor=
        safe_text,
    ycor=
        safe_text
)
shape::CommonLayout_strategy = st.builds(
    shape::CommonLayout,
    ycor=
        st.integers(),
    xcor=
        st.integers(),
    width=
        st.integers(),
    heigth=
        st.integers()
)
shape::CompartmentPolygon_strategy = st.builds(
    shape::CompartmentPolygon,
)
shape::CompartmentRoundedRectangle_strategy = st.builds(
    shape::CompartmentRoundedRectangle,
)
CompartmentShape_strategy = st.builds(
    CompartmentShape,
)
shape::CompartmentEllipse_strategy = st.builds(
    shape::CompartmentEllipse,
)
shape::CompartmentRectangle_strategy = st.builds(
    shape::CompartmentRectangle,
)
shape::CompartmentShape_strategy = st.builds(
    shape::CompartmentShape,
)
shape::Compartment_strategy = st.builds(
    shape::Compartment,
    compartmentLayout=
        safe_text
)
shape::CompartmentInfo_strategy = st.builds(
    shape::CompartmentInfo,
    compartmentLayout=
        safe_text,
    margin=
        st.integers(),
    stretchV=
        safe_text,
    stretchH=
        safe_text,
    spacing=
        st.integers(),
    invisible=
        st.booleans()
)
Shape_strategy = st.builds(
    Shape,
)
shape::Polyline_strategy = st.builds(
    shape::Polyline,
)
shape::Polygon_strategy = st.builds(
    shape::Polygon,
)
shape::RoundedRectangle_strategy = st.builds(
    shape::RoundedRectangle,
)
shape::Text_strategy = st.builds(
    shape::Text,
    texttype=
        safe_text
)
shape::Rectangle_strategy = st.builds(
    shape::Rectangle,
)
shape::Ellipse_strategy = st.builds(
    shape::Ellipse,
)
shape::Line_strategy = st.builds(
    shape::Line,
)
shape::TextLayout_strategy = st.builds(
    shape::TextLayout,
    hAlign=
        safe_text,
    vAlign=
        safe_text
)
shape::RoundedRectangleLayout_strategy = st.builds(
    shape::RoundedRectangleLayout,
    curveHeight=
        st.integers(),
    curveWidth=
        st.integers()
)
shape::RectangleEllipseLayout_strategy = st.builds(
    shape::RectangleEllipseLayout,
)
shape::PolyLineLayout_strategy = st.builds(
    shape::PolyLineLayout,
)
shape::LineLayout_strategy = st.builds(
    shape::LineLayout,
)
ShapeConnection_strategy = st.builds(
    ShapeConnection,
)
shape::CDRectangle_strategy = st.builds(
    shape::CDRectangle,
)
shape::CDPolyline_strategy = st.builds(
    shape::CDPolyline,
)
shape::CDText_strategy = st.builds(
    shape::CDText,
    texttype=
        safe_text
)
shape::CDPolygon_strategy = st.builds(
    shape::CDPolygon,
)
shape::CDEllipse_strategy = st.builds(
    shape::CDEllipse,
)
shape::CDRoundedRectangle_strategy = st.builds(
    shape::CDRoundedRectangle,
)
shape::CDLine_strategy = st.builds(
    shape::CDLine,
)
AnchorPositionPos_strategy = st.builds(
    AnchorPositionPos,
)
shape::AnchorFixPointPosition_strategy = st.builds(
    shape::AnchorFixPointPosition,
    ycor=
        st.integers(),
    xcor=
        st.integers()
)
shape::AnchorRelativePosition_strategy = st.builds(
    shape::AnchorRelativePosition,
    xoffset=
        safe_text,
    yoffset=
        safe_text
)
shape::AnchorPositionPos_strategy = st.builds(
    shape::AnchorPositionPos,
)
shape::AnchorPosition_strategy = st.builds(
    shape::AnchorPosition,
)
shape::TextBody_strategy = st.builds(
    shape::TextBody,
    value=
        safe_text
)
AnchorType_strategy = st.builds(
    AnchorType,
)
shape::AnchorManual_strategy = st.builds(
    shape::AnchorManual,
)
shape::AnchorPredefinied_strategy = st.builds(
    shape::AnchorPredefinied,
    value=
        safe_text
)
shape::AnchorType_strategy = st.builds(
    shape::AnchorType,
)
shape::ShapeConnection_strategy = st.builds(
    shape::ShapeConnection,
    style=
        safe_text
)
shape::Anchor_strategy = st.builds(
    shape::Anchor,
)
shape::Description_strategy = st.builds(
    shape::Description,
    style=
        safe_text,
    vAlign=
        safe_text,
    hAlign=
        safe_text
)
shape::Shape_strategy = st.builds(
    shape::Shape,
    style=
        safe_text
)
shape::ShapeLayout_strategy = st.builds(
    shape::ShapeLayout,
    stretchV=
        safe_text,
    maxwidth=
        st.integers(),
    proportional=
        safe_text,
    minwidth=
        st.integers(),
    stretchH=
        safe_text,
    minheight=
        st.integers(),
    maxheight=
        st.integers()
)
shape::PlacingDefinition_strategy = st.builds(
    shape::PlacingDefinition,
    offset=
        safe_text,
    distance=
        st.integers(),
    angle=
        st.integers()
)
shape::ShapestyleLayout_strategy = st.builds(
    shape::ShapestyleLayout,
)
ShapeContainerElement_strategy = st.builds(
    ShapeContainerElement,
)
shape::ShapeDefinition_strategy = st.builds(
    shape::ShapeDefinition,
)
shape::ConnectionDefinition_strategy = st.builds(
    shape::ConnectionDefinition,
    connectionStyle=
        safe_text
)
shape::ShapeContainerElement_strategy = st.builds(
    shape::ShapeContainerElement,
    name=
        safe_text,
    style=
        safe_text
)
shape::ShapeContainer_strategy = st.builds(
    shape::ShapeContainer,
)

@given(instance=shape::Point_strategy)
@settings(max_examples=50)
def test_shape::point_instantiation(instance):
    assert isinstance(instance, shape::Point)

@given(instance=shape::Point_strategy)
def test_shape::point_curveAfter_type(instance):
    assert isinstance(instance.curveAfter, int)


@given(instance=shape::Point_strategy)
def test_shape::point_curveAfter_setter(instance):
    original = instance.curveAfter
    instance.curveAfter = original
    assert instance.curveAfter == original

@given(instance=shape::Point_strategy)
def test_shape::point_curveBefore_type(instance):
    assert isinstance(instance.curveBefore, int)


@given(instance=shape::Point_strategy)
def test_shape::point_curveBefore_setter(instance):
    original = instance.curveBefore
    instance.curveBefore = original
    assert instance.curveBefore == original

@given(instance=shape::Point_strategy)
def test_shape::point_xcor_type(instance):
    assert isinstance(instance.xcor, str)


@given(instance=shape::Point_strategy)
def test_shape::point_xcor_setter(instance):
    original = instance.xcor
    instance.xcor = original
    assert instance.xcor == original

@given(instance=shape::Point_strategy)
def test_shape::point_ycor_type(instance):
    assert isinstance(instance.ycor, str)


@given(instance=shape::Point_strategy)
def test_shape::point_ycor_setter(instance):
    original = instance.ycor
    instance.ycor = original
    assert instance.ycor == original

@given(instance=shape::CommonLayout_strategy)
@settings(max_examples=50)
def test_shape::commonlayout_instantiation(instance):
    assert isinstance(instance, shape::CommonLayout)

@given(instance=shape::CommonLayout_strategy)
def test_shape::commonlayout_ycor_type(instance):
    assert isinstance(instance.ycor, int)


@given(instance=shape::CommonLayout_strategy)
def test_shape::commonlayout_ycor_setter(instance):
    original = instance.ycor
    instance.ycor = original
    assert instance.ycor == original

@given(instance=shape::CommonLayout_strategy)
def test_shape::commonlayout_xcor_type(instance):
    assert isinstance(instance.xcor, int)


@given(instance=shape::CommonLayout_strategy)
def test_shape::commonlayout_xcor_setter(instance):
    original = instance.xcor
    instance.xcor = original
    assert instance.xcor == original

@given(instance=shape::CommonLayout_strategy)
def test_shape::commonlayout_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=shape::CommonLayout_strategy)
def test_shape::commonlayout_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=shape::CommonLayout_strategy)
def test_shape::commonlayout_heigth_type(instance):
    assert isinstance(instance.heigth, int)


@given(instance=shape::CommonLayout_strategy)
def test_shape::commonlayout_heigth_setter(instance):
    original = instance.heigth
    instance.heigth = original
    assert instance.heigth == original

@given(instance=shape::CompartmentPolygon_strategy)
@settings(max_examples=50)
def test_shape::compartmentpolygon_instantiation(instance):
    assert isinstance(instance, shape::CompartmentPolygon)

@given(instance=shape::CompartmentRoundedRectangle_strategy)
@settings(max_examples=50)
def test_shape::compartmentroundedrectangle_instantiation(instance):
    assert isinstance(instance, shape::CompartmentRoundedRectangle)

@given(instance=CompartmentShape_strategy)
@settings(max_examples=50)
def test_compartmentshape_instantiation(instance):
    assert isinstance(instance, CompartmentShape)

@given(instance=shape::CompartmentEllipse_strategy)
@settings(max_examples=50)
def test_shape::compartmentellipse_instantiation(instance):
    assert isinstance(instance, shape::CompartmentEllipse)

@given(instance=shape::CompartmentRectangle_strategy)
@settings(max_examples=50)
def test_shape::compartmentrectangle_instantiation(instance):
    assert isinstance(instance, shape::CompartmentRectangle)

@given(instance=shape::CompartmentShape_strategy)
@settings(max_examples=50)
def test_shape::compartmentshape_instantiation(instance):
    assert isinstance(instance, shape::CompartmentShape)

@given(instance=shape::Compartment_strategy)
@settings(max_examples=50)
def test_shape::compartment_instantiation(instance):
    assert isinstance(instance, shape::Compartment)

@given(instance=shape::Compartment_strategy)
def test_shape::compartment_compartmentLayout_type(instance):
    assert isinstance(instance.compartmentLayout, str)


@given(instance=shape::Compartment_strategy)
def test_shape::compartment_compartmentLayout_setter(instance):
    original = instance.compartmentLayout
    instance.compartmentLayout = original
    assert instance.compartmentLayout == original

@given(instance=shape::CompartmentInfo_strategy)
@settings(max_examples=50)
def test_shape::compartmentinfo_instantiation(instance):
    assert isinstance(instance, shape::CompartmentInfo)

@given(instance=shape::CompartmentInfo_strategy)
def test_shape::compartmentinfo_compartmentLayout_type(instance):
    assert isinstance(instance.compartmentLayout, str)


@given(instance=shape::CompartmentInfo_strategy)
def test_shape::compartmentinfo_compartmentLayout_setter(instance):
    original = instance.compartmentLayout
    instance.compartmentLayout = original
    assert instance.compartmentLayout == original

@given(instance=shape::CompartmentInfo_strategy)
def test_shape::compartmentinfo_margin_type(instance):
    assert isinstance(instance.margin, int)


@given(instance=shape::CompartmentInfo_strategy)
def test_shape::compartmentinfo_margin_setter(instance):
    original = instance.margin
    instance.margin = original
    assert instance.margin == original

@given(instance=shape::CompartmentInfo_strategy)
def test_shape::compartmentinfo_stretchV_type(instance):
    assert isinstance(instance.stretchV, str)


@given(instance=shape::CompartmentInfo_strategy)
def test_shape::compartmentinfo_stretchV_setter(instance):
    original = instance.stretchV
    instance.stretchV = original
    assert instance.stretchV == original

@given(instance=shape::CompartmentInfo_strategy)
def test_shape::compartmentinfo_stretchH_type(instance):
    assert isinstance(instance.stretchH, str)


@given(instance=shape::CompartmentInfo_strategy)
def test_shape::compartmentinfo_stretchH_setter(instance):
    original = instance.stretchH
    instance.stretchH = original
    assert instance.stretchH == original

@given(instance=shape::CompartmentInfo_strategy)
def test_shape::compartmentinfo_spacing_type(instance):
    assert isinstance(instance.spacing, int)


@given(instance=shape::CompartmentInfo_strategy)
def test_shape::compartmentinfo_spacing_setter(instance):
    original = instance.spacing
    instance.spacing = original
    assert instance.spacing == original

@given(instance=shape::CompartmentInfo_strategy)
def test_shape::compartmentinfo_invisible_type(instance):
    assert isinstance(instance.invisible, bool)


@given(instance=shape::CompartmentInfo_strategy)
def test_shape::compartmentinfo_invisible_setter(instance):
    original = instance.invisible
    instance.invisible = original
    assert instance.invisible == original

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=shape::Polyline_strategy)
@settings(max_examples=50)
def test_shape::polyline_instantiation(instance):
    assert isinstance(instance, shape::Polyline)

@given(instance=shape::Polygon_strategy)
@settings(max_examples=50)
def test_shape::polygon_instantiation(instance):
    assert isinstance(instance, shape::Polygon)

@given(instance=shape::RoundedRectangle_strategy)
@settings(max_examples=50)
def test_shape::roundedrectangle_instantiation(instance):
    assert isinstance(instance, shape::RoundedRectangle)

@given(instance=shape::Text_strategy)
@settings(max_examples=50)
def test_shape::text_instantiation(instance):
    assert isinstance(instance, shape::Text)

@given(instance=shape::Text_strategy)
def test_shape::text_texttype_type(instance):
    assert isinstance(instance.texttype, str)


@given(instance=shape::Text_strategy)
def test_shape::text_texttype_setter(instance):
    original = instance.texttype
    instance.texttype = original
    assert instance.texttype == original

@given(instance=shape::Rectangle_strategy)
@settings(max_examples=50)
def test_shape::rectangle_instantiation(instance):
    assert isinstance(instance, shape::Rectangle)

@given(instance=shape::Ellipse_strategy)
@settings(max_examples=50)
def test_shape::ellipse_instantiation(instance):
    assert isinstance(instance, shape::Ellipse)

@given(instance=shape::Line_strategy)
@settings(max_examples=50)
def test_shape::line_instantiation(instance):
    assert isinstance(instance, shape::Line)

@given(instance=shape::TextLayout_strategy)
@settings(max_examples=50)
def test_shape::textlayout_instantiation(instance):
    assert isinstance(instance, shape::TextLayout)

@given(instance=shape::TextLayout_strategy)
def test_shape::textlayout_hAlign_type(instance):
    assert isinstance(instance.hAlign, str)


@given(instance=shape::TextLayout_strategy)
def test_shape::textlayout_hAlign_setter(instance):
    original = instance.hAlign
    instance.hAlign = original
    assert instance.hAlign == original

@given(instance=shape::TextLayout_strategy)
def test_shape::textlayout_vAlign_type(instance):
    assert isinstance(instance.vAlign, str)


@given(instance=shape::TextLayout_strategy)
def test_shape::textlayout_vAlign_setter(instance):
    original = instance.vAlign
    instance.vAlign = original
    assert instance.vAlign == original

@given(instance=shape::RoundedRectangleLayout_strategy)
@settings(max_examples=50)
def test_shape::roundedrectanglelayout_instantiation(instance):
    assert isinstance(instance, shape::RoundedRectangleLayout)

@given(instance=shape::RoundedRectangleLayout_strategy)
def test_shape::roundedrectanglelayout_curveHeight_type(instance):
    assert isinstance(instance.curveHeight, int)


@given(instance=shape::RoundedRectangleLayout_strategy)
def test_shape::roundedrectanglelayout_curveHeight_setter(instance):
    original = instance.curveHeight
    instance.curveHeight = original
    assert instance.curveHeight == original

@given(instance=shape::RoundedRectangleLayout_strategy)
def test_shape::roundedrectanglelayout_curveWidth_type(instance):
    assert isinstance(instance.curveWidth, int)


@given(instance=shape::RoundedRectangleLayout_strategy)
def test_shape::roundedrectanglelayout_curveWidth_setter(instance):
    original = instance.curveWidth
    instance.curveWidth = original
    assert instance.curveWidth == original

@given(instance=shape::RectangleEllipseLayout_strategy)
@settings(max_examples=50)
def test_shape::rectangleellipselayout_instantiation(instance):
    assert isinstance(instance, shape::RectangleEllipseLayout)

@given(instance=shape::PolyLineLayout_strategy)
@settings(max_examples=50)
def test_shape::polylinelayout_instantiation(instance):
    assert isinstance(instance, shape::PolyLineLayout)

@given(instance=shape::LineLayout_strategy)
@settings(max_examples=50)
def test_shape::linelayout_instantiation(instance):
    assert isinstance(instance, shape::LineLayout)

@given(instance=ShapeConnection_strategy)
@settings(max_examples=50)
def test_shapeconnection_instantiation(instance):
    assert isinstance(instance, ShapeConnection)

@given(instance=shape::CDRectangle_strategy)
@settings(max_examples=50)
def test_shape::cdrectangle_instantiation(instance):
    assert isinstance(instance, shape::CDRectangle)

@given(instance=shape::CDPolyline_strategy)
@settings(max_examples=50)
def test_shape::cdpolyline_instantiation(instance):
    assert isinstance(instance, shape::CDPolyline)

@given(instance=shape::CDText_strategy)
@settings(max_examples=50)
def test_shape::cdtext_instantiation(instance):
    assert isinstance(instance, shape::CDText)

@given(instance=shape::CDText_strategy)
def test_shape::cdtext_texttype_type(instance):
    assert isinstance(instance.texttype, str)


@given(instance=shape::CDText_strategy)
def test_shape::cdtext_texttype_setter(instance):
    original = instance.texttype
    instance.texttype = original
    assert instance.texttype == original

@given(instance=shape::CDPolygon_strategy)
@settings(max_examples=50)
def test_shape::cdpolygon_instantiation(instance):
    assert isinstance(instance, shape::CDPolygon)

@given(instance=shape::CDEllipse_strategy)
@settings(max_examples=50)
def test_shape::cdellipse_instantiation(instance):
    assert isinstance(instance, shape::CDEllipse)

@given(instance=shape::CDRoundedRectangle_strategy)
@settings(max_examples=50)
def test_shape::cdroundedrectangle_instantiation(instance):
    assert isinstance(instance, shape::CDRoundedRectangle)

@given(instance=shape::CDLine_strategy)
@settings(max_examples=50)
def test_shape::cdline_instantiation(instance):
    assert isinstance(instance, shape::CDLine)

@given(instance=AnchorPositionPos_strategy)
@settings(max_examples=50)
def test_anchorpositionpos_instantiation(instance):
    assert isinstance(instance, AnchorPositionPos)

@given(instance=shape::AnchorFixPointPosition_strategy)
@settings(max_examples=50)
def test_shape::anchorfixpointposition_instantiation(instance):
    assert isinstance(instance, shape::AnchorFixPointPosition)

@given(instance=shape::AnchorFixPointPosition_strategy)
def test_shape::anchorfixpointposition_ycor_type(instance):
    assert isinstance(instance.ycor, int)


@given(instance=shape::AnchorFixPointPosition_strategy)
def test_shape::anchorfixpointposition_ycor_setter(instance):
    original = instance.ycor
    instance.ycor = original
    assert instance.ycor == original

@given(instance=shape::AnchorFixPointPosition_strategy)
def test_shape::anchorfixpointposition_xcor_type(instance):
    assert isinstance(instance.xcor, int)


@given(instance=shape::AnchorFixPointPosition_strategy)
def test_shape::anchorfixpointposition_xcor_setter(instance):
    original = instance.xcor
    instance.xcor = original
    assert instance.xcor == original

@given(instance=shape::AnchorRelativePosition_strategy)
@settings(max_examples=50)
def test_shape::anchorrelativeposition_instantiation(instance):
    assert isinstance(instance, shape::AnchorRelativePosition)

@given(instance=shape::AnchorRelativePosition_strategy)
def test_shape::anchorrelativeposition_xoffset_type(instance):
    assert isinstance(instance.xoffset, str)


@given(instance=shape::AnchorRelativePosition_strategy)
def test_shape::anchorrelativeposition_xoffset_setter(instance):
    original = instance.xoffset
    instance.xoffset = original
    assert instance.xoffset == original

@given(instance=shape::AnchorRelativePosition_strategy)
def test_shape::anchorrelativeposition_yoffset_type(instance):
    assert isinstance(instance.yoffset, str)


@given(instance=shape::AnchorRelativePosition_strategy)
def test_shape::anchorrelativeposition_yoffset_setter(instance):
    original = instance.yoffset
    instance.yoffset = original
    assert instance.yoffset == original

@given(instance=shape::AnchorPositionPos_strategy)
@settings(max_examples=50)
def test_shape::anchorpositionpos_instantiation(instance):
    assert isinstance(instance, shape::AnchorPositionPos)

@given(instance=shape::AnchorPosition_strategy)
@settings(max_examples=50)
def test_shape::anchorposition_instantiation(instance):
    assert isinstance(instance, shape::AnchorPosition)

@given(instance=shape::TextBody_strategy)
@settings(max_examples=50)
def test_shape::textbody_instantiation(instance):
    assert isinstance(instance, shape::TextBody)

@given(instance=shape::TextBody_strategy)
def test_shape::textbody_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=shape::TextBody_strategy)
def test_shape::textbody_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=AnchorType_strategy)
@settings(max_examples=50)
def test_anchortype_instantiation(instance):
    assert isinstance(instance, AnchorType)

@given(instance=shape::AnchorManual_strategy)
@settings(max_examples=50)
def test_shape::anchormanual_instantiation(instance):
    assert isinstance(instance, shape::AnchorManual)

@given(instance=shape::AnchorPredefinied_strategy)
@settings(max_examples=50)
def test_shape::anchorpredefinied_instantiation(instance):
    assert isinstance(instance, shape::AnchorPredefinied)

@given(instance=shape::AnchorPredefinied_strategy)
def test_shape::anchorpredefinied_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=shape::AnchorPredefinied_strategy)
def test_shape::anchorpredefinied_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=shape::AnchorType_strategy)
@settings(max_examples=50)
def test_shape::anchortype_instantiation(instance):
    assert isinstance(instance, shape::AnchorType)

@given(instance=shape::ShapeConnection_strategy)
@settings(max_examples=50)
def test_shape::shapeconnection_instantiation(instance):
    assert isinstance(instance, shape::ShapeConnection)

@given(instance=shape::ShapeConnection_strategy)
def test_shape::shapeconnection_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=shape::ShapeConnection_strategy)
def test_shape::shapeconnection_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=shape::Anchor_strategy)
@settings(max_examples=50)
def test_shape::anchor_instantiation(instance):
    assert isinstance(instance, shape::Anchor)

@given(instance=shape::Description_strategy)
@settings(max_examples=50)
def test_shape::description_instantiation(instance):
    assert isinstance(instance, shape::Description)

@given(instance=shape::Description_strategy)
def test_shape::description_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=shape::Description_strategy)
def test_shape::description_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=shape::Description_strategy)
def test_shape::description_vAlign_type(instance):
    assert isinstance(instance.vAlign, str)


@given(instance=shape::Description_strategy)
def test_shape::description_vAlign_setter(instance):
    original = instance.vAlign
    instance.vAlign = original
    assert instance.vAlign == original

@given(instance=shape::Description_strategy)
def test_shape::description_hAlign_type(instance):
    assert isinstance(instance.hAlign, str)


@given(instance=shape::Description_strategy)
def test_shape::description_hAlign_setter(instance):
    original = instance.hAlign
    instance.hAlign = original
    assert instance.hAlign == original

@given(instance=shape::Shape_strategy)
@settings(max_examples=50)
def test_shape::shape_instantiation(instance):
    assert isinstance(instance, shape::Shape)

@given(instance=shape::Shape_strategy)
def test_shape::shape_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=shape::Shape_strategy)
def test_shape::shape_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=shape::ShapeLayout_strategy)
@settings(max_examples=50)
def test_shape::shapelayout_instantiation(instance):
    assert isinstance(instance, shape::ShapeLayout)

@given(instance=shape::ShapeLayout_strategy)
def test_shape::shapelayout_stretchV_type(instance):
    assert isinstance(instance.stretchV, str)


@given(instance=shape::ShapeLayout_strategy)
def test_shape::shapelayout_stretchV_setter(instance):
    original = instance.stretchV
    instance.stretchV = original
    assert instance.stretchV == original

@given(instance=shape::ShapeLayout_strategy)
def test_shape::shapelayout_maxwidth_type(instance):
    assert isinstance(instance.maxwidth, int)


@given(instance=shape::ShapeLayout_strategy)
def test_shape::shapelayout_maxwidth_setter(instance):
    original = instance.maxwidth
    instance.maxwidth = original
    assert instance.maxwidth == original

@given(instance=shape::ShapeLayout_strategy)
def test_shape::shapelayout_proportional_type(instance):
    assert isinstance(instance.proportional, str)


@given(instance=shape::ShapeLayout_strategy)
def test_shape::shapelayout_proportional_setter(instance):
    original = instance.proportional
    instance.proportional = original
    assert instance.proportional == original

@given(instance=shape::ShapeLayout_strategy)
def test_shape::shapelayout_minwidth_type(instance):
    assert isinstance(instance.minwidth, int)


@given(instance=shape::ShapeLayout_strategy)
def test_shape::shapelayout_minwidth_setter(instance):
    original = instance.minwidth
    instance.minwidth = original
    assert instance.minwidth == original

@given(instance=shape::ShapeLayout_strategy)
def test_shape::shapelayout_stretchH_type(instance):
    assert isinstance(instance.stretchH, str)


@given(instance=shape::ShapeLayout_strategy)
def test_shape::shapelayout_stretchH_setter(instance):
    original = instance.stretchH
    instance.stretchH = original
    assert instance.stretchH == original

@given(instance=shape::ShapeLayout_strategy)
def test_shape::shapelayout_minheight_type(instance):
    assert isinstance(instance.minheight, int)


@given(instance=shape::ShapeLayout_strategy)
def test_shape::shapelayout_minheight_setter(instance):
    original = instance.minheight
    instance.minheight = original
    assert instance.minheight == original

@given(instance=shape::ShapeLayout_strategy)
def test_shape::shapelayout_maxheight_type(instance):
    assert isinstance(instance.maxheight, int)


@given(instance=shape::ShapeLayout_strategy)
def test_shape::shapelayout_maxheight_setter(instance):
    original = instance.maxheight
    instance.maxheight = original
    assert instance.maxheight == original

@given(instance=shape::PlacingDefinition_strategy)
@settings(max_examples=50)
def test_shape::placingdefinition_instantiation(instance):
    assert isinstance(instance, shape::PlacingDefinition)

@given(instance=shape::PlacingDefinition_strategy)
def test_shape::placingdefinition_offset_type(instance):
    assert isinstance(instance.offset, str)


@given(instance=shape::PlacingDefinition_strategy)
def test_shape::placingdefinition_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=shape::PlacingDefinition_strategy)
def test_shape::placingdefinition_distance_type(instance):
    assert isinstance(instance.distance, int)


@given(instance=shape::PlacingDefinition_strategy)
def test_shape::placingdefinition_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=shape::PlacingDefinition_strategy)
def test_shape::placingdefinition_angle_type(instance):
    assert isinstance(instance.angle, int)


@given(instance=shape::PlacingDefinition_strategy)
def test_shape::placingdefinition_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=shape::ShapestyleLayout_strategy)
@settings(max_examples=50)
def test_shape::shapestylelayout_instantiation(instance):
    assert isinstance(instance, shape::ShapestyleLayout)

@given(instance=ShapeContainerElement_strategy)
@settings(max_examples=50)
def test_shapecontainerelement_instantiation(instance):
    assert isinstance(instance, ShapeContainerElement)

@given(instance=shape::ShapeDefinition_strategy)
@settings(max_examples=50)
def test_shape::shapedefinition_instantiation(instance):
    assert isinstance(instance, shape::ShapeDefinition)

@given(instance=shape::ConnectionDefinition_strategy)
@settings(max_examples=50)
def test_shape::connectiondefinition_instantiation(instance):
    assert isinstance(instance, shape::ConnectionDefinition)

@given(instance=shape::ConnectionDefinition_strategy)
def test_shape::connectiondefinition_connectionStyle_type(instance):
    assert isinstance(instance.connectionStyle, str)


@given(instance=shape::ConnectionDefinition_strategy)
def test_shape::connectiondefinition_connectionStyle_setter(instance):
    original = instance.connectionStyle
    instance.connectionStyle = original
    assert instance.connectionStyle == original

@given(instance=shape::ShapeContainerElement_strategy)
@settings(max_examples=50)
def test_shape::shapecontainerelement_instantiation(instance):
    assert isinstance(instance, shape::ShapeContainerElement)

@given(instance=shape::ShapeContainerElement_strategy)
def test_shape::shapecontainerelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=shape::ShapeContainerElement_strategy)
def test_shape::shapecontainerelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=shape::ShapeContainerElement_strategy)
def test_shape::shapecontainerelement_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=shape::ShapeContainerElement_strategy)
def test_shape::shapecontainerelement_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=shape::ShapeContainer_strategy)
@settings(max_examples=50)
def test_shape::shapecontainer_instantiation(instance):
    assert isinstance(instance, shape::ShapeContainer)
