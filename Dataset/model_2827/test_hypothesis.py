import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mm::styles::TextStyle,
    mm::styles::PrecisionPoint,
    styles::TextStyle,
    mm::styles::TextStyleRegion,
    mm::styles::GradientColoredLocation,
    styles::RenderingStyle,
    mm::styles::Color,
    mm::styles::Point,
    mm::styles::Font,
    styles::GradientColoredAreas,
    mm::styles::AdaptedGradientColoredAreas,
    styles::GradientColoredArea,
    mm::styles::GradientColoredAreas,
    styles::GradientColoredLocation,
    mm::styles::GradientColoredArea,
    styles::TextStyleRegion,
    mm::styles::AbstractStyle,
    styles::mm::StyleContainer,
    styles::AdaptedGradientColoredAreas,
    mm::styles::RenderingStyle,
    styles::AbstractStyle,
    Polyline,
    mm::algorithms::Polygon,
    AbstractText,
    mm::algorithms::MultiText,
    mm::algorithms::Text,
    styles::Point,
    AdvancedAnchor,
    mm::pictograms::BoxRelativeAnchor,
    mm::pictograms::FixPointAnchor,
    CurvedConnection,
    styles::PrecisionPoint,
    pictograms::mm::EObject,
    PictogramLink,
    styles::Font,
    styles::Color,
    PictogramElement,
    mm::pictograms::AnchorContainer,
    mm::pictograms::Anchor,
    ConnectionDecorator,
    Diagram,
    Anchor,
    mm::pictograms::ChopboxAnchor,
    mm::pictograms::AdvancedAnchor,
    GraphicsAlgorithm,
    mm::algorithms::RoundedRectangle,
    mm::algorithms::Rectangle,
    mm::algorithms::Image,
    mm::algorithms::PlatformGraphicsAlgorithm,
    mm::algorithms::Ellipse,
    mm::algorithms::AbstractText,
    mm::algorithms::Polyline,
    GraphicsAlgorithmContainer,
    mm::algorithms::GraphicsAlgorithm,
    mm::pictograms::PictogramElement,
    Connection,
    mm::pictograms::FreeFormConnection,
    mm::pictograms::ManhattanConnection,
    mm::pictograms::CurvedConnection,
    mm::pictograms::CompositeConnection,
    StyleContainer,
    mm::styles::Style,
    pictograms::ContainerShape,
    mm::pictograms::Diagram,
    Shape,
    mm::pictograms::ConnectionDecorator,
    mm::pictograms::ContainerShape,
    ContainerShape,
    AnchorContainer,
    mm::pictograms::Connection,
    mm::pictograms::Shape,
    styles::Style,
    mm::StyleContainer,
    PropertyContainer,
    mm::pictograms::PictogramLink,
    mm::GraphicsAlgorithmContainer,
    mm::PropertyContainer,
    mm::Property,
    LineStyle,
    Orientation,
    LocationType,
    UnderlineStyle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mm::styles::textstyle_is_not_abstract():
    assert not inspect.isabstract(mm::styles::TextStyle)


def test_mm::styles::textstyle_constructor_exists():
    assert callable(mm::styles::TextStyle.__init__)


def test_mm::styles::textstyle_constructor_args():
    sig = inspect.signature(mm::styles::TextStyle.__init__)
    params = list(sig.parameters.keys())
    assert "underline" in params, "Missing parameter 'underline'"
    assert "underlineStyle" in params, "Missing parameter 'underlineStyle'"
    assert "strikeout" in params, "Missing parameter 'strikeout'"

def test_mm::styles::textstyle_has_underline():
    assert hasattr(mm::styles::TextStyle, "underline")
    descriptor = None
    for klass in mm::styles::TextStyle.__mro__:
        if "underline" in klass.__dict__:
            descriptor = klass.__dict__["underline"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::textstyle_has_underlineStyle():
    assert hasattr(mm::styles::TextStyle, "underlineStyle")
    descriptor = None
    for klass in mm::styles::TextStyle.__mro__:
        if "underlineStyle" in klass.__dict__:
            descriptor = klass.__dict__["underlineStyle"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::textstyle_has_strikeout():
    assert hasattr(mm::styles::TextStyle, "strikeout")
    descriptor = None
    for klass in mm::styles::TextStyle.__mro__:
        if "strikeout" in klass.__dict__:
            descriptor = klass.__dict__["strikeout"]
            break
    assert isinstance(descriptor, property)



def test_mm::styles::precisionpoint_is_not_abstract():
    assert not inspect.isabstract(mm::styles::PrecisionPoint)


def test_mm::styles::precisionpoint_constructor_exists():
    assert callable(mm::styles::PrecisionPoint.__init__)


def test_mm::styles::precisionpoint_constructor_args():
    sig = inspect.signature(mm::styles::PrecisionPoint.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_mm::styles::precisionpoint_has_x():
    assert hasattr(mm::styles::PrecisionPoint, "x")
    descriptor = None
    for klass in mm::styles::PrecisionPoint.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::precisionpoint_has_y():
    assert hasattr(mm::styles::PrecisionPoint, "y")
    descriptor = None
    for klass in mm::styles::PrecisionPoint.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_styles::textstyle_is_not_abstract():
    assert not inspect.isabstract(styles::TextStyle)


def test_styles::textstyle_constructor_exists():
    assert callable(styles::TextStyle.__init__)


def test_styles::textstyle_constructor_args():
    sig = inspect.signature(styles::TextStyle.__init__)
    params = list(sig.parameters.keys())



def test_mm::styles::textstyleregion_is_not_abstract():
    assert not inspect.isabstract(mm::styles::TextStyleRegion)


def test_mm::styles::textstyleregion_constructor_exists():
    assert callable(mm::styles::TextStyleRegion.__init__)


def test_mm::styles::textstyleregion_constructor_args():
    sig = inspect.signature(mm::styles::TextStyleRegion.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "end" in params, "Missing parameter 'end'"

def test_mm::styles::textstyleregion_has_start():
    assert hasattr(mm::styles::TextStyleRegion, "start")
    descriptor = None
    for klass in mm::styles::TextStyleRegion.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::textstyleregion_has_end():
    assert hasattr(mm::styles::TextStyleRegion, "end")
    descriptor = None
    for klass in mm::styles::TextStyleRegion.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_mm::styles::gradientcoloredlocation_is_not_abstract():
    assert not inspect.isabstract(mm::styles::GradientColoredLocation)


def test_mm::styles::gradientcoloredlocation_constructor_exists():
    assert callable(mm::styles::GradientColoredLocation.__init__)


def test_mm::styles::gradientcoloredlocation_constructor_args():
    sig = inspect.signature(mm::styles::GradientColoredLocation.__init__)
    params = list(sig.parameters.keys())
    assert "locationType" in params, "Missing parameter 'locationType'"
    assert "locationValue" in params, "Missing parameter 'locationValue'"

def test_mm::styles::gradientcoloredlocation_has_locationType():
    assert hasattr(mm::styles::GradientColoredLocation, "locationType")
    descriptor = None
    for klass in mm::styles::GradientColoredLocation.__mro__:
        if "locationType" in klass.__dict__:
            descriptor = klass.__dict__["locationType"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::gradientcoloredlocation_has_locationValue():
    assert hasattr(mm::styles::GradientColoredLocation, "locationValue")
    descriptor = None
    for klass in mm::styles::GradientColoredLocation.__mro__:
        if "locationValue" in klass.__dict__:
            descriptor = klass.__dict__["locationValue"]
            break
    assert isinstance(descriptor, property)



def test_styles::renderingstyle_is_not_abstract():
    assert not inspect.isabstract(styles::RenderingStyle)


def test_styles::renderingstyle_constructor_exists():
    assert callable(styles::RenderingStyle.__init__)


def test_styles::renderingstyle_constructor_args():
    sig = inspect.signature(styles::RenderingStyle.__init__)
    params = list(sig.parameters.keys())



def test_mm::styles::color_is_not_abstract():
    assert not inspect.isabstract(mm::styles::Color)


def test_mm::styles::color_constructor_exists():
    assert callable(mm::styles::Color.__init__)


def test_mm::styles::color_constructor_args():
    sig = inspect.signature(mm::styles::Color.__init__)
    params = list(sig.parameters.keys())
    assert "green" in params, "Missing parameter 'green'"
    assert "red" in params, "Missing parameter 'red'"
    assert "blue" in params, "Missing parameter 'blue'"

def test_mm::styles::color_has_green():
    assert hasattr(mm::styles::Color, "green")
    descriptor = None
    for klass in mm::styles::Color.__mro__:
        if "green" in klass.__dict__:
            descriptor = klass.__dict__["green"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::color_has_red():
    assert hasattr(mm::styles::Color, "red")
    descriptor = None
    for klass in mm::styles::Color.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::color_has_blue():
    assert hasattr(mm::styles::Color, "blue")
    descriptor = None
    for klass in mm::styles::Color.__mro__:
        if "blue" in klass.__dict__:
            descriptor = klass.__dict__["blue"]
            break
    assert isinstance(descriptor, property)



def test_mm::styles::point_is_not_abstract():
    assert not inspect.isabstract(mm::styles::Point)


def test_mm::styles::point_constructor_exists():
    assert callable(mm::styles::Point.__init__)


def test_mm::styles::point_constructor_args():
    sig = inspect.signature(mm::styles::Point.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "before" in params, "Missing parameter 'before'"
    assert "y" in params, "Missing parameter 'y'"
    assert "after" in params, "Missing parameter 'after'"

def test_mm::styles::point_has_x():
    assert hasattr(mm::styles::Point, "x")
    descriptor = None
    for klass in mm::styles::Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::point_has_before():
    assert hasattr(mm::styles::Point, "before")
    descriptor = None
    for klass in mm::styles::Point.__mro__:
        if "before" in klass.__dict__:
            descriptor = klass.__dict__["before"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::point_has_y():
    assert hasattr(mm::styles::Point, "y")
    descriptor = None
    for klass in mm::styles::Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::point_has_after():
    assert hasattr(mm::styles::Point, "after")
    descriptor = None
    for klass in mm::styles::Point.__mro__:
        if "after" in klass.__dict__:
            descriptor = klass.__dict__["after"]
            break
    assert isinstance(descriptor, property)



def test_mm::styles::font_is_not_abstract():
    assert not inspect.isabstract(mm::styles::Font)


def test_mm::styles::font_constructor_exists():
    assert callable(mm::styles::Font.__init__)


def test_mm::styles::font_constructor_args():
    sig = inspect.signature(mm::styles::Font.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "name" in params, "Missing parameter 'name'"
    assert "bold" in params, "Missing parameter 'bold'"
    assert "italic" in params, "Missing parameter 'italic'"

def test_mm::styles::font_has_size():
    assert hasattr(mm::styles::Font, "size")
    descriptor = None
    for klass in mm::styles::Font.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::font_has_name():
    assert hasattr(mm::styles::Font, "name")
    descriptor = None
    for klass in mm::styles::Font.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::font_has_bold():
    assert hasattr(mm::styles::Font, "bold")
    descriptor = None
    for klass in mm::styles::Font.__mro__:
        if "bold" in klass.__dict__:
            descriptor = klass.__dict__["bold"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::font_has_italic():
    assert hasattr(mm::styles::Font, "italic")
    descriptor = None
    for klass in mm::styles::Font.__mro__:
        if "italic" in klass.__dict__:
            descriptor = klass.__dict__["italic"]
            break
    assert isinstance(descriptor, property)



def test_styles::gradientcoloredareas_is_not_abstract():
    assert not inspect.isabstract(styles::GradientColoredAreas)


def test_styles::gradientcoloredareas_constructor_exists():
    assert callable(styles::GradientColoredAreas.__init__)


def test_styles::gradientcoloredareas_constructor_args():
    sig = inspect.signature(styles::GradientColoredAreas.__init__)
    params = list(sig.parameters.keys())



def test_mm::styles::adaptedgradientcoloredareas_is_not_abstract():
    assert not inspect.isabstract(mm::styles::AdaptedGradientColoredAreas)


def test_mm::styles::adaptedgradientcoloredareas_constructor_exists():
    assert callable(mm::styles::AdaptedGradientColoredAreas.__init__)


def test_mm::styles::adaptedgradientcoloredareas_constructor_args():
    sig = inspect.signature(mm::styles::AdaptedGradientColoredAreas.__init__)
    params = list(sig.parameters.keys())
    assert "gradientType" in params, "Missing parameter 'gradientType'"
    assert "definedStyleId" in params, "Missing parameter 'definedStyleId'"

def test_mm::styles::adaptedgradientcoloredareas_has_gradientType():
    assert hasattr(mm::styles::AdaptedGradientColoredAreas, "gradientType")
    descriptor = None
    for klass in mm::styles::AdaptedGradientColoredAreas.__mro__:
        if "gradientType" in klass.__dict__:
            descriptor = klass.__dict__["gradientType"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::adaptedgradientcoloredareas_has_definedStyleId():
    assert hasattr(mm::styles::AdaptedGradientColoredAreas, "definedStyleId")
    descriptor = None
    for klass in mm::styles::AdaptedGradientColoredAreas.__mro__:
        if "definedStyleId" in klass.__dict__:
            descriptor = klass.__dict__["definedStyleId"]
            break
    assert isinstance(descriptor, property)



def test_styles::gradientcoloredarea_is_not_abstract():
    assert not inspect.isabstract(styles::GradientColoredArea)


def test_styles::gradientcoloredarea_constructor_exists():
    assert callable(styles::GradientColoredArea.__init__)


def test_styles::gradientcoloredarea_constructor_args():
    sig = inspect.signature(styles::GradientColoredArea.__init__)
    params = list(sig.parameters.keys())



def test_mm::styles::gradientcoloredareas_is_not_abstract():
    assert not inspect.isabstract(mm::styles::GradientColoredAreas)


def test_mm::styles::gradientcoloredareas_constructor_exists():
    assert callable(mm::styles::GradientColoredAreas.__init__)


def test_mm::styles::gradientcoloredareas_constructor_args():
    sig = inspect.signature(mm::styles::GradientColoredAreas.__init__)
    params = list(sig.parameters.keys())
    assert "styleAdaption" in params, "Missing parameter 'styleAdaption'"

def test_mm::styles::gradientcoloredareas_has_styleAdaption():
    assert hasattr(mm::styles::GradientColoredAreas, "styleAdaption")
    descriptor = None
    for klass in mm::styles::GradientColoredAreas.__mro__:
        if "styleAdaption" in klass.__dict__:
            descriptor = klass.__dict__["styleAdaption"]
            break
    assert isinstance(descriptor, property)



def test_styles::gradientcoloredlocation_is_not_abstract():
    assert not inspect.isabstract(styles::GradientColoredLocation)


def test_styles::gradientcoloredlocation_constructor_exists():
    assert callable(styles::GradientColoredLocation.__init__)


def test_styles::gradientcoloredlocation_constructor_args():
    sig = inspect.signature(styles::GradientColoredLocation.__init__)
    params = list(sig.parameters.keys())



def test_mm::styles::gradientcoloredarea_is_not_abstract():
    assert not inspect.isabstract(mm::styles::GradientColoredArea)


def test_mm::styles::gradientcoloredarea_constructor_exists():
    assert callable(mm::styles::GradientColoredArea.__init__)


def test_mm::styles::gradientcoloredarea_constructor_args():
    sig = inspect.signature(mm::styles::GradientColoredArea.__init__)
    params = list(sig.parameters.keys())



def test_styles::textstyleregion_is_not_abstract():
    assert not inspect.isabstract(styles::TextStyleRegion)


def test_styles::textstyleregion_constructor_exists():
    assert callable(styles::TextStyleRegion.__init__)


def test_styles::textstyleregion_constructor_args():
    sig = inspect.signature(styles::TextStyleRegion.__init__)
    params = list(sig.parameters.keys())



def test_mm::styles::abstractstyle_is_not_abstract():
    assert not inspect.isabstract(mm::styles::AbstractStyle)


def test_mm::styles::abstractstyle_constructor_exists():
    assert callable(mm::styles::AbstractStyle.__init__)


def test_mm::styles::abstractstyle_constructor_args():
    sig = inspect.signature(mm::styles::AbstractStyle.__init__)
    params = list(sig.parameters.keys())
    assert "filled" in params, "Missing parameter 'filled'"
    assert "lineVisible" in params, "Missing parameter 'lineVisible'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "transparency" in params, "Missing parameter 'transparency'"
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"

def test_mm::styles::abstractstyle_has_filled():
    assert hasattr(mm::styles::AbstractStyle, "filled")
    descriptor = None
    for klass in mm::styles::AbstractStyle.__mro__:
        if "filled" in klass.__dict__:
            descriptor = klass.__dict__["filled"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::abstractstyle_has_lineVisible():
    assert hasattr(mm::styles::AbstractStyle, "lineVisible")
    descriptor = None
    for klass in mm::styles::AbstractStyle.__mro__:
        if "lineVisible" in klass.__dict__:
            descriptor = klass.__dict__["lineVisible"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::abstractstyle_has_lineStyle():
    assert hasattr(mm::styles::AbstractStyle, "lineStyle")
    descriptor = None
    for klass in mm::styles::AbstractStyle.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::abstractstyle_has_transparency():
    assert hasattr(mm::styles::AbstractStyle, "transparency")
    descriptor = None
    for klass in mm::styles::AbstractStyle.__mro__:
        if "transparency" in klass.__dict__:
            descriptor = klass.__dict__["transparency"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::abstractstyle_has_lineWidth():
    assert hasattr(mm::styles::AbstractStyle, "lineWidth")
    descriptor = None
    for klass in mm::styles::AbstractStyle.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)



def test_styles::mm::stylecontainer_is_not_abstract():
    assert not inspect.isabstract(styles::mm::StyleContainer)


def test_styles::mm::stylecontainer_constructor_exists():
    assert callable(styles::mm::StyleContainer.__init__)


def test_styles::mm::stylecontainer_constructor_args():
    sig = inspect.signature(styles::mm::StyleContainer.__init__)
    params = list(sig.parameters.keys())



def test_styles::adaptedgradientcoloredareas_is_not_abstract():
    assert not inspect.isabstract(styles::AdaptedGradientColoredAreas)


def test_styles::adaptedgradientcoloredareas_constructor_exists():
    assert callable(styles::AdaptedGradientColoredAreas.__init__)


def test_styles::adaptedgradientcoloredareas_constructor_args():
    sig = inspect.signature(styles::AdaptedGradientColoredAreas.__init__)
    params = list(sig.parameters.keys())



def test_mm::styles::renderingstyle_is_not_abstract():
    assert not inspect.isabstract(mm::styles::RenderingStyle)


def test_mm::styles::renderingstyle_constructor_exists():
    assert callable(mm::styles::RenderingStyle.__init__)


def test_mm::styles::renderingstyle_constructor_args():
    sig = inspect.signature(mm::styles::RenderingStyle.__init__)
    params = list(sig.parameters.keys())



def test_styles::abstractstyle_is_not_abstract():
    assert not inspect.isabstract(styles::AbstractStyle)


def test_styles::abstractstyle_constructor_exists():
    assert callable(styles::AbstractStyle.__init__)


def test_styles::abstractstyle_constructor_args():
    sig = inspect.signature(styles::AbstractStyle.__init__)
    params = list(sig.parameters.keys())



def test_polyline_is_not_abstract():
    assert not inspect.isabstract(Polyline)


def test_polyline_constructor_exists():
    assert callable(Polyline.__init__)


def test_polyline_constructor_args():
    sig = inspect.signature(Polyline.__init__)
    params = list(sig.parameters.keys())



def test_mm::algorithms::polygon_is_not_abstract():
    assert not inspect.isabstract(mm::algorithms::Polygon)


def test_mm::algorithms::polygon_constructor_exists():
    assert callable(mm::algorithms::Polygon.__init__)


def test_mm::algorithms::polygon_constructor_args():
    sig = inspect.signature(mm::algorithms::Polygon.__init__)
    params = list(sig.parameters.keys())



def test_abstracttext_is_not_abstract():
    assert not inspect.isabstract(AbstractText)


def test_abstracttext_constructor_exists():
    assert callable(AbstractText.__init__)


def test_abstracttext_constructor_args():
    sig = inspect.signature(AbstractText.__init__)
    params = list(sig.parameters.keys())



def test_mm::algorithms::multitext_is_not_abstract():
    assert not inspect.isabstract(mm::algorithms::MultiText)


def test_mm::algorithms::multitext_constructor_exists():
    assert callable(mm::algorithms::MultiText.__init__)


def test_mm::algorithms::multitext_constructor_args():
    sig = inspect.signature(mm::algorithms::MultiText.__init__)
    params = list(sig.parameters.keys())



def test_mm::algorithms::text_is_not_abstract():
    assert not inspect.isabstract(mm::algorithms::Text)


def test_mm::algorithms::text_constructor_exists():
    assert callable(mm::algorithms::Text.__init__)


def test_mm::algorithms::text_constructor_args():
    sig = inspect.signature(mm::algorithms::Text.__init__)
    params = list(sig.parameters.keys())



def test_styles::point_is_not_abstract():
    assert not inspect.isabstract(styles::Point)


def test_styles::point_constructor_exists():
    assert callable(styles::Point.__init__)


def test_styles::point_constructor_args():
    sig = inspect.signature(styles::Point.__init__)
    params = list(sig.parameters.keys())



def test_advancedanchor_is_not_abstract():
    assert not inspect.isabstract(AdvancedAnchor)


def test_advancedanchor_constructor_exists():
    assert callable(AdvancedAnchor.__init__)


def test_advancedanchor_constructor_args():
    sig = inspect.signature(AdvancedAnchor.__init__)
    params = list(sig.parameters.keys())



def test_mm::pictograms::boxrelativeanchor_is_not_abstract():
    assert not inspect.isabstract(mm::pictograms::BoxRelativeAnchor)


def test_mm::pictograms::boxrelativeanchor_constructor_exists():
    assert callable(mm::pictograms::BoxRelativeAnchor.__init__)


def test_mm::pictograms::boxrelativeanchor_constructor_args():
    sig = inspect.signature(mm::pictograms::BoxRelativeAnchor.__init__)
    params = list(sig.parameters.keys())
    assert "relativeHeight" in params, "Missing parameter 'relativeHeight'"
    assert "relativeWidth" in params, "Missing parameter 'relativeWidth'"

def test_mm::pictograms::boxrelativeanchor_has_relativeHeight():
    assert hasattr(mm::pictograms::BoxRelativeAnchor, "relativeHeight")
    descriptor = None
    for klass in mm::pictograms::BoxRelativeAnchor.__mro__:
        if "relativeHeight" in klass.__dict__:
            descriptor = klass.__dict__["relativeHeight"]
            break
    assert isinstance(descriptor, property)

def test_mm::pictograms::boxrelativeanchor_has_relativeWidth():
    assert hasattr(mm::pictograms::BoxRelativeAnchor, "relativeWidth")
    descriptor = None
    for klass in mm::pictograms::BoxRelativeAnchor.__mro__:
        if "relativeWidth" in klass.__dict__:
            descriptor = klass.__dict__["relativeWidth"]
            break
    assert isinstance(descriptor, property)



def test_mm::pictograms::fixpointanchor_is_not_abstract():
    assert not inspect.isabstract(mm::pictograms::FixPointAnchor)


def test_mm::pictograms::fixpointanchor_constructor_exists():
    assert callable(mm::pictograms::FixPointAnchor.__init__)


def test_mm::pictograms::fixpointanchor_constructor_args():
    sig = inspect.signature(mm::pictograms::FixPointAnchor.__init__)
    params = list(sig.parameters.keys())



def test_curvedconnection_is_not_abstract():
    assert not inspect.isabstract(CurvedConnection)


def test_curvedconnection_constructor_exists():
    assert callable(CurvedConnection.__init__)


def test_curvedconnection_constructor_args():
    sig = inspect.signature(CurvedConnection.__init__)
    params = list(sig.parameters.keys())



def test_styles::precisionpoint_is_not_abstract():
    assert not inspect.isabstract(styles::PrecisionPoint)


def test_styles::precisionpoint_constructor_exists():
    assert callable(styles::PrecisionPoint.__init__)


def test_styles::precisionpoint_constructor_args():
    sig = inspect.signature(styles::PrecisionPoint.__init__)
    params = list(sig.parameters.keys())



def test_pictograms::mm::eobject_is_not_abstract():
    assert not inspect.isabstract(pictograms::mm::EObject)


def test_pictograms::mm::eobject_constructor_exists():
    assert callable(pictograms::mm::EObject.__init__)


def test_pictograms::mm::eobject_constructor_args():
    sig = inspect.signature(pictograms::mm::EObject.__init__)
    params = list(sig.parameters.keys())



def test_pictogramlink_is_not_abstract():
    assert not inspect.isabstract(PictogramLink)


def test_pictogramlink_constructor_exists():
    assert callable(PictogramLink.__init__)


def test_pictogramlink_constructor_args():
    sig = inspect.signature(PictogramLink.__init__)
    params = list(sig.parameters.keys())



def test_styles::font_is_not_abstract():
    assert not inspect.isabstract(styles::Font)


def test_styles::font_constructor_exists():
    assert callable(styles::Font.__init__)


def test_styles::font_constructor_args():
    sig = inspect.signature(styles::Font.__init__)
    params = list(sig.parameters.keys())



def test_styles::color_is_not_abstract():
    assert not inspect.isabstract(styles::Color)


def test_styles::color_constructor_exists():
    assert callable(styles::Color.__init__)


def test_styles::color_constructor_args():
    sig = inspect.signature(styles::Color.__init__)
    params = list(sig.parameters.keys())



def test_pictogramelement_is_not_abstract():
    assert not inspect.isabstract(PictogramElement)


def test_pictogramelement_constructor_exists():
    assert callable(PictogramElement.__init__)


def test_pictogramelement_constructor_args():
    sig = inspect.signature(PictogramElement.__init__)
    params = list(sig.parameters.keys())



def test_mm::pictograms::anchorcontainer_is_not_abstract():
    assert not inspect.isabstract(mm::pictograms::AnchorContainer)


def test_mm::pictograms::anchorcontainer_constructor_exists():
    assert callable(mm::pictograms::AnchorContainer.__init__)


def test_mm::pictograms::anchorcontainer_constructor_args():
    sig = inspect.signature(mm::pictograms::AnchorContainer.__init__)
    params = list(sig.parameters.keys())



def test_mm::pictograms::anchor_is_not_abstract():
    assert not inspect.isabstract(mm::pictograms::Anchor)


def test_mm::pictograms::anchor_constructor_exists():
    assert callable(mm::pictograms::Anchor.__init__)


def test_mm::pictograms::anchor_constructor_args():
    sig = inspect.signature(mm::pictograms::Anchor.__init__)
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



def test_mm::pictograms::chopboxanchor_is_not_abstract():
    assert not inspect.isabstract(mm::pictograms::ChopboxAnchor)


def test_mm::pictograms::chopboxanchor_constructor_exists():
    assert callable(mm::pictograms::ChopboxAnchor.__init__)


def test_mm::pictograms::chopboxanchor_constructor_args():
    sig = inspect.signature(mm::pictograms::ChopboxAnchor.__init__)
    params = list(sig.parameters.keys())



def test_mm::pictograms::advancedanchor_is_not_abstract():
    assert not inspect.isabstract(mm::pictograms::AdvancedAnchor)


def test_mm::pictograms::advancedanchor_constructor_exists():
    assert callable(mm::pictograms::AdvancedAnchor.__init__)


def test_mm::pictograms::advancedanchor_constructor_args():
    sig = inspect.signature(mm::pictograms::AdvancedAnchor.__init__)
    params = list(sig.parameters.keys())
    assert "useAnchorLocationAsConnectionEndpoint" in params, "Missing parameter 'useAnchorLocationAsConnectionEndpoint'"

def test_mm::pictograms::advancedanchor_has_useAnchorLocationAsConnectionEndpoint():
    assert hasattr(mm::pictograms::AdvancedAnchor, "useAnchorLocationAsConnectionEndpoint")
    descriptor = None
    for klass in mm::pictograms::AdvancedAnchor.__mro__:
        if "useAnchorLocationAsConnectionEndpoint" in klass.__dict__:
            descriptor = klass.__dict__["useAnchorLocationAsConnectionEndpoint"]
            break
    assert isinstance(descriptor, property)



def test_graphicsalgorithm_is_not_abstract():
    assert not inspect.isabstract(GraphicsAlgorithm)


def test_graphicsalgorithm_constructor_exists():
    assert callable(GraphicsAlgorithm.__init__)


def test_graphicsalgorithm_constructor_args():
    sig = inspect.signature(GraphicsAlgorithm.__init__)
    params = list(sig.parameters.keys())



def test_mm::algorithms::roundedrectangle_is_not_abstract():
    assert not inspect.isabstract(mm::algorithms::RoundedRectangle)


def test_mm::algorithms::roundedrectangle_constructor_exists():
    assert callable(mm::algorithms::RoundedRectangle.__init__)


def test_mm::algorithms::roundedrectangle_constructor_args():
    sig = inspect.signature(mm::algorithms::RoundedRectangle.__init__)
    params = list(sig.parameters.keys())
    assert "cornerHeight" in params, "Missing parameter 'cornerHeight'"
    assert "cornerWidth" in params, "Missing parameter 'cornerWidth'"

def test_mm::algorithms::roundedrectangle_has_cornerHeight():
    assert hasattr(mm::algorithms::RoundedRectangle, "cornerHeight")
    descriptor = None
    for klass in mm::algorithms::RoundedRectangle.__mro__:
        if "cornerHeight" in klass.__dict__:
            descriptor = klass.__dict__["cornerHeight"]
            break
    assert isinstance(descriptor, property)

def test_mm::algorithms::roundedrectangle_has_cornerWidth():
    assert hasattr(mm::algorithms::RoundedRectangle, "cornerWidth")
    descriptor = None
    for klass in mm::algorithms::RoundedRectangle.__mro__:
        if "cornerWidth" in klass.__dict__:
            descriptor = klass.__dict__["cornerWidth"]
            break
    assert isinstance(descriptor, property)



def test_mm::algorithms::rectangle_is_not_abstract():
    assert not inspect.isabstract(mm::algorithms::Rectangle)


def test_mm::algorithms::rectangle_constructor_exists():
    assert callable(mm::algorithms::Rectangle.__init__)


def test_mm::algorithms::rectangle_constructor_args():
    sig = inspect.signature(mm::algorithms::Rectangle.__init__)
    params = list(sig.parameters.keys())



def test_mm::algorithms::image_is_not_abstract():
    assert not inspect.isabstract(mm::algorithms::Image)


def test_mm::algorithms::image_constructor_exists():
    assert callable(mm::algorithms::Image.__init__)


def test_mm::algorithms::image_constructor_args():
    sig = inspect.signature(mm::algorithms::Image.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "proportional" in params, "Missing parameter 'proportional'"
    assert "stretchV" in params, "Missing parameter 'stretchV'"
    assert "stretchH" in params, "Missing parameter 'stretchH'"

def test_mm::algorithms::image_has_id():
    assert hasattr(mm::algorithms::Image, "id")
    descriptor = None
    for klass in mm::algorithms::Image.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mm::algorithms::image_has_proportional():
    assert hasattr(mm::algorithms::Image, "proportional")
    descriptor = None
    for klass in mm::algorithms::Image.__mro__:
        if "proportional" in klass.__dict__:
            descriptor = klass.__dict__["proportional"]
            break
    assert isinstance(descriptor, property)

def test_mm::algorithms::image_has_stretchV():
    assert hasattr(mm::algorithms::Image, "stretchV")
    descriptor = None
    for klass in mm::algorithms::Image.__mro__:
        if "stretchV" in klass.__dict__:
            descriptor = klass.__dict__["stretchV"]
            break
    assert isinstance(descriptor, property)

def test_mm::algorithms::image_has_stretchH():
    assert hasattr(mm::algorithms::Image, "stretchH")
    descriptor = None
    for klass in mm::algorithms::Image.__mro__:
        if "stretchH" in klass.__dict__:
            descriptor = klass.__dict__["stretchH"]
            break
    assert isinstance(descriptor, property)



def test_mm::algorithms::platformgraphicsalgorithm_is_not_abstract():
    assert not inspect.isabstract(mm::algorithms::PlatformGraphicsAlgorithm)


def test_mm::algorithms::platformgraphicsalgorithm_constructor_exists():
    assert callable(mm::algorithms::PlatformGraphicsAlgorithm.__init__)


def test_mm::algorithms::platformgraphicsalgorithm_constructor_args():
    sig = inspect.signature(mm::algorithms::PlatformGraphicsAlgorithm.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mm::algorithms::platformgraphicsalgorithm_has_id():
    assert hasattr(mm::algorithms::PlatformGraphicsAlgorithm, "id")
    descriptor = None
    for klass in mm::algorithms::PlatformGraphicsAlgorithm.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mm::algorithms::ellipse_is_not_abstract():
    assert not inspect.isabstract(mm::algorithms::Ellipse)


def test_mm::algorithms::ellipse_constructor_exists():
    assert callable(mm::algorithms::Ellipse.__init__)


def test_mm::algorithms::ellipse_constructor_args():
    sig = inspect.signature(mm::algorithms::Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_mm::algorithms::abstracttext_is_not_abstract():
    assert not inspect.isabstract(mm::algorithms::AbstractText)


def test_mm::algorithms::abstracttext_constructor_exists():
    assert callable(mm::algorithms::AbstractText.__init__)


def test_mm::algorithms::abstracttext_constructor_args():
    sig = inspect.signature(mm::algorithms::AbstractText.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"
    assert "horizontalAlignment" in params, "Missing parameter 'horizontalAlignment'"
    assert "value" in params, "Missing parameter 'value'"
    assert "verticalAlignment" in params, "Missing parameter 'verticalAlignment'"

def test_mm::algorithms::abstracttext_has_angle():
    assert hasattr(mm::algorithms::AbstractText, "angle")
    descriptor = None
    for klass in mm::algorithms::AbstractText.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)

def test_mm::algorithms::abstracttext_has_horizontalAlignment():
    assert hasattr(mm::algorithms::AbstractText, "horizontalAlignment")
    descriptor = None
    for klass in mm::algorithms::AbstractText.__mro__:
        if "horizontalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["horizontalAlignment"]
            break
    assert isinstance(descriptor, property)

def test_mm::algorithms::abstracttext_has_value():
    assert hasattr(mm::algorithms::AbstractText, "value")
    descriptor = None
    for klass in mm::algorithms::AbstractText.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_mm::algorithms::abstracttext_has_verticalAlignment():
    assert hasattr(mm::algorithms::AbstractText, "verticalAlignment")
    descriptor = None
    for klass in mm::algorithms::AbstractText.__mro__:
        if "verticalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["verticalAlignment"]
            break
    assert isinstance(descriptor, property)



def test_mm::algorithms::polyline_is_not_abstract():
    assert not inspect.isabstract(mm::algorithms::Polyline)


def test_mm::algorithms::polyline_constructor_exists():
    assert callable(mm::algorithms::Polyline.__init__)


def test_mm::algorithms::polyline_constructor_args():
    sig = inspect.signature(mm::algorithms::Polyline.__init__)
    params = list(sig.parameters.keys())



def test_graphicsalgorithmcontainer_is_not_abstract():
    assert not inspect.isabstract(GraphicsAlgorithmContainer)


def test_graphicsalgorithmcontainer_constructor_exists():
    assert callable(GraphicsAlgorithmContainer.__init__)


def test_graphicsalgorithmcontainer_constructor_args():
    sig = inspect.signature(GraphicsAlgorithmContainer.__init__)
    params = list(sig.parameters.keys())



def test_mm::algorithms::graphicsalgorithm_is_not_abstract():
    assert not inspect.isabstract(mm::algorithms::GraphicsAlgorithm)


def test_mm::algorithms::graphicsalgorithm_constructor_exists():
    assert callable(mm::algorithms::GraphicsAlgorithm.__init__)


def test_mm::algorithms::graphicsalgorithm_constructor_args():
    sig = inspect.signature(mm::algorithms::GraphicsAlgorithm.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_mm::algorithms::graphicsalgorithm_has_height():
    assert hasattr(mm::algorithms::GraphicsAlgorithm, "height")
    descriptor = None
    for klass in mm::algorithms::GraphicsAlgorithm.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_mm::algorithms::graphicsalgorithm_has_width():
    assert hasattr(mm::algorithms::GraphicsAlgorithm, "width")
    descriptor = None
    for klass in mm::algorithms::GraphicsAlgorithm.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_mm::algorithms::graphicsalgorithm_has_x():
    assert hasattr(mm::algorithms::GraphicsAlgorithm, "x")
    descriptor = None
    for klass in mm::algorithms::GraphicsAlgorithm.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_mm::algorithms::graphicsalgorithm_has_y():
    assert hasattr(mm::algorithms::GraphicsAlgorithm, "y")
    descriptor = None
    for klass in mm::algorithms::GraphicsAlgorithm.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_mm::pictograms::pictogramelement_is_not_abstract():
    assert not inspect.isabstract(mm::pictograms::PictogramElement)


def test_mm::pictograms::pictogramelement_constructor_exists():
    assert callable(mm::pictograms::PictogramElement.__init__)


def test_mm::pictograms::pictogramelement_constructor_args():
    sig = inspect.signature(mm::pictograms::PictogramElement.__init__)
    params = list(sig.parameters.keys())
    assert "visible" in params, "Missing parameter 'visible'"
    assert "active" in params, "Missing parameter 'active'"

def test_mm::pictograms::pictogramelement_has_visible():
    assert hasattr(mm::pictograms::PictogramElement, "visible")
    descriptor = None
    for klass in mm::pictograms::PictogramElement.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_mm::pictograms::pictogramelement_has_active():
    assert hasattr(mm::pictograms::PictogramElement, "active")
    descriptor = None
    for klass in mm::pictograms::PictogramElement.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)



def test_connection_is_not_abstract():
    assert not inspect.isabstract(Connection)


def test_connection_constructor_exists():
    assert callable(Connection.__init__)


def test_connection_constructor_args():
    sig = inspect.signature(Connection.__init__)
    params = list(sig.parameters.keys())



def test_mm::pictograms::freeformconnection_is_not_abstract():
    assert not inspect.isabstract(mm::pictograms::FreeFormConnection)


def test_mm::pictograms::freeformconnection_constructor_exists():
    assert callable(mm::pictograms::FreeFormConnection.__init__)


def test_mm::pictograms::freeformconnection_constructor_args():
    sig = inspect.signature(mm::pictograms::FreeFormConnection.__init__)
    params = list(sig.parameters.keys())



def test_mm::pictograms::manhattanconnection_is_not_abstract():
    assert not inspect.isabstract(mm::pictograms::ManhattanConnection)


def test_mm::pictograms::manhattanconnection_constructor_exists():
    assert callable(mm::pictograms::ManhattanConnection.__init__)


def test_mm::pictograms::manhattanconnection_constructor_args():
    sig = inspect.signature(mm::pictograms::ManhattanConnection.__init__)
    params = list(sig.parameters.keys())



def test_mm::pictograms::curvedconnection_is_not_abstract():
    assert not inspect.isabstract(mm::pictograms::CurvedConnection)


def test_mm::pictograms::curvedconnection_constructor_exists():
    assert callable(mm::pictograms::CurvedConnection.__init__)


def test_mm::pictograms::curvedconnection_constructor_args():
    sig = inspect.signature(mm::pictograms::CurvedConnection.__init__)
    params = list(sig.parameters.keys())



def test_mm::pictograms::compositeconnection_is_not_abstract():
    assert not inspect.isabstract(mm::pictograms::CompositeConnection)


def test_mm::pictograms::compositeconnection_constructor_exists():
    assert callable(mm::pictograms::CompositeConnection.__init__)


def test_mm::pictograms::compositeconnection_constructor_args():
    sig = inspect.signature(mm::pictograms::CompositeConnection.__init__)
    params = list(sig.parameters.keys())



def test_stylecontainer_is_not_abstract():
    assert not inspect.isabstract(StyleContainer)


def test_stylecontainer_constructor_exists():
    assert callable(StyleContainer.__init__)


def test_stylecontainer_constructor_args():
    sig = inspect.signature(StyleContainer.__init__)
    params = list(sig.parameters.keys())



def test_mm::styles::style_is_not_abstract():
    assert not inspect.isabstract(mm::styles::Style)


def test_mm::styles::style_constructor_exists():
    assert callable(mm::styles::Style.__init__)


def test_mm::styles::style_constructor_args():
    sig = inspect.signature(mm::styles::Style.__init__)
    params = list(sig.parameters.keys())
    assert "horizontalAlignment" in params, "Missing parameter 'horizontalAlignment'"
    assert "verticalAlignment" in params, "Missing parameter 'verticalAlignment'"
    assert "stretchH" in params, "Missing parameter 'stretchH'"
    assert "proportional" in params, "Missing parameter 'proportional'"
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"
    assert "angle" in params, "Missing parameter 'angle'"
    assert "stretchV" in params, "Missing parameter 'stretchV'"

def test_mm::styles::style_has_horizontalAlignment():
    assert hasattr(mm::styles::Style, "horizontalAlignment")
    descriptor = None
    for klass in mm::styles::Style.__mro__:
        if "horizontalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["horizontalAlignment"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::style_has_verticalAlignment():
    assert hasattr(mm::styles::Style, "verticalAlignment")
    descriptor = None
    for klass in mm::styles::Style.__mro__:
        if "verticalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["verticalAlignment"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::style_has_stretchH():
    assert hasattr(mm::styles::Style, "stretchH")
    descriptor = None
    for klass in mm::styles::Style.__mro__:
        if "stretchH" in klass.__dict__:
            descriptor = klass.__dict__["stretchH"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::style_has_proportional():
    assert hasattr(mm::styles::Style, "proportional")
    descriptor = None
    for klass in mm::styles::Style.__mro__:
        if "proportional" in klass.__dict__:
            descriptor = klass.__dict__["proportional"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::style_has_description():
    assert hasattr(mm::styles::Style, "description")
    descriptor = None
    for klass in mm::styles::Style.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::style_has_id():
    assert hasattr(mm::styles::Style, "id")
    descriptor = None
    for klass in mm::styles::Style.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::style_has_angle():
    assert hasattr(mm::styles::Style, "angle")
    descriptor = None
    for klass in mm::styles::Style.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)

def test_mm::styles::style_has_stretchV():
    assert hasattr(mm::styles::Style, "stretchV")
    descriptor = None
    for klass in mm::styles::Style.__mro__:
        if "stretchV" in klass.__dict__:
            descriptor = klass.__dict__["stretchV"]
            break
    assert isinstance(descriptor, property)



def test_pictograms::containershape_is_not_abstract():
    assert not inspect.isabstract(pictograms::ContainerShape)


def test_pictograms::containershape_constructor_exists():
    assert callable(pictograms::ContainerShape.__init__)


def test_pictograms::containershape_constructor_args():
    sig = inspect.signature(pictograms::ContainerShape.__init__)
    params = list(sig.parameters.keys())



def test_mm::pictograms::diagram_is_not_abstract():
    assert not inspect.isabstract(mm::pictograms::Diagram)


def test_mm::pictograms::diagram_constructor_exists():
    assert callable(mm::pictograms::Diagram.__init__)


def test_mm::pictograms::diagram_constructor_args():
    sig = inspect.signature(mm::pictograms::Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "diagramTypeId" in params, "Missing parameter 'diagramTypeId'"
    assert "showGuides" in params, "Missing parameter 'showGuides'"
    assert "verticalGridUnit" in params, "Missing parameter 'verticalGridUnit'"
    assert "name" in params, "Missing parameter 'name'"
    assert "snapToGrid" in params, "Missing parameter 'snapToGrid'"
    assert "gridUnit" in params, "Missing parameter 'gridUnit'"

def test_mm::pictograms::diagram_has_version():
    assert hasattr(mm::pictograms::Diagram, "version")
    descriptor = None
    for klass in mm::pictograms::Diagram.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_mm::pictograms::diagram_has_diagramTypeId():
    assert hasattr(mm::pictograms::Diagram, "diagramTypeId")
    descriptor = None
    for klass in mm::pictograms::Diagram.__mro__:
        if "diagramTypeId" in klass.__dict__:
            descriptor = klass.__dict__["diagramTypeId"]
            break
    assert isinstance(descriptor, property)

def test_mm::pictograms::diagram_has_showGuides():
    assert hasattr(mm::pictograms::Diagram, "showGuides")
    descriptor = None
    for klass in mm::pictograms::Diagram.__mro__:
        if "showGuides" in klass.__dict__:
            descriptor = klass.__dict__["showGuides"]
            break
    assert isinstance(descriptor, property)

def test_mm::pictograms::diagram_has_verticalGridUnit():
    assert hasattr(mm::pictograms::Diagram, "verticalGridUnit")
    descriptor = None
    for klass in mm::pictograms::Diagram.__mro__:
        if "verticalGridUnit" in klass.__dict__:
            descriptor = klass.__dict__["verticalGridUnit"]
            break
    assert isinstance(descriptor, property)

def test_mm::pictograms::diagram_has_name():
    assert hasattr(mm::pictograms::Diagram, "name")
    descriptor = None
    for klass in mm::pictograms::Diagram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm::pictograms::diagram_has_snapToGrid():
    assert hasattr(mm::pictograms::Diagram, "snapToGrid")
    descriptor = None
    for klass in mm::pictograms::Diagram.__mro__:
        if "snapToGrid" in klass.__dict__:
            descriptor = klass.__dict__["snapToGrid"]
            break
    assert isinstance(descriptor, property)

def test_mm::pictograms::diagram_has_gridUnit():
    assert hasattr(mm::pictograms::Diagram, "gridUnit")
    descriptor = None
    for klass in mm::pictograms::Diagram.__mro__:
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



def test_mm::pictograms::connectiondecorator_is_not_abstract():
    assert not inspect.isabstract(mm::pictograms::ConnectionDecorator)


def test_mm::pictograms::connectiondecorator_constructor_exists():
    assert callable(mm::pictograms::ConnectionDecorator.__init__)


def test_mm::pictograms::connectiondecorator_constructor_args():
    sig = inspect.signature(mm::pictograms::ConnectionDecorator.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "locationRelative" in params, "Missing parameter 'locationRelative'"

def test_mm::pictograms::connectiondecorator_has_location():
    assert hasattr(mm::pictograms::ConnectionDecorator, "location")
    descriptor = None
    for klass in mm::pictograms::ConnectionDecorator.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_mm::pictograms::connectiondecorator_has_locationRelative():
    assert hasattr(mm::pictograms::ConnectionDecorator, "locationRelative")
    descriptor = None
    for klass in mm::pictograms::ConnectionDecorator.__mro__:
        if "locationRelative" in klass.__dict__:
            descriptor = klass.__dict__["locationRelative"]
            break
    assert isinstance(descriptor, property)



def test_mm::pictograms::containershape_is_not_abstract():
    assert not inspect.isabstract(mm::pictograms::ContainerShape)


def test_mm::pictograms::containershape_constructor_exists():
    assert callable(mm::pictograms::ContainerShape.__init__)


def test_mm::pictograms::containershape_constructor_args():
    sig = inspect.signature(mm::pictograms::ContainerShape.__init__)
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



def test_mm::pictograms::connection_is_not_abstract():
    assert not inspect.isabstract(mm::pictograms::Connection)


def test_mm::pictograms::connection_constructor_exists():
    assert callable(mm::pictograms::Connection.__init__)


def test_mm::pictograms::connection_constructor_args():
    sig = inspect.signature(mm::pictograms::Connection.__init__)
    params = list(sig.parameters.keys())



def test_mm::pictograms::shape_is_not_abstract():
    assert not inspect.isabstract(mm::pictograms::Shape)


def test_mm::pictograms::shape_constructor_exists():
    assert callable(mm::pictograms::Shape.__init__)


def test_mm::pictograms::shape_constructor_args():
    sig = inspect.signature(mm::pictograms::Shape.__init__)
    params = list(sig.parameters.keys())



def test_styles::style_is_not_abstract():
    assert not inspect.isabstract(styles::Style)


def test_styles::style_constructor_exists():
    assert callable(styles::Style.__init__)


def test_styles::style_constructor_args():
    sig = inspect.signature(styles::Style.__init__)
    params = list(sig.parameters.keys())



def test_mm::stylecontainer_is_not_abstract():
    assert not inspect.isabstract(mm::StyleContainer)


def test_mm::stylecontainer_constructor_exists():
    assert callable(mm::StyleContainer.__init__)


def test_mm::stylecontainer_constructor_args():
    sig = inspect.signature(mm::StyleContainer.__init__)
    params = list(sig.parameters.keys())



def test_propertycontainer_is_not_abstract():
    assert not inspect.isabstract(PropertyContainer)


def test_propertycontainer_constructor_exists():
    assert callable(PropertyContainer.__init__)


def test_propertycontainer_constructor_args():
    sig = inspect.signature(PropertyContainer.__init__)
    params = list(sig.parameters.keys())



def test_mm::pictograms::pictogramlink_is_not_abstract():
    assert not inspect.isabstract(mm::pictograms::PictogramLink)


def test_mm::pictograms::pictogramlink_constructor_exists():
    assert callable(mm::pictograms::PictogramLink.__init__)


def test_mm::pictograms::pictogramlink_constructor_args():
    sig = inspect.signature(mm::pictograms::PictogramLink.__init__)
    params = list(sig.parameters.keys())



def test_mm::graphicsalgorithmcontainer_is_not_abstract():
    assert not inspect.isabstract(mm::GraphicsAlgorithmContainer)


def test_mm::graphicsalgorithmcontainer_constructor_exists():
    assert callable(mm::GraphicsAlgorithmContainer.__init__)


def test_mm::graphicsalgorithmcontainer_constructor_args():
    sig = inspect.signature(mm::GraphicsAlgorithmContainer.__init__)
    params = list(sig.parameters.keys())



def test_mm::propertycontainer_is_not_abstract():
    assert not inspect.isabstract(mm::PropertyContainer)


def test_mm::propertycontainer_constructor_exists():
    assert callable(mm::PropertyContainer.__init__)


def test_mm::propertycontainer_constructor_args():
    sig = inspect.signature(mm::PropertyContainer.__init__)
    params = list(sig.parameters.keys())



def test_mm::property_is_not_abstract():
    assert not inspect.isabstract(mm::Property)


def test_mm::property_constructor_exists():
    assert callable(mm::Property.__init__)


def test_mm::property_constructor_args():
    sig = inspect.signature(mm::Property.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_mm::property_has_key():
    assert hasattr(mm::Property, "key")
    descriptor = None
    for klass in mm::Property.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_mm::property_has_value():
    assert hasattr(mm::Property, "value")
    descriptor = None
    for klass in mm::Property.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_linestyle_exists():
    # Check that the Enumeration exists
    assert LineStyle is not None

def test_linestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineStyle]
    expected_literals = [
        "UNSPECIFIED",
        "DASH",
        "DASHDOTDOT",
        "DOT",
        "DASHDOT",
        "SOLID",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineStyle"

def test_orientation_exists():
    # Check that the Enumeration exists
    assert Orientation is not None

def test_orientation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Orientation]
    expected_literals = [
        "ALIGNMENT_LEFT",
        "ALIGNMENT_RIGHT",
        "ALIGNMENT_BOTTOM",
        "ALIGNMENT_TOP",
        "UNSPECIFIED",
        "ALIGNMENT_CENTER",
        "ALIGNMENT_MIDDLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Orientation"

def test_locationtype_exists():
    # Check that the Enumeration exists
    assert LocationType is not None

def test_locationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LocationType]
    expected_literals = [
        "LOCATION_TYPE_ABSOLUTE_END",
        "LOCATION_TYPE_ABSOLUTE_START",
        "LOCATION_TYPE_RELATIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LocationType"

def test_underlinestyle_exists():
    # Check that the Enumeration exists
    assert UnderlineStyle is not None

def test_underlinestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnderlineStyle]
    expected_literals = [
        "UNDERLINE_ERROR",
        "UNDERLINE_SQUIGGLE",
        "UNDERLINE_DOUBLE",
        "UNDERLINE_SINGLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnderlineStyle"


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
mm::styles::TextStyle_strategy = st.builds(
    mm::styles::TextStyle,
    underline=
        st.booleans(),
    underlineStyle=
        safe_text,
    strikeout=
        st.booleans()
)
mm::styles::PrecisionPoint_strategy = st.builds(
    mm::styles::PrecisionPoint,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
styles::TextStyle_strategy = st.builds(
    styles::TextStyle,
)
mm::styles::TextStyleRegion_strategy = st.builds(
    mm::styles::TextStyleRegion,
    start=
        st.integers(),
    end=
        st.integers()
)
mm::styles::GradientColoredLocation_strategy = st.builds(
    mm::styles::GradientColoredLocation,
    locationType=
        safe_text,
    locationValue=
        safe_text
)
styles::RenderingStyle_strategy = st.builds(
    styles::RenderingStyle,
)
mm::styles::Color_strategy = st.builds(
    mm::styles::Color,
    green=
        st.integers(),
    red=
        st.integers(),
    blue=
        st.integers()
)
mm::styles::Point_strategy = st.builds(
    mm::styles::Point,
    x=
        st.integers(),
    before=
        st.integers(),
    y=
        st.integers(),
    after=
        st.integers()
)
mm::styles::Font_strategy = st.builds(
    mm::styles::Font,
    size=
        st.integers(),
    name=
        safe_text,
    bold=
        st.booleans(),
    italic=
        st.booleans()
)
styles::GradientColoredAreas_strategy = st.builds(
    styles::GradientColoredAreas,
)
mm::styles::AdaptedGradientColoredAreas_strategy = st.builds(
    mm::styles::AdaptedGradientColoredAreas,
    gradientType=
        safe_text,
    definedStyleId=
        safe_text
)
styles::GradientColoredArea_strategy = st.builds(
    styles::GradientColoredArea,
)
mm::styles::GradientColoredAreas_strategy = st.builds(
    mm::styles::GradientColoredAreas,
    styleAdaption=
        safe_text
)
styles::GradientColoredLocation_strategy = st.builds(
    styles::GradientColoredLocation,
)
mm::styles::GradientColoredArea_strategy = st.builds(
    mm::styles::GradientColoredArea,
)
styles::TextStyleRegion_strategy = st.builds(
    styles::TextStyleRegion,
)
mm::styles::AbstractStyle_strategy = st.builds(
    mm::styles::AbstractStyle,
    filled=
        safe_text,
    lineVisible=
        safe_text,
    lineStyle=
        safe_text,
    transparency=
        safe_text,
    lineWidth=
        safe_text
)
styles::mm::StyleContainer_strategy = st.builds(
    styles::mm::StyleContainer,
)
styles::AdaptedGradientColoredAreas_strategy = st.builds(
    styles::AdaptedGradientColoredAreas,
)
mm::styles::RenderingStyle_strategy = st.builds(
    mm::styles::RenderingStyle,
)
styles::AbstractStyle_strategy = st.builds(
    styles::AbstractStyle,
)
Polyline_strategy = st.builds(
    Polyline,
)
mm::algorithms::Polygon_strategy = st.builds(
    mm::algorithms::Polygon,
)
AbstractText_strategy = st.builds(
    AbstractText,
)
mm::algorithms::MultiText_strategy = st.builds(
    mm::algorithms::MultiText,
)
mm::algorithms::Text_strategy = st.builds(
    mm::algorithms::Text,
)
styles::Point_strategy = st.builds(
    styles::Point,
)
AdvancedAnchor_strategy = st.builds(
    AdvancedAnchor,
)
mm::pictograms::BoxRelativeAnchor_strategy = st.builds(
    mm::pictograms::BoxRelativeAnchor,
    relativeHeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    relativeWidth=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
mm::pictograms::FixPointAnchor_strategy = st.builds(
    mm::pictograms::FixPointAnchor,
)
CurvedConnection_strategy = st.builds(
    CurvedConnection,
)
styles::PrecisionPoint_strategy = st.builds(
    styles::PrecisionPoint,
)
pictograms::mm::EObject_strategy = st.builds(
    pictograms::mm::EObject,
)
PictogramLink_strategy = st.builds(
    PictogramLink,
)
styles::Font_strategy = st.builds(
    styles::Font,
)
styles::Color_strategy = st.builds(
    styles::Color,
)
PictogramElement_strategy = st.builds(
    PictogramElement,
)
mm::pictograms::AnchorContainer_strategy = st.builds(
    mm::pictograms::AnchorContainer,
)
mm::pictograms::Anchor_strategy = st.builds(
    mm::pictograms::Anchor,
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
mm::pictograms::ChopboxAnchor_strategy = st.builds(
    mm::pictograms::ChopboxAnchor,
)
mm::pictograms::AdvancedAnchor_strategy = st.builds(
    mm::pictograms::AdvancedAnchor,
    useAnchorLocationAsConnectionEndpoint=
        st.booleans()
)
GraphicsAlgorithm_strategy = st.builds(
    GraphicsAlgorithm,
)
mm::algorithms::RoundedRectangle_strategy = st.builds(
    mm::algorithms::RoundedRectangle,
    cornerHeight=
        st.integers(),
    cornerWidth=
        st.integers()
)
mm::algorithms::Rectangle_strategy = st.builds(
    mm::algorithms::Rectangle,
)
mm::algorithms::Image_strategy = st.builds(
    mm::algorithms::Image,
    id=
        safe_text,
    proportional=
        safe_text,
    stretchV=
        safe_text,
    stretchH=
        safe_text
)
mm::algorithms::PlatformGraphicsAlgorithm_strategy = st.builds(
    mm::algorithms::PlatformGraphicsAlgorithm,
    id=
        safe_text
)
mm::algorithms::Ellipse_strategy = st.builds(
    mm::algorithms::Ellipse,
)
mm::algorithms::AbstractText_strategy = st.builds(
    mm::algorithms::AbstractText,
    angle=
        safe_text,
    horizontalAlignment=
        safe_text,
    value=
        safe_text,
    verticalAlignment=
        safe_text
)
mm::algorithms::Polyline_strategy = st.builds(
    mm::algorithms::Polyline,
)
GraphicsAlgorithmContainer_strategy = st.builds(
    GraphicsAlgorithmContainer,
)
mm::algorithms::GraphicsAlgorithm_strategy = st.builds(
    mm::algorithms::GraphicsAlgorithm,
    height=
        st.integers(),
    width=
        st.integers(),
    x=
        st.integers(),
    y=
        st.integers()
)
mm::pictograms::PictogramElement_strategy = st.builds(
    mm::pictograms::PictogramElement,
    visible=
        st.booleans(),
    active=
        st.booleans()
)
Connection_strategy = st.builds(
    Connection,
)
mm::pictograms::FreeFormConnection_strategy = st.builds(
    mm::pictograms::FreeFormConnection,
)
mm::pictograms::ManhattanConnection_strategy = st.builds(
    mm::pictograms::ManhattanConnection,
)
mm::pictograms::CurvedConnection_strategy = st.builds(
    mm::pictograms::CurvedConnection,
)
mm::pictograms::CompositeConnection_strategy = st.builds(
    mm::pictograms::CompositeConnection,
)
StyleContainer_strategy = st.builds(
    StyleContainer,
)
mm::styles::Style_strategy = st.builds(
    mm::styles::Style,
    horizontalAlignment=
        safe_text,
    verticalAlignment=
        safe_text,
    stretchH=
        safe_text,
    proportional=
        safe_text,
    description=
        safe_text,
    id=
        safe_text,
    angle=
        safe_text,
    stretchV=
        safe_text
)
pictograms::ContainerShape_strategy = st.builds(
    pictograms::ContainerShape,
)
mm::pictograms::Diagram_strategy = st.builds(
    mm::pictograms::Diagram,
    version=
        safe_text,
    diagramTypeId=
        safe_text,
    showGuides=
        st.booleans(),
    verticalGridUnit=
        st.integers(),
    name=
        safe_text,
    snapToGrid=
        st.booleans(),
    gridUnit=
        st.integers()
)
Shape_strategy = st.builds(
    Shape,
)
mm::pictograms::ConnectionDecorator_strategy = st.builds(
    mm::pictograms::ConnectionDecorator,
    location=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    locationRelative=
        st.booleans()
)
mm::pictograms::ContainerShape_strategy = st.builds(
    mm::pictograms::ContainerShape,
)
ContainerShape_strategy = st.builds(
    ContainerShape,
)
AnchorContainer_strategy = st.builds(
    AnchorContainer,
)
mm::pictograms::Connection_strategy = st.builds(
    mm::pictograms::Connection,
)
mm::pictograms::Shape_strategy = st.builds(
    mm::pictograms::Shape,
)
styles::Style_strategy = st.builds(
    styles::Style,
)
mm::StyleContainer_strategy = st.builds(
    mm::StyleContainer,
)
PropertyContainer_strategy = st.builds(
    PropertyContainer,
)
mm::pictograms::PictogramLink_strategy = st.builds(
    mm::pictograms::PictogramLink,
)
mm::GraphicsAlgorithmContainer_strategy = st.builds(
    mm::GraphicsAlgorithmContainer,
)
mm::PropertyContainer_strategy = st.builds(
    mm::PropertyContainer,
)
mm::Property_strategy = st.builds(
    mm::Property,
    key=
        safe_text,
    value=
        safe_text
)

@given(instance=mm::styles::TextStyle_strategy)
@settings(max_examples=50)
def test_mm::styles::textstyle_instantiation(instance):
    assert isinstance(instance, mm::styles::TextStyle)

@given(instance=mm::styles::TextStyle_strategy)
def test_mm::styles::textstyle_underline_type(instance):
    assert isinstance(instance.underline, bool)


@given(instance=mm::styles::TextStyle_strategy)
def test_mm::styles::textstyle_underline_setter(instance):
    original = instance.underline
    instance.underline = original
    assert instance.underline == original

@given(instance=mm::styles::TextStyle_strategy)
def test_mm::styles::textstyle_underlineStyle_type(instance):
    assert isinstance(instance.underlineStyle, str)


@given(instance=mm::styles::TextStyle_strategy)
def test_mm::styles::textstyle_underlineStyle_setter(instance):
    original = instance.underlineStyle
    instance.underlineStyle = original
    assert instance.underlineStyle == original

@given(instance=mm::styles::TextStyle_strategy)
def test_mm::styles::textstyle_strikeout_type(instance):
    assert isinstance(instance.strikeout, bool)


@given(instance=mm::styles::TextStyle_strategy)
def test_mm::styles::textstyle_strikeout_setter(instance):
    original = instance.strikeout
    instance.strikeout = original
    assert instance.strikeout == original

@given(instance=mm::styles::PrecisionPoint_strategy)
@settings(max_examples=50)
def test_mm::styles::precisionpoint_instantiation(instance):
    assert isinstance(instance, mm::styles::PrecisionPoint)

@given(instance=mm::styles::PrecisionPoint_strategy)
def test_mm::styles::precisionpoint_x_type(instance):
    assert isinstance(instance.x, float)


@given(instance=mm::styles::PrecisionPoint_strategy)
def test_mm::styles::precisionpoint_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mm::styles::PrecisionPoint_strategy)
def test_mm::styles::precisionpoint_y_type(instance):
    assert isinstance(instance.y, float)


@given(instance=mm::styles::PrecisionPoint_strategy)
def test_mm::styles::precisionpoint_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=styles::TextStyle_strategy)
@settings(max_examples=50)
def test_styles::textstyle_instantiation(instance):
    assert isinstance(instance, styles::TextStyle)

@given(instance=mm::styles::TextStyleRegion_strategy)
@settings(max_examples=50)
def test_mm::styles::textstyleregion_instantiation(instance):
    assert isinstance(instance, mm::styles::TextStyleRegion)

@given(instance=mm::styles::TextStyleRegion_strategy)
def test_mm::styles::textstyleregion_start_type(instance):
    assert isinstance(instance.start, int)


@given(instance=mm::styles::TextStyleRegion_strategy)
def test_mm::styles::textstyleregion_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=mm::styles::TextStyleRegion_strategy)
def test_mm::styles::textstyleregion_end_type(instance):
    assert isinstance(instance.end, int)


@given(instance=mm::styles::TextStyleRegion_strategy)
def test_mm::styles::textstyleregion_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=mm::styles::GradientColoredLocation_strategy)
@settings(max_examples=50)
def test_mm::styles::gradientcoloredlocation_instantiation(instance):
    assert isinstance(instance, mm::styles::GradientColoredLocation)

@given(instance=mm::styles::GradientColoredLocation_strategy)
def test_mm::styles::gradientcoloredlocation_locationType_type(instance):
    assert isinstance(instance.locationType, str)


@given(instance=mm::styles::GradientColoredLocation_strategy)
def test_mm::styles::gradientcoloredlocation_locationType_setter(instance):
    original = instance.locationType
    instance.locationType = original
    assert instance.locationType == original

@given(instance=mm::styles::GradientColoredLocation_strategy)
def test_mm::styles::gradientcoloredlocation_locationValue_type(instance):
    assert isinstance(instance.locationValue, str)


@given(instance=mm::styles::GradientColoredLocation_strategy)
def test_mm::styles::gradientcoloredlocation_locationValue_setter(instance):
    original = instance.locationValue
    instance.locationValue = original
    assert instance.locationValue == original

@given(instance=styles::RenderingStyle_strategy)
@settings(max_examples=50)
def test_styles::renderingstyle_instantiation(instance):
    assert isinstance(instance, styles::RenderingStyle)

@given(instance=mm::styles::Color_strategy)
@settings(max_examples=50)
def test_mm::styles::color_instantiation(instance):
    assert isinstance(instance, mm::styles::Color)

@given(instance=mm::styles::Color_strategy)
def test_mm::styles::color_green_type(instance):
    assert isinstance(instance.green, int)


@given(instance=mm::styles::Color_strategy)
def test_mm::styles::color_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original

@given(instance=mm::styles::Color_strategy)
def test_mm::styles::color_red_type(instance):
    assert isinstance(instance.red, int)


@given(instance=mm::styles::Color_strategy)
def test_mm::styles::color_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original

@given(instance=mm::styles::Color_strategy)
def test_mm::styles::color_blue_type(instance):
    assert isinstance(instance.blue, int)


@given(instance=mm::styles::Color_strategy)
def test_mm::styles::color_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original

@given(instance=mm::styles::Point_strategy)
@settings(max_examples=50)
def test_mm::styles::point_instantiation(instance):
    assert isinstance(instance, mm::styles::Point)

@given(instance=mm::styles::Point_strategy)
def test_mm::styles::point_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=mm::styles::Point_strategy)
def test_mm::styles::point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mm::styles::Point_strategy)
def test_mm::styles::point_before_type(instance):
    assert isinstance(instance.before, int)


@given(instance=mm::styles::Point_strategy)
def test_mm::styles::point_before_setter(instance):
    original = instance.before
    instance.before = original
    assert instance.before == original

@given(instance=mm::styles::Point_strategy)
def test_mm::styles::point_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=mm::styles::Point_strategy)
def test_mm::styles::point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=mm::styles::Point_strategy)
def test_mm::styles::point_after_type(instance):
    assert isinstance(instance.after, int)


@given(instance=mm::styles::Point_strategy)
def test_mm::styles::point_after_setter(instance):
    original = instance.after
    instance.after = original
    assert instance.after == original

@given(instance=mm::styles::Font_strategy)
@settings(max_examples=50)
def test_mm::styles::font_instantiation(instance):
    assert isinstance(instance, mm::styles::Font)

@given(instance=mm::styles::Font_strategy)
def test_mm::styles::font_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=mm::styles::Font_strategy)
def test_mm::styles::font_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=mm::styles::Font_strategy)
def test_mm::styles::font_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::styles::Font_strategy)
def test_mm::styles::font_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm::styles::Font_strategy)
def test_mm::styles::font_bold_type(instance):
    assert isinstance(instance.bold, bool)


@given(instance=mm::styles::Font_strategy)
def test_mm::styles::font_bold_setter(instance):
    original = instance.bold
    instance.bold = original
    assert instance.bold == original

@given(instance=mm::styles::Font_strategy)
def test_mm::styles::font_italic_type(instance):
    assert isinstance(instance.italic, bool)


@given(instance=mm::styles::Font_strategy)
def test_mm::styles::font_italic_setter(instance):
    original = instance.italic
    instance.italic = original
    assert instance.italic == original

@given(instance=styles::GradientColoredAreas_strategy)
@settings(max_examples=50)
def test_styles::gradientcoloredareas_instantiation(instance):
    assert isinstance(instance, styles::GradientColoredAreas)

@given(instance=mm::styles::AdaptedGradientColoredAreas_strategy)
@settings(max_examples=50)
def test_mm::styles::adaptedgradientcoloredareas_instantiation(instance):
    assert isinstance(instance, mm::styles::AdaptedGradientColoredAreas)

@given(instance=mm::styles::AdaptedGradientColoredAreas_strategy)
def test_mm::styles::adaptedgradientcoloredareas_gradientType_type(instance):
    assert isinstance(instance.gradientType, str)


@given(instance=mm::styles::AdaptedGradientColoredAreas_strategy)
def test_mm::styles::adaptedgradientcoloredareas_gradientType_setter(instance):
    original = instance.gradientType
    instance.gradientType = original
    assert instance.gradientType == original

@given(instance=mm::styles::AdaptedGradientColoredAreas_strategy)
def test_mm::styles::adaptedgradientcoloredareas_definedStyleId_type(instance):
    assert isinstance(instance.definedStyleId, str)


@given(instance=mm::styles::AdaptedGradientColoredAreas_strategy)
def test_mm::styles::adaptedgradientcoloredareas_definedStyleId_setter(instance):
    original = instance.definedStyleId
    instance.definedStyleId = original
    assert instance.definedStyleId == original

@given(instance=styles::GradientColoredArea_strategy)
@settings(max_examples=50)
def test_styles::gradientcoloredarea_instantiation(instance):
    assert isinstance(instance, styles::GradientColoredArea)

@given(instance=mm::styles::GradientColoredAreas_strategy)
@settings(max_examples=50)
def test_mm::styles::gradientcoloredareas_instantiation(instance):
    assert isinstance(instance, mm::styles::GradientColoredAreas)

@given(instance=mm::styles::GradientColoredAreas_strategy)
def test_mm::styles::gradientcoloredareas_styleAdaption_type(instance):
    assert isinstance(instance.styleAdaption, str)


@given(instance=mm::styles::GradientColoredAreas_strategy)
def test_mm::styles::gradientcoloredareas_styleAdaption_setter(instance):
    original = instance.styleAdaption
    instance.styleAdaption = original
    assert instance.styleAdaption == original

@given(instance=styles::GradientColoredLocation_strategy)
@settings(max_examples=50)
def test_styles::gradientcoloredlocation_instantiation(instance):
    assert isinstance(instance, styles::GradientColoredLocation)

@given(instance=mm::styles::GradientColoredArea_strategy)
@settings(max_examples=50)
def test_mm::styles::gradientcoloredarea_instantiation(instance):
    assert isinstance(instance, mm::styles::GradientColoredArea)

@given(instance=styles::TextStyleRegion_strategy)
@settings(max_examples=50)
def test_styles::textstyleregion_instantiation(instance):
    assert isinstance(instance, styles::TextStyleRegion)

@given(instance=mm::styles::AbstractStyle_strategy)
@settings(max_examples=50)
def test_mm::styles::abstractstyle_instantiation(instance):
    assert isinstance(instance, mm::styles::AbstractStyle)

@given(instance=mm::styles::AbstractStyle_strategy)
def test_mm::styles::abstractstyle_filled_type(instance):
    assert isinstance(instance.filled, str)


@given(instance=mm::styles::AbstractStyle_strategy)
def test_mm::styles::abstractstyle_filled_setter(instance):
    original = instance.filled
    instance.filled = original
    assert instance.filled == original

@given(instance=mm::styles::AbstractStyle_strategy)
def test_mm::styles::abstractstyle_lineVisible_type(instance):
    assert isinstance(instance.lineVisible, str)


@given(instance=mm::styles::AbstractStyle_strategy)
def test_mm::styles::abstractstyle_lineVisible_setter(instance):
    original = instance.lineVisible
    instance.lineVisible = original
    assert instance.lineVisible == original

@given(instance=mm::styles::AbstractStyle_strategy)
def test_mm::styles::abstractstyle_lineStyle_type(instance):
    assert isinstance(instance.lineStyle, str)


@given(instance=mm::styles::AbstractStyle_strategy)
def test_mm::styles::abstractstyle_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original

@given(instance=mm::styles::AbstractStyle_strategy)
def test_mm::styles::abstractstyle_transparency_type(instance):
    assert isinstance(instance.transparency, str)


@given(instance=mm::styles::AbstractStyle_strategy)
def test_mm::styles::abstractstyle_transparency_setter(instance):
    original = instance.transparency
    instance.transparency = original
    assert instance.transparency == original

@given(instance=mm::styles::AbstractStyle_strategy)
def test_mm::styles::abstractstyle_lineWidth_type(instance):
    assert isinstance(instance.lineWidth, str)


@given(instance=mm::styles::AbstractStyle_strategy)
def test_mm::styles::abstractstyle_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original

@given(instance=styles::mm::StyleContainer_strategy)
@settings(max_examples=50)
def test_styles::mm::stylecontainer_instantiation(instance):
    assert isinstance(instance, styles::mm::StyleContainer)

@given(instance=styles::AdaptedGradientColoredAreas_strategy)
@settings(max_examples=50)
def test_styles::adaptedgradientcoloredareas_instantiation(instance):
    assert isinstance(instance, styles::AdaptedGradientColoredAreas)

@given(instance=mm::styles::RenderingStyle_strategy)
@settings(max_examples=50)
def test_mm::styles::renderingstyle_instantiation(instance):
    assert isinstance(instance, mm::styles::RenderingStyle)

@given(instance=styles::AbstractStyle_strategy)
@settings(max_examples=50)
def test_styles::abstractstyle_instantiation(instance):
    assert isinstance(instance, styles::AbstractStyle)

@given(instance=Polyline_strategy)
@settings(max_examples=50)
def test_polyline_instantiation(instance):
    assert isinstance(instance, Polyline)

@given(instance=mm::algorithms::Polygon_strategy)
@settings(max_examples=50)
def test_mm::algorithms::polygon_instantiation(instance):
    assert isinstance(instance, mm::algorithms::Polygon)

@given(instance=AbstractText_strategy)
@settings(max_examples=50)
def test_abstracttext_instantiation(instance):
    assert isinstance(instance, AbstractText)

@given(instance=mm::algorithms::MultiText_strategy)
@settings(max_examples=50)
def test_mm::algorithms::multitext_instantiation(instance):
    assert isinstance(instance, mm::algorithms::MultiText)

@given(instance=mm::algorithms::Text_strategy)
@settings(max_examples=50)
def test_mm::algorithms::text_instantiation(instance):
    assert isinstance(instance, mm::algorithms::Text)

@given(instance=styles::Point_strategy)
@settings(max_examples=50)
def test_styles::point_instantiation(instance):
    assert isinstance(instance, styles::Point)

@given(instance=AdvancedAnchor_strategy)
@settings(max_examples=50)
def test_advancedanchor_instantiation(instance):
    assert isinstance(instance, AdvancedAnchor)

@given(instance=mm::pictograms::BoxRelativeAnchor_strategy)
@settings(max_examples=50)
def test_mm::pictograms::boxrelativeanchor_instantiation(instance):
    assert isinstance(instance, mm::pictograms::BoxRelativeAnchor)

@given(instance=mm::pictograms::BoxRelativeAnchor_strategy)
def test_mm::pictograms::boxrelativeanchor_relativeHeight_type(instance):
    assert isinstance(instance.relativeHeight, float)


@given(instance=mm::pictograms::BoxRelativeAnchor_strategy)
def test_mm::pictograms::boxrelativeanchor_relativeHeight_setter(instance):
    original = instance.relativeHeight
    instance.relativeHeight = original
    assert instance.relativeHeight == original

@given(instance=mm::pictograms::BoxRelativeAnchor_strategy)
def test_mm::pictograms::boxrelativeanchor_relativeWidth_type(instance):
    assert isinstance(instance.relativeWidth, float)


@given(instance=mm::pictograms::BoxRelativeAnchor_strategy)
def test_mm::pictograms::boxrelativeanchor_relativeWidth_setter(instance):
    original = instance.relativeWidth
    instance.relativeWidth = original
    assert instance.relativeWidth == original

@given(instance=mm::pictograms::FixPointAnchor_strategy)
@settings(max_examples=50)
def test_mm::pictograms::fixpointanchor_instantiation(instance):
    assert isinstance(instance, mm::pictograms::FixPointAnchor)

@given(instance=CurvedConnection_strategy)
@settings(max_examples=50)
def test_curvedconnection_instantiation(instance):
    assert isinstance(instance, CurvedConnection)

@given(instance=styles::PrecisionPoint_strategy)
@settings(max_examples=50)
def test_styles::precisionpoint_instantiation(instance):
    assert isinstance(instance, styles::PrecisionPoint)

@given(instance=pictograms::mm::EObject_strategy)
@settings(max_examples=50)
def test_pictograms::mm::eobject_instantiation(instance):
    assert isinstance(instance, pictograms::mm::EObject)

@given(instance=PictogramLink_strategy)
@settings(max_examples=50)
def test_pictogramlink_instantiation(instance):
    assert isinstance(instance, PictogramLink)

@given(instance=styles::Font_strategy)
@settings(max_examples=50)
def test_styles::font_instantiation(instance):
    assert isinstance(instance, styles::Font)

@given(instance=styles::Color_strategy)
@settings(max_examples=50)
def test_styles::color_instantiation(instance):
    assert isinstance(instance, styles::Color)

@given(instance=PictogramElement_strategy)
@settings(max_examples=50)
def test_pictogramelement_instantiation(instance):
    assert isinstance(instance, PictogramElement)

@given(instance=mm::pictograms::AnchorContainer_strategy)
@settings(max_examples=50)
def test_mm::pictograms::anchorcontainer_instantiation(instance):
    assert isinstance(instance, mm::pictograms::AnchorContainer)

@given(instance=mm::pictograms::Anchor_strategy)
@settings(max_examples=50)
def test_mm::pictograms::anchor_instantiation(instance):
    assert isinstance(instance, mm::pictograms::Anchor)

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

@given(instance=mm::pictograms::ChopboxAnchor_strategy)
@settings(max_examples=50)
def test_mm::pictograms::chopboxanchor_instantiation(instance):
    assert isinstance(instance, mm::pictograms::ChopboxAnchor)

@given(instance=mm::pictograms::AdvancedAnchor_strategy)
@settings(max_examples=50)
def test_mm::pictograms::advancedanchor_instantiation(instance):
    assert isinstance(instance, mm::pictograms::AdvancedAnchor)

@given(instance=mm::pictograms::AdvancedAnchor_strategy)
def test_mm::pictograms::advancedanchor_useAnchorLocationAsConnectionEndpoint_type(instance):
    assert isinstance(instance.useAnchorLocationAsConnectionEndpoint, bool)


@given(instance=mm::pictograms::AdvancedAnchor_strategy)
def test_mm::pictograms::advancedanchor_useAnchorLocationAsConnectionEndpoint_setter(instance):
    original = instance.useAnchorLocationAsConnectionEndpoint
    instance.useAnchorLocationAsConnectionEndpoint = original
    assert instance.useAnchorLocationAsConnectionEndpoint == original

@given(instance=GraphicsAlgorithm_strategy)
@settings(max_examples=50)
def test_graphicsalgorithm_instantiation(instance):
    assert isinstance(instance, GraphicsAlgorithm)

@given(instance=mm::algorithms::RoundedRectangle_strategy)
@settings(max_examples=50)
def test_mm::algorithms::roundedrectangle_instantiation(instance):
    assert isinstance(instance, mm::algorithms::RoundedRectangle)

@given(instance=mm::algorithms::RoundedRectangle_strategy)
def test_mm::algorithms::roundedrectangle_cornerHeight_type(instance):
    assert isinstance(instance.cornerHeight, int)


@given(instance=mm::algorithms::RoundedRectangle_strategy)
def test_mm::algorithms::roundedrectangle_cornerHeight_setter(instance):
    original = instance.cornerHeight
    instance.cornerHeight = original
    assert instance.cornerHeight == original

@given(instance=mm::algorithms::RoundedRectangle_strategy)
def test_mm::algorithms::roundedrectangle_cornerWidth_type(instance):
    assert isinstance(instance.cornerWidth, int)


@given(instance=mm::algorithms::RoundedRectangle_strategy)
def test_mm::algorithms::roundedrectangle_cornerWidth_setter(instance):
    original = instance.cornerWidth
    instance.cornerWidth = original
    assert instance.cornerWidth == original

@given(instance=mm::algorithms::Rectangle_strategy)
@settings(max_examples=50)
def test_mm::algorithms::rectangle_instantiation(instance):
    assert isinstance(instance, mm::algorithms::Rectangle)

@given(instance=mm::algorithms::Image_strategy)
@settings(max_examples=50)
def test_mm::algorithms::image_instantiation(instance):
    assert isinstance(instance, mm::algorithms::Image)

@given(instance=mm::algorithms::Image_strategy)
def test_mm::algorithms::image_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=mm::algorithms::Image_strategy)
def test_mm::algorithms::image_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=mm::algorithms::Image_strategy)
def test_mm::algorithms::image_proportional_type(instance):
    assert isinstance(instance.proportional, str)


@given(instance=mm::algorithms::Image_strategy)
def test_mm::algorithms::image_proportional_setter(instance):
    original = instance.proportional
    instance.proportional = original
    assert instance.proportional == original

@given(instance=mm::algorithms::Image_strategy)
def test_mm::algorithms::image_stretchV_type(instance):
    assert isinstance(instance.stretchV, str)


@given(instance=mm::algorithms::Image_strategy)
def test_mm::algorithms::image_stretchV_setter(instance):
    original = instance.stretchV
    instance.stretchV = original
    assert instance.stretchV == original

@given(instance=mm::algorithms::Image_strategy)
def test_mm::algorithms::image_stretchH_type(instance):
    assert isinstance(instance.stretchH, str)


@given(instance=mm::algorithms::Image_strategy)
def test_mm::algorithms::image_stretchH_setter(instance):
    original = instance.stretchH
    instance.stretchH = original
    assert instance.stretchH == original

@given(instance=mm::algorithms::PlatformGraphicsAlgorithm_strategy)
@settings(max_examples=50)
def test_mm::algorithms::platformgraphicsalgorithm_instantiation(instance):
    assert isinstance(instance, mm::algorithms::PlatformGraphicsAlgorithm)

@given(instance=mm::algorithms::PlatformGraphicsAlgorithm_strategy)
def test_mm::algorithms::platformgraphicsalgorithm_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=mm::algorithms::PlatformGraphicsAlgorithm_strategy)
def test_mm::algorithms::platformgraphicsalgorithm_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=mm::algorithms::Ellipse_strategy)
@settings(max_examples=50)
def test_mm::algorithms::ellipse_instantiation(instance):
    assert isinstance(instance, mm::algorithms::Ellipse)

@given(instance=mm::algorithms::AbstractText_strategy)
@settings(max_examples=50)
def test_mm::algorithms::abstracttext_instantiation(instance):
    assert isinstance(instance, mm::algorithms::AbstractText)

@given(instance=mm::algorithms::AbstractText_strategy)
def test_mm::algorithms::abstracttext_angle_type(instance):
    assert isinstance(instance.angle, str)


@given(instance=mm::algorithms::AbstractText_strategy)
def test_mm::algorithms::abstracttext_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=mm::algorithms::AbstractText_strategy)
def test_mm::algorithms::abstracttext_horizontalAlignment_type(instance):
    assert isinstance(instance.horizontalAlignment, str)


@given(instance=mm::algorithms::AbstractText_strategy)
def test_mm::algorithms::abstracttext_horizontalAlignment_setter(instance):
    original = instance.horizontalAlignment
    instance.horizontalAlignment = original
    assert instance.horizontalAlignment == original

@given(instance=mm::algorithms::AbstractText_strategy)
def test_mm::algorithms::abstracttext_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=mm::algorithms::AbstractText_strategy)
def test_mm::algorithms::abstracttext_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mm::algorithms::AbstractText_strategy)
def test_mm::algorithms::abstracttext_verticalAlignment_type(instance):
    assert isinstance(instance.verticalAlignment, str)


@given(instance=mm::algorithms::AbstractText_strategy)
def test_mm::algorithms::abstracttext_verticalAlignment_setter(instance):
    original = instance.verticalAlignment
    instance.verticalAlignment = original
    assert instance.verticalAlignment == original

@given(instance=mm::algorithms::Polyline_strategy)
@settings(max_examples=50)
def test_mm::algorithms::polyline_instantiation(instance):
    assert isinstance(instance, mm::algorithms::Polyline)

@given(instance=GraphicsAlgorithmContainer_strategy)
@settings(max_examples=50)
def test_graphicsalgorithmcontainer_instantiation(instance):
    assert isinstance(instance, GraphicsAlgorithmContainer)

@given(instance=mm::algorithms::GraphicsAlgorithm_strategy)
@settings(max_examples=50)
def test_mm::algorithms::graphicsalgorithm_instantiation(instance):
    assert isinstance(instance, mm::algorithms::GraphicsAlgorithm)

@given(instance=mm::algorithms::GraphicsAlgorithm_strategy)
def test_mm::algorithms::graphicsalgorithm_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=mm::algorithms::GraphicsAlgorithm_strategy)
def test_mm::algorithms::graphicsalgorithm_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=mm::algorithms::GraphicsAlgorithm_strategy)
def test_mm::algorithms::graphicsalgorithm_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=mm::algorithms::GraphicsAlgorithm_strategy)
def test_mm::algorithms::graphicsalgorithm_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=mm::algorithms::GraphicsAlgorithm_strategy)
def test_mm::algorithms::graphicsalgorithm_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=mm::algorithms::GraphicsAlgorithm_strategy)
def test_mm::algorithms::graphicsalgorithm_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mm::algorithms::GraphicsAlgorithm_strategy)
def test_mm::algorithms::graphicsalgorithm_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=mm::algorithms::GraphicsAlgorithm_strategy)
def test_mm::algorithms::graphicsalgorithm_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=mm::pictograms::PictogramElement_strategy)
@settings(max_examples=50)
def test_mm::pictograms::pictogramelement_instantiation(instance):
    assert isinstance(instance, mm::pictograms::PictogramElement)

@given(instance=mm::pictograms::PictogramElement_strategy)
def test_mm::pictograms::pictogramelement_visible_type(instance):
    assert isinstance(instance.visible, bool)


@given(instance=mm::pictograms::PictogramElement_strategy)
def test_mm::pictograms::pictogramelement_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=mm::pictograms::PictogramElement_strategy)
def test_mm::pictograms::pictogramelement_active_type(instance):
    assert isinstance(instance.active, bool)


@given(instance=mm::pictograms::PictogramElement_strategy)
def test_mm::pictograms::pictogramelement_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=Connection_strategy)
@settings(max_examples=50)
def test_connection_instantiation(instance):
    assert isinstance(instance, Connection)

@given(instance=mm::pictograms::FreeFormConnection_strategy)
@settings(max_examples=50)
def test_mm::pictograms::freeformconnection_instantiation(instance):
    assert isinstance(instance, mm::pictograms::FreeFormConnection)

@given(instance=mm::pictograms::ManhattanConnection_strategy)
@settings(max_examples=50)
def test_mm::pictograms::manhattanconnection_instantiation(instance):
    assert isinstance(instance, mm::pictograms::ManhattanConnection)

@given(instance=mm::pictograms::CurvedConnection_strategy)
@settings(max_examples=50)
def test_mm::pictograms::curvedconnection_instantiation(instance):
    assert isinstance(instance, mm::pictograms::CurvedConnection)

@given(instance=mm::pictograms::CompositeConnection_strategy)
@settings(max_examples=50)
def test_mm::pictograms::compositeconnection_instantiation(instance):
    assert isinstance(instance, mm::pictograms::CompositeConnection)

@given(instance=StyleContainer_strategy)
@settings(max_examples=50)
def test_stylecontainer_instantiation(instance):
    assert isinstance(instance, StyleContainer)

@given(instance=mm::styles::Style_strategy)
@settings(max_examples=50)
def test_mm::styles::style_instantiation(instance):
    assert isinstance(instance, mm::styles::Style)

@given(instance=mm::styles::Style_strategy)
def test_mm::styles::style_horizontalAlignment_type(instance):
    assert isinstance(instance.horizontalAlignment, str)


@given(instance=mm::styles::Style_strategy)
def test_mm::styles::style_horizontalAlignment_setter(instance):
    original = instance.horizontalAlignment
    instance.horizontalAlignment = original
    assert instance.horizontalAlignment == original

@given(instance=mm::styles::Style_strategy)
def test_mm::styles::style_verticalAlignment_type(instance):
    assert isinstance(instance.verticalAlignment, str)


@given(instance=mm::styles::Style_strategy)
def test_mm::styles::style_verticalAlignment_setter(instance):
    original = instance.verticalAlignment
    instance.verticalAlignment = original
    assert instance.verticalAlignment == original

@given(instance=mm::styles::Style_strategy)
def test_mm::styles::style_stretchH_type(instance):
    assert isinstance(instance.stretchH, str)


@given(instance=mm::styles::Style_strategy)
def test_mm::styles::style_stretchH_setter(instance):
    original = instance.stretchH
    instance.stretchH = original
    assert instance.stretchH == original

@given(instance=mm::styles::Style_strategy)
def test_mm::styles::style_proportional_type(instance):
    assert isinstance(instance.proportional, str)


@given(instance=mm::styles::Style_strategy)
def test_mm::styles::style_proportional_setter(instance):
    original = instance.proportional
    instance.proportional = original
    assert instance.proportional == original

@given(instance=mm::styles::Style_strategy)
def test_mm::styles::style_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=mm::styles::Style_strategy)
def test_mm::styles::style_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=mm::styles::Style_strategy)
def test_mm::styles::style_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=mm::styles::Style_strategy)
def test_mm::styles::style_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=mm::styles::Style_strategy)
def test_mm::styles::style_angle_type(instance):
    assert isinstance(instance.angle, str)


@given(instance=mm::styles::Style_strategy)
def test_mm::styles::style_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=mm::styles::Style_strategy)
def test_mm::styles::style_stretchV_type(instance):
    assert isinstance(instance.stretchV, str)


@given(instance=mm::styles::Style_strategy)
def test_mm::styles::style_stretchV_setter(instance):
    original = instance.stretchV
    instance.stretchV = original
    assert instance.stretchV == original

@given(instance=pictograms::ContainerShape_strategy)
@settings(max_examples=50)
def test_pictograms::containershape_instantiation(instance):
    assert isinstance(instance, pictograms::ContainerShape)

@given(instance=mm::pictograms::Diagram_strategy)
@settings(max_examples=50)
def test_mm::pictograms::diagram_instantiation(instance):
    assert isinstance(instance, mm::pictograms::Diagram)

@given(instance=mm::pictograms::Diagram_strategy)
def test_mm::pictograms::diagram_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=mm::pictograms::Diagram_strategy)
def test_mm::pictograms::diagram_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=mm::pictograms::Diagram_strategy)
def test_mm::pictograms::diagram_diagramTypeId_type(instance):
    assert isinstance(instance.diagramTypeId, str)


@given(instance=mm::pictograms::Diagram_strategy)
def test_mm::pictograms::diagram_diagramTypeId_setter(instance):
    original = instance.diagramTypeId
    instance.diagramTypeId = original
    assert instance.diagramTypeId == original

@given(instance=mm::pictograms::Diagram_strategy)
def test_mm::pictograms::diagram_showGuides_type(instance):
    assert isinstance(instance.showGuides, bool)


@given(instance=mm::pictograms::Diagram_strategy)
def test_mm::pictograms::diagram_showGuides_setter(instance):
    original = instance.showGuides
    instance.showGuides = original
    assert instance.showGuides == original

@given(instance=mm::pictograms::Diagram_strategy)
def test_mm::pictograms::diagram_verticalGridUnit_type(instance):
    assert isinstance(instance.verticalGridUnit, int)


@given(instance=mm::pictograms::Diagram_strategy)
def test_mm::pictograms::diagram_verticalGridUnit_setter(instance):
    original = instance.verticalGridUnit
    instance.verticalGridUnit = original
    assert instance.verticalGridUnit == original

@given(instance=mm::pictograms::Diagram_strategy)
def test_mm::pictograms::diagram_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::pictograms::Diagram_strategy)
def test_mm::pictograms::diagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm::pictograms::Diagram_strategy)
def test_mm::pictograms::diagram_snapToGrid_type(instance):
    assert isinstance(instance.snapToGrid, bool)


@given(instance=mm::pictograms::Diagram_strategy)
def test_mm::pictograms::diagram_snapToGrid_setter(instance):
    original = instance.snapToGrid
    instance.snapToGrid = original
    assert instance.snapToGrid == original

@given(instance=mm::pictograms::Diagram_strategy)
def test_mm::pictograms::diagram_gridUnit_type(instance):
    assert isinstance(instance.gridUnit, int)


@given(instance=mm::pictograms::Diagram_strategy)
def test_mm::pictograms::diagram_gridUnit_setter(instance):
    original = instance.gridUnit
    instance.gridUnit = original
    assert instance.gridUnit == original

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=mm::pictograms::ConnectionDecorator_strategy)
@settings(max_examples=50)
def test_mm::pictograms::connectiondecorator_instantiation(instance):
    assert isinstance(instance, mm::pictograms::ConnectionDecorator)

@given(instance=mm::pictograms::ConnectionDecorator_strategy)
def test_mm::pictograms::connectiondecorator_location_type(instance):
    assert isinstance(instance.location, float)


@given(instance=mm::pictograms::ConnectionDecorator_strategy)
def test_mm::pictograms::connectiondecorator_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=mm::pictograms::ConnectionDecorator_strategy)
def test_mm::pictograms::connectiondecorator_locationRelative_type(instance):
    assert isinstance(instance.locationRelative, bool)


@given(instance=mm::pictograms::ConnectionDecorator_strategy)
def test_mm::pictograms::connectiondecorator_locationRelative_setter(instance):
    original = instance.locationRelative
    instance.locationRelative = original
    assert instance.locationRelative == original

@given(instance=mm::pictograms::ContainerShape_strategy)
@settings(max_examples=50)
def test_mm::pictograms::containershape_instantiation(instance):
    assert isinstance(instance, mm::pictograms::ContainerShape)

@given(instance=ContainerShape_strategy)
@settings(max_examples=50)
def test_containershape_instantiation(instance):
    assert isinstance(instance, ContainerShape)

@given(instance=AnchorContainer_strategy)
@settings(max_examples=50)
def test_anchorcontainer_instantiation(instance):
    assert isinstance(instance, AnchorContainer)

@given(instance=mm::pictograms::Connection_strategy)
@settings(max_examples=50)
def test_mm::pictograms::connection_instantiation(instance):
    assert isinstance(instance, mm::pictograms::Connection)

@given(instance=mm::pictograms::Shape_strategy)
@settings(max_examples=50)
def test_mm::pictograms::shape_instantiation(instance):
    assert isinstance(instance, mm::pictograms::Shape)

@given(instance=styles::Style_strategy)
@settings(max_examples=50)
def test_styles::style_instantiation(instance):
    assert isinstance(instance, styles::Style)

@given(instance=mm::StyleContainer_strategy)
@settings(max_examples=50)
def test_mm::stylecontainer_instantiation(instance):
    assert isinstance(instance, mm::StyleContainer)

@given(instance=PropertyContainer_strategy)
@settings(max_examples=50)
def test_propertycontainer_instantiation(instance):
    assert isinstance(instance, PropertyContainer)

@given(instance=mm::pictograms::PictogramLink_strategy)
@settings(max_examples=50)
def test_mm::pictograms::pictogramlink_instantiation(instance):
    assert isinstance(instance, mm::pictograms::PictogramLink)

@given(instance=mm::GraphicsAlgorithmContainer_strategy)
@settings(max_examples=50)
def test_mm::graphicsalgorithmcontainer_instantiation(instance):
    assert isinstance(instance, mm::GraphicsAlgorithmContainer)

@given(instance=mm::PropertyContainer_strategy)
@settings(max_examples=50)
def test_mm::propertycontainer_instantiation(instance):
    assert isinstance(instance, mm::PropertyContainer)

@given(instance=mm::Property_strategy)
@settings(max_examples=50)
def test_mm::property_instantiation(instance):
    assert isinstance(instance, mm::Property)

@given(instance=mm::Property_strategy)
def test_mm::property_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=mm::Property_strategy)
def test_mm::property_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=mm::Property_strategy)
def test_mm::property_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=mm::Property_strategy)
def test_mm::property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
