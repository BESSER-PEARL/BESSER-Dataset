import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Border,
    draw2d_LabeledBorder,
    ConnectionAnchor,
    draw2d_XYAnchor,
    draw2d_ConnectionAnchor,
    draw2d_FlowBorder,
    ColoredLabeledBorder,
    draw2d_TitleBarBorder,
    draw2d_GroupBoxBorder,
    LabeledBorder,
    draw2d_ColoredLabeledBorder,
    draw2d_FrameBorder,
    Polyline,
    draw2d_Polygon,
    PointListShape,
    draw2d_PolygonShape,
    draw2d_PolylineShape,
    draw2d_Polyline,
    Shape,
    draw2d_Ellipse,
    draw2d_RoundedRectangle,
    draw2d_Triangle,
    draw2d_PointListShape,
    draw2d_RectangleFigure,
    draw2d_Figure,
    Canvas,
    draw2d_Draw2DCanvas,
    Figure,
    draw2d_ImageFigure,
    draw2d_Shape,
    draw2d_BlockFlow,
    draw2d_Label,
    draw2d_Border,
    draw2d_Font,
    draw2d_Color,
    Direction,
    Alignment,
    Orientation,
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



def test_draw2d_labeledborder_is_not_abstract():
    assert not inspect.isabstract(draw2d_LabeledBorder)


def test_draw2d_labeledborder_constructor_exists():
    assert callable(draw2d_LabeledBorder.__init__)


def test_draw2d_labeledborder_constructor_args():
    sig = inspect.signature(draw2d_LabeledBorder.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_draw2d_labeledborder_has_label():
    assert hasattr(draw2d_LabeledBorder, "label")
    descriptor = None
    for klass in draw2d_LabeledBorder.__mro__:
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



def test_draw2d_xyanchor_is_not_abstract():
    assert not inspect.isabstract(draw2d_XYAnchor)


def test_draw2d_xyanchor_constructor_exists():
    assert callable(draw2d_XYAnchor.__init__)


def test_draw2d_xyanchor_constructor_args():
    sig = inspect.signature(draw2d_XYAnchor.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_draw2d_xyanchor_has_location():
    assert hasattr(draw2d_XYAnchor, "location")
    descriptor = None
    for klass in draw2d_XYAnchor.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_draw2d_connectionanchor_is_not_abstract():
    assert not inspect.isabstract(draw2d_ConnectionAnchor)


def test_draw2d_connectionanchor_constructor_exists():
    assert callable(draw2d_ConnectionAnchor.__init__)


def test_draw2d_connectionanchor_constructor_args():
    sig = inspect.signature(draw2d_ConnectionAnchor.__init__)
    params = list(sig.parameters.keys())



def test_draw2d_flowborder_is_not_abstract():
    assert not inspect.isabstract(draw2d_FlowBorder)


def test_draw2d_flowborder_constructor_exists():
    assert callable(draw2d_FlowBorder.__init__)


def test_draw2d_flowborder_constructor_args():
    sig = inspect.signature(draw2d_FlowBorder.__init__)
    params = list(sig.parameters.keys())
    assert "bottomMargin" in params, "Missing parameter 'bottomMargin'"
    assert "rightMargin" in params, "Missing parameter 'rightMargin'"
    assert "leftMargin" in params, "Missing parameter 'leftMargin'"
    assert "topMargin" in params, "Missing parameter 'topMargin'"

def test_draw2d_flowborder_has_bottomMargin():
    assert hasattr(draw2d_FlowBorder, "bottomMargin")
    descriptor = None
    for klass in draw2d_FlowBorder.__mro__:
        if "bottomMargin" in klass.__dict__:
            descriptor = klass.__dict__["bottomMargin"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_flowborder_has_rightMargin():
    assert hasattr(draw2d_FlowBorder, "rightMargin")
    descriptor = None
    for klass in draw2d_FlowBorder.__mro__:
        if "rightMargin" in klass.__dict__:
            descriptor = klass.__dict__["rightMargin"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_flowborder_has_leftMargin():
    assert hasattr(draw2d_FlowBorder, "leftMargin")
    descriptor = None
    for klass in draw2d_FlowBorder.__mro__:
        if "leftMargin" in klass.__dict__:
            descriptor = klass.__dict__["leftMargin"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_flowborder_has_topMargin():
    assert hasattr(draw2d_FlowBorder, "topMargin")
    descriptor = None
    for klass in draw2d_FlowBorder.__mro__:
        if "topMargin" in klass.__dict__:
            descriptor = klass.__dict__["topMargin"]
            break
    assert isinstance(descriptor, property)



def test_coloredlabeledborder_is_not_abstract():
    assert not inspect.isabstract(ColoredLabeledBorder)


def test_coloredlabeledborder_constructor_exists():
    assert callable(ColoredLabeledBorder.__init__)


def test_coloredlabeledborder_constructor_args():
    sig = inspect.signature(ColoredLabeledBorder.__init__)
    params = list(sig.parameters.keys())



def test_draw2d_titlebarborder_is_not_abstract():
    assert not inspect.isabstract(draw2d_TitleBarBorder)


def test_draw2d_titlebarborder_constructor_exists():
    assert callable(draw2d_TitleBarBorder.__init__)


def test_draw2d_titlebarborder_constructor_args():
    sig = inspect.signature(draw2d_TitleBarBorder.__init__)
    params = list(sig.parameters.keys())



def test_draw2d_groupboxborder_is_not_abstract():
    assert not inspect.isabstract(draw2d_GroupBoxBorder)


def test_draw2d_groupboxborder_constructor_exists():
    assert callable(draw2d_GroupBoxBorder.__init__)


def test_draw2d_groupboxborder_constructor_args():
    sig = inspect.signature(draw2d_GroupBoxBorder.__init__)
    params = list(sig.parameters.keys())



def test_labeledborder_is_not_abstract():
    assert not inspect.isabstract(LabeledBorder)


def test_labeledborder_constructor_exists():
    assert callable(LabeledBorder.__init__)


def test_labeledborder_constructor_args():
    sig = inspect.signature(LabeledBorder.__init__)
    params = list(sig.parameters.keys())



def test_draw2d_coloredlabeledborder_is_not_abstract():
    assert not inspect.isabstract(draw2d_ColoredLabeledBorder)


def test_draw2d_coloredlabeledborder_constructor_exists():
    assert callable(draw2d_ColoredLabeledBorder.__init__)


def test_draw2d_coloredlabeledborder_constructor_args():
    sig = inspect.signature(draw2d_ColoredLabeledBorder.__init__)
    params = list(sig.parameters.keys())



def test_draw2d_frameborder_is_not_abstract():
    assert not inspect.isabstract(draw2d_FrameBorder)


def test_draw2d_frameborder_constructor_exists():
    assert callable(draw2d_FrameBorder.__init__)


def test_draw2d_frameborder_constructor_args():
    sig = inspect.signature(draw2d_FrameBorder.__init__)
    params = list(sig.parameters.keys())



def test_polyline_is_not_abstract():
    assert not inspect.isabstract(Polyline)


def test_polyline_constructor_exists():
    assert callable(Polyline.__init__)


def test_polyline_constructor_args():
    sig = inspect.signature(Polyline.__init__)
    params = list(sig.parameters.keys())



def test_draw2d_polygon_is_not_abstract():
    assert not inspect.isabstract(draw2d_Polygon)


def test_draw2d_polygon_constructor_exists():
    assert callable(draw2d_Polygon.__init__)


def test_draw2d_polygon_constructor_args():
    sig = inspect.signature(draw2d_Polygon.__init__)
    params = list(sig.parameters.keys())



def test_pointlistshape_is_not_abstract():
    assert not inspect.isabstract(PointListShape)


def test_pointlistshape_constructor_exists():
    assert callable(PointListShape.__init__)


def test_pointlistshape_constructor_args():
    sig = inspect.signature(PointListShape.__init__)
    params = list(sig.parameters.keys())



def test_draw2d_polygonshape_is_not_abstract():
    assert not inspect.isabstract(draw2d_PolygonShape)


def test_draw2d_polygonshape_constructor_exists():
    assert callable(draw2d_PolygonShape.__init__)


def test_draw2d_polygonshape_constructor_args():
    sig = inspect.signature(draw2d_PolygonShape.__init__)
    params = list(sig.parameters.keys())



def test_draw2d_polylineshape_is_not_abstract():
    assert not inspect.isabstract(draw2d_PolylineShape)


def test_draw2d_polylineshape_constructor_exists():
    assert callable(draw2d_PolylineShape.__init__)


def test_draw2d_polylineshape_constructor_args():
    sig = inspect.signature(draw2d_PolylineShape.__init__)
    params = list(sig.parameters.keys())
    assert "tolerance" in params, "Missing parameter 'tolerance'"

def test_draw2d_polylineshape_has_tolerance():
    assert hasattr(draw2d_PolylineShape, "tolerance")
    descriptor = None
    for klass in draw2d_PolylineShape.__mro__:
        if "tolerance" in klass.__dict__:
            descriptor = klass.__dict__["tolerance"]
            break
    assert isinstance(descriptor, property)



def test_draw2d_polyline_is_not_abstract():
    assert not inspect.isabstract(draw2d_Polyline)


def test_draw2d_polyline_constructor_exists():
    assert callable(draw2d_Polyline.__init__)


def test_draw2d_polyline_constructor_args():
    sig = inspect.signature(draw2d_Polyline.__init__)
    params = list(sig.parameters.keys())
    assert "tolerance" in params, "Missing parameter 'tolerance'"

def test_draw2d_polyline_has_tolerance():
    assert hasattr(draw2d_Polyline, "tolerance")
    descriptor = None
    for klass in draw2d_Polyline.__mro__:
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



def test_draw2d_ellipse_is_not_abstract():
    assert not inspect.isabstract(draw2d_Ellipse)


def test_draw2d_ellipse_constructor_exists():
    assert callable(draw2d_Ellipse.__init__)


def test_draw2d_ellipse_constructor_args():
    sig = inspect.signature(draw2d_Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_draw2d_roundedrectangle_is_not_abstract():
    assert not inspect.isabstract(draw2d_RoundedRectangle)


def test_draw2d_roundedrectangle_constructor_exists():
    assert callable(draw2d_RoundedRectangle.__init__)


def test_draw2d_roundedrectangle_constructor_args():
    sig = inspect.signature(draw2d_RoundedRectangle.__init__)
    params = list(sig.parameters.keys())
    assert "cornerDimensions" in params, "Missing parameter 'cornerDimensions'"

def test_draw2d_roundedrectangle_has_cornerDimensions():
    assert hasattr(draw2d_RoundedRectangle, "cornerDimensions")
    descriptor = None
    for klass in draw2d_RoundedRectangle.__mro__:
        if "cornerDimensions" in klass.__dict__:
            descriptor = klass.__dict__["cornerDimensions"]
            break
    assert isinstance(descriptor, property)



def test_draw2d_triangle_is_not_abstract():
    assert not inspect.isabstract(draw2d_Triangle)


def test_draw2d_triangle_constructor_exists():
    assert callable(draw2d_Triangle.__init__)


def test_draw2d_triangle_constructor_args():
    sig = inspect.signature(draw2d_Triangle.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "direction" in params, "Missing parameter 'direction'"

def test_draw2d_triangle_has_orientation():
    assert hasattr(draw2d_Triangle, "orientation")
    descriptor = None
    for klass in draw2d_Triangle.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_triangle_has_direction():
    assert hasattr(draw2d_Triangle, "direction")
    descriptor = None
    for klass in draw2d_Triangle.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_draw2d_pointlistshape_is_not_abstract():
    assert not inspect.isabstract(draw2d_PointListShape)


def test_draw2d_pointlistshape_constructor_exists():
    assert callable(draw2d_PointListShape.__init__)


def test_draw2d_pointlistshape_constructor_args():
    sig = inspect.signature(draw2d_PointListShape.__init__)
    params = list(sig.parameters.keys())
    assert "pointList" in params, "Missing parameter 'pointList'"

def test_draw2d_pointlistshape_has_pointList():
    assert hasattr(draw2d_PointListShape, "pointList")
    descriptor = None
    for klass in draw2d_PointListShape.__mro__:
        if "pointList" in klass.__dict__:
            descriptor = klass.__dict__["pointList"]
            break
    assert isinstance(descriptor, property)



def test_draw2d_rectanglefigure_is_not_abstract():
    assert not inspect.isabstract(draw2d_RectangleFigure)


def test_draw2d_rectanglefigure_constructor_exists():
    assert callable(draw2d_RectangleFigure.__init__)


def test_draw2d_rectanglefigure_constructor_args():
    sig = inspect.signature(draw2d_RectangleFigure.__init__)
    params = list(sig.parameters.keys())



def test_draw2d_figure_is_not_abstract():
    assert not inspect.isabstract(draw2d_Figure)


def test_draw2d_figure_constructor_exists():
    assert callable(draw2d_Figure.__init__)


def test_draw2d_figure_constructor_args():
    sig = inspect.signature(draw2d_Figure.__init__)
    params = list(sig.parameters.keys())
    assert "focusTraversable" in params, "Missing parameter 'focusTraversable'"
    assert "minimumSize" in params, "Missing parameter 'minimumSize'"
    assert "maximumSize" in params, "Missing parameter 'maximumSize'"
    assert "preferredSize" in params, "Missing parameter 'preferredSize'"
    assert "bounds" in params, "Missing parameter 'bounds'"
    assert "enabled" in params, "Missing parameter 'enabled'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "opaque" in params, "Missing parameter 'opaque'"

def test_draw2d_figure_has_focusTraversable():
    assert hasattr(draw2d_Figure, "focusTraversable")
    descriptor = None
    for klass in draw2d_Figure.__mro__:
        if "focusTraversable" in klass.__dict__:
            descriptor = klass.__dict__["focusTraversable"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_figure_has_minimumSize():
    assert hasattr(draw2d_Figure, "minimumSize")
    descriptor = None
    for klass in draw2d_Figure.__mro__:
        if "minimumSize" in klass.__dict__:
            descriptor = klass.__dict__["minimumSize"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_figure_has_maximumSize():
    assert hasattr(draw2d_Figure, "maximumSize")
    descriptor = None
    for klass in draw2d_Figure.__mro__:
        if "maximumSize" in klass.__dict__:
            descriptor = klass.__dict__["maximumSize"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_figure_has_preferredSize():
    assert hasattr(draw2d_Figure, "preferredSize")
    descriptor = None
    for klass in draw2d_Figure.__mro__:
        if "preferredSize" in klass.__dict__:
            descriptor = klass.__dict__["preferredSize"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_figure_has_bounds():
    assert hasattr(draw2d_Figure, "bounds")
    descriptor = None
    for klass in draw2d_Figure.__mro__:
        if "bounds" in klass.__dict__:
            descriptor = klass.__dict__["bounds"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_figure_has_enabled():
    assert hasattr(draw2d_Figure, "enabled")
    descriptor = None
    for klass in draw2d_Figure.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_figure_has_visible():
    assert hasattr(draw2d_Figure, "visible")
    descriptor = None
    for klass in draw2d_Figure.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_figure_has_opaque():
    assert hasattr(draw2d_Figure, "opaque")
    descriptor = None
    for klass in draw2d_Figure.__mro__:
        if "opaque" in klass.__dict__:
            descriptor = klass.__dict__["opaque"]
            break
    assert isinstance(descriptor, property)



def test_canvas_is_not_abstract():
    assert not inspect.isabstract(Canvas)


def test_canvas_constructor_exists():
    assert callable(Canvas.__init__)


def test_canvas_constructor_args():
    sig = inspect.signature(Canvas.__init__)
    params = list(sig.parameters.keys())



def test_draw2d_draw2dcanvas_is_not_abstract():
    assert not inspect.isabstract(draw2d_Draw2DCanvas)


def test_draw2d_draw2dcanvas_constructor_exists():
    assert callable(draw2d_Draw2DCanvas.__init__)


def test_draw2d_draw2dcanvas_constructor_args():
    sig = inspect.signature(draw2d_Draw2DCanvas.__init__)
    params = list(sig.parameters.keys())



def test_figure_is_not_abstract():
    assert not inspect.isabstract(Figure)


def test_figure_constructor_exists():
    assert callable(Figure.__init__)


def test_figure_constructor_args():
    sig = inspect.signature(Figure.__init__)
    params = list(sig.parameters.keys())



def test_draw2d_imagefigure_is_not_abstract():
    assert not inspect.isabstract(draw2d_ImageFigure)


def test_draw2d_imagefigure_constructor_exists():
    assert callable(draw2d_ImageFigure.__init__)


def test_draw2d_imagefigure_constructor_args():
    sig = inspect.signature(draw2d_ImageFigure.__init__)
    params = list(sig.parameters.keys())
    assert "image" in params, "Missing parameter 'image'"

def test_draw2d_imagefigure_has_image():
    assert hasattr(draw2d_ImageFigure, "image")
    descriptor = None
    for klass in draw2d_ImageFigure.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)



def test_draw2d_shape_is_not_abstract():
    assert not inspect.isabstract(draw2d_Shape)


def test_draw2d_shape_constructor_exists():
    assert callable(draw2d_Shape.__init__)


def test_draw2d_shape_constructor_args():
    sig = inspect.signature(draw2d_Shape.__init__)
    params = list(sig.parameters.keys())
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "fill" in params, "Missing parameter 'fill'"
    assert "lineWidthFloat" in params, "Missing parameter 'lineWidthFloat'"
    assert "lineMiterLimit" in params, "Missing parameter 'lineMiterLimit'"
    assert "lineDash" in params, "Missing parameter 'lineDash'"
    assert "lineJoin" in params, "Missing parameter 'lineJoin'"
    assert "lineCap" in params, "Missing parameter 'lineCap'"
    assert "outlineXOR" in params, "Missing parameter 'outlineXOR'"
    assert "lineDashOffset" in params, "Missing parameter 'lineDashOffset'"
    assert "antialias" in params, "Missing parameter 'antialias'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "fillXOR" in params, "Missing parameter 'fillXOR'"
    assert "outline" in params, "Missing parameter 'outline'"

def test_draw2d_shape_has_lineStyle():
    assert hasattr(draw2d_Shape, "lineStyle")
    descriptor = None
    for klass in draw2d_Shape.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_shape_has_fill():
    assert hasattr(draw2d_Shape, "fill")
    descriptor = None
    for klass in draw2d_Shape.__mro__:
        if "fill" in klass.__dict__:
            descriptor = klass.__dict__["fill"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_shape_has_lineWidthFloat():
    assert hasattr(draw2d_Shape, "lineWidthFloat")
    descriptor = None
    for klass in draw2d_Shape.__mro__:
        if "lineWidthFloat" in klass.__dict__:
            descriptor = klass.__dict__["lineWidthFloat"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_shape_has_lineMiterLimit():
    assert hasattr(draw2d_Shape, "lineMiterLimit")
    descriptor = None
    for klass in draw2d_Shape.__mro__:
        if "lineMiterLimit" in klass.__dict__:
            descriptor = klass.__dict__["lineMiterLimit"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_shape_has_lineDash():
    assert hasattr(draw2d_Shape, "lineDash")
    descriptor = None
    for klass in draw2d_Shape.__mro__:
        if "lineDash" in klass.__dict__:
            descriptor = klass.__dict__["lineDash"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_shape_has_lineJoin():
    assert hasattr(draw2d_Shape, "lineJoin")
    descriptor = None
    for klass in draw2d_Shape.__mro__:
        if "lineJoin" in klass.__dict__:
            descriptor = klass.__dict__["lineJoin"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_shape_has_lineCap():
    assert hasattr(draw2d_Shape, "lineCap")
    descriptor = None
    for klass in draw2d_Shape.__mro__:
        if "lineCap" in klass.__dict__:
            descriptor = klass.__dict__["lineCap"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_shape_has_outlineXOR():
    assert hasattr(draw2d_Shape, "outlineXOR")
    descriptor = None
    for klass in draw2d_Shape.__mro__:
        if "outlineXOR" in klass.__dict__:
            descriptor = klass.__dict__["outlineXOR"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_shape_has_lineDashOffset():
    assert hasattr(draw2d_Shape, "lineDashOffset")
    descriptor = None
    for klass in draw2d_Shape.__mro__:
        if "lineDashOffset" in klass.__dict__:
            descriptor = klass.__dict__["lineDashOffset"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_shape_has_antialias():
    assert hasattr(draw2d_Shape, "antialias")
    descriptor = None
    for klass in draw2d_Shape.__mro__:
        if "antialias" in klass.__dict__:
            descriptor = klass.__dict__["antialias"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_shape_has_alpha():
    assert hasattr(draw2d_Shape, "alpha")
    descriptor = None
    for klass in draw2d_Shape.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_shape_has_fillXOR():
    assert hasattr(draw2d_Shape, "fillXOR")
    descriptor = None
    for klass in draw2d_Shape.__mro__:
        if "fillXOR" in klass.__dict__:
            descriptor = klass.__dict__["fillXOR"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_shape_has_outline():
    assert hasattr(draw2d_Shape, "outline")
    descriptor = None
    for klass in draw2d_Shape.__mro__:
        if "outline" in klass.__dict__:
            descriptor = klass.__dict__["outline"]
            break
    assert isinstance(descriptor, property)



def test_draw2d_blockflow_is_not_abstract():
    assert not inspect.isabstract(draw2d_BlockFlow)


def test_draw2d_blockflow_constructor_exists():
    assert callable(draw2d_BlockFlow.__init__)


def test_draw2d_blockflow_constructor_args():
    sig = inspect.signature(draw2d_BlockFlow.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"

def test_draw2d_blockflow_has_orientation():
    assert hasattr(draw2d_BlockFlow, "orientation")
    descriptor = None
    for klass in draw2d_BlockFlow.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)



def test_draw2d_label_is_not_abstract():
    assert not inspect.isabstract(draw2d_Label)


def test_draw2d_label_constructor_exists():
    assert callable(draw2d_Label.__init__)


def test_draw2d_label_constructor_args():
    sig = inspect.signature(draw2d_Label.__init__)
    params = list(sig.parameters.keys())
    assert "iconAlignment" in params, "Missing parameter 'iconAlignment'"
    assert "iconTextGap" in params, "Missing parameter 'iconTextGap'"
    assert "textPlacement" in params, "Missing parameter 'textPlacement'"
    assert "textAlignment" in params, "Missing parameter 'textAlignment'"
    assert "icon" in params, "Missing parameter 'icon'"
    assert "text" in params, "Missing parameter 'text'"

def test_draw2d_label_has_iconAlignment():
    assert hasattr(draw2d_Label, "iconAlignment")
    descriptor = None
    for klass in draw2d_Label.__mro__:
        if "iconAlignment" in klass.__dict__:
            descriptor = klass.__dict__["iconAlignment"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_label_has_iconTextGap():
    assert hasattr(draw2d_Label, "iconTextGap")
    descriptor = None
    for klass in draw2d_Label.__mro__:
        if "iconTextGap" in klass.__dict__:
            descriptor = klass.__dict__["iconTextGap"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_label_has_textPlacement():
    assert hasattr(draw2d_Label, "textPlacement")
    descriptor = None
    for klass in draw2d_Label.__mro__:
        if "textPlacement" in klass.__dict__:
            descriptor = klass.__dict__["textPlacement"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_label_has_textAlignment():
    assert hasattr(draw2d_Label, "textAlignment")
    descriptor = None
    for klass in draw2d_Label.__mro__:
        if "textAlignment" in klass.__dict__:
            descriptor = klass.__dict__["textAlignment"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_label_has_icon():
    assert hasattr(draw2d_Label, "icon")
    descriptor = None
    for klass in draw2d_Label.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)

def test_draw2d_label_has_text():
    assert hasattr(draw2d_Label, "text")
    descriptor = None
    for klass in draw2d_Label.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_draw2d_border_is_not_abstract():
    assert not inspect.isabstract(draw2d_Border)


def test_draw2d_border_constructor_exists():
    assert callable(draw2d_Border.__init__)


def test_draw2d_border_constructor_args():
    sig = inspect.signature(draw2d_Border.__init__)
    params = list(sig.parameters.keys())
    assert "opaque" in params, "Missing parameter 'opaque'"

def test_draw2d_border_has_opaque():
    assert hasattr(draw2d_Border, "opaque")
    descriptor = None
    for klass in draw2d_Border.__mro__:
        if "opaque" in klass.__dict__:
            descriptor = klass.__dict__["opaque"]
            break
    assert isinstance(descriptor, property)



def test_draw2d_font_is_not_abstract():
    assert not inspect.isabstract(draw2d_Font)


def test_draw2d_font_constructor_exists():
    assert callable(draw2d_Font.__init__)


def test_draw2d_font_constructor_args():
    sig = inspect.signature(draw2d_Font.__init__)
    params = list(sig.parameters.keys())



def test_draw2d_color_is_not_abstract():
    assert not inspect.isabstract(draw2d_Color)


def test_draw2d_color_constructor_exists():
    assert callable(draw2d_Color.__init__)


def test_draw2d_color_constructor_args():
    sig = inspect.signature(draw2d_Color.__init__)
    params = list(sig.parameters.keys())

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "EAST",
        "NORTH",
        "SOUTH",
        "WEST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"

def test_alignment_exists():
    # Check that the Enumeration exists
    assert Alignment is not None

def test_alignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Alignment]
    expected_literals = [
        "TOP",
        "MIDDLE",
        "CENTER",
        "RIGHT",
        "BOTTOM",
        "LEFT",
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
draw2d_LabeledBorder_strategy = st.builds(
    draw2d_LabeledBorder,
    label=
        safe_text
)
ConnectionAnchor_strategy = st.builds(
    ConnectionAnchor,
)
draw2d_XYAnchor_strategy = st.builds(
    draw2d_XYAnchor,
    location=
        safe_text
)
draw2d_ConnectionAnchor_strategy = st.builds(
    draw2d_ConnectionAnchor,
)
draw2d_FlowBorder_strategy = st.builds(
    draw2d_FlowBorder,
    bottomMargin=
        st.integers(),
    rightMargin=
        st.integers(),
    leftMargin=
        st.integers(),
    topMargin=
        st.integers()
)
ColoredLabeledBorder_strategy = st.builds(
    ColoredLabeledBorder,
)
draw2d_TitleBarBorder_strategy = st.builds(
    draw2d_TitleBarBorder,
)
draw2d_GroupBoxBorder_strategy = st.builds(
    draw2d_GroupBoxBorder,
)
LabeledBorder_strategy = st.builds(
    LabeledBorder,
)
draw2d_ColoredLabeledBorder_strategy = st.builds(
    draw2d_ColoredLabeledBorder,
)
draw2d_FrameBorder_strategy = st.builds(
    draw2d_FrameBorder,
)
Polyline_strategy = st.builds(
    Polyline,
)
draw2d_Polygon_strategy = st.builds(
    draw2d_Polygon,
)
PointListShape_strategy = st.builds(
    PointListShape,
)
draw2d_PolygonShape_strategy = st.builds(
    draw2d_PolygonShape,
)
draw2d_PolylineShape_strategy = st.builds(
    draw2d_PolylineShape,
    tolerance=
        st.integers()
)
draw2d_Polyline_strategy = st.builds(
    draw2d_Polyline,
    tolerance=
        st.integers()
)
Shape_strategy = st.builds(
    Shape,
)
draw2d_Ellipse_strategy = st.builds(
    draw2d_Ellipse,
)
draw2d_RoundedRectangle_strategy = st.builds(
    draw2d_RoundedRectangle,
    cornerDimensions=
        safe_text
)
draw2d_Triangle_strategy = st.builds(
    draw2d_Triangle,
    orientation=
        safe_text,
    direction=
        safe_text
)
draw2d_PointListShape_strategy = st.builds(
    draw2d_PointListShape,
    pointList=
        st.integers()
)
draw2d_RectangleFigure_strategy = st.builds(
    draw2d_RectangleFigure,
)
draw2d_Figure_strategy = st.builds(
    draw2d_Figure,
    focusTraversable=
        st.booleans(),
    minimumSize=
        safe_text,
    maximumSize=
        safe_text,
    preferredSize=
        safe_text,
    bounds=
        safe_text,
    enabled=
        st.booleans(),
    visible=
        st.booleans(),
    opaque=
        st.booleans()
)
Canvas_strategy = st.builds(
    Canvas,
)
draw2d_Draw2DCanvas_strategy = st.builds(
    draw2d_Draw2DCanvas,
)
Figure_strategy = st.builds(
    Figure,
)
draw2d_ImageFigure_strategy = st.builds(
    draw2d_ImageFigure,
    image=
        safe_text
)
draw2d_Shape_strategy = st.builds(
    draw2d_Shape,
    lineStyle=
        safe_text,
    fill=
        st.booleans(),
    lineWidthFloat=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    lineMiterLimit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    lineDash=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    lineJoin=
        safe_text,
    lineCap=
        safe_text,
    outlineXOR=
        st.booleans(),
    lineDashOffset=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    antialias=
        safe_text,
    alpha=
        safe_text,
    fillXOR=
        st.booleans(),
    outline=
        st.booleans()
)
draw2d_BlockFlow_strategy = st.builds(
    draw2d_BlockFlow,
    orientation=
        safe_text
)
draw2d_Label_strategy = st.builds(
    draw2d_Label,
    iconAlignment=
        safe_text,
    iconTextGap=
        st.integers(),
    textPlacement=
        safe_text,
    textAlignment=
        safe_text,
    icon=
        safe_text,
    text=
        safe_text
)
draw2d_Border_strategy = st.builds(
    draw2d_Border,
    opaque=
        st.booleans()
)
draw2d_Font_strategy = st.builds(
    draw2d_Font,
)
draw2d_Color_strategy = st.builds(
    draw2d_Color,
)

@given(instance=Border_strategy)
@settings(max_examples=50)
def test_border_instantiation(instance):
    assert isinstance(instance, Border)

@given(instance=draw2d_LabeledBorder_strategy)
@settings(max_examples=50)
def test_draw2d_labeledborder_instantiation(instance):
    assert isinstance(instance, draw2d_LabeledBorder)



@given(instance=draw2d_LabeledBorder_strategy)
def test_draw2d_labeledborder_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=ConnectionAnchor_strategy)
@settings(max_examples=50)
def test_connectionanchor_instantiation(instance):
    assert isinstance(instance, ConnectionAnchor)

@given(instance=draw2d_XYAnchor_strategy)
@settings(max_examples=50)
def test_draw2d_xyanchor_instantiation(instance):
    assert isinstance(instance, draw2d_XYAnchor)



@given(instance=draw2d_XYAnchor_strategy)
def test_draw2d_xyanchor_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=draw2d_ConnectionAnchor_strategy)
@settings(max_examples=50)
def test_draw2d_connectionanchor_instantiation(instance):
    assert isinstance(instance, draw2d_ConnectionAnchor)

@given(instance=draw2d_FlowBorder_strategy)
@settings(max_examples=50)
def test_draw2d_flowborder_instantiation(instance):
    assert isinstance(instance, draw2d_FlowBorder)



@given(instance=draw2d_FlowBorder_strategy)
def test_draw2d_flowborder_bottomMargin_setter(instance):
    original = instance.bottomMargin
    instance.bottomMargin = original
    assert instance.bottomMargin == original



@given(instance=draw2d_FlowBorder_strategy)
def test_draw2d_flowborder_rightMargin_setter(instance):
    original = instance.rightMargin
    instance.rightMargin = original
    assert instance.rightMargin == original



@given(instance=draw2d_FlowBorder_strategy)
def test_draw2d_flowborder_leftMargin_setter(instance):
    original = instance.leftMargin
    instance.leftMargin = original
    assert instance.leftMargin == original



@given(instance=draw2d_FlowBorder_strategy)
def test_draw2d_flowborder_topMargin_setter(instance):
    original = instance.topMargin
    instance.topMargin = original
    assert instance.topMargin == original

@given(instance=ColoredLabeledBorder_strategy)
@settings(max_examples=50)
def test_coloredlabeledborder_instantiation(instance):
    assert isinstance(instance, ColoredLabeledBorder)

@given(instance=draw2d_TitleBarBorder_strategy)
@settings(max_examples=50)
def test_draw2d_titlebarborder_instantiation(instance):
    assert isinstance(instance, draw2d_TitleBarBorder)

@given(instance=draw2d_GroupBoxBorder_strategy)
@settings(max_examples=50)
def test_draw2d_groupboxborder_instantiation(instance):
    assert isinstance(instance, draw2d_GroupBoxBorder)

@given(instance=LabeledBorder_strategy)
@settings(max_examples=50)
def test_labeledborder_instantiation(instance):
    assert isinstance(instance, LabeledBorder)

@given(instance=draw2d_ColoredLabeledBorder_strategy)
@settings(max_examples=50)
def test_draw2d_coloredlabeledborder_instantiation(instance):
    assert isinstance(instance, draw2d_ColoredLabeledBorder)

@given(instance=draw2d_FrameBorder_strategy)
@settings(max_examples=50)
def test_draw2d_frameborder_instantiation(instance):
    assert isinstance(instance, draw2d_FrameBorder)

@given(instance=Polyline_strategy)
@settings(max_examples=50)
def test_polyline_instantiation(instance):
    assert isinstance(instance, Polyline)

@given(instance=draw2d_Polygon_strategy)
@settings(max_examples=50)
def test_draw2d_polygon_instantiation(instance):
    assert isinstance(instance, draw2d_Polygon)

@given(instance=PointListShape_strategy)
@settings(max_examples=50)
def test_pointlistshape_instantiation(instance):
    assert isinstance(instance, PointListShape)

@given(instance=draw2d_PolygonShape_strategy)
@settings(max_examples=50)
def test_draw2d_polygonshape_instantiation(instance):
    assert isinstance(instance, draw2d_PolygonShape)

@given(instance=draw2d_PolylineShape_strategy)
@settings(max_examples=50)
def test_draw2d_polylineshape_instantiation(instance):
    assert isinstance(instance, draw2d_PolylineShape)



@given(instance=draw2d_PolylineShape_strategy)
def test_draw2d_polylineshape_tolerance_setter(instance):
    original = instance.tolerance
    instance.tolerance = original
    assert instance.tolerance == original

@given(instance=draw2d_Polyline_strategy)
@settings(max_examples=50)
def test_draw2d_polyline_instantiation(instance):
    assert isinstance(instance, draw2d_Polyline)



@given(instance=draw2d_Polyline_strategy)
def test_draw2d_polyline_tolerance_setter(instance):
    original = instance.tolerance
    instance.tolerance = original
    assert instance.tolerance == original

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=draw2d_Ellipse_strategy)
@settings(max_examples=50)
def test_draw2d_ellipse_instantiation(instance):
    assert isinstance(instance, draw2d_Ellipse)

@given(instance=draw2d_RoundedRectangle_strategy)
@settings(max_examples=50)
def test_draw2d_roundedrectangle_instantiation(instance):
    assert isinstance(instance, draw2d_RoundedRectangle)



@given(instance=draw2d_RoundedRectangle_strategy)
def test_draw2d_roundedrectangle_cornerDimensions_setter(instance):
    original = instance.cornerDimensions
    instance.cornerDimensions = original
    assert instance.cornerDimensions == original

@given(instance=draw2d_Triangle_strategy)
@settings(max_examples=50)
def test_draw2d_triangle_instantiation(instance):
    assert isinstance(instance, draw2d_Triangle)



@given(instance=draw2d_Triangle_strategy)
def test_draw2d_triangle_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original



@given(instance=draw2d_Triangle_strategy)
def test_draw2d_triangle_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=draw2d_PointListShape_strategy)
@settings(max_examples=50)
def test_draw2d_pointlistshape_instantiation(instance):
    assert isinstance(instance, draw2d_PointListShape)



@given(instance=draw2d_PointListShape_strategy)
def test_draw2d_pointlistshape_pointList_setter(instance):
    original = instance.pointList
    instance.pointList = original
    assert instance.pointList == original

@given(instance=draw2d_RectangleFigure_strategy)
@settings(max_examples=50)
def test_draw2d_rectanglefigure_instantiation(instance):
    assert isinstance(instance, draw2d_RectangleFigure)

@given(instance=draw2d_Figure_strategy)
@settings(max_examples=50)
def test_draw2d_figure_instantiation(instance):
    assert isinstance(instance, draw2d_Figure)



@given(instance=draw2d_Figure_strategy)
def test_draw2d_figure_focusTraversable_setter(instance):
    original = instance.focusTraversable
    instance.focusTraversable = original
    assert instance.focusTraversable == original



@given(instance=draw2d_Figure_strategy)
def test_draw2d_figure_minimumSize_setter(instance):
    original = instance.minimumSize
    instance.minimumSize = original
    assert instance.minimumSize == original



@given(instance=draw2d_Figure_strategy)
def test_draw2d_figure_maximumSize_setter(instance):
    original = instance.maximumSize
    instance.maximumSize = original
    assert instance.maximumSize == original



@given(instance=draw2d_Figure_strategy)
def test_draw2d_figure_preferredSize_setter(instance):
    original = instance.preferredSize
    instance.preferredSize = original
    assert instance.preferredSize == original



@given(instance=draw2d_Figure_strategy)
def test_draw2d_figure_bounds_setter(instance):
    original = instance.bounds
    instance.bounds = original
    assert instance.bounds == original



@given(instance=draw2d_Figure_strategy)
def test_draw2d_figure_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original



@given(instance=draw2d_Figure_strategy)
def test_draw2d_figure_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=draw2d_Figure_strategy)
def test_draw2d_figure_opaque_setter(instance):
    original = instance.opaque
    instance.opaque = original
    assert instance.opaque == original

@given(instance=Canvas_strategy)
@settings(max_examples=50)
def test_canvas_instantiation(instance):
    assert isinstance(instance, Canvas)

@given(instance=draw2d_Draw2DCanvas_strategy)
@settings(max_examples=50)
def test_draw2d_draw2dcanvas_instantiation(instance):
    assert isinstance(instance, draw2d_Draw2DCanvas)

@given(instance=Figure_strategy)
@settings(max_examples=50)
def test_figure_instantiation(instance):
    assert isinstance(instance, Figure)

@given(instance=draw2d_ImageFigure_strategy)
@settings(max_examples=50)
def test_draw2d_imagefigure_instantiation(instance):
    assert isinstance(instance, draw2d_ImageFigure)



@given(instance=draw2d_ImageFigure_strategy)
def test_draw2d_imagefigure_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=draw2d_Shape_strategy)
@settings(max_examples=50)
def test_draw2d_shape_instantiation(instance):
    assert isinstance(instance, draw2d_Shape)



@given(instance=draw2d_Shape_strategy)
def test_draw2d_shape_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original



@given(instance=draw2d_Shape_strategy)
def test_draw2d_shape_fill_setter(instance):
    original = instance.fill
    instance.fill = original
    assert instance.fill == original



@given(instance=draw2d_Shape_strategy)
def test_draw2d_shape_lineWidthFloat_setter(instance):
    original = instance.lineWidthFloat
    instance.lineWidthFloat = original
    assert instance.lineWidthFloat == original



@given(instance=draw2d_Shape_strategy)
def test_draw2d_shape_lineMiterLimit_setter(instance):
    original = instance.lineMiterLimit
    instance.lineMiterLimit = original
    assert instance.lineMiterLimit == original



@given(instance=draw2d_Shape_strategy)
def test_draw2d_shape_lineDash_setter(instance):
    original = instance.lineDash
    instance.lineDash = original
    assert instance.lineDash == original



@given(instance=draw2d_Shape_strategy)
def test_draw2d_shape_lineJoin_setter(instance):
    original = instance.lineJoin
    instance.lineJoin = original
    assert instance.lineJoin == original



@given(instance=draw2d_Shape_strategy)
def test_draw2d_shape_lineCap_setter(instance):
    original = instance.lineCap
    instance.lineCap = original
    assert instance.lineCap == original



@given(instance=draw2d_Shape_strategy)
def test_draw2d_shape_outlineXOR_setter(instance):
    original = instance.outlineXOR
    instance.outlineXOR = original
    assert instance.outlineXOR == original



@given(instance=draw2d_Shape_strategy)
def test_draw2d_shape_lineDashOffset_setter(instance):
    original = instance.lineDashOffset
    instance.lineDashOffset = original
    assert instance.lineDashOffset == original



@given(instance=draw2d_Shape_strategy)
def test_draw2d_shape_antialias_setter(instance):
    original = instance.antialias
    instance.antialias = original
    assert instance.antialias == original



@given(instance=draw2d_Shape_strategy)
def test_draw2d_shape_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=draw2d_Shape_strategy)
def test_draw2d_shape_fillXOR_setter(instance):
    original = instance.fillXOR
    instance.fillXOR = original
    assert instance.fillXOR == original



@given(instance=draw2d_Shape_strategy)
def test_draw2d_shape_outline_setter(instance):
    original = instance.outline
    instance.outline = original
    assert instance.outline == original

@given(instance=draw2d_BlockFlow_strategy)
@settings(max_examples=50)
def test_draw2d_blockflow_instantiation(instance):
    assert isinstance(instance, draw2d_BlockFlow)



@given(instance=draw2d_BlockFlow_strategy)
def test_draw2d_blockflow_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=draw2d_Label_strategy)
@settings(max_examples=50)
def test_draw2d_label_instantiation(instance):
    assert isinstance(instance, draw2d_Label)



@given(instance=draw2d_Label_strategy)
def test_draw2d_label_iconAlignment_setter(instance):
    original = instance.iconAlignment
    instance.iconAlignment = original
    assert instance.iconAlignment == original



@given(instance=draw2d_Label_strategy)
def test_draw2d_label_iconTextGap_setter(instance):
    original = instance.iconTextGap
    instance.iconTextGap = original
    assert instance.iconTextGap == original



@given(instance=draw2d_Label_strategy)
def test_draw2d_label_textPlacement_setter(instance):
    original = instance.textPlacement
    instance.textPlacement = original
    assert instance.textPlacement == original



@given(instance=draw2d_Label_strategy)
def test_draw2d_label_textAlignment_setter(instance):
    original = instance.textAlignment
    instance.textAlignment = original
    assert instance.textAlignment == original



@given(instance=draw2d_Label_strategy)
def test_draw2d_label_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original



@given(instance=draw2d_Label_strategy)
def test_draw2d_label_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=draw2d_Border_strategy)
@settings(max_examples=50)
def test_draw2d_border_instantiation(instance):
    assert isinstance(instance, draw2d_Border)



@given(instance=draw2d_Border_strategy)
def test_draw2d_border_opaque_setter(instance):
    original = instance.opaque
    instance.opaque = original
    assert instance.opaque == original

@given(instance=draw2d_Font_strategy)
@settings(max_examples=50)
def test_draw2d_font_instantiation(instance):
    assert isinstance(instance, draw2d_Font)

@given(instance=draw2d_Color_strategy)
@settings(max_examples=50)
def test_draw2d_color_instantiation(instance):
    assert isinstance(instance, draw2d_Color)
