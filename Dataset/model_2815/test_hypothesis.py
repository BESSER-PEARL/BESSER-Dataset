import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fxg::FXGElement,
    fxg::GradientBevelFilter,
    fxg::GradientGlowFilter,
    Filter,
    fxg::ColorMatrixFilter,
    fxg::BevelFilter,
    fxg::DropShadowFilter,
    fxg::BlurFilter,
    fxg::RadialGradientStroke,
    fxg::LinearGradient,
    fxg::LinearGradientStroke,
    Stroke,
    fxg::SolidColorStroke,
    fxg::RadialGradient,
    Fill,
    fxg::BitmapFill,
    fxg::SolidColor,
    fxg::linkActiveFormat,
    RichTextContentContainer,
    fxg::CharacterAttributes,
    fxg::ContainerAttributes,
    fxg::ParagraphAttributes,
    RichTextContent,
    fxg::linkHoverFormat,
    fxg::span,
    fxg::tab,
    fxg::linkNormalFormat,
    fxg::a,
    fxg::rawtext,
    fxg::img,
    fxg::div,
    fxg::br,
    fxg::tcy,
    fxg::RichTextContentContainer,
    fxg::RichTextContent,
    CharacterAttributes,
    ContainerAttributes,
    ParagraphAttributes,
    fxg::p,
    Shape,
    fxg::Ellipse,
    fxg::Line,
    fxg::Rect,
    fxg::Definition,
    FXGElement,
    fxg::Transform,
    fxg::ContainerElement,
    fxg::GradientEntry,
    fxg::ColorTransform,
    fxg::Stroke,
    fxg::PlaceObject,
    fxg::BitmapImage,
    fxg::Fill,
    fxg::Matrix,
    fxg::Filter,
    fxg::RichText,
    fxg::Path,
    fxg::Shape,
    fxg::Private,
    fxg::Library,
    fxg::Group,
    fxg::Graphic,
    JustificationStyle,
    LeadingModel,
    WhitespaceCollapse,
    JustificationRule,
    Joint,
    TextRotation,
    DominantBaseline,
    DigitWidth,
    VerticalAlign,
    Kerning,
    BevelFilterType,
    ScaleMode,
    FontWeight,
    TypographicCase,
    SpreadMethod,
    AlignmentBaseline,
    InterpolationMethod,
    BreakOpportunity,
    BlockProgression,
    TextJustify,
    FillMode,
    Winding,
    Cap,
    TextAlign,
    BlendMode,
    FontStyle,
    LigatureLevel,
    LineBreak,
    MaskType,
    DigitCase,
    TextDecoration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fxg::fxgelement_is_not_abstract():
    assert not inspect.isabstract(fxg::FXGElement)


def test_fxg::fxgelement_constructor_exists():
    assert callable(fxg::FXGElement.__init__)


def test_fxg::fxgelement_constructor_args():
    sig = inspect.signature(fxg::FXGElement.__init__)
    params = list(sig.parameters.keys())



def test_fxg::gradientbevelfilter_is_not_abstract():
    assert not inspect.isabstract(fxg::GradientBevelFilter)


def test_fxg::gradientbevelfilter_constructor_exists():
    assert callable(fxg::GradientBevelFilter.__init__)


def test_fxg::gradientbevelfilter_constructor_args():
    sig = inspect.signature(fxg::GradientBevelFilter.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"
    assert "blurX" in params, "Missing parameter 'blurX'"
    assert "distance" in params, "Missing parameter 'distance'"
    assert "type" in params, "Missing parameter 'type'"
    assert "blurY" in params, "Missing parameter 'blurY'"
    assert "strength" in params, "Missing parameter 'strength'"
    assert "quality" in params, "Missing parameter 'quality'"
    assert "knockout" in params, "Missing parameter 'knockout'"

def test_fxg::gradientbevelfilter_has_angle():
    assert hasattr(fxg::GradientBevelFilter, "angle")
    descriptor = None
    for klass in fxg::GradientBevelFilter.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)

def test_fxg::gradientbevelfilter_has_blurX():
    assert hasattr(fxg::GradientBevelFilter, "blurX")
    descriptor = None
    for klass in fxg::GradientBevelFilter.__mro__:
        if "blurX" in klass.__dict__:
            descriptor = klass.__dict__["blurX"]
            break
    assert isinstance(descriptor, property)

def test_fxg::gradientbevelfilter_has_distance():
    assert hasattr(fxg::GradientBevelFilter, "distance")
    descriptor = None
    for klass in fxg::GradientBevelFilter.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)

def test_fxg::gradientbevelfilter_has_type():
    assert hasattr(fxg::GradientBevelFilter, "type")
    descriptor = None
    for klass in fxg::GradientBevelFilter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_fxg::gradientbevelfilter_has_blurY():
    assert hasattr(fxg::GradientBevelFilter, "blurY")
    descriptor = None
    for klass in fxg::GradientBevelFilter.__mro__:
        if "blurY" in klass.__dict__:
            descriptor = klass.__dict__["blurY"]
            break
    assert isinstance(descriptor, property)

def test_fxg::gradientbevelfilter_has_strength():
    assert hasattr(fxg::GradientBevelFilter, "strength")
    descriptor = None
    for klass in fxg::GradientBevelFilter.__mro__:
        if "strength" in klass.__dict__:
            descriptor = klass.__dict__["strength"]
            break
    assert isinstance(descriptor, property)

def test_fxg::gradientbevelfilter_has_quality():
    assert hasattr(fxg::GradientBevelFilter, "quality")
    descriptor = None
    for klass in fxg::GradientBevelFilter.__mro__:
        if "quality" in klass.__dict__:
            descriptor = klass.__dict__["quality"]
            break
    assert isinstance(descriptor, property)

def test_fxg::gradientbevelfilter_has_knockout():
    assert hasattr(fxg::GradientBevelFilter, "knockout")
    descriptor = None
    for klass in fxg::GradientBevelFilter.__mro__:
        if "knockout" in klass.__dict__:
            descriptor = klass.__dict__["knockout"]
            break
    assert isinstance(descriptor, property)



def test_fxg::gradientglowfilter_is_not_abstract():
    assert not inspect.isabstract(fxg::GradientGlowFilter)


def test_fxg::gradientglowfilter_constructor_exists():
    assert callable(fxg::GradientGlowFilter.__init__)


def test_fxg::gradientglowfilter_constructor_args():
    sig = inspect.signature(fxg::GradientGlowFilter.__init__)
    params = list(sig.parameters.keys())
    assert "strength" in params, "Missing parameter 'strength'"
    assert "distance" in params, "Missing parameter 'distance'"
    assert "knockout" in params, "Missing parameter 'knockout'"
    assert "blurY" in params, "Missing parameter 'blurY'"
    assert "inner" in params, "Missing parameter 'inner'"
    assert "quality" in params, "Missing parameter 'quality'"
    assert "blurX" in params, "Missing parameter 'blurX'"
    assert "angle" in params, "Missing parameter 'angle'"

def test_fxg::gradientglowfilter_has_strength():
    assert hasattr(fxg::GradientGlowFilter, "strength")
    descriptor = None
    for klass in fxg::GradientGlowFilter.__mro__:
        if "strength" in klass.__dict__:
            descriptor = klass.__dict__["strength"]
            break
    assert isinstance(descriptor, property)

def test_fxg::gradientglowfilter_has_distance():
    assert hasattr(fxg::GradientGlowFilter, "distance")
    descriptor = None
    for klass in fxg::GradientGlowFilter.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)

def test_fxg::gradientglowfilter_has_knockout():
    assert hasattr(fxg::GradientGlowFilter, "knockout")
    descriptor = None
    for klass in fxg::GradientGlowFilter.__mro__:
        if "knockout" in klass.__dict__:
            descriptor = klass.__dict__["knockout"]
            break
    assert isinstance(descriptor, property)

def test_fxg::gradientglowfilter_has_blurY():
    assert hasattr(fxg::GradientGlowFilter, "blurY")
    descriptor = None
    for klass in fxg::GradientGlowFilter.__mro__:
        if "blurY" in klass.__dict__:
            descriptor = klass.__dict__["blurY"]
            break
    assert isinstance(descriptor, property)

def test_fxg::gradientglowfilter_has_inner():
    assert hasattr(fxg::GradientGlowFilter, "inner")
    descriptor = None
    for klass in fxg::GradientGlowFilter.__mro__:
        if "inner" in klass.__dict__:
            descriptor = klass.__dict__["inner"]
            break
    assert isinstance(descriptor, property)

def test_fxg::gradientglowfilter_has_quality():
    assert hasattr(fxg::GradientGlowFilter, "quality")
    descriptor = None
    for klass in fxg::GradientGlowFilter.__mro__:
        if "quality" in klass.__dict__:
            descriptor = klass.__dict__["quality"]
            break
    assert isinstance(descriptor, property)

def test_fxg::gradientglowfilter_has_blurX():
    assert hasattr(fxg::GradientGlowFilter, "blurX")
    descriptor = None
    for klass in fxg::GradientGlowFilter.__mro__:
        if "blurX" in klass.__dict__:
            descriptor = klass.__dict__["blurX"]
            break
    assert isinstance(descriptor, property)

def test_fxg::gradientglowfilter_has_angle():
    assert hasattr(fxg::GradientGlowFilter, "angle")
    descriptor = None
    for klass in fxg::GradientGlowFilter.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_filter_is_not_abstract():
    assert not inspect.isabstract(Filter)


def test_filter_constructor_exists():
    assert callable(Filter.__init__)


def test_filter_constructor_args():
    sig = inspect.signature(Filter.__init__)
    params = list(sig.parameters.keys())



def test_fxg::colormatrixfilter_is_not_abstract():
    assert not inspect.isabstract(fxg::ColorMatrixFilter)


def test_fxg::colormatrixfilter_constructor_exists():
    assert callable(fxg::ColorMatrixFilter.__init__)


def test_fxg::colormatrixfilter_constructor_args():
    sig = inspect.signature(fxg::ColorMatrixFilter.__init__)
    params = list(sig.parameters.keys())
    assert "matrix" in params, "Missing parameter 'matrix'"

def test_fxg::colormatrixfilter_has_matrix():
    assert hasattr(fxg::ColorMatrixFilter, "matrix")
    descriptor = None
    for klass in fxg::ColorMatrixFilter.__mro__:
        if "matrix" in klass.__dict__:
            descriptor = klass.__dict__["matrix"]
            break
    assert isinstance(descriptor, property)



def test_fxg::bevelfilter_is_not_abstract():
    assert not inspect.isabstract(fxg::BevelFilter)


def test_fxg::bevelfilter_constructor_exists():
    assert callable(fxg::BevelFilter.__init__)


def test_fxg::bevelfilter_constructor_args():
    sig = inspect.signature(fxg::BevelFilter.__init__)
    params = list(sig.parameters.keys())
    assert "highlightAlpha" in params, "Missing parameter 'highlightAlpha'"
    assert "blurX" in params, "Missing parameter 'blurX'"
    assert "blurY" in params, "Missing parameter 'blurY'"
    assert "strength" in params, "Missing parameter 'strength'"
    assert "knockout" in params, "Missing parameter 'knockout'"
    assert "distance" in params, "Missing parameter 'distance'"
    assert "angle" in params, "Missing parameter 'angle'"
    assert "highlightColor" in params, "Missing parameter 'highlightColor'"
    assert "quality" in params, "Missing parameter 'quality'"
    assert "type" in params, "Missing parameter 'type'"
    assert "shadowAlpha" in params, "Missing parameter 'shadowAlpha'"
    assert "shadowColor" in params, "Missing parameter 'shadowColor'"

def test_fxg::bevelfilter_has_highlightAlpha():
    assert hasattr(fxg::BevelFilter, "highlightAlpha")
    descriptor = None
    for klass in fxg::BevelFilter.__mro__:
        if "highlightAlpha" in klass.__dict__:
            descriptor = klass.__dict__["highlightAlpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bevelfilter_has_blurX():
    assert hasattr(fxg::BevelFilter, "blurX")
    descriptor = None
    for klass in fxg::BevelFilter.__mro__:
        if "blurX" in klass.__dict__:
            descriptor = klass.__dict__["blurX"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bevelfilter_has_blurY():
    assert hasattr(fxg::BevelFilter, "blurY")
    descriptor = None
    for klass in fxg::BevelFilter.__mro__:
        if "blurY" in klass.__dict__:
            descriptor = klass.__dict__["blurY"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bevelfilter_has_strength():
    assert hasattr(fxg::BevelFilter, "strength")
    descriptor = None
    for klass in fxg::BevelFilter.__mro__:
        if "strength" in klass.__dict__:
            descriptor = klass.__dict__["strength"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bevelfilter_has_knockout():
    assert hasattr(fxg::BevelFilter, "knockout")
    descriptor = None
    for klass in fxg::BevelFilter.__mro__:
        if "knockout" in klass.__dict__:
            descriptor = klass.__dict__["knockout"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bevelfilter_has_distance():
    assert hasattr(fxg::BevelFilter, "distance")
    descriptor = None
    for klass in fxg::BevelFilter.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bevelfilter_has_angle():
    assert hasattr(fxg::BevelFilter, "angle")
    descriptor = None
    for klass in fxg::BevelFilter.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bevelfilter_has_highlightColor():
    assert hasattr(fxg::BevelFilter, "highlightColor")
    descriptor = None
    for klass in fxg::BevelFilter.__mro__:
        if "highlightColor" in klass.__dict__:
            descriptor = klass.__dict__["highlightColor"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bevelfilter_has_quality():
    assert hasattr(fxg::BevelFilter, "quality")
    descriptor = None
    for klass in fxg::BevelFilter.__mro__:
        if "quality" in klass.__dict__:
            descriptor = klass.__dict__["quality"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bevelfilter_has_type():
    assert hasattr(fxg::BevelFilter, "type")
    descriptor = None
    for klass in fxg::BevelFilter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bevelfilter_has_shadowAlpha():
    assert hasattr(fxg::BevelFilter, "shadowAlpha")
    descriptor = None
    for klass in fxg::BevelFilter.__mro__:
        if "shadowAlpha" in klass.__dict__:
            descriptor = klass.__dict__["shadowAlpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bevelfilter_has_shadowColor():
    assert hasattr(fxg::BevelFilter, "shadowColor")
    descriptor = None
    for klass in fxg::BevelFilter.__mro__:
        if "shadowColor" in klass.__dict__:
            descriptor = klass.__dict__["shadowColor"]
            break
    assert isinstance(descriptor, property)



def test_fxg::dropshadowfilter_is_not_abstract():
    assert not inspect.isabstract(fxg::DropShadowFilter)


def test_fxg::dropshadowfilter_constructor_exists():
    assert callable(fxg::DropShadowFilter.__init__)


def test_fxg::dropshadowfilter_constructor_args():
    sig = inspect.signature(fxg::DropShadowFilter.__init__)
    params = list(sig.parameters.keys())
    assert "inner" in params, "Missing parameter 'inner'"
    assert "distance" in params, "Missing parameter 'distance'"
    assert "hideObject" in params, "Missing parameter 'hideObject'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "quality" in params, "Missing parameter 'quality'"
    assert "strength" in params, "Missing parameter 'strength'"
    assert "knockout" in params, "Missing parameter 'knockout'"
    assert "blurX" in params, "Missing parameter 'blurX'"
    assert "blurY" in params, "Missing parameter 'blurY'"
    assert "color" in params, "Missing parameter 'color'"
    assert "angle" in params, "Missing parameter 'angle'"

def test_fxg::dropshadowfilter_has_inner():
    assert hasattr(fxg::DropShadowFilter, "inner")
    descriptor = None
    for klass in fxg::DropShadowFilter.__mro__:
        if "inner" in klass.__dict__:
            descriptor = klass.__dict__["inner"]
            break
    assert isinstance(descriptor, property)

def test_fxg::dropshadowfilter_has_distance():
    assert hasattr(fxg::DropShadowFilter, "distance")
    descriptor = None
    for klass in fxg::DropShadowFilter.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)

def test_fxg::dropshadowfilter_has_hideObject():
    assert hasattr(fxg::DropShadowFilter, "hideObject")
    descriptor = None
    for klass in fxg::DropShadowFilter.__mro__:
        if "hideObject" in klass.__dict__:
            descriptor = klass.__dict__["hideObject"]
            break
    assert isinstance(descriptor, property)

def test_fxg::dropshadowfilter_has_alpha():
    assert hasattr(fxg::DropShadowFilter, "alpha")
    descriptor = None
    for klass in fxg::DropShadowFilter.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg::dropshadowfilter_has_quality():
    assert hasattr(fxg::DropShadowFilter, "quality")
    descriptor = None
    for klass in fxg::DropShadowFilter.__mro__:
        if "quality" in klass.__dict__:
            descriptor = klass.__dict__["quality"]
            break
    assert isinstance(descriptor, property)

def test_fxg::dropshadowfilter_has_strength():
    assert hasattr(fxg::DropShadowFilter, "strength")
    descriptor = None
    for klass in fxg::DropShadowFilter.__mro__:
        if "strength" in klass.__dict__:
            descriptor = klass.__dict__["strength"]
            break
    assert isinstance(descriptor, property)

def test_fxg::dropshadowfilter_has_knockout():
    assert hasattr(fxg::DropShadowFilter, "knockout")
    descriptor = None
    for klass in fxg::DropShadowFilter.__mro__:
        if "knockout" in klass.__dict__:
            descriptor = klass.__dict__["knockout"]
            break
    assert isinstance(descriptor, property)

def test_fxg::dropshadowfilter_has_blurX():
    assert hasattr(fxg::DropShadowFilter, "blurX")
    descriptor = None
    for klass in fxg::DropShadowFilter.__mro__:
        if "blurX" in klass.__dict__:
            descriptor = klass.__dict__["blurX"]
            break
    assert isinstance(descriptor, property)

def test_fxg::dropshadowfilter_has_blurY():
    assert hasattr(fxg::DropShadowFilter, "blurY")
    descriptor = None
    for klass in fxg::DropShadowFilter.__mro__:
        if "blurY" in klass.__dict__:
            descriptor = klass.__dict__["blurY"]
            break
    assert isinstance(descriptor, property)

def test_fxg::dropshadowfilter_has_color():
    assert hasattr(fxg::DropShadowFilter, "color")
    descriptor = None
    for klass in fxg::DropShadowFilter.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_fxg::dropshadowfilter_has_angle():
    assert hasattr(fxg::DropShadowFilter, "angle")
    descriptor = None
    for klass in fxg::DropShadowFilter.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_fxg::blurfilter_is_not_abstract():
    assert not inspect.isabstract(fxg::BlurFilter)


def test_fxg::blurfilter_constructor_exists():
    assert callable(fxg::BlurFilter.__init__)


def test_fxg::blurfilter_constructor_args():
    sig = inspect.signature(fxg::BlurFilter.__init__)
    params = list(sig.parameters.keys())
    assert "quality" in params, "Missing parameter 'quality'"
    assert "blurY" in params, "Missing parameter 'blurY'"
    assert "blurX" in params, "Missing parameter 'blurX'"

def test_fxg::blurfilter_has_quality():
    assert hasattr(fxg::BlurFilter, "quality")
    descriptor = None
    for klass in fxg::BlurFilter.__mro__:
        if "quality" in klass.__dict__:
            descriptor = klass.__dict__["quality"]
            break
    assert isinstance(descriptor, property)

def test_fxg::blurfilter_has_blurY():
    assert hasattr(fxg::BlurFilter, "blurY")
    descriptor = None
    for klass in fxg::BlurFilter.__mro__:
        if "blurY" in klass.__dict__:
            descriptor = klass.__dict__["blurY"]
            break
    assert isinstance(descriptor, property)

def test_fxg::blurfilter_has_blurX():
    assert hasattr(fxg::BlurFilter, "blurX")
    descriptor = None
    for klass in fxg::BlurFilter.__mro__:
        if "blurX" in klass.__dict__:
            descriptor = klass.__dict__["blurX"]
            break
    assert isinstance(descriptor, property)



def test_fxg::radialgradientstroke_is_not_abstract():
    assert not inspect.isabstract(fxg::RadialGradientStroke)


def test_fxg::radialgradientstroke_constructor_exists():
    assert callable(fxg::RadialGradientStroke.__init__)


def test_fxg::radialgradientstroke_constructor_args():
    sig = inspect.signature(fxg::RadialGradientStroke.__init__)
    params = list(sig.parameters.keys())
    assert "caps" in params, "Missing parameter 'caps'"
    assert "spreadMethod" in params, "Missing parameter 'spreadMethod'"
    assert "pixelHinting" in params, "Missing parameter 'pixelHinting'"
    assert "y" in params, "Missing parameter 'y'"
    assert "focalPointRatio" in params, "Missing parameter 'focalPointRatio'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "interpolationMethod" in params, "Missing parameter 'interpolationMethod'"
    assert "x" in params, "Missing parameter 'x'"
    assert "scaleMode" in params, "Missing parameter 'scaleMode'"
    assert "joints" in params, "Missing parameter 'joints'"
    assert "miterLimit" in params, "Missing parameter 'miterLimit'"

def test_fxg::radialgradientstroke_has_caps():
    assert hasattr(fxg::RadialGradientStroke, "caps")
    descriptor = None
    for klass in fxg::RadialGradientStroke.__mro__:
        if "caps" in klass.__dict__:
            descriptor = klass.__dict__["caps"]
            break
    assert isinstance(descriptor, property)

def test_fxg::radialgradientstroke_has_spreadMethod():
    assert hasattr(fxg::RadialGradientStroke, "spreadMethod")
    descriptor = None
    for klass in fxg::RadialGradientStroke.__mro__:
        if "spreadMethod" in klass.__dict__:
            descriptor = klass.__dict__["spreadMethod"]
            break
    assert isinstance(descriptor, property)

def test_fxg::radialgradientstroke_has_pixelHinting():
    assert hasattr(fxg::RadialGradientStroke, "pixelHinting")
    descriptor = None
    for klass in fxg::RadialGradientStroke.__mro__:
        if "pixelHinting" in klass.__dict__:
            descriptor = klass.__dict__["pixelHinting"]
            break
    assert isinstance(descriptor, property)

def test_fxg::radialgradientstroke_has_y():
    assert hasattr(fxg::RadialGradientStroke, "y")
    descriptor = None
    for klass in fxg::RadialGradientStroke.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg::radialgradientstroke_has_focalPointRatio():
    assert hasattr(fxg::RadialGradientStroke, "focalPointRatio")
    descriptor = None
    for klass in fxg::RadialGradientStroke.__mro__:
        if "focalPointRatio" in klass.__dict__:
            descriptor = klass.__dict__["focalPointRatio"]
            break
    assert isinstance(descriptor, property)

def test_fxg::radialgradientstroke_has_rotation():
    assert hasattr(fxg::RadialGradientStroke, "rotation")
    descriptor = None
    for klass in fxg::RadialGradientStroke.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg::radialgradientstroke_has_scaleX():
    assert hasattr(fxg::RadialGradientStroke, "scaleX")
    descriptor = None
    for klass in fxg::RadialGradientStroke.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)

def test_fxg::radialgradientstroke_has_scaleY():
    assert hasattr(fxg::RadialGradientStroke, "scaleY")
    descriptor = None
    for klass in fxg::RadialGradientStroke.__mro__:
        if "scaleY" in klass.__dict__:
            descriptor = klass.__dict__["scaleY"]
            break
    assert isinstance(descriptor, property)

def test_fxg::radialgradientstroke_has_weight():
    assert hasattr(fxg::RadialGradientStroke, "weight")
    descriptor = None
    for klass in fxg::RadialGradientStroke.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_fxg::radialgradientstroke_has_interpolationMethod():
    assert hasattr(fxg::RadialGradientStroke, "interpolationMethod")
    descriptor = None
    for klass in fxg::RadialGradientStroke.__mro__:
        if "interpolationMethod" in klass.__dict__:
            descriptor = klass.__dict__["interpolationMethod"]
            break
    assert isinstance(descriptor, property)

def test_fxg::radialgradientstroke_has_x():
    assert hasattr(fxg::RadialGradientStroke, "x")
    descriptor = None
    for klass in fxg::RadialGradientStroke.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fxg::radialgradientstroke_has_scaleMode():
    assert hasattr(fxg::RadialGradientStroke, "scaleMode")
    descriptor = None
    for klass in fxg::RadialGradientStroke.__mro__:
        if "scaleMode" in klass.__dict__:
            descriptor = klass.__dict__["scaleMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg::radialgradientstroke_has_joints():
    assert hasattr(fxg::RadialGradientStroke, "joints")
    descriptor = None
    for klass in fxg::RadialGradientStroke.__mro__:
        if "joints" in klass.__dict__:
            descriptor = klass.__dict__["joints"]
            break
    assert isinstance(descriptor, property)

def test_fxg::radialgradientstroke_has_miterLimit():
    assert hasattr(fxg::RadialGradientStroke, "miterLimit")
    descriptor = None
    for klass in fxg::RadialGradientStroke.__mro__:
        if "miterLimit" in klass.__dict__:
            descriptor = klass.__dict__["miterLimit"]
            break
    assert isinstance(descriptor, property)



def test_fxg::lineargradient_is_not_abstract():
    assert not inspect.isabstract(fxg::LinearGradient)


def test_fxg::lineargradient_constructor_exists():
    assert callable(fxg::LinearGradient.__init__)


def test_fxg::lineargradient_constructor_args():
    sig = inspect.signature(fxg::LinearGradient.__init__)
    params = list(sig.parameters.keys())
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "interpolationMethod" in params, "Missing parameter 'interpolationMethod'"
    assert "spreadMethod" in params, "Missing parameter 'spreadMethod'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_fxg::lineargradient_has_rotation():
    assert hasattr(fxg::LinearGradient, "rotation")
    descriptor = None
    for klass in fxg::LinearGradient.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg::lineargradient_has_scaleX():
    assert hasattr(fxg::LinearGradient, "scaleX")
    descriptor = None
    for klass in fxg::LinearGradient.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)

def test_fxg::lineargradient_has_interpolationMethod():
    assert hasattr(fxg::LinearGradient, "interpolationMethod")
    descriptor = None
    for klass in fxg::LinearGradient.__mro__:
        if "interpolationMethod" in klass.__dict__:
            descriptor = klass.__dict__["interpolationMethod"]
            break
    assert isinstance(descriptor, property)

def test_fxg::lineargradient_has_spreadMethod():
    assert hasattr(fxg::LinearGradient, "spreadMethod")
    descriptor = None
    for klass in fxg::LinearGradient.__mro__:
        if "spreadMethod" in klass.__dict__:
            descriptor = klass.__dict__["spreadMethod"]
            break
    assert isinstance(descriptor, property)

def test_fxg::lineargradient_has_y():
    assert hasattr(fxg::LinearGradient, "y")
    descriptor = None
    for klass in fxg::LinearGradient.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg::lineargradient_has_x():
    assert hasattr(fxg::LinearGradient, "x")
    descriptor = None
    for klass in fxg::LinearGradient.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_fxg::lineargradientstroke_is_not_abstract():
    assert not inspect.isabstract(fxg::LinearGradientStroke)


def test_fxg::lineargradientstroke_constructor_exists():
    assert callable(fxg::LinearGradientStroke.__init__)


def test_fxg::lineargradientstroke_constructor_args():
    sig = inspect.signature(fxg::LinearGradientStroke.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "joints" in params, "Missing parameter 'joints'"
    assert "scaleMode" in params, "Missing parameter 'scaleMode'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "miterLimit" in params, "Missing parameter 'miterLimit'"
    assert "x" in params, "Missing parameter 'x'"
    assert "spreadMethod" in params, "Missing parameter 'spreadMethod'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "caps" in params, "Missing parameter 'caps'"
    assert "interpolationMethod" in params, "Missing parameter 'interpolationMethod'"
    assert "pixelHinting" in params, "Missing parameter 'pixelHinting'"
    assert "y" in params, "Missing parameter 'y'"

def test_fxg::lineargradientstroke_has_weight():
    assert hasattr(fxg::LinearGradientStroke, "weight")
    descriptor = None
    for klass in fxg::LinearGradientStroke.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_fxg::lineargradientstroke_has_joints():
    assert hasattr(fxg::LinearGradientStroke, "joints")
    descriptor = None
    for klass in fxg::LinearGradientStroke.__mro__:
        if "joints" in klass.__dict__:
            descriptor = klass.__dict__["joints"]
            break
    assert isinstance(descriptor, property)

def test_fxg::lineargradientstroke_has_scaleMode():
    assert hasattr(fxg::LinearGradientStroke, "scaleMode")
    descriptor = None
    for klass in fxg::LinearGradientStroke.__mro__:
        if "scaleMode" in klass.__dict__:
            descriptor = klass.__dict__["scaleMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg::lineargradientstroke_has_scaleX():
    assert hasattr(fxg::LinearGradientStroke, "scaleX")
    descriptor = None
    for klass in fxg::LinearGradientStroke.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)

def test_fxg::lineargradientstroke_has_miterLimit():
    assert hasattr(fxg::LinearGradientStroke, "miterLimit")
    descriptor = None
    for klass in fxg::LinearGradientStroke.__mro__:
        if "miterLimit" in klass.__dict__:
            descriptor = klass.__dict__["miterLimit"]
            break
    assert isinstance(descriptor, property)

def test_fxg::lineargradientstroke_has_x():
    assert hasattr(fxg::LinearGradientStroke, "x")
    descriptor = None
    for klass in fxg::LinearGradientStroke.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fxg::lineargradientstroke_has_spreadMethod():
    assert hasattr(fxg::LinearGradientStroke, "spreadMethod")
    descriptor = None
    for klass in fxg::LinearGradientStroke.__mro__:
        if "spreadMethod" in klass.__dict__:
            descriptor = klass.__dict__["spreadMethod"]
            break
    assert isinstance(descriptor, property)

def test_fxg::lineargradientstroke_has_rotation():
    assert hasattr(fxg::LinearGradientStroke, "rotation")
    descriptor = None
    for klass in fxg::LinearGradientStroke.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg::lineargradientstroke_has_caps():
    assert hasattr(fxg::LinearGradientStroke, "caps")
    descriptor = None
    for klass in fxg::LinearGradientStroke.__mro__:
        if "caps" in klass.__dict__:
            descriptor = klass.__dict__["caps"]
            break
    assert isinstance(descriptor, property)

def test_fxg::lineargradientstroke_has_interpolationMethod():
    assert hasattr(fxg::LinearGradientStroke, "interpolationMethod")
    descriptor = None
    for klass in fxg::LinearGradientStroke.__mro__:
        if "interpolationMethod" in klass.__dict__:
            descriptor = klass.__dict__["interpolationMethod"]
            break
    assert isinstance(descriptor, property)

def test_fxg::lineargradientstroke_has_pixelHinting():
    assert hasattr(fxg::LinearGradientStroke, "pixelHinting")
    descriptor = None
    for klass in fxg::LinearGradientStroke.__mro__:
        if "pixelHinting" in klass.__dict__:
            descriptor = klass.__dict__["pixelHinting"]
            break
    assert isinstance(descriptor, property)

def test_fxg::lineargradientstroke_has_y():
    assert hasattr(fxg::LinearGradientStroke, "y")
    descriptor = None
    for klass in fxg::LinearGradientStroke.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_stroke_is_not_abstract():
    assert not inspect.isabstract(Stroke)


def test_stroke_constructor_exists():
    assert callable(Stroke.__init__)


def test_stroke_constructor_args():
    sig = inspect.signature(Stroke.__init__)
    params = list(sig.parameters.keys())



def test_fxg::solidcolorstroke_is_not_abstract():
    assert not inspect.isabstract(fxg::SolidColorStroke)


def test_fxg::solidcolorstroke_constructor_exists():
    assert callable(fxg::SolidColorStroke.__init__)


def test_fxg::solidcolorstroke_constructor_args():
    sig = inspect.signature(fxg::SolidColorStroke.__init__)
    params = list(sig.parameters.keys())
    assert "miterLimit" in params, "Missing parameter 'miterLimit'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "caps" in params, "Missing parameter 'caps'"
    assert "scaleMode" in params, "Missing parameter 'scaleMode'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "color" in params, "Missing parameter 'color'"
    assert "pixelHinting" in params, "Missing parameter 'pixelHinting'"
    assert "joints" in params, "Missing parameter 'joints'"

def test_fxg::solidcolorstroke_has_miterLimit():
    assert hasattr(fxg::SolidColorStroke, "miterLimit")
    descriptor = None
    for klass in fxg::SolidColorStroke.__mro__:
        if "miterLimit" in klass.__dict__:
            descriptor = klass.__dict__["miterLimit"]
            break
    assert isinstance(descriptor, property)

def test_fxg::solidcolorstroke_has_alpha():
    assert hasattr(fxg::SolidColorStroke, "alpha")
    descriptor = None
    for klass in fxg::SolidColorStroke.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg::solidcolorstroke_has_caps():
    assert hasattr(fxg::SolidColorStroke, "caps")
    descriptor = None
    for klass in fxg::SolidColorStroke.__mro__:
        if "caps" in klass.__dict__:
            descriptor = klass.__dict__["caps"]
            break
    assert isinstance(descriptor, property)

def test_fxg::solidcolorstroke_has_scaleMode():
    assert hasattr(fxg::SolidColorStroke, "scaleMode")
    descriptor = None
    for klass in fxg::SolidColorStroke.__mro__:
        if "scaleMode" in klass.__dict__:
            descriptor = klass.__dict__["scaleMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg::solidcolorstroke_has_weight():
    assert hasattr(fxg::SolidColorStroke, "weight")
    descriptor = None
    for klass in fxg::SolidColorStroke.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_fxg::solidcolorstroke_has_color():
    assert hasattr(fxg::SolidColorStroke, "color")
    descriptor = None
    for klass in fxg::SolidColorStroke.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_fxg::solidcolorstroke_has_pixelHinting():
    assert hasattr(fxg::SolidColorStroke, "pixelHinting")
    descriptor = None
    for klass in fxg::SolidColorStroke.__mro__:
        if "pixelHinting" in klass.__dict__:
            descriptor = klass.__dict__["pixelHinting"]
            break
    assert isinstance(descriptor, property)

def test_fxg::solidcolorstroke_has_joints():
    assert hasattr(fxg::SolidColorStroke, "joints")
    descriptor = None
    for klass in fxg::SolidColorStroke.__mro__:
        if "joints" in klass.__dict__:
            descriptor = klass.__dict__["joints"]
            break
    assert isinstance(descriptor, property)



def test_fxg::radialgradient_is_not_abstract():
    assert not inspect.isabstract(fxg::RadialGradient)


def test_fxg::radialgradient_constructor_exists():
    assert callable(fxg::RadialGradient.__init__)


def test_fxg::radialgradient_constructor_args():
    sig = inspect.signature(fxg::RadialGradient.__init__)
    params = list(sig.parameters.keys())
    assert "focalPointRatio" in params, "Missing parameter 'focalPointRatio'"
    assert "interpolationMethod" in params, "Missing parameter 'interpolationMethod'"
    assert "y" in params, "Missing parameter 'y'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "x" in params, "Missing parameter 'x'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "spreadMethod" in params, "Missing parameter 'spreadMethod'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"

def test_fxg::radialgradient_has_focalPointRatio():
    assert hasattr(fxg::RadialGradient, "focalPointRatio")
    descriptor = None
    for klass in fxg::RadialGradient.__mro__:
        if "focalPointRatio" in klass.__dict__:
            descriptor = klass.__dict__["focalPointRatio"]
            break
    assert isinstance(descriptor, property)

def test_fxg::radialgradient_has_interpolationMethod():
    assert hasattr(fxg::RadialGradient, "interpolationMethod")
    descriptor = None
    for klass in fxg::RadialGradient.__mro__:
        if "interpolationMethod" in klass.__dict__:
            descriptor = klass.__dict__["interpolationMethod"]
            break
    assert isinstance(descriptor, property)

def test_fxg::radialgradient_has_y():
    assert hasattr(fxg::RadialGradient, "y")
    descriptor = None
    for klass in fxg::RadialGradient.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg::radialgradient_has_scaleY():
    assert hasattr(fxg::RadialGradient, "scaleY")
    descriptor = None
    for klass in fxg::RadialGradient.__mro__:
        if "scaleY" in klass.__dict__:
            descriptor = klass.__dict__["scaleY"]
            break
    assert isinstance(descriptor, property)

def test_fxg::radialgradient_has_x():
    assert hasattr(fxg::RadialGradient, "x")
    descriptor = None
    for klass in fxg::RadialGradient.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fxg::radialgradient_has_rotation():
    assert hasattr(fxg::RadialGradient, "rotation")
    descriptor = None
    for klass in fxg::RadialGradient.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg::radialgradient_has_spreadMethod():
    assert hasattr(fxg::RadialGradient, "spreadMethod")
    descriptor = None
    for klass in fxg::RadialGradient.__mro__:
        if "spreadMethod" in klass.__dict__:
            descriptor = klass.__dict__["spreadMethod"]
            break
    assert isinstance(descriptor, property)

def test_fxg::radialgradient_has_scaleX():
    assert hasattr(fxg::RadialGradient, "scaleX")
    descriptor = None
    for klass in fxg::RadialGradient.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)



def test_fill_is_not_abstract():
    assert not inspect.isabstract(Fill)


def test_fill_constructor_exists():
    assert callable(Fill.__init__)


def test_fill_constructor_args():
    sig = inspect.signature(Fill.__init__)
    params = list(sig.parameters.keys())



def test_fxg::bitmapfill_is_not_abstract():
    assert not inspect.isabstract(fxg::BitmapFill)


def test_fxg::bitmapfill_constructor_exists():
    assert callable(fxg::BitmapFill.__init__)


def test_fxg::bitmapfill_constructor_args():
    sig = inspect.signature(fxg::BitmapFill.__init__)
    params = list(sig.parameters.keys())
    assert "fillMode" in params, "Missing parameter 'fillMode'"
    assert "x" in params, "Missing parameter 'x'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "y" in params, "Missing parameter 'y'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "source" in params, "Missing parameter 'source'"
    assert "rotation" in params, "Missing parameter 'rotation'"

def test_fxg::bitmapfill_has_fillMode():
    assert hasattr(fxg::BitmapFill, "fillMode")
    descriptor = None
    for klass in fxg::BitmapFill.__mro__:
        if "fillMode" in klass.__dict__:
            descriptor = klass.__dict__["fillMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bitmapfill_has_x():
    assert hasattr(fxg::BitmapFill, "x")
    descriptor = None
    for klass in fxg::BitmapFill.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bitmapfill_has_scaleY():
    assert hasattr(fxg::BitmapFill, "scaleY")
    descriptor = None
    for klass in fxg::BitmapFill.__mro__:
        if "scaleY" in klass.__dict__:
            descriptor = klass.__dict__["scaleY"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bitmapfill_has_y():
    assert hasattr(fxg::BitmapFill, "y")
    descriptor = None
    for klass in fxg::BitmapFill.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bitmapfill_has_scaleX():
    assert hasattr(fxg::BitmapFill, "scaleX")
    descriptor = None
    for klass in fxg::BitmapFill.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bitmapfill_has_source():
    assert hasattr(fxg::BitmapFill, "source")
    descriptor = None
    for klass in fxg::BitmapFill.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bitmapfill_has_rotation():
    assert hasattr(fxg::BitmapFill, "rotation")
    descriptor = None
    for klass in fxg::BitmapFill.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)



def test_fxg::solidcolor_is_not_abstract():
    assert not inspect.isabstract(fxg::SolidColor)


def test_fxg::solidcolor_constructor_exists():
    assert callable(fxg::SolidColor.__init__)


def test_fxg::solidcolor_constructor_args():
    sig = inspect.signature(fxg::SolidColor.__init__)
    params = list(sig.parameters.keys())
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "color" in params, "Missing parameter 'color'"

def test_fxg::solidcolor_has_alpha():
    assert hasattr(fxg::SolidColor, "alpha")
    descriptor = None
    for klass in fxg::SolidColor.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg::solidcolor_has_color():
    assert hasattr(fxg::SolidColor, "color")
    descriptor = None
    for klass in fxg::SolidColor.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_fxg::linkactiveformat_is_not_abstract():
    assert not inspect.isabstract(fxg::linkActiveFormat)


def test_fxg::linkactiveformat_constructor_exists():
    assert callable(fxg::linkActiveFormat.__init__)


def test_fxg::linkactiveformat_constructor_args():
    sig = inspect.signature(fxg::linkActiveFormat.__init__)
    params = list(sig.parameters.keys())



def test_richtextcontentcontainer_is_not_abstract():
    assert not inspect.isabstract(RichTextContentContainer)


def test_richtextcontentcontainer_constructor_exists():
    assert callable(RichTextContentContainer.__init__)


def test_richtextcontentcontainer_constructor_args():
    sig = inspect.signature(RichTextContentContainer.__init__)
    params = list(sig.parameters.keys())



def test_fxg::characterattributes_is_not_abstract():
    assert not inspect.isabstract(fxg::CharacterAttributes)


def test_fxg::characterattributes_constructor_exists():
    assert callable(fxg::CharacterAttributes.__init__)


def test_fxg::characterattributes_constructor_args():
    sig = inspect.signature(fxg::CharacterAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "locale" in params, "Missing parameter 'locale'"
    assert "lineHeight" in params, "Missing parameter 'lineHeight'"
    assert "fontWeight" in params, "Missing parameter 'fontWeight'"
    assert "textRotation" in params, "Missing parameter 'textRotation'"
    assert "trackingRight" in params, "Missing parameter 'trackingRight'"
    assert "typographicCase" in params, "Missing parameter 'typographicCase'"
    assert "baselineShift" in params, "Missing parameter 'baselineShift'"
    assert "trackingLeft" in params, "Missing parameter 'trackingLeft'"
    assert "dominantBaseline" in params, "Missing parameter 'dominantBaseline'"
    assert "breakOpportunity" in params, "Missing parameter 'breakOpportunity'"
    assert "digitCase" in params, "Missing parameter 'digitCase'"
    assert "lineThrough" in params, "Missing parameter 'lineThrough'"
    assert "whiteSpaceCollapse" in params, "Missing parameter 'whiteSpaceCollapse'"
    assert "fontStyle" in params, "Missing parameter 'fontStyle'"
    assert "fontSize" in params, "Missing parameter 'fontSize'"
    assert "textAlpha" in params, "Missing parameter 'textAlpha'"
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"
    assert "kerning" in params, "Missing parameter 'kerning'"
    assert "backgroundAlpha" in params, "Missing parameter 'backgroundAlpha'"
    assert "digitWidth" in params, "Missing parameter 'digitWidth'"
    assert "ligatureLevel" in params, "Missing parameter 'ligatureLevel'"
    assert "textDecoration" in params, "Missing parameter 'textDecoration'"
    assert "alignmentBaseline" in params, "Missing parameter 'alignmentBaseline'"
    assert "fontFamily" in params, "Missing parameter 'fontFamily'"

def test_fxg::characterattributes_has_color():
    assert hasattr(fxg::CharacterAttributes, "color")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_locale():
    assert hasattr(fxg::CharacterAttributes, "locale")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "locale" in klass.__dict__:
            descriptor = klass.__dict__["locale"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_lineHeight():
    assert hasattr(fxg::CharacterAttributes, "lineHeight")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "lineHeight" in klass.__dict__:
            descriptor = klass.__dict__["lineHeight"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_fontWeight():
    assert hasattr(fxg::CharacterAttributes, "fontWeight")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "fontWeight" in klass.__dict__:
            descriptor = klass.__dict__["fontWeight"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_textRotation():
    assert hasattr(fxg::CharacterAttributes, "textRotation")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "textRotation" in klass.__dict__:
            descriptor = klass.__dict__["textRotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_trackingRight():
    assert hasattr(fxg::CharacterAttributes, "trackingRight")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "trackingRight" in klass.__dict__:
            descriptor = klass.__dict__["trackingRight"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_typographicCase():
    assert hasattr(fxg::CharacterAttributes, "typographicCase")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "typographicCase" in klass.__dict__:
            descriptor = klass.__dict__["typographicCase"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_baselineShift():
    assert hasattr(fxg::CharacterAttributes, "baselineShift")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "baselineShift" in klass.__dict__:
            descriptor = klass.__dict__["baselineShift"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_trackingLeft():
    assert hasattr(fxg::CharacterAttributes, "trackingLeft")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "trackingLeft" in klass.__dict__:
            descriptor = klass.__dict__["trackingLeft"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_dominantBaseline():
    assert hasattr(fxg::CharacterAttributes, "dominantBaseline")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "dominantBaseline" in klass.__dict__:
            descriptor = klass.__dict__["dominantBaseline"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_breakOpportunity():
    assert hasattr(fxg::CharacterAttributes, "breakOpportunity")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "breakOpportunity" in klass.__dict__:
            descriptor = klass.__dict__["breakOpportunity"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_digitCase():
    assert hasattr(fxg::CharacterAttributes, "digitCase")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "digitCase" in klass.__dict__:
            descriptor = klass.__dict__["digitCase"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_lineThrough():
    assert hasattr(fxg::CharacterAttributes, "lineThrough")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "lineThrough" in klass.__dict__:
            descriptor = klass.__dict__["lineThrough"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_whiteSpaceCollapse():
    assert hasattr(fxg::CharacterAttributes, "whiteSpaceCollapse")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "whiteSpaceCollapse" in klass.__dict__:
            descriptor = klass.__dict__["whiteSpaceCollapse"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_fontStyle():
    assert hasattr(fxg::CharacterAttributes, "fontStyle")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "fontStyle" in klass.__dict__:
            descriptor = klass.__dict__["fontStyle"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_fontSize():
    assert hasattr(fxg::CharacterAttributes, "fontSize")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "fontSize" in klass.__dict__:
            descriptor = klass.__dict__["fontSize"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_textAlpha():
    assert hasattr(fxg::CharacterAttributes, "textAlpha")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "textAlpha" in klass.__dict__:
            descriptor = klass.__dict__["textAlpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_backgroundColor():
    assert hasattr(fxg::CharacterAttributes, "backgroundColor")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "backgroundColor" in klass.__dict__:
            descriptor = klass.__dict__["backgroundColor"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_kerning():
    assert hasattr(fxg::CharacterAttributes, "kerning")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "kerning" in klass.__dict__:
            descriptor = klass.__dict__["kerning"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_backgroundAlpha():
    assert hasattr(fxg::CharacterAttributes, "backgroundAlpha")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "backgroundAlpha" in klass.__dict__:
            descriptor = klass.__dict__["backgroundAlpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_digitWidth():
    assert hasattr(fxg::CharacterAttributes, "digitWidth")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "digitWidth" in klass.__dict__:
            descriptor = klass.__dict__["digitWidth"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_ligatureLevel():
    assert hasattr(fxg::CharacterAttributes, "ligatureLevel")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "ligatureLevel" in klass.__dict__:
            descriptor = klass.__dict__["ligatureLevel"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_textDecoration():
    assert hasattr(fxg::CharacterAttributes, "textDecoration")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "textDecoration" in klass.__dict__:
            descriptor = klass.__dict__["textDecoration"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_alignmentBaseline():
    assert hasattr(fxg::CharacterAttributes, "alignmentBaseline")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "alignmentBaseline" in klass.__dict__:
            descriptor = klass.__dict__["alignmentBaseline"]
            break
    assert isinstance(descriptor, property)

def test_fxg::characterattributes_has_fontFamily():
    assert hasattr(fxg::CharacterAttributes, "fontFamily")
    descriptor = None
    for klass in fxg::CharacterAttributes.__mro__:
        if "fontFamily" in klass.__dict__:
            descriptor = klass.__dict__["fontFamily"]
            break
    assert isinstance(descriptor, property)



def test_fxg::containerattributes_is_not_abstract():
    assert not inspect.isabstract(fxg::ContainerAttributes)


def test_fxg::containerattributes_constructor_exists():
    assert callable(fxg::ContainerAttributes.__init__)


def test_fxg::containerattributes_constructor_args():
    sig = inspect.signature(fxg::ContainerAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "paddingLeft" in params, "Missing parameter 'paddingLeft'"
    assert "columnGap" in params, "Missing parameter 'columnGap'"
    assert "columnWidth" in params, "Missing parameter 'columnWidth'"
    assert "firstBaselineOffset" in params, "Missing parameter 'firstBaselineOffset'"
    assert "verticalAlign" in params, "Missing parameter 'verticalAlign'"
    assert "lineBreak" in params, "Missing parameter 'lineBreak'"
    assert "paddingBottom" in params, "Missing parameter 'paddingBottom'"
    assert "paddingRight" in params, "Missing parameter 'paddingRight'"
    assert "blockProgression" in params, "Missing parameter 'blockProgression'"
    assert "paddingTop" in params, "Missing parameter 'paddingTop'"
    assert "columnCount" in params, "Missing parameter 'columnCount'"

def test_fxg::containerattributes_has_paddingLeft():
    assert hasattr(fxg::ContainerAttributes, "paddingLeft")
    descriptor = None
    for klass in fxg::ContainerAttributes.__mro__:
        if "paddingLeft" in klass.__dict__:
            descriptor = klass.__dict__["paddingLeft"]
            break
    assert isinstance(descriptor, property)

def test_fxg::containerattributes_has_columnGap():
    assert hasattr(fxg::ContainerAttributes, "columnGap")
    descriptor = None
    for klass in fxg::ContainerAttributes.__mro__:
        if "columnGap" in klass.__dict__:
            descriptor = klass.__dict__["columnGap"]
            break
    assert isinstance(descriptor, property)

def test_fxg::containerattributes_has_columnWidth():
    assert hasattr(fxg::ContainerAttributes, "columnWidth")
    descriptor = None
    for klass in fxg::ContainerAttributes.__mro__:
        if "columnWidth" in klass.__dict__:
            descriptor = klass.__dict__["columnWidth"]
            break
    assert isinstance(descriptor, property)

def test_fxg::containerattributes_has_firstBaselineOffset():
    assert hasattr(fxg::ContainerAttributes, "firstBaselineOffset")
    descriptor = None
    for klass in fxg::ContainerAttributes.__mro__:
        if "firstBaselineOffset" in klass.__dict__:
            descriptor = klass.__dict__["firstBaselineOffset"]
            break
    assert isinstance(descriptor, property)

def test_fxg::containerattributes_has_verticalAlign():
    assert hasattr(fxg::ContainerAttributes, "verticalAlign")
    descriptor = None
    for klass in fxg::ContainerAttributes.__mro__:
        if "verticalAlign" in klass.__dict__:
            descriptor = klass.__dict__["verticalAlign"]
            break
    assert isinstance(descriptor, property)

def test_fxg::containerattributes_has_lineBreak():
    assert hasattr(fxg::ContainerAttributes, "lineBreak")
    descriptor = None
    for klass in fxg::ContainerAttributes.__mro__:
        if "lineBreak" in klass.__dict__:
            descriptor = klass.__dict__["lineBreak"]
            break
    assert isinstance(descriptor, property)

def test_fxg::containerattributes_has_paddingBottom():
    assert hasattr(fxg::ContainerAttributes, "paddingBottom")
    descriptor = None
    for klass in fxg::ContainerAttributes.__mro__:
        if "paddingBottom" in klass.__dict__:
            descriptor = klass.__dict__["paddingBottom"]
            break
    assert isinstance(descriptor, property)

def test_fxg::containerattributes_has_paddingRight():
    assert hasattr(fxg::ContainerAttributes, "paddingRight")
    descriptor = None
    for klass in fxg::ContainerAttributes.__mro__:
        if "paddingRight" in klass.__dict__:
            descriptor = klass.__dict__["paddingRight"]
            break
    assert isinstance(descriptor, property)

def test_fxg::containerattributes_has_blockProgression():
    assert hasattr(fxg::ContainerAttributes, "blockProgression")
    descriptor = None
    for klass in fxg::ContainerAttributes.__mro__:
        if "blockProgression" in klass.__dict__:
            descriptor = klass.__dict__["blockProgression"]
            break
    assert isinstance(descriptor, property)

def test_fxg::containerattributes_has_paddingTop():
    assert hasattr(fxg::ContainerAttributes, "paddingTop")
    descriptor = None
    for klass in fxg::ContainerAttributes.__mro__:
        if "paddingTop" in klass.__dict__:
            descriptor = klass.__dict__["paddingTop"]
            break
    assert isinstance(descriptor, property)

def test_fxg::containerattributes_has_columnCount():
    assert hasattr(fxg::ContainerAttributes, "columnCount")
    descriptor = None
    for klass in fxg::ContainerAttributes.__mro__:
        if "columnCount" in klass.__dict__:
            descriptor = klass.__dict__["columnCount"]
            break
    assert isinstance(descriptor, property)



def test_fxg::paragraphattributes_is_not_abstract():
    assert not inspect.isabstract(fxg::ParagraphAttributes)


def test_fxg::paragraphattributes_constructor_exists():
    assert callable(fxg::ParagraphAttributes.__init__)


def test_fxg::paragraphattributes_constructor_args():
    sig = inspect.signature(fxg::ParagraphAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "paragraphSpaceAfter" in params, "Missing parameter 'paragraphSpaceAfter'"
    assert "textAlignLast" in params, "Missing parameter 'textAlignLast'"
    assert "textIndent" in params, "Missing parameter 'textIndent'"
    assert "paragraphStartIndent" in params, "Missing parameter 'paragraphStartIndent'"
    assert "leadingModel" in params, "Missing parameter 'leadingModel'"
    assert "tabStops" in params, "Missing parameter 'tabStops'"
    assert "textJustify" in params, "Missing parameter 'textJustify'"
    assert "justificationRule" in params, "Missing parameter 'justificationRule'"
    assert "justificationStyle" in params, "Missing parameter 'justificationStyle'"
    assert "textAlign" in params, "Missing parameter 'textAlign'"
    assert "paragraphSpaceBefore" in params, "Missing parameter 'paragraphSpaceBefore'"
    assert "paragraphEndIndent" in params, "Missing parameter 'paragraphEndIndent'"

def test_fxg::paragraphattributes_has_paragraphSpaceAfter():
    assert hasattr(fxg::ParagraphAttributes, "paragraphSpaceAfter")
    descriptor = None
    for klass in fxg::ParagraphAttributes.__mro__:
        if "paragraphSpaceAfter" in klass.__dict__:
            descriptor = klass.__dict__["paragraphSpaceAfter"]
            break
    assert isinstance(descriptor, property)

def test_fxg::paragraphattributes_has_textAlignLast():
    assert hasattr(fxg::ParagraphAttributes, "textAlignLast")
    descriptor = None
    for klass in fxg::ParagraphAttributes.__mro__:
        if "textAlignLast" in klass.__dict__:
            descriptor = klass.__dict__["textAlignLast"]
            break
    assert isinstance(descriptor, property)

def test_fxg::paragraphattributes_has_textIndent():
    assert hasattr(fxg::ParagraphAttributes, "textIndent")
    descriptor = None
    for klass in fxg::ParagraphAttributes.__mro__:
        if "textIndent" in klass.__dict__:
            descriptor = klass.__dict__["textIndent"]
            break
    assert isinstance(descriptor, property)

def test_fxg::paragraphattributes_has_paragraphStartIndent():
    assert hasattr(fxg::ParagraphAttributes, "paragraphStartIndent")
    descriptor = None
    for klass in fxg::ParagraphAttributes.__mro__:
        if "paragraphStartIndent" in klass.__dict__:
            descriptor = klass.__dict__["paragraphStartIndent"]
            break
    assert isinstance(descriptor, property)

def test_fxg::paragraphattributes_has_leadingModel():
    assert hasattr(fxg::ParagraphAttributes, "leadingModel")
    descriptor = None
    for klass in fxg::ParagraphAttributes.__mro__:
        if "leadingModel" in klass.__dict__:
            descriptor = klass.__dict__["leadingModel"]
            break
    assert isinstance(descriptor, property)

def test_fxg::paragraphattributes_has_tabStops():
    assert hasattr(fxg::ParagraphAttributes, "tabStops")
    descriptor = None
    for klass in fxg::ParagraphAttributes.__mro__:
        if "tabStops" in klass.__dict__:
            descriptor = klass.__dict__["tabStops"]
            break
    assert isinstance(descriptor, property)

def test_fxg::paragraphattributes_has_textJustify():
    assert hasattr(fxg::ParagraphAttributes, "textJustify")
    descriptor = None
    for klass in fxg::ParagraphAttributes.__mro__:
        if "textJustify" in klass.__dict__:
            descriptor = klass.__dict__["textJustify"]
            break
    assert isinstance(descriptor, property)

def test_fxg::paragraphattributes_has_justificationRule():
    assert hasattr(fxg::ParagraphAttributes, "justificationRule")
    descriptor = None
    for klass in fxg::ParagraphAttributes.__mro__:
        if "justificationRule" in klass.__dict__:
            descriptor = klass.__dict__["justificationRule"]
            break
    assert isinstance(descriptor, property)

def test_fxg::paragraphattributes_has_justificationStyle():
    assert hasattr(fxg::ParagraphAttributes, "justificationStyle")
    descriptor = None
    for klass in fxg::ParagraphAttributes.__mro__:
        if "justificationStyle" in klass.__dict__:
            descriptor = klass.__dict__["justificationStyle"]
            break
    assert isinstance(descriptor, property)

def test_fxg::paragraphattributes_has_textAlign():
    assert hasattr(fxg::ParagraphAttributes, "textAlign")
    descriptor = None
    for klass in fxg::ParagraphAttributes.__mro__:
        if "textAlign" in klass.__dict__:
            descriptor = klass.__dict__["textAlign"]
            break
    assert isinstance(descriptor, property)

def test_fxg::paragraphattributes_has_paragraphSpaceBefore():
    assert hasattr(fxg::ParagraphAttributes, "paragraphSpaceBefore")
    descriptor = None
    for klass in fxg::ParagraphAttributes.__mro__:
        if "paragraphSpaceBefore" in klass.__dict__:
            descriptor = klass.__dict__["paragraphSpaceBefore"]
            break
    assert isinstance(descriptor, property)

def test_fxg::paragraphattributes_has_paragraphEndIndent():
    assert hasattr(fxg::ParagraphAttributes, "paragraphEndIndent")
    descriptor = None
    for klass in fxg::ParagraphAttributes.__mro__:
        if "paragraphEndIndent" in klass.__dict__:
            descriptor = klass.__dict__["paragraphEndIndent"]
            break
    assert isinstance(descriptor, property)



def test_richtextcontent_is_not_abstract():
    assert not inspect.isabstract(RichTextContent)


def test_richtextcontent_constructor_exists():
    assert callable(RichTextContent.__init__)


def test_richtextcontent_constructor_args():
    sig = inspect.signature(RichTextContent.__init__)
    params = list(sig.parameters.keys())



def test_fxg::linkhoverformat_is_not_abstract():
    assert not inspect.isabstract(fxg::linkHoverFormat)


def test_fxg::linkhoverformat_constructor_exists():
    assert callable(fxg::linkHoverFormat.__init__)


def test_fxg::linkhoverformat_constructor_args():
    sig = inspect.signature(fxg::linkHoverFormat.__init__)
    params = list(sig.parameters.keys())



def test_fxg::span_is_not_abstract():
    assert not inspect.isabstract(fxg::span)


def test_fxg::span_constructor_exists():
    assert callable(fxg::span.__init__)


def test_fxg::span_constructor_args():
    sig = inspect.signature(fxg::span.__init__)
    params = list(sig.parameters.keys())



def test_fxg::tab_is_not_abstract():
    assert not inspect.isabstract(fxg::tab)


def test_fxg::tab_constructor_exists():
    assert callable(fxg::tab.__init__)


def test_fxg::tab_constructor_args():
    sig = inspect.signature(fxg::tab.__init__)
    params = list(sig.parameters.keys())



def test_fxg::linknormalformat_is_not_abstract():
    assert not inspect.isabstract(fxg::linkNormalFormat)


def test_fxg::linknormalformat_constructor_exists():
    assert callable(fxg::linkNormalFormat.__init__)


def test_fxg::linknormalformat_constructor_args():
    sig = inspect.signature(fxg::linkNormalFormat.__init__)
    params = list(sig.parameters.keys())



def test_fxg::a_is_not_abstract():
    assert not inspect.isabstract(fxg::a)


def test_fxg::a_constructor_exists():
    assert callable(fxg::a.__init__)


def test_fxg::a_constructor_args():
    sig = inspect.signature(fxg::a.__init__)
    params = list(sig.parameters.keys())



def test_fxg::rawtext_is_not_abstract():
    assert not inspect.isabstract(fxg::rawtext)


def test_fxg::rawtext_constructor_exists():
    assert callable(fxg::rawtext.__init__)


def test_fxg::rawtext_constructor_args():
    sig = inspect.signature(fxg::rawtext.__init__)
    params = list(sig.parameters.keys())
    assert "_text" in params, "Missing parameter '_text'"

def test_fxg::rawtext_has__text():
    assert hasattr(fxg::rawtext, "_text")
    descriptor = None
    for klass in fxg::rawtext.__mro__:
        if "_text" in klass.__dict__:
            descriptor = klass.__dict__["_text"]
            break
    assert isinstance(descriptor, property)



def test_fxg::img_is_not_abstract():
    assert not inspect.isabstract(fxg::img)


def test_fxg::img_constructor_exists():
    assert callable(fxg::img.__init__)


def test_fxg::img_constructor_args():
    sig = inspect.signature(fxg::img.__init__)
    params = list(sig.parameters.keys())



def test_fxg::div_is_not_abstract():
    assert not inspect.isabstract(fxg::div)


def test_fxg::div_constructor_exists():
    assert callable(fxg::div.__init__)


def test_fxg::div_constructor_args():
    sig = inspect.signature(fxg::div.__init__)
    params = list(sig.parameters.keys())



def test_fxg::br_is_not_abstract():
    assert not inspect.isabstract(fxg::br)


def test_fxg::br_constructor_exists():
    assert callable(fxg::br.__init__)


def test_fxg::br_constructor_args():
    sig = inspect.signature(fxg::br.__init__)
    params = list(sig.parameters.keys())



def test_fxg::tcy_is_not_abstract():
    assert not inspect.isabstract(fxg::tcy)


def test_fxg::tcy_constructor_exists():
    assert callable(fxg::tcy.__init__)


def test_fxg::tcy_constructor_args():
    sig = inspect.signature(fxg::tcy.__init__)
    params = list(sig.parameters.keys())



def test_fxg::richtextcontentcontainer_is_not_abstract():
    assert not inspect.isabstract(fxg::RichTextContentContainer)


def test_fxg::richtextcontentcontainer_constructor_exists():
    assert callable(fxg::RichTextContentContainer.__init__)


def test_fxg::richtextcontentcontainer_constructor_args():
    sig = inspect.signature(fxg::RichTextContentContainer.__init__)
    params = list(sig.parameters.keys())



def test_fxg::richtextcontent_is_not_abstract():
    assert not inspect.isabstract(fxg::RichTextContent)


def test_fxg::richtextcontent_constructor_exists():
    assert callable(fxg::RichTextContent.__init__)


def test_fxg::richtextcontent_constructor_args():
    sig = inspect.signature(fxg::RichTextContent.__init__)
    params = list(sig.parameters.keys())



def test_characterattributes_is_not_abstract():
    assert not inspect.isabstract(CharacterAttributes)


def test_characterattributes_constructor_exists():
    assert callable(CharacterAttributes.__init__)


def test_characterattributes_constructor_args():
    sig = inspect.signature(CharacterAttributes.__init__)
    params = list(sig.parameters.keys())



def test_containerattributes_is_not_abstract():
    assert not inspect.isabstract(ContainerAttributes)


def test_containerattributes_constructor_exists():
    assert callable(ContainerAttributes.__init__)


def test_containerattributes_constructor_args():
    sig = inspect.signature(ContainerAttributes.__init__)
    params = list(sig.parameters.keys())



def test_paragraphattributes_is_not_abstract():
    assert not inspect.isabstract(ParagraphAttributes)


def test_paragraphattributes_constructor_exists():
    assert callable(ParagraphAttributes.__init__)


def test_paragraphattributes_constructor_args():
    sig = inspect.signature(ParagraphAttributes.__init__)
    params = list(sig.parameters.keys())



def test_fxg::p_is_not_abstract():
    assert not inspect.isabstract(fxg::p)


def test_fxg::p_constructor_exists():
    assert callable(fxg::p.__init__)


def test_fxg::p_constructor_args():
    sig = inspect.signature(fxg::p.__init__)
    params = list(sig.parameters.keys())



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_fxg::ellipse_is_not_abstract():
    assert not inspect.isabstract(fxg::Ellipse)


def test_fxg::ellipse_constructor_exists():
    assert callable(fxg::Ellipse.__init__)


def test_fxg::ellipse_constructor_args():
    sig = inspect.signature(fxg::Ellipse.__init__)
    params = list(sig.parameters.keys())
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "width" in params, "Missing parameter 'width'"
    assert "x" in params, "Missing parameter 'x'"
    assert "blendMode" in params, "Missing parameter 'blendMode'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "height" in params, "Missing parameter 'height'"
    assert "y" in params, "Missing parameter 'y'"
    assert "rotation" in params, "Missing parameter 'rotation'"

def test_fxg::ellipse_has_scaleX():
    assert hasattr(fxg::Ellipse, "scaleX")
    descriptor = None
    for klass in fxg::Ellipse.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)

def test_fxg::ellipse_has_visible():
    assert hasattr(fxg::Ellipse, "visible")
    descriptor = None
    for klass in fxg::Ellipse.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_fxg::ellipse_has_alpha():
    assert hasattr(fxg::Ellipse, "alpha")
    descriptor = None
    for klass in fxg::Ellipse.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg::ellipse_has_width():
    assert hasattr(fxg::Ellipse, "width")
    descriptor = None
    for klass in fxg::Ellipse.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_fxg::ellipse_has_x():
    assert hasattr(fxg::Ellipse, "x")
    descriptor = None
    for klass in fxg::Ellipse.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fxg::ellipse_has_blendMode():
    assert hasattr(fxg::Ellipse, "blendMode")
    descriptor = None
    for klass in fxg::Ellipse.__mro__:
        if "blendMode" in klass.__dict__:
            descriptor = klass.__dict__["blendMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg::ellipse_has_scaleY():
    assert hasattr(fxg::Ellipse, "scaleY")
    descriptor = None
    for klass in fxg::Ellipse.__mro__:
        if "scaleY" in klass.__dict__:
            descriptor = klass.__dict__["scaleY"]
            break
    assert isinstance(descriptor, property)

def test_fxg::ellipse_has_height():
    assert hasattr(fxg::Ellipse, "height")
    descriptor = None
    for klass in fxg::Ellipse.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_fxg::ellipse_has_y():
    assert hasattr(fxg::Ellipse, "y")
    descriptor = None
    for klass in fxg::Ellipse.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg::ellipse_has_rotation():
    assert hasattr(fxg::Ellipse, "rotation")
    descriptor = None
    for klass in fxg::Ellipse.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)



def test_fxg::line_is_not_abstract():
    assert not inspect.isabstract(fxg::Line)


def test_fxg::line_constructor_exists():
    assert callable(fxg::Line.__init__)


def test_fxg::line_constructor_args():
    sig = inspect.signature(fxg::Line.__init__)
    params = list(sig.parameters.keys())
    assert "yFrom" in params, "Missing parameter 'yFrom'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "xTo" in params, "Missing parameter 'xTo'"
    assert "xFrom" in params, "Missing parameter 'xFrom'"
    assert "yTo" in params, "Missing parameter 'yTo'"
    assert "x" in params, "Missing parameter 'x'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "y" in params, "Missing parameter 'y'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "id" in params, "Missing parameter 'id'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "blendMode" in params, "Missing parameter 'blendMode'"
    assert "maskType" in params, "Missing parameter 'maskType'"

def test_fxg::line_has_yFrom():
    assert hasattr(fxg::Line, "yFrom")
    descriptor = None
    for klass in fxg::Line.__mro__:
        if "yFrom" in klass.__dict__:
            descriptor = klass.__dict__["yFrom"]
            break
    assert isinstance(descriptor, property)

def test_fxg::line_has_rotation():
    assert hasattr(fxg::Line, "rotation")
    descriptor = None
    for klass in fxg::Line.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg::line_has_xTo():
    assert hasattr(fxg::Line, "xTo")
    descriptor = None
    for klass in fxg::Line.__mro__:
        if "xTo" in klass.__dict__:
            descriptor = klass.__dict__["xTo"]
            break
    assert isinstance(descriptor, property)

def test_fxg::line_has_xFrom():
    assert hasattr(fxg::Line, "xFrom")
    descriptor = None
    for klass in fxg::Line.__mro__:
        if "xFrom" in klass.__dict__:
            descriptor = klass.__dict__["xFrom"]
            break
    assert isinstance(descriptor, property)

def test_fxg::line_has_yTo():
    assert hasattr(fxg::Line, "yTo")
    descriptor = None
    for klass in fxg::Line.__mro__:
        if "yTo" in klass.__dict__:
            descriptor = klass.__dict__["yTo"]
            break
    assert isinstance(descriptor, property)

def test_fxg::line_has_x():
    assert hasattr(fxg::Line, "x")
    descriptor = None
    for klass in fxg::Line.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fxg::line_has_scaleY():
    assert hasattr(fxg::Line, "scaleY")
    descriptor = None
    for klass in fxg::Line.__mro__:
        if "scaleY" in klass.__dict__:
            descriptor = klass.__dict__["scaleY"]
            break
    assert isinstance(descriptor, property)

def test_fxg::line_has_y():
    assert hasattr(fxg::Line, "y")
    descriptor = None
    for klass in fxg::Line.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg::line_has_scaleX():
    assert hasattr(fxg::Line, "scaleX")
    descriptor = None
    for klass in fxg::Line.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)

def test_fxg::line_has_id():
    assert hasattr(fxg::Line, "id")
    descriptor = None
    for klass in fxg::Line.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_fxg::line_has_visible():
    assert hasattr(fxg::Line, "visible")
    descriptor = None
    for klass in fxg::Line.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_fxg::line_has_alpha():
    assert hasattr(fxg::Line, "alpha")
    descriptor = None
    for klass in fxg::Line.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg::line_has_blendMode():
    assert hasattr(fxg::Line, "blendMode")
    descriptor = None
    for klass in fxg::Line.__mro__:
        if "blendMode" in klass.__dict__:
            descriptor = klass.__dict__["blendMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg::line_has_maskType():
    assert hasattr(fxg::Line, "maskType")
    descriptor = None
    for klass in fxg::Line.__mro__:
        if "maskType" in klass.__dict__:
            descriptor = klass.__dict__["maskType"]
            break
    assert isinstance(descriptor, property)



def test_fxg::rect_is_not_abstract():
    assert not inspect.isabstract(fxg::Rect)


def test_fxg::rect_constructor_exists():
    assert callable(fxg::Rect.__init__)


def test_fxg::rect_constructor_args():
    sig = inspect.signature(fxg::Rect.__init__)
    params = list(sig.parameters.keys())
    assert "bottomRightRadiusY" in params, "Missing parameter 'bottomRightRadiusY'"
    assert "radiusY" in params, "Missing parameter 'radiusY'"
    assert "bottomLeftRadiusX" in params, "Missing parameter 'bottomLeftRadiusX'"
    assert "x" in params, "Missing parameter 'x'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "radiusX" in params, "Missing parameter 'radiusX'"
    assert "height" in params, "Missing parameter 'height'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "topRightRadiusX" in params, "Missing parameter 'topRightRadiusX'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "topLeftRadiusY" in params, "Missing parameter 'topLeftRadiusY'"
    assert "topLeftRadiusX" in params, "Missing parameter 'topLeftRadiusX'"
    assert "topRightRadiusY" in params, "Missing parameter 'topRightRadiusY'"
    assert "blendMode" in params, "Missing parameter 'blendMode'"
    assert "y" in params, "Missing parameter 'y'"
    assert "bottomRightRadiusX" in params, "Missing parameter 'bottomRightRadiusX'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "bottomLeftRadiusY" in params, "Missing parameter 'bottomLeftRadiusY'"
    assert "width" in params, "Missing parameter 'width'"

def test_fxg::rect_has_bottomRightRadiusY():
    assert hasattr(fxg::Rect, "bottomRightRadiusY")
    descriptor = None
    for klass in fxg::Rect.__mro__:
        if "bottomRightRadiusY" in klass.__dict__:
            descriptor = klass.__dict__["bottomRightRadiusY"]
            break
    assert isinstance(descriptor, property)

def test_fxg::rect_has_radiusY():
    assert hasattr(fxg::Rect, "radiusY")
    descriptor = None
    for klass in fxg::Rect.__mro__:
        if "radiusY" in klass.__dict__:
            descriptor = klass.__dict__["radiusY"]
            break
    assert isinstance(descriptor, property)

def test_fxg::rect_has_bottomLeftRadiusX():
    assert hasattr(fxg::Rect, "bottomLeftRadiusX")
    descriptor = None
    for klass in fxg::Rect.__mro__:
        if "bottomLeftRadiusX" in klass.__dict__:
            descriptor = klass.__dict__["bottomLeftRadiusX"]
            break
    assert isinstance(descriptor, property)

def test_fxg::rect_has_x():
    assert hasattr(fxg::Rect, "x")
    descriptor = None
    for klass in fxg::Rect.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fxg::rect_has_rotation():
    assert hasattr(fxg::Rect, "rotation")
    descriptor = None
    for klass in fxg::Rect.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg::rect_has_scaleY():
    assert hasattr(fxg::Rect, "scaleY")
    descriptor = None
    for klass in fxg::Rect.__mro__:
        if "scaleY" in klass.__dict__:
            descriptor = klass.__dict__["scaleY"]
            break
    assert isinstance(descriptor, property)

def test_fxg::rect_has_radiusX():
    assert hasattr(fxg::Rect, "radiusX")
    descriptor = None
    for klass in fxg::Rect.__mro__:
        if "radiusX" in klass.__dict__:
            descriptor = klass.__dict__["radiusX"]
            break
    assert isinstance(descriptor, property)

def test_fxg::rect_has_height():
    assert hasattr(fxg::Rect, "height")
    descriptor = None
    for klass in fxg::Rect.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_fxg::rect_has_scaleX():
    assert hasattr(fxg::Rect, "scaleX")
    descriptor = None
    for klass in fxg::Rect.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)

def test_fxg::rect_has_topRightRadiusX():
    assert hasattr(fxg::Rect, "topRightRadiusX")
    descriptor = None
    for klass in fxg::Rect.__mro__:
        if "topRightRadiusX" in klass.__dict__:
            descriptor = klass.__dict__["topRightRadiusX"]
            break
    assert isinstance(descriptor, property)

def test_fxg::rect_has_alpha():
    assert hasattr(fxg::Rect, "alpha")
    descriptor = None
    for klass in fxg::Rect.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg::rect_has_topLeftRadiusY():
    assert hasattr(fxg::Rect, "topLeftRadiusY")
    descriptor = None
    for klass in fxg::Rect.__mro__:
        if "topLeftRadiusY" in klass.__dict__:
            descriptor = klass.__dict__["topLeftRadiusY"]
            break
    assert isinstance(descriptor, property)

def test_fxg::rect_has_topLeftRadiusX():
    assert hasattr(fxg::Rect, "topLeftRadiusX")
    descriptor = None
    for klass in fxg::Rect.__mro__:
        if "topLeftRadiusX" in klass.__dict__:
            descriptor = klass.__dict__["topLeftRadiusX"]
            break
    assert isinstance(descriptor, property)

def test_fxg::rect_has_topRightRadiusY():
    assert hasattr(fxg::Rect, "topRightRadiusY")
    descriptor = None
    for klass in fxg::Rect.__mro__:
        if "topRightRadiusY" in klass.__dict__:
            descriptor = klass.__dict__["topRightRadiusY"]
            break
    assert isinstance(descriptor, property)

def test_fxg::rect_has_blendMode():
    assert hasattr(fxg::Rect, "blendMode")
    descriptor = None
    for klass in fxg::Rect.__mro__:
        if "blendMode" in klass.__dict__:
            descriptor = klass.__dict__["blendMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg::rect_has_y():
    assert hasattr(fxg::Rect, "y")
    descriptor = None
    for klass in fxg::Rect.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg::rect_has_bottomRightRadiusX():
    assert hasattr(fxg::Rect, "bottomRightRadiusX")
    descriptor = None
    for klass in fxg::Rect.__mro__:
        if "bottomRightRadiusX" in klass.__dict__:
            descriptor = klass.__dict__["bottomRightRadiusX"]
            break
    assert isinstance(descriptor, property)

def test_fxg::rect_has_visible():
    assert hasattr(fxg::Rect, "visible")
    descriptor = None
    for klass in fxg::Rect.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_fxg::rect_has_bottomLeftRadiusY():
    assert hasattr(fxg::Rect, "bottomLeftRadiusY")
    descriptor = None
    for klass in fxg::Rect.__mro__:
        if "bottomLeftRadiusY" in klass.__dict__:
            descriptor = klass.__dict__["bottomLeftRadiusY"]
            break
    assert isinstance(descriptor, property)

def test_fxg::rect_has_width():
    assert hasattr(fxg::Rect, "width")
    descriptor = None
    for klass in fxg::Rect.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_fxg::definition_is_not_abstract():
    assert not inspect.isabstract(fxg::Definition)


def test_fxg::definition_constructor_exists():
    assert callable(fxg::Definition.__init__)


def test_fxg::definition_constructor_args():
    sig = inspect.signature(fxg::Definition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fxg::definition_has_name():
    assert hasattr(fxg::Definition, "name")
    descriptor = None
    for klass in fxg::Definition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fxgelement_is_not_abstract():
    assert not inspect.isabstract(FXGElement)


def test_fxgelement_constructor_exists():
    assert callable(FXGElement.__init__)


def test_fxgelement_constructor_args():
    sig = inspect.signature(FXGElement.__init__)
    params = list(sig.parameters.keys())



def test_fxg::transform_is_not_abstract():
    assert not inspect.isabstract(fxg::Transform)


def test_fxg::transform_constructor_exists():
    assert callable(fxg::Transform.__init__)


def test_fxg::transform_constructor_args():
    sig = inspect.signature(fxg::Transform.__init__)
    params = list(sig.parameters.keys())



def test_fxg::containerelement_is_not_abstract():
    assert not inspect.isabstract(fxg::ContainerElement)


def test_fxg::containerelement_constructor_exists():
    assert callable(fxg::ContainerElement.__init__)


def test_fxg::containerelement_constructor_args():
    sig = inspect.signature(fxg::ContainerElement.__init__)
    params = list(sig.parameters.keys())



def test_fxg::gradiententry_is_not_abstract():
    assert not inspect.isabstract(fxg::GradientEntry)


def test_fxg::gradiententry_constructor_exists():
    assert callable(fxg::GradientEntry.__init__)


def test_fxg::gradiententry_constructor_args():
    sig = inspect.signature(fxg::GradientEntry.__init__)
    params = list(sig.parameters.keys())
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "ratio" in params, "Missing parameter 'ratio'"
    assert "color" in params, "Missing parameter 'color'"

def test_fxg::gradiententry_has_alpha():
    assert hasattr(fxg::GradientEntry, "alpha")
    descriptor = None
    for klass in fxg::GradientEntry.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg::gradiententry_has_ratio():
    assert hasattr(fxg::GradientEntry, "ratio")
    descriptor = None
    for klass in fxg::GradientEntry.__mro__:
        if "ratio" in klass.__dict__:
            descriptor = klass.__dict__["ratio"]
            break
    assert isinstance(descriptor, property)

def test_fxg::gradiententry_has_color():
    assert hasattr(fxg::GradientEntry, "color")
    descriptor = None
    for klass in fxg::GradientEntry.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_fxg::colortransform_is_not_abstract():
    assert not inspect.isabstract(fxg::ColorTransform)


def test_fxg::colortransform_constructor_exists():
    assert callable(fxg::ColorTransform.__init__)


def test_fxg::colortransform_constructor_args():
    sig = inspect.signature(fxg::ColorTransform.__init__)
    params = list(sig.parameters.keys())
    assert "alphaMultiplier" in params, "Missing parameter 'alphaMultiplier'"
    assert "redOffset" in params, "Missing parameter 'redOffset'"
    assert "greenOffset" in params, "Missing parameter 'greenOffset'"
    assert "greenMultiplier" in params, "Missing parameter 'greenMultiplier'"
    assert "blueOffset" in params, "Missing parameter 'blueOffset'"
    assert "alphaOffset" in params, "Missing parameter 'alphaOffset'"
    assert "redMultiplier" in params, "Missing parameter 'redMultiplier'"
    assert "blueMultiplier" in params, "Missing parameter 'blueMultiplier'"

def test_fxg::colortransform_has_alphaMultiplier():
    assert hasattr(fxg::ColorTransform, "alphaMultiplier")
    descriptor = None
    for klass in fxg::ColorTransform.__mro__:
        if "alphaMultiplier" in klass.__dict__:
            descriptor = klass.__dict__["alphaMultiplier"]
            break
    assert isinstance(descriptor, property)

def test_fxg::colortransform_has_redOffset():
    assert hasattr(fxg::ColorTransform, "redOffset")
    descriptor = None
    for klass in fxg::ColorTransform.__mro__:
        if "redOffset" in klass.__dict__:
            descriptor = klass.__dict__["redOffset"]
            break
    assert isinstance(descriptor, property)

def test_fxg::colortransform_has_greenOffset():
    assert hasattr(fxg::ColorTransform, "greenOffset")
    descriptor = None
    for klass in fxg::ColorTransform.__mro__:
        if "greenOffset" in klass.__dict__:
            descriptor = klass.__dict__["greenOffset"]
            break
    assert isinstance(descriptor, property)

def test_fxg::colortransform_has_greenMultiplier():
    assert hasattr(fxg::ColorTransform, "greenMultiplier")
    descriptor = None
    for klass in fxg::ColorTransform.__mro__:
        if "greenMultiplier" in klass.__dict__:
            descriptor = klass.__dict__["greenMultiplier"]
            break
    assert isinstance(descriptor, property)

def test_fxg::colortransform_has_blueOffset():
    assert hasattr(fxg::ColorTransform, "blueOffset")
    descriptor = None
    for klass in fxg::ColorTransform.__mro__:
        if "blueOffset" in klass.__dict__:
            descriptor = klass.__dict__["blueOffset"]
            break
    assert isinstance(descriptor, property)

def test_fxg::colortransform_has_alphaOffset():
    assert hasattr(fxg::ColorTransform, "alphaOffset")
    descriptor = None
    for klass in fxg::ColorTransform.__mro__:
        if "alphaOffset" in klass.__dict__:
            descriptor = klass.__dict__["alphaOffset"]
            break
    assert isinstance(descriptor, property)

def test_fxg::colortransform_has_redMultiplier():
    assert hasattr(fxg::ColorTransform, "redMultiplier")
    descriptor = None
    for klass in fxg::ColorTransform.__mro__:
        if "redMultiplier" in klass.__dict__:
            descriptor = klass.__dict__["redMultiplier"]
            break
    assert isinstance(descriptor, property)

def test_fxg::colortransform_has_blueMultiplier():
    assert hasattr(fxg::ColorTransform, "blueMultiplier")
    descriptor = None
    for klass in fxg::ColorTransform.__mro__:
        if "blueMultiplier" in klass.__dict__:
            descriptor = klass.__dict__["blueMultiplier"]
            break
    assert isinstance(descriptor, property)



def test_fxg::stroke_is_not_abstract():
    assert not inspect.isabstract(fxg::Stroke)


def test_fxg::stroke_constructor_exists():
    assert callable(fxg::Stroke.__init__)


def test_fxg::stroke_constructor_args():
    sig = inspect.signature(fxg::Stroke.__init__)
    params = list(sig.parameters.keys())



def test_fxg::placeobject_is_not_abstract():
    assert not inspect.isabstract(fxg::PlaceObject)


def test_fxg::placeobject_constructor_exists():
    assert callable(fxg::PlaceObject.__init__)


def test_fxg::placeobject_constructor_args():
    sig = inspect.signature(fxg::PlaceObject.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_fxg::placeobject_has_id():
    assert hasattr(fxg::PlaceObject, "id")
    descriptor = None
    for klass in fxg::PlaceObject.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_fxg::bitmapimage_is_not_abstract():
    assert not inspect.isabstract(fxg::BitmapImage)


def test_fxg::bitmapimage_constructor_exists():
    assert callable(fxg::BitmapImage.__init__)


def test_fxg::bitmapimage_constructor_args():
    sig = inspect.signature(fxg::BitmapImage.__init__)
    params = list(sig.parameters.keys())
    assert "fillMode" in params, "Missing parameter 'fillMode'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "blendMode" in params, "Missing parameter 'blendMode'"
    assert "y" in params, "Missing parameter 'y'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "height" in params, "Missing parameter 'height'"
    assert "source" in params, "Missing parameter 'source'"
    assert "x" in params, "Missing parameter 'x'"
    assert "width" in params, "Missing parameter 'width'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"

def test_fxg::bitmapimage_has_fillMode():
    assert hasattr(fxg::BitmapImage, "fillMode")
    descriptor = None
    for klass in fxg::BitmapImage.__mro__:
        if "fillMode" in klass.__dict__:
            descriptor = klass.__dict__["fillMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bitmapimage_has_scaleX():
    assert hasattr(fxg::BitmapImage, "scaleX")
    descriptor = None
    for klass in fxg::BitmapImage.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bitmapimage_has_visible():
    assert hasattr(fxg::BitmapImage, "visible")
    descriptor = None
    for klass in fxg::BitmapImage.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bitmapimage_has_alpha():
    assert hasattr(fxg::BitmapImage, "alpha")
    descriptor = None
    for klass in fxg::BitmapImage.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bitmapimage_has_blendMode():
    assert hasattr(fxg::BitmapImage, "blendMode")
    descriptor = None
    for klass in fxg::BitmapImage.__mro__:
        if "blendMode" in klass.__dict__:
            descriptor = klass.__dict__["blendMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bitmapimage_has_y():
    assert hasattr(fxg::BitmapImage, "y")
    descriptor = None
    for klass in fxg::BitmapImage.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bitmapimage_has_rotation():
    assert hasattr(fxg::BitmapImage, "rotation")
    descriptor = None
    for klass in fxg::BitmapImage.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bitmapimage_has_height():
    assert hasattr(fxg::BitmapImage, "height")
    descriptor = None
    for klass in fxg::BitmapImage.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bitmapimage_has_source():
    assert hasattr(fxg::BitmapImage, "source")
    descriptor = None
    for klass in fxg::BitmapImage.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bitmapimage_has_x():
    assert hasattr(fxg::BitmapImage, "x")
    descriptor = None
    for klass in fxg::BitmapImage.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bitmapimage_has_width():
    assert hasattr(fxg::BitmapImage, "width")
    descriptor = None
    for klass in fxg::BitmapImage.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_fxg::bitmapimage_has_scaleY():
    assert hasattr(fxg::BitmapImage, "scaleY")
    descriptor = None
    for klass in fxg::BitmapImage.__mro__:
        if "scaleY" in klass.__dict__:
            descriptor = klass.__dict__["scaleY"]
            break
    assert isinstance(descriptor, property)



def test_fxg::fill_is_not_abstract():
    assert not inspect.isabstract(fxg::Fill)


def test_fxg::fill_constructor_exists():
    assert callable(fxg::Fill.__init__)


def test_fxg::fill_constructor_args():
    sig = inspect.signature(fxg::Fill.__init__)
    params = list(sig.parameters.keys())



def test_fxg::matrix_is_not_abstract():
    assert not inspect.isabstract(fxg::Matrix)


def test_fxg::matrix_constructor_exists():
    assert callable(fxg::Matrix.__init__)


def test_fxg::matrix_constructor_args():
    sig = inspect.signature(fxg::Matrix.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"
    assert "c" in params, "Missing parameter 'c'"
    assert "ty" in params, "Missing parameter 'ty'"
    assert "b" in params, "Missing parameter 'b'"
    assert "tx" in params, "Missing parameter 'tx'"
    assert "d" in params, "Missing parameter 'd'"

def test_fxg::matrix_has_a():
    assert hasattr(fxg::Matrix, "a")
    descriptor = None
    for klass in fxg::Matrix.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)

def test_fxg::matrix_has_c():
    assert hasattr(fxg::Matrix, "c")
    descriptor = None
    for klass in fxg::Matrix.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)

def test_fxg::matrix_has_ty():
    assert hasattr(fxg::Matrix, "ty")
    descriptor = None
    for klass in fxg::Matrix.__mro__:
        if "ty" in klass.__dict__:
            descriptor = klass.__dict__["ty"]
            break
    assert isinstance(descriptor, property)

def test_fxg::matrix_has_b():
    assert hasattr(fxg::Matrix, "b")
    descriptor = None
    for klass in fxg::Matrix.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_fxg::matrix_has_tx():
    assert hasattr(fxg::Matrix, "tx")
    descriptor = None
    for klass in fxg::Matrix.__mro__:
        if "tx" in klass.__dict__:
            descriptor = klass.__dict__["tx"]
            break
    assert isinstance(descriptor, property)

def test_fxg::matrix_has_d():
    assert hasattr(fxg::Matrix, "d")
    descriptor = None
    for klass in fxg::Matrix.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
            break
    assert isinstance(descriptor, property)



def test_fxg::filter_is_not_abstract():
    assert not inspect.isabstract(fxg::Filter)


def test_fxg::filter_constructor_exists():
    assert callable(fxg::Filter.__init__)


def test_fxg::filter_constructor_args():
    sig = inspect.signature(fxg::Filter.__init__)
    params = list(sig.parameters.keys())



def test_fxg::richtext_is_not_abstract():
    assert not inspect.isabstract(fxg::RichText)


def test_fxg::richtext_constructor_exists():
    assert callable(fxg::RichText.__init__)


def test_fxg::richtext_constructor_args():
    sig = inspect.signature(fxg::RichText.__init__)
    params = list(sig.parameters.keys())
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "width" in params, "Missing parameter 'width'"
    assert "x" in params, "Missing parameter 'x'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "maskType" in params, "Missing parameter 'maskType'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "_tempcontent" in params, "Missing parameter '_tempcontent'"
    assert "blendMode" in params, "Missing parameter 'blendMode'"
    assert "id" in params, "Missing parameter 'id'"
    assert "y" in params, "Missing parameter 'y'"
    assert "height" in params, "Missing parameter 'height'"
    assert "rotation" in params, "Missing parameter 'rotation'"

def test_fxg::richtext_has_scaleY():
    assert hasattr(fxg::RichText, "scaleY")
    descriptor = None
    for klass in fxg::RichText.__mro__:
        if "scaleY" in klass.__dict__:
            descriptor = klass.__dict__["scaleY"]
            break
    assert isinstance(descriptor, property)

def test_fxg::richtext_has_alpha():
    assert hasattr(fxg::RichText, "alpha")
    descriptor = None
    for klass in fxg::RichText.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg::richtext_has_width():
    assert hasattr(fxg::RichText, "width")
    descriptor = None
    for klass in fxg::RichText.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_fxg::richtext_has_x():
    assert hasattr(fxg::RichText, "x")
    descriptor = None
    for klass in fxg::RichText.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fxg::richtext_has_visible():
    assert hasattr(fxg::RichText, "visible")
    descriptor = None
    for klass in fxg::RichText.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_fxg::richtext_has_maskType():
    assert hasattr(fxg::RichText, "maskType")
    descriptor = None
    for klass in fxg::RichText.__mro__:
        if "maskType" in klass.__dict__:
            descriptor = klass.__dict__["maskType"]
            break
    assert isinstance(descriptor, property)

def test_fxg::richtext_has_scaleX():
    assert hasattr(fxg::RichText, "scaleX")
    descriptor = None
    for klass in fxg::RichText.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)

def test_fxg::richtext_has__tempcontent():
    assert hasattr(fxg::RichText, "_tempcontent")
    descriptor = None
    for klass in fxg::RichText.__mro__:
        if "_tempcontent" in klass.__dict__:
            descriptor = klass.__dict__["_tempcontent"]
            break
    assert isinstance(descriptor, property)

def test_fxg::richtext_has_blendMode():
    assert hasattr(fxg::RichText, "blendMode")
    descriptor = None
    for klass in fxg::RichText.__mro__:
        if "blendMode" in klass.__dict__:
            descriptor = klass.__dict__["blendMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg::richtext_has_id():
    assert hasattr(fxg::RichText, "id")
    descriptor = None
    for klass in fxg::RichText.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_fxg::richtext_has_y():
    assert hasattr(fxg::RichText, "y")
    descriptor = None
    for klass in fxg::RichText.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg::richtext_has_height():
    assert hasattr(fxg::RichText, "height")
    descriptor = None
    for klass in fxg::RichText.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_fxg::richtext_has_rotation():
    assert hasattr(fxg::RichText, "rotation")
    descriptor = None
    for klass in fxg::RichText.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)



def test_fxg::path_is_not_abstract():
    assert not inspect.isabstract(fxg::Path)


def test_fxg::path_constructor_exists():
    assert callable(fxg::Path.__init__)


def test_fxg::path_constructor_args():
    sig = inspect.signature(fxg::Path.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "winding" in params, "Missing parameter 'winding'"
    assert "blendMode" in params, "Missing parameter 'blendMode'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "data" in params, "Missing parameter 'data'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "x" in params, "Missing parameter 'x'"

def test_fxg::path_has_y():
    assert hasattr(fxg::Path, "y")
    descriptor = None
    for klass in fxg::Path.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg::path_has_winding():
    assert hasattr(fxg::Path, "winding")
    descriptor = None
    for klass in fxg::Path.__mro__:
        if "winding" in klass.__dict__:
            descriptor = klass.__dict__["winding"]
            break
    assert isinstance(descriptor, property)

def test_fxg::path_has_blendMode():
    assert hasattr(fxg::Path, "blendMode")
    descriptor = None
    for klass in fxg::Path.__mro__:
        if "blendMode" in klass.__dict__:
            descriptor = klass.__dict__["blendMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg::path_has_rotation():
    assert hasattr(fxg::Path, "rotation")
    descriptor = None
    for klass in fxg::Path.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg::path_has_data():
    assert hasattr(fxg::Path, "data")
    descriptor = None
    for klass in fxg::Path.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)

def test_fxg::path_has_scaleX():
    assert hasattr(fxg::Path, "scaleX")
    descriptor = None
    for klass in fxg::Path.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)

def test_fxg::path_has_visible():
    assert hasattr(fxg::Path, "visible")
    descriptor = None
    for klass in fxg::Path.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_fxg::path_has_scaleY():
    assert hasattr(fxg::Path, "scaleY")
    descriptor = None
    for klass in fxg::Path.__mro__:
        if "scaleY" in klass.__dict__:
            descriptor = klass.__dict__["scaleY"]
            break
    assert isinstance(descriptor, property)

def test_fxg::path_has_alpha():
    assert hasattr(fxg::Path, "alpha")
    descriptor = None
    for klass in fxg::Path.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg::path_has_x():
    assert hasattr(fxg::Path, "x")
    descriptor = None
    for klass in fxg::Path.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_fxg::shape_is_not_abstract():
    assert not inspect.isabstract(fxg::Shape)


def test_fxg::shape_constructor_exists():
    assert callable(fxg::Shape.__init__)


def test_fxg::shape_constructor_args():
    sig = inspect.signature(fxg::Shape.__init__)
    params = list(sig.parameters.keys())



def test_fxg::private_is_not_abstract():
    assert not inspect.isabstract(fxg::Private)


def test_fxg::private_constructor_exists():
    assert callable(fxg::Private.__init__)


def test_fxg::private_constructor_args():
    sig = inspect.signature(fxg::Private.__init__)
    params = list(sig.parameters.keys())



def test_fxg::library_is_not_abstract():
    assert not inspect.isabstract(fxg::Library)


def test_fxg::library_constructor_exists():
    assert callable(fxg::Library.__init__)


def test_fxg::library_constructor_args():
    sig = inspect.signature(fxg::Library.__init__)
    params = list(sig.parameters.keys())



def test_fxg::group_is_not_abstract():
    assert not inspect.isabstract(fxg::Group)


def test_fxg::group_constructor_exists():
    assert callable(fxg::Group.__init__)


def test_fxg::group_constructor_args():
    sig = inspect.signature(fxg::Group.__init__)
    params = list(sig.parameters.keys())
    assert "scaleGridTop" in params, "Missing parameter 'scaleGridTop'"
    assert "scaleGridLeft" in params, "Missing parameter 'scaleGridLeft'"
    assert "scaleGridRight" in params, "Missing parameter 'scaleGridRight'"
    assert "transformX" in params, "Missing parameter 'transformX'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "y" in params, "Missing parameter 'y'"
    assert "id" in params, "Missing parameter 'id'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "scaleGridBottom" in params, "Missing parameter 'scaleGridBottom'"
    assert "maskType" in params, "Missing parameter 'maskType'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "transformY" in params, "Missing parameter 'transformY'"
    assert "blendMode" in params, "Missing parameter 'blendMode'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "x" in params, "Missing parameter 'x'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"

def test_fxg::group_has_scaleGridTop():
    assert hasattr(fxg::Group, "scaleGridTop")
    descriptor = None
    for klass in fxg::Group.__mro__:
        if "scaleGridTop" in klass.__dict__:
            descriptor = klass.__dict__["scaleGridTop"]
            break
    assert isinstance(descriptor, property)

def test_fxg::group_has_scaleGridLeft():
    assert hasattr(fxg::Group, "scaleGridLeft")
    descriptor = None
    for klass in fxg::Group.__mro__:
        if "scaleGridLeft" in klass.__dict__:
            descriptor = klass.__dict__["scaleGridLeft"]
            break
    assert isinstance(descriptor, property)

def test_fxg::group_has_scaleGridRight():
    assert hasattr(fxg::Group, "scaleGridRight")
    descriptor = None
    for klass in fxg::Group.__mro__:
        if "scaleGridRight" in klass.__dict__:
            descriptor = klass.__dict__["scaleGridRight"]
            break
    assert isinstance(descriptor, property)

def test_fxg::group_has_transformX():
    assert hasattr(fxg::Group, "transformX")
    descriptor = None
    for klass in fxg::Group.__mro__:
        if "transformX" in klass.__dict__:
            descriptor = klass.__dict__["transformX"]
            break
    assert isinstance(descriptor, property)

def test_fxg::group_has_scaleY():
    assert hasattr(fxg::Group, "scaleY")
    descriptor = None
    for klass in fxg::Group.__mro__:
        if "scaleY" in klass.__dict__:
            descriptor = klass.__dict__["scaleY"]
            break
    assert isinstance(descriptor, property)

def test_fxg::group_has_y():
    assert hasattr(fxg::Group, "y")
    descriptor = None
    for klass in fxg::Group.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg::group_has_id():
    assert hasattr(fxg::Group, "id")
    descriptor = None
    for klass in fxg::Group.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_fxg::group_has_visible():
    assert hasattr(fxg::Group, "visible")
    descriptor = None
    for klass in fxg::Group.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_fxg::group_has_scaleGridBottom():
    assert hasattr(fxg::Group, "scaleGridBottom")
    descriptor = None
    for klass in fxg::Group.__mro__:
        if "scaleGridBottom" in klass.__dict__:
            descriptor = klass.__dict__["scaleGridBottom"]
            break
    assert isinstance(descriptor, property)

def test_fxg::group_has_maskType():
    assert hasattr(fxg::Group, "maskType")
    descriptor = None
    for klass in fxg::Group.__mro__:
        if "maskType" in klass.__dict__:
            descriptor = klass.__dict__["maskType"]
            break
    assert isinstance(descriptor, property)

def test_fxg::group_has_rotation():
    assert hasattr(fxg::Group, "rotation")
    descriptor = None
    for klass in fxg::Group.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg::group_has_transformY():
    assert hasattr(fxg::Group, "transformY")
    descriptor = None
    for klass in fxg::Group.__mro__:
        if "transformY" in klass.__dict__:
            descriptor = klass.__dict__["transformY"]
            break
    assert isinstance(descriptor, property)

def test_fxg::group_has_blendMode():
    assert hasattr(fxg::Group, "blendMode")
    descriptor = None
    for klass in fxg::Group.__mro__:
        if "blendMode" in klass.__dict__:
            descriptor = klass.__dict__["blendMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg::group_has_alpha():
    assert hasattr(fxg::Group, "alpha")
    descriptor = None
    for klass in fxg::Group.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg::group_has_x():
    assert hasattr(fxg::Group, "x")
    descriptor = None
    for klass in fxg::Group.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fxg::group_has_scaleX():
    assert hasattr(fxg::Group, "scaleX")
    descriptor = None
    for klass in fxg::Group.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)



def test_fxg::graphic_is_not_abstract():
    assert not inspect.isabstract(fxg::Graphic)


def test_fxg::graphic_constructor_exists():
    assert callable(fxg::Graphic.__init__)


def test_fxg::graphic_constructor_args():
    sig = inspect.signature(fxg::Graphic.__init__)
    params = list(sig.parameters.keys())
    assert "scaleGridRight" in params, "Missing parameter 'scaleGridRight'"
    assert "scaleGridLeft" in params, "Missing parameter 'scaleGridLeft'"
    assert "viewHeight" in params, "Missing parameter 'viewHeight'"
    assert "viewWidth" in params, "Missing parameter 'viewWidth'"
    assert "scaleGridBottom" in params, "Missing parameter 'scaleGridBottom'"
    assert "version" in params, "Missing parameter 'version'"
    assert "scaleGridTop" in params, "Missing parameter 'scaleGridTop'"

def test_fxg::graphic_has_scaleGridRight():
    assert hasattr(fxg::Graphic, "scaleGridRight")
    descriptor = None
    for klass in fxg::Graphic.__mro__:
        if "scaleGridRight" in klass.__dict__:
            descriptor = klass.__dict__["scaleGridRight"]
            break
    assert isinstance(descriptor, property)

def test_fxg::graphic_has_scaleGridLeft():
    assert hasattr(fxg::Graphic, "scaleGridLeft")
    descriptor = None
    for klass in fxg::Graphic.__mro__:
        if "scaleGridLeft" in klass.__dict__:
            descriptor = klass.__dict__["scaleGridLeft"]
            break
    assert isinstance(descriptor, property)

def test_fxg::graphic_has_viewHeight():
    assert hasattr(fxg::Graphic, "viewHeight")
    descriptor = None
    for klass in fxg::Graphic.__mro__:
        if "viewHeight" in klass.__dict__:
            descriptor = klass.__dict__["viewHeight"]
            break
    assert isinstance(descriptor, property)

def test_fxg::graphic_has_viewWidth():
    assert hasattr(fxg::Graphic, "viewWidth")
    descriptor = None
    for klass in fxg::Graphic.__mro__:
        if "viewWidth" in klass.__dict__:
            descriptor = klass.__dict__["viewWidth"]
            break
    assert isinstance(descriptor, property)

def test_fxg::graphic_has_scaleGridBottom():
    assert hasattr(fxg::Graphic, "scaleGridBottom")
    descriptor = None
    for klass in fxg::Graphic.__mro__:
        if "scaleGridBottom" in klass.__dict__:
            descriptor = klass.__dict__["scaleGridBottom"]
            break
    assert isinstance(descriptor, property)

def test_fxg::graphic_has_version():
    assert hasattr(fxg::Graphic, "version")
    descriptor = None
    for klass in fxg::Graphic.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_fxg::graphic_has_scaleGridTop():
    assert hasattr(fxg::Graphic, "scaleGridTop")
    descriptor = None
    for klass in fxg::Graphic.__mro__:
        if "scaleGridTop" in klass.__dict__:
            descriptor = klass.__dict__["scaleGridTop"]
            break
    assert isinstance(descriptor, property)

def test_justificationstyle_exists():
    # Check that the Enumeration exists
    assert JustificationStyle is not None

def test_justificationstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JustificationStyle]
    expected_literals = [
        "pushOutOnly",
        "auto",
        "pushInKinsoku",
        "prioritizeLeastAdjustment",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JustificationStyle"

def test_leadingmodel_exists():
    # Check that the Enumeration exists
    assert LeadingModel is not None

def test_leadingmodel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LeadingModel]
    expected_literals = [
        "ascentDescentUp",
        "auto",
        "romanUp",
        "ideographicTopDown",
        "ideographicTopUp",
        "ideographicCenterDown",
        "ideographicCenterUp",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LeadingModel"

def test_whitespacecollapse_exists():
    # Check that the Enumeration exists
    assert WhitespaceCollapse is not None

def test_whitespacecollapse_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WhitespaceCollapse]
    expected_literals = [
        "PRESERVE",
        "COLLAPSE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WhitespaceCollapse"

def test_justificationrule_exists():
    # Check that the Enumeration exists
    assert JustificationRule is not None

def test_justificationrule_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JustificationRule]
    expected_literals = [
        "auto",
        "space",
        "eastAsian",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JustificationRule"

def test_joint_exists():
    # Check that the Enumeration exists
    assert Joint is not None

def test_joint_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Joint]
    expected_literals = [
        "MITER",
        "ROUND",
        "BEVEL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Joint"

def test_textrotation_exists():
    # Check that the Enumeration exists
    assert TextRotation is not None

def test_textrotation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextRotation]
    expected_literals = [
        "rotate90",
        "auto",
        "rotate180",
        "rotate270",
        "rotate0",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextRotation"

def test_dominantbaseline_exists():
    # Check that the Enumeration exists
    assert DominantBaseline is not None

def test_dominantbaseline_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DominantBaseline]
    expected_literals = [
        "ascent",
        "auto",
        "ideographicTop",
        "roman",
        "descent",
        "ideographicCenter",
        "ideographicBottom",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DominantBaseline"

def test_digitwidth_exists():
    # Check that the Enumeration exists
    assert DigitWidth is not None

def test_digitwidth_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DigitWidth]
    expected_literals = [
        "tabular",
        "proportional",
        "default",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DigitWidth"

def test_verticalalign_exists():
    # Check that the Enumeration exists
    assert VerticalAlign is not None

def test_verticalalign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VerticalAlign]
    expected_literals = [
        "inherit",
        "justify",
        "top",
        "middle",
        "bottom",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VerticalAlign"

def test_kerning_exists():
    # Check that the Enumeration exists
    assert Kerning is not None

def test_kerning_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Kerning]
    expected_literals = [
        "OFF",
        "ON",
        "AUTO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Kerning"

def test_bevelfiltertype_exists():
    # Check that the Enumeration exists
    assert BevelFilterType is not None

def test_bevelfiltertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BevelFilterType]
    expected_literals = [
        "FULL",
        "OUTER",
        "INNER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BevelFilterType"

def test_scalemode_exists():
    # Check that the Enumeration exists
    assert ScaleMode is not None

def test_scalemode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScaleMode]
    expected_literals = [
        "HORIZONTAL",
        "NONE",
        "NORMAL",
        "VERTICAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScaleMode"

def test_fontweight_exists():
    # Check that the Enumeration exists
    assert FontWeight is not None

def test_fontweight_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontWeight]
    expected_literals = [
        "BOLD",
        "NORMAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontWeight"

def test_typographiccase_exists():
    # Check that the Enumeration exists
    assert TypographicCase is not None

def test_typographiccase_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypographicCase]
    expected_literals = [
        "lowercase",
        "capsToSmallCaps",
        "default",
        "uppercase",
        "lowercaseToSmallCaps",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypographicCase"

def test_spreadmethod_exists():
    # Check that the Enumeration exists
    assert SpreadMethod is not None

def test_spreadmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SpreadMethod]
    expected_literals = [
        "pad",
        "reflect",
        "repeat",
        "NOT_SET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SpreadMethod"

def test_alignmentbaseline_exists():
    # Check that the Enumeration exists
    assert AlignmentBaseline is not None

def test_alignmentbaseline_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AlignmentBaseline]
    expected_literals = [
        "descent",
        "roman",
        "useDominantBaseline",
        "ideographicCenter",
        "ideographicBottom",
        "auto",
        "ascent",
        "ideographicTop",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AlignmentBaseline"

def test_interpolationmethod_exists():
    # Check that the Enumeration exists
    assert InterpolationMethod is not None

def test_interpolationmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InterpolationMethod]
    expected_literals = [
        "rgb",
        "linearRGB",
        "NOT_SET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InterpolationMethod"

def test_breakopportunity_exists():
    # Check that the Enumeration exists
    assert BreakOpportunity is not None

def test_breakopportunity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BreakOpportunity]
    expected_literals = [
        "all",
        "auto",
        "none",
        "any",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BreakOpportunity"

def test_blockprogression_exists():
    # Check that the Enumeration exists
    assert BlockProgression is not None

def test_blockprogression_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BlockProgression]
    expected_literals = [
        "tb",
        "rl",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BlockProgression"

def test_textjustify_exists():
    # Check that the Enumeration exists
    assert TextJustify is not None

def test_textjustify_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextJustify]
    expected_literals = [
        "distribute",
        "interWord",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextJustify"

def test_fillmode_exists():
    # Check that the Enumeration exists
    assert FillMode is not None

def test_fillmode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FillMode]
    expected_literals = [
        "CLIP",
        "REPEAT",
        "SCALE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FillMode"

def test_winding_exists():
    # Check that the Enumeration exists
    assert Winding is not None

def test_winding_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Winding]
    expected_literals = [
        "nonZero",
        "evenOdd",
        "NOT_SET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Winding"

def test_cap_exists():
    # Check that the Enumeration exists
    assert Cap is not None

def test_cap_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Cap]
    expected_literals = [
        "SQUARE",
        "NONE",
        "ROUND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Cap"

def test_textalign_exists():
    # Check that the Enumeration exists
    assert TextAlign is not None

def test_textalign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextAlign]
    expected_literals = [
        "start",
        "justify",
        "left",
        "right",
        "end",
        "center",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextAlign"

def test_blendmode_exists():
    # Check that the Enumeration exists
    assert BlendMode is not None

def test_blendmode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BlendMode]
    expected_literals = [
        "lighten",
        "overlay",
        "difference",
        "darken",
        "invert",
        "layer",
        "multiply",
        "normal",
        "subtract",
        "add",
        "alpha",
        "erase",
        "hardlight",
        "shader",
        "screen",
        "NOT_SET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BlendMode"

def test_fontstyle_exists():
    # Check that the Enumeration exists
    assert FontStyle is not None

def test_fontstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontStyle]
    expected_literals = [
        "ITALIC",
        "NORMAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontStyle"

def test_ligaturelevel_exists():
    # Check that the Enumeration exists
    assert LigatureLevel is not None

def test_ligaturelevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LigatureLevel]
    expected_literals = [
        "minimum",
        "exotic",
        "uncommon",
        "common",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LigatureLevel"

def test_linebreak_exists():
    # Check that the Enumeration exists
    assert LineBreak is not None

def test_linebreak_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineBreak]
    expected_literals = [
        "toFit",
        "explicit",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineBreak"

def test_masktype_exists():
    # Check that the Enumeration exists
    assert MaskType is not None

def test_masktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MaskType]
    expected_literals = [
        "ALPHA",
        "CLIP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MaskType"

def test_digitcase_exists():
    # Check that the Enumeration exists
    assert DigitCase is not None

def test_digitcase_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DigitCase]
    expected_literals = [
        "default",
        "oldStyle",
        "lining",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DigitCase"

def test_textdecoration_exists():
    # Check that the Enumeration exists
    assert TextDecoration is not None

def test_textdecoration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextDecoration]
    expected_literals = [
        "NONE",
        "UNDERLINE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextDecoration"


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
fxg::FXGElement_strategy = st.builds(
    fxg::FXGElement,
)
fxg::GradientBevelFilter_strategy = st.builds(
    fxg::GradientBevelFilter,
    angle=
        safe_text,
    blurX=
        safe_text,
    distance=
        safe_text,
    type=
        safe_text,
    blurY=
        safe_text,
    strength=
        safe_text,
    quality=
        safe_text,
    knockout=
        safe_text
)
fxg::GradientGlowFilter_strategy = st.builds(
    fxg::GradientGlowFilter,
    strength=
        safe_text,
    distance=
        safe_text,
    knockout=
        safe_text,
    blurY=
        safe_text,
    inner=
        safe_text,
    quality=
        safe_text,
    blurX=
        safe_text,
    angle=
        safe_text
)
Filter_strategy = st.builds(
    Filter,
)
fxg::ColorMatrixFilter_strategy = st.builds(
    fxg::ColorMatrixFilter,
    matrix=
        safe_text
)
fxg::BevelFilter_strategy = st.builds(
    fxg::BevelFilter,
    highlightAlpha=
        safe_text,
    blurX=
        safe_text,
    blurY=
        safe_text,
    strength=
        safe_text,
    knockout=
        safe_text,
    distance=
        safe_text,
    angle=
        safe_text,
    highlightColor=
        safe_text,
    quality=
        safe_text,
    type=
        safe_text,
    shadowAlpha=
        safe_text,
    shadowColor=
        safe_text
)
fxg::DropShadowFilter_strategy = st.builds(
    fxg::DropShadowFilter,
    inner=
        safe_text,
    distance=
        safe_text,
    hideObject=
        safe_text,
    alpha=
        safe_text,
    quality=
        safe_text,
    strength=
        safe_text,
    knockout=
        safe_text,
    blurX=
        safe_text,
    blurY=
        safe_text,
    color=
        safe_text,
    angle=
        safe_text
)
fxg::BlurFilter_strategy = st.builds(
    fxg::BlurFilter,
    quality=
        safe_text,
    blurY=
        safe_text,
    blurX=
        safe_text
)
fxg::RadialGradientStroke_strategy = st.builds(
    fxg::RadialGradientStroke,
    caps=
        safe_text,
    spreadMethod=
        safe_text,
    pixelHinting=
        safe_text,
    y=
        safe_text,
    focalPointRatio=
        safe_text,
    rotation=
        safe_text,
    scaleX=
        safe_text,
    scaleY=
        safe_text,
    weight=
        safe_text,
    interpolationMethod=
        safe_text,
    x=
        safe_text,
    scaleMode=
        safe_text,
    joints=
        safe_text,
    miterLimit=
        safe_text
)
fxg::LinearGradient_strategy = st.builds(
    fxg::LinearGradient,
    rotation=
        safe_text,
    scaleX=
        safe_text,
    interpolationMethod=
        safe_text,
    spreadMethod=
        safe_text,
    y=
        safe_text,
    x=
        safe_text
)
fxg::LinearGradientStroke_strategy = st.builds(
    fxg::LinearGradientStroke,
    weight=
        safe_text,
    joints=
        safe_text,
    scaleMode=
        safe_text,
    scaleX=
        safe_text,
    miterLimit=
        safe_text,
    x=
        safe_text,
    spreadMethod=
        safe_text,
    rotation=
        safe_text,
    caps=
        safe_text,
    interpolationMethod=
        safe_text,
    pixelHinting=
        safe_text,
    y=
        safe_text
)
Stroke_strategy = st.builds(
    Stroke,
)
fxg::SolidColorStroke_strategy = st.builds(
    fxg::SolidColorStroke,
    miterLimit=
        safe_text,
    alpha=
        safe_text,
    caps=
        safe_text,
    scaleMode=
        safe_text,
    weight=
        safe_text,
    color=
        safe_text,
    pixelHinting=
        safe_text,
    joints=
        safe_text
)
fxg::RadialGradient_strategy = st.builds(
    fxg::RadialGradient,
    focalPointRatio=
        safe_text,
    interpolationMethod=
        safe_text,
    y=
        safe_text,
    scaleY=
        safe_text,
    x=
        safe_text,
    rotation=
        safe_text,
    spreadMethod=
        safe_text,
    scaleX=
        safe_text
)
Fill_strategy = st.builds(
    Fill,
)
fxg::BitmapFill_strategy = st.builds(
    fxg::BitmapFill,
    fillMode=
        safe_text,
    x=
        safe_text,
    scaleY=
        safe_text,
    y=
        safe_text,
    scaleX=
        safe_text,
    source=
        safe_text,
    rotation=
        safe_text
)
fxg::SolidColor_strategy = st.builds(
    fxg::SolidColor,
    alpha=
        safe_text,
    color=
        safe_text
)
fxg::linkActiveFormat_strategy = st.builds(
    fxg::linkActiveFormat,
)
RichTextContentContainer_strategy = st.builds(
    RichTextContentContainer,
)
fxg::CharacterAttributes_strategy = st.builds(
    fxg::CharacterAttributes,
    color=
        safe_text,
    locale=
        safe_text,
    lineHeight=
        safe_text,
    fontWeight=
        safe_text,
    textRotation=
        safe_text,
    trackingRight=
        safe_text,
    typographicCase=
        safe_text,
    baselineShift=
        safe_text,
    trackingLeft=
        safe_text,
    dominantBaseline=
        safe_text,
    breakOpportunity=
        safe_text,
    digitCase=
        safe_text,
    lineThrough=
        safe_text,
    whiteSpaceCollapse=
        safe_text,
    fontStyle=
        safe_text,
    fontSize=
        safe_text,
    textAlpha=
        safe_text,
    backgroundColor=
        safe_text,
    kerning=
        safe_text,
    backgroundAlpha=
        safe_text,
    digitWidth=
        safe_text,
    ligatureLevel=
        safe_text,
    textDecoration=
        safe_text,
    alignmentBaseline=
        safe_text,
    fontFamily=
        safe_text
)
fxg::ContainerAttributes_strategy = st.builds(
    fxg::ContainerAttributes,
    paddingLeft=
        safe_text,
    columnGap=
        safe_text,
    columnWidth=
        safe_text,
    firstBaselineOffset=
        safe_text,
    verticalAlign=
        safe_text,
    lineBreak=
        safe_text,
    paddingBottom=
        safe_text,
    paddingRight=
        safe_text,
    blockProgression=
        safe_text,
    paddingTop=
        safe_text,
    columnCount=
        safe_text
)
fxg::ParagraphAttributes_strategy = st.builds(
    fxg::ParagraphAttributes,
    paragraphSpaceAfter=
        safe_text,
    textAlignLast=
        safe_text,
    textIndent=
        safe_text,
    paragraphStartIndent=
        safe_text,
    leadingModel=
        safe_text,
    tabStops=
        safe_text,
    textJustify=
        safe_text,
    justificationRule=
        safe_text,
    justificationStyle=
        safe_text,
    textAlign=
        safe_text,
    paragraphSpaceBefore=
        safe_text,
    paragraphEndIndent=
        safe_text
)
RichTextContent_strategy = st.builds(
    RichTextContent,
)
fxg::linkHoverFormat_strategy = st.builds(
    fxg::linkHoverFormat,
)
fxg::span_strategy = st.builds(
    fxg::span,
)
fxg::tab_strategy = st.builds(
    fxg::tab,
)
fxg::linkNormalFormat_strategy = st.builds(
    fxg::linkNormalFormat,
)
fxg::a_strategy = st.builds(
    fxg::a,
)
fxg::rawtext_strategy = st.builds(
    fxg::rawtext,
    _text=
        safe_text
)
fxg::img_strategy = st.builds(
    fxg::img,
)
fxg::div_strategy = st.builds(
    fxg::div,
)
fxg::br_strategy = st.builds(
    fxg::br,
)
fxg::tcy_strategy = st.builds(
    fxg::tcy,
)
fxg::RichTextContentContainer_strategy = st.builds(
    fxg::RichTextContentContainer,
)
fxg::RichTextContent_strategy = st.builds(
    fxg::RichTextContent,
)
CharacterAttributes_strategy = st.builds(
    CharacterAttributes,
)
ContainerAttributes_strategy = st.builds(
    ContainerAttributes,
)
ParagraphAttributes_strategy = st.builds(
    ParagraphAttributes,
)
fxg::p_strategy = st.builds(
    fxg::p,
)
Shape_strategy = st.builds(
    Shape,
)
fxg::Ellipse_strategy = st.builds(
    fxg::Ellipse,
    scaleX=
        safe_text,
    visible=
        safe_text,
    alpha=
        safe_text,
    width=
        safe_text,
    x=
        safe_text,
    blendMode=
        safe_text,
    scaleY=
        safe_text,
    height=
        safe_text,
    y=
        safe_text,
    rotation=
        safe_text
)
fxg::Line_strategy = st.builds(
    fxg::Line,
    yFrom=
        safe_text,
    rotation=
        safe_text,
    xTo=
        safe_text,
    xFrom=
        safe_text,
    yTo=
        safe_text,
    x=
        safe_text,
    scaleY=
        safe_text,
    y=
        safe_text,
    scaleX=
        safe_text,
    id=
        safe_text,
    visible=
        safe_text,
    alpha=
        safe_text,
    blendMode=
        safe_text,
    maskType=
        safe_text
)
fxg::Rect_strategy = st.builds(
    fxg::Rect,
    bottomRightRadiusY=
        safe_text,
    radiusY=
        safe_text,
    bottomLeftRadiusX=
        safe_text,
    x=
        safe_text,
    rotation=
        safe_text,
    scaleY=
        safe_text,
    radiusX=
        safe_text,
    height=
        safe_text,
    scaleX=
        safe_text,
    topRightRadiusX=
        safe_text,
    alpha=
        safe_text,
    topLeftRadiusY=
        safe_text,
    topLeftRadiusX=
        safe_text,
    topRightRadiusY=
        safe_text,
    blendMode=
        safe_text,
    y=
        safe_text,
    bottomRightRadiusX=
        safe_text,
    visible=
        safe_text,
    bottomLeftRadiusY=
        safe_text,
    width=
        safe_text
)
fxg::Definition_strategy = st.builds(
    fxg::Definition,
    name=
        safe_text
)
FXGElement_strategy = st.builds(
    FXGElement,
)
fxg::Transform_strategy = st.builds(
    fxg::Transform,
)
fxg::ContainerElement_strategy = st.builds(
    fxg::ContainerElement,
)
fxg::GradientEntry_strategy = st.builds(
    fxg::GradientEntry,
    alpha=
        safe_text,
    ratio=
        safe_text,
    color=
        safe_text
)
fxg::ColorTransform_strategy = st.builds(
    fxg::ColorTransform,
    alphaMultiplier=
        safe_text,
    redOffset=
        safe_text,
    greenOffset=
        safe_text,
    greenMultiplier=
        safe_text,
    blueOffset=
        safe_text,
    alphaOffset=
        safe_text,
    redMultiplier=
        safe_text,
    blueMultiplier=
        safe_text
)
fxg::Stroke_strategy = st.builds(
    fxg::Stroke,
)
fxg::PlaceObject_strategy = st.builds(
    fxg::PlaceObject,
    id=
        safe_text
)
fxg::BitmapImage_strategy = st.builds(
    fxg::BitmapImage,
    fillMode=
        safe_text,
    scaleX=
        safe_text,
    visible=
        safe_text,
    alpha=
        safe_text,
    blendMode=
        safe_text,
    y=
        safe_text,
    rotation=
        safe_text,
    height=
        safe_text,
    source=
        safe_text,
    x=
        safe_text,
    width=
        safe_text,
    scaleY=
        safe_text
)
fxg::Fill_strategy = st.builds(
    fxg::Fill,
)
fxg::Matrix_strategy = st.builds(
    fxg::Matrix,
    a=
        safe_text,
    c=
        safe_text,
    ty=
        safe_text,
    b=
        safe_text,
    tx=
        safe_text,
    d=
        safe_text
)
fxg::Filter_strategy = st.builds(
    fxg::Filter,
)
fxg::RichText_strategy = st.builds(
    fxg::RichText,
    scaleY=
        safe_text,
    alpha=
        safe_text,
    width=
        safe_text,
    x=
        safe_text,
    visible=
        safe_text,
    maskType=
        safe_text,
    scaleX=
        safe_text,
    _tempcontent=
        safe_text,
    blendMode=
        safe_text,
    id=
        safe_text,
    y=
        safe_text,
    height=
        safe_text,
    rotation=
        safe_text
)
fxg::Path_strategy = st.builds(
    fxg::Path,
    y=
        safe_text,
    winding=
        safe_text,
    blendMode=
        safe_text,
    rotation=
        safe_text,
    data=
        safe_text,
    scaleX=
        safe_text,
    visible=
        safe_text,
    scaleY=
        safe_text,
    alpha=
        safe_text,
    x=
        safe_text
)
fxg::Shape_strategy = st.builds(
    fxg::Shape,
)
fxg::Private_strategy = st.builds(
    fxg::Private,
)
fxg::Library_strategy = st.builds(
    fxg::Library,
)
fxg::Group_strategy = st.builds(
    fxg::Group,
    scaleGridTop=
        safe_text,
    scaleGridLeft=
        safe_text,
    scaleGridRight=
        safe_text,
    transformX=
        safe_text,
    scaleY=
        safe_text,
    y=
        safe_text,
    id=
        safe_text,
    visible=
        safe_text,
    scaleGridBottom=
        safe_text,
    maskType=
        safe_text,
    rotation=
        safe_text,
    transformY=
        safe_text,
    blendMode=
        safe_text,
    alpha=
        safe_text,
    x=
        safe_text,
    scaleX=
        safe_text
)
fxg::Graphic_strategy = st.builds(
    fxg::Graphic,
    scaleGridRight=
        safe_text,
    scaleGridLeft=
        safe_text,
    viewHeight=
        st.integers(),
    viewWidth=
        st.integers(),
    scaleGridBottom=
        safe_text,
    version=
        safe_text,
    scaleGridTop=
        safe_text
)

@given(instance=fxg::FXGElement_strategy)
@settings(max_examples=50)
def test_fxg::fxgelement_instantiation(instance):
    assert isinstance(instance, fxg::FXGElement)

@given(instance=fxg::GradientBevelFilter_strategy)
@settings(max_examples=50)
def test_fxg::gradientbevelfilter_instantiation(instance):
    assert isinstance(instance, fxg::GradientBevelFilter)

@given(instance=fxg::GradientBevelFilter_strategy)
def test_fxg::gradientbevelfilter_angle_type(instance):
    assert isinstance(instance.angle, str)


@given(instance=fxg::GradientBevelFilter_strategy)
def test_fxg::gradientbevelfilter_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=fxg::GradientBevelFilter_strategy)
def test_fxg::gradientbevelfilter_blurX_type(instance):
    assert isinstance(instance.blurX, str)


@given(instance=fxg::GradientBevelFilter_strategy)
def test_fxg::gradientbevelfilter_blurX_setter(instance):
    original = instance.blurX
    instance.blurX = original
    assert instance.blurX == original

@given(instance=fxg::GradientBevelFilter_strategy)
def test_fxg::gradientbevelfilter_distance_type(instance):
    assert isinstance(instance.distance, str)


@given(instance=fxg::GradientBevelFilter_strategy)
def test_fxg::gradientbevelfilter_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=fxg::GradientBevelFilter_strategy)
def test_fxg::gradientbevelfilter_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=fxg::GradientBevelFilter_strategy)
def test_fxg::gradientbevelfilter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=fxg::GradientBevelFilter_strategy)
def test_fxg::gradientbevelfilter_blurY_type(instance):
    assert isinstance(instance.blurY, str)


@given(instance=fxg::GradientBevelFilter_strategy)
def test_fxg::gradientbevelfilter_blurY_setter(instance):
    original = instance.blurY
    instance.blurY = original
    assert instance.blurY == original

@given(instance=fxg::GradientBevelFilter_strategy)
def test_fxg::gradientbevelfilter_strength_type(instance):
    assert isinstance(instance.strength, str)


@given(instance=fxg::GradientBevelFilter_strategy)
def test_fxg::gradientbevelfilter_strength_setter(instance):
    original = instance.strength
    instance.strength = original
    assert instance.strength == original

@given(instance=fxg::GradientBevelFilter_strategy)
def test_fxg::gradientbevelfilter_quality_type(instance):
    assert isinstance(instance.quality, str)


@given(instance=fxg::GradientBevelFilter_strategy)
def test_fxg::gradientbevelfilter_quality_setter(instance):
    original = instance.quality
    instance.quality = original
    assert instance.quality == original

@given(instance=fxg::GradientBevelFilter_strategy)
def test_fxg::gradientbevelfilter_knockout_type(instance):
    assert isinstance(instance.knockout, str)


@given(instance=fxg::GradientBevelFilter_strategy)
def test_fxg::gradientbevelfilter_knockout_setter(instance):
    original = instance.knockout
    instance.knockout = original
    assert instance.knockout == original

@given(instance=fxg::GradientGlowFilter_strategy)
@settings(max_examples=50)
def test_fxg::gradientglowfilter_instantiation(instance):
    assert isinstance(instance, fxg::GradientGlowFilter)

@given(instance=fxg::GradientGlowFilter_strategy)
def test_fxg::gradientglowfilter_strength_type(instance):
    assert isinstance(instance.strength, str)


@given(instance=fxg::GradientGlowFilter_strategy)
def test_fxg::gradientglowfilter_strength_setter(instance):
    original = instance.strength
    instance.strength = original
    assert instance.strength == original

@given(instance=fxg::GradientGlowFilter_strategy)
def test_fxg::gradientglowfilter_distance_type(instance):
    assert isinstance(instance.distance, str)


@given(instance=fxg::GradientGlowFilter_strategy)
def test_fxg::gradientglowfilter_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=fxg::GradientGlowFilter_strategy)
def test_fxg::gradientglowfilter_knockout_type(instance):
    assert isinstance(instance.knockout, str)


@given(instance=fxg::GradientGlowFilter_strategy)
def test_fxg::gradientglowfilter_knockout_setter(instance):
    original = instance.knockout
    instance.knockout = original
    assert instance.knockout == original

@given(instance=fxg::GradientGlowFilter_strategy)
def test_fxg::gradientglowfilter_blurY_type(instance):
    assert isinstance(instance.blurY, str)


@given(instance=fxg::GradientGlowFilter_strategy)
def test_fxg::gradientglowfilter_blurY_setter(instance):
    original = instance.blurY
    instance.blurY = original
    assert instance.blurY == original

@given(instance=fxg::GradientGlowFilter_strategy)
def test_fxg::gradientglowfilter_inner_type(instance):
    assert isinstance(instance.inner, str)


@given(instance=fxg::GradientGlowFilter_strategy)
def test_fxg::gradientglowfilter_inner_setter(instance):
    original = instance.inner
    instance.inner = original
    assert instance.inner == original

@given(instance=fxg::GradientGlowFilter_strategy)
def test_fxg::gradientglowfilter_quality_type(instance):
    assert isinstance(instance.quality, str)


@given(instance=fxg::GradientGlowFilter_strategy)
def test_fxg::gradientglowfilter_quality_setter(instance):
    original = instance.quality
    instance.quality = original
    assert instance.quality == original

@given(instance=fxg::GradientGlowFilter_strategy)
def test_fxg::gradientglowfilter_blurX_type(instance):
    assert isinstance(instance.blurX, str)


@given(instance=fxg::GradientGlowFilter_strategy)
def test_fxg::gradientglowfilter_blurX_setter(instance):
    original = instance.blurX
    instance.blurX = original
    assert instance.blurX == original

@given(instance=fxg::GradientGlowFilter_strategy)
def test_fxg::gradientglowfilter_angle_type(instance):
    assert isinstance(instance.angle, str)


@given(instance=fxg::GradientGlowFilter_strategy)
def test_fxg::gradientglowfilter_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=Filter_strategy)
@settings(max_examples=50)
def test_filter_instantiation(instance):
    assert isinstance(instance, Filter)

@given(instance=fxg::ColorMatrixFilter_strategy)
@settings(max_examples=50)
def test_fxg::colormatrixfilter_instantiation(instance):
    assert isinstance(instance, fxg::ColorMatrixFilter)

@given(instance=fxg::ColorMatrixFilter_strategy)
def test_fxg::colormatrixfilter_matrix_type(instance):
    assert isinstance(instance.matrix, str)


@given(instance=fxg::ColorMatrixFilter_strategy)
def test_fxg::colormatrixfilter_matrix_setter(instance):
    original = instance.matrix
    instance.matrix = original
    assert instance.matrix == original

@given(instance=fxg::BevelFilter_strategy)
@settings(max_examples=50)
def test_fxg::bevelfilter_instantiation(instance):
    assert isinstance(instance, fxg::BevelFilter)

@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_highlightAlpha_type(instance):
    assert isinstance(instance.highlightAlpha, str)


@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_highlightAlpha_setter(instance):
    original = instance.highlightAlpha
    instance.highlightAlpha = original
    assert instance.highlightAlpha == original

@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_blurX_type(instance):
    assert isinstance(instance.blurX, str)


@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_blurX_setter(instance):
    original = instance.blurX
    instance.blurX = original
    assert instance.blurX == original

@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_blurY_type(instance):
    assert isinstance(instance.blurY, str)


@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_blurY_setter(instance):
    original = instance.blurY
    instance.blurY = original
    assert instance.blurY == original

@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_strength_type(instance):
    assert isinstance(instance.strength, str)


@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_strength_setter(instance):
    original = instance.strength
    instance.strength = original
    assert instance.strength == original

@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_knockout_type(instance):
    assert isinstance(instance.knockout, str)


@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_knockout_setter(instance):
    original = instance.knockout
    instance.knockout = original
    assert instance.knockout == original

@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_distance_type(instance):
    assert isinstance(instance.distance, str)


@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_angle_type(instance):
    assert isinstance(instance.angle, str)


@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_highlightColor_type(instance):
    assert isinstance(instance.highlightColor, str)


@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_highlightColor_setter(instance):
    original = instance.highlightColor
    instance.highlightColor = original
    assert instance.highlightColor == original

@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_quality_type(instance):
    assert isinstance(instance.quality, str)


@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_quality_setter(instance):
    original = instance.quality
    instance.quality = original
    assert instance.quality == original

@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_shadowAlpha_type(instance):
    assert isinstance(instance.shadowAlpha, str)


@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_shadowAlpha_setter(instance):
    original = instance.shadowAlpha
    instance.shadowAlpha = original
    assert instance.shadowAlpha == original

@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_shadowColor_type(instance):
    assert isinstance(instance.shadowColor, str)


@given(instance=fxg::BevelFilter_strategy)
def test_fxg::bevelfilter_shadowColor_setter(instance):
    original = instance.shadowColor
    instance.shadowColor = original
    assert instance.shadowColor == original

@given(instance=fxg::DropShadowFilter_strategy)
@settings(max_examples=50)
def test_fxg::dropshadowfilter_instantiation(instance):
    assert isinstance(instance, fxg::DropShadowFilter)

@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_inner_type(instance):
    assert isinstance(instance.inner, str)


@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_inner_setter(instance):
    original = instance.inner
    instance.inner = original
    assert instance.inner == original

@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_distance_type(instance):
    assert isinstance(instance.distance, str)


@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_hideObject_type(instance):
    assert isinstance(instance.hideObject, str)


@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_hideObject_setter(instance):
    original = instance.hideObject
    instance.hideObject = original
    assert instance.hideObject == original

@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_alpha_type(instance):
    assert isinstance(instance.alpha, str)


@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original

@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_quality_type(instance):
    assert isinstance(instance.quality, str)


@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_quality_setter(instance):
    original = instance.quality
    instance.quality = original
    assert instance.quality == original

@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_strength_type(instance):
    assert isinstance(instance.strength, str)


@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_strength_setter(instance):
    original = instance.strength
    instance.strength = original
    assert instance.strength == original

@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_knockout_type(instance):
    assert isinstance(instance.knockout, str)


@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_knockout_setter(instance):
    original = instance.knockout
    instance.knockout = original
    assert instance.knockout == original

@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_blurX_type(instance):
    assert isinstance(instance.blurX, str)


@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_blurX_setter(instance):
    original = instance.blurX
    instance.blurX = original
    assert instance.blurX == original

@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_blurY_type(instance):
    assert isinstance(instance.blurY, str)


@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_blurY_setter(instance):
    original = instance.blurY
    instance.blurY = original
    assert instance.blurY == original

@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_angle_type(instance):
    assert isinstance(instance.angle, str)


@given(instance=fxg::DropShadowFilter_strategy)
def test_fxg::dropshadowfilter_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=fxg::BlurFilter_strategy)
@settings(max_examples=50)
def test_fxg::blurfilter_instantiation(instance):
    assert isinstance(instance, fxg::BlurFilter)

@given(instance=fxg::BlurFilter_strategy)
def test_fxg::blurfilter_quality_type(instance):
    assert isinstance(instance.quality, str)


@given(instance=fxg::BlurFilter_strategy)
def test_fxg::blurfilter_quality_setter(instance):
    original = instance.quality
    instance.quality = original
    assert instance.quality == original

@given(instance=fxg::BlurFilter_strategy)
def test_fxg::blurfilter_blurY_type(instance):
    assert isinstance(instance.blurY, str)


@given(instance=fxg::BlurFilter_strategy)
def test_fxg::blurfilter_blurY_setter(instance):
    original = instance.blurY
    instance.blurY = original
    assert instance.blurY == original

@given(instance=fxg::BlurFilter_strategy)
def test_fxg::blurfilter_blurX_type(instance):
    assert isinstance(instance.blurX, str)


@given(instance=fxg::BlurFilter_strategy)
def test_fxg::blurfilter_blurX_setter(instance):
    original = instance.blurX
    instance.blurX = original
    assert instance.blurX == original

@given(instance=fxg::RadialGradientStroke_strategy)
@settings(max_examples=50)
def test_fxg::radialgradientstroke_instantiation(instance):
    assert isinstance(instance, fxg::RadialGradientStroke)

@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_caps_type(instance):
    assert isinstance(instance.caps, str)


@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_caps_setter(instance):
    original = instance.caps
    instance.caps = original
    assert instance.caps == original

@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_spreadMethod_type(instance):
    assert isinstance(instance.spreadMethod, str)


@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_spreadMethod_setter(instance):
    original = instance.spreadMethod
    instance.spreadMethod = original
    assert instance.spreadMethod == original

@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_pixelHinting_type(instance):
    assert isinstance(instance.pixelHinting, str)


@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_pixelHinting_setter(instance):
    original = instance.pixelHinting
    instance.pixelHinting = original
    assert instance.pixelHinting == original

@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_focalPointRatio_type(instance):
    assert isinstance(instance.focalPointRatio, str)


@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_focalPointRatio_setter(instance):
    original = instance.focalPointRatio
    instance.focalPointRatio = original
    assert instance.focalPointRatio == original

@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_rotation_type(instance):
    assert isinstance(instance.rotation, str)


@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original

@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_scaleX_type(instance):
    assert isinstance(instance.scaleX, str)


@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original

@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_scaleY_type(instance):
    assert isinstance(instance.scaleY, str)


@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original

@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_weight_type(instance):
    assert isinstance(instance.weight, str)


@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_interpolationMethod_type(instance):
    assert isinstance(instance.interpolationMethod, str)


@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_interpolationMethod_setter(instance):
    original = instance.interpolationMethod
    instance.interpolationMethod = original
    assert instance.interpolationMethod == original

@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_scaleMode_type(instance):
    assert isinstance(instance.scaleMode, str)


@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_scaleMode_setter(instance):
    original = instance.scaleMode
    instance.scaleMode = original
    assert instance.scaleMode == original

@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_joints_type(instance):
    assert isinstance(instance.joints, str)


@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_joints_setter(instance):
    original = instance.joints
    instance.joints = original
    assert instance.joints == original

@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_miterLimit_type(instance):
    assert isinstance(instance.miterLimit, str)


@given(instance=fxg::RadialGradientStroke_strategy)
def test_fxg::radialgradientstroke_miterLimit_setter(instance):
    original = instance.miterLimit
    instance.miterLimit = original
    assert instance.miterLimit == original

@given(instance=fxg::LinearGradient_strategy)
@settings(max_examples=50)
def test_fxg::lineargradient_instantiation(instance):
    assert isinstance(instance, fxg::LinearGradient)

@given(instance=fxg::LinearGradient_strategy)
def test_fxg::lineargradient_rotation_type(instance):
    assert isinstance(instance.rotation, str)


@given(instance=fxg::LinearGradient_strategy)
def test_fxg::lineargradient_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original

@given(instance=fxg::LinearGradient_strategy)
def test_fxg::lineargradient_scaleX_type(instance):
    assert isinstance(instance.scaleX, str)


@given(instance=fxg::LinearGradient_strategy)
def test_fxg::lineargradient_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original

@given(instance=fxg::LinearGradient_strategy)
def test_fxg::lineargradient_interpolationMethod_type(instance):
    assert isinstance(instance.interpolationMethod, str)


@given(instance=fxg::LinearGradient_strategy)
def test_fxg::lineargradient_interpolationMethod_setter(instance):
    original = instance.interpolationMethod
    instance.interpolationMethod = original
    assert instance.interpolationMethod == original

@given(instance=fxg::LinearGradient_strategy)
def test_fxg::lineargradient_spreadMethod_type(instance):
    assert isinstance(instance.spreadMethod, str)


@given(instance=fxg::LinearGradient_strategy)
def test_fxg::lineargradient_spreadMethod_setter(instance):
    original = instance.spreadMethod
    instance.spreadMethod = original
    assert instance.spreadMethod == original

@given(instance=fxg::LinearGradient_strategy)
def test_fxg::lineargradient_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=fxg::LinearGradient_strategy)
def test_fxg::lineargradient_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=fxg::LinearGradient_strategy)
def test_fxg::lineargradient_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=fxg::LinearGradient_strategy)
def test_fxg::lineargradient_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=fxg::LinearGradientStroke_strategy)
@settings(max_examples=50)
def test_fxg::lineargradientstroke_instantiation(instance):
    assert isinstance(instance, fxg::LinearGradientStroke)

@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_weight_type(instance):
    assert isinstance(instance.weight, str)


@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_joints_type(instance):
    assert isinstance(instance.joints, str)


@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_joints_setter(instance):
    original = instance.joints
    instance.joints = original
    assert instance.joints == original

@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_scaleMode_type(instance):
    assert isinstance(instance.scaleMode, str)


@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_scaleMode_setter(instance):
    original = instance.scaleMode
    instance.scaleMode = original
    assert instance.scaleMode == original

@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_scaleX_type(instance):
    assert isinstance(instance.scaleX, str)


@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original

@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_miterLimit_type(instance):
    assert isinstance(instance.miterLimit, str)


@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_miterLimit_setter(instance):
    original = instance.miterLimit
    instance.miterLimit = original
    assert instance.miterLimit == original

@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_spreadMethod_type(instance):
    assert isinstance(instance.spreadMethod, str)


@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_spreadMethod_setter(instance):
    original = instance.spreadMethod
    instance.spreadMethod = original
    assert instance.spreadMethod == original

@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_rotation_type(instance):
    assert isinstance(instance.rotation, str)


@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original

@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_caps_type(instance):
    assert isinstance(instance.caps, str)


@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_caps_setter(instance):
    original = instance.caps
    instance.caps = original
    assert instance.caps == original

@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_interpolationMethod_type(instance):
    assert isinstance(instance.interpolationMethod, str)


@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_interpolationMethod_setter(instance):
    original = instance.interpolationMethod
    instance.interpolationMethod = original
    assert instance.interpolationMethod == original

@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_pixelHinting_type(instance):
    assert isinstance(instance.pixelHinting, str)


@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_pixelHinting_setter(instance):
    original = instance.pixelHinting
    instance.pixelHinting = original
    assert instance.pixelHinting == original

@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=fxg::LinearGradientStroke_strategy)
def test_fxg::lineargradientstroke_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=Stroke_strategy)
@settings(max_examples=50)
def test_stroke_instantiation(instance):
    assert isinstance(instance, Stroke)

@given(instance=fxg::SolidColorStroke_strategy)
@settings(max_examples=50)
def test_fxg::solidcolorstroke_instantiation(instance):
    assert isinstance(instance, fxg::SolidColorStroke)

@given(instance=fxg::SolidColorStroke_strategy)
def test_fxg::solidcolorstroke_miterLimit_type(instance):
    assert isinstance(instance.miterLimit, str)


@given(instance=fxg::SolidColorStroke_strategy)
def test_fxg::solidcolorstroke_miterLimit_setter(instance):
    original = instance.miterLimit
    instance.miterLimit = original
    assert instance.miterLimit == original

@given(instance=fxg::SolidColorStroke_strategy)
def test_fxg::solidcolorstroke_alpha_type(instance):
    assert isinstance(instance.alpha, str)


@given(instance=fxg::SolidColorStroke_strategy)
def test_fxg::solidcolorstroke_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original

@given(instance=fxg::SolidColorStroke_strategy)
def test_fxg::solidcolorstroke_caps_type(instance):
    assert isinstance(instance.caps, str)


@given(instance=fxg::SolidColorStroke_strategy)
def test_fxg::solidcolorstroke_caps_setter(instance):
    original = instance.caps
    instance.caps = original
    assert instance.caps == original

@given(instance=fxg::SolidColorStroke_strategy)
def test_fxg::solidcolorstroke_scaleMode_type(instance):
    assert isinstance(instance.scaleMode, str)


@given(instance=fxg::SolidColorStroke_strategy)
def test_fxg::solidcolorstroke_scaleMode_setter(instance):
    original = instance.scaleMode
    instance.scaleMode = original
    assert instance.scaleMode == original

@given(instance=fxg::SolidColorStroke_strategy)
def test_fxg::solidcolorstroke_weight_type(instance):
    assert isinstance(instance.weight, str)


@given(instance=fxg::SolidColorStroke_strategy)
def test_fxg::solidcolorstroke_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=fxg::SolidColorStroke_strategy)
def test_fxg::solidcolorstroke_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=fxg::SolidColorStroke_strategy)
def test_fxg::solidcolorstroke_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=fxg::SolidColorStroke_strategy)
def test_fxg::solidcolorstroke_pixelHinting_type(instance):
    assert isinstance(instance.pixelHinting, str)


@given(instance=fxg::SolidColorStroke_strategy)
def test_fxg::solidcolorstroke_pixelHinting_setter(instance):
    original = instance.pixelHinting
    instance.pixelHinting = original
    assert instance.pixelHinting == original

@given(instance=fxg::SolidColorStroke_strategy)
def test_fxg::solidcolorstroke_joints_type(instance):
    assert isinstance(instance.joints, str)


@given(instance=fxg::SolidColorStroke_strategy)
def test_fxg::solidcolorstroke_joints_setter(instance):
    original = instance.joints
    instance.joints = original
    assert instance.joints == original

@given(instance=fxg::RadialGradient_strategy)
@settings(max_examples=50)
def test_fxg::radialgradient_instantiation(instance):
    assert isinstance(instance, fxg::RadialGradient)

@given(instance=fxg::RadialGradient_strategy)
def test_fxg::radialgradient_focalPointRatio_type(instance):
    assert isinstance(instance.focalPointRatio, str)


@given(instance=fxg::RadialGradient_strategy)
def test_fxg::radialgradient_focalPointRatio_setter(instance):
    original = instance.focalPointRatio
    instance.focalPointRatio = original
    assert instance.focalPointRatio == original

@given(instance=fxg::RadialGradient_strategy)
def test_fxg::radialgradient_interpolationMethod_type(instance):
    assert isinstance(instance.interpolationMethod, str)


@given(instance=fxg::RadialGradient_strategy)
def test_fxg::radialgradient_interpolationMethod_setter(instance):
    original = instance.interpolationMethod
    instance.interpolationMethod = original
    assert instance.interpolationMethod == original

@given(instance=fxg::RadialGradient_strategy)
def test_fxg::radialgradient_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=fxg::RadialGradient_strategy)
def test_fxg::radialgradient_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=fxg::RadialGradient_strategy)
def test_fxg::radialgradient_scaleY_type(instance):
    assert isinstance(instance.scaleY, str)


@given(instance=fxg::RadialGradient_strategy)
def test_fxg::radialgradient_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original

@given(instance=fxg::RadialGradient_strategy)
def test_fxg::radialgradient_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=fxg::RadialGradient_strategy)
def test_fxg::radialgradient_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=fxg::RadialGradient_strategy)
def test_fxg::radialgradient_rotation_type(instance):
    assert isinstance(instance.rotation, str)


@given(instance=fxg::RadialGradient_strategy)
def test_fxg::radialgradient_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original

@given(instance=fxg::RadialGradient_strategy)
def test_fxg::radialgradient_spreadMethod_type(instance):
    assert isinstance(instance.spreadMethod, str)


@given(instance=fxg::RadialGradient_strategy)
def test_fxg::radialgradient_spreadMethod_setter(instance):
    original = instance.spreadMethod
    instance.spreadMethod = original
    assert instance.spreadMethod == original

@given(instance=fxg::RadialGradient_strategy)
def test_fxg::radialgradient_scaleX_type(instance):
    assert isinstance(instance.scaleX, str)


@given(instance=fxg::RadialGradient_strategy)
def test_fxg::radialgradient_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original

@given(instance=Fill_strategy)
@settings(max_examples=50)
def test_fill_instantiation(instance):
    assert isinstance(instance, Fill)

@given(instance=fxg::BitmapFill_strategy)
@settings(max_examples=50)
def test_fxg::bitmapfill_instantiation(instance):
    assert isinstance(instance, fxg::BitmapFill)

@given(instance=fxg::BitmapFill_strategy)
def test_fxg::bitmapfill_fillMode_type(instance):
    assert isinstance(instance.fillMode, str)


@given(instance=fxg::BitmapFill_strategy)
def test_fxg::bitmapfill_fillMode_setter(instance):
    original = instance.fillMode
    instance.fillMode = original
    assert instance.fillMode == original

@given(instance=fxg::BitmapFill_strategy)
def test_fxg::bitmapfill_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=fxg::BitmapFill_strategy)
def test_fxg::bitmapfill_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=fxg::BitmapFill_strategy)
def test_fxg::bitmapfill_scaleY_type(instance):
    assert isinstance(instance.scaleY, str)


@given(instance=fxg::BitmapFill_strategy)
def test_fxg::bitmapfill_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original

@given(instance=fxg::BitmapFill_strategy)
def test_fxg::bitmapfill_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=fxg::BitmapFill_strategy)
def test_fxg::bitmapfill_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=fxg::BitmapFill_strategy)
def test_fxg::bitmapfill_scaleX_type(instance):
    assert isinstance(instance.scaleX, str)


@given(instance=fxg::BitmapFill_strategy)
def test_fxg::bitmapfill_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original

@given(instance=fxg::BitmapFill_strategy)
def test_fxg::bitmapfill_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=fxg::BitmapFill_strategy)
def test_fxg::bitmapfill_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=fxg::BitmapFill_strategy)
def test_fxg::bitmapfill_rotation_type(instance):
    assert isinstance(instance.rotation, str)


@given(instance=fxg::BitmapFill_strategy)
def test_fxg::bitmapfill_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original

@given(instance=fxg::SolidColor_strategy)
@settings(max_examples=50)
def test_fxg::solidcolor_instantiation(instance):
    assert isinstance(instance, fxg::SolidColor)

@given(instance=fxg::SolidColor_strategy)
def test_fxg::solidcolor_alpha_type(instance):
    assert isinstance(instance.alpha, str)


@given(instance=fxg::SolidColor_strategy)
def test_fxg::solidcolor_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original

@given(instance=fxg::SolidColor_strategy)
def test_fxg::solidcolor_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=fxg::SolidColor_strategy)
def test_fxg::solidcolor_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=fxg::linkActiveFormat_strategy)
@settings(max_examples=50)
def test_fxg::linkactiveformat_instantiation(instance):
    assert isinstance(instance, fxg::linkActiveFormat)

@given(instance=RichTextContentContainer_strategy)
@settings(max_examples=50)
def test_richtextcontentcontainer_instantiation(instance):
    assert isinstance(instance, RichTextContentContainer)

@given(instance=fxg::CharacterAttributes_strategy)
@settings(max_examples=50)
def test_fxg::characterattributes_instantiation(instance):
    assert isinstance(instance, fxg::CharacterAttributes)

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_locale_type(instance):
    assert isinstance(instance.locale, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_locale_setter(instance):
    original = instance.locale
    instance.locale = original
    assert instance.locale == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_lineHeight_type(instance):
    assert isinstance(instance.lineHeight, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_lineHeight_setter(instance):
    original = instance.lineHeight
    instance.lineHeight = original
    assert instance.lineHeight == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_fontWeight_type(instance):
    assert isinstance(instance.fontWeight, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_fontWeight_setter(instance):
    original = instance.fontWeight
    instance.fontWeight = original
    assert instance.fontWeight == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_textRotation_type(instance):
    assert isinstance(instance.textRotation, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_textRotation_setter(instance):
    original = instance.textRotation
    instance.textRotation = original
    assert instance.textRotation == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_trackingRight_type(instance):
    assert isinstance(instance.trackingRight, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_trackingRight_setter(instance):
    original = instance.trackingRight
    instance.trackingRight = original
    assert instance.trackingRight == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_typographicCase_type(instance):
    assert isinstance(instance.typographicCase, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_typographicCase_setter(instance):
    original = instance.typographicCase
    instance.typographicCase = original
    assert instance.typographicCase == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_baselineShift_type(instance):
    assert isinstance(instance.baselineShift, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_baselineShift_setter(instance):
    original = instance.baselineShift
    instance.baselineShift = original
    assert instance.baselineShift == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_trackingLeft_type(instance):
    assert isinstance(instance.trackingLeft, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_trackingLeft_setter(instance):
    original = instance.trackingLeft
    instance.trackingLeft = original
    assert instance.trackingLeft == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_dominantBaseline_type(instance):
    assert isinstance(instance.dominantBaseline, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_dominantBaseline_setter(instance):
    original = instance.dominantBaseline
    instance.dominantBaseline = original
    assert instance.dominantBaseline == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_breakOpportunity_type(instance):
    assert isinstance(instance.breakOpportunity, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_breakOpportunity_setter(instance):
    original = instance.breakOpportunity
    instance.breakOpportunity = original
    assert instance.breakOpportunity == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_digitCase_type(instance):
    assert isinstance(instance.digitCase, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_digitCase_setter(instance):
    original = instance.digitCase
    instance.digitCase = original
    assert instance.digitCase == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_lineThrough_type(instance):
    assert isinstance(instance.lineThrough, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_lineThrough_setter(instance):
    original = instance.lineThrough
    instance.lineThrough = original
    assert instance.lineThrough == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_whiteSpaceCollapse_type(instance):
    assert isinstance(instance.whiteSpaceCollapse, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_whiteSpaceCollapse_setter(instance):
    original = instance.whiteSpaceCollapse
    instance.whiteSpaceCollapse = original
    assert instance.whiteSpaceCollapse == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_fontStyle_type(instance):
    assert isinstance(instance.fontStyle, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_fontStyle_setter(instance):
    original = instance.fontStyle
    instance.fontStyle = original
    assert instance.fontStyle == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_fontSize_type(instance):
    assert isinstance(instance.fontSize, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_fontSize_setter(instance):
    original = instance.fontSize
    instance.fontSize = original
    assert instance.fontSize == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_textAlpha_type(instance):
    assert isinstance(instance.textAlpha, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_textAlpha_setter(instance):
    original = instance.textAlpha
    instance.textAlpha = original
    assert instance.textAlpha == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_backgroundColor_type(instance):
    assert isinstance(instance.backgroundColor, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_kerning_type(instance):
    assert isinstance(instance.kerning, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_kerning_setter(instance):
    original = instance.kerning
    instance.kerning = original
    assert instance.kerning == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_backgroundAlpha_type(instance):
    assert isinstance(instance.backgroundAlpha, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_backgroundAlpha_setter(instance):
    original = instance.backgroundAlpha
    instance.backgroundAlpha = original
    assert instance.backgroundAlpha == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_digitWidth_type(instance):
    assert isinstance(instance.digitWidth, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_digitWidth_setter(instance):
    original = instance.digitWidth
    instance.digitWidth = original
    assert instance.digitWidth == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_ligatureLevel_type(instance):
    assert isinstance(instance.ligatureLevel, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_ligatureLevel_setter(instance):
    original = instance.ligatureLevel
    instance.ligatureLevel = original
    assert instance.ligatureLevel == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_textDecoration_type(instance):
    assert isinstance(instance.textDecoration, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_textDecoration_setter(instance):
    original = instance.textDecoration
    instance.textDecoration = original
    assert instance.textDecoration == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_alignmentBaseline_type(instance):
    assert isinstance(instance.alignmentBaseline, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_alignmentBaseline_setter(instance):
    original = instance.alignmentBaseline
    instance.alignmentBaseline = original
    assert instance.alignmentBaseline == original

@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_fontFamily_type(instance):
    assert isinstance(instance.fontFamily, str)


@given(instance=fxg::CharacterAttributes_strategy)
def test_fxg::characterattributes_fontFamily_setter(instance):
    original = instance.fontFamily
    instance.fontFamily = original
    assert instance.fontFamily == original

@given(instance=fxg::ContainerAttributes_strategy)
@settings(max_examples=50)
def test_fxg::containerattributes_instantiation(instance):
    assert isinstance(instance, fxg::ContainerAttributes)

@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_paddingLeft_type(instance):
    assert isinstance(instance.paddingLeft, str)


@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_paddingLeft_setter(instance):
    original = instance.paddingLeft
    instance.paddingLeft = original
    assert instance.paddingLeft == original

@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_columnGap_type(instance):
    assert isinstance(instance.columnGap, str)


@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_columnGap_setter(instance):
    original = instance.columnGap
    instance.columnGap = original
    assert instance.columnGap == original

@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_columnWidth_type(instance):
    assert isinstance(instance.columnWidth, str)


@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_columnWidth_setter(instance):
    original = instance.columnWidth
    instance.columnWidth = original
    assert instance.columnWidth == original

@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_firstBaselineOffset_type(instance):
    assert isinstance(instance.firstBaselineOffset, str)


@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_firstBaselineOffset_setter(instance):
    original = instance.firstBaselineOffset
    instance.firstBaselineOffset = original
    assert instance.firstBaselineOffset == original

@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_verticalAlign_type(instance):
    assert isinstance(instance.verticalAlign, str)


@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_verticalAlign_setter(instance):
    original = instance.verticalAlign
    instance.verticalAlign = original
    assert instance.verticalAlign == original

@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_lineBreak_type(instance):
    assert isinstance(instance.lineBreak, str)


@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_lineBreak_setter(instance):
    original = instance.lineBreak
    instance.lineBreak = original
    assert instance.lineBreak == original

@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_paddingBottom_type(instance):
    assert isinstance(instance.paddingBottom, str)


@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_paddingBottom_setter(instance):
    original = instance.paddingBottom
    instance.paddingBottom = original
    assert instance.paddingBottom == original

@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_paddingRight_type(instance):
    assert isinstance(instance.paddingRight, str)


@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_paddingRight_setter(instance):
    original = instance.paddingRight
    instance.paddingRight = original
    assert instance.paddingRight == original

@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_blockProgression_type(instance):
    assert isinstance(instance.blockProgression, str)


@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_blockProgression_setter(instance):
    original = instance.blockProgression
    instance.blockProgression = original
    assert instance.blockProgression == original

@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_paddingTop_type(instance):
    assert isinstance(instance.paddingTop, str)


@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_paddingTop_setter(instance):
    original = instance.paddingTop
    instance.paddingTop = original
    assert instance.paddingTop == original

@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_columnCount_type(instance):
    assert isinstance(instance.columnCount, str)


@given(instance=fxg::ContainerAttributes_strategy)
def test_fxg::containerattributes_columnCount_setter(instance):
    original = instance.columnCount
    instance.columnCount = original
    assert instance.columnCount == original

@given(instance=fxg::ParagraphAttributes_strategy)
@settings(max_examples=50)
def test_fxg::paragraphattributes_instantiation(instance):
    assert isinstance(instance, fxg::ParagraphAttributes)

@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_paragraphSpaceAfter_type(instance):
    assert isinstance(instance.paragraphSpaceAfter, str)


@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_paragraphSpaceAfter_setter(instance):
    original = instance.paragraphSpaceAfter
    instance.paragraphSpaceAfter = original
    assert instance.paragraphSpaceAfter == original

@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_textAlignLast_type(instance):
    assert isinstance(instance.textAlignLast, str)


@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_textAlignLast_setter(instance):
    original = instance.textAlignLast
    instance.textAlignLast = original
    assert instance.textAlignLast == original

@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_textIndent_type(instance):
    assert isinstance(instance.textIndent, str)


@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_textIndent_setter(instance):
    original = instance.textIndent
    instance.textIndent = original
    assert instance.textIndent == original

@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_paragraphStartIndent_type(instance):
    assert isinstance(instance.paragraphStartIndent, str)


@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_paragraphStartIndent_setter(instance):
    original = instance.paragraphStartIndent
    instance.paragraphStartIndent = original
    assert instance.paragraphStartIndent == original

@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_leadingModel_type(instance):
    assert isinstance(instance.leadingModel, str)


@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_leadingModel_setter(instance):
    original = instance.leadingModel
    instance.leadingModel = original
    assert instance.leadingModel == original

@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_tabStops_type(instance):
    assert isinstance(instance.tabStops, str)


@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_tabStops_setter(instance):
    original = instance.tabStops
    instance.tabStops = original
    assert instance.tabStops == original

@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_textJustify_type(instance):
    assert isinstance(instance.textJustify, str)


@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_textJustify_setter(instance):
    original = instance.textJustify
    instance.textJustify = original
    assert instance.textJustify == original

@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_justificationRule_type(instance):
    assert isinstance(instance.justificationRule, str)


@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_justificationRule_setter(instance):
    original = instance.justificationRule
    instance.justificationRule = original
    assert instance.justificationRule == original

@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_justificationStyle_type(instance):
    assert isinstance(instance.justificationStyle, str)


@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_justificationStyle_setter(instance):
    original = instance.justificationStyle
    instance.justificationStyle = original
    assert instance.justificationStyle == original

@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_textAlign_type(instance):
    assert isinstance(instance.textAlign, str)


@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_textAlign_setter(instance):
    original = instance.textAlign
    instance.textAlign = original
    assert instance.textAlign == original

@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_paragraphSpaceBefore_type(instance):
    assert isinstance(instance.paragraphSpaceBefore, str)


@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_paragraphSpaceBefore_setter(instance):
    original = instance.paragraphSpaceBefore
    instance.paragraphSpaceBefore = original
    assert instance.paragraphSpaceBefore == original

@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_paragraphEndIndent_type(instance):
    assert isinstance(instance.paragraphEndIndent, str)


@given(instance=fxg::ParagraphAttributes_strategy)
def test_fxg::paragraphattributes_paragraphEndIndent_setter(instance):
    original = instance.paragraphEndIndent
    instance.paragraphEndIndent = original
    assert instance.paragraphEndIndent == original

@given(instance=RichTextContent_strategy)
@settings(max_examples=50)
def test_richtextcontent_instantiation(instance):
    assert isinstance(instance, RichTextContent)

@given(instance=fxg::linkHoverFormat_strategy)
@settings(max_examples=50)
def test_fxg::linkhoverformat_instantiation(instance):
    assert isinstance(instance, fxg::linkHoverFormat)

@given(instance=fxg::span_strategy)
@settings(max_examples=50)
def test_fxg::span_instantiation(instance):
    assert isinstance(instance, fxg::span)

@given(instance=fxg::tab_strategy)
@settings(max_examples=50)
def test_fxg::tab_instantiation(instance):
    assert isinstance(instance, fxg::tab)

@given(instance=fxg::linkNormalFormat_strategy)
@settings(max_examples=50)
def test_fxg::linknormalformat_instantiation(instance):
    assert isinstance(instance, fxg::linkNormalFormat)

@given(instance=fxg::a_strategy)
@settings(max_examples=50)
def test_fxg::a_instantiation(instance):
    assert isinstance(instance, fxg::a)

@given(instance=fxg::rawtext_strategy)
@settings(max_examples=50)
def test_fxg::rawtext_instantiation(instance):
    assert isinstance(instance, fxg::rawtext)

@given(instance=fxg::rawtext_strategy)
def test_fxg::rawtext__text_type(instance):
    assert isinstance(instance._text, str)


@given(instance=fxg::rawtext_strategy)
def test_fxg::rawtext__text_setter(instance):
    original = instance._text
    instance._text = original
    assert instance._text == original

@given(instance=fxg::img_strategy)
@settings(max_examples=50)
def test_fxg::img_instantiation(instance):
    assert isinstance(instance, fxg::img)

@given(instance=fxg::div_strategy)
@settings(max_examples=50)
def test_fxg::div_instantiation(instance):
    assert isinstance(instance, fxg::div)

@given(instance=fxg::br_strategy)
@settings(max_examples=50)
def test_fxg::br_instantiation(instance):
    assert isinstance(instance, fxg::br)

@given(instance=fxg::tcy_strategy)
@settings(max_examples=50)
def test_fxg::tcy_instantiation(instance):
    assert isinstance(instance, fxg::tcy)

@given(instance=fxg::RichTextContentContainer_strategy)
@settings(max_examples=50)
def test_fxg::richtextcontentcontainer_instantiation(instance):
    assert isinstance(instance, fxg::RichTextContentContainer)

@given(instance=fxg::RichTextContent_strategy)
@settings(max_examples=50)
def test_fxg::richtextcontent_instantiation(instance):
    assert isinstance(instance, fxg::RichTextContent)

@given(instance=CharacterAttributes_strategy)
@settings(max_examples=50)
def test_characterattributes_instantiation(instance):
    assert isinstance(instance, CharacterAttributes)

@given(instance=ContainerAttributes_strategy)
@settings(max_examples=50)
def test_containerattributes_instantiation(instance):
    assert isinstance(instance, ContainerAttributes)

@given(instance=ParagraphAttributes_strategy)
@settings(max_examples=50)
def test_paragraphattributes_instantiation(instance):
    assert isinstance(instance, ParagraphAttributes)

@given(instance=fxg::p_strategy)
@settings(max_examples=50)
def test_fxg::p_instantiation(instance):
    assert isinstance(instance, fxg::p)

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=fxg::Ellipse_strategy)
@settings(max_examples=50)
def test_fxg::ellipse_instantiation(instance):
    assert isinstance(instance, fxg::Ellipse)

@given(instance=fxg::Ellipse_strategy)
def test_fxg::ellipse_scaleX_type(instance):
    assert isinstance(instance.scaleX, str)


@given(instance=fxg::Ellipse_strategy)
def test_fxg::ellipse_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original

@given(instance=fxg::Ellipse_strategy)
def test_fxg::ellipse_visible_type(instance):
    assert isinstance(instance.visible, str)


@given(instance=fxg::Ellipse_strategy)
def test_fxg::ellipse_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=fxg::Ellipse_strategy)
def test_fxg::ellipse_alpha_type(instance):
    assert isinstance(instance.alpha, str)


@given(instance=fxg::Ellipse_strategy)
def test_fxg::ellipse_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original

@given(instance=fxg::Ellipse_strategy)
def test_fxg::ellipse_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=fxg::Ellipse_strategy)
def test_fxg::ellipse_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=fxg::Ellipse_strategy)
def test_fxg::ellipse_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=fxg::Ellipse_strategy)
def test_fxg::ellipse_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=fxg::Ellipse_strategy)
def test_fxg::ellipse_blendMode_type(instance):
    assert isinstance(instance.blendMode, str)


@given(instance=fxg::Ellipse_strategy)
def test_fxg::ellipse_blendMode_setter(instance):
    original = instance.blendMode
    instance.blendMode = original
    assert instance.blendMode == original

@given(instance=fxg::Ellipse_strategy)
def test_fxg::ellipse_scaleY_type(instance):
    assert isinstance(instance.scaleY, str)


@given(instance=fxg::Ellipse_strategy)
def test_fxg::ellipse_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original

@given(instance=fxg::Ellipse_strategy)
def test_fxg::ellipse_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=fxg::Ellipse_strategy)
def test_fxg::ellipse_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=fxg::Ellipse_strategy)
def test_fxg::ellipse_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=fxg::Ellipse_strategy)
def test_fxg::ellipse_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=fxg::Ellipse_strategy)
def test_fxg::ellipse_rotation_type(instance):
    assert isinstance(instance.rotation, str)


@given(instance=fxg::Ellipse_strategy)
def test_fxg::ellipse_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original

@given(instance=fxg::Line_strategy)
@settings(max_examples=50)
def test_fxg::line_instantiation(instance):
    assert isinstance(instance, fxg::Line)

@given(instance=fxg::Line_strategy)
def test_fxg::line_yFrom_type(instance):
    assert isinstance(instance.yFrom, str)


@given(instance=fxg::Line_strategy)
def test_fxg::line_yFrom_setter(instance):
    original = instance.yFrom
    instance.yFrom = original
    assert instance.yFrom == original

@given(instance=fxg::Line_strategy)
def test_fxg::line_rotation_type(instance):
    assert isinstance(instance.rotation, str)


@given(instance=fxg::Line_strategy)
def test_fxg::line_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original

@given(instance=fxg::Line_strategy)
def test_fxg::line_xTo_type(instance):
    assert isinstance(instance.xTo, str)


@given(instance=fxg::Line_strategy)
def test_fxg::line_xTo_setter(instance):
    original = instance.xTo
    instance.xTo = original
    assert instance.xTo == original

@given(instance=fxg::Line_strategy)
def test_fxg::line_xFrom_type(instance):
    assert isinstance(instance.xFrom, str)


@given(instance=fxg::Line_strategy)
def test_fxg::line_xFrom_setter(instance):
    original = instance.xFrom
    instance.xFrom = original
    assert instance.xFrom == original

@given(instance=fxg::Line_strategy)
def test_fxg::line_yTo_type(instance):
    assert isinstance(instance.yTo, str)


@given(instance=fxg::Line_strategy)
def test_fxg::line_yTo_setter(instance):
    original = instance.yTo
    instance.yTo = original
    assert instance.yTo == original

@given(instance=fxg::Line_strategy)
def test_fxg::line_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=fxg::Line_strategy)
def test_fxg::line_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=fxg::Line_strategy)
def test_fxg::line_scaleY_type(instance):
    assert isinstance(instance.scaleY, str)


@given(instance=fxg::Line_strategy)
def test_fxg::line_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original

@given(instance=fxg::Line_strategy)
def test_fxg::line_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=fxg::Line_strategy)
def test_fxg::line_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=fxg::Line_strategy)
def test_fxg::line_scaleX_type(instance):
    assert isinstance(instance.scaleX, str)


@given(instance=fxg::Line_strategy)
def test_fxg::line_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original

@given(instance=fxg::Line_strategy)
def test_fxg::line_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=fxg::Line_strategy)
def test_fxg::line_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=fxg::Line_strategy)
def test_fxg::line_visible_type(instance):
    assert isinstance(instance.visible, str)


@given(instance=fxg::Line_strategy)
def test_fxg::line_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=fxg::Line_strategy)
def test_fxg::line_alpha_type(instance):
    assert isinstance(instance.alpha, str)


@given(instance=fxg::Line_strategy)
def test_fxg::line_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original

@given(instance=fxg::Line_strategy)
def test_fxg::line_blendMode_type(instance):
    assert isinstance(instance.blendMode, str)


@given(instance=fxg::Line_strategy)
def test_fxg::line_blendMode_setter(instance):
    original = instance.blendMode
    instance.blendMode = original
    assert instance.blendMode == original

@given(instance=fxg::Line_strategy)
def test_fxg::line_maskType_type(instance):
    assert isinstance(instance.maskType, str)


@given(instance=fxg::Line_strategy)
def test_fxg::line_maskType_setter(instance):
    original = instance.maskType
    instance.maskType = original
    assert instance.maskType == original

@given(instance=fxg::Rect_strategy)
@settings(max_examples=50)
def test_fxg::rect_instantiation(instance):
    assert isinstance(instance, fxg::Rect)

@given(instance=fxg::Rect_strategy)
def test_fxg::rect_bottomRightRadiusY_type(instance):
    assert isinstance(instance.bottomRightRadiusY, str)


@given(instance=fxg::Rect_strategy)
def test_fxg::rect_bottomRightRadiusY_setter(instance):
    original = instance.bottomRightRadiusY
    instance.bottomRightRadiusY = original
    assert instance.bottomRightRadiusY == original

@given(instance=fxg::Rect_strategy)
def test_fxg::rect_radiusY_type(instance):
    assert isinstance(instance.radiusY, str)


@given(instance=fxg::Rect_strategy)
def test_fxg::rect_radiusY_setter(instance):
    original = instance.radiusY
    instance.radiusY = original
    assert instance.radiusY == original

@given(instance=fxg::Rect_strategy)
def test_fxg::rect_bottomLeftRadiusX_type(instance):
    assert isinstance(instance.bottomLeftRadiusX, str)


@given(instance=fxg::Rect_strategy)
def test_fxg::rect_bottomLeftRadiusX_setter(instance):
    original = instance.bottomLeftRadiusX
    instance.bottomLeftRadiusX = original
    assert instance.bottomLeftRadiusX == original

@given(instance=fxg::Rect_strategy)
def test_fxg::rect_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=fxg::Rect_strategy)
def test_fxg::rect_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=fxg::Rect_strategy)
def test_fxg::rect_rotation_type(instance):
    assert isinstance(instance.rotation, str)


@given(instance=fxg::Rect_strategy)
def test_fxg::rect_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original

@given(instance=fxg::Rect_strategy)
def test_fxg::rect_scaleY_type(instance):
    assert isinstance(instance.scaleY, str)


@given(instance=fxg::Rect_strategy)
def test_fxg::rect_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original

@given(instance=fxg::Rect_strategy)
def test_fxg::rect_radiusX_type(instance):
    assert isinstance(instance.radiusX, str)


@given(instance=fxg::Rect_strategy)
def test_fxg::rect_radiusX_setter(instance):
    original = instance.radiusX
    instance.radiusX = original
    assert instance.radiusX == original

@given(instance=fxg::Rect_strategy)
def test_fxg::rect_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=fxg::Rect_strategy)
def test_fxg::rect_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=fxg::Rect_strategy)
def test_fxg::rect_scaleX_type(instance):
    assert isinstance(instance.scaleX, str)


@given(instance=fxg::Rect_strategy)
def test_fxg::rect_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original

@given(instance=fxg::Rect_strategy)
def test_fxg::rect_topRightRadiusX_type(instance):
    assert isinstance(instance.topRightRadiusX, str)


@given(instance=fxg::Rect_strategy)
def test_fxg::rect_topRightRadiusX_setter(instance):
    original = instance.topRightRadiusX
    instance.topRightRadiusX = original
    assert instance.topRightRadiusX == original

@given(instance=fxg::Rect_strategy)
def test_fxg::rect_alpha_type(instance):
    assert isinstance(instance.alpha, str)


@given(instance=fxg::Rect_strategy)
def test_fxg::rect_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original

@given(instance=fxg::Rect_strategy)
def test_fxg::rect_topLeftRadiusY_type(instance):
    assert isinstance(instance.topLeftRadiusY, str)


@given(instance=fxg::Rect_strategy)
def test_fxg::rect_topLeftRadiusY_setter(instance):
    original = instance.topLeftRadiusY
    instance.topLeftRadiusY = original
    assert instance.topLeftRadiusY == original

@given(instance=fxg::Rect_strategy)
def test_fxg::rect_topLeftRadiusX_type(instance):
    assert isinstance(instance.topLeftRadiusX, str)


@given(instance=fxg::Rect_strategy)
def test_fxg::rect_topLeftRadiusX_setter(instance):
    original = instance.topLeftRadiusX
    instance.topLeftRadiusX = original
    assert instance.topLeftRadiusX == original

@given(instance=fxg::Rect_strategy)
def test_fxg::rect_topRightRadiusY_type(instance):
    assert isinstance(instance.topRightRadiusY, str)


@given(instance=fxg::Rect_strategy)
def test_fxg::rect_topRightRadiusY_setter(instance):
    original = instance.topRightRadiusY
    instance.topRightRadiusY = original
    assert instance.topRightRadiusY == original

@given(instance=fxg::Rect_strategy)
def test_fxg::rect_blendMode_type(instance):
    assert isinstance(instance.blendMode, str)


@given(instance=fxg::Rect_strategy)
def test_fxg::rect_blendMode_setter(instance):
    original = instance.blendMode
    instance.blendMode = original
    assert instance.blendMode == original

@given(instance=fxg::Rect_strategy)
def test_fxg::rect_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=fxg::Rect_strategy)
def test_fxg::rect_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=fxg::Rect_strategy)
def test_fxg::rect_bottomRightRadiusX_type(instance):
    assert isinstance(instance.bottomRightRadiusX, str)


@given(instance=fxg::Rect_strategy)
def test_fxg::rect_bottomRightRadiusX_setter(instance):
    original = instance.bottomRightRadiusX
    instance.bottomRightRadiusX = original
    assert instance.bottomRightRadiusX == original

@given(instance=fxg::Rect_strategy)
def test_fxg::rect_visible_type(instance):
    assert isinstance(instance.visible, str)


@given(instance=fxg::Rect_strategy)
def test_fxg::rect_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=fxg::Rect_strategy)
def test_fxg::rect_bottomLeftRadiusY_type(instance):
    assert isinstance(instance.bottomLeftRadiusY, str)


@given(instance=fxg::Rect_strategy)
def test_fxg::rect_bottomLeftRadiusY_setter(instance):
    original = instance.bottomLeftRadiusY
    instance.bottomLeftRadiusY = original
    assert instance.bottomLeftRadiusY == original

@given(instance=fxg::Rect_strategy)
def test_fxg::rect_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=fxg::Rect_strategy)
def test_fxg::rect_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=fxg::Definition_strategy)
@settings(max_examples=50)
def test_fxg::definition_instantiation(instance):
    assert isinstance(instance, fxg::Definition)

@given(instance=fxg::Definition_strategy)
def test_fxg::definition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fxg::Definition_strategy)
def test_fxg::definition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FXGElement_strategy)
@settings(max_examples=50)
def test_fxgelement_instantiation(instance):
    assert isinstance(instance, FXGElement)

@given(instance=fxg::Transform_strategy)
@settings(max_examples=50)
def test_fxg::transform_instantiation(instance):
    assert isinstance(instance, fxg::Transform)

@given(instance=fxg::ContainerElement_strategy)
@settings(max_examples=50)
def test_fxg::containerelement_instantiation(instance):
    assert isinstance(instance, fxg::ContainerElement)

@given(instance=fxg::GradientEntry_strategy)
@settings(max_examples=50)
def test_fxg::gradiententry_instantiation(instance):
    assert isinstance(instance, fxg::GradientEntry)

@given(instance=fxg::GradientEntry_strategy)
def test_fxg::gradiententry_alpha_type(instance):
    assert isinstance(instance.alpha, str)


@given(instance=fxg::GradientEntry_strategy)
def test_fxg::gradiententry_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original

@given(instance=fxg::GradientEntry_strategy)
def test_fxg::gradiententry_ratio_type(instance):
    assert isinstance(instance.ratio, str)


@given(instance=fxg::GradientEntry_strategy)
def test_fxg::gradiententry_ratio_setter(instance):
    original = instance.ratio
    instance.ratio = original
    assert instance.ratio == original

@given(instance=fxg::GradientEntry_strategy)
def test_fxg::gradiententry_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=fxg::GradientEntry_strategy)
def test_fxg::gradiententry_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=fxg::ColorTransform_strategy)
@settings(max_examples=50)
def test_fxg::colortransform_instantiation(instance):
    assert isinstance(instance, fxg::ColorTransform)

@given(instance=fxg::ColorTransform_strategy)
def test_fxg::colortransform_alphaMultiplier_type(instance):
    assert isinstance(instance.alphaMultiplier, str)


@given(instance=fxg::ColorTransform_strategy)
def test_fxg::colortransform_alphaMultiplier_setter(instance):
    original = instance.alphaMultiplier
    instance.alphaMultiplier = original
    assert instance.alphaMultiplier == original

@given(instance=fxg::ColorTransform_strategy)
def test_fxg::colortransform_redOffset_type(instance):
    assert isinstance(instance.redOffset, str)


@given(instance=fxg::ColorTransform_strategy)
def test_fxg::colortransform_redOffset_setter(instance):
    original = instance.redOffset
    instance.redOffset = original
    assert instance.redOffset == original

@given(instance=fxg::ColorTransform_strategy)
def test_fxg::colortransform_greenOffset_type(instance):
    assert isinstance(instance.greenOffset, str)


@given(instance=fxg::ColorTransform_strategy)
def test_fxg::colortransform_greenOffset_setter(instance):
    original = instance.greenOffset
    instance.greenOffset = original
    assert instance.greenOffset == original

@given(instance=fxg::ColorTransform_strategy)
def test_fxg::colortransform_greenMultiplier_type(instance):
    assert isinstance(instance.greenMultiplier, str)


@given(instance=fxg::ColorTransform_strategy)
def test_fxg::colortransform_greenMultiplier_setter(instance):
    original = instance.greenMultiplier
    instance.greenMultiplier = original
    assert instance.greenMultiplier == original

@given(instance=fxg::ColorTransform_strategy)
def test_fxg::colortransform_blueOffset_type(instance):
    assert isinstance(instance.blueOffset, str)


@given(instance=fxg::ColorTransform_strategy)
def test_fxg::colortransform_blueOffset_setter(instance):
    original = instance.blueOffset
    instance.blueOffset = original
    assert instance.blueOffset == original

@given(instance=fxg::ColorTransform_strategy)
def test_fxg::colortransform_alphaOffset_type(instance):
    assert isinstance(instance.alphaOffset, str)


@given(instance=fxg::ColorTransform_strategy)
def test_fxg::colortransform_alphaOffset_setter(instance):
    original = instance.alphaOffset
    instance.alphaOffset = original
    assert instance.alphaOffset == original

@given(instance=fxg::ColorTransform_strategy)
def test_fxg::colortransform_redMultiplier_type(instance):
    assert isinstance(instance.redMultiplier, str)


@given(instance=fxg::ColorTransform_strategy)
def test_fxg::colortransform_redMultiplier_setter(instance):
    original = instance.redMultiplier
    instance.redMultiplier = original
    assert instance.redMultiplier == original

@given(instance=fxg::ColorTransform_strategy)
def test_fxg::colortransform_blueMultiplier_type(instance):
    assert isinstance(instance.blueMultiplier, str)


@given(instance=fxg::ColorTransform_strategy)
def test_fxg::colortransform_blueMultiplier_setter(instance):
    original = instance.blueMultiplier
    instance.blueMultiplier = original
    assert instance.blueMultiplier == original

@given(instance=fxg::Stroke_strategy)
@settings(max_examples=50)
def test_fxg::stroke_instantiation(instance):
    assert isinstance(instance, fxg::Stroke)

@given(instance=fxg::PlaceObject_strategy)
@settings(max_examples=50)
def test_fxg::placeobject_instantiation(instance):
    assert isinstance(instance, fxg::PlaceObject)

@given(instance=fxg::PlaceObject_strategy)
def test_fxg::placeobject_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=fxg::PlaceObject_strategy)
def test_fxg::placeobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=fxg::BitmapImage_strategy)
@settings(max_examples=50)
def test_fxg::bitmapimage_instantiation(instance):
    assert isinstance(instance, fxg::BitmapImage)

@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_fillMode_type(instance):
    assert isinstance(instance.fillMode, str)


@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_fillMode_setter(instance):
    original = instance.fillMode
    instance.fillMode = original
    assert instance.fillMode == original

@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_scaleX_type(instance):
    assert isinstance(instance.scaleX, str)


@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original

@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_visible_type(instance):
    assert isinstance(instance.visible, str)


@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_alpha_type(instance):
    assert isinstance(instance.alpha, str)


@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original

@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_blendMode_type(instance):
    assert isinstance(instance.blendMode, str)


@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_blendMode_setter(instance):
    original = instance.blendMode
    instance.blendMode = original
    assert instance.blendMode == original

@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_rotation_type(instance):
    assert isinstance(instance.rotation, str)


@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original

@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_scaleY_type(instance):
    assert isinstance(instance.scaleY, str)


@given(instance=fxg::BitmapImage_strategy)
def test_fxg::bitmapimage_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original

@given(instance=fxg::Fill_strategy)
@settings(max_examples=50)
def test_fxg::fill_instantiation(instance):
    assert isinstance(instance, fxg::Fill)

@given(instance=fxg::Matrix_strategy)
@settings(max_examples=50)
def test_fxg::matrix_instantiation(instance):
    assert isinstance(instance, fxg::Matrix)

@given(instance=fxg::Matrix_strategy)
def test_fxg::matrix_a_type(instance):
    assert isinstance(instance.a, str)


@given(instance=fxg::Matrix_strategy)
def test_fxg::matrix_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=fxg::Matrix_strategy)
def test_fxg::matrix_c_type(instance):
    assert isinstance(instance.c, str)


@given(instance=fxg::Matrix_strategy)
def test_fxg::matrix_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original

@given(instance=fxg::Matrix_strategy)
def test_fxg::matrix_ty_type(instance):
    assert isinstance(instance.ty, str)


@given(instance=fxg::Matrix_strategy)
def test_fxg::matrix_ty_setter(instance):
    original = instance.ty
    instance.ty = original
    assert instance.ty == original

@given(instance=fxg::Matrix_strategy)
def test_fxg::matrix_b_type(instance):
    assert isinstance(instance.b, str)


@given(instance=fxg::Matrix_strategy)
def test_fxg::matrix_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=fxg::Matrix_strategy)
def test_fxg::matrix_tx_type(instance):
    assert isinstance(instance.tx, str)


@given(instance=fxg::Matrix_strategy)
def test_fxg::matrix_tx_setter(instance):
    original = instance.tx
    instance.tx = original
    assert instance.tx == original

@given(instance=fxg::Matrix_strategy)
def test_fxg::matrix_d_type(instance):
    assert isinstance(instance.d, str)


@given(instance=fxg::Matrix_strategy)
def test_fxg::matrix_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original

@given(instance=fxg::Filter_strategy)
@settings(max_examples=50)
def test_fxg::filter_instantiation(instance):
    assert isinstance(instance, fxg::Filter)

@given(instance=fxg::RichText_strategy)
@settings(max_examples=50)
def test_fxg::richtext_instantiation(instance):
    assert isinstance(instance, fxg::RichText)

@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_scaleY_type(instance):
    assert isinstance(instance.scaleY, str)


@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original

@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_alpha_type(instance):
    assert isinstance(instance.alpha, str)


@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original

@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_visible_type(instance):
    assert isinstance(instance.visible, str)


@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_maskType_type(instance):
    assert isinstance(instance.maskType, str)


@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_maskType_setter(instance):
    original = instance.maskType
    instance.maskType = original
    assert instance.maskType == original

@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_scaleX_type(instance):
    assert isinstance(instance.scaleX, str)


@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original

@given(instance=fxg::RichText_strategy)
def test_fxg::richtext__tempcontent_type(instance):
    assert isinstance(instance._tempcontent, str)


@given(instance=fxg::RichText_strategy)
def test_fxg::richtext__tempcontent_setter(instance):
    original = instance._tempcontent
    instance._tempcontent = original
    assert instance._tempcontent == original

@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_blendMode_type(instance):
    assert isinstance(instance.blendMode, str)


@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_blendMode_setter(instance):
    original = instance.blendMode
    instance.blendMode = original
    assert instance.blendMode == original

@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_rotation_type(instance):
    assert isinstance(instance.rotation, str)


@given(instance=fxg::RichText_strategy)
def test_fxg::richtext_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original

@given(instance=fxg::Path_strategy)
@settings(max_examples=50)
def test_fxg::path_instantiation(instance):
    assert isinstance(instance, fxg::Path)

@given(instance=fxg::Path_strategy)
def test_fxg::path_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=fxg::Path_strategy)
def test_fxg::path_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=fxg::Path_strategy)
def test_fxg::path_winding_type(instance):
    assert isinstance(instance.winding, str)


@given(instance=fxg::Path_strategy)
def test_fxg::path_winding_setter(instance):
    original = instance.winding
    instance.winding = original
    assert instance.winding == original

@given(instance=fxg::Path_strategy)
def test_fxg::path_blendMode_type(instance):
    assert isinstance(instance.blendMode, str)


@given(instance=fxg::Path_strategy)
def test_fxg::path_blendMode_setter(instance):
    original = instance.blendMode
    instance.blendMode = original
    assert instance.blendMode == original

@given(instance=fxg::Path_strategy)
def test_fxg::path_rotation_type(instance):
    assert isinstance(instance.rotation, str)


@given(instance=fxg::Path_strategy)
def test_fxg::path_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original

@given(instance=fxg::Path_strategy)
def test_fxg::path_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=fxg::Path_strategy)
def test_fxg::path_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=fxg::Path_strategy)
def test_fxg::path_scaleX_type(instance):
    assert isinstance(instance.scaleX, str)


@given(instance=fxg::Path_strategy)
def test_fxg::path_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original

@given(instance=fxg::Path_strategy)
def test_fxg::path_visible_type(instance):
    assert isinstance(instance.visible, str)


@given(instance=fxg::Path_strategy)
def test_fxg::path_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=fxg::Path_strategy)
def test_fxg::path_scaleY_type(instance):
    assert isinstance(instance.scaleY, str)


@given(instance=fxg::Path_strategy)
def test_fxg::path_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original

@given(instance=fxg::Path_strategy)
def test_fxg::path_alpha_type(instance):
    assert isinstance(instance.alpha, str)


@given(instance=fxg::Path_strategy)
def test_fxg::path_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original

@given(instance=fxg::Path_strategy)
def test_fxg::path_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=fxg::Path_strategy)
def test_fxg::path_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=fxg::Shape_strategy)
@settings(max_examples=50)
def test_fxg::shape_instantiation(instance):
    assert isinstance(instance, fxg::Shape)

@given(instance=fxg::Private_strategy)
@settings(max_examples=50)
def test_fxg::private_instantiation(instance):
    assert isinstance(instance, fxg::Private)

@given(instance=fxg::Library_strategy)
@settings(max_examples=50)
def test_fxg::library_instantiation(instance):
    assert isinstance(instance, fxg::Library)

@given(instance=fxg::Group_strategy)
@settings(max_examples=50)
def test_fxg::group_instantiation(instance):
    assert isinstance(instance, fxg::Group)

@given(instance=fxg::Group_strategy)
def test_fxg::group_scaleGridTop_type(instance):
    assert isinstance(instance.scaleGridTop, str)


@given(instance=fxg::Group_strategy)
def test_fxg::group_scaleGridTop_setter(instance):
    original = instance.scaleGridTop
    instance.scaleGridTop = original
    assert instance.scaleGridTop == original

@given(instance=fxg::Group_strategy)
def test_fxg::group_scaleGridLeft_type(instance):
    assert isinstance(instance.scaleGridLeft, str)


@given(instance=fxg::Group_strategy)
def test_fxg::group_scaleGridLeft_setter(instance):
    original = instance.scaleGridLeft
    instance.scaleGridLeft = original
    assert instance.scaleGridLeft == original

@given(instance=fxg::Group_strategy)
def test_fxg::group_scaleGridRight_type(instance):
    assert isinstance(instance.scaleGridRight, str)


@given(instance=fxg::Group_strategy)
def test_fxg::group_scaleGridRight_setter(instance):
    original = instance.scaleGridRight
    instance.scaleGridRight = original
    assert instance.scaleGridRight == original

@given(instance=fxg::Group_strategy)
def test_fxg::group_transformX_type(instance):
    assert isinstance(instance.transformX, str)


@given(instance=fxg::Group_strategy)
def test_fxg::group_transformX_setter(instance):
    original = instance.transformX
    instance.transformX = original
    assert instance.transformX == original

@given(instance=fxg::Group_strategy)
def test_fxg::group_scaleY_type(instance):
    assert isinstance(instance.scaleY, str)


@given(instance=fxg::Group_strategy)
def test_fxg::group_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original

@given(instance=fxg::Group_strategy)
def test_fxg::group_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=fxg::Group_strategy)
def test_fxg::group_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=fxg::Group_strategy)
def test_fxg::group_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=fxg::Group_strategy)
def test_fxg::group_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=fxg::Group_strategy)
def test_fxg::group_visible_type(instance):
    assert isinstance(instance.visible, str)


@given(instance=fxg::Group_strategy)
def test_fxg::group_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=fxg::Group_strategy)
def test_fxg::group_scaleGridBottom_type(instance):
    assert isinstance(instance.scaleGridBottom, str)


@given(instance=fxg::Group_strategy)
def test_fxg::group_scaleGridBottom_setter(instance):
    original = instance.scaleGridBottom
    instance.scaleGridBottom = original
    assert instance.scaleGridBottom == original

@given(instance=fxg::Group_strategy)
def test_fxg::group_maskType_type(instance):
    assert isinstance(instance.maskType, str)


@given(instance=fxg::Group_strategy)
def test_fxg::group_maskType_setter(instance):
    original = instance.maskType
    instance.maskType = original
    assert instance.maskType == original

@given(instance=fxg::Group_strategy)
def test_fxg::group_rotation_type(instance):
    assert isinstance(instance.rotation, str)


@given(instance=fxg::Group_strategy)
def test_fxg::group_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original

@given(instance=fxg::Group_strategy)
def test_fxg::group_transformY_type(instance):
    assert isinstance(instance.transformY, str)


@given(instance=fxg::Group_strategy)
def test_fxg::group_transformY_setter(instance):
    original = instance.transformY
    instance.transformY = original
    assert instance.transformY == original

@given(instance=fxg::Group_strategy)
def test_fxg::group_blendMode_type(instance):
    assert isinstance(instance.blendMode, str)


@given(instance=fxg::Group_strategy)
def test_fxg::group_blendMode_setter(instance):
    original = instance.blendMode
    instance.blendMode = original
    assert instance.blendMode == original

@given(instance=fxg::Group_strategy)
def test_fxg::group_alpha_type(instance):
    assert isinstance(instance.alpha, str)


@given(instance=fxg::Group_strategy)
def test_fxg::group_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original

@given(instance=fxg::Group_strategy)
def test_fxg::group_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=fxg::Group_strategy)
def test_fxg::group_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=fxg::Group_strategy)
def test_fxg::group_scaleX_type(instance):
    assert isinstance(instance.scaleX, str)


@given(instance=fxg::Group_strategy)
def test_fxg::group_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original

@given(instance=fxg::Graphic_strategy)
@settings(max_examples=50)
def test_fxg::graphic_instantiation(instance):
    assert isinstance(instance, fxg::Graphic)

@given(instance=fxg::Graphic_strategy)
def test_fxg::graphic_scaleGridRight_type(instance):
    assert isinstance(instance.scaleGridRight, str)


@given(instance=fxg::Graphic_strategy)
def test_fxg::graphic_scaleGridRight_setter(instance):
    original = instance.scaleGridRight
    instance.scaleGridRight = original
    assert instance.scaleGridRight == original

@given(instance=fxg::Graphic_strategy)
def test_fxg::graphic_scaleGridLeft_type(instance):
    assert isinstance(instance.scaleGridLeft, str)


@given(instance=fxg::Graphic_strategy)
def test_fxg::graphic_scaleGridLeft_setter(instance):
    original = instance.scaleGridLeft
    instance.scaleGridLeft = original
    assert instance.scaleGridLeft == original

@given(instance=fxg::Graphic_strategy)
def test_fxg::graphic_viewHeight_type(instance):
    assert isinstance(instance.viewHeight, int)


@given(instance=fxg::Graphic_strategy)
def test_fxg::graphic_viewHeight_setter(instance):
    original = instance.viewHeight
    instance.viewHeight = original
    assert instance.viewHeight == original

@given(instance=fxg::Graphic_strategy)
def test_fxg::graphic_viewWidth_type(instance):
    assert isinstance(instance.viewWidth, int)


@given(instance=fxg::Graphic_strategy)
def test_fxg::graphic_viewWidth_setter(instance):
    original = instance.viewWidth
    instance.viewWidth = original
    assert instance.viewWidth == original

@given(instance=fxg::Graphic_strategy)
def test_fxg::graphic_scaleGridBottom_type(instance):
    assert isinstance(instance.scaleGridBottom, str)


@given(instance=fxg::Graphic_strategy)
def test_fxg::graphic_scaleGridBottom_setter(instance):
    original = instance.scaleGridBottom
    instance.scaleGridBottom = original
    assert instance.scaleGridBottom == original

@given(instance=fxg::Graphic_strategy)
def test_fxg::graphic_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=fxg::Graphic_strategy)
def test_fxg::graphic_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=fxg::Graphic_strategy)
def test_fxg::graphic_scaleGridTop_type(instance):
    assert isinstance(instance.scaleGridTop, str)


@given(instance=fxg::Graphic_strategy)
def test_fxg::graphic_scaleGridTop_setter(instance):
    original = instance.scaleGridTop
    instance.scaleGridTop = original
    assert instance.scaleGridTop == original
