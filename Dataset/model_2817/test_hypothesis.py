import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Border,
    draw2d::LabeledBorder,
    ConnectionAnchor,
    draw2d::XYAnchor,
    draw2d::ConnectionAnchor,
    draw2d::FlowBorder,
    ColoredLabeledBorder,
    draw2d::TitleBarBorder,
    draw2d::GroupBoxBorder,
    LabeledBorder,
    draw2d::ColoredLabeledBorder,
    draw2d::FrameBorder,
    Polyline,
    draw2d::Polygon,
    PointListShape,
    draw2d::PolylineShape,
    draw2d::PolygonShape,
    draw2d::Polyline,
    Shape,
    draw2d::RoundedRectangle,
    draw2d::PointListShape,
    draw2d::Triangle,
    draw2d::Ellipse,
    draw2d::RectangleFigure,
    draw2d::Figure,
    Canvas,
    draw2d::Draw2DCanvas,
    Figure,
    draw2d::BlockFlow,
    draw2d::Shape,
    draw2d::ImageFigure,
    draw2d::Label,
    draw2d::Border,
    draw2d::Font,
    draw2d::Color,
    Alignment,
    Orientation,
    Direction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_border_is_not_abstract():
    assert not inspect.isabstract(Border)


def test_border_constructor_exists():
    assert callable(Border.__init__)


def test_border_constructor_args():
    sig = inspect.signature(Border.__init__)
    params = list(sig.parameters.keys())



def test_draw2d::labeledborder_is_not_abstract():
    assert not inspect.isabstract(draw2d::LabeledBorder)


def test_draw2d::labeledborder_constructor_exists():
    assert callable(draw2d::LabeledBorder.__init__)


def test_draw2d::labeledborder_constructor_args():
    sig = inspect.signature(draw2d::LabeledBorder.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_draw2d::labeledborder_has_label():
    assert hasattr(draw2d::LabeledBorder, "label")
    descriptor = None
    for klass in draw2d::LabeledBorder.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_connectionanchor_is_not_abstract():
    assert not inspect.isabstract(ConnectionAnchor)


def test_connectionanchor_constructor_exists():
    assert callable(ConnectionAnchor.__init__)


def test_connectionanchor_constructor_args():
    sig = inspect.signature(ConnectionAnchor.__init__)
    params = list(sig.parameters.keys())



def test_draw2d::xyanchor_is_not_abstract():
    assert not inspect.isabstract(draw2d::XYAnchor)


def test_draw2d::xyanchor_constructor_exists():
    assert callable(draw2d::XYAnchor.__init__)


def test_draw2d::xyanchor_constructor_args():
    sig = inspect.signature(draw2d::XYAnchor.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_draw2d::xyanchor_has_location():
    assert hasattr(draw2d::XYAnchor, "location")
    descriptor = None
    for klass in draw2d::XYAnchor.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_draw2d::connectionanchor_is_not_abstract():
    assert not inspect.isabstract(draw2d::ConnectionAnchor)


def test_draw2d::connectionanchor_constructor_exists():
    assert callable(draw2d::ConnectionAnchor.__init__)


def test_draw2d::connectionanchor_constructor_args():
    sig = inspect.signature(draw2d::ConnectionAnchor.__init__)
    params = list(sig.parameters.keys())



def test_draw2d::flowborder_is_not_abstract():
    assert not inspect.isabstract(draw2d::FlowBorder)


def test_draw2d::flowborder_constructor_exists():
    assert callable(draw2d::FlowBorder.__init__)


def test_draw2d::flowborder_constructor_args():
    sig = inspect.signature(draw2d::FlowBorder.__init__)
    params = list(sig.parameters.keys())
    assert "bottomMargin" in params, "Missing parameter 'bottomMargin'"
    assert "leftMargin" in params, "Missing parameter 'leftMargin'"
    assert "topMargin" in params, "Missing parameter 'topMargin'"
    assert "rightMargin" in params, "Missing parameter 'rightMargin'"

def test_draw2d::flowborder_has_bottomMargin():
    assert hasattr(draw2d::FlowBorder, "bottomMargin")
    descriptor = None
    for klass in draw2d::FlowBorder.__mro__:
        if "bottomMargin" in klass.__dict__:
            descriptor = klass.__dict__["bottomMargin"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::flowborder_has_leftMargin():
    assert hasattr(draw2d::FlowBorder, "leftMargin")
    descriptor = None
    for klass in draw2d::FlowBorder.__mro__:
        if "leftMargin" in klass.__dict__:
            descriptor = klass.__dict__["leftMargin"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::flowborder_has_topMargin():
    assert hasattr(draw2d::FlowBorder, "topMargin")
    descriptor = None
    for klass in draw2d::FlowBorder.__mro__:
        if "topMargin" in klass.__dict__:
            descriptor = klass.__dict__["topMargin"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::flowborder_has_rightMargin():
    assert hasattr(draw2d::FlowBorder, "rightMargin")
    descriptor = None
    for klass in draw2d::FlowBorder.__mro__:
        if "rightMargin" in klass.__dict__:
            descriptor = klass.__dict__["rightMargin"]
            break
    assert isinstance(descriptor, property)



def test_coloredlabeledborder_is_not_abstract():
    assert not inspect.isabstract(ColoredLabeledBorder)


def test_coloredlabeledborder_constructor_exists():
    assert callable(ColoredLabeledBorder.__init__)


def test_coloredlabeledborder_constructor_args():
    sig = inspect.signature(ColoredLabeledBorder.__init__)
    params = list(sig.parameters.keys())



def test_draw2d::titlebarborder_is_not_abstract():
    assert not inspect.isabstract(draw2d::TitleBarBorder)


def test_draw2d::titlebarborder_constructor_exists():
    assert callable(draw2d::TitleBarBorder.__init__)


def test_draw2d::titlebarborder_constructor_args():
    sig = inspect.signature(draw2d::TitleBarBorder.__init__)
    params = list(sig.parameters.keys())



def test_draw2d::groupboxborder_is_not_abstract():
    assert not inspect.isabstract(draw2d::GroupBoxBorder)


def test_draw2d::groupboxborder_constructor_exists():
    assert callable(draw2d::GroupBoxBorder.__init__)


def test_draw2d::groupboxborder_constructor_args():
    sig = inspect.signature(draw2d::GroupBoxBorder.__init__)
    params = list(sig.parameters.keys())



def test_labeledborder_is_not_abstract():
    assert not inspect.isabstract(LabeledBorder)


def test_labeledborder_constructor_exists():
    assert callable(LabeledBorder.__init__)


def test_labeledborder_constructor_args():
    sig = inspect.signature(LabeledBorder.__init__)
    params = list(sig.parameters.keys())



def test_draw2d::coloredlabeledborder_is_not_abstract():
    assert not inspect.isabstract(draw2d::ColoredLabeledBorder)


def test_draw2d::coloredlabeledborder_constructor_exists():
    assert callable(draw2d::ColoredLabeledBorder.__init__)


def test_draw2d::coloredlabeledborder_constructor_args():
    sig = inspect.signature(draw2d::ColoredLabeledBorder.__init__)
    params = list(sig.parameters.keys())



def test_draw2d::frameborder_is_not_abstract():
    assert not inspect.isabstract(draw2d::FrameBorder)


def test_draw2d::frameborder_constructor_exists():
    assert callable(draw2d::FrameBorder.__init__)


def test_draw2d::frameborder_constructor_args():
    sig = inspect.signature(draw2d::FrameBorder.__init__)
    params = list(sig.parameters.keys())



def test_polyline_is_not_abstract():
    assert not inspect.isabstract(Polyline)


def test_polyline_constructor_exists():
    assert callable(Polyline.__init__)


def test_polyline_constructor_args():
    sig = inspect.signature(Polyline.__init__)
    params = list(sig.parameters.keys())



def test_draw2d::polygon_is_not_abstract():
    assert not inspect.isabstract(draw2d::Polygon)


def test_draw2d::polygon_constructor_exists():
    assert callable(draw2d::Polygon.__init__)


def test_draw2d::polygon_constructor_args():
    sig = inspect.signature(draw2d::Polygon.__init__)
    params = list(sig.parameters.keys())



def test_pointlistshape_is_not_abstract():
    assert not inspect.isabstract(PointListShape)


def test_pointlistshape_constructor_exists():
    assert callable(PointListShape.__init__)


def test_pointlistshape_constructor_args():
    sig = inspect.signature(PointListShape.__init__)
    params = list(sig.parameters.keys())



def test_draw2d::polylineshape_is_not_abstract():
    assert not inspect.isabstract(draw2d::PolylineShape)


def test_draw2d::polylineshape_constructor_exists():
    assert callable(draw2d::PolylineShape.__init__)


def test_draw2d::polylineshape_constructor_args():
    sig = inspect.signature(draw2d::PolylineShape.__init__)
    params = list(sig.parameters.keys())
    assert "tolerance" in params, "Missing parameter 'tolerance'"

def test_draw2d::polylineshape_has_tolerance():
    assert hasattr(draw2d::PolylineShape, "tolerance")
    descriptor = None
    for klass in draw2d::PolylineShape.__mro__:
        if "tolerance" in klass.__dict__:
            descriptor = klass.__dict__["tolerance"]
            break
    assert isinstance(descriptor, property)



def test_draw2d::polygonshape_is_not_abstract():
    assert not inspect.isabstract(draw2d::PolygonShape)


def test_draw2d::polygonshape_constructor_exists():
    assert callable(draw2d::PolygonShape.__init__)


def test_draw2d::polygonshape_constructor_args():
    sig = inspect.signature(draw2d::PolygonShape.__init__)
    params = list(sig.parameters.keys())



def test_draw2d::polyline_is_not_abstract():
    assert not inspect.isabstract(draw2d::Polyline)


def test_draw2d::polyline_constructor_exists():
    assert callable(draw2d::Polyline.__init__)


def test_draw2d::polyline_constructor_args():
    sig = inspect.signature(draw2d::Polyline.__init__)
    params = list(sig.parameters.keys())
    assert "tolerance" in params, "Missing parameter 'tolerance'"

def test_draw2d::polyline_has_tolerance():
    assert hasattr(draw2d::Polyline, "tolerance")
    descriptor = None
    for klass in draw2d::Polyline.__mro__:
        if "tolerance" in klass.__dict__:
            descriptor = klass.__dict__["tolerance"]
            break
    assert isinstance(descriptor, property)



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_draw2d::roundedrectangle_is_not_abstract():
    assert not inspect.isabstract(draw2d::RoundedRectangle)


def test_draw2d::roundedrectangle_constructor_exists():
    assert callable(draw2d::RoundedRectangle.__init__)


def test_draw2d::roundedrectangle_constructor_args():
    sig = inspect.signature(draw2d::RoundedRectangle.__init__)
    params = list(sig.parameters.keys())
    assert "cornerDimensions" in params, "Missing parameter 'cornerDimensions'"

def test_draw2d::roundedrectangle_has_cornerDimensions():
    assert hasattr(draw2d::RoundedRectangle, "cornerDimensions")
    descriptor = None
    for klass in draw2d::RoundedRectangle.__mro__:
        if "cornerDimensions" in klass.__dict__:
            descriptor = klass.__dict__["cornerDimensions"]
            break
    assert isinstance(descriptor, property)



def test_draw2d::pointlistshape_is_not_abstract():
    assert not inspect.isabstract(draw2d::PointListShape)


def test_draw2d::pointlistshape_constructor_exists():
    assert callable(draw2d::PointListShape.__init__)


def test_draw2d::pointlistshape_constructor_args():
    sig = inspect.signature(draw2d::PointListShape.__init__)
    params = list(sig.parameters.keys())
    assert "pointList" in params, "Missing parameter 'pointList'"

def test_draw2d::pointlistshape_has_pointList():
    assert hasattr(draw2d::PointListShape, "pointList")
    descriptor = None
    for klass in draw2d::PointListShape.__mro__:
        if "pointList" in klass.__dict__:
            descriptor = klass.__dict__["pointList"]
            break
    assert isinstance(descriptor, property)



def test_draw2d::triangle_is_not_abstract():
    assert not inspect.isabstract(draw2d::Triangle)


def test_draw2d::triangle_constructor_exists():
    assert callable(draw2d::Triangle.__init__)


def test_draw2d::triangle_constructor_args():
    sig = inspect.signature(draw2d::Triangle.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "direction" in params, "Missing parameter 'direction'"

def test_draw2d::triangle_has_orientation():
    assert hasattr(draw2d::Triangle, "orientation")
    descriptor = None
    for klass in draw2d::Triangle.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::triangle_has_direction():
    assert hasattr(draw2d::Triangle, "direction")
    descriptor = None
    for klass in draw2d::Triangle.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_draw2d::ellipse_is_not_abstract():
    assert not inspect.isabstract(draw2d::Ellipse)


def test_draw2d::ellipse_constructor_exists():
    assert callable(draw2d::Ellipse.__init__)


def test_draw2d::ellipse_constructor_args():
    sig = inspect.signature(draw2d::Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_draw2d::rectanglefigure_is_not_abstract():
    assert not inspect.isabstract(draw2d::RectangleFigure)


def test_draw2d::rectanglefigure_constructor_exists():
    assert callable(draw2d::RectangleFigure.__init__)


def test_draw2d::rectanglefigure_constructor_args():
    sig = inspect.signature(draw2d::RectangleFigure.__init__)
    params = list(sig.parameters.keys())



def test_draw2d::figure_is_not_abstract():
    assert not inspect.isabstract(draw2d::Figure)


def test_draw2d::figure_constructor_exists():
    assert callable(draw2d::Figure.__init__)


def test_draw2d::figure_constructor_args():
    sig = inspect.signature(draw2d::Figure.__init__)
    params = list(sig.parameters.keys())
    assert "minimumSize" in params, "Missing parameter 'minimumSize'"
    assert "bounds" in params, "Missing parameter 'bounds'"
    assert "opaque" in params, "Missing parameter 'opaque'"
    assert "preferredSize" in params, "Missing parameter 'preferredSize'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "focusTraversable" in params, "Missing parameter 'focusTraversable'"
    assert "maximumSize" in params, "Missing parameter 'maximumSize'"
    assert "enabled" in params, "Missing parameter 'enabled'"

def test_draw2d::figure_has_minimumSize():
    assert hasattr(draw2d::Figure, "minimumSize")
    descriptor = None
    for klass in draw2d::Figure.__mro__:
        if "minimumSize" in klass.__dict__:
            descriptor = klass.__dict__["minimumSize"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::figure_has_bounds():
    assert hasattr(draw2d::Figure, "bounds")
    descriptor = None
    for klass in draw2d::Figure.__mro__:
        if "bounds" in klass.__dict__:
            descriptor = klass.__dict__["bounds"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::figure_has_opaque():
    assert hasattr(draw2d::Figure, "opaque")
    descriptor = None
    for klass in draw2d::Figure.__mro__:
        if "opaque" in klass.__dict__:
            descriptor = klass.__dict__["opaque"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::figure_has_preferredSize():
    assert hasattr(draw2d::Figure, "preferredSize")
    descriptor = None
    for klass in draw2d::Figure.__mro__:
        if "preferredSize" in klass.__dict__:
            descriptor = klass.__dict__["preferredSize"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::figure_has_visible():
    assert hasattr(draw2d::Figure, "visible")
    descriptor = None
    for klass in draw2d::Figure.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::figure_has_focusTraversable():
    assert hasattr(draw2d::Figure, "focusTraversable")
    descriptor = None
    for klass in draw2d::Figure.__mro__:
        if "focusTraversable" in klass.__dict__:
            descriptor = klass.__dict__["focusTraversable"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::figure_has_maximumSize():
    assert hasattr(draw2d::Figure, "maximumSize")
    descriptor = None
    for klass in draw2d::Figure.__mro__:
        if "maximumSize" in klass.__dict__:
            descriptor = klass.__dict__["maximumSize"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::figure_has_enabled():
    assert hasattr(draw2d::Figure, "enabled")
    descriptor = None
    for klass in draw2d::Figure.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)



def test_canvas_is_not_abstract():
    assert not inspect.isabstract(Canvas)


def test_canvas_constructor_exists():
    assert callable(Canvas.__init__)


def test_canvas_constructor_args():
    sig = inspect.signature(Canvas.__init__)
    params = list(sig.parameters.keys())



def test_draw2d::draw2dcanvas_is_not_abstract():
    assert not inspect.isabstract(draw2d::Draw2DCanvas)


def test_draw2d::draw2dcanvas_constructor_exists():
    assert callable(draw2d::Draw2DCanvas.__init__)


def test_draw2d::draw2dcanvas_constructor_args():
    sig = inspect.signature(draw2d::Draw2DCanvas.__init__)
    params = list(sig.parameters.keys())



def test_figure_is_not_abstract():
    assert not inspect.isabstract(Figure)


def test_figure_constructor_exists():
    assert callable(Figure.__init__)


def test_figure_constructor_args():
    sig = inspect.signature(Figure.__init__)
    params = list(sig.parameters.keys())



def test_draw2d::blockflow_is_not_abstract():
    assert not inspect.isabstract(draw2d::BlockFlow)


def test_draw2d::blockflow_constructor_exists():
    assert callable(draw2d::BlockFlow.__init__)


def test_draw2d::blockflow_constructor_args():
    sig = inspect.signature(draw2d::BlockFlow.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"

def test_draw2d::blockflow_has_orientation():
    assert hasattr(draw2d::BlockFlow, "orientation")
    descriptor = None
    for klass in draw2d::BlockFlow.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)



def test_draw2d::shape_is_not_abstract():
    assert not inspect.isabstract(draw2d::Shape)


def test_draw2d::shape_constructor_exists():
    assert callable(draw2d::Shape.__init__)


def test_draw2d::shape_constructor_args():
    sig = inspect.signature(draw2d::Shape.__init__)
    params = list(sig.parameters.keys())
    assert "fillXOR" in params, "Missing parameter 'fillXOR'"
    assert "lineJoin" in params, "Missing parameter 'lineJoin'"
    assert "lineDash" in params, "Missing parameter 'lineDash'"
    assert "lineDashOffset" in params, "Missing parameter 'lineDashOffset'"
    assert "lineWidthFloat" in params, "Missing parameter 'lineWidthFloat'"
    assert "outlineXOR" in params, "Missing parameter 'outlineXOR'"
    assert "antialias" in params, "Missing parameter 'antialias'"
    assert "lineCap" in params, "Missing parameter 'lineCap'"
    assert "lineMiterLimit" in params, "Missing parameter 'lineMiterLimit'"
    assert "fill" in params, "Missing parameter 'fill'"
    assert "outline" in params, "Missing parameter 'outline'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "alpha" in params, "Missing parameter 'alpha'"

def test_draw2d::shape_has_fillXOR():
    assert hasattr(draw2d::Shape, "fillXOR")
    descriptor = None
    for klass in draw2d::Shape.__mro__:
        if "fillXOR" in klass.__dict__:
            descriptor = klass.__dict__["fillXOR"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::shape_has_lineJoin():
    assert hasattr(draw2d::Shape, "lineJoin")
    descriptor = None
    for klass in draw2d::Shape.__mro__:
        if "lineJoin" in klass.__dict__:
            descriptor = klass.__dict__["lineJoin"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::shape_has_lineDash():
    assert hasattr(draw2d::Shape, "lineDash")
    descriptor = None
    for klass in draw2d::Shape.__mro__:
        if "lineDash" in klass.__dict__:
            descriptor = klass.__dict__["lineDash"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::shape_has_lineDashOffset():
    assert hasattr(draw2d::Shape, "lineDashOffset")
    descriptor = None
    for klass in draw2d::Shape.__mro__:
        if "lineDashOffset" in klass.__dict__:
            descriptor = klass.__dict__["lineDashOffset"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::shape_has_lineWidthFloat():
    assert hasattr(draw2d::Shape, "lineWidthFloat")
    descriptor = None
    for klass in draw2d::Shape.__mro__:
        if "lineWidthFloat" in klass.__dict__:
            descriptor = klass.__dict__["lineWidthFloat"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::shape_has_outlineXOR():
    assert hasattr(draw2d::Shape, "outlineXOR")
    descriptor = None
    for klass in draw2d::Shape.__mro__:
        if "outlineXOR" in klass.__dict__:
            descriptor = klass.__dict__["outlineXOR"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::shape_has_antialias():
    assert hasattr(draw2d::Shape, "antialias")
    descriptor = None
    for klass in draw2d::Shape.__mro__:
        if "antialias" in klass.__dict__:
            descriptor = klass.__dict__["antialias"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::shape_has_lineCap():
    assert hasattr(draw2d::Shape, "lineCap")
    descriptor = None
    for klass in draw2d::Shape.__mro__:
        if "lineCap" in klass.__dict__:
            descriptor = klass.__dict__["lineCap"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::shape_has_lineMiterLimit():
    assert hasattr(draw2d::Shape, "lineMiterLimit")
    descriptor = None
    for klass in draw2d::Shape.__mro__:
        if "lineMiterLimit" in klass.__dict__:
            descriptor = klass.__dict__["lineMiterLimit"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::shape_has_fill():
    assert hasattr(draw2d::Shape, "fill")
    descriptor = None
    for klass in draw2d::Shape.__mro__:
        if "fill" in klass.__dict__:
            descriptor = klass.__dict__["fill"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::shape_has_outline():
    assert hasattr(draw2d::Shape, "outline")
    descriptor = None
    for klass in draw2d::Shape.__mro__:
        if "outline" in klass.__dict__:
            descriptor = klass.__dict__["outline"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::shape_has_lineStyle():
    assert hasattr(draw2d::Shape, "lineStyle")
    descriptor = None
    for klass in draw2d::Shape.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::shape_has_alpha():
    assert hasattr(draw2d::Shape, "alpha")
    descriptor = None
    for klass in draw2d::Shape.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)



def test_draw2d::imagefigure_is_not_abstract():
    assert not inspect.isabstract(draw2d::ImageFigure)


def test_draw2d::imagefigure_constructor_exists():
    assert callable(draw2d::ImageFigure.__init__)


def test_draw2d::imagefigure_constructor_args():
    sig = inspect.signature(draw2d::ImageFigure.__init__)
    params = list(sig.parameters.keys())
    assert "image" in params, "Missing parameter 'image'"

def test_draw2d::imagefigure_has_image():
    assert hasattr(draw2d::ImageFigure, "image")
    descriptor = None
    for klass in draw2d::ImageFigure.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)



def test_draw2d::label_is_not_abstract():
    assert not inspect.isabstract(draw2d::Label)


def test_draw2d::label_constructor_exists():
    assert callable(draw2d::Label.__init__)


def test_draw2d::label_constructor_args():
    sig = inspect.signature(draw2d::Label.__init__)
    params = list(sig.parameters.keys())
    assert "iconAlignment" in params, "Missing parameter 'iconAlignment'"
    assert "text" in params, "Missing parameter 'text'"
    assert "iconTextGap" in params, "Missing parameter 'iconTextGap'"
    assert "icon" in params, "Missing parameter 'icon'"
    assert "textPlacement" in params, "Missing parameter 'textPlacement'"
    assert "textAlignment" in params, "Missing parameter 'textAlignment'"

def test_draw2d::label_has_iconAlignment():
    assert hasattr(draw2d::Label, "iconAlignment")
    descriptor = None
    for klass in draw2d::Label.__mro__:
        if "iconAlignment" in klass.__dict__:
            descriptor = klass.__dict__["iconAlignment"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::label_has_text():
    assert hasattr(draw2d::Label, "text")
    descriptor = None
    for klass in draw2d::Label.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::label_has_iconTextGap():
    assert hasattr(draw2d::Label, "iconTextGap")
    descriptor = None
    for klass in draw2d::Label.__mro__:
        if "iconTextGap" in klass.__dict__:
            descriptor = klass.__dict__["iconTextGap"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::label_has_icon():
    assert hasattr(draw2d::Label, "icon")
    descriptor = None
    for klass in draw2d::Label.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::label_has_textPlacement():
    assert hasattr(draw2d::Label, "textPlacement")
    descriptor = None
    for klass in draw2d::Label.__mro__:
        if "textPlacement" in klass.__dict__:
            descriptor = klass.__dict__["textPlacement"]
            break
    assert isinstance(descriptor, property)

def test_draw2d::label_has_textAlignment():
    assert hasattr(draw2d::Label, "textAlignment")
    descriptor = None
    for klass in draw2d::Label.__mro__:
        if "textAlignment" in klass.__dict__:
            descriptor = klass.__dict__["textAlignment"]
            break
    assert isinstance(descriptor, property)



def test_draw2d::border_is_not_abstract():
    assert not inspect.isabstract(draw2d::Border)


def test_draw2d::border_constructor_exists():
    assert callable(draw2d::Border.__init__)


def test_draw2d::border_constructor_args():
    sig = inspect.signature(draw2d::Border.__init__)
    params = list(sig.parameters.keys())
    assert "opaque" in params, "Missing parameter 'opaque'"

def test_draw2d::border_has_opaque():
    assert hasattr(draw2d::Border, "opaque")
    descriptor = None
    for klass in draw2d::Border.__mro__:
        if "opaque" in klass.__dict__:
            descriptor = klass.__dict__["opaque"]
            break
    assert isinstance(descriptor, property)



def test_draw2d::font_is_not_abstract():
    assert not inspect.isabstract(draw2d::Font)


def test_draw2d::font_constructor_exists():
    assert callable(draw2d::Font.__init__)


def test_draw2d::font_constructor_args():
    sig = inspect.signature(draw2d::Font.__init__)
    params = list(sig.parameters.keys())



def test_draw2d::color_is_not_abstract():
    assert not inspect.isabstract(draw2d::Color)


def test_draw2d::color_constructor_exists():
    assert callable(draw2d::Color.__init__)


def test_draw2d::color_constructor_args():
    sig = inspect.signature(draw2d::Color.__init__)
    params = list(sig.parameters.keys())

def test_alignment_exists():
    # Check that the Enumeration exists
    assert Alignment is not None

def test_alignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Alignment]
    expected_literals = [
        "TOP",
        "CENTER",
        "MIDDLE",
        "LEFT",
        "RIGHT",
        "BOTTOM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Alignment"

def test_orientation_exists():
    # Check that the Enumeration exists
    assert Orientation is not None

def test_orientation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Orientation]
    expected_literals = [
        "HORIZONTAL",
        "VERTICAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Orientation"

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "WEST",
        "SOUTH",
        "EAST",
        "NORTH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"


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
Border_strategy = st.builds(
    Border,
)
draw2d::LabeledBorder_strategy = st.builds(
    draw2d::LabeledBorder,
    label=
        safe_text
)
ConnectionAnchor_strategy = st.builds(
    ConnectionAnchor,
)
draw2d::XYAnchor_strategy = st.builds(
    draw2d::XYAnchor,
    location=
        safe_text
)
draw2d::ConnectionAnchor_strategy = st.builds(
    draw2d::ConnectionAnchor,
)
draw2d::FlowBorder_strategy = st.builds(
    draw2d::FlowBorder,
    bottomMargin=
        st.integers(),
    leftMargin=
        st.integers(),
    topMargin=
        st.integers(),
    rightMargin=
        st.integers()
)
ColoredLabeledBorder_strategy = st.builds(
    ColoredLabeledBorder,
)
draw2d::TitleBarBorder_strategy = st.builds(
    draw2d::TitleBarBorder,
)
draw2d::GroupBoxBorder_strategy = st.builds(
    draw2d::GroupBoxBorder,
)
LabeledBorder_strategy = st.builds(
    LabeledBorder,
)
draw2d::ColoredLabeledBorder_strategy = st.builds(
    draw2d::ColoredLabeledBorder,
)
draw2d::FrameBorder_strategy = st.builds(
    draw2d::FrameBorder,
)
Polyline_strategy = st.builds(
    Polyline,
)
draw2d::Polygon_strategy = st.builds(
    draw2d::Polygon,
)
PointListShape_strategy = st.builds(
    PointListShape,
)
draw2d::PolylineShape_strategy = st.builds(
    draw2d::PolylineShape,
    tolerance=
        st.integers()
)
draw2d::PolygonShape_strategy = st.builds(
    draw2d::PolygonShape,
)
draw2d::Polyline_strategy = st.builds(
    draw2d::Polyline,
    tolerance=
        st.integers()
)
Shape_strategy = st.builds(
    Shape,
)
draw2d::RoundedRectangle_strategy = st.builds(
    draw2d::RoundedRectangle,
    cornerDimensions=
        safe_text
)
draw2d::PointListShape_strategy = st.builds(
    draw2d::PointListShape,
    pointList=
        st.integers()
)
draw2d::Triangle_strategy = st.builds(
    draw2d::Triangle,
    orientation=
        safe_text,
    direction=
        safe_text
)
draw2d::Ellipse_strategy = st.builds(
    draw2d::Ellipse,
)
draw2d::RectangleFigure_strategy = st.builds(
    draw2d::RectangleFigure,
)
draw2d::Figure_strategy = st.builds(
    draw2d::Figure,
    minimumSize=
        safe_text,
    bounds=
        safe_text,
    opaque=
        st.booleans(),
    preferredSize=
        safe_text,
    visible=
        st.booleans(),
    focusTraversable=
        st.booleans(),
    maximumSize=
        safe_text,
    enabled=
        st.booleans()
)
Canvas_strategy = st.builds(
    Canvas,
)
draw2d::Draw2DCanvas_strategy = st.builds(
    draw2d::Draw2DCanvas,
)
Figure_strategy = st.builds(
    Figure,
)
draw2d::BlockFlow_strategy = st.builds(
    draw2d::BlockFlow,
    orientation=
        safe_text
)
draw2d::Shape_strategy = st.builds(
    draw2d::Shape,
    fillXOR=
        st.booleans(),
    lineJoin=
        safe_text,
    lineDash=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    lineDashOffset=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    lineWidthFloat=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    outlineXOR=
        st.booleans(),
    antialias=
        safe_text,
    lineCap=
        safe_text,
    lineMiterLimit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    fill=
        st.booleans(),
    outline=
        st.booleans(),
    lineStyle=
        safe_text,
    alpha=
        safe_text
)
draw2d::ImageFigure_strategy = st.builds(
    draw2d::ImageFigure,
    image=
        safe_text
)
draw2d::Label_strategy = st.builds(
    draw2d::Label,
    iconAlignment=
        safe_text,
    text=
        safe_text,
    iconTextGap=
        st.integers(),
    icon=
        safe_text,
    textPlacement=
        safe_text,
    textAlignment=
        safe_text
)
draw2d::Border_strategy = st.builds(
    draw2d::Border,
    opaque=
        st.booleans()
)
draw2d::Font_strategy = st.builds(
    draw2d::Font,
)
draw2d::Color_strategy = st.builds(
    draw2d::Color,
)

@given(instance=Border_strategy)
@settings(max_examples=50)
def test_border_instantiation(instance):
    assert isinstance(instance, Border)

@given(instance=draw2d::LabeledBorder_strategy)
@settings(max_examples=50)
def test_draw2d::labeledborder_instantiation(instance):
    assert isinstance(instance, draw2d::LabeledBorder)

@given(instance=draw2d::LabeledBorder_strategy)
def test_draw2d::labeledborder_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=draw2d::LabeledBorder_strategy)
def test_draw2d::labeledborder_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=ConnectionAnchor_strategy)
@settings(max_examples=50)
def test_connectionanchor_instantiation(instance):
    assert isinstance(instance, ConnectionAnchor)

@given(instance=draw2d::XYAnchor_strategy)
@settings(max_examples=50)
def test_draw2d::xyanchor_instantiation(instance):
    assert isinstance(instance, draw2d::XYAnchor)

@given(instance=draw2d::XYAnchor_strategy)
def test_draw2d::xyanchor_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=draw2d::XYAnchor_strategy)
def test_draw2d::xyanchor_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=draw2d::ConnectionAnchor_strategy)
@settings(max_examples=50)
def test_draw2d::connectionanchor_instantiation(instance):
    assert isinstance(instance, draw2d::ConnectionAnchor)

@given(instance=draw2d::FlowBorder_strategy)
@settings(max_examples=50)
def test_draw2d::flowborder_instantiation(instance):
    assert isinstance(instance, draw2d::FlowBorder)

@given(instance=draw2d::FlowBorder_strategy)
def test_draw2d::flowborder_bottomMargin_type(instance):
    assert isinstance(instance.bottomMargin, int)


@given(instance=draw2d::FlowBorder_strategy)
def test_draw2d::flowborder_bottomMargin_setter(instance):
    original = instance.bottomMargin
    instance.bottomMargin = original
    assert instance.bottomMargin == original

@given(instance=draw2d::FlowBorder_strategy)
def test_draw2d::flowborder_leftMargin_type(instance):
    assert isinstance(instance.leftMargin, int)


@given(instance=draw2d::FlowBorder_strategy)
def test_draw2d::flowborder_leftMargin_setter(instance):
    original = instance.leftMargin
    instance.leftMargin = original
    assert instance.leftMargin == original

@given(instance=draw2d::FlowBorder_strategy)
def test_draw2d::flowborder_topMargin_type(instance):
    assert isinstance(instance.topMargin, int)


@given(instance=draw2d::FlowBorder_strategy)
def test_draw2d::flowborder_topMargin_setter(instance):
    original = instance.topMargin
    instance.topMargin = original
    assert instance.topMargin == original

@given(instance=draw2d::FlowBorder_strategy)
def test_draw2d::flowborder_rightMargin_type(instance):
    assert isinstance(instance.rightMargin, int)


@given(instance=draw2d::FlowBorder_strategy)
def test_draw2d::flowborder_rightMargin_setter(instance):
    original = instance.rightMargin
    instance.rightMargin = original
    assert instance.rightMargin == original

@given(instance=ColoredLabeledBorder_strategy)
@settings(max_examples=50)
def test_coloredlabeledborder_instantiation(instance):
    assert isinstance(instance, ColoredLabeledBorder)

@given(instance=draw2d::TitleBarBorder_strategy)
@settings(max_examples=50)
def test_draw2d::titlebarborder_instantiation(instance):
    assert isinstance(instance, draw2d::TitleBarBorder)

@given(instance=draw2d::GroupBoxBorder_strategy)
@settings(max_examples=50)
def test_draw2d::groupboxborder_instantiation(instance):
    assert isinstance(instance, draw2d::GroupBoxBorder)

@given(instance=LabeledBorder_strategy)
@settings(max_examples=50)
def test_labeledborder_instantiation(instance):
    assert isinstance(instance, LabeledBorder)

@given(instance=draw2d::ColoredLabeledBorder_strategy)
@settings(max_examples=50)
def test_draw2d::coloredlabeledborder_instantiation(instance):
    assert isinstance(instance, draw2d::ColoredLabeledBorder)

@given(instance=draw2d::FrameBorder_strategy)
@settings(max_examples=50)
def test_draw2d::frameborder_instantiation(instance):
    assert isinstance(instance, draw2d::FrameBorder)

@given(instance=Polyline_strategy)
@settings(max_examples=50)
def test_polyline_instantiation(instance):
    assert isinstance(instance, Polyline)

@given(instance=draw2d::Polygon_strategy)
@settings(max_examples=50)
def test_draw2d::polygon_instantiation(instance):
    assert isinstance(instance, draw2d::Polygon)

@given(instance=PointListShape_strategy)
@settings(max_examples=50)
def test_pointlistshape_instantiation(instance):
    assert isinstance(instance, PointListShape)

@given(instance=draw2d::PolylineShape_strategy)
@settings(max_examples=50)
def test_draw2d::polylineshape_instantiation(instance):
    assert isinstance(instance, draw2d::PolylineShape)

@given(instance=draw2d::PolylineShape_strategy)
def test_draw2d::polylineshape_tolerance_type(instance):
    assert isinstance(instance.tolerance, int)


@given(instance=draw2d::PolylineShape_strategy)
def test_draw2d::polylineshape_tolerance_setter(instance):
    original = instance.tolerance
    instance.tolerance = original
    assert instance.tolerance == original

@given(instance=draw2d::PolygonShape_strategy)
@settings(max_examples=50)
def test_draw2d::polygonshape_instantiation(instance):
    assert isinstance(instance, draw2d::PolygonShape)

@given(instance=draw2d::Polyline_strategy)
@settings(max_examples=50)
def test_draw2d::polyline_instantiation(instance):
    assert isinstance(instance, draw2d::Polyline)

@given(instance=draw2d::Polyline_strategy)
def test_draw2d::polyline_tolerance_type(instance):
    assert isinstance(instance.tolerance, int)


@given(instance=draw2d::Polyline_strategy)
def test_draw2d::polyline_tolerance_setter(instance):
    original = instance.tolerance
    instance.tolerance = original
    assert instance.tolerance == original

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=draw2d::RoundedRectangle_strategy)
@settings(max_examples=50)
def test_draw2d::roundedrectangle_instantiation(instance):
    assert isinstance(instance, draw2d::RoundedRectangle)

@given(instance=draw2d::RoundedRectangle_strategy)
def test_draw2d::roundedrectangle_cornerDimensions_type(instance):
    assert isinstance(instance.cornerDimensions, str)


@given(instance=draw2d::RoundedRectangle_strategy)
def test_draw2d::roundedrectangle_cornerDimensions_setter(instance):
    original = instance.cornerDimensions
    instance.cornerDimensions = original
    assert instance.cornerDimensions == original

@given(instance=draw2d::PointListShape_strategy)
@settings(max_examples=50)
def test_draw2d::pointlistshape_instantiation(instance):
    assert isinstance(instance, draw2d::PointListShape)

@given(instance=draw2d::PointListShape_strategy)
def test_draw2d::pointlistshape_pointList_type(instance):
    assert isinstance(instance.pointList, int)


@given(instance=draw2d::PointListShape_strategy)
def test_draw2d::pointlistshape_pointList_setter(instance):
    original = instance.pointList
    instance.pointList = original
    assert instance.pointList == original

@given(instance=draw2d::Triangle_strategy)
@settings(max_examples=50)
def test_draw2d::triangle_instantiation(instance):
    assert isinstance(instance, draw2d::Triangle)

@given(instance=draw2d::Triangle_strategy)
def test_draw2d::triangle_orientation_type(instance):
    assert isinstance(instance.orientation, str)


@given(instance=draw2d::Triangle_strategy)
def test_draw2d::triangle_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=draw2d::Triangle_strategy)
def test_draw2d::triangle_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=draw2d::Triangle_strategy)
def test_draw2d::triangle_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=draw2d::Ellipse_strategy)
@settings(max_examples=50)
def test_draw2d::ellipse_instantiation(instance):
    assert isinstance(instance, draw2d::Ellipse)

@given(instance=draw2d::RectangleFigure_strategy)
@settings(max_examples=50)
def test_draw2d::rectanglefigure_instantiation(instance):
    assert isinstance(instance, draw2d::RectangleFigure)

@given(instance=draw2d::Figure_strategy)
@settings(max_examples=50)
def test_draw2d::figure_instantiation(instance):
    assert isinstance(instance, draw2d::Figure)

@given(instance=draw2d::Figure_strategy)
def test_draw2d::figure_minimumSize_type(instance):
    assert isinstance(instance.minimumSize, str)


@given(instance=draw2d::Figure_strategy)
def test_draw2d::figure_minimumSize_setter(instance):
    original = instance.minimumSize
    instance.minimumSize = original
    assert instance.minimumSize == original

@given(instance=draw2d::Figure_strategy)
def test_draw2d::figure_bounds_type(instance):
    assert isinstance(instance.bounds, str)


@given(instance=draw2d::Figure_strategy)
def test_draw2d::figure_bounds_setter(instance):
    original = instance.bounds
    instance.bounds = original
    assert instance.bounds == original

@given(instance=draw2d::Figure_strategy)
def test_draw2d::figure_opaque_type(instance):
    assert isinstance(instance.opaque, bool)


@given(instance=draw2d::Figure_strategy)
def test_draw2d::figure_opaque_setter(instance):
    original = instance.opaque
    instance.opaque = original
    assert instance.opaque == original

@given(instance=draw2d::Figure_strategy)
def test_draw2d::figure_preferredSize_type(instance):
    assert isinstance(instance.preferredSize, str)


@given(instance=draw2d::Figure_strategy)
def test_draw2d::figure_preferredSize_setter(instance):
    original = instance.preferredSize
    instance.preferredSize = original
    assert instance.preferredSize == original

@given(instance=draw2d::Figure_strategy)
def test_draw2d::figure_visible_type(instance):
    assert isinstance(instance.visible, bool)


@given(instance=draw2d::Figure_strategy)
def test_draw2d::figure_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=draw2d::Figure_strategy)
def test_draw2d::figure_focusTraversable_type(instance):
    assert isinstance(instance.focusTraversable, bool)


@given(instance=draw2d::Figure_strategy)
def test_draw2d::figure_focusTraversable_setter(instance):
    original = instance.focusTraversable
    instance.focusTraversable = original
    assert instance.focusTraversable == original

@given(instance=draw2d::Figure_strategy)
def test_draw2d::figure_maximumSize_type(instance):
    assert isinstance(instance.maximumSize, str)


@given(instance=draw2d::Figure_strategy)
def test_draw2d::figure_maximumSize_setter(instance):
    original = instance.maximumSize
    instance.maximumSize = original
    assert instance.maximumSize == original

@given(instance=draw2d::Figure_strategy)
def test_draw2d::figure_enabled_type(instance):
    assert isinstance(instance.enabled, bool)


@given(instance=draw2d::Figure_strategy)
def test_draw2d::figure_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original

@given(instance=Canvas_strategy)
@settings(max_examples=50)
def test_canvas_instantiation(instance):
    assert isinstance(instance, Canvas)

@given(instance=draw2d::Draw2DCanvas_strategy)
@settings(max_examples=50)
def test_draw2d::draw2dcanvas_instantiation(instance):
    assert isinstance(instance, draw2d::Draw2DCanvas)

@given(instance=Figure_strategy)
@settings(max_examples=50)
def test_figure_instantiation(instance):
    assert isinstance(instance, Figure)

@given(instance=draw2d::BlockFlow_strategy)
@settings(max_examples=50)
def test_draw2d::blockflow_instantiation(instance):
    assert isinstance(instance, draw2d::BlockFlow)

@given(instance=draw2d::BlockFlow_strategy)
def test_draw2d::blockflow_orientation_type(instance):
    assert isinstance(instance.orientation, str)


@given(instance=draw2d::BlockFlow_strategy)
def test_draw2d::blockflow_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=draw2d::Shape_strategy)
@settings(max_examples=50)
def test_draw2d::shape_instantiation(instance):
    assert isinstance(instance, draw2d::Shape)

@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_fillXOR_type(instance):
    assert isinstance(instance.fillXOR, bool)


@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_fillXOR_setter(instance):
    original = instance.fillXOR
    instance.fillXOR = original
    assert instance.fillXOR == original

@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_lineJoin_type(instance):
    assert isinstance(instance.lineJoin, str)


@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_lineJoin_setter(instance):
    original = instance.lineJoin
    instance.lineJoin = original
    assert instance.lineJoin == original

@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_lineDash_type(instance):
    assert isinstance(instance.lineDash, float)


@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_lineDash_setter(instance):
    original = instance.lineDash
    instance.lineDash = original
    assert instance.lineDash == original

@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_lineDashOffset_type(instance):
    assert isinstance(instance.lineDashOffset, float)


@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_lineDashOffset_setter(instance):
    original = instance.lineDashOffset
    instance.lineDashOffset = original
    assert instance.lineDashOffset == original

@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_lineWidthFloat_type(instance):
    assert isinstance(instance.lineWidthFloat, float)


@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_lineWidthFloat_setter(instance):
    original = instance.lineWidthFloat
    instance.lineWidthFloat = original
    assert instance.lineWidthFloat == original

@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_outlineXOR_type(instance):
    assert isinstance(instance.outlineXOR, bool)


@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_outlineXOR_setter(instance):
    original = instance.outlineXOR
    instance.outlineXOR = original
    assert instance.outlineXOR == original

@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_antialias_type(instance):
    assert isinstance(instance.antialias, str)


@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_antialias_setter(instance):
    original = instance.antialias
    instance.antialias = original
    assert instance.antialias == original

@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_lineCap_type(instance):
    assert isinstance(instance.lineCap, str)


@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_lineCap_setter(instance):
    original = instance.lineCap
    instance.lineCap = original
    assert instance.lineCap == original

@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_lineMiterLimit_type(instance):
    assert isinstance(instance.lineMiterLimit, float)


@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_lineMiterLimit_setter(instance):
    original = instance.lineMiterLimit
    instance.lineMiterLimit = original
    assert instance.lineMiterLimit == original

@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_fill_type(instance):
    assert isinstance(instance.fill, bool)


@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_fill_setter(instance):
    original = instance.fill
    instance.fill = original
    assert instance.fill == original

@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_outline_type(instance):
    assert isinstance(instance.outline, bool)


@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_outline_setter(instance):
    original = instance.outline
    instance.outline = original
    assert instance.outline == original

@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_lineStyle_type(instance):
    assert isinstance(instance.lineStyle, str)


@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original

@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_alpha_type(instance):
    assert isinstance(instance.alpha, str)


@given(instance=draw2d::Shape_strategy)
def test_draw2d::shape_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original

@given(instance=draw2d::ImageFigure_strategy)
@settings(max_examples=50)
def test_draw2d::imagefigure_instantiation(instance):
    assert isinstance(instance, draw2d::ImageFigure)

@given(instance=draw2d::ImageFigure_strategy)
def test_draw2d::imagefigure_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=draw2d::ImageFigure_strategy)
def test_draw2d::imagefigure_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=draw2d::Label_strategy)
@settings(max_examples=50)
def test_draw2d::label_instantiation(instance):
    assert isinstance(instance, draw2d::Label)

@given(instance=draw2d::Label_strategy)
def test_draw2d::label_iconAlignment_type(instance):
    assert isinstance(instance.iconAlignment, str)


@given(instance=draw2d::Label_strategy)
def test_draw2d::label_iconAlignment_setter(instance):
    original = instance.iconAlignment
    instance.iconAlignment = original
    assert instance.iconAlignment == original

@given(instance=draw2d::Label_strategy)
def test_draw2d::label_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=draw2d::Label_strategy)
def test_draw2d::label_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=draw2d::Label_strategy)
def test_draw2d::label_iconTextGap_type(instance):
    assert isinstance(instance.iconTextGap, int)


@given(instance=draw2d::Label_strategy)
def test_draw2d::label_iconTextGap_setter(instance):
    original = instance.iconTextGap
    instance.iconTextGap = original
    assert instance.iconTextGap == original

@given(instance=draw2d::Label_strategy)
def test_draw2d::label_icon_type(instance):
    assert isinstance(instance.icon, str)


@given(instance=draw2d::Label_strategy)
def test_draw2d::label_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=draw2d::Label_strategy)
def test_draw2d::label_textPlacement_type(instance):
    assert isinstance(instance.textPlacement, str)


@given(instance=draw2d::Label_strategy)
def test_draw2d::label_textPlacement_setter(instance):
    original = instance.textPlacement
    instance.textPlacement = original
    assert instance.textPlacement == original

@given(instance=draw2d::Label_strategy)
def test_draw2d::label_textAlignment_type(instance):
    assert isinstance(instance.textAlignment, str)


@given(instance=draw2d::Label_strategy)
def test_draw2d::label_textAlignment_setter(instance):
    original = instance.textAlignment
    instance.textAlignment = original
    assert instance.textAlignment == original

@given(instance=draw2d::Border_strategy)
@settings(max_examples=50)
def test_draw2d::border_instantiation(instance):
    assert isinstance(instance, draw2d::Border)

@given(instance=draw2d::Border_strategy)
def test_draw2d::border_opaque_type(instance):
    assert isinstance(instance.opaque, bool)


@given(instance=draw2d::Border_strategy)
def test_draw2d::border_opaque_setter(instance):
    original = instance.opaque
    instance.opaque = original
    assert instance.opaque == original

@given(instance=draw2d::Font_strategy)
@settings(max_examples=50)
def test_draw2d::font_instantiation(instance):
    assert isinstance(instance, draw2d::Font)

@given(instance=draw2d::Color_strategy)
@settings(max_examples=50)
def test_draw2d::color_instantiation(instance):
    assert isinstance(instance, draw2d::Color)
