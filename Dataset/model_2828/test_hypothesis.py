import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    styles_TextStyle,
    mm_styles_TextStyleRegion,
    mm_styles_Font,
    styles_GradientColoredAreas,
    mm_styles_AdaptedGradientColoredAreas,
    styles_GradientColoredArea,
    mm_styles_GradientColoredAreas,
    styles_GradientColoredLocation,
    mm_styles_GradientColoredArea,
    mm_styles_GradientColoredLocation,
    styles_RenderingStyle,
    mm_styles_TextStyle,
    mm_styles_PrecisionPoint,
    mm_styles_Color,
    mm_styles_Point,
    styles_AdaptedGradientColoredAreas,
    mm_styles_RenderingStyle,
    styles_TextStyleRegion,
    mm_styles_AbstractStyle,
    styles_mm_StyleContainer,
    styles_AbstractStyle,
    CurvedConnection,
    styles_PrecisionPoint,
    Polyline,
    mm_algorithms_Polygon,
    AbstractText,
    mm_algorithms_MultiText,
    mm_algorithms_Text,
    styles_Point,
    AdvancedAnchor,
    mm_pictograms_FixPointAnchor,
    PictogramElement,
    mm_pictograms_AnchorContainer,
    mm_pictograms_Anchor,
    ConnectionDecorator,
    Diagram,
    Anchor,
    mm_pictograms_AdvancedAnchor,
    pictograms_mm_EObject,
    mm_pictograms_ChopboxAnchor,
    mm_pictograms_BoxRelativeAnchor,
    Connection,
    mm_pictograms_ManhattanConnection,
    mm_pictograms_CurvedConnection,
    mm_pictograms_FreeFormConnection,
    mm_pictograms_CompositeConnection,
    StyleContainer,
    mm_styles_Style,
    pictograms_ContainerShape,
    mm_pictograms_Diagram,
    Shape,
    mm_pictograms_ConnectionDecorator,
    mm_pictograms_ContainerShape,
    ContainerShape,
    AnchorContainer,
    mm_pictograms_Connection,
    mm_pictograms_Shape,
    styles_Style,
    mm_StyleContainer,
    PropertyContainer,
    mm_pictograms_PictogramLink,
    mm_GraphicsAlgorithmContainer,
    GraphicsAlgorithm,
    mm_algorithms_Image,
    mm_algorithms_Ellipse,
    mm_algorithms_PlatformGraphicsAlgorithm,
    mm_algorithms_Polyline,
    mm_algorithms_Rectangle,
    mm_algorithms_RoundedRectangle,
    mm_algorithms_AbstractText,
    GraphicsAlgorithmContainer,
    mm_algorithms_GraphicsAlgorithm,
    mm_pictograms_PictogramElement,
    PictogramLink,
    styles_Font,
    styles_Color,
    mm_PropertyContainer,
    mm_Property,
    Orientation,
    LineStyle,
    UnderlineStyle,
    LocationType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_styles_textstyle_is_not_abstract():
    assert not inspect.isabstract(styles_TextStyle)


def test_styles_textstyle_constructor_exists():
    assert callable(styles_TextStyle.__init__)


def test_styles_textstyle_constructor_args():
    sig = inspect.signature(styles_TextStyle.__init__)
    params = list(sig.parameters.keys())



def test_mm_styles_textstyleregion_is_not_abstract():
    assert not inspect.isabstract(mm_styles_TextStyleRegion)


def test_mm_styles_textstyleregion_constructor_exists():
    assert callable(mm_styles_TextStyleRegion.__init__)


def test_mm_styles_textstyleregion_constructor_args():
    sig = inspect.signature(mm_styles_TextStyleRegion.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"
    assert "start" in params, "Missing parameter 'start'"

def test_mm_styles_textstyleregion_has_end():
    assert hasattr(mm_styles_TextStyleRegion, "end")
    descriptor = None
    for klass in mm_styles_TextStyleRegion.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_textstyleregion_has_start():
    assert hasattr(mm_styles_TextStyleRegion, "start")
    descriptor = None
    for klass in mm_styles_TextStyleRegion.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_mm_styles_font_is_not_abstract():
    assert not inspect.isabstract(mm_styles_Font)


def test_mm_styles_font_constructor_exists():
    assert callable(mm_styles_Font.__init__)


def test_mm_styles_font_constructor_args():
    sig = inspect.signature(mm_styles_Font.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "bold" in params, "Missing parameter 'bold'"
    assert "italic" in params, "Missing parameter 'italic'"
    assert "size" in params, "Missing parameter 'size'"

def test_mm_styles_font_has_name():
    assert hasattr(mm_styles_Font, "name")
    descriptor = None
    for klass in mm_styles_Font.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_font_has_bold():
    assert hasattr(mm_styles_Font, "bold")
    descriptor = None
    for klass in mm_styles_Font.__mro__:
        if "bold" in klass.__dict__:
            descriptor = klass.__dict__["bold"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_font_has_italic():
    assert hasattr(mm_styles_Font, "italic")
    descriptor = None
    for klass in mm_styles_Font.__mro__:
        if "italic" in klass.__dict__:
            descriptor = klass.__dict__["italic"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_font_has_size():
    assert hasattr(mm_styles_Font, "size")
    descriptor = None
    for klass in mm_styles_Font.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_styles_gradientcoloredareas_is_not_abstract():
    assert not inspect.isabstract(styles_GradientColoredAreas)


def test_styles_gradientcoloredareas_constructor_exists():
    assert callable(styles_GradientColoredAreas.__init__)


def test_styles_gradientcoloredareas_constructor_args():
    sig = inspect.signature(styles_GradientColoredAreas.__init__)
    params = list(sig.parameters.keys())



def test_mm_styles_adaptedgradientcoloredareas_is_not_abstract():
    assert not inspect.isabstract(mm_styles_AdaptedGradientColoredAreas)


def test_mm_styles_adaptedgradientcoloredareas_constructor_exists():
    assert callable(mm_styles_AdaptedGradientColoredAreas.__init__)


def test_mm_styles_adaptedgradientcoloredareas_constructor_args():
    sig = inspect.signature(mm_styles_AdaptedGradientColoredAreas.__init__)
    params = list(sig.parameters.keys())
    assert "gradientType" in params, "Missing parameter 'gradientType'"
    assert "definedStyleId" in params, "Missing parameter 'definedStyleId'"

def test_mm_styles_adaptedgradientcoloredareas_has_gradientType():
    assert hasattr(mm_styles_AdaptedGradientColoredAreas, "gradientType")
    descriptor = None
    for klass in mm_styles_AdaptedGradientColoredAreas.__mro__:
        if "gradientType" in klass.__dict__:
            descriptor = klass.__dict__["gradientType"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_adaptedgradientcoloredareas_has_definedStyleId():
    assert hasattr(mm_styles_AdaptedGradientColoredAreas, "definedStyleId")
    descriptor = None
    for klass in mm_styles_AdaptedGradientColoredAreas.__mro__:
        if "definedStyleId" in klass.__dict__:
            descriptor = klass.__dict__["definedStyleId"]
            break
    assert isinstance(descriptor, property)



def test_styles_gradientcoloredarea_is_not_abstract():
    assert not inspect.isabstract(styles_GradientColoredArea)


def test_styles_gradientcoloredarea_constructor_exists():
    assert callable(styles_GradientColoredArea.__init__)


def test_styles_gradientcoloredarea_constructor_args():
    sig = inspect.signature(styles_GradientColoredArea.__init__)
    params = list(sig.parameters.keys())



def test_mm_styles_gradientcoloredareas_is_not_abstract():
    assert not inspect.isabstract(mm_styles_GradientColoredAreas)


def test_mm_styles_gradientcoloredareas_constructor_exists():
    assert callable(mm_styles_GradientColoredAreas.__init__)


def test_mm_styles_gradientcoloredareas_constructor_args():
    sig = inspect.signature(mm_styles_GradientColoredAreas.__init__)
    params = list(sig.parameters.keys())
    assert "styleAdaption" in params, "Missing parameter 'styleAdaption'"

def test_mm_styles_gradientcoloredareas_has_styleAdaption():
    assert hasattr(mm_styles_GradientColoredAreas, "styleAdaption")
    descriptor = None
    for klass in mm_styles_GradientColoredAreas.__mro__:
        if "styleAdaption" in klass.__dict__:
            descriptor = klass.__dict__["styleAdaption"]
            break
    assert isinstance(descriptor, property)



def test_styles_gradientcoloredlocation_is_not_abstract():
    assert not inspect.isabstract(styles_GradientColoredLocation)


def test_styles_gradientcoloredlocation_constructor_exists():
    assert callable(styles_GradientColoredLocation.__init__)


def test_styles_gradientcoloredlocation_constructor_args():
    sig = inspect.signature(styles_GradientColoredLocation.__init__)
    params = list(sig.parameters.keys())



def test_mm_styles_gradientcoloredarea_is_not_abstract():
    assert not inspect.isabstract(mm_styles_GradientColoredArea)


def test_mm_styles_gradientcoloredarea_constructor_exists():
    assert callable(mm_styles_GradientColoredArea.__init__)


def test_mm_styles_gradientcoloredarea_constructor_args():
    sig = inspect.signature(mm_styles_GradientColoredArea.__init__)
    params = list(sig.parameters.keys())



def test_mm_styles_gradientcoloredlocation_is_not_abstract():
    assert not inspect.isabstract(mm_styles_GradientColoredLocation)


def test_mm_styles_gradientcoloredlocation_constructor_exists():
    assert callable(mm_styles_GradientColoredLocation.__init__)


def test_mm_styles_gradientcoloredlocation_constructor_args():
    sig = inspect.signature(mm_styles_GradientColoredLocation.__init__)
    params = list(sig.parameters.keys())
    assert "locationType" in params, "Missing parameter 'locationType'"
    assert "locationValue" in params, "Missing parameter 'locationValue'"

def test_mm_styles_gradientcoloredlocation_has_locationType():
    assert hasattr(mm_styles_GradientColoredLocation, "locationType")
    descriptor = None
    for klass in mm_styles_GradientColoredLocation.__mro__:
        if "locationType" in klass.__dict__:
            descriptor = klass.__dict__["locationType"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_gradientcoloredlocation_has_locationValue():
    assert hasattr(mm_styles_GradientColoredLocation, "locationValue")
    descriptor = None
    for klass in mm_styles_GradientColoredLocation.__mro__:
        if "locationValue" in klass.__dict__:
            descriptor = klass.__dict__["locationValue"]
            break
    assert isinstance(descriptor, property)



def test_styles_renderingstyle_is_not_abstract():
    assert not inspect.isabstract(styles_RenderingStyle)


def test_styles_renderingstyle_constructor_exists():
    assert callable(styles_RenderingStyle.__init__)


def test_styles_renderingstyle_constructor_args():
    sig = inspect.signature(styles_RenderingStyle.__init__)
    params = list(sig.parameters.keys())



def test_mm_styles_textstyle_is_not_abstract():
    assert not inspect.isabstract(mm_styles_TextStyle)


def test_mm_styles_textstyle_constructor_exists():
    assert callable(mm_styles_TextStyle.__init__)


def test_mm_styles_textstyle_constructor_args():
    sig = inspect.signature(mm_styles_TextStyle.__init__)
    params = list(sig.parameters.keys())
    assert "strikeout" in params, "Missing parameter 'strikeout'"
    assert "underlineStyle" in params, "Missing parameter 'underlineStyle'"
    assert "underline" in params, "Missing parameter 'underline'"

def test_mm_styles_textstyle_has_strikeout():
    assert hasattr(mm_styles_TextStyle, "strikeout")
    descriptor = None
    for klass in mm_styles_TextStyle.__mro__:
        if "strikeout" in klass.__dict__:
            descriptor = klass.__dict__["strikeout"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_textstyle_has_underlineStyle():
    assert hasattr(mm_styles_TextStyle, "underlineStyle")
    descriptor = None
    for klass in mm_styles_TextStyle.__mro__:
        if "underlineStyle" in klass.__dict__:
            descriptor = klass.__dict__["underlineStyle"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_textstyle_has_underline():
    assert hasattr(mm_styles_TextStyle, "underline")
    descriptor = None
    for klass in mm_styles_TextStyle.__mro__:
        if "underline" in klass.__dict__:
            descriptor = klass.__dict__["underline"]
            break
    assert isinstance(descriptor, property)



def test_mm_styles_precisionpoint_is_not_abstract():
    assert not inspect.isabstract(mm_styles_PrecisionPoint)


def test_mm_styles_precisionpoint_constructor_exists():
    assert callable(mm_styles_PrecisionPoint.__init__)


def test_mm_styles_precisionpoint_constructor_args():
    sig = inspect.signature(mm_styles_PrecisionPoint.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_mm_styles_precisionpoint_has_x():
    assert hasattr(mm_styles_PrecisionPoint, "x")
    descriptor = None
    for klass in mm_styles_PrecisionPoint.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_precisionpoint_has_y():
    assert hasattr(mm_styles_PrecisionPoint, "y")
    descriptor = None
    for klass in mm_styles_PrecisionPoint.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_mm_styles_color_is_not_abstract():
    assert not inspect.isabstract(mm_styles_Color)


def test_mm_styles_color_constructor_exists():
    assert callable(mm_styles_Color.__init__)


def test_mm_styles_color_constructor_args():
    sig = inspect.signature(mm_styles_Color.__init__)
    params = list(sig.parameters.keys())
    assert "red" in params, "Missing parameter 'red'"
    assert "green" in params, "Missing parameter 'green'"
    assert "blue" in params, "Missing parameter 'blue'"

def test_mm_styles_color_has_red():
    assert hasattr(mm_styles_Color, "red")
    descriptor = None
    for klass in mm_styles_Color.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_color_has_green():
    assert hasattr(mm_styles_Color, "green")
    descriptor = None
    for klass in mm_styles_Color.__mro__:
        if "green" in klass.__dict__:
            descriptor = klass.__dict__["green"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_color_has_blue():
    assert hasattr(mm_styles_Color, "blue")
    descriptor = None
    for klass in mm_styles_Color.__mro__:
        if "blue" in klass.__dict__:
            descriptor = klass.__dict__["blue"]
            break
    assert isinstance(descriptor, property)



def test_mm_styles_point_is_not_abstract():
    assert not inspect.isabstract(mm_styles_Point)


def test_mm_styles_point_constructor_exists():
    assert callable(mm_styles_Point.__init__)


def test_mm_styles_point_constructor_args():
    sig = inspect.signature(mm_styles_Point.__init__)
    params = list(sig.parameters.keys())
    assert "after" in params, "Missing parameter 'after'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "before" in params, "Missing parameter 'before'"

def test_mm_styles_point_has_after():
    assert hasattr(mm_styles_Point, "after")
    descriptor = None
    for klass in mm_styles_Point.__mro__:
        if "after" in klass.__dict__:
            descriptor = klass.__dict__["after"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_point_has_x():
    assert hasattr(mm_styles_Point, "x")
    descriptor = None
    for klass in mm_styles_Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_point_has_y():
    assert hasattr(mm_styles_Point, "y")
    descriptor = None
    for klass in mm_styles_Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_point_has_before():
    assert hasattr(mm_styles_Point, "before")
    descriptor = None
    for klass in mm_styles_Point.__mro__:
        if "before" in klass.__dict__:
            descriptor = klass.__dict__["before"]
            break
    assert isinstance(descriptor, property)



def test_styles_adaptedgradientcoloredareas_is_not_abstract():
    assert not inspect.isabstract(styles_AdaptedGradientColoredAreas)


def test_styles_adaptedgradientcoloredareas_constructor_exists():
    assert callable(styles_AdaptedGradientColoredAreas.__init__)


def test_styles_adaptedgradientcoloredareas_constructor_args():
    sig = inspect.signature(styles_AdaptedGradientColoredAreas.__init__)
    params = list(sig.parameters.keys())



def test_mm_styles_renderingstyle_is_not_abstract():
    assert not inspect.isabstract(mm_styles_RenderingStyle)


def test_mm_styles_renderingstyle_constructor_exists():
    assert callable(mm_styles_RenderingStyle.__init__)


def test_mm_styles_renderingstyle_constructor_args():
    sig = inspect.signature(mm_styles_RenderingStyle.__init__)
    params = list(sig.parameters.keys())



def test_styles_textstyleregion_is_not_abstract():
    assert not inspect.isabstract(styles_TextStyleRegion)


def test_styles_textstyleregion_constructor_exists():
    assert callable(styles_TextStyleRegion.__init__)


def test_styles_textstyleregion_constructor_args():
    sig = inspect.signature(styles_TextStyleRegion.__init__)
    params = list(sig.parameters.keys())



def test_mm_styles_abstractstyle_is_not_abstract():
    assert not inspect.isabstract(mm_styles_AbstractStyle)


def test_mm_styles_abstractstyle_constructor_exists():
    assert callable(mm_styles_AbstractStyle.__init__)


def test_mm_styles_abstractstyle_constructor_args():
    sig = inspect.signature(mm_styles_AbstractStyle.__init__)
    params = list(sig.parameters.keys())
    assert "transparency" in params, "Missing parameter 'transparency'"
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"
    assert "lineVisible" in params, "Missing parameter 'lineVisible'"
    assert "filled" in params, "Missing parameter 'filled'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"

def test_mm_styles_abstractstyle_has_transparency():
    assert hasattr(mm_styles_AbstractStyle, "transparency")
    descriptor = None
    for klass in mm_styles_AbstractStyle.__mro__:
        if "transparency" in klass.__dict__:
            descriptor = klass.__dict__["transparency"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_abstractstyle_has_lineWidth():
    assert hasattr(mm_styles_AbstractStyle, "lineWidth")
    descriptor = None
    for klass in mm_styles_AbstractStyle.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_abstractstyle_has_lineVisible():
    assert hasattr(mm_styles_AbstractStyle, "lineVisible")
    descriptor = None
    for klass in mm_styles_AbstractStyle.__mro__:
        if "lineVisible" in klass.__dict__:
            descriptor = klass.__dict__["lineVisible"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_abstractstyle_has_filled():
    assert hasattr(mm_styles_AbstractStyle, "filled")
    descriptor = None
    for klass in mm_styles_AbstractStyle.__mro__:
        if "filled" in klass.__dict__:
            descriptor = klass.__dict__["filled"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_abstractstyle_has_lineStyle():
    assert hasattr(mm_styles_AbstractStyle, "lineStyle")
    descriptor = None
    for klass in mm_styles_AbstractStyle.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)



def test_styles_mm_stylecontainer_is_not_abstract():
    assert not inspect.isabstract(styles_mm_StyleContainer)


def test_styles_mm_stylecontainer_constructor_exists():
    assert callable(styles_mm_StyleContainer.__init__)


def test_styles_mm_stylecontainer_constructor_args():
    sig = inspect.signature(styles_mm_StyleContainer.__init__)
    params = list(sig.parameters.keys())



def test_styles_abstractstyle_is_not_abstract():
    assert not inspect.isabstract(styles_AbstractStyle)


def test_styles_abstractstyle_constructor_exists():
    assert callable(styles_AbstractStyle.__init__)


def test_styles_abstractstyle_constructor_args():
    sig = inspect.signature(styles_AbstractStyle.__init__)
    params = list(sig.parameters.keys())



def test_curvedconnection_is_not_abstract():
    assert not inspect.isabstract(CurvedConnection)


def test_curvedconnection_constructor_exists():
    assert callable(CurvedConnection.__init__)


def test_curvedconnection_constructor_args():
    sig = inspect.signature(CurvedConnection.__init__)
    params = list(sig.parameters.keys())



def test_styles_precisionpoint_is_not_abstract():
    assert not inspect.isabstract(styles_PrecisionPoint)


def test_styles_precisionpoint_constructor_exists():
    assert callable(styles_PrecisionPoint.__init__)


def test_styles_precisionpoint_constructor_args():
    sig = inspect.signature(styles_PrecisionPoint.__init__)
    params = list(sig.parameters.keys())



def test_polyline_is_not_abstract():
    assert not inspect.isabstract(Polyline)


def test_polyline_constructor_exists():
    assert callable(Polyline.__init__)


def test_polyline_constructor_args():
    sig = inspect.signature(Polyline.__init__)
    params = list(sig.parameters.keys())



def test_mm_algorithms_polygon_is_not_abstract():
    assert not inspect.isabstract(mm_algorithms_Polygon)


def test_mm_algorithms_polygon_constructor_exists():
    assert callable(mm_algorithms_Polygon.__init__)


def test_mm_algorithms_polygon_constructor_args():
    sig = inspect.signature(mm_algorithms_Polygon.__init__)
    params = list(sig.parameters.keys())



def test_abstracttext_is_not_abstract():
    assert not inspect.isabstract(AbstractText)


def test_abstracttext_constructor_exists():
    assert callable(AbstractText.__init__)


def test_abstracttext_constructor_args():
    sig = inspect.signature(AbstractText.__init__)
    params = list(sig.parameters.keys())



def test_mm_algorithms_multitext_is_not_abstract():
    assert not inspect.isabstract(mm_algorithms_MultiText)


def test_mm_algorithms_multitext_constructor_exists():
    assert callable(mm_algorithms_MultiText.__init__)


def test_mm_algorithms_multitext_constructor_args():
    sig = inspect.signature(mm_algorithms_MultiText.__init__)
    params = list(sig.parameters.keys())



def test_mm_algorithms_text_is_not_abstract():
    assert not inspect.isabstract(mm_algorithms_Text)


def test_mm_algorithms_text_constructor_exists():
    assert callable(mm_algorithms_Text.__init__)


def test_mm_algorithms_text_constructor_args():
    sig = inspect.signature(mm_algorithms_Text.__init__)
    params = list(sig.parameters.keys())



def test_styles_point_is_not_abstract():
    assert not inspect.isabstract(styles_Point)


def test_styles_point_constructor_exists():
    assert callable(styles_Point.__init__)


def test_styles_point_constructor_args():
    sig = inspect.signature(styles_Point.__init__)
    params = list(sig.parameters.keys())



def test_advancedanchor_is_not_abstract():
    assert not inspect.isabstract(AdvancedAnchor)


def test_advancedanchor_constructor_exists():
    assert callable(AdvancedAnchor.__init__)


def test_advancedanchor_constructor_args():
    sig = inspect.signature(AdvancedAnchor.__init__)
    params = list(sig.parameters.keys())



def test_mm_pictograms_fixpointanchor_is_not_abstract():
    assert not inspect.isabstract(mm_pictograms_FixPointAnchor)


def test_mm_pictograms_fixpointanchor_constructor_exists():
    assert callable(mm_pictograms_FixPointAnchor.__init__)


def test_mm_pictograms_fixpointanchor_constructor_args():
    sig = inspect.signature(mm_pictograms_FixPointAnchor.__init__)
    params = list(sig.parameters.keys())



def test_pictogramelement_is_not_abstract():
    assert not inspect.isabstract(PictogramElement)


def test_pictogramelement_constructor_exists():
    assert callable(PictogramElement.__init__)


def test_pictogramelement_constructor_args():
    sig = inspect.signature(PictogramElement.__init__)
    params = list(sig.parameters.keys())



def test_mm_pictograms_anchorcontainer_is_not_abstract():
    assert not inspect.isabstract(mm_pictograms_AnchorContainer)


def test_mm_pictograms_anchorcontainer_constructor_exists():
    assert callable(mm_pictograms_AnchorContainer.__init__)


def test_mm_pictograms_anchorcontainer_constructor_args():
    sig = inspect.signature(mm_pictograms_AnchorContainer.__init__)
    params = list(sig.parameters.keys())



def test_mm_pictograms_anchor_is_not_abstract():
    assert not inspect.isabstract(mm_pictograms_Anchor)


def test_mm_pictograms_anchor_constructor_exists():
    assert callable(mm_pictograms_Anchor.__init__)


def test_mm_pictograms_anchor_constructor_args():
    sig = inspect.signature(mm_pictograms_Anchor.__init__)
    params = list(sig.parameters.keys())



def test_connectiondecorator_is_not_abstract():
    assert not inspect.isabstract(ConnectionDecorator)


def test_connectiondecorator_constructor_exists():
    assert callable(ConnectionDecorator.__init__)


def test_connectiondecorator_constructor_args():
    sig = inspect.signature(ConnectionDecorator.__init__)
    params = list(sig.parameters.keys())



def test_diagram_is_not_abstract():
    assert not inspect.isabstract(Diagram)


def test_diagram_constructor_exists():
    assert callable(Diagram.__init__)


def test_diagram_constructor_args():
    sig = inspect.signature(Diagram.__init__)
    params = list(sig.parameters.keys())



def test_anchor_is_not_abstract():
    assert not inspect.isabstract(Anchor)


def test_anchor_constructor_exists():
    assert callable(Anchor.__init__)


def test_anchor_constructor_args():
    sig = inspect.signature(Anchor.__init__)
    params = list(sig.parameters.keys())



def test_mm_pictograms_advancedanchor_is_not_abstract():
    assert not inspect.isabstract(mm_pictograms_AdvancedAnchor)


def test_mm_pictograms_advancedanchor_constructor_exists():
    assert callable(mm_pictograms_AdvancedAnchor.__init__)


def test_mm_pictograms_advancedanchor_constructor_args():
    sig = inspect.signature(mm_pictograms_AdvancedAnchor.__init__)
    params = list(sig.parameters.keys())
    assert "useAnchorLocationAsConnectionEndpoint" in params, "Missing parameter 'useAnchorLocationAsConnectionEndpoint'"

def test_mm_pictograms_advancedanchor_has_useAnchorLocationAsConnectionEndpoint():
    assert hasattr(mm_pictograms_AdvancedAnchor, "useAnchorLocationAsConnectionEndpoint")
    descriptor = None
    for klass in mm_pictograms_AdvancedAnchor.__mro__:
        if "useAnchorLocationAsConnectionEndpoint" in klass.__dict__:
            descriptor = klass.__dict__["useAnchorLocationAsConnectionEndpoint"]
            break
    assert isinstance(descriptor, property)



def test_pictograms_mm_eobject_is_not_abstract():
    assert not inspect.isabstract(pictograms_mm_EObject)


def test_pictograms_mm_eobject_constructor_exists():
    assert callable(pictograms_mm_EObject.__init__)


def test_pictograms_mm_eobject_constructor_args():
    sig = inspect.signature(pictograms_mm_EObject.__init__)
    params = list(sig.parameters.keys())



def test_mm_pictograms_chopboxanchor_is_not_abstract():
    assert not inspect.isabstract(mm_pictograms_ChopboxAnchor)


def test_mm_pictograms_chopboxanchor_constructor_exists():
    assert callable(mm_pictograms_ChopboxAnchor.__init__)


def test_mm_pictograms_chopboxanchor_constructor_args():
    sig = inspect.signature(mm_pictograms_ChopboxAnchor.__init__)
    params = list(sig.parameters.keys())



def test_mm_pictograms_boxrelativeanchor_is_not_abstract():
    assert not inspect.isabstract(mm_pictograms_BoxRelativeAnchor)


def test_mm_pictograms_boxrelativeanchor_constructor_exists():
    assert callable(mm_pictograms_BoxRelativeAnchor.__init__)


def test_mm_pictograms_boxrelativeanchor_constructor_args():
    sig = inspect.signature(mm_pictograms_BoxRelativeAnchor.__init__)
    params = list(sig.parameters.keys())
    assert "relativeHeight" in params, "Missing parameter 'relativeHeight'"
    assert "relativeWidth" in params, "Missing parameter 'relativeWidth'"

def test_mm_pictograms_boxrelativeanchor_has_relativeHeight():
    assert hasattr(mm_pictograms_BoxRelativeAnchor, "relativeHeight")
    descriptor = None
    for klass in mm_pictograms_BoxRelativeAnchor.__mro__:
        if "relativeHeight" in klass.__dict__:
            descriptor = klass.__dict__["relativeHeight"]
            break
    assert isinstance(descriptor, property)

def test_mm_pictograms_boxrelativeanchor_has_relativeWidth():
    assert hasattr(mm_pictograms_BoxRelativeAnchor, "relativeWidth")
    descriptor = None
    for klass in mm_pictograms_BoxRelativeAnchor.__mro__:
        if "relativeWidth" in klass.__dict__:
            descriptor = klass.__dict__["relativeWidth"]
            break
    assert isinstance(descriptor, property)



def test_connection_is_not_abstract():
    assert not inspect.isabstract(Connection)


def test_connection_constructor_exists():
    assert callable(Connection.__init__)


def test_connection_constructor_args():
    sig = inspect.signature(Connection.__init__)
    params = list(sig.parameters.keys())



def test_mm_pictograms_manhattanconnection_is_not_abstract():
    assert not inspect.isabstract(mm_pictograms_ManhattanConnection)


def test_mm_pictograms_manhattanconnection_constructor_exists():
    assert callable(mm_pictograms_ManhattanConnection.__init__)


def test_mm_pictograms_manhattanconnection_constructor_args():
    sig = inspect.signature(mm_pictograms_ManhattanConnection.__init__)
    params = list(sig.parameters.keys())



def test_mm_pictograms_curvedconnection_is_not_abstract():
    assert not inspect.isabstract(mm_pictograms_CurvedConnection)


def test_mm_pictograms_curvedconnection_constructor_exists():
    assert callable(mm_pictograms_CurvedConnection.__init__)


def test_mm_pictograms_curvedconnection_constructor_args():
    sig = inspect.signature(mm_pictograms_CurvedConnection.__init__)
    params = list(sig.parameters.keys())



def test_mm_pictograms_freeformconnection_is_not_abstract():
    assert not inspect.isabstract(mm_pictograms_FreeFormConnection)


def test_mm_pictograms_freeformconnection_constructor_exists():
    assert callable(mm_pictograms_FreeFormConnection.__init__)


def test_mm_pictograms_freeformconnection_constructor_args():
    sig = inspect.signature(mm_pictograms_FreeFormConnection.__init__)
    params = list(sig.parameters.keys())



def test_mm_pictograms_compositeconnection_is_not_abstract():
    assert not inspect.isabstract(mm_pictograms_CompositeConnection)


def test_mm_pictograms_compositeconnection_constructor_exists():
    assert callable(mm_pictograms_CompositeConnection.__init__)


def test_mm_pictograms_compositeconnection_constructor_args():
    sig = inspect.signature(mm_pictograms_CompositeConnection.__init__)
    params = list(sig.parameters.keys())



def test_stylecontainer_is_not_abstract():
    assert not inspect.isabstract(StyleContainer)


def test_stylecontainer_constructor_exists():
    assert callable(StyleContainer.__init__)


def test_stylecontainer_constructor_args():
    sig = inspect.signature(StyleContainer.__init__)
    params = list(sig.parameters.keys())



def test_mm_styles_style_is_not_abstract():
    assert not inspect.isabstract(mm_styles_Style)


def test_mm_styles_style_constructor_exists():
    assert callable(mm_styles_Style.__init__)


def test_mm_styles_style_constructor_args():
    sig = inspect.signature(mm_styles_Style.__init__)
    params = list(sig.parameters.keys())
    assert "proportional" in params, "Missing parameter 'proportional'"
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"
    assert "verticalAlignment" in params, "Missing parameter 'verticalAlignment'"
    assert "stretchH" in params, "Missing parameter 'stretchH'"
    assert "stretchV" in params, "Missing parameter 'stretchV'"
    assert "angle" in params, "Missing parameter 'angle'"
    assert "horizontalAlignment" in params, "Missing parameter 'horizontalAlignment'"

def test_mm_styles_style_has_proportional():
    assert hasattr(mm_styles_Style, "proportional")
    descriptor = None
    for klass in mm_styles_Style.__mro__:
        if "proportional" in klass.__dict__:
            descriptor = klass.__dict__["proportional"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_style_has_id():
    assert hasattr(mm_styles_Style, "id")
    descriptor = None
    for klass in mm_styles_Style.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_style_has_description():
    assert hasattr(mm_styles_Style, "description")
    descriptor = None
    for klass in mm_styles_Style.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_style_has_verticalAlignment():
    assert hasattr(mm_styles_Style, "verticalAlignment")
    descriptor = None
    for klass in mm_styles_Style.__mro__:
        if "verticalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["verticalAlignment"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_style_has_stretchH():
    assert hasattr(mm_styles_Style, "stretchH")
    descriptor = None
    for klass in mm_styles_Style.__mro__:
        if "stretchH" in klass.__dict__:
            descriptor = klass.__dict__["stretchH"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_style_has_stretchV():
    assert hasattr(mm_styles_Style, "stretchV")
    descriptor = None
    for klass in mm_styles_Style.__mro__:
        if "stretchV" in klass.__dict__:
            descriptor = klass.__dict__["stretchV"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_style_has_angle():
    assert hasattr(mm_styles_Style, "angle")
    descriptor = None
    for klass in mm_styles_Style.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)

def test_mm_styles_style_has_horizontalAlignment():
    assert hasattr(mm_styles_Style, "horizontalAlignment")
    descriptor = None
    for klass in mm_styles_Style.__mro__:
        if "horizontalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["horizontalAlignment"]
            break
    assert isinstance(descriptor, property)



def test_pictograms_containershape_is_not_abstract():
    assert not inspect.isabstract(pictograms_ContainerShape)


def test_pictograms_containershape_constructor_exists():
    assert callable(pictograms_ContainerShape.__init__)


def test_pictograms_containershape_constructor_args():
    sig = inspect.signature(pictograms_ContainerShape.__init__)
    params = list(sig.parameters.keys())



def test_mm_pictograms_diagram_is_not_abstract():
    assert not inspect.isabstract(mm_pictograms_Diagram)


def test_mm_pictograms_diagram_constructor_exists():
    assert callable(mm_pictograms_Diagram.__init__)


def test_mm_pictograms_diagram_constructor_args():
    sig = inspect.signature(mm_pictograms_Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "showGuides" in params, "Missing parameter 'showGuides'"
    assert "name" in params, "Missing parameter 'name'"
    assert "verticalGridUnit" in params, "Missing parameter 'verticalGridUnit'"
    assert "version" in params, "Missing parameter 'version'"
    assert "snapToGrid" in params, "Missing parameter 'snapToGrid'"
    assert "diagramTypeId" in params, "Missing parameter 'diagramTypeId'"
    assert "gridUnit" in params, "Missing parameter 'gridUnit'"

def test_mm_pictograms_diagram_has_showGuides():
    assert hasattr(mm_pictograms_Diagram, "showGuides")
    descriptor = None
    for klass in mm_pictograms_Diagram.__mro__:
        if "showGuides" in klass.__dict__:
            descriptor = klass.__dict__["showGuides"]
            break
    assert isinstance(descriptor, property)

def test_mm_pictograms_diagram_has_name():
    assert hasattr(mm_pictograms_Diagram, "name")
    descriptor = None
    for klass in mm_pictograms_Diagram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm_pictograms_diagram_has_verticalGridUnit():
    assert hasattr(mm_pictograms_Diagram, "verticalGridUnit")
    descriptor = None
    for klass in mm_pictograms_Diagram.__mro__:
        if "verticalGridUnit" in klass.__dict__:
            descriptor = klass.__dict__["verticalGridUnit"]
            break
    assert isinstance(descriptor, property)

def test_mm_pictograms_diagram_has_version():
    assert hasattr(mm_pictograms_Diagram, "version")
    descriptor = None
    for klass in mm_pictograms_Diagram.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_mm_pictograms_diagram_has_snapToGrid():
    assert hasattr(mm_pictograms_Diagram, "snapToGrid")
    descriptor = None
    for klass in mm_pictograms_Diagram.__mro__:
        if "snapToGrid" in klass.__dict__:
            descriptor = klass.__dict__["snapToGrid"]
            break
    assert isinstance(descriptor, property)

def test_mm_pictograms_diagram_has_diagramTypeId():
    assert hasattr(mm_pictograms_Diagram, "diagramTypeId")
    descriptor = None
    for klass in mm_pictograms_Diagram.__mro__:
        if "diagramTypeId" in klass.__dict__:
            descriptor = klass.__dict__["diagramTypeId"]
            break
    assert isinstance(descriptor, property)

def test_mm_pictograms_diagram_has_gridUnit():
    assert hasattr(mm_pictograms_Diagram, "gridUnit")
    descriptor = None
    for klass in mm_pictograms_Diagram.__mro__:
        if "gridUnit" in klass.__dict__:
            descriptor = klass.__dict__["gridUnit"]
            break
    assert isinstance(descriptor, property)



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_mm_pictograms_connectiondecorator_is_not_abstract():
    assert not inspect.isabstract(mm_pictograms_ConnectionDecorator)


def test_mm_pictograms_connectiondecorator_constructor_exists():
    assert callable(mm_pictograms_ConnectionDecorator.__init__)


def test_mm_pictograms_connectiondecorator_constructor_args():
    sig = inspect.signature(mm_pictograms_ConnectionDecorator.__init__)
    params = list(sig.parameters.keys())
    assert "locationRelative" in params, "Missing parameter 'locationRelative'"
    assert "location" in params, "Missing parameter 'location'"

def test_mm_pictograms_connectiondecorator_has_locationRelative():
    assert hasattr(mm_pictograms_ConnectionDecorator, "locationRelative")
    descriptor = None
    for klass in mm_pictograms_ConnectionDecorator.__mro__:
        if "locationRelative" in klass.__dict__:
            descriptor = klass.__dict__["locationRelative"]
            break
    assert isinstance(descriptor, property)

def test_mm_pictograms_connectiondecorator_has_location():
    assert hasattr(mm_pictograms_ConnectionDecorator, "location")
    descriptor = None
    for klass in mm_pictograms_ConnectionDecorator.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_mm_pictograms_containershape_is_not_abstract():
    assert not inspect.isabstract(mm_pictograms_ContainerShape)


def test_mm_pictograms_containershape_constructor_exists():
    assert callable(mm_pictograms_ContainerShape.__init__)


def test_mm_pictograms_containershape_constructor_args():
    sig = inspect.signature(mm_pictograms_ContainerShape.__init__)
    params = list(sig.parameters.keys())



def test_containershape_is_not_abstract():
    assert not inspect.isabstract(ContainerShape)


def test_containershape_constructor_exists():
    assert callable(ContainerShape.__init__)


def test_containershape_constructor_args():
    sig = inspect.signature(ContainerShape.__init__)
    params = list(sig.parameters.keys())



def test_anchorcontainer_is_not_abstract():
    assert not inspect.isabstract(AnchorContainer)


def test_anchorcontainer_constructor_exists():
    assert callable(AnchorContainer.__init__)


def test_anchorcontainer_constructor_args():
    sig = inspect.signature(AnchorContainer.__init__)
    params = list(sig.parameters.keys())



def test_mm_pictograms_connection_is_not_abstract():
    assert not inspect.isabstract(mm_pictograms_Connection)


def test_mm_pictograms_connection_constructor_exists():
    assert callable(mm_pictograms_Connection.__init__)


def test_mm_pictograms_connection_constructor_args():
    sig = inspect.signature(mm_pictograms_Connection.__init__)
    params = list(sig.parameters.keys())



def test_mm_pictograms_shape_is_not_abstract():
    assert not inspect.isabstract(mm_pictograms_Shape)


def test_mm_pictograms_shape_constructor_exists():
    assert callable(mm_pictograms_Shape.__init__)


def test_mm_pictograms_shape_constructor_args():
    sig = inspect.signature(mm_pictograms_Shape.__init__)
    params = list(sig.parameters.keys())



def test_styles_style_is_not_abstract():
    assert not inspect.isabstract(styles_Style)


def test_styles_style_constructor_exists():
    assert callable(styles_Style.__init__)


def test_styles_style_constructor_args():
    sig = inspect.signature(styles_Style.__init__)
    params = list(sig.parameters.keys())



def test_mm_stylecontainer_is_not_abstract():
    assert not inspect.isabstract(mm_StyleContainer)


def test_mm_stylecontainer_constructor_exists():
    assert callable(mm_StyleContainer.__init__)


def test_mm_stylecontainer_constructor_args():
    sig = inspect.signature(mm_StyleContainer.__init__)
    params = list(sig.parameters.keys())



def test_propertycontainer_is_not_abstract():
    assert not inspect.isabstract(PropertyContainer)


def test_propertycontainer_constructor_exists():
    assert callable(PropertyContainer.__init__)


def test_propertycontainer_constructor_args():
    sig = inspect.signature(PropertyContainer.__init__)
    params = list(sig.parameters.keys())



def test_mm_pictograms_pictogramlink_is_not_abstract():
    assert not inspect.isabstract(mm_pictograms_PictogramLink)


def test_mm_pictograms_pictogramlink_constructor_exists():
    assert callable(mm_pictograms_PictogramLink.__init__)


def test_mm_pictograms_pictogramlink_constructor_args():
    sig = inspect.signature(mm_pictograms_PictogramLink.__init__)
    params = list(sig.parameters.keys())



def test_mm_graphicsalgorithmcontainer_is_not_abstract():
    assert not inspect.isabstract(mm_GraphicsAlgorithmContainer)


def test_mm_graphicsalgorithmcontainer_constructor_exists():
    assert callable(mm_GraphicsAlgorithmContainer.__init__)


def test_mm_graphicsalgorithmcontainer_constructor_args():
    sig = inspect.signature(mm_GraphicsAlgorithmContainer.__init__)
    params = list(sig.parameters.keys())



def test_graphicsalgorithm_is_not_abstract():
    assert not inspect.isabstract(GraphicsAlgorithm)


def test_graphicsalgorithm_constructor_exists():
    assert callable(GraphicsAlgorithm.__init__)


def test_graphicsalgorithm_constructor_args():
    sig = inspect.signature(GraphicsAlgorithm.__init__)
    params = list(sig.parameters.keys())



def test_mm_algorithms_image_is_not_abstract():
    assert not inspect.isabstract(mm_algorithms_Image)


def test_mm_algorithms_image_constructor_exists():
    assert callable(mm_algorithms_Image.__init__)


def test_mm_algorithms_image_constructor_args():
    sig = inspect.signature(mm_algorithms_Image.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "stretchV" in params, "Missing parameter 'stretchV'"
    assert "stretchH" in params, "Missing parameter 'stretchH'"
    assert "proportional" in params, "Missing parameter 'proportional'"

def test_mm_algorithms_image_has_id():
    assert hasattr(mm_algorithms_Image, "id")
    descriptor = None
    for klass in mm_algorithms_Image.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mm_algorithms_image_has_stretchV():
    assert hasattr(mm_algorithms_Image, "stretchV")
    descriptor = None
    for klass in mm_algorithms_Image.__mro__:
        if "stretchV" in klass.__dict__:
            descriptor = klass.__dict__["stretchV"]
            break
    assert isinstance(descriptor, property)

def test_mm_algorithms_image_has_stretchH():
    assert hasattr(mm_algorithms_Image, "stretchH")
    descriptor = None
    for klass in mm_algorithms_Image.__mro__:
        if "stretchH" in klass.__dict__:
            descriptor = klass.__dict__["stretchH"]
            break
    assert isinstance(descriptor, property)

def test_mm_algorithms_image_has_proportional():
    assert hasattr(mm_algorithms_Image, "proportional")
    descriptor = None
    for klass in mm_algorithms_Image.__mro__:
        if "proportional" in klass.__dict__:
            descriptor = klass.__dict__["proportional"]
            break
    assert isinstance(descriptor, property)



def test_mm_algorithms_ellipse_is_not_abstract():
    assert not inspect.isabstract(mm_algorithms_Ellipse)


def test_mm_algorithms_ellipse_constructor_exists():
    assert callable(mm_algorithms_Ellipse.__init__)


def test_mm_algorithms_ellipse_constructor_args():
    sig = inspect.signature(mm_algorithms_Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_mm_algorithms_platformgraphicsalgorithm_is_not_abstract():
    assert not inspect.isabstract(mm_algorithms_PlatformGraphicsAlgorithm)


def test_mm_algorithms_platformgraphicsalgorithm_constructor_exists():
    assert callable(mm_algorithms_PlatformGraphicsAlgorithm.__init__)


def test_mm_algorithms_platformgraphicsalgorithm_constructor_args():
    sig = inspect.signature(mm_algorithms_PlatformGraphicsAlgorithm.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mm_algorithms_platformgraphicsalgorithm_has_id():
    assert hasattr(mm_algorithms_PlatformGraphicsAlgorithm, "id")
    descriptor = None
    for klass in mm_algorithms_PlatformGraphicsAlgorithm.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mm_algorithms_polyline_is_not_abstract():
    assert not inspect.isabstract(mm_algorithms_Polyline)


def test_mm_algorithms_polyline_constructor_exists():
    assert callable(mm_algorithms_Polyline.__init__)


def test_mm_algorithms_polyline_constructor_args():
    sig = inspect.signature(mm_algorithms_Polyline.__init__)
    params = list(sig.parameters.keys())



def test_mm_algorithms_rectangle_is_not_abstract():
    assert not inspect.isabstract(mm_algorithms_Rectangle)


def test_mm_algorithms_rectangle_constructor_exists():
    assert callable(mm_algorithms_Rectangle.__init__)


def test_mm_algorithms_rectangle_constructor_args():
    sig = inspect.signature(mm_algorithms_Rectangle.__init__)
    params = list(sig.parameters.keys())



def test_mm_algorithms_roundedrectangle_is_not_abstract():
    assert not inspect.isabstract(mm_algorithms_RoundedRectangle)


def test_mm_algorithms_roundedrectangle_constructor_exists():
    assert callable(mm_algorithms_RoundedRectangle.__init__)


def test_mm_algorithms_roundedrectangle_constructor_args():
    sig = inspect.signature(mm_algorithms_RoundedRectangle.__init__)
    params = list(sig.parameters.keys())
    assert "cornerWidth" in params, "Missing parameter 'cornerWidth'"
    assert "cornerHeight" in params, "Missing parameter 'cornerHeight'"

def test_mm_algorithms_roundedrectangle_has_cornerWidth():
    assert hasattr(mm_algorithms_RoundedRectangle, "cornerWidth")
    descriptor = None
    for klass in mm_algorithms_RoundedRectangle.__mro__:
        if "cornerWidth" in klass.__dict__:
            descriptor = klass.__dict__["cornerWidth"]
            break
    assert isinstance(descriptor, property)

def test_mm_algorithms_roundedrectangle_has_cornerHeight():
    assert hasattr(mm_algorithms_RoundedRectangle, "cornerHeight")
    descriptor = None
    for klass in mm_algorithms_RoundedRectangle.__mro__:
        if "cornerHeight" in klass.__dict__:
            descriptor = klass.__dict__["cornerHeight"]
            break
    assert isinstance(descriptor, property)



def test_mm_algorithms_abstracttext_is_not_abstract():
    assert not inspect.isabstract(mm_algorithms_AbstractText)


def test_mm_algorithms_abstracttext_constructor_exists():
    assert callable(mm_algorithms_AbstractText.__init__)


def test_mm_algorithms_abstracttext_constructor_args():
    sig = inspect.signature(mm_algorithms_AbstractText.__init__)
    params = list(sig.parameters.keys())
    assert "horizontalAlignment" in params, "Missing parameter 'horizontalAlignment'"
    assert "angle" in params, "Missing parameter 'angle'"
    assert "value" in params, "Missing parameter 'value'"
    assert "verticalAlignment" in params, "Missing parameter 'verticalAlignment'"

def test_mm_algorithms_abstracttext_has_horizontalAlignment():
    assert hasattr(mm_algorithms_AbstractText, "horizontalAlignment")
    descriptor = None
    for klass in mm_algorithms_AbstractText.__mro__:
        if "horizontalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["horizontalAlignment"]
            break
    assert isinstance(descriptor, property)

def test_mm_algorithms_abstracttext_has_angle():
    assert hasattr(mm_algorithms_AbstractText, "angle")
    descriptor = None
    for klass in mm_algorithms_AbstractText.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)

def test_mm_algorithms_abstracttext_has_value():
    assert hasattr(mm_algorithms_AbstractText, "value")
    descriptor = None
    for klass in mm_algorithms_AbstractText.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_mm_algorithms_abstracttext_has_verticalAlignment():
    assert hasattr(mm_algorithms_AbstractText, "verticalAlignment")
    descriptor = None
    for klass in mm_algorithms_AbstractText.__mro__:
        if "verticalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["verticalAlignment"]
            break
    assert isinstance(descriptor, property)



def test_graphicsalgorithmcontainer_is_not_abstract():
    assert not inspect.isabstract(GraphicsAlgorithmContainer)


def test_graphicsalgorithmcontainer_constructor_exists():
    assert callable(GraphicsAlgorithmContainer.__init__)


def test_graphicsalgorithmcontainer_constructor_args():
    sig = inspect.signature(GraphicsAlgorithmContainer.__init__)
    params = list(sig.parameters.keys())



def test_mm_algorithms_graphicsalgorithm_is_not_abstract():
    assert not inspect.isabstract(mm_algorithms_GraphicsAlgorithm)


def test_mm_algorithms_graphicsalgorithm_constructor_exists():
    assert callable(mm_algorithms_GraphicsAlgorithm.__init__)


def test_mm_algorithms_graphicsalgorithm_constructor_args():
    sig = inspect.signature(mm_algorithms_GraphicsAlgorithm.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_mm_algorithms_graphicsalgorithm_has_height():
    assert hasattr(mm_algorithms_GraphicsAlgorithm, "height")
    descriptor = None
    for klass in mm_algorithms_GraphicsAlgorithm.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_mm_algorithms_graphicsalgorithm_has_width():
    assert hasattr(mm_algorithms_GraphicsAlgorithm, "width")
    descriptor = None
    for klass in mm_algorithms_GraphicsAlgorithm.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_mm_algorithms_graphicsalgorithm_has_x():
    assert hasattr(mm_algorithms_GraphicsAlgorithm, "x")
    descriptor = None
    for klass in mm_algorithms_GraphicsAlgorithm.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_mm_algorithms_graphicsalgorithm_has_y():
    assert hasattr(mm_algorithms_GraphicsAlgorithm, "y")
    descriptor = None
    for klass in mm_algorithms_GraphicsAlgorithm.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_mm_pictograms_pictogramelement_is_not_abstract():
    assert not inspect.isabstract(mm_pictograms_PictogramElement)


def test_mm_pictograms_pictogramelement_constructor_exists():
    assert callable(mm_pictograms_PictogramElement.__init__)


def test_mm_pictograms_pictogramelement_constructor_args():
    sig = inspect.signature(mm_pictograms_PictogramElement.__init__)
    params = list(sig.parameters.keys())
    assert "visible" in params, "Missing parameter 'visible'"
    assert "active" in params, "Missing parameter 'active'"

def test_mm_pictograms_pictogramelement_has_visible():
    assert hasattr(mm_pictograms_PictogramElement, "visible")
    descriptor = None
    for klass in mm_pictograms_PictogramElement.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_mm_pictograms_pictogramelement_has_active():
    assert hasattr(mm_pictograms_PictogramElement, "active")
    descriptor = None
    for klass in mm_pictograms_PictogramElement.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)



def test_pictogramlink_is_not_abstract():
    assert not inspect.isabstract(PictogramLink)


def test_pictogramlink_constructor_exists():
    assert callable(PictogramLink.__init__)


def test_pictogramlink_constructor_args():
    sig = inspect.signature(PictogramLink.__init__)
    params = list(sig.parameters.keys())



def test_styles_font_is_not_abstract():
    assert not inspect.isabstract(styles_Font)


def test_styles_font_constructor_exists():
    assert callable(styles_Font.__init__)


def test_styles_font_constructor_args():
    sig = inspect.signature(styles_Font.__init__)
    params = list(sig.parameters.keys())



def test_styles_color_is_not_abstract():
    assert not inspect.isabstract(styles_Color)


def test_styles_color_constructor_exists():
    assert callable(styles_Color.__init__)


def test_styles_color_constructor_args():
    sig = inspect.signature(styles_Color.__init__)
    params = list(sig.parameters.keys())



def test_mm_propertycontainer_is_not_abstract():
    assert not inspect.isabstract(mm_PropertyContainer)


def test_mm_propertycontainer_constructor_exists():
    assert callable(mm_PropertyContainer.__init__)


def test_mm_propertycontainer_constructor_args():
    sig = inspect.signature(mm_PropertyContainer.__init__)
    params = list(sig.parameters.keys())



def test_mm_property_is_not_abstract():
    assert not inspect.isabstract(mm_Property)


def test_mm_property_constructor_exists():
    assert callable(mm_Property.__init__)


def test_mm_property_constructor_args():
    sig = inspect.signature(mm_Property.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_mm_property_has_key():
    assert hasattr(mm_Property, "key")
    descriptor = None
    for klass in mm_Property.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_mm_property_has_value():
    assert hasattr(mm_Property, "value")
    descriptor = None
    for klass in mm_Property.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_orientation_exists():
    # Check that the Enumeration exists
    assert Orientation is not None

def test_orientation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Orientation]
    expected_literals = [
        "UNSPECIFIED",
        "ALIGNMENT_LEFT",
        "ALIGNMENT_CENTER",
        "ALIGNMENT_MIDDLE",
        "ALIGNMENT_TOP",
        "ALIGNMENT_RIGHT",
        "ALIGNMENT_BOTTOM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Orientation"

def test_linestyle_exists():
    # Check that the Enumeration exists
    assert LineStyle is not None

def test_linestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineStyle]
    expected_literals = [
        "DASH",
        "DOT",
        "DASHDOTDOT",
        "UNSPECIFIED",
        "DASHDOT",
        "SOLID",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineStyle"

def test_underlinestyle_exists():
    # Check that the Enumeration exists
    assert UnderlineStyle is not None

def test_underlinestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnderlineStyle]
    expected_literals = [
        "UNDERLINE_SINGLE",
        "UNDERLINE_SQUIGGLE",
        "UNDERLINE_DOUBLE",
        "UNDERLINE_ERROR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnderlineStyle"

def test_locationtype_exists():
    # Check that the Enumeration exists
    assert LocationType is not None

def test_locationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LocationType]
    expected_literals = [
        "LOCATION_TYPE_RELATIVE",
        "LOCATION_TYPE_ABSOLUTE_START",
        "LOCATION_TYPE_ABSOLUTE_END",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LocationType"


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
styles_TextStyle_strategy = st.builds(
    styles_TextStyle,
)
mm_styles_TextStyleRegion_strategy = st.builds(
    mm_styles_TextStyleRegion,
    end=
        st.integers(),
    start=
        st.integers()
)
mm_styles_Font_strategy = st.builds(
    mm_styles_Font,
    name=
        safe_text,
    bold=
        st.booleans(),
    italic=
        st.booleans(),
    size=
        st.integers()
)
styles_GradientColoredAreas_strategy = st.builds(
    styles_GradientColoredAreas,
)
mm_styles_AdaptedGradientColoredAreas_strategy = st.builds(
    mm_styles_AdaptedGradientColoredAreas,
    gradientType=
        safe_text,
    definedStyleId=
        safe_text
)
styles_GradientColoredArea_strategy = st.builds(
    styles_GradientColoredArea,
)
mm_styles_GradientColoredAreas_strategy = st.builds(
    mm_styles_GradientColoredAreas,
    styleAdaption=
        safe_text
)
styles_GradientColoredLocation_strategy = st.builds(
    styles_GradientColoredLocation,
)
mm_styles_GradientColoredArea_strategy = st.builds(
    mm_styles_GradientColoredArea,
)
mm_styles_GradientColoredLocation_strategy = st.builds(
    mm_styles_GradientColoredLocation,
    locationType=
        safe_text,
    locationValue=
        safe_text
)
styles_RenderingStyle_strategy = st.builds(
    styles_RenderingStyle,
)
mm_styles_TextStyle_strategy = st.builds(
    mm_styles_TextStyle,
    strikeout=
        st.booleans(),
    underlineStyle=
        safe_text,
    underline=
        st.booleans()
)
mm_styles_PrecisionPoint_strategy = st.builds(
    mm_styles_PrecisionPoint,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
mm_styles_Color_strategy = st.builds(
    mm_styles_Color,
    red=
        st.integers(),
    green=
        st.integers(),
    blue=
        st.integers()
)
mm_styles_Point_strategy = st.builds(
    mm_styles_Point,
    after=
        st.integers(),
    x=
        st.integers(),
    y=
        st.integers(),
    before=
        st.integers()
)
styles_AdaptedGradientColoredAreas_strategy = st.builds(
    styles_AdaptedGradientColoredAreas,
)
mm_styles_RenderingStyle_strategy = st.builds(
    mm_styles_RenderingStyle,
)
styles_TextStyleRegion_strategy = st.builds(
    styles_TextStyleRegion,
)
mm_styles_AbstractStyle_strategy = st.builds(
    mm_styles_AbstractStyle,
    transparency=
        safe_text,
    lineWidth=
        safe_text,
    lineVisible=
        safe_text,
    filled=
        safe_text,
    lineStyle=
        safe_text
)
styles_mm_StyleContainer_strategy = st.builds(
    styles_mm_StyleContainer,
)
styles_AbstractStyle_strategy = st.builds(
    styles_AbstractStyle,
)
CurvedConnection_strategy = st.builds(
    CurvedConnection,
)
styles_PrecisionPoint_strategy = st.builds(
    styles_PrecisionPoint,
)
Polyline_strategy = st.builds(
    Polyline,
)
mm_algorithms_Polygon_strategy = st.builds(
    mm_algorithms_Polygon,
)
AbstractText_strategy = st.builds(
    AbstractText,
)
mm_algorithms_MultiText_strategy = st.builds(
    mm_algorithms_MultiText,
)
mm_algorithms_Text_strategy = st.builds(
    mm_algorithms_Text,
)
styles_Point_strategy = st.builds(
    styles_Point,
)
AdvancedAnchor_strategy = st.builds(
    AdvancedAnchor,
)
mm_pictograms_FixPointAnchor_strategy = st.builds(
    mm_pictograms_FixPointAnchor,
)
PictogramElement_strategy = st.builds(
    PictogramElement,
)
mm_pictograms_AnchorContainer_strategy = st.builds(
    mm_pictograms_AnchorContainer,
)
mm_pictograms_Anchor_strategy = st.builds(
    mm_pictograms_Anchor,
)
ConnectionDecorator_strategy = st.builds(
    ConnectionDecorator,
)
Diagram_strategy = st.builds(
    Diagram,
)
Anchor_strategy = st.builds(
    Anchor,
)
mm_pictograms_AdvancedAnchor_strategy = st.builds(
    mm_pictograms_AdvancedAnchor,
    useAnchorLocationAsConnectionEndpoint=
        st.booleans()
)
pictograms_mm_EObject_strategy = st.builds(
    pictograms_mm_EObject,
)
mm_pictograms_ChopboxAnchor_strategy = st.builds(
    mm_pictograms_ChopboxAnchor,
)
mm_pictograms_BoxRelativeAnchor_strategy = st.builds(
    mm_pictograms_BoxRelativeAnchor,
    relativeHeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    relativeWidth=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Connection_strategy = st.builds(
    Connection,
)
mm_pictograms_ManhattanConnection_strategy = st.builds(
    mm_pictograms_ManhattanConnection,
)
mm_pictograms_CurvedConnection_strategy = st.builds(
    mm_pictograms_CurvedConnection,
)
mm_pictograms_FreeFormConnection_strategy = st.builds(
    mm_pictograms_FreeFormConnection,
)
mm_pictograms_CompositeConnection_strategy = st.builds(
    mm_pictograms_CompositeConnection,
)
StyleContainer_strategy = st.builds(
    StyleContainer,
)
mm_styles_Style_strategy = st.builds(
    mm_styles_Style,
    proportional=
        safe_text,
    id=
        safe_text,
    description=
        safe_text,
    verticalAlignment=
        safe_text,
    stretchH=
        safe_text,
    stretchV=
        safe_text,
    angle=
        safe_text,
    horizontalAlignment=
        safe_text
)
pictograms_ContainerShape_strategy = st.builds(
    pictograms_ContainerShape,
)
mm_pictograms_Diagram_strategy = st.builds(
    mm_pictograms_Diagram,
    showGuides=
        st.booleans(),
    name=
        safe_text,
    verticalGridUnit=
        st.integers(),
    version=
        safe_text,
    snapToGrid=
        st.booleans(),
    diagramTypeId=
        safe_text,
    gridUnit=
        st.integers()
)
Shape_strategy = st.builds(
    Shape,
)
mm_pictograms_ConnectionDecorator_strategy = st.builds(
    mm_pictograms_ConnectionDecorator,
    locationRelative=
        st.booleans(),
    location=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
mm_pictograms_ContainerShape_strategy = st.builds(
    mm_pictograms_ContainerShape,
)
ContainerShape_strategy = st.builds(
    ContainerShape,
)
AnchorContainer_strategy = st.builds(
    AnchorContainer,
)
mm_pictograms_Connection_strategy = st.builds(
    mm_pictograms_Connection,
)
mm_pictograms_Shape_strategy = st.builds(
    mm_pictograms_Shape,
)
styles_Style_strategy = st.builds(
    styles_Style,
)
mm_StyleContainer_strategy = st.builds(
    mm_StyleContainer,
)
PropertyContainer_strategy = st.builds(
    PropertyContainer,
)
mm_pictograms_PictogramLink_strategy = st.builds(
    mm_pictograms_PictogramLink,
)
mm_GraphicsAlgorithmContainer_strategy = st.builds(
    mm_GraphicsAlgorithmContainer,
)
GraphicsAlgorithm_strategy = st.builds(
    GraphicsAlgorithm,
)
mm_algorithms_Image_strategy = st.builds(
    mm_algorithms_Image,
    id=
        safe_text,
    stretchV=
        safe_text,
    stretchH=
        safe_text,
    proportional=
        safe_text
)
mm_algorithms_Ellipse_strategy = st.builds(
    mm_algorithms_Ellipse,
)
mm_algorithms_PlatformGraphicsAlgorithm_strategy = st.builds(
    mm_algorithms_PlatformGraphicsAlgorithm,
    id=
        safe_text
)
mm_algorithms_Polyline_strategy = st.builds(
    mm_algorithms_Polyline,
)
mm_algorithms_Rectangle_strategy = st.builds(
    mm_algorithms_Rectangle,
)
mm_algorithms_RoundedRectangle_strategy = st.builds(
    mm_algorithms_RoundedRectangle,
    cornerWidth=
        st.integers(),
    cornerHeight=
        st.integers()
)
mm_algorithms_AbstractText_strategy = st.builds(
    mm_algorithms_AbstractText,
    horizontalAlignment=
        safe_text,
    angle=
        safe_text,
    value=
        safe_text,
    verticalAlignment=
        safe_text
)
GraphicsAlgorithmContainer_strategy = st.builds(
    GraphicsAlgorithmContainer,
)
mm_algorithms_GraphicsAlgorithm_strategy = st.builds(
    mm_algorithms_GraphicsAlgorithm,
    height=
        st.integers(),
    width=
        st.integers(),
    x=
        st.integers(),
    y=
        st.integers()
)
mm_pictograms_PictogramElement_strategy = st.builds(
    mm_pictograms_PictogramElement,
    visible=
        st.booleans(),
    active=
        st.booleans()
)
PictogramLink_strategy = st.builds(
    PictogramLink,
)
styles_Font_strategy = st.builds(
    styles_Font,
)
styles_Color_strategy = st.builds(
    styles_Color,
)
mm_PropertyContainer_strategy = st.builds(
    mm_PropertyContainer,
)
mm_Property_strategy = st.builds(
    mm_Property,
    key=
        safe_text,
    value=
        safe_text
)

@given(instance=styles_TextStyle_strategy)
@settings(max_examples=50)
def test_styles_textstyle_instantiation(instance):
    assert isinstance(instance, styles_TextStyle)

@given(instance=mm_styles_TextStyleRegion_strategy)
@settings(max_examples=50)
def test_mm_styles_textstyleregion_instantiation(instance):
    assert isinstance(instance, mm_styles_TextStyleRegion)



@given(instance=mm_styles_TextStyleRegion_strategy)
def test_mm_styles_textstyleregion_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original



@given(instance=mm_styles_TextStyleRegion_strategy)
def test_mm_styles_textstyleregion_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=mm_styles_Font_strategy)
@settings(max_examples=50)
def test_mm_styles_font_instantiation(instance):
    assert isinstance(instance, mm_styles_Font)



@given(instance=mm_styles_Font_strategy)
def test_mm_styles_font_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_styles_Font_strategy)
def test_mm_styles_font_bold_setter(instance):
    original = instance.bold
    instance.bold = original
    assert instance.bold == original



@given(instance=mm_styles_Font_strategy)
def test_mm_styles_font_italic_setter(instance):
    original = instance.italic
    instance.italic = original
    assert instance.italic == original



@given(instance=mm_styles_Font_strategy)
def test_mm_styles_font_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=styles_GradientColoredAreas_strategy)
@settings(max_examples=50)
def test_styles_gradientcoloredareas_instantiation(instance):
    assert isinstance(instance, styles_GradientColoredAreas)

@given(instance=mm_styles_AdaptedGradientColoredAreas_strategy)
@settings(max_examples=50)
def test_mm_styles_adaptedgradientcoloredareas_instantiation(instance):
    assert isinstance(instance, mm_styles_AdaptedGradientColoredAreas)



@given(instance=mm_styles_AdaptedGradientColoredAreas_strategy)
def test_mm_styles_adaptedgradientcoloredareas_gradientType_setter(instance):
    original = instance.gradientType
    instance.gradientType = original
    assert instance.gradientType == original



@given(instance=mm_styles_AdaptedGradientColoredAreas_strategy)
def test_mm_styles_adaptedgradientcoloredareas_definedStyleId_setter(instance):
    original = instance.definedStyleId
    instance.definedStyleId = original
    assert instance.definedStyleId == original

@given(instance=styles_GradientColoredArea_strategy)
@settings(max_examples=50)
def test_styles_gradientcoloredarea_instantiation(instance):
    assert isinstance(instance, styles_GradientColoredArea)

@given(instance=mm_styles_GradientColoredAreas_strategy)
@settings(max_examples=50)
def test_mm_styles_gradientcoloredareas_instantiation(instance):
    assert isinstance(instance, mm_styles_GradientColoredAreas)



@given(instance=mm_styles_GradientColoredAreas_strategy)
def test_mm_styles_gradientcoloredareas_styleAdaption_setter(instance):
    original = instance.styleAdaption
    instance.styleAdaption = original
    assert instance.styleAdaption == original

@given(instance=styles_GradientColoredLocation_strategy)
@settings(max_examples=50)
def test_styles_gradientcoloredlocation_instantiation(instance):
    assert isinstance(instance, styles_GradientColoredLocation)

@given(instance=mm_styles_GradientColoredArea_strategy)
@settings(max_examples=50)
def test_mm_styles_gradientcoloredarea_instantiation(instance):
    assert isinstance(instance, mm_styles_GradientColoredArea)

@given(instance=mm_styles_GradientColoredLocation_strategy)
@settings(max_examples=50)
def test_mm_styles_gradientcoloredlocation_instantiation(instance):
    assert isinstance(instance, mm_styles_GradientColoredLocation)



@given(instance=mm_styles_GradientColoredLocation_strategy)
def test_mm_styles_gradientcoloredlocation_locationType_setter(instance):
    original = instance.locationType
    instance.locationType = original
    assert instance.locationType == original



@given(instance=mm_styles_GradientColoredLocation_strategy)
def test_mm_styles_gradientcoloredlocation_locationValue_setter(instance):
    original = instance.locationValue
    instance.locationValue = original
    assert instance.locationValue == original

@given(instance=styles_RenderingStyle_strategy)
@settings(max_examples=50)
def test_styles_renderingstyle_instantiation(instance):
    assert isinstance(instance, styles_RenderingStyle)

@given(instance=mm_styles_TextStyle_strategy)
@settings(max_examples=50)
def test_mm_styles_textstyle_instantiation(instance):
    assert isinstance(instance, mm_styles_TextStyle)



@given(instance=mm_styles_TextStyle_strategy)
def test_mm_styles_textstyle_strikeout_setter(instance):
    original = instance.strikeout
    instance.strikeout = original
    assert instance.strikeout == original



@given(instance=mm_styles_TextStyle_strategy)
def test_mm_styles_textstyle_underlineStyle_setter(instance):
    original = instance.underlineStyle
    instance.underlineStyle = original
    assert instance.underlineStyle == original



@given(instance=mm_styles_TextStyle_strategy)
def test_mm_styles_textstyle_underline_setter(instance):
    original = instance.underline
    instance.underline = original
    assert instance.underline == original

@given(instance=mm_styles_PrecisionPoint_strategy)
@settings(max_examples=50)
def test_mm_styles_precisionpoint_instantiation(instance):
    assert isinstance(instance, mm_styles_PrecisionPoint)



@given(instance=mm_styles_PrecisionPoint_strategy)
def test_mm_styles_precisionpoint_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=mm_styles_PrecisionPoint_strategy)
def test_mm_styles_precisionpoint_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=mm_styles_Color_strategy)
@settings(max_examples=50)
def test_mm_styles_color_instantiation(instance):
    assert isinstance(instance, mm_styles_Color)



@given(instance=mm_styles_Color_strategy)
def test_mm_styles_color_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original



@given(instance=mm_styles_Color_strategy)
def test_mm_styles_color_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original



@given(instance=mm_styles_Color_strategy)
def test_mm_styles_color_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original

@given(instance=mm_styles_Point_strategy)
@settings(max_examples=50)
def test_mm_styles_point_instantiation(instance):
    assert isinstance(instance, mm_styles_Point)



@given(instance=mm_styles_Point_strategy)
def test_mm_styles_point_after_setter(instance):
    original = instance.after
    instance.after = original
    assert instance.after == original



@given(instance=mm_styles_Point_strategy)
def test_mm_styles_point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=mm_styles_Point_strategy)
def test_mm_styles_point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=mm_styles_Point_strategy)
def test_mm_styles_point_before_setter(instance):
    original = instance.before
    instance.before = original
    assert instance.before == original

@given(instance=styles_AdaptedGradientColoredAreas_strategy)
@settings(max_examples=50)
def test_styles_adaptedgradientcoloredareas_instantiation(instance):
    assert isinstance(instance, styles_AdaptedGradientColoredAreas)

@given(instance=mm_styles_RenderingStyle_strategy)
@settings(max_examples=50)
def test_mm_styles_renderingstyle_instantiation(instance):
    assert isinstance(instance, mm_styles_RenderingStyle)

@given(instance=styles_TextStyleRegion_strategy)
@settings(max_examples=50)
def test_styles_textstyleregion_instantiation(instance):
    assert isinstance(instance, styles_TextStyleRegion)

@given(instance=mm_styles_AbstractStyle_strategy)
@settings(max_examples=50)
def test_mm_styles_abstractstyle_instantiation(instance):
    assert isinstance(instance, mm_styles_AbstractStyle)



@given(instance=mm_styles_AbstractStyle_strategy)
def test_mm_styles_abstractstyle_transparency_setter(instance):
    original = instance.transparency
    instance.transparency = original
    assert instance.transparency == original



@given(instance=mm_styles_AbstractStyle_strategy)
def test_mm_styles_abstractstyle_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original



@given(instance=mm_styles_AbstractStyle_strategy)
def test_mm_styles_abstractstyle_lineVisible_setter(instance):
    original = instance.lineVisible
    instance.lineVisible = original
    assert instance.lineVisible == original



@given(instance=mm_styles_AbstractStyle_strategy)
def test_mm_styles_abstractstyle_filled_setter(instance):
    original = instance.filled
    instance.filled = original
    assert instance.filled == original



@given(instance=mm_styles_AbstractStyle_strategy)
def test_mm_styles_abstractstyle_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original

@given(instance=styles_mm_StyleContainer_strategy)
@settings(max_examples=50)
def test_styles_mm_stylecontainer_instantiation(instance):
    assert isinstance(instance, styles_mm_StyleContainer)

@given(instance=styles_AbstractStyle_strategy)
@settings(max_examples=50)
def test_styles_abstractstyle_instantiation(instance):
    assert isinstance(instance, styles_AbstractStyle)

@given(instance=CurvedConnection_strategy)
@settings(max_examples=50)
def test_curvedconnection_instantiation(instance):
    assert isinstance(instance, CurvedConnection)

@given(instance=styles_PrecisionPoint_strategy)
@settings(max_examples=50)
def test_styles_precisionpoint_instantiation(instance):
    assert isinstance(instance, styles_PrecisionPoint)

@given(instance=Polyline_strategy)
@settings(max_examples=50)
def test_polyline_instantiation(instance):
    assert isinstance(instance, Polyline)

@given(instance=mm_algorithms_Polygon_strategy)
@settings(max_examples=50)
def test_mm_algorithms_polygon_instantiation(instance):
    assert isinstance(instance, mm_algorithms_Polygon)

@given(instance=AbstractText_strategy)
@settings(max_examples=50)
def test_abstracttext_instantiation(instance):
    assert isinstance(instance, AbstractText)

@given(instance=mm_algorithms_MultiText_strategy)
@settings(max_examples=50)
def test_mm_algorithms_multitext_instantiation(instance):
    assert isinstance(instance, mm_algorithms_MultiText)

@given(instance=mm_algorithms_Text_strategy)
@settings(max_examples=50)
def test_mm_algorithms_text_instantiation(instance):
    assert isinstance(instance, mm_algorithms_Text)

@given(instance=styles_Point_strategy)
@settings(max_examples=50)
def test_styles_point_instantiation(instance):
    assert isinstance(instance, styles_Point)

@given(instance=AdvancedAnchor_strategy)
@settings(max_examples=50)
def test_advancedanchor_instantiation(instance):
    assert isinstance(instance, AdvancedAnchor)

@given(instance=mm_pictograms_FixPointAnchor_strategy)
@settings(max_examples=50)
def test_mm_pictograms_fixpointanchor_instantiation(instance):
    assert isinstance(instance, mm_pictograms_FixPointAnchor)

@given(instance=PictogramElement_strategy)
@settings(max_examples=50)
def test_pictogramelement_instantiation(instance):
    assert isinstance(instance, PictogramElement)

@given(instance=mm_pictograms_AnchorContainer_strategy)
@settings(max_examples=50)
def test_mm_pictograms_anchorcontainer_instantiation(instance):
    assert isinstance(instance, mm_pictograms_AnchorContainer)

@given(instance=mm_pictograms_Anchor_strategy)
@settings(max_examples=50)
def test_mm_pictograms_anchor_instantiation(instance):
    assert isinstance(instance, mm_pictograms_Anchor)

@given(instance=ConnectionDecorator_strategy)
@settings(max_examples=50)
def test_connectiondecorator_instantiation(instance):
    assert isinstance(instance, ConnectionDecorator)

@given(instance=Diagram_strategy)
@settings(max_examples=50)
def test_diagram_instantiation(instance):
    assert isinstance(instance, Diagram)

@given(instance=Anchor_strategy)
@settings(max_examples=50)
def test_anchor_instantiation(instance):
    assert isinstance(instance, Anchor)

@given(instance=mm_pictograms_AdvancedAnchor_strategy)
@settings(max_examples=50)
def test_mm_pictograms_advancedanchor_instantiation(instance):
    assert isinstance(instance, mm_pictograms_AdvancedAnchor)



@given(instance=mm_pictograms_AdvancedAnchor_strategy)
def test_mm_pictograms_advancedanchor_useAnchorLocationAsConnectionEndpoint_setter(instance):
    original = instance.useAnchorLocationAsConnectionEndpoint
    instance.useAnchorLocationAsConnectionEndpoint = original
    assert instance.useAnchorLocationAsConnectionEndpoint == original

@given(instance=pictograms_mm_EObject_strategy)
@settings(max_examples=50)
def test_pictograms_mm_eobject_instantiation(instance):
    assert isinstance(instance, pictograms_mm_EObject)

@given(instance=mm_pictograms_ChopboxAnchor_strategy)
@settings(max_examples=50)
def test_mm_pictograms_chopboxanchor_instantiation(instance):
    assert isinstance(instance, mm_pictograms_ChopboxAnchor)

@given(instance=mm_pictograms_BoxRelativeAnchor_strategy)
@settings(max_examples=50)
def test_mm_pictograms_boxrelativeanchor_instantiation(instance):
    assert isinstance(instance, mm_pictograms_BoxRelativeAnchor)



@given(instance=mm_pictograms_BoxRelativeAnchor_strategy)
def test_mm_pictograms_boxrelativeanchor_relativeHeight_setter(instance):
    original = instance.relativeHeight
    instance.relativeHeight = original
    assert instance.relativeHeight == original



@given(instance=mm_pictograms_BoxRelativeAnchor_strategy)
def test_mm_pictograms_boxrelativeanchor_relativeWidth_setter(instance):
    original = instance.relativeWidth
    instance.relativeWidth = original
    assert instance.relativeWidth == original

@given(instance=Connection_strategy)
@settings(max_examples=50)
def test_connection_instantiation(instance):
    assert isinstance(instance, Connection)

@given(instance=mm_pictograms_ManhattanConnection_strategy)
@settings(max_examples=50)
def test_mm_pictograms_manhattanconnection_instantiation(instance):
    assert isinstance(instance, mm_pictograms_ManhattanConnection)

@given(instance=mm_pictograms_CurvedConnection_strategy)
@settings(max_examples=50)
def test_mm_pictograms_curvedconnection_instantiation(instance):
    assert isinstance(instance, mm_pictograms_CurvedConnection)

@given(instance=mm_pictograms_FreeFormConnection_strategy)
@settings(max_examples=50)
def test_mm_pictograms_freeformconnection_instantiation(instance):
    assert isinstance(instance, mm_pictograms_FreeFormConnection)

@given(instance=mm_pictograms_CompositeConnection_strategy)
@settings(max_examples=50)
def test_mm_pictograms_compositeconnection_instantiation(instance):
    assert isinstance(instance, mm_pictograms_CompositeConnection)

@given(instance=StyleContainer_strategy)
@settings(max_examples=50)
def test_stylecontainer_instantiation(instance):
    assert isinstance(instance, StyleContainer)

@given(instance=mm_styles_Style_strategy)
@settings(max_examples=50)
def test_mm_styles_style_instantiation(instance):
    assert isinstance(instance, mm_styles_Style)



@given(instance=mm_styles_Style_strategy)
def test_mm_styles_style_proportional_setter(instance):
    original = instance.proportional
    instance.proportional = original
    assert instance.proportional == original



@given(instance=mm_styles_Style_strategy)
def test_mm_styles_style_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=mm_styles_Style_strategy)
def test_mm_styles_style_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=mm_styles_Style_strategy)
def test_mm_styles_style_verticalAlignment_setter(instance):
    original = instance.verticalAlignment
    instance.verticalAlignment = original
    assert instance.verticalAlignment == original



@given(instance=mm_styles_Style_strategy)
def test_mm_styles_style_stretchH_setter(instance):
    original = instance.stretchH
    instance.stretchH = original
    assert instance.stretchH == original



@given(instance=mm_styles_Style_strategy)
def test_mm_styles_style_stretchV_setter(instance):
    original = instance.stretchV
    instance.stretchV = original
    assert instance.stretchV == original



@given(instance=mm_styles_Style_strategy)
def test_mm_styles_style_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original



@given(instance=mm_styles_Style_strategy)
def test_mm_styles_style_horizontalAlignment_setter(instance):
    original = instance.horizontalAlignment
    instance.horizontalAlignment = original
    assert instance.horizontalAlignment == original

@given(instance=pictograms_ContainerShape_strategy)
@settings(max_examples=50)
def test_pictograms_containershape_instantiation(instance):
    assert isinstance(instance, pictograms_ContainerShape)

@given(instance=mm_pictograms_Diagram_strategy)
@settings(max_examples=50)
def test_mm_pictograms_diagram_instantiation(instance):
    assert isinstance(instance, mm_pictograms_Diagram)



@given(instance=mm_pictograms_Diagram_strategy)
def test_mm_pictograms_diagram_showGuides_setter(instance):
    original = instance.showGuides
    instance.showGuides = original
    assert instance.showGuides == original



@given(instance=mm_pictograms_Diagram_strategy)
def test_mm_pictograms_diagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_pictograms_Diagram_strategy)
def test_mm_pictograms_diagram_verticalGridUnit_setter(instance):
    original = instance.verticalGridUnit
    instance.verticalGridUnit = original
    assert instance.verticalGridUnit == original



@given(instance=mm_pictograms_Diagram_strategy)
def test_mm_pictograms_diagram_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=mm_pictograms_Diagram_strategy)
def test_mm_pictograms_diagram_snapToGrid_setter(instance):
    original = instance.snapToGrid
    instance.snapToGrid = original
    assert instance.snapToGrid == original



@given(instance=mm_pictograms_Diagram_strategy)
def test_mm_pictograms_diagram_diagramTypeId_setter(instance):
    original = instance.diagramTypeId
    instance.diagramTypeId = original
    assert instance.diagramTypeId == original



@given(instance=mm_pictograms_Diagram_strategy)
def test_mm_pictograms_diagram_gridUnit_setter(instance):
    original = instance.gridUnit
    instance.gridUnit = original
    assert instance.gridUnit == original

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=mm_pictograms_ConnectionDecorator_strategy)
@settings(max_examples=50)
def test_mm_pictograms_connectiondecorator_instantiation(instance):
    assert isinstance(instance, mm_pictograms_ConnectionDecorator)



@given(instance=mm_pictograms_ConnectionDecorator_strategy)
def test_mm_pictograms_connectiondecorator_locationRelative_setter(instance):
    original = instance.locationRelative
    instance.locationRelative = original
    assert instance.locationRelative == original



@given(instance=mm_pictograms_ConnectionDecorator_strategy)
def test_mm_pictograms_connectiondecorator_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=mm_pictograms_ContainerShape_strategy)
@settings(max_examples=50)
def test_mm_pictograms_containershape_instantiation(instance):
    assert isinstance(instance, mm_pictograms_ContainerShape)

@given(instance=ContainerShape_strategy)
@settings(max_examples=50)
def test_containershape_instantiation(instance):
    assert isinstance(instance, ContainerShape)

@given(instance=AnchorContainer_strategy)
@settings(max_examples=50)
def test_anchorcontainer_instantiation(instance):
    assert isinstance(instance, AnchorContainer)

@given(instance=mm_pictograms_Connection_strategy)
@settings(max_examples=50)
def test_mm_pictograms_connection_instantiation(instance):
    assert isinstance(instance, mm_pictograms_Connection)

@given(instance=mm_pictograms_Shape_strategy)
@settings(max_examples=50)
def test_mm_pictograms_shape_instantiation(instance):
    assert isinstance(instance, mm_pictograms_Shape)

@given(instance=styles_Style_strategy)
@settings(max_examples=50)
def test_styles_style_instantiation(instance):
    assert isinstance(instance, styles_Style)

@given(instance=mm_StyleContainer_strategy)
@settings(max_examples=50)
def test_mm_stylecontainer_instantiation(instance):
    assert isinstance(instance, mm_StyleContainer)

@given(instance=PropertyContainer_strategy)
@settings(max_examples=50)
def test_propertycontainer_instantiation(instance):
    assert isinstance(instance, PropertyContainer)

@given(instance=mm_pictograms_PictogramLink_strategy)
@settings(max_examples=50)
def test_mm_pictograms_pictogramlink_instantiation(instance):
    assert isinstance(instance, mm_pictograms_PictogramLink)

@given(instance=mm_GraphicsAlgorithmContainer_strategy)
@settings(max_examples=50)
def test_mm_graphicsalgorithmcontainer_instantiation(instance):
    assert isinstance(instance, mm_GraphicsAlgorithmContainer)

@given(instance=GraphicsAlgorithm_strategy)
@settings(max_examples=50)
def test_graphicsalgorithm_instantiation(instance):
    assert isinstance(instance, GraphicsAlgorithm)

@given(instance=mm_algorithms_Image_strategy)
@settings(max_examples=50)
def test_mm_algorithms_image_instantiation(instance):
    assert isinstance(instance, mm_algorithms_Image)



@given(instance=mm_algorithms_Image_strategy)
def test_mm_algorithms_image_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=mm_algorithms_Image_strategy)
def test_mm_algorithms_image_stretchV_setter(instance):
    original = instance.stretchV
    instance.stretchV = original
    assert instance.stretchV == original



@given(instance=mm_algorithms_Image_strategy)
def test_mm_algorithms_image_stretchH_setter(instance):
    original = instance.stretchH
    instance.stretchH = original
    assert instance.stretchH == original



@given(instance=mm_algorithms_Image_strategy)
def test_mm_algorithms_image_proportional_setter(instance):
    original = instance.proportional
    instance.proportional = original
    assert instance.proportional == original

@given(instance=mm_algorithms_Ellipse_strategy)
@settings(max_examples=50)
def test_mm_algorithms_ellipse_instantiation(instance):
    assert isinstance(instance, mm_algorithms_Ellipse)

@given(instance=mm_algorithms_PlatformGraphicsAlgorithm_strategy)
@settings(max_examples=50)
def test_mm_algorithms_platformgraphicsalgorithm_instantiation(instance):
    assert isinstance(instance, mm_algorithms_PlatformGraphicsAlgorithm)



@given(instance=mm_algorithms_PlatformGraphicsAlgorithm_strategy)
def test_mm_algorithms_platformgraphicsalgorithm_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=mm_algorithms_Polyline_strategy)
@settings(max_examples=50)
def test_mm_algorithms_polyline_instantiation(instance):
    assert isinstance(instance, mm_algorithms_Polyline)

@given(instance=mm_algorithms_Rectangle_strategy)
@settings(max_examples=50)
def test_mm_algorithms_rectangle_instantiation(instance):
    assert isinstance(instance, mm_algorithms_Rectangle)

@given(instance=mm_algorithms_RoundedRectangle_strategy)
@settings(max_examples=50)
def test_mm_algorithms_roundedrectangle_instantiation(instance):
    assert isinstance(instance, mm_algorithms_RoundedRectangle)



@given(instance=mm_algorithms_RoundedRectangle_strategy)
def test_mm_algorithms_roundedrectangle_cornerWidth_setter(instance):
    original = instance.cornerWidth
    instance.cornerWidth = original
    assert instance.cornerWidth == original



@given(instance=mm_algorithms_RoundedRectangle_strategy)
def test_mm_algorithms_roundedrectangle_cornerHeight_setter(instance):
    original = instance.cornerHeight
    instance.cornerHeight = original
    assert instance.cornerHeight == original

@given(instance=mm_algorithms_AbstractText_strategy)
@settings(max_examples=50)
def test_mm_algorithms_abstracttext_instantiation(instance):
    assert isinstance(instance, mm_algorithms_AbstractText)



@given(instance=mm_algorithms_AbstractText_strategy)
def test_mm_algorithms_abstracttext_horizontalAlignment_setter(instance):
    original = instance.horizontalAlignment
    instance.horizontalAlignment = original
    assert instance.horizontalAlignment == original



@given(instance=mm_algorithms_AbstractText_strategy)
def test_mm_algorithms_abstracttext_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original



@given(instance=mm_algorithms_AbstractText_strategy)
def test_mm_algorithms_abstracttext_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=mm_algorithms_AbstractText_strategy)
def test_mm_algorithms_abstracttext_verticalAlignment_setter(instance):
    original = instance.verticalAlignment
    instance.verticalAlignment = original
    assert instance.verticalAlignment == original

@given(instance=GraphicsAlgorithmContainer_strategy)
@settings(max_examples=50)
def test_graphicsalgorithmcontainer_instantiation(instance):
    assert isinstance(instance, GraphicsAlgorithmContainer)

@given(instance=mm_algorithms_GraphicsAlgorithm_strategy)
@settings(max_examples=50)
def test_mm_algorithms_graphicsalgorithm_instantiation(instance):
    assert isinstance(instance, mm_algorithms_GraphicsAlgorithm)



@given(instance=mm_algorithms_GraphicsAlgorithm_strategy)
def test_mm_algorithms_graphicsalgorithm_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=mm_algorithms_GraphicsAlgorithm_strategy)
def test_mm_algorithms_graphicsalgorithm_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=mm_algorithms_GraphicsAlgorithm_strategy)
def test_mm_algorithms_graphicsalgorithm_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=mm_algorithms_GraphicsAlgorithm_strategy)
def test_mm_algorithms_graphicsalgorithm_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=mm_pictograms_PictogramElement_strategy)
@settings(max_examples=50)
def test_mm_pictograms_pictogramelement_instantiation(instance):
    assert isinstance(instance, mm_pictograms_PictogramElement)



@given(instance=mm_pictograms_PictogramElement_strategy)
def test_mm_pictograms_pictogramelement_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=mm_pictograms_PictogramElement_strategy)
def test_mm_pictograms_pictogramelement_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=PictogramLink_strategy)
@settings(max_examples=50)
def test_pictogramlink_instantiation(instance):
    assert isinstance(instance, PictogramLink)

@given(instance=styles_Font_strategy)
@settings(max_examples=50)
def test_styles_font_instantiation(instance):
    assert isinstance(instance, styles_Font)

@given(instance=styles_Color_strategy)
@settings(max_examples=50)
def test_styles_color_instantiation(instance):
    assert isinstance(instance, styles_Color)

@given(instance=mm_PropertyContainer_strategy)
@settings(max_examples=50)
def test_mm_propertycontainer_instantiation(instance):
    assert isinstance(instance, mm_PropertyContainer)

@given(instance=mm_Property_strategy)
@settings(max_examples=50)
def test_mm_property_instantiation(instance):
    assert isinstance(instance, mm_Property)



@given(instance=mm_Property_strategy)
def test_mm_property_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=mm_Property_strategy)
def test_mm_property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
