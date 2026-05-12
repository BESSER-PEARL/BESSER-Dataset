import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fxg_FXGElement,
    fxg_GradientBevelFilter,
    fxg_GradientGlowFilter,
    Filter,
    fxg_BevelFilter,
    fxg_DropShadowFilter,
    fxg_ColorMatrixFilter,
    fxg_BlurFilter,
    fxg_LinearGradientStroke,
    Stroke,
    fxg_SolidColorStroke,
    fxg_RadialGradientStroke,
    fxg_RadialGradient,
    fxg_LinearGradient,
    Fill,
    fxg_SolidColor,
    fxg_linkActiveFormat,
    RichTextContentContainer,
    fxg_BitmapFill,
    fxg_CharacterAttributes,
    fxg_ContainerAttributes,
    fxg_ParagraphAttributes,
    RichTextContent,
    fxg_a,
    fxg_br,
    fxg_rawtext,
    fxg_tab,
    fxg_img,
    fxg_span,
    fxg_linkNormalFormat,
    fxg_div,
    fxg_linkHoverFormat,
    fxg_tcy,
    fxg_RichTextContentContainer,
    fxg_RichTextContent,
    CharacterAttributes,
    ContainerAttributes,
    ParagraphAttributes,
    fxg_p,
    Shape,
    fxg_Line,
    fxg_Ellipse,
    fxg_Rect,
    fxg_Definition,
    FXGElement,
    fxg_PlaceObject,
    fxg_Fill,
    fxg_Path,
    fxg_ContainerElement,
    fxg_GradientEntry,
    fxg_BitmapImage,
    fxg_RichText,
    fxg_Filter,
    fxg_Shape,
    fxg_Stroke,
    fxg_Transform,
    fxg_Private,
    fxg_Library,
    fxg_Group,
    fxg_Graphic,
    fxg_ColorTransform,
    fxg_Matrix,
    TypographicCase,
    FillMode,
    JustificationRule,
    ScaleMode,
    BreakOpportunity,
    SpreadMethod,
    TextRotation,
    Joint,
    BlockProgression,
    WhitespaceCollapse,
    BevelFilterType,
    InterpolationMethod,
    DigitCase,
    LeadingModel,
    Cap,
    FontWeight,
    DigitWidth,
    TextDecoration,
    JustificationStyle,
    TextJustify,
    AlignmentBaseline,
    Winding,
    DominantBaseline,
    Kerning,
    LineBreak,
    VerticalAlign,
    TextAlign,
    MaskType,
    BlendMode,
    LigatureLevel,
    FontStyle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fxg_fxgelement_is_not_abstract():
    assert not inspect.isabstract(fxg_FXGElement)


def test_fxg_fxgelement_constructor_exists():
    assert callable(fxg_FXGElement.__init__)


def test_fxg_fxgelement_constructor_args():
    sig = inspect.signature(fxg_FXGElement.__init__)
    params = list(sig.parameters.keys())



def test_fxg_gradientbevelfilter_is_not_abstract():
    assert not inspect.isabstract(fxg_GradientBevelFilter)


def test_fxg_gradientbevelfilter_constructor_exists():
    assert callable(fxg_GradientBevelFilter.__init__)


def test_fxg_gradientbevelfilter_constructor_args():
    sig = inspect.signature(fxg_GradientBevelFilter.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "angle" in params, "Missing parameter 'angle'"
    assert "knockout" in params, "Missing parameter 'knockout'"
    assert "strength" in params, "Missing parameter 'strength'"
    assert "blurX" in params, "Missing parameter 'blurX'"
    assert "blurY" in params, "Missing parameter 'blurY'"
    assert "distance" in params, "Missing parameter 'distance'"
    assert "quality" in params, "Missing parameter 'quality'"

def test_fxg_gradientbevelfilter_has_type():
    assert hasattr(fxg_GradientBevelFilter, "type")
    descriptor = None
    for klass in fxg_GradientBevelFilter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_fxg_gradientbevelfilter_has_angle():
    assert hasattr(fxg_GradientBevelFilter, "angle")
    descriptor = None
    for klass in fxg_GradientBevelFilter.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)

def test_fxg_gradientbevelfilter_has_knockout():
    assert hasattr(fxg_GradientBevelFilter, "knockout")
    descriptor = None
    for klass in fxg_GradientBevelFilter.__mro__:
        if "knockout" in klass.__dict__:
            descriptor = klass.__dict__["knockout"]
            break
    assert isinstance(descriptor, property)

def test_fxg_gradientbevelfilter_has_strength():
    assert hasattr(fxg_GradientBevelFilter, "strength")
    descriptor = None
    for klass in fxg_GradientBevelFilter.__mro__:
        if "strength" in klass.__dict__:
            descriptor = klass.__dict__["strength"]
            break
    assert isinstance(descriptor, property)

def test_fxg_gradientbevelfilter_has_blurX():
    assert hasattr(fxg_GradientBevelFilter, "blurX")
    descriptor = None
    for klass in fxg_GradientBevelFilter.__mro__:
        if "blurX" in klass.__dict__:
            descriptor = klass.__dict__["blurX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_gradientbevelfilter_has_blurY():
    assert hasattr(fxg_GradientBevelFilter, "blurY")
    descriptor = None
    for klass in fxg_GradientBevelFilter.__mro__:
        if "blurY" in klass.__dict__:
            descriptor = klass.__dict__["blurY"]
            break
    assert isinstance(descriptor, property)

def test_fxg_gradientbevelfilter_has_distance():
    assert hasattr(fxg_GradientBevelFilter, "distance")
    descriptor = None
    for klass in fxg_GradientBevelFilter.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)

def test_fxg_gradientbevelfilter_has_quality():
    assert hasattr(fxg_GradientBevelFilter, "quality")
    descriptor = None
    for klass in fxg_GradientBevelFilter.__mro__:
        if "quality" in klass.__dict__:
            descriptor = klass.__dict__["quality"]
            break
    assert isinstance(descriptor, property)



def test_fxg_gradientglowfilter_is_not_abstract():
    assert not inspect.isabstract(fxg_GradientGlowFilter)


def test_fxg_gradientglowfilter_constructor_exists():
    assert callable(fxg_GradientGlowFilter.__init__)


def test_fxg_gradientglowfilter_constructor_args():
    sig = inspect.signature(fxg_GradientGlowFilter.__init__)
    params = list(sig.parameters.keys())
    assert "quality" in params, "Missing parameter 'quality'"
    assert "distance" in params, "Missing parameter 'distance'"
    assert "strength" in params, "Missing parameter 'strength'"
    assert "inner" in params, "Missing parameter 'inner'"
    assert "knockout" in params, "Missing parameter 'knockout'"
    assert "blurX" in params, "Missing parameter 'blurX'"
    assert "angle" in params, "Missing parameter 'angle'"
    assert "blurY" in params, "Missing parameter 'blurY'"

def test_fxg_gradientglowfilter_has_quality():
    assert hasattr(fxg_GradientGlowFilter, "quality")
    descriptor = None
    for klass in fxg_GradientGlowFilter.__mro__:
        if "quality" in klass.__dict__:
            descriptor = klass.__dict__["quality"]
            break
    assert isinstance(descriptor, property)

def test_fxg_gradientglowfilter_has_distance():
    assert hasattr(fxg_GradientGlowFilter, "distance")
    descriptor = None
    for klass in fxg_GradientGlowFilter.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)

def test_fxg_gradientglowfilter_has_strength():
    assert hasattr(fxg_GradientGlowFilter, "strength")
    descriptor = None
    for klass in fxg_GradientGlowFilter.__mro__:
        if "strength" in klass.__dict__:
            descriptor = klass.__dict__["strength"]
            break
    assert isinstance(descriptor, property)

def test_fxg_gradientglowfilter_has_inner():
    assert hasattr(fxg_GradientGlowFilter, "inner")
    descriptor = None
    for klass in fxg_GradientGlowFilter.__mro__:
        if "inner" in klass.__dict__:
            descriptor = klass.__dict__["inner"]
            break
    assert isinstance(descriptor, property)

def test_fxg_gradientglowfilter_has_knockout():
    assert hasattr(fxg_GradientGlowFilter, "knockout")
    descriptor = None
    for klass in fxg_GradientGlowFilter.__mro__:
        if "knockout" in klass.__dict__:
            descriptor = klass.__dict__["knockout"]
            break
    assert isinstance(descriptor, property)

def test_fxg_gradientglowfilter_has_blurX():
    assert hasattr(fxg_GradientGlowFilter, "blurX")
    descriptor = None
    for klass in fxg_GradientGlowFilter.__mro__:
        if "blurX" in klass.__dict__:
            descriptor = klass.__dict__["blurX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_gradientglowfilter_has_angle():
    assert hasattr(fxg_GradientGlowFilter, "angle")
    descriptor = None
    for klass in fxg_GradientGlowFilter.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)

def test_fxg_gradientglowfilter_has_blurY():
    assert hasattr(fxg_GradientGlowFilter, "blurY")
    descriptor = None
    for klass in fxg_GradientGlowFilter.__mro__:
        if "blurY" in klass.__dict__:
            descriptor = klass.__dict__["blurY"]
            break
    assert isinstance(descriptor, property)



def test_filter_is_not_abstract():
    assert not inspect.isabstract(Filter)


def test_filter_constructor_exists():
    assert callable(Filter.__init__)


def test_filter_constructor_args():
    sig = inspect.signature(Filter.__init__)
    params = list(sig.parameters.keys())



def test_fxg_bevelfilter_is_not_abstract():
    assert not inspect.isabstract(fxg_BevelFilter)


def test_fxg_bevelfilter_constructor_exists():
    assert callable(fxg_BevelFilter.__init__)


def test_fxg_bevelfilter_constructor_args():
    sig = inspect.signature(fxg_BevelFilter.__init__)
    params = list(sig.parameters.keys())
    assert "highlightColor" in params, "Missing parameter 'highlightColor'"
    assert "distance" in params, "Missing parameter 'distance'"
    assert "shadowColor" in params, "Missing parameter 'shadowColor'"
    assert "type" in params, "Missing parameter 'type'"
    assert "blurY" in params, "Missing parameter 'blurY'"
    assert "blurX" in params, "Missing parameter 'blurX'"
    assert "quality" in params, "Missing parameter 'quality'"
    assert "knockout" in params, "Missing parameter 'knockout'"
    assert "strength" in params, "Missing parameter 'strength'"
    assert "highlightAlpha" in params, "Missing parameter 'highlightAlpha'"
    assert "angle" in params, "Missing parameter 'angle'"
    assert "shadowAlpha" in params, "Missing parameter 'shadowAlpha'"

def test_fxg_bevelfilter_has_highlightColor():
    assert hasattr(fxg_BevelFilter, "highlightColor")
    descriptor = None
    for klass in fxg_BevelFilter.__mro__:
        if "highlightColor" in klass.__dict__:
            descriptor = klass.__dict__["highlightColor"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bevelfilter_has_distance():
    assert hasattr(fxg_BevelFilter, "distance")
    descriptor = None
    for klass in fxg_BevelFilter.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bevelfilter_has_shadowColor():
    assert hasattr(fxg_BevelFilter, "shadowColor")
    descriptor = None
    for klass in fxg_BevelFilter.__mro__:
        if "shadowColor" in klass.__dict__:
            descriptor = klass.__dict__["shadowColor"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bevelfilter_has_type():
    assert hasattr(fxg_BevelFilter, "type")
    descriptor = None
    for klass in fxg_BevelFilter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bevelfilter_has_blurY():
    assert hasattr(fxg_BevelFilter, "blurY")
    descriptor = None
    for klass in fxg_BevelFilter.__mro__:
        if "blurY" in klass.__dict__:
            descriptor = klass.__dict__["blurY"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bevelfilter_has_blurX():
    assert hasattr(fxg_BevelFilter, "blurX")
    descriptor = None
    for klass in fxg_BevelFilter.__mro__:
        if "blurX" in klass.__dict__:
            descriptor = klass.__dict__["blurX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bevelfilter_has_quality():
    assert hasattr(fxg_BevelFilter, "quality")
    descriptor = None
    for klass in fxg_BevelFilter.__mro__:
        if "quality" in klass.__dict__:
            descriptor = klass.__dict__["quality"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bevelfilter_has_knockout():
    assert hasattr(fxg_BevelFilter, "knockout")
    descriptor = None
    for klass in fxg_BevelFilter.__mro__:
        if "knockout" in klass.__dict__:
            descriptor = klass.__dict__["knockout"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bevelfilter_has_strength():
    assert hasattr(fxg_BevelFilter, "strength")
    descriptor = None
    for klass in fxg_BevelFilter.__mro__:
        if "strength" in klass.__dict__:
            descriptor = klass.__dict__["strength"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bevelfilter_has_highlightAlpha():
    assert hasattr(fxg_BevelFilter, "highlightAlpha")
    descriptor = None
    for klass in fxg_BevelFilter.__mro__:
        if "highlightAlpha" in klass.__dict__:
            descriptor = klass.__dict__["highlightAlpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bevelfilter_has_angle():
    assert hasattr(fxg_BevelFilter, "angle")
    descriptor = None
    for klass in fxg_BevelFilter.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bevelfilter_has_shadowAlpha():
    assert hasattr(fxg_BevelFilter, "shadowAlpha")
    descriptor = None
    for klass in fxg_BevelFilter.__mro__:
        if "shadowAlpha" in klass.__dict__:
            descriptor = klass.__dict__["shadowAlpha"]
            break
    assert isinstance(descriptor, property)



def test_fxg_dropshadowfilter_is_not_abstract():
    assert not inspect.isabstract(fxg_DropShadowFilter)


def test_fxg_dropshadowfilter_constructor_exists():
    assert callable(fxg_DropShadowFilter.__init__)


def test_fxg_dropshadowfilter_constructor_args():
    sig = inspect.signature(fxg_DropShadowFilter.__init__)
    params = list(sig.parameters.keys())
    assert "hideObject" in params, "Missing parameter 'hideObject'"
    assert "color" in params, "Missing parameter 'color'"
    assert "inner" in params, "Missing parameter 'inner'"
    assert "strength" in params, "Missing parameter 'strength'"
    assert "blurY" in params, "Missing parameter 'blurY'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "distance" in params, "Missing parameter 'distance'"
    assert "blurX" in params, "Missing parameter 'blurX'"
    assert "angle" in params, "Missing parameter 'angle'"
    assert "quality" in params, "Missing parameter 'quality'"
    assert "knockout" in params, "Missing parameter 'knockout'"

def test_fxg_dropshadowfilter_has_hideObject():
    assert hasattr(fxg_DropShadowFilter, "hideObject")
    descriptor = None
    for klass in fxg_DropShadowFilter.__mro__:
        if "hideObject" in klass.__dict__:
            descriptor = klass.__dict__["hideObject"]
            break
    assert isinstance(descriptor, property)

def test_fxg_dropshadowfilter_has_color():
    assert hasattr(fxg_DropShadowFilter, "color")
    descriptor = None
    for klass in fxg_DropShadowFilter.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_fxg_dropshadowfilter_has_inner():
    assert hasattr(fxg_DropShadowFilter, "inner")
    descriptor = None
    for klass in fxg_DropShadowFilter.__mro__:
        if "inner" in klass.__dict__:
            descriptor = klass.__dict__["inner"]
            break
    assert isinstance(descriptor, property)

def test_fxg_dropshadowfilter_has_strength():
    assert hasattr(fxg_DropShadowFilter, "strength")
    descriptor = None
    for klass in fxg_DropShadowFilter.__mro__:
        if "strength" in klass.__dict__:
            descriptor = klass.__dict__["strength"]
            break
    assert isinstance(descriptor, property)

def test_fxg_dropshadowfilter_has_blurY():
    assert hasattr(fxg_DropShadowFilter, "blurY")
    descriptor = None
    for klass in fxg_DropShadowFilter.__mro__:
        if "blurY" in klass.__dict__:
            descriptor = klass.__dict__["blurY"]
            break
    assert isinstance(descriptor, property)

def test_fxg_dropshadowfilter_has_alpha():
    assert hasattr(fxg_DropShadowFilter, "alpha")
    descriptor = None
    for klass in fxg_DropShadowFilter.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg_dropshadowfilter_has_distance():
    assert hasattr(fxg_DropShadowFilter, "distance")
    descriptor = None
    for klass in fxg_DropShadowFilter.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)

def test_fxg_dropshadowfilter_has_blurX():
    assert hasattr(fxg_DropShadowFilter, "blurX")
    descriptor = None
    for klass in fxg_DropShadowFilter.__mro__:
        if "blurX" in klass.__dict__:
            descriptor = klass.__dict__["blurX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_dropshadowfilter_has_angle():
    assert hasattr(fxg_DropShadowFilter, "angle")
    descriptor = None
    for klass in fxg_DropShadowFilter.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)

def test_fxg_dropshadowfilter_has_quality():
    assert hasattr(fxg_DropShadowFilter, "quality")
    descriptor = None
    for klass in fxg_DropShadowFilter.__mro__:
        if "quality" in klass.__dict__:
            descriptor = klass.__dict__["quality"]
            break
    assert isinstance(descriptor, property)

def test_fxg_dropshadowfilter_has_knockout():
    assert hasattr(fxg_DropShadowFilter, "knockout")
    descriptor = None
    for klass in fxg_DropShadowFilter.__mro__:
        if "knockout" in klass.__dict__:
            descriptor = klass.__dict__["knockout"]
            break
    assert isinstance(descriptor, property)



def test_fxg_colormatrixfilter_is_not_abstract():
    assert not inspect.isabstract(fxg_ColorMatrixFilter)


def test_fxg_colormatrixfilter_constructor_exists():
    assert callable(fxg_ColorMatrixFilter.__init__)


def test_fxg_colormatrixfilter_constructor_args():
    sig = inspect.signature(fxg_ColorMatrixFilter.__init__)
    params = list(sig.parameters.keys())
    assert "matrix" in params, "Missing parameter 'matrix'"

def test_fxg_colormatrixfilter_has_matrix():
    assert hasattr(fxg_ColorMatrixFilter, "matrix")
    descriptor = None
    for klass in fxg_ColorMatrixFilter.__mro__:
        if "matrix" in klass.__dict__:
            descriptor = klass.__dict__["matrix"]
            break
    assert isinstance(descriptor, property)



def test_fxg_blurfilter_is_not_abstract():
    assert not inspect.isabstract(fxg_BlurFilter)


def test_fxg_blurfilter_constructor_exists():
    assert callable(fxg_BlurFilter.__init__)


def test_fxg_blurfilter_constructor_args():
    sig = inspect.signature(fxg_BlurFilter.__init__)
    params = list(sig.parameters.keys())
    assert "blurY" in params, "Missing parameter 'blurY'"
    assert "blurX" in params, "Missing parameter 'blurX'"
    assert "quality" in params, "Missing parameter 'quality'"

def test_fxg_blurfilter_has_blurY():
    assert hasattr(fxg_BlurFilter, "blurY")
    descriptor = None
    for klass in fxg_BlurFilter.__mro__:
        if "blurY" in klass.__dict__:
            descriptor = klass.__dict__["blurY"]
            break
    assert isinstance(descriptor, property)

def test_fxg_blurfilter_has_blurX():
    assert hasattr(fxg_BlurFilter, "blurX")
    descriptor = None
    for klass in fxg_BlurFilter.__mro__:
        if "blurX" in klass.__dict__:
            descriptor = klass.__dict__["blurX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_blurfilter_has_quality():
    assert hasattr(fxg_BlurFilter, "quality")
    descriptor = None
    for klass in fxg_BlurFilter.__mro__:
        if "quality" in klass.__dict__:
            descriptor = klass.__dict__["quality"]
            break
    assert isinstance(descriptor, property)



def test_fxg_lineargradientstroke_is_not_abstract():
    assert not inspect.isabstract(fxg_LinearGradientStroke)


def test_fxg_lineargradientstroke_constructor_exists():
    assert callable(fxg_LinearGradientStroke.__init__)


def test_fxg_lineargradientstroke_constructor_args():
    sig = inspect.signature(fxg_LinearGradientStroke.__init__)
    params = list(sig.parameters.keys())
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "y" in params, "Missing parameter 'y'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "miterLimit" in params, "Missing parameter 'miterLimit'"
    assert "pixelHinting" in params, "Missing parameter 'pixelHinting'"
    assert "x" in params, "Missing parameter 'x'"
    assert "interpolationMethod" in params, "Missing parameter 'interpolationMethod'"
    assert "spreadMethod" in params, "Missing parameter 'spreadMethod'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "scaleMode" in params, "Missing parameter 'scaleMode'"
    assert "joints" in params, "Missing parameter 'joints'"
    assert "caps" in params, "Missing parameter 'caps'"

def test_fxg_lineargradientstroke_has_scaleX():
    assert hasattr(fxg_LinearGradientStroke, "scaleX")
    descriptor = None
    for klass in fxg_LinearGradientStroke.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_lineargradientstroke_has_y():
    assert hasattr(fxg_LinearGradientStroke, "y")
    descriptor = None
    for klass in fxg_LinearGradientStroke.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg_lineargradientstroke_has_weight():
    assert hasattr(fxg_LinearGradientStroke, "weight")
    descriptor = None
    for klass in fxg_LinearGradientStroke.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_fxg_lineargradientstroke_has_miterLimit():
    assert hasattr(fxg_LinearGradientStroke, "miterLimit")
    descriptor = None
    for klass in fxg_LinearGradientStroke.__mro__:
        if "miterLimit" in klass.__dict__:
            descriptor = klass.__dict__["miterLimit"]
            break
    assert isinstance(descriptor, property)

def test_fxg_lineargradientstroke_has_pixelHinting():
    assert hasattr(fxg_LinearGradientStroke, "pixelHinting")
    descriptor = None
    for klass in fxg_LinearGradientStroke.__mro__:
        if "pixelHinting" in klass.__dict__:
            descriptor = klass.__dict__["pixelHinting"]
            break
    assert isinstance(descriptor, property)

def test_fxg_lineargradientstroke_has_x():
    assert hasattr(fxg_LinearGradientStroke, "x")
    descriptor = None
    for klass in fxg_LinearGradientStroke.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fxg_lineargradientstroke_has_interpolationMethod():
    assert hasattr(fxg_LinearGradientStroke, "interpolationMethod")
    descriptor = None
    for klass in fxg_LinearGradientStroke.__mro__:
        if "interpolationMethod" in klass.__dict__:
            descriptor = klass.__dict__["interpolationMethod"]
            break
    assert isinstance(descriptor, property)

def test_fxg_lineargradientstroke_has_spreadMethod():
    assert hasattr(fxg_LinearGradientStroke, "spreadMethod")
    descriptor = None
    for klass in fxg_LinearGradientStroke.__mro__:
        if "spreadMethod" in klass.__dict__:
            descriptor = klass.__dict__["spreadMethod"]
            break
    assert isinstance(descriptor, property)

def test_fxg_lineargradientstroke_has_rotation():
    assert hasattr(fxg_LinearGradientStroke, "rotation")
    descriptor = None
    for klass in fxg_LinearGradientStroke.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg_lineargradientstroke_has_scaleMode():
    assert hasattr(fxg_LinearGradientStroke, "scaleMode")
    descriptor = None
    for klass in fxg_LinearGradientStroke.__mro__:
        if "scaleMode" in klass.__dict__:
            descriptor = klass.__dict__["scaleMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg_lineargradientstroke_has_joints():
    assert hasattr(fxg_LinearGradientStroke, "joints")
    descriptor = None
    for klass in fxg_LinearGradientStroke.__mro__:
        if "joints" in klass.__dict__:
            descriptor = klass.__dict__["joints"]
            break
    assert isinstance(descriptor, property)

def test_fxg_lineargradientstroke_has_caps():
    assert hasattr(fxg_LinearGradientStroke, "caps")
    descriptor = None
    for klass in fxg_LinearGradientStroke.__mro__:
        if "caps" in klass.__dict__:
            descriptor = klass.__dict__["caps"]
            break
    assert isinstance(descriptor, property)



def test_stroke_is_not_abstract():
    assert not inspect.isabstract(Stroke)


def test_stroke_constructor_exists():
    assert callable(Stroke.__init__)


def test_stroke_constructor_args():
    sig = inspect.signature(Stroke.__init__)
    params = list(sig.parameters.keys())



def test_fxg_solidcolorstroke_is_not_abstract():
    assert not inspect.isabstract(fxg_SolidColorStroke)


def test_fxg_solidcolorstroke_constructor_exists():
    assert callable(fxg_SolidColorStroke.__init__)


def test_fxg_solidcolorstroke_constructor_args():
    sig = inspect.signature(fxg_SolidColorStroke.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "scaleMode" in params, "Missing parameter 'scaleMode'"
    assert "joints" in params, "Missing parameter 'joints'"
    assert "miterLimit" in params, "Missing parameter 'miterLimit'"
    assert "pixelHinting" in params, "Missing parameter 'pixelHinting'"
    assert "color" in params, "Missing parameter 'color'"
    assert "caps" in params, "Missing parameter 'caps'"

def test_fxg_solidcolorstroke_has_weight():
    assert hasattr(fxg_SolidColorStroke, "weight")
    descriptor = None
    for klass in fxg_SolidColorStroke.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_fxg_solidcolorstroke_has_alpha():
    assert hasattr(fxg_SolidColorStroke, "alpha")
    descriptor = None
    for klass in fxg_SolidColorStroke.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg_solidcolorstroke_has_scaleMode():
    assert hasattr(fxg_SolidColorStroke, "scaleMode")
    descriptor = None
    for klass in fxg_SolidColorStroke.__mro__:
        if "scaleMode" in klass.__dict__:
            descriptor = klass.__dict__["scaleMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg_solidcolorstroke_has_joints():
    assert hasattr(fxg_SolidColorStroke, "joints")
    descriptor = None
    for klass in fxg_SolidColorStroke.__mro__:
        if "joints" in klass.__dict__:
            descriptor = klass.__dict__["joints"]
            break
    assert isinstance(descriptor, property)

def test_fxg_solidcolorstroke_has_miterLimit():
    assert hasattr(fxg_SolidColorStroke, "miterLimit")
    descriptor = None
    for klass in fxg_SolidColorStroke.__mro__:
        if "miterLimit" in klass.__dict__:
            descriptor = klass.__dict__["miterLimit"]
            break
    assert isinstance(descriptor, property)

def test_fxg_solidcolorstroke_has_pixelHinting():
    assert hasattr(fxg_SolidColorStroke, "pixelHinting")
    descriptor = None
    for klass in fxg_SolidColorStroke.__mro__:
        if "pixelHinting" in klass.__dict__:
            descriptor = klass.__dict__["pixelHinting"]
            break
    assert isinstance(descriptor, property)

def test_fxg_solidcolorstroke_has_color():
    assert hasattr(fxg_SolidColorStroke, "color")
    descriptor = None
    for klass in fxg_SolidColorStroke.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_fxg_solidcolorstroke_has_caps():
    assert hasattr(fxg_SolidColorStroke, "caps")
    descriptor = None
    for klass in fxg_SolidColorStroke.__mro__:
        if "caps" in klass.__dict__:
            descriptor = klass.__dict__["caps"]
            break
    assert isinstance(descriptor, property)



def test_fxg_radialgradientstroke_is_not_abstract():
    assert not inspect.isabstract(fxg_RadialGradientStroke)


def test_fxg_radialgradientstroke_constructor_exists():
    assert callable(fxg_RadialGradientStroke.__init__)


def test_fxg_radialgradientstroke_constructor_args():
    sig = inspect.signature(fxg_RadialGradientStroke.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "focalPointRatio" in params, "Missing parameter 'focalPointRatio'"
    assert "joints" in params, "Missing parameter 'joints'"
    assert "scaleMode" in params, "Missing parameter 'scaleMode'"
    assert "pixelHinting" in params, "Missing parameter 'pixelHinting'"
    assert "interpolationMethod" in params, "Missing parameter 'interpolationMethod'"
    assert "caps" in params, "Missing parameter 'caps'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "miterLimit" in params, "Missing parameter 'miterLimit'"
    assert "x" in params, "Missing parameter 'x'"
    assert "spreadMethod" in params, "Missing parameter 'spreadMethod'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"

def test_fxg_radialgradientstroke_has_y():
    assert hasattr(fxg_RadialGradientStroke, "y")
    descriptor = None
    for klass in fxg_RadialGradientStroke.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg_radialgradientstroke_has_weight():
    assert hasattr(fxg_RadialGradientStroke, "weight")
    descriptor = None
    for klass in fxg_RadialGradientStroke.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_fxg_radialgradientstroke_has_focalPointRatio():
    assert hasattr(fxg_RadialGradientStroke, "focalPointRatio")
    descriptor = None
    for klass in fxg_RadialGradientStroke.__mro__:
        if "focalPointRatio" in klass.__dict__:
            descriptor = klass.__dict__["focalPointRatio"]
            break
    assert isinstance(descriptor, property)

def test_fxg_radialgradientstroke_has_joints():
    assert hasattr(fxg_RadialGradientStroke, "joints")
    descriptor = None
    for klass in fxg_RadialGradientStroke.__mro__:
        if "joints" in klass.__dict__:
            descriptor = klass.__dict__["joints"]
            break
    assert isinstance(descriptor, property)

def test_fxg_radialgradientstroke_has_scaleMode():
    assert hasattr(fxg_RadialGradientStroke, "scaleMode")
    descriptor = None
    for klass in fxg_RadialGradientStroke.__mro__:
        if "scaleMode" in klass.__dict__:
            descriptor = klass.__dict__["scaleMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg_radialgradientstroke_has_pixelHinting():
    assert hasattr(fxg_RadialGradientStroke, "pixelHinting")
    descriptor = None
    for klass in fxg_RadialGradientStroke.__mro__:
        if "pixelHinting" in klass.__dict__:
            descriptor = klass.__dict__["pixelHinting"]
            break
    assert isinstance(descriptor, property)

def test_fxg_radialgradientstroke_has_interpolationMethod():
    assert hasattr(fxg_RadialGradientStroke, "interpolationMethod")
    descriptor = None
    for klass in fxg_RadialGradientStroke.__mro__:
        if "interpolationMethod" in klass.__dict__:
            descriptor = klass.__dict__["interpolationMethod"]
            break
    assert isinstance(descriptor, property)

def test_fxg_radialgradientstroke_has_caps():
    assert hasattr(fxg_RadialGradientStroke, "caps")
    descriptor = None
    for klass in fxg_RadialGradientStroke.__mro__:
        if "caps" in klass.__dict__:
            descriptor = klass.__dict__["caps"]
            break
    assert isinstance(descriptor, property)

def test_fxg_radialgradientstroke_has_scaleX():
    assert hasattr(fxg_RadialGradientStroke, "scaleX")
    descriptor = None
    for klass in fxg_RadialGradientStroke.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_radialgradientstroke_has_rotation():
    assert hasattr(fxg_RadialGradientStroke, "rotation")
    descriptor = None
    for klass in fxg_RadialGradientStroke.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg_radialgradientstroke_has_miterLimit():
    assert hasattr(fxg_RadialGradientStroke, "miterLimit")
    descriptor = None
    for klass in fxg_RadialGradientStroke.__mro__:
        if "miterLimit" in klass.__dict__:
            descriptor = klass.__dict__["miterLimit"]
            break
    assert isinstance(descriptor, property)

def test_fxg_radialgradientstroke_has_x():
    assert hasattr(fxg_RadialGradientStroke, "x")
    descriptor = None
    for klass in fxg_RadialGradientStroke.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fxg_radialgradientstroke_has_spreadMethod():
    assert hasattr(fxg_RadialGradientStroke, "spreadMethod")
    descriptor = None
    for klass in fxg_RadialGradientStroke.__mro__:
        if "spreadMethod" in klass.__dict__:
            descriptor = klass.__dict__["spreadMethod"]
            break
    assert isinstance(descriptor, property)

def test_fxg_radialgradientstroke_has_scaleY():
    assert hasattr(fxg_RadialGradientStroke, "scaleY")
    descriptor = None
    for klass in fxg_RadialGradientStroke.__mro__:
        if "scaleY" in klass.__dict__:
            descriptor = klass.__dict__["scaleY"]
            break
    assert isinstance(descriptor, property)



def test_fxg_radialgradient_is_not_abstract():
    assert not inspect.isabstract(fxg_RadialGradient)


def test_fxg_radialgradient_constructor_exists():
    assert callable(fxg_RadialGradient.__init__)


def test_fxg_radialgradient_constructor_args():
    sig = inspect.signature(fxg_RadialGradient.__init__)
    params = list(sig.parameters.keys())
    assert "focalPointRatio" in params, "Missing parameter 'focalPointRatio'"
    assert "x" in params, "Missing parameter 'x'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "y" in params, "Missing parameter 'y'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "spreadMethod" in params, "Missing parameter 'spreadMethod'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "interpolationMethod" in params, "Missing parameter 'interpolationMethod'"

def test_fxg_radialgradient_has_focalPointRatio():
    assert hasattr(fxg_RadialGradient, "focalPointRatio")
    descriptor = None
    for klass in fxg_RadialGradient.__mro__:
        if "focalPointRatio" in klass.__dict__:
            descriptor = klass.__dict__["focalPointRatio"]
            break
    assert isinstance(descriptor, property)

def test_fxg_radialgradient_has_x():
    assert hasattr(fxg_RadialGradient, "x")
    descriptor = None
    for klass in fxg_RadialGradient.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fxg_radialgradient_has_scaleY():
    assert hasattr(fxg_RadialGradient, "scaleY")
    descriptor = None
    for klass in fxg_RadialGradient.__mro__:
        if "scaleY" in klass.__dict__:
            descriptor = klass.__dict__["scaleY"]
            break
    assert isinstance(descriptor, property)

def test_fxg_radialgradient_has_y():
    assert hasattr(fxg_RadialGradient, "y")
    descriptor = None
    for klass in fxg_RadialGradient.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg_radialgradient_has_rotation():
    assert hasattr(fxg_RadialGradient, "rotation")
    descriptor = None
    for klass in fxg_RadialGradient.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg_radialgradient_has_spreadMethod():
    assert hasattr(fxg_RadialGradient, "spreadMethod")
    descriptor = None
    for klass in fxg_RadialGradient.__mro__:
        if "spreadMethod" in klass.__dict__:
            descriptor = klass.__dict__["spreadMethod"]
            break
    assert isinstance(descriptor, property)

def test_fxg_radialgradient_has_scaleX():
    assert hasattr(fxg_RadialGradient, "scaleX")
    descriptor = None
    for klass in fxg_RadialGradient.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_radialgradient_has_interpolationMethod():
    assert hasattr(fxg_RadialGradient, "interpolationMethod")
    descriptor = None
    for klass in fxg_RadialGradient.__mro__:
        if "interpolationMethod" in klass.__dict__:
            descriptor = klass.__dict__["interpolationMethod"]
            break
    assert isinstance(descriptor, property)



def test_fxg_lineargradient_is_not_abstract():
    assert not inspect.isabstract(fxg_LinearGradient)


def test_fxg_lineargradient_constructor_exists():
    assert callable(fxg_LinearGradient.__init__)


def test_fxg_lineargradient_constructor_args():
    sig = inspect.signature(fxg_LinearGradient.__init__)
    params = list(sig.parameters.keys())
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "interpolationMethod" in params, "Missing parameter 'interpolationMethod'"
    assert "x" in params, "Missing parameter 'x'"
    assert "spreadMethod" in params, "Missing parameter 'spreadMethod'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "y" in params, "Missing parameter 'y'"

def test_fxg_lineargradient_has_scaleX():
    assert hasattr(fxg_LinearGradient, "scaleX")
    descriptor = None
    for klass in fxg_LinearGradient.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_lineargradient_has_interpolationMethod():
    assert hasattr(fxg_LinearGradient, "interpolationMethod")
    descriptor = None
    for klass in fxg_LinearGradient.__mro__:
        if "interpolationMethod" in klass.__dict__:
            descriptor = klass.__dict__["interpolationMethod"]
            break
    assert isinstance(descriptor, property)

def test_fxg_lineargradient_has_x():
    assert hasattr(fxg_LinearGradient, "x")
    descriptor = None
    for klass in fxg_LinearGradient.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fxg_lineargradient_has_spreadMethod():
    assert hasattr(fxg_LinearGradient, "spreadMethod")
    descriptor = None
    for klass in fxg_LinearGradient.__mro__:
        if "spreadMethod" in klass.__dict__:
            descriptor = klass.__dict__["spreadMethod"]
            break
    assert isinstance(descriptor, property)

def test_fxg_lineargradient_has_rotation():
    assert hasattr(fxg_LinearGradient, "rotation")
    descriptor = None
    for klass in fxg_LinearGradient.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg_lineargradient_has_y():
    assert hasattr(fxg_LinearGradient, "y")
    descriptor = None
    for klass in fxg_LinearGradient.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_fill_is_not_abstract():
    assert not inspect.isabstract(Fill)


def test_fill_constructor_exists():
    assert callable(Fill.__init__)


def test_fill_constructor_args():
    sig = inspect.signature(Fill.__init__)
    params = list(sig.parameters.keys())



def test_fxg_solidcolor_is_not_abstract():
    assert not inspect.isabstract(fxg_SolidColor)


def test_fxg_solidcolor_constructor_exists():
    assert callable(fxg_SolidColor.__init__)


def test_fxg_solidcolor_constructor_args():
    sig = inspect.signature(fxg_SolidColor.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "alpha" in params, "Missing parameter 'alpha'"

def test_fxg_solidcolor_has_color():
    assert hasattr(fxg_SolidColor, "color")
    descriptor = None
    for klass in fxg_SolidColor.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_fxg_solidcolor_has_alpha():
    assert hasattr(fxg_SolidColor, "alpha")
    descriptor = None
    for klass in fxg_SolidColor.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)



def test_fxg_linkactiveformat_is_not_abstract():
    assert not inspect.isabstract(fxg_linkActiveFormat)


def test_fxg_linkactiveformat_constructor_exists():
    assert callable(fxg_linkActiveFormat.__init__)


def test_fxg_linkactiveformat_constructor_args():
    sig = inspect.signature(fxg_linkActiveFormat.__init__)
    params = list(sig.parameters.keys())



def test_richtextcontentcontainer_is_not_abstract():
    assert not inspect.isabstract(RichTextContentContainer)


def test_richtextcontentcontainer_constructor_exists():
    assert callable(RichTextContentContainer.__init__)


def test_richtextcontentcontainer_constructor_args():
    sig = inspect.signature(RichTextContentContainer.__init__)
    params = list(sig.parameters.keys())



def test_fxg_bitmapfill_is_not_abstract():
    assert not inspect.isabstract(fxg_BitmapFill)


def test_fxg_bitmapfill_constructor_exists():
    assert callable(fxg_BitmapFill.__init__)


def test_fxg_bitmapfill_constructor_args():
    sig = inspect.signature(fxg_BitmapFill.__init__)
    params = list(sig.parameters.keys())
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "fillMode" in params, "Missing parameter 'fillMode'"
    assert "y" in params, "Missing parameter 'y'"
    assert "source" in params, "Missing parameter 'source'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "x" in params, "Missing parameter 'x'"

def test_fxg_bitmapfill_has_scaleX():
    assert hasattr(fxg_BitmapFill, "scaleX")
    descriptor = None
    for klass in fxg_BitmapFill.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bitmapfill_has_fillMode():
    assert hasattr(fxg_BitmapFill, "fillMode")
    descriptor = None
    for klass in fxg_BitmapFill.__mro__:
        if "fillMode" in klass.__dict__:
            descriptor = klass.__dict__["fillMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bitmapfill_has_y():
    assert hasattr(fxg_BitmapFill, "y")
    descriptor = None
    for klass in fxg_BitmapFill.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bitmapfill_has_source():
    assert hasattr(fxg_BitmapFill, "source")
    descriptor = None
    for klass in fxg_BitmapFill.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bitmapfill_has_scaleY():
    assert hasattr(fxg_BitmapFill, "scaleY")
    descriptor = None
    for klass in fxg_BitmapFill.__mro__:
        if "scaleY" in klass.__dict__:
            descriptor = klass.__dict__["scaleY"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bitmapfill_has_rotation():
    assert hasattr(fxg_BitmapFill, "rotation")
    descriptor = None
    for klass in fxg_BitmapFill.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bitmapfill_has_x():
    assert hasattr(fxg_BitmapFill, "x")
    descriptor = None
    for klass in fxg_BitmapFill.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_fxg_characterattributes_is_not_abstract():
    assert not inspect.isabstract(fxg_CharacterAttributes)


def test_fxg_characterattributes_constructor_exists():
    assert callable(fxg_CharacterAttributes.__init__)


def test_fxg_characterattributes_constructor_args():
    sig = inspect.signature(fxg_CharacterAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "backgroundAlpha" in params, "Missing parameter 'backgroundAlpha'"
    assert "breakOpportunity" in params, "Missing parameter 'breakOpportunity'"
    assert "digitWidth" in params, "Missing parameter 'digitWidth'"
    assert "textDecoration" in params, "Missing parameter 'textDecoration'"
    assert "alignmentBaseline" in params, "Missing parameter 'alignmentBaseline'"
    assert "dominantBaseline" in params, "Missing parameter 'dominantBaseline'"
    assert "color" in params, "Missing parameter 'color'"
    assert "baselineShift" in params, "Missing parameter 'baselineShift'"
    assert "fontStyle" in params, "Missing parameter 'fontStyle'"
    assert "fontWeight" in params, "Missing parameter 'fontWeight'"
    assert "fontSize" in params, "Missing parameter 'fontSize'"
    assert "fontFamily" in params, "Missing parameter 'fontFamily'"
    assert "ligatureLevel" in params, "Missing parameter 'ligatureLevel'"
    assert "lineHeight" in params, "Missing parameter 'lineHeight'"
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"
    assert "digitCase" in params, "Missing parameter 'digitCase'"
    assert "kerning" in params, "Missing parameter 'kerning'"
    assert "trackingLeft" in params, "Missing parameter 'trackingLeft'"
    assert "locale" in params, "Missing parameter 'locale'"
    assert "textRotation" in params, "Missing parameter 'textRotation'"
    assert "textAlpha" in params, "Missing parameter 'textAlpha'"
    assert "trackingRight" in params, "Missing parameter 'trackingRight'"
    assert "whiteSpaceCollapse" in params, "Missing parameter 'whiteSpaceCollapse'"
    assert "lineThrough" in params, "Missing parameter 'lineThrough'"
    assert "typographicCase" in params, "Missing parameter 'typographicCase'"

def test_fxg_characterattributes_has_backgroundAlpha():
    assert hasattr(fxg_CharacterAttributes, "backgroundAlpha")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "backgroundAlpha" in klass.__dict__:
            descriptor = klass.__dict__["backgroundAlpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_breakOpportunity():
    assert hasattr(fxg_CharacterAttributes, "breakOpportunity")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "breakOpportunity" in klass.__dict__:
            descriptor = klass.__dict__["breakOpportunity"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_digitWidth():
    assert hasattr(fxg_CharacterAttributes, "digitWidth")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "digitWidth" in klass.__dict__:
            descriptor = klass.__dict__["digitWidth"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_textDecoration():
    assert hasattr(fxg_CharacterAttributes, "textDecoration")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "textDecoration" in klass.__dict__:
            descriptor = klass.__dict__["textDecoration"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_alignmentBaseline():
    assert hasattr(fxg_CharacterAttributes, "alignmentBaseline")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "alignmentBaseline" in klass.__dict__:
            descriptor = klass.__dict__["alignmentBaseline"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_dominantBaseline():
    assert hasattr(fxg_CharacterAttributes, "dominantBaseline")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "dominantBaseline" in klass.__dict__:
            descriptor = klass.__dict__["dominantBaseline"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_color():
    assert hasattr(fxg_CharacterAttributes, "color")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_baselineShift():
    assert hasattr(fxg_CharacterAttributes, "baselineShift")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "baselineShift" in klass.__dict__:
            descriptor = klass.__dict__["baselineShift"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_fontStyle():
    assert hasattr(fxg_CharacterAttributes, "fontStyle")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "fontStyle" in klass.__dict__:
            descriptor = klass.__dict__["fontStyle"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_fontWeight():
    assert hasattr(fxg_CharacterAttributes, "fontWeight")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "fontWeight" in klass.__dict__:
            descriptor = klass.__dict__["fontWeight"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_fontSize():
    assert hasattr(fxg_CharacterAttributes, "fontSize")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "fontSize" in klass.__dict__:
            descriptor = klass.__dict__["fontSize"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_fontFamily():
    assert hasattr(fxg_CharacterAttributes, "fontFamily")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "fontFamily" in klass.__dict__:
            descriptor = klass.__dict__["fontFamily"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_ligatureLevel():
    assert hasattr(fxg_CharacterAttributes, "ligatureLevel")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "ligatureLevel" in klass.__dict__:
            descriptor = klass.__dict__["ligatureLevel"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_lineHeight():
    assert hasattr(fxg_CharacterAttributes, "lineHeight")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "lineHeight" in klass.__dict__:
            descriptor = klass.__dict__["lineHeight"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_backgroundColor():
    assert hasattr(fxg_CharacterAttributes, "backgroundColor")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "backgroundColor" in klass.__dict__:
            descriptor = klass.__dict__["backgroundColor"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_digitCase():
    assert hasattr(fxg_CharacterAttributes, "digitCase")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "digitCase" in klass.__dict__:
            descriptor = klass.__dict__["digitCase"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_kerning():
    assert hasattr(fxg_CharacterAttributes, "kerning")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "kerning" in klass.__dict__:
            descriptor = klass.__dict__["kerning"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_trackingLeft():
    assert hasattr(fxg_CharacterAttributes, "trackingLeft")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "trackingLeft" in klass.__dict__:
            descriptor = klass.__dict__["trackingLeft"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_locale():
    assert hasattr(fxg_CharacterAttributes, "locale")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "locale" in klass.__dict__:
            descriptor = klass.__dict__["locale"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_textRotation():
    assert hasattr(fxg_CharacterAttributes, "textRotation")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "textRotation" in klass.__dict__:
            descriptor = klass.__dict__["textRotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_textAlpha():
    assert hasattr(fxg_CharacterAttributes, "textAlpha")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "textAlpha" in klass.__dict__:
            descriptor = klass.__dict__["textAlpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_trackingRight():
    assert hasattr(fxg_CharacterAttributes, "trackingRight")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "trackingRight" in klass.__dict__:
            descriptor = klass.__dict__["trackingRight"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_whiteSpaceCollapse():
    assert hasattr(fxg_CharacterAttributes, "whiteSpaceCollapse")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "whiteSpaceCollapse" in klass.__dict__:
            descriptor = klass.__dict__["whiteSpaceCollapse"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_lineThrough():
    assert hasattr(fxg_CharacterAttributes, "lineThrough")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "lineThrough" in klass.__dict__:
            descriptor = klass.__dict__["lineThrough"]
            break
    assert isinstance(descriptor, property)

def test_fxg_characterattributes_has_typographicCase():
    assert hasattr(fxg_CharacterAttributes, "typographicCase")
    descriptor = None
    for klass in fxg_CharacterAttributes.__mro__:
        if "typographicCase" in klass.__dict__:
            descriptor = klass.__dict__["typographicCase"]
            break
    assert isinstance(descriptor, property)



def test_fxg_containerattributes_is_not_abstract():
    assert not inspect.isabstract(fxg_ContainerAttributes)


def test_fxg_containerattributes_constructor_exists():
    assert callable(fxg_ContainerAttributes.__init__)


def test_fxg_containerattributes_constructor_args():
    sig = inspect.signature(fxg_ContainerAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "paddingBottom" in params, "Missing parameter 'paddingBottom'"
    assert "paddingTop" in params, "Missing parameter 'paddingTop'"
    assert "columnWidth" in params, "Missing parameter 'columnWidth'"
    assert "blockProgression" in params, "Missing parameter 'blockProgression'"
    assert "paddingLeft" in params, "Missing parameter 'paddingLeft'"
    assert "firstBaselineOffset" in params, "Missing parameter 'firstBaselineOffset'"
    assert "verticalAlign" in params, "Missing parameter 'verticalAlign'"
    assert "paddingRight" in params, "Missing parameter 'paddingRight'"
    assert "columnCount" in params, "Missing parameter 'columnCount'"
    assert "lineBreak" in params, "Missing parameter 'lineBreak'"
    assert "columnGap" in params, "Missing parameter 'columnGap'"

def test_fxg_containerattributes_has_paddingBottom():
    assert hasattr(fxg_ContainerAttributes, "paddingBottom")
    descriptor = None
    for klass in fxg_ContainerAttributes.__mro__:
        if "paddingBottom" in klass.__dict__:
            descriptor = klass.__dict__["paddingBottom"]
            break
    assert isinstance(descriptor, property)

def test_fxg_containerattributes_has_paddingTop():
    assert hasattr(fxg_ContainerAttributes, "paddingTop")
    descriptor = None
    for klass in fxg_ContainerAttributes.__mro__:
        if "paddingTop" in klass.__dict__:
            descriptor = klass.__dict__["paddingTop"]
            break
    assert isinstance(descriptor, property)

def test_fxg_containerattributes_has_columnWidth():
    assert hasattr(fxg_ContainerAttributes, "columnWidth")
    descriptor = None
    for klass in fxg_ContainerAttributes.__mro__:
        if "columnWidth" in klass.__dict__:
            descriptor = klass.__dict__["columnWidth"]
            break
    assert isinstance(descriptor, property)

def test_fxg_containerattributes_has_blockProgression():
    assert hasattr(fxg_ContainerAttributes, "blockProgression")
    descriptor = None
    for klass in fxg_ContainerAttributes.__mro__:
        if "blockProgression" in klass.__dict__:
            descriptor = klass.__dict__["blockProgression"]
            break
    assert isinstance(descriptor, property)

def test_fxg_containerattributes_has_paddingLeft():
    assert hasattr(fxg_ContainerAttributes, "paddingLeft")
    descriptor = None
    for klass in fxg_ContainerAttributes.__mro__:
        if "paddingLeft" in klass.__dict__:
            descriptor = klass.__dict__["paddingLeft"]
            break
    assert isinstance(descriptor, property)

def test_fxg_containerattributes_has_firstBaselineOffset():
    assert hasattr(fxg_ContainerAttributes, "firstBaselineOffset")
    descriptor = None
    for klass in fxg_ContainerAttributes.__mro__:
        if "firstBaselineOffset" in klass.__dict__:
            descriptor = klass.__dict__["firstBaselineOffset"]
            break
    assert isinstance(descriptor, property)

def test_fxg_containerattributes_has_verticalAlign():
    assert hasattr(fxg_ContainerAttributes, "verticalAlign")
    descriptor = None
    for klass in fxg_ContainerAttributes.__mro__:
        if "verticalAlign" in klass.__dict__:
            descriptor = klass.__dict__["verticalAlign"]
            break
    assert isinstance(descriptor, property)

def test_fxg_containerattributes_has_paddingRight():
    assert hasattr(fxg_ContainerAttributes, "paddingRight")
    descriptor = None
    for klass in fxg_ContainerAttributes.__mro__:
        if "paddingRight" in klass.__dict__:
            descriptor = klass.__dict__["paddingRight"]
            break
    assert isinstance(descriptor, property)

def test_fxg_containerattributes_has_columnCount():
    assert hasattr(fxg_ContainerAttributes, "columnCount")
    descriptor = None
    for klass in fxg_ContainerAttributes.__mro__:
        if "columnCount" in klass.__dict__:
            descriptor = klass.__dict__["columnCount"]
            break
    assert isinstance(descriptor, property)

def test_fxg_containerattributes_has_lineBreak():
    assert hasattr(fxg_ContainerAttributes, "lineBreak")
    descriptor = None
    for klass in fxg_ContainerAttributes.__mro__:
        if "lineBreak" in klass.__dict__:
            descriptor = klass.__dict__["lineBreak"]
            break
    assert isinstance(descriptor, property)

def test_fxg_containerattributes_has_columnGap():
    assert hasattr(fxg_ContainerAttributes, "columnGap")
    descriptor = None
    for klass in fxg_ContainerAttributes.__mro__:
        if "columnGap" in klass.__dict__:
            descriptor = klass.__dict__["columnGap"]
            break
    assert isinstance(descriptor, property)



def test_fxg_paragraphattributes_is_not_abstract():
    assert not inspect.isabstract(fxg_ParagraphAttributes)


def test_fxg_paragraphattributes_constructor_exists():
    assert callable(fxg_ParagraphAttributes.__init__)


def test_fxg_paragraphattributes_constructor_args():
    sig = inspect.signature(fxg_ParagraphAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "paragraphSpaceBefore" in params, "Missing parameter 'paragraphSpaceBefore'"
    assert "textAlign" in params, "Missing parameter 'textAlign'"
    assert "paragraphSpaceAfter" in params, "Missing parameter 'paragraphSpaceAfter'"
    assert "justificationStyle" in params, "Missing parameter 'justificationStyle'"
    assert "leadingModel" in params, "Missing parameter 'leadingModel'"
    assert "textIndent" in params, "Missing parameter 'textIndent'"
    assert "tabStops" in params, "Missing parameter 'tabStops'"
    assert "textAlignLast" in params, "Missing parameter 'textAlignLast'"
    assert "paragraphEndIndent" in params, "Missing parameter 'paragraphEndIndent'"
    assert "justificationRule" in params, "Missing parameter 'justificationRule'"
    assert "paragraphStartIndent" in params, "Missing parameter 'paragraphStartIndent'"
    assert "textJustify" in params, "Missing parameter 'textJustify'"

def test_fxg_paragraphattributes_has_paragraphSpaceBefore():
    assert hasattr(fxg_ParagraphAttributes, "paragraphSpaceBefore")
    descriptor = None
    for klass in fxg_ParagraphAttributes.__mro__:
        if "paragraphSpaceBefore" in klass.__dict__:
            descriptor = klass.__dict__["paragraphSpaceBefore"]
            break
    assert isinstance(descriptor, property)

def test_fxg_paragraphattributes_has_textAlign():
    assert hasattr(fxg_ParagraphAttributes, "textAlign")
    descriptor = None
    for klass in fxg_ParagraphAttributes.__mro__:
        if "textAlign" in klass.__dict__:
            descriptor = klass.__dict__["textAlign"]
            break
    assert isinstance(descriptor, property)

def test_fxg_paragraphattributes_has_paragraphSpaceAfter():
    assert hasattr(fxg_ParagraphAttributes, "paragraphSpaceAfter")
    descriptor = None
    for klass in fxg_ParagraphAttributes.__mro__:
        if "paragraphSpaceAfter" in klass.__dict__:
            descriptor = klass.__dict__["paragraphSpaceAfter"]
            break
    assert isinstance(descriptor, property)

def test_fxg_paragraphattributes_has_justificationStyle():
    assert hasattr(fxg_ParagraphAttributes, "justificationStyle")
    descriptor = None
    for klass in fxg_ParagraphAttributes.__mro__:
        if "justificationStyle" in klass.__dict__:
            descriptor = klass.__dict__["justificationStyle"]
            break
    assert isinstance(descriptor, property)

def test_fxg_paragraphattributes_has_leadingModel():
    assert hasattr(fxg_ParagraphAttributes, "leadingModel")
    descriptor = None
    for klass in fxg_ParagraphAttributes.__mro__:
        if "leadingModel" in klass.__dict__:
            descriptor = klass.__dict__["leadingModel"]
            break
    assert isinstance(descriptor, property)

def test_fxg_paragraphattributes_has_textIndent():
    assert hasattr(fxg_ParagraphAttributes, "textIndent")
    descriptor = None
    for klass in fxg_ParagraphAttributes.__mro__:
        if "textIndent" in klass.__dict__:
            descriptor = klass.__dict__["textIndent"]
            break
    assert isinstance(descriptor, property)

def test_fxg_paragraphattributes_has_tabStops():
    assert hasattr(fxg_ParagraphAttributes, "tabStops")
    descriptor = None
    for klass in fxg_ParagraphAttributes.__mro__:
        if "tabStops" in klass.__dict__:
            descriptor = klass.__dict__["tabStops"]
            break
    assert isinstance(descriptor, property)

def test_fxg_paragraphattributes_has_textAlignLast():
    assert hasattr(fxg_ParagraphAttributes, "textAlignLast")
    descriptor = None
    for klass in fxg_ParagraphAttributes.__mro__:
        if "textAlignLast" in klass.__dict__:
            descriptor = klass.__dict__["textAlignLast"]
            break
    assert isinstance(descriptor, property)

def test_fxg_paragraphattributes_has_paragraphEndIndent():
    assert hasattr(fxg_ParagraphAttributes, "paragraphEndIndent")
    descriptor = None
    for klass in fxg_ParagraphAttributes.__mro__:
        if "paragraphEndIndent" in klass.__dict__:
            descriptor = klass.__dict__["paragraphEndIndent"]
            break
    assert isinstance(descriptor, property)

def test_fxg_paragraphattributes_has_justificationRule():
    assert hasattr(fxg_ParagraphAttributes, "justificationRule")
    descriptor = None
    for klass in fxg_ParagraphAttributes.__mro__:
        if "justificationRule" in klass.__dict__:
            descriptor = klass.__dict__["justificationRule"]
            break
    assert isinstance(descriptor, property)

def test_fxg_paragraphattributes_has_paragraphStartIndent():
    assert hasattr(fxg_ParagraphAttributes, "paragraphStartIndent")
    descriptor = None
    for klass in fxg_ParagraphAttributes.__mro__:
        if "paragraphStartIndent" in klass.__dict__:
            descriptor = klass.__dict__["paragraphStartIndent"]
            break
    assert isinstance(descriptor, property)

def test_fxg_paragraphattributes_has_textJustify():
    assert hasattr(fxg_ParagraphAttributes, "textJustify")
    descriptor = None
    for klass in fxg_ParagraphAttributes.__mro__:
        if "textJustify" in klass.__dict__:
            descriptor = klass.__dict__["textJustify"]
            break
    assert isinstance(descriptor, property)



def test_richtextcontent_is_not_abstract():
    assert not inspect.isabstract(RichTextContent)


def test_richtextcontent_constructor_exists():
    assert callable(RichTextContent.__init__)


def test_richtextcontent_constructor_args():
    sig = inspect.signature(RichTextContent.__init__)
    params = list(sig.parameters.keys())



def test_fxg_a_is_not_abstract():
    assert not inspect.isabstract(fxg_a)


def test_fxg_a_constructor_exists():
    assert callable(fxg_a.__init__)


def test_fxg_a_constructor_args():
    sig = inspect.signature(fxg_a.__init__)
    params = list(sig.parameters.keys())



def test_fxg_br_is_not_abstract():
    assert not inspect.isabstract(fxg_br)


def test_fxg_br_constructor_exists():
    assert callable(fxg_br.__init__)


def test_fxg_br_constructor_args():
    sig = inspect.signature(fxg_br.__init__)
    params = list(sig.parameters.keys())



def test_fxg_rawtext_is_not_abstract():
    assert not inspect.isabstract(fxg_rawtext)


def test_fxg_rawtext_constructor_exists():
    assert callable(fxg_rawtext.__init__)


def test_fxg_rawtext_constructor_args():
    sig = inspect.signature(fxg_rawtext.__init__)
    params = list(sig.parameters.keys())
    assert "_text" in params, "Missing parameter '_text'"

def test_fxg_rawtext_has__text():
    assert hasattr(fxg_rawtext, "_text")
    descriptor = None
    for klass in fxg_rawtext.__mro__:
        if "_text" in klass.__dict__:
            descriptor = klass.__dict__["_text"]
            break
    assert isinstance(descriptor, property)



def test_fxg_tab_is_not_abstract():
    assert not inspect.isabstract(fxg_tab)


def test_fxg_tab_constructor_exists():
    assert callable(fxg_tab.__init__)


def test_fxg_tab_constructor_args():
    sig = inspect.signature(fxg_tab.__init__)
    params = list(sig.parameters.keys())



def test_fxg_img_is_not_abstract():
    assert not inspect.isabstract(fxg_img)


def test_fxg_img_constructor_exists():
    assert callable(fxg_img.__init__)


def test_fxg_img_constructor_args():
    sig = inspect.signature(fxg_img.__init__)
    params = list(sig.parameters.keys())



def test_fxg_span_is_not_abstract():
    assert not inspect.isabstract(fxg_span)


def test_fxg_span_constructor_exists():
    assert callable(fxg_span.__init__)


def test_fxg_span_constructor_args():
    sig = inspect.signature(fxg_span.__init__)
    params = list(sig.parameters.keys())



def test_fxg_linknormalformat_is_not_abstract():
    assert not inspect.isabstract(fxg_linkNormalFormat)


def test_fxg_linknormalformat_constructor_exists():
    assert callable(fxg_linkNormalFormat.__init__)


def test_fxg_linknormalformat_constructor_args():
    sig = inspect.signature(fxg_linkNormalFormat.__init__)
    params = list(sig.parameters.keys())



def test_fxg_div_is_not_abstract():
    assert not inspect.isabstract(fxg_div)


def test_fxg_div_constructor_exists():
    assert callable(fxg_div.__init__)


def test_fxg_div_constructor_args():
    sig = inspect.signature(fxg_div.__init__)
    params = list(sig.parameters.keys())



def test_fxg_linkhoverformat_is_not_abstract():
    assert not inspect.isabstract(fxg_linkHoverFormat)


def test_fxg_linkhoverformat_constructor_exists():
    assert callable(fxg_linkHoverFormat.__init__)


def test_fxg_linkhoverformat_constructor_args():
    sig = inspect.signature(fxg_linkHoverFormat.__init__)
    params = list(sig.parameters.keys())



def test_fxg_tcy_is_not_abstract():
    assert not inspect.isabstract(fxg_tcy)


def test_fxg_tcy_constructor_exists():
    assert callable(fxg_tcy.__init__)


def test_fxg_tcy_constructor_args():
    sig = inspect.signature(fxg_tcy.__init__)
    params = list(sig.parameters.keys())



def test_fxg_richtextcontentcontainer_is_not_abstract():
    assert not inspect.isabstract(fxg_RichTextContentContainer)


def test_fxg_richtextcontentcontainer_constructor_exists():
    assert callable(fxg_RichTextContentContainer.__init__)


def test_fxg_richtextcontentcontainer_constructor_args():
    sig = inspect.signature(fxg_RichTextContentContainer.__init__)
    params = list(sig.parameters.keys())



def test_fxg_richtextcontent_is_not_abstract():
    assert not inspect.isabstract(fxg_RichTextContent)


def test_fxg_richtextcontent_constructor_exists():
    assert callable(fxg_RichTextContent.__init__)


def test_fxg_richtextcontent_constructor_args():
    sig = inspect.signature(fxg_RichTextContent.__init__)
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



def test_fxg_p_is_not_abstract():
    assert not inspect.isabstract(fxg_p)


def test_fxg_p_constructor_exists():
    assert callable(fxg_p.__init__)


def test_fxg_p_constructor_args():
    sig = inspect.signature(fxg_p.__init__)
    params = list(sig.parameters.keys())



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_fxg_line_is_not_abstract():
    assert not inspect.isabstract(fxg_Line)


def test_fxg_line_constructor_exists():
    assert callable(fxg_Line.__init__)


def test_fxg_line_constructor_args():
    sig = inspect.signature(fxg_Line.__init__)
    params = list(sig.parameters.keys())
    assert "yFrom" in params, "Missing parameter 'yFrom'"
    assert "yTo" in params, "Missing parameter 'yTo'"
    assert "blendMode" in params, "Missing parameter 'blendMode'"
    assert "xTo" in params, "Missing parameter 'xTo'"
    assert "xFrom" in params, "Missing parameter 'xFrom'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "maskType" in params, "Missing parameter 'maskType'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "y" in params, "Missing parameter 'y'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "x" in params, "Missing parameter 'x'"
    assert "id" in params, "Missing parameter 'id'"

def test_fxg_line_has_yFrom():
    assert hasattr(fxg_Line, "yFrom")
    descriptor = None
    for klass in fxg_Line.__mro__:
        if "yFrom" in klass.__dict__:
            descriptor = klass.__dict__["yFrom"]
            break
    assert isinstance(descriptor, property)

def test_fxg_line_has_yTo():
    assert hasattr(fxg_Line, "yTo")
    descriptor = None
    for klass in fxg_Line.__mro__:
        if "yTo" in klass.__dict__:
            descriptor = klass.__dict__["yTo"]
            break
    assert isinstance(descriptor, property)

def test_fxg_line_has_blendMode():
    assert hasattr(fxg_Line, "blendMode")
    descriptor = None
    for klass in fxg_Line.__mro__:
        if "blendMode" in klass.__dict__:
            descriptor = klass.__dict__["blendMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg_line_has_xTo():
    assert hasattr(fxg_Line, "xTo")
    descriptor = None
    for klass in fxg_Line.__mro__:
        if "xTo" in klass.__dict__:
            descriptor = klass.__dict__["xTo"]
            break
    assert isinstance(descriptor, property)

def test_fxg_line_has_xFrom():
    assert hasattr(fxg_Line, "xFrom")
    descriptor = None
    for klass in fxg_Line.__mro__:
        if "xFrom" in klass.__dict__:
            descriptor = klass.__dict__["xFrom"]
            break
    assert isinstance(descriptor, property)

def test_fxg_line_has_alpha():
    assert hasattr(fxg_Line, "alpha")
    descriptor = None
    for klass in fxg_Line.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg_line_has_maskType():
    assert hasattr(fxg_Line, "maskType")
    descriptor = None
    for klass in fxg_Line.__mro__:
        if "maskType" in klass.__dict__:
            descriptor = klass.__dict__["maskType"]
            break
    assert isinstance(descriptor, property)

def test_fxg_line_has_visible():
    assert hasattr(fxg_Line, "visible")
    descriptor = None
    for klass in fxg_Line.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_fxg_line_has_y():
    assert hasattr(fxg_Line, "y")
    descriptor = None
    for klass in fxg_Line.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg_line_has_rotation():
    assert hasattr(fxg_Line, "rotation")
    descriptor = None
    for klass in fxg_Line.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg_line_has_scaleX():
    assert hasattr(fxg_Line, "scaleX")
    descriptor = None
    for klass in fxg_Line.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_line_has_scaleY():
    assert hasattr(fxg_Line, "scaleY")
    descriptor = None
    for klass in fxg_Line.__mro__:
        if "scaleY" in klass.__dict__:
            descriptor = klass.__dict__["scaleY"]
            break
    assert isinstance(descriptor, property)

def test_fxg_line_has_x():
    assert hasattr(fxg_Line, "x")
    descriptor = None
    for klass in fxg_Line.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fxg_line_has_id():
    assert hasattr(fxg_Line, "id")
    descriptor = None
    for klass in fxg_Line.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_fxg_ellipse_is_not_abstract():
    assert not inspect.isabstract(fxg_Ellipse)


def test_fxg_ellipse_constructor_exists():
    assert callable(fxg_Ellipse.__init__)


def test_fxg_ellipse_constructor_args():
    sig = inspect.signature(fxg_Ellipse.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "blendMode" in params, "Missing parameter 'blendMode'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "height" in params, "Missing parameter 'height'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"

def test_fxg_ellipse_has_width():
    assert hasattr(fxg_Ellipse, "width")
    descriptor = None
    for klass in fxg_Ellipse.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_fxg_ellipse_has_x():
    assert hasattr(fxg_Ellipse, "x")
    descriptor = None
    for klass in fxg_Ellipse.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fxg_ellipse_has_y():
    assert hasattr(fxg_Ellipse, "y")
    descriptor = None
    for klass in fxg_Ellipse.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg_ellipse_has_blendMode():
    assert hasattr(fxg_Ellipse, "blendMode")
    descriptor = None
    for klass in fxg_Ellipse.__mro__:
        if "blendMode" in klass.__dict__:
            descriptor = klass.__dict__["blendMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg_ellipse_has_alpha():
    assert hasattr(fxg_Ellipse, "alpha")
    descriptor = None
    for klass in fxg_Ellipse.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg_ellipse_has_rotation():
    assert hasattr(fxg_Ellipse, "rotation")
    descriptor = None
    for klass in fxg_Ellipse.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg_ellipse_has_scaleY():
    assert hasattr(fxg_Ellipse, "scaleY")
    descriptor = None
    for klass in fxg_Ellipse.__mro__:
        if "scaleY" in klass.__dict__:
            descriptor = klass.__dict__["scaleY"]
            break
    assert isinstance(descriptor, property)

def test_fxg_ellipse_has_visible():
    assert hasattr(fxg_Ellipse, "visible")
    descriptor = None
    for klass in fxg_Ellipse.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_fxg_ellipse_has_height():
    assert hasattr(fxg_Ellipse, "height")
    descriptor = None
    for klass in fxg_Ellipse.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_fxg_ellipse_has_scaleX():
    assert hasattr(fxg_Ellipse, "scaleX")
    descriptor = None
    for klass in fxg_Ellipse.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)



def test_fxg_rect_is_not_abstract():
    assert not inspect.isabstract(fxg_Rect)


def test_fxg_rect_constructor_exists():
    assert callable(fxg_Rect.__init__)


def test_fxg_rect_constructor_args():
    sig = inspect.signature(fxg_Rect.__init__)
    params = list(sig.parameters.keys())
    assert "radiusX" in params, "Missing parameter 'radiusX'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "blendMode" in params, "Missing parameter 'blendMode'"
    assert "topRightRadiusX" in params, "Missing parameter 'topRightRadiusX'"
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"
    assert "radiusY" in params, "Missing parameter 'radiusY'"
    assert "bottomLeftRadiusX" in params, "Missing parameter 'bottomLeftRadiusX'"
    assert "topLeftRadiusY" in params, "Missing parameter 'topLeftRadiusY'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "x" in params, "Missing parameter 'x'"
    assert "topLeftRadiusX" in params, "Missing parameter 'topLeftRadiusX'"
    assert "topRightRadiusY" in params, "Missing parameter 'topRightRadiusY'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "bottomRightRadiusX" in params, "Missing parameter 'bottomRightRadiusX'"
    assert "y" in params, "Missing parameter 'y'"
    assert "bottomRightRadiusY" in params, "Missing parameter 'bottomRightRadiusY'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "bottomLeftRadiusY" in params, "Missing parameter 'bottomLeftRadiusY'"

def test_fxg_rect_has_radiusX():
    assert hasattr(fxg_Rect, "radiusX")
    descriptor = None
    for klass in fxg_Rect.__mro__:
        if "radiusX" in klass.__dict__:
            descriptor = klass.__dict__["radiusX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_rect_has_rotation():
    assert hasattr(fxg_Rect, "rotation")
    descriptor = None
    for klass in fxg_Rect.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg_rect_has_blendMode():
    assert hasattr(fxg_Rect, "blendMode")
    descriptor = None
    for klass in fxg_Rect.__mro__:
        if "blendMode" in klass.__dict__:
            descriptor = klass.__dict__["blendMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg_rect_has_topRightRadiusX():
    assert hasattr(fxg_Rect, "topRightRadiusX")
    descriptor = None
    for klass in fxg_Rect.__mro__:
        if "topRightRadiusX" in klass.__dict__:
            descriptor = klass.__dict__["topRightRadiusX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_rect_has_height():
    assert hasattr(fxg_Rect, "height")
    descriptor = None
    for klass in fxg_Rect.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_fxg_rect_has_width():
    assert hasattr(fxg_Rect, "width")
    descriptor = None
    for klass in fxg_Rect.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_fxg_rect_has_radiusY():
    assert hasattr(fxg_Rect, "radiusY")
    descriptor = None
    for klass in fxg_Rect.__mro__:
        if "radiusY" in klass.__dict__:
            descriptor = klass.__dict__["radiusY"]
            break
    assert isinstance(descriptor, property)

def test_fxg_rect_has_bottomLeftRadiusX():
    assert hasattr(fxg_Rect, "bottomLeftRadiusX")
    descriptor = None
    for klass in fxg_Rect.__mro__:
        if "bottomLeftRadiusX" in klass.__dict__:
            descriptor = klass.__dict__["bottomLeftRadiusX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_rect_has_topLeftRadiusY():
    assert hasattr(fxg_Rect, "topLeftRadiusY")
    descriptor = None
    for klass in fxg_Rect.__mro__:
        if "topLeftRadiusY" in klass.__dict__:
            descriptor = klass.__dict__["topLeftRadiusY"]
            break
    assert isinstance(descriptor, property)

def test_fxg_rect_has_scaleY():
    assert hasattr(fxg_Rect, "scaleY")
    descriptor = None
    for klass in fxg_Rect.__mro__:
        if "scaleY" in klass.__dict__:
            descriptor = klass.__dict__["scaleY"]
            break
    assert isinstance(descriptor, property)

def test_fxg_rect_has_x():
    assert hasattr(fxg_Rect, "x")
    descriptor = None
    for klass in fxg_Rect.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fxg_rect_has_topLeftRadiusX():
    assert hasattr(fxg_Rect, "topLeftRadiusX")
    descriptor = None
    for klass in fxg_Rect.__mro__:
        if "topLeftRadiusX" in klass.__dict__:
            descriptor = klass.__dict__["topLeftRadiusX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_rect_has_topRightRadiusY():
    assert hasattr(fxg_Rect, "topRightRadiusY")
    descriptor = None
    for klass in fxg_Rect.__mro__:
        if "topRightRadiusY" in klass.__dict__:
            descriptor = klass.__dict__["topRightRadiusY"]
            break
    assert isinstance(descriptor, property)

def test_fxg_rect_has_alpha():
    assert hasattr(fxg_Rect, "alpha")
    descriptor = None
    for klass in fxg_Rect.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg_rect_has_bottomRightRadiusX():
    assert hasattr(fxg_Rect, "bottomRightRadiusX")
    descriptor = None
    for klass in fxg_Rect.__mro__:
        if "bottomRightRadiusX" in klass.__dict__:
            descriptor = klass.__dict__["bottomRightRadiusX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_rect_has_y():
    assert hasattr(fxg_Rect, "y")
    descriptor = None
    for klass in fxg_Rect.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg_rect_has_bottomRightRadiusY():
    assert hasattr(fxg_Rect, "bottomRightRadiusY")
    descriptor = None
    for klass in fxg_Rect.__mro__:
        if "bottomRightRadiusY" in klass.__dict__:
            descriptor = klass.__dict__["bottomRightRadiusY"]
            break
    assert isinstance(descriptor, property)

def test_fxg_rect_has_visible():
    assert hasattr(fxg_Rect, "visible")
    descriptor = None
    for klass in fxg_Rect.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_fxg_rect_has_scaleX():
    assert hasattr(fxg_Rect, "scaleX")
    descriptor = None
    for klass in fxg_Rect.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_rect_has_bottomLeftRadiusY():
    assert hasattr(fxg_Rect, "bottomLeftRadiusY")
    descriptor = None
    for klass in fxg_Rect.__mro__:
        if "bottomLeftRadiusY" in klass.__dict__:
            descriptor = klass.__dict__["bottomLeftRadiusY"]
            break
    assert isinstance(descriptor, property)



def test_fxg_definition_is_not_abstract():
    assert not inspect.isabstract(fxg_Definition)


def test_fxg_definition_constructor_exists():
    assert callable(fxg_Definition.__init__)


def test_fxg_definition_constructor_args():
    sig = inspect.signature(fxg_Definition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fxg_definition_has_name():
    assert hasattr(fxg_Definition, "name")
    descriptor = None
    for klass in fxg_Definition.__mro__:
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



def test_fxg_placeobject_is_not_abstract():
    assert not inspect.isabstract(fxg_PlaceObject)


def test_fxg_placeobject_constructor_exists():
    assert callable(fxg_PlaceObject.__init__)


def test_fxg_placeobject_constructor_args():
    sig = inspect.signature(fxg_PlaceObject.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_fxg_placeobject_has_id():
    assert hasattr(fxg_PlaceObject, "id")
    descriptor = None
    for klass in fxg_PlaceObject.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_fxg_fill_is_not_abstract():
    assert not inspect.isabstract(fxg_Fill)


def test_fxg_fill_constructor_exists():
    assert callable(fxg_Fill.__init__)


def test_fxg_fill_constructor_args():
    sig = inspect.signature(fxg_Fill.__init__)
    params = list(sig.parameters.keys())



def test_fxg_path_is_not_abstract():
    assert not inspect.isabstract(fxg_Path)


def test_fxg_path_constructor_exists():
    assert callable(fxg_Path.__init__)


def test_fxg_path_constructor_args():
    sig = inspect.signature(fxg_Path.__init__)
    params = list(sig.parameters.keys())
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "x" in params, "Missing parameter 'x'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "winding" in params, "Missing parameter 'winding'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "y" in params, "Missing parameter 'y'"
    assert "data" in params, "Missing parameter 'data'"
    assert "blendMode" in params, "Missing parameter 'blendMode'"
    assert "visible" in params, "Missing parameter 'visible'"

def test_fxg_path_has_alpha():
    assert hasattr(fxg_Path, "alpha")
    descriptor = None
    for klass in fxg_Path.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg_path_has_scaleY():
    assert hasattr(fxg_Path, "scaleY")
    descriptor = None
    for klass in fxg_Path.__mro__:
        if "scaleY" in klass.__dict__:
            descriptor = klass.__dict__["scaleY"]
            break
    assert isinstance(descriptor, property)

def test_fxg_path_has_x():
    assert hasattr(fxg_Path, "x")
    descriptor = None
    for klass in fxg_Path.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fxg_path_has_scaleX():
    assert hasattr(fxg_Path, "scaleX")
    descriptor = None
    for klass in fxg_Path.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_path_has_winding():
    assert hasattr(fxg_Path, "winding")
    descriptor = None
    for klass in fxg_Path.__mro__:
        if "winding" in klass.__dict__:
            descriptor = klass.__dict__["winding"]
            break
    assert isinstance(descriptor, property)

def test_fxg_path_has_rotation():
    assert hasattr(fxg_Path, "rotation")
    descriptor = None
    for klass in fxg_Path.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg_path_has_y():
    assert hasattr(fxg_Path, "y")
    descriptor = None
    for klass in fxg_Path.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg_path_has_data():
    assert hasattr(fxg_Path, "data")
    descriptor = None
    for klass in fxg_Path.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)

def test_fxg_path_has_blendMode():
    assert hasattr(fxg_Path, "blendMode")
    descriptor = None
    for klass in fxg_Path.__mro__:
        if "blendMode" in klass.__dict__:
            descriptor = klass.__dict__["blendMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg_path_has_visible():
    assert hasattr(fxg_Path, "visible")
    descriptor = None
    for klass in fxg_Path.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)



def test_fxg_containerelement_is_not_abstract():
    assert not inspect.isabstract(fxg_ContainerElement)


def test_fxg_containerelement_constructor_exists():
    assert callable(fxg_ContainerElement.__init__)


def test_fxg_containerelement_constructor_args():
    sig = inspect.signature(fxg_ContainerElement.__init__)
    params = list(sig.parameters.keys())



def test_fxg_gradiententry_is_not_abstract():
    assert not inspect.isabstract(fxg_GradientEntry)


def test_fxg_gradiententry_constructor_exists():
    assert callable(fxg_GradientEntry.__init__)


def test_fxg_gradiententry_constructor_args():
    sig = inspect.signature(fxg_GradientEntry.__init__)
    params = list(sig.parameters.keys())
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "ratio" in params, "Missing parameter 'ratio'"
    assert "color" in params, "Missing parameter 'color'"

def test_fxg_gradiententry_has_alpha():
    assert hasattr(fxg_GradientEntry, "alpha")
    descriptor = None
    for klass in fxg_GradientEntry.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg_gradiententry_has_ratio():
    assert hasattr(fxg_GradientEntry, "ratio")
    descriptor = None
    for klass in fxg_GradientEntry.__mro__:
        if "ratio" in klass.__dict__:
            descriptor = klass.__dict__["ratio"]
            break
    assert isinstance(descriptor, property)

def test_fxg_gradiententry_has_color():
    assert hasattr(fxg_GradientEntry, "color")
    descriptor = None
    for klass in fxg_GradientEntry.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_fxg_bitmapimage_is_not_abstract():
    assert not inspect.isabstract(fxg_BitmapImage)


def test_fxg_bitmapimage_constructor_exists():
    assert callable(fxg_BitmapImage.__init__)


def test_fxg_bitmapimage_constructor_args():
    sig = inspect.signature(fxg_BitmapImage.__init__)
    params = list(sig.parameters.keys())
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "source" in params, "Missing parameter 'source'"
    assert "height" in params, "Missing parameter 'height'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "width" in params, "Missing parameter 'width'"
    assert "blendMode" in params, "Missing parameter 'blendMode'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "fillMode" in params, "Missing parameter 'fillMode'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "visible" in params, "Missing parameter 'visible'"

def test_fxg_bitmapimage_has_rotation():
    assert hasattr(fxg_BitmapImage, "rotation")
    descriptor = None
    for klass in fxg_BitmapImage.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bitmapimage_has_source():
    assert hasattr(fxg_BitmapImage, "source")
    descriptor = None
    for klass in fxg_BitmapImage.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bitmapimage_has_height():
    assert hasattr(fxg_BitmapImage, "height")
    descriptor = None
    for klass in fxg_BitmapImage.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bitmapimage_has_x():
    assert hasattr(fxg_BitmapImage, "x")
    descriptor = None
    for klass in fxg_BitmapImage.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bitmapimage_has_y():
    assert hasattr(fxg_BitmapImage, "y")
    descriptor = None
    for klass in fxg_BitmapImage.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bitmapimage_has_width():
    assert hasattr(fxg_BitmapImage, "width")
    descriptor = None
    for klass in fxg_BitmapImage.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bitmapimage_has_blendMode():
    assert hasattr(fxg_BitmapImage, "blendMode")
    descriptor = None
    for klass in fxg_BitmapImage.__mro__:
        if "blendMode" in klass.__dict__:
            descriptor = klass.__dict__["blendMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bitmapimage_has_scaleY():
    assert hasattr(fxg_BitmapImage, "scaleY")
    descriptor = None
    for klass in fxg_BitmapImage.__mro__:
        if "scaleY" in klass.__dict__:
            descriptor = klass.__dict__["scaleY"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bitmapimage_has_alpha():
    assert hasattr(fxg_BitmapImage, "alpha")
    descriptor = None
    for klass in fxg_BitmapImage.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bitmapimage_has_fillMode():
    assert hasattr(fxg_BitmapImage, "fillMode")
    descriptor = None
    for klass in fxg_BitmapImage.__mro__:
        if "fillMode" in klass.__dict__:
            descriptor = klass.__dict__["fillMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bitmapimage_has_scaleX():
    assert hasattr(fxg_BitmapImage, "scaleX")
    descriptor = None
    for klass in fxg_BitmapImage.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_bitmapimage_has_visible():
    assert hasattr(fxg_BitmapImage, "visible")
    descriptor = None
    for klass in fxg_BitmapImage.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)



def test_fxg_richtext_is_not_abstract():
    assert not inspect.isabstract(fxg_RichText)


def test_fxg_richtext_constructor_exists():
    assert callable(fxg_RichText.__init__)


def test_fxg_richtext_constructor_args():
    sig = inspect.signature(fxg_RichText.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "x" in params, "Missing parameter 'x'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"
    assert "_tempcontent" in params, "Missing parameter '_tempcontent'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "id" in params, "Missing parameter 'id'"
    assert "y" in params, "Missing parameter 'y'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "maskType" in params, "Missing parameter 'maskType'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "blendMode" in params, "Missing parameter 'blendMode'"
    assert "height" in params, "Missing parameter 'height'"

def test_fxg_richtext_has_width():
    assert hasattr(fxg_RichText, "width")
    descriptor = None
    for klass in fxg_RichText.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_fxg_richtext_has_alpha():
    assert hasattr(fxg_RichText, "alpha")
    descriptor = None
    for klass in fxg_RichText.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg_richtext_has_x():
    assert hasattr(fxg_RichText, "x")
    descriptor = None
    for klass in fxg_RichText.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fxg_richtext_has_scaleY():
    assert hasattr(fxg_RichText, "scaleY")
    descriptor = None
    for klass in fxg_RichText.__mro__:
        if "scaleY" in klass.__dict__:
            descriptor = klass.__dict__["scaleY"]
            break
    assert isinstance(descriptor, property)

def test_fxg_richtext_has__tempcontent():
    assert hasattr(fxg_RichText, "_tempcontent")
    descriptor = None
    for klass in fxg_RichText.__mro__:
        if "_tempcontent" in klass.__dict__:
            descriptor = klass.__dict__["_tempcontent"]
            break
    assert isinstance(descriptor, property)

def test_fxg_richtext_has_rotation():
    assert hasattr(fxg_RichText, "rotation")
    descriptor = None
    for klass in fxg_RichText.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg_richtext_has_id():
    assert hasattr(fxg_RichText, "id")
    descriptor = None
    for klass in fxg_RichText.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_fxg_richtext_has_y():
    assert hasattr(fxg_RichText, "y")
    descriptor = None
    for klass in fxg_RichText.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg_richtext_has_visible():
    assert hasattr(fxg_RichText, "visible")
    descriptor = None
    for klass in fxg_RichText.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_fxg_richtext_has_maskType():
    assert hasattr(fxg_RichText, "maskType")
    descriptor = None
    for klass in fxg_RichText.__mro__:
        if "maskType" in klass.__dict__:
            descriptor = klass.__dict__["maskType"]
            break
    assert isinstance(descriptor, property)

def test_fxg_richtext_has_scaleX():
    assert hasattr(fxg_RichText, "scaleX")
    descriptor = None
    for klass in fxg_RichText.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_richtext_has_blendMode():
    assert hasattr(fxg_RichText, "blendMode")
    descriptor = None
    for klass in fxg_RichText.__mro__:
        if "blendMode" in klass.__dict__:
            descriptor = klass.__dict__["blendMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg_richtext_has_height():
    assert hasattr(fxg_RichText, "height")
    descriptor = None
    for klass in fxg_RichText.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_fxg_filter_is_not_abstract():
    assert not inspect.isabstract(fxg_Filter)


def test_fxg_filter_constructor_exists():
    assert callable(fxg_Filter.__init__)


def test_fxg_filter_constructor_args():
    sig = inspect.signature(fxg_Filter.__init__)
    params = list(sig.parameters.keys())



def test_fxg_shape_is_not_abstract():
    assert not inspect.isabstract(fxg_Shape)


def test_fxg_shape_constructor_exists():
    assert callable(fxg_Shape.__init__)


def test_fxg_shape_constructor_args():
    sig = inspect.signature(fxg_Shape.__init__)
    params = list(sig.parameters.keys())



def test_fxg_stroke_is_not_abstract():
    assert not inspect.isabstract(fxg_Stroke)


def test_fxg_stroke_constructor_exists():
    assert callable(fxg_Stroke.__init__)


def test_fxg_stroke_constructor_args():
    sig = inspect.signature(fxg_Stroke.__init__)
    params = list(sig.parameters.keys())



def test_fxg_transform_is_not_abstract():
    assert not inspect.isabstract(fxg_Transform)


def test_fxg_transform_constructor_exists():
    assert callable(fxg_Transform.__init__)


def test_fxg_transform_constructor_args():
    sig = inspect.signature(fxg_Transform.__init__)
    params = list(sig.parameters.keys())



def test_fxg_private_is_not_abstract():
    assert not inspect.isabstract(fxg_Private)


def test_fxg_private_constructor_exists():
    assert callable(fxg_Private.__init__)


def test_fxg_private_constructor_args():
    sig = inspect.signature(fxg_Private.__init__)
    params = list(sig.parameters.keys())



def test_fxg_library_is_not_abstract():
    assert not inspect.isabstract(fxg_Library)


def test_fxg_library_constructor_exists():
    assert callable(fxg_Library.__init__)


def test_fxg_library_constructor_args():
    sig = inspect.signature(fxg_Library.__init__)
    params = list(sig.parameters.keys())



def test_fxg_group_is_not_abstract():
    assert not inspect.isabstract(fxg_Group)


def test_fxg_group_constructor_exists():
    assert callable(fxg_Group.__init__)


def test_fxg_group_constructor_args():
    sig = inspect.signature(fxg_Group.__init__)
    params = list(sig.parameters.keys())
    assert "scaleGridLeft" in params, "Missing parameter 'scaleGridLeft'"
    assert "y" in params, "Missing parameter 'y'"
    assert "scaleGridRight" in params, "Missing parameter 'scaleGridRight'"
    assert "blendMode" in params, "Missing parameter 'blendMode'"
    assert "x" in params, "Missing parameter 'x'"
    assert "transformY" in params, "Missing parameter 'transformY'"
    assert "transformX" in params, "Missing parameter 'transformX'"
    assert "scaleGridTop" in params, "Missing parameter 'scaleGridTop'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "maskType" in params, "Missing parameter 'maskType'"
    assert "id" in params, "Missing parameter 'id'"
    assert "scaleGridBottom" in params, "Missing parameter 'scaleGridBottom'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "scaleX" in params, "Missing parameter 'scaleX'"
    assert "scaleY" in params, "Missing parameter 'scaleY'"

def test_fxg_group_has_scaleGridLeft():
    assert hasattr(fxg_Group, "scaleGridLeft")
    descriptor = None
    for klass in fxg_Group.__mro__:
        if "scaleGridLeft" in klass.__dict__:
            descriptor = klass.__dict__["scaleGridLeft"]
            break
    assert isinstance(descriptor, property)

def test_fxg_group_has_y():
    assert hasattr(fxg_Group, "y")
    descriptor = None
    for klass in fxg_Group.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fxg_group_has_scaleGridRight():
    assert hasattr(fxg_Group, "scaleGridRight")
    descriptor = None
    for klass in fxg_Group.__mro__:
        if "scaleGridRight" in klass.__dict__:
            descriptor = klass.__dict__["scaleGridRight"]
            break
    assert isinstance(descriptor, property)

def test_fxg_group_has_blendMode():
    assert hasattr(fxg_Group, "blendMode")
    descriptor = None
    for klass in fxg_Group.__mro__:
        if "blendMode" in klass.__dict__:
            descriptor = klass.__dict__["blendMode"]
            break
    assert isinstance(descriptor, property)

def test_fxg_group_has_x():
    assert hasattr(fxg_Group, "x")
    descriptor = None
    for klass in fxg_Group.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_fxg_group_has_transformY():
    assert hasattr(fxg_Group, "transformY")
    descriptor = None
    for klass in fxg_Group.__mro__:
        if "transformY" in klass.__dict__:
            descriptor = klass.__dict__["transformY"]
            break
    assert isinstance(descriptor, property)

def test_fxg_group_has_transformX():
    assert hasattr(fxg_Group, "transformX")
    descriptor = None
    for klass in fxg_Group.__mro__:
        if "transformX" in klass.__dict__:
            descriptor = klass.__dict__["transformX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_group_has_scaleGridTop():
    assert hasattr(fxg_Group, "scaleGridTop")
    descriptor = None
    for klass in fxg_Group.__mro__:
        if "scaleGridTop" in klass.__dict__:
            descriptor = klass.__dict__["scaleGridTop"]
            break
    assert isinstance(descriptor, property)

def test_fxg_group_has_alpha():
    assert hasattr(fxg_Group, "alpha")
    descriptor = None
    for klass in fxg_Group.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_fxg_group_has_maskType():
    assert hasattr(fxg_Group, "maskType")
    descriptor = None
    for klass in fxg_Group.__mro__:
        if "maskType" in klass.__dict__:
            descriptor = klass.__dict__["maskType"]
            break
    assert isinstance(descriptor, property)

def test_fxg_group_has_id():
    assert hasattr(fxg_Group, "id")
    descriptor = None
    for klass in fxg_Group.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_fxg_group_has_scaleGridBottom():
    assert hasattr(fxg_Group, "scaleGridBottom")
    descriptor = None
    for klass in fxg_Group.__mro__:
        if "scaleGridBottom" in klass.__dict__:
            descriptor = klass.__dict__["scaleGridBottom"]
            break
    assert isinstance(descriptor, property)

def test_fxg_group_has_visible():
    assert hasattr(fxg_Group, "visible")
    descriptor = None
    for klass in fxg_Group.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_fxg_group_has_rotation():
    assert hasattr(fxg_Group, "rotation")
    descriptor = None
    for klass in fxg_Group.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_fxg_group_has_scaleX():
    assert hasattr(fxg_Group, "scaleX")
    descriptor = None
    for klass in fxg_Group.__mro__:
        if "scaleX" in klass.__dict__:
            descriptor = klass.__dict__["scaleX"]
            break
    assert isinstance(descriptor, property)

def test_fxg_group_has_scaleY():
    assert hasattr(fxg_Group, "scaleY")
    descriptor = None
    for klass in fxg_Group.__mro__:
        if "scaleY" in klass.__dict__:
            descriptor = klass.__dict__["scaleY"]
            break
    assert isinstance(descriptor, property)



def test_fxg_graphic_is_not_abstract():
    assert not inspect.isabstract(fxg_Graphic)


def test_fxg_graphic_constructor_exists():
    assert callable(fxg_Graphic.__init__)


def test_fxg_graphic_constructor_args():
    sig = inspect.signature(fxg_Graphic.__init__)
    params = list(sig.parameters.keys())
    assert "viewHeight" in params, "Missing parameter 'viewHeight'"
    assert "version" in params, "Missing parameter 'version'"
    assert "scaleGridRight" in params, "Missing parameter 'scaleGridRight'"
    assert "scaleGridTop" in params, "Missing parameter 'scaleGridTop'"
    assert "scaleGridBottom" in params, "Missing parameter 'scaleGridBottom'"
    assert "scaleGridLeft" in params, "Missing parameter 'scaleGridLeft'"
    assert "viewWidth" in params, "Missing parameter 'viewWidth'"

def test_fxg_graphic_has_viewHeight():
    assert hasattr(fxg_Graphic, "viewHeight")
    descriptor = None
    for klass in fxg_Graphic.__mro__:
        if "viewHeight" in klass.__dict__:
            descriptor = klass.__dict__["viewHeight"]
            break
    assert isinstance(descriptor, property)

def test_fxg_graphic_has_version():
    assert hasattr(fxg_Graphic, "version")
    descriptor = None
    for klass in fxg_Graphic.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_fxg_graphic_has_scaleGridRight():
    assert hasattr(fxg_Graphic, "scaleGridRight")
    descriptor = None
    for klass in fxg_Graphic.__mro__:
        if "scaleGridRight" in klass.__dict__:
            descriptor = klass.__dict__["scaleGridRight"]
            break
    assert isinstance(descriptor, property)

def test_fxg_graphic_has_scaleGridTop():
    assert hasattr(fxg_Graphic, "scaleGridTop")
    descriptor = None
    for klass in fxg_Graphic.__mro__:
        if "scaleGridTop" in klass.__dict__:
            descriptor = klass.__dict__["scaleGridTop"]
            break
    assert isinstance(descriptor, property)

def test_fxg_graphic_has_scaleGridBottom():
    assert hasattr(fxg_Graphic, "scaleGridBottom")
    descriptor = None
    for klass in fxg_Graphic.__mro__:
        if "scaleGridBottom" in klass.__dict__:
            descriptor = klass.__dict__["scaleGridBottom"]
            break
    assert isinstance(descriptor, property)

def test_fxg_graphic_has_scaleGridLeft():
    assert hasattr(fxg_Graphic, "scaleGridLeft")
    descriptor = None
    for klass in fxg_Graphic.__mro__:
        if "scaleGridLeft" in klass.__dict__:
            descriptor = klass.__dict__["scaleGridLeft"]
            break
    assert isinstance(descriptor, property)

def test_fxg_graphic_has_viewWidth():
    assert hasattr(fxg_Graphic, "viewWidth")
    descriptor = None
    for klass in fxg_Graphic.__mro__:
        if "viewWidth" in klass.__dict__:
            descriptor = klass.__dict__["viewWidth"]
            break
    assert isinstance(descriptor, property)



def test_fxg_colortransform_is_not_abstract():
    assert not inspect.isabstract(fxg_ColorTransform)


def test_fxg_colortransform_constructor_exists():
    assert callable(fxg_ColorTransform.__init__)


def test_fxg_colortransform_constructor_args():
    sig = inspect.signature(fxg_ColorTransform.__init__)
    params = list(sig.parameters.keys())
    assert "blueOffset" in params, "Missing parameter 'blueOffset'"
    assert "greenOffset" in params, "Missing parameter 'greenOffset'"
    assert "redOffset" in params, "Missing parameter 'redOffset'"
    assert "redMultiplier" in params, "Missing parameter 'redMultiplier'"
    assert "alphaMultiplier" in params, "Missing parameter 'alphaMultiplier'"
    assert "greenMultiplier" in params, "Missing parameter 'greenMultiplier'"
    assert "alphaOffset" in params, "Missing parameter 'alphaOffset'"
    assert "blueMultiplier" in params, "Missing parameter 'blueMultiplier'"

def test_fxg_colortransform_has_blueOffset():
    assert hasattr(fxg_ColorTransform, "blueOffset")
    descriptor = None
    for klass in fxg_ColorTransform.__mro__:
        if "blueOffset" in klass.__dict__:
            descriptor = klass.__dict__["blueOffset"]
            break
    assert isinstance(descriptor, property)

def test_fxg_colortransform_has_greenOffset():
    assert hasattr(fxg_ColorTransform, "greenOffset")
    descriptor = None
    for klass in fxg_ColorTransform.__mro__:
        if "greenOffset" in klass.__dict__:
            descriptor = klass.__dict__["greenOffset"]
            break
    assert isinstance(descriptor, property)

def test_fxg_colortransform_has_redOffset():
    assert hasattr(fxg_ColorTransform, "redOffset")
    descriptor = None
    for klass in fxg_ColorTransform.__mro__:
        if "redOffset" in klass.__dict__:
            descriptor = klass.__dict__["redOffset"]
            break
    assert isinstance(descriptor, property)

def test_fxg_colortransform_has_redMultiplier():
    assert hasattr(fxg_ColorTransform, "redMultiplier")
    descriptor = None
    for klass in fxg_ColorTransform.__mro__:
        if "redMultiplier" in klass.__dict__:
            descriptor = klass.__dict__["redMultiplier"]
            break
    assert isinstance(descriptor, property)

def test_fxg_colortransform_has_alphaMultiplier():
    assert hasattr(fxg_ColorTransform, "alphaMultiplier")
    descriptor = None
    for klass in fxg_ColorTransform.__mro__:
        if "alphaMultiplier" in klass.__dict__:
            descriptor = klass.__dict__["alphaMultiplier"]
            break
    assert isinstance(descriptor, property)

def test_fxg_colortransform_has_greenMultiplier():
    assert hasattr(fxg_ColorTransform, "greenMultiplier")
    descriptor = None
    for klass in fxg_ColorTransform.__mro__:
        if "greenMultiplier" in klass.__dict__:
            descriptor = klass.__dict__["greenMultiplier"]
            break
    assert isinstance(descriptor, property)

def test_fxg_colortransform_has_alphaOffset():
    assert hasattr(fxg_ColorTransform, "alphaOffset")
    descriptor = None
    for klass in fxg_ColorTransform.__mro__:
        if "alphaOffset" in klass.__dict__:
            descriptor = klass.__dict__["alphaOffset"]
            break
    assert isinstance(descriptor, property)

def test_fxg_colortransform_has_blueMultiplier():
    assert hasattr(fxg_ColorTransform, "blueMultiplier")
    descriptor = None
    for klass in fxg_ColorTransform.__mro__:
        if "blueMultiplier" in klass.__dict__:
            descriptor = klass.__dict__["blueMultiplier"]
            break
    assert isinstance(descriptor, property)



def test_fxg_matrix_is_not_abstract():
    assert not inspect.isabstract(fxg_Matrix)


def test_fxg_matrix_constructor_exists():
    assert callable(fxg_Matrix.__init__)


def test_fxg_matrix_constructor_args():
    sig = inspect.signature(fxg_Matrix.__init__)
    params = list(sig.parameters.keys())
    assert "d" in params, "Missing parameter 'd'"
    assert "c" in params, "Missing parameter 'c'"
    assert "ty" in params, "Missing parameter 'ty'"
    assert "a" in params, "Missing parameter 'a'"
    assert "b" in params, "Missing parameter 'b'"
    assert "tx" in params, "Missing parameter 'tx'"

def test_fxg_matrix_has_d():
    assert hasattr(fxg_Matrix, "d")
    descriptor = None
    for klass in fxg_Matrix.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
            break
    assert isinstance(descriptor, property)

def test_fxg_matrix_has_c():
    assert hasattr(fxg_Matrix, "c")
    descriptor = None
    for klass in fxg_Matrix.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)

def test_fxg_matrix_has_ty():
    assert hasattr(fxg_Matrix, "ty")
    descriptor = None
    for klass in fxg_Matrix.__mro__:
        if "ty" in klass.__dict__:
            descriptor = klass.__dict__["ty"]
            break
    assert isinstance(descriptor, property)

def test_fxg_matrix_has_a():
    assert hasattr(fxg_Matrix, "a")
    descriptor = None
    for klass in fxg_Matrix.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)

def test_fxg_matrix_has_b():
    assert hasattr(fxg_Matrix, "b")
    descriptor = None
    for klass in fxg_Matrix.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_fxg_matrix_has_tx():
    assert hasattr(fxg_Matrix, "tx")
    descriptor = None
    for klass in fxg_Matrix.__mro__:
        if "tx" in klass.__dict__:
            descriptor = klass.__dict__["tx"]
            break
    assert isinstance(descriptor, property)

def test_typographiccase_exists():
    # Check that the Enumeration exists
    assert TypographicCase is not None

def test_typographiccase_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypographicCase]
    expected_literals = [
        "capsToSmallCaps",
        "default",
        "lowercase",
        "uppercase",
        "lowercaseToSmallCaps",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypographicCase"

def test_fillmode_exists():
    # Check that the Enumeration exists
    assert FillMode is not None

def test_fillmode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FillMode]
    expected_literals = [
        "REPEAT",
        "CLIP",
        "SCALE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FillMode"

def test_justificationrule_exists():
    # Check that the Enumeration exists
    assert JustificationRule is not None

def test_justificationrule_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JustificationRule]
    expected_literals = [
        "space",
        "eastAsian",
        "auto",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JustificationRule"

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

def test_breakopportunity_exists():
    # Check that the Enumeration exists
    assert BreakOpportunity is not None

def test_breakopportunity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BreakOpportunity]
    expected_literals = [
        "all",
        "any",
        "auto",
        "none",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BreakOpportunity"

def test_spreadmethod_exists():
    # Check that the Enumeration exists
    assert SpreadMethod is not None

def test_spreadmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SpreadMethod]
    expected_literals = [
        "pad",
        "repeat",
        "reflect",
        "NOT_SET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SpreadMethod"

def test_textrotation_exists():
    # Check that the Enumeration exists
    assert TextRotation is not None

def test_textrotation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextRotation]
    expected_literals = [
        "auto",
        "rotate270",
        "rotate180",
        "rotate90",
        "rotate0",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextRotation"

def test_joint_exists():
    # Check that the Enumeration exists
    assert Joint is not None

def test_joint_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Joint]
    expected_literals = [
        "BEVEL",
        "ROUND",
        "MITER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Joint"

def test_blockprogression_exists():
    # Check that the Enumeration exists
    assert BlockProgression is not None

def test_blockprogression_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BlockProgression]
    expected_literals = [
        "rl",
        "tb",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BlockProgression"

def test_whitespacecollapse_exists():
    # Check that the Enumeration exists
    assert WhitespaceCollapse is not None

def test_whitespacecollapse_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WhitespaceCollapse]
    expected_literals = [
        "COLLAPSE",
        "PRESERVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WhitespaceCollapse"

def test_bevelfiltertype_exists():
    # Check that the Enumeration exists
    assert BevelFilterType is not None

def test_bevelfiltertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BevelFilterType]
    expected_literals = [
        "INNER",
        "FULL",
        "OUTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BevelFilterType"

def test_interpolationmethod_exists():
    # Check that the Enumeration exists
    assert InterpolationMethod is not None

def test_interpolationmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InterpolationMethod]
    expected_literals = [
        "NOT_SET",
        "rgb",
        "linearRGB",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InterpolationMethod"

def test_digitcase_exists():
    # Check that the Enumeration exists
    assert DigitCase is not None

def test_digitcase_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DigitCase]
    expected_literals = [
        "lining",
        "oldStyle",
        "default",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DigitCase"

def test_leadingmodel_exists():
    # Check that the Enumeration exists
    assert LeadingModel is not None

def test_leadingmodel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LeadingModel]
    expected_literals = [
        "ideographicCenterUp",
        "ideographicTopDown",
        "romanUp",
        "ascentDescentUp",
        "ideographicCenterDown",
        "ideographicTopUp",
        "auto",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LeadingModel"

def test_cap_exists():
    # Check that the Enumeration exists
    assert Cap is not None

def test_cap_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Cap]
    expected_literals = [
        "SQUARE",
        "ROUND",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Cap"

def test_fontweight_exists():
    # Check that the Enumeration exists
    assert FontWeight is not None

def test_fontweight_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontWeight]
    expected_literals = [
        "NORMAL",
        "BOLD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontWeight"

def test_digitwidth_exists():
    # Check that the Enumeration exists
    assert DigitWidth is not None

def test_digitwidth_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DigitWidth]
    expected_literals = [
        "tabular",
        "default",
        "proportional",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DigitWidth"

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

def test_justificationstyle_exists():
    # Check that the Enumeration exists
    assert JustificationStyle is not None

def test_justificationstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JustificationStyle]
    expected_literals = [
        "pushInKinsoku",
        "auto",
        "prioritizeLeastAdjustment",
        "pushOutOnly",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JustificationStyle"

def test_textjustify_exists():
    # Check that the Enumeration exists
    assert TextJustify is not None

def test_textjustify_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextJustify]
    expected_literals = [
        "interWord",
        "distribute",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextJustify"

def test_alignmentbaseline_exists():
    # Check that the Enumeration exists
    assert AlignmentBaseline is not None

def test_alignmentbaseline_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AlignmentBaseline]
    expected_literals = [
        "auto",
        "useDominantBaseline",
        "ideographicCenter",
        "descent",
        "roman",
        "ascent",
        "ideographicTop",
        "ideographicBottom",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AlignmentBaseline"

def test_winding_exists():
    # Check that the Enumeration exists
    assert Winding is not None

def test_winding_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Winding]
    expected_literals = [
        "evenOdd",
        "NOT_SET",
        "nonZero",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Winding"

def test_dominantbaseline_exists():
    # Check that the Enumeration exists
    assert DominantBaseline is not None

def test_dominantbaseline_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DominantBaseline]
    expected_literals = [
        "auto",
        "ascent",
        "roman",
        "descent",
        "ideographicCenter",
        "ideographicBottom",
        "ideographicTop",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DominantBaseline"

def test_kerning_exists():
    # Check that the Enumeration exists
    assert Kerning is not None

def test_kerning_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Kerning]
    expected_literals = [
        "AUTO",
        "ON",
        "OFF",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Kerning"

def test_linebreak_exists():
    # Check that the Enumeration exists
    assert LineBreak is not None

def test_linebreak_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineBreak]
    expected_literals = [
        "explicit",
        "toFit",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineBreak"

def test_verticalalign_exists():
    # Check that the Enumeration exists
    assert VerticalAlign is not None

def test_verticalalign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VerticalAlign]
    expected_literals = [
        "inherit",
        "bottom",
        "top",
        "middle",
        "justify",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VerticalAlign"

def test_textalign_exists():
    # Check that the Enumeration exists
    assert TextAlign is not None

def test_textalign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextAlign]
    expected_literals = [
        "end",
        "start",
        "right",
        "left",
        "justify",
        "center",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextAlign"

def test_masktype_exists():
    # Check that the Enumeration exists
    assert MaskType is not None

def test_masktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MaskType]
    expected_literals = [
        "CLIP",
        "ALPHA",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MaskType"

def test_blendmode_exists():
    # Check that the Enumeration exists
    assert BlendMode is not None

def test_blendmode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BlendMode]
    expected_literals = [
        "screen",
        "alpha",
        "multiply",
        "normal",
        "darken",
        "erase",
        "hardlight",
        "shader",
        "subtract",
        "lighten",
        "layer",
        "difference",
        "overlay",
        "add",
        "invert",
        "NOT_SET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BlendMode"

def test_ligaturelevel_exists():
    # Check that the Enumeration exists
    assert LigatureLevel is not None

def test_ligaturelevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LigatureLevel]
    expected_literals = [
        "common",
        "exotic",
        "uncommon",
        "minimum",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LigatureLevel"

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
fxg_FXGElement_strategy = st.builds(
    fxg_FXGElement,
)
fxg_GradientBevelFilter_strategy = st.builds(
    fxg_GradientBevelFilter,
    type=
        safe_text,
    angle=
        safe_text,
    knockout=
        safe_text,
    strength=
        safe_text,
    blurX=
        safe_text,
    blurY=
        safe_text,
    distance=
        safe_text,
    quality=
        safe_text
)
fxg_GradientGlowFilter_strategy = st.builds(
    fxg_GradientGlowFilter,
    quality=
        safe_text,
    distance=
        safe_text,
    strength=
        safe_text,
    inner=
        safe_text,
    knockout=
        safe_text,
    blurX=
        safe_text,
    angle=
        safe_text,
    blurY=
        safe_text
)
Filter_strategy = st.builds(
    Filter,
)
fxg_BevelFilter_strategy = st.builds(
    fxg_BevelFilter,
    highlightColor=
        safe_text,
    distance=
        safe_text,
    shadowColor=
        safe_text,
    type=
        safe_text,
    blurY=
        safe_text,
    blurX=
        safe_text,
    quality=
        safe_text,
    knockout=
        safe_text,
    strength=
        safe_text,
    highlightAlpha=
        safe_text,
    angle=
        safe_text,
    shadowAlpha=
        safe_text
)
fxg_DropShadowFilter_strategy = st.builds(
    fxg_DropShadowFilter,
    hideObject=
        safe_text,
    color=
        safe_text,
    inner=
        safe_text,
    strength=
        safe_text,
    blurY=
        safe_text,
    alpha=
        safe_text,
    distance=
        safe_text,
    blurX=
        safe_text,
    angle=
        safe_text,
    quality=
        safe_text,
    knockout=
        safe_text
)
fxg_ColorMatrixFilter_strategy = st.builds(
    fxg_ColorMatrixFilter,
    matrix=
        safe_text
)
fxg_BlurFilter_strategy = st.builds(
    fxg_BlurFilter,
    blurY=
        safe_text,
    blurX=
        safe_text,
    quality=
        safe_text
)
fxg_LinearGradientStroke_strategy = st.builds(
    fxg_LinearGradientStroke,
    scaleX=
        safe_text,
    y=
        safe_text,
    weight=
        safe_text,
    miterLimit=
        safe_text,
    pixelHinting=
        safe_text,
    x=
        safe_text,
    interpolationMethod=
        safe_text,
    spreadMethod=
        safe_text,
    rotation=
        safe_text,
    scaleMode=
        safe_text,
    joints=
        safe_text,
    caps=
        safe_text
)
Stroke_strategy = st.builds(
    Stroke,
)
fxg_SolidColorStroke_strategy = st.builds(
    fxg_SolidColorStroke,
    weight=
        safe_text,
    alpha=
        safe_text,
    scaleMode=
        safe_text,
    joints=
        safe_text,
    miterLimit=
        safe_text,
    pixelHinting=
        safe_text,
    color=
        safe_text,
    caps=
        safe_text
)
fxg_RadialGradientStroke_strategy = st.builds(
    fxg_RadialGradientStroke,
    y=
        safe_text,
    weight=
        safe_text,
    focalPointRatio=
        safe_text,
    joints=
        safe_text,
    scaleMode=
        safe_text,
    pixelHinting=
        safe_text,
    interpolationMethod=
        safe_text,
    caps=
        safe_text,
    scaleX=
        safe_text,
    rotation=
        safe_text,
    miterLimit=
        safe_text,
    x=
        safe_text,
    spreadMethod=
        safe_text,
    scaleY=
        safe_text
)
fxg_RadialGradient_strategy = st.builds(
    fxg_RadialGradient,
    focalPointRatio=
        safe_text,
    x=
        safe_text,
    scaleY=
        safe_text,
    y=
        safe_text,
    rotation=
        safe_text,
    spreadMethod=
        safe_text,
    scaleX=
        safe_text,
    interpolationMethod=
        safe_text
)
fxg_LinearGradient_strategy = st.builds(
    fxg_LinearGradient,
    scaleX=
        safe_text,
    interpolationMethod=
        safe_text,
    x=
        safe_text,
    spreadMethod=
        safe_text,
    rotation=
        safe_text,
    y=
        safe_text
)
Fill_strategy = st.builds(
    Fill,
)
fxg_SolidColor_strategy = st.builds(
    fxg_SolidColor,
    color=
        safe_text,
    alpha=
        safe_text
)
fxg_linkActiveFormat_strategy = st.builds(
    fxg_linkActiveFormat,
)
RichTextContentContainer_strategy = st.builds(
    RichTextContentContainer,
)
fxg_BitmapFill_strategy = st.builds(
    fxg_BitmapFill,
    scaleX=
        safe_text,
    fillMode=
        safe_text,
    y=
        safe_text,
    source=
        safe_text,
    scaleY=
        safe_text,
    rotation=
        safe_text,
    x=
        safe_text
)
fxg_CharacterAttributes_strategy = st.builds(
    fxg_CharacterAttributes,
    backgroundAlpha=
        safe_text,
    breakOpportunity=
        safe_text,
    digitWidth=
        safe_text,
    textDecoration=
        safe_text,
    alignmentBaseline=
        safe_text,
    dominantBaseline=
        safe_text,
    color=
        safe_text,
    baselineShift=
        safe_text,
    fontStyle=
        safe_text,
    fontWeight=
        safe_text,
    fontSize=
        safe_text,
    fontFamily=
        safe_text,
    ligatureLevel=
        safe_text,
    lineHeight=
        safe_text,
    backgroundColor=
        safe_text,
    digitCase=
        safe_text,
    kerning=
        safe_text,
    trackingLeft=
        safe_text,
    locale=
        safe_text,
    textRotation=
        safe_text,
    textAlpha=
        safe_text,
    trackingRight=
        safe_text,
    whiteSpaceCollapse=
        safe_text,
    lineThrough=
        safe_text,
    typographicCase=
        safe_text
)
fxg_ContainerAttributes_strategy = st.builds(
    fxg_ContainerAttributes,
    paddingBottom=
        safe_text,
    paddingTop=
        safe_text,
    columnWidth=
        safe_text,
    blockProgression=
        safe_text,
    paddingLeft=
        safe_text,
    firstBaselineOffset=
        safe_text,
    verticalAlign=
        safe_text,
    paddingRight=
        safe_text,
    columnCount=
        safe_text,
    lineBreak=
        safe_text,
    columnGap=
        safe_text
)
fxg_ParagraphAttributes_strategy = st.builds(
    fxg_ParagraphAttributes,
    paragraphSpaceBefore=
        safe_text,
    textAlign=
        safe_text,
    paragraphSpaceAfter=
        safe_text,
    justificationStyle=
        safe_text,
    leadingModel=
        safe_text,
    textIndent=
        safe_text,
    tabStops=
        safe_text,
    textAlignLast=
        safe_text,
    paragraphEndIndent=
        safe_text,
    justificationRule=
        safe_text,
    paragraphStartIndent=
        safe_text,
    textJustify=
        safe_text
)
RichTextContent_strategy = st.builds(
    RichTextContent,
)
fxg_a_strategy = st.builds(
    fxg_a,
)
fxg_br_strategy = st.builds(
    fxg_br,
)
fxg_rawtext_strategy = st.builds(
    fxg_rawtext,
    _text=
        safe_text
)
fxg_tab_strategy = st.builds(
    fxg_tab,
)
fxg_img_strategy = st.builds(
    fxg_img,
)
fxg_span_strategy = st.builds(
    fxg_span,
)
fxg_linkNormalFormat_strategy = st.builds(
    fxg_linkNormalFormat,
)
fxg_div_strategy = st.builds(
    fxg_div,
)
fxg_linkHoverFormat_strategy = st.builds(
    fxg_linkHoverFormat,
)
fxg_tcy_strategy = st.builds(
    fxg_tcy,
)
fxg_RichTextContentContainer_strategy = st.builds(
    fxg_RichTextContentContainer,
)
fxg_RichTextContent_strategy = st.builds(
    fxg_RichTextContent,
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
fxg_p_strategy = st.builds(
    fxg_p,
)
Shape_strategy = st.builds(
    Shape,
)
fxg_Line_strategy = st.builds(
    fxg_Line,
    yFrom=
        safe_text,
    yTo=
        safe_text,
    blendMode=
        safe_text,
    xTo=
        safe_text,
    xFrom=
        safe_text,
    alpha=
        safe_text,
    maskType=
        safe_text,
    visible=
        safe_text,
    y=
        safe_text,
    rotation=
        safe_text,
    scaleX=
        safe_text,
    scaleY=
        safe_text,
    x=
        safe_text,
    id=
        safe_text
)
fxg_Ellipse_strategy = st.builds(
    fxg_Ellipse,
    width=
        safe_text,
    x=
        safe_text,
    y=
        safe_text,
    blendMode=
        safe_text,
    alpha=
        safe_text,
    rotation=
        safe_text,
    scaleY=
        safe_text,
    visible=
        safe_text,
    height=
        safe_text,
    scaleX=
        safe_text
)
fxg_Rect_strategy = st.builds(
    fxg_Rect,
    radiusX=
        safe_text,
    rotation=
        safe_text,
    blendMode=
        safe_text,
    topRightRadiusX=
        safe_text,
    height=
        safe_text,
    width=
        safe_text,
    radiusY=
        safe_text,
    bottomLeftRadiusX=
        safe_text,
    topLeftRadiusY=
        safe_text,
    scaleY=
        safe_text,
    x=
        safe_text,
    topLeftRadiusX=
        safe_text,
    topRightRadiusY=
        safe_text,
    alpha=
        safe_text,
    bottomRightRadiusX=
        safe_text,
    y=
        safe_text,
    bottomRightRadiusY=
        safe_text,
    visible=
        safe_text,
    scaleX=
        safe_text,
    bottomLeftRadiusY=
        safe_text
)
fxg_Definition_strategy = st.builds(
    fxg_Definition,
    name=
        safe_text
)
FXGElement_strategy = st.builds(
    FXGElement,
)
fxg_PlaceObject_strategy = st.builds(
    fxg_PlaceObject,
    id=
        safe_text
)
fxg_Fill_strategy = st.builds(
    fxg_Fill,
)
fxg_Path_strategy = st.builds(
    fxg_Path,
    alpha=
        safe_text,
    scaleY=
        safe_text,
    x=
        safe_text,
    scaleX=
        safe_text,
    winding=
        safe_text,
    rotation=
        safe_text,
    y=
        safe_text,
    data=
        safe_text,
    blendMode=
        safe_text,
    visible=
        safe_text
)
fxg_ContainerElement_strategy = st.builds(
    fxg_ContainerElement,
)
fxg_GradientEntry_strategy = st.builds(
    fxg_GradientEntry,
    alpha=
        safe_text,
    ratio=
        safe_text,
    color=
        safe_text
)
fxg_BitmapImage_strategy = st.builds(
    fxg_BitmapImage,
    rotation=
        safe_text,
    source=
        safe_text,
    height=
        safe_text,
    x=
        safe_text,
    y=
        safe_text,
    width=
        safe_text,
    blendMode=
        safe_text,
    scaleY=
        safe_text,
    alpha=
        safe_text,
    fillMode=
        safe_text,
    scaleX=
        safe_text,
    visible=
        safe_text
)
fxg_RichText_strategy = st.builds(
    fxg_RichText,
    width=
        safe_text,
    alpha=
        safe_text,
    x=
        safe_text,
    scaleY=
        safe_text,
    _tempcontent=
        safe_text,
    rotation=
        safe_text,
    id=
        safe_text,
    y=
        safe_text,
    visible=
        safe_text,
    maskType=
        safe_text,
    scaleX=
        safe_text,
    blendMode=
        safe_text,
    height=
        safe_text
)
fxg_Filter_strategy = st.builds(
    fxg_Filter,
)
fxg_Shape_strategy = st.builds(
    fxg_Shape,
)
fxg_Stroke_strategy = st.builds(
    fxg_Stroke,
)
fxg_Transform_strategy = st.builds(
    fxg_Transform,
)
fxg_Private_strategy = st.builds(
    fxg_Private,
)
fxg_Library_strategy = st.builds(
    fxg_Library,
)
fxg_Group_strategy = st.builds(
    fxg_Group,
    scaleGridLeft=
        safe_text,
    y=
        safe_text,
    scaleGridRight=
        safe_text,
    blendMode=
        safe_text,
    x=
        safe_text,
    transformY=
        safe_text,
    transformX=
        safe_text,
    scaleGridTop=
        safe_text,
    alpha=
        safe_text,
    maskType=
        safe_text,
    id=
        safe_text,
    scaleGridBottom=
        safe_text,
    visible=
        safe_text,
    rotation=
        safe_text,
    scaleX=
        safe_text,
    scaleY=
        safe_text
)
fxg_Graphic_strategy = st.builds(
    fxg_Graphic,
    viewHeight=
        st.integers(),
    version=
        safe_text,
    scaleGridRight=
        safe_text,
    scaleGridTop=
        safe_text,
    scaleGridBottom=
        safe_text,
    scaleGridLeft=
        safe_text,
    viewWidth=
        st.integers()
)
fxg_ColorTransform_strategy = st.builds(
    fxg_ColorTransform,
    blueOffset=
        safe_text,
    greenOffset=
        safe_text,
    redOffset=
        safe_text,
    redMultiplier=
        safe_text,
    alphaMultiplier=
        safe_text,
    greenMultiplier=
        safe_text,
    alphaOffset=
        safe_text,
    blueMultiplier=
        safe_text
)
fxg_Matrix_strategy = st.builds(
    fxg_Matrix,
    d=
        safe_text,
    c=
        safe_text,
    ty=
        safe_text,
    a=
        safe_text,
    b=
        safe_text,
    tx=
        safe_text
)

@given(instance=fxg_FXGElement_strategy)
@settings(max_examples=50)
def test_fxg_fxgelement_instantiation(instance):
    assert isinstance(instance, fxg_FXGElement)

@given(instance=fxg_GradientBevelFilter_strategy)
@settings(max_examples=50)
def test_fxg_gradientbevelfilter_instantiation(instance):
    assert isinstance(instance, fxg_GradientBevelFilter)



@given(instance=fxg_GradientBevelFilter_strategy)
def test_fxg_gradientbevelfilter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=fxg_GradientBevelFilter_strategy)
def test_fxg_gradientbevelfilter_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original



@given(instance=fxg_GradientBevelFilter_strategy)
def test_fxg_gradientbevelfilter_knockout_setter(instance):
    original = instance.knockout
    instance.knockout = original
    assert instance.knockout == original



@given(instance=fxg_GradientBevelFilter_strategy)
def test_fxg_gradientbevelfilter_strength_setter(instance):
    original = instance.strength
    instance.strength = original
    assert instance.strength == original



@given(instance=fxg_GradientBevelFilter_strategy)
def test_fxg_gradientbevelfilter_blurX_setter(instance):
    original = instance.blurX
    instance.blurX = original
    assert instance.blurX == original



@given(instance=fxg_GradientBevelFilter_strategy)
def test_fxg_gradientbevelfilter_blurY_setter(instance):
    original = instance.blurY
    instance.blurY = original
    assert instance.blurY == original



@given(instance=fxg_GradientBevelFilter_strategy)
def test_fxg_gradientbevelfilter_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original



@given(instance=fxg_GradientBevelFilter_strategy)
def test_fxg_gradientbevelfilter_quality_setter(instance):
    original = instance.quality
    instance.quality = original
    assert instance.quality == original

@given(instance=fxg_GradientGlowFilter_strategy)
@settings(max_examples=50)
def test_fxg_gradientglowfilter_instantiation(instance):
    assert isinstance(instance, fxg_GradientGlowFilter)



@given(instance=fxg_GradientGlowFilter_strategy)
def test_fxg_gradientglowfilter_quality_setter(instance):
    original = instance.quality
    instance.quality = original
    assert instance.quality == original



@given(instance=fxg_GradientGlowFilter_strategy)
def test_fxg_gradientglowfilter_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original



@given(instance=fxg_GradientGlowFilter_strategy)
def test_fxg_gradientglowfilter_strength_setter(instance):
    original = instance.strength
    instance.strength = original
    assert instance.strength == original



@given(instance=fxg_GradientGlowFilter_strategy)
def test_fxg_gradientglowfilter_inner_setter(instance):
    original = instance.inner
    instance.inner = original
    assert instance.inner == original



@given(instance=fxg_GradientGlowFilter_strategy)
def test_fxg_gradientglowfilter_knockout_setter(instance):
    original = instance.knockout
    instance.knockout = original
    assert instance.knockout == original



@given(instance=fxg_GradientGlowFilter_strategy)
def test_fxg_gradientglowfilter_blurX_setter(instance):
    original = instance.blurX
    instance.blurX = original
    assert instance.blurX == original



@given(instance=fxg_GradientGlowFilter_strategy)
def test_fxg_gradientglowfilter_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original



@given(instance=fxg_GradientGlowFilter_strategy)
def test_fxg_gradientglowfilter_blurY_setter(instance):
    original = instance.blurY
    instance.blurY = original
    assert instance.blurY == original

@given(instance=Filter_strategy)
@settings(max_examples=50)
def test_filter_instantiation(instance):
    assert isinstance(instance, Filter)

@given(instance=fxg_BevelFilter_strategy)
@settings(max_examples=50)
def test_fxg_bevelfilter_instantiation(instance):
    assert isinstance(instance, fxg_BevelFilter)



@given(instance=fxg_BevelFilter_strategy)
def test_fxg_bevelfilter_highlightColor_setter(instance):
    original = instance.highlightColor
    instance.highlightColor = original
    assert instance.highlightColor == original



@given(instance=fxg_BevelFilter_strategy)
def test_fxg_bevelfilter_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original



@given(instance=fxg_BevelFilter_strategy)
def test_fxg_bevelfilter_shadowColor_setter(instance):
    original = instance.shadowColor
    instance.shadowColor = original
    assert instance.shadowColor == original



@given(instance=fxg_BevelFilter_strategy)
def test_fxg_bevelfilter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=fxg_BevelFilter_strategy)
def test_fxg_bevelfilter_blurY_setter(instance):
    original = instance.blurY
    instance.blurY = original
    assert instance.blurY == original



@given(instance=fxg_BevelFilter_strategy)
def test_fxg_bevelfilter_blurX_setter(instance):
    original = instance.blurX
    instance.blurX = original
    assert instance.blurX == original



@given(instance=fxg_BevelFilter_strategy)
def test_fxg_bevelfilter_quality_setter(instance):
    original = instance.quality
    instance.quality = original
    assert instance.quality == original



@given(instance=fxg_BevelFilter_strategy)
def test_fxg_bevelfilter_knockout_setter(instance):
    original = instance.knockout
    instance.knockout = original
    assert instance.knockout == original



@given(instance=fxg_BevelFilter_strategy)
def test_fxg_bevelfilter_strength_setter(instance):
    original = instance.strength
    instance.strength = original
    assert instance.strength == original



@given(instance=fxg_BevelFilter_strategy)
def test_fxg_bevelfilter_highlightAlpha_setter(instance):
    original = instance.highlightAlpha
    instance.highlightAlpha = original
    assert instance.highlightAlpha == original



@given(instance=fxg_BevelFilter_strategy)
def test_fxg_bevelfilter_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original



@given(instance=fxg_BevelFilter_strategy)
def test_fxg_bevelfilter_shadowAlpha_setter(instance):
    original = instance.shadowAlpha
    instance.shadowAlpha = original
    assert instance.shadowAlpha == original

@given(instance=fxg_DropShadowFilter_strategy)
@settings(max_examples=50)
def test_fxg_dropshadowfilter_instantiation(instance):
    assert isinstance(instance, fxg_DropShadowFilter)



@given(instance=fxg_DropShadowFilter_strategy)
def test_fxg_dropshadowfilter_hideObject_setter(instance):
    original = instance.hideObject
    instance.hideObject = original
    assert instance.hideObject == original



@given(instance=fxg_DropShadowFilter_strategy)
def test_fxg_dropshadowfilter_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=fxg_DropShadowFilter_strategy)
def test_fxg_dropshadowfilter_inner_setter(instance):
    original = instance.inner
    instance.inner = original
    assert instance.inner == original



@given(instance=fxg_DropShadowFilter_strategy)
def test_fxg_dropshadowfilter_strength_setter(instance):
    original = instance.strength
    instance.strength = original
    assert instance.strength == original



@given(instance=fxg_DropShadowFilter_strategy)
def test_fxg_dropshadowfilter_blurY_setter(instance):
    original = instance.blurY
    instance.blurY = original
    assert instance.blurY == original



@given(instance=fxg_DropShadowFilter_strategy)
def test_fxg_dropshadowfilter_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=fxg_DropShadowFilter_strategy)
def test_fxg_dropshadowfilter_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original



@given(instance=fxg_DropShadowFilter_strategy)
def test_fxg_dropshadowfilter_blurX_setter(instance):
    original = instance.blurX
    instance.blurX = original
    assert instance.blurX == original



@given(instance=fxg_DropShadowFilter_strategy)
def test_fxg_dropshadowfilter_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original



@given(instance=fxg_DropShadowFilter_strategy)
def test_fxg_dropshadowfilter_quality_setter(instance):
    original = instance.quality
    instance.quality = original
    assert instance.quality == original



@given(instance=fxg_DropShadowFilter_strategy)
def test_fxg_dropshadowfilter_knockout_setter(instance):
    original = instance.knockout
    instance.knockout = original
    assert instance.knockout == original

@given(instance=fxg_ColorMatrixFilter_strategy)
@settings(max_examples=50)
def test_fxg_colormatrixfilter_instantiation(instance):
    assert isinstance(instance, fxg_ColorMatrixFilter)



@given(instance=fxg_ColorMatrixFilter_strategy)
def test_fxg_colormatrixfilter_matrix_setter(instance):
    original = instance.matrix
    instance.matrix = original
    assert instance.matrix == original

@given(instance=fxg_BlurFilter_strategy)
@settings(max_examples=50)
def test_fxg_blurfilter_instantiation(instance):
    assert isinstance(instance, fxg_BlurFilter)



@given(instance=fxg_BlurFilter_strategy)
def test_fxg_blurfilter_blurY_setter(instance):
    original = instance.blurY
    instance.blurY = original
    assert instance.blurY == original



@given(instance=fxg_BlurFilter_strategy)
def test_fxg_blurfilter_blurX_setter(instance):
    original = instance.blurX
    instance.blurX = original
    assert instance.blurX == original



@given(instance=fxg_BlurFilter_strategy)
def test_fxg_blurfilter_quality_setter(instance):
    original = instance.quality
    instance.quality = original
    assert instance.quality == original

@given(instance=fxg_LinearGradientStroke_strategy)
@settings(max_examples=50)
def test_fxg_lineargradientstroke_instantiation(instance):
    assert isinstance(instance, fxg_LinearGradientStroke)



@given(instance=fxg_LinearGradientStroke_strategy)
def test_fxg_lineargradientstroke_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_fxg_lineargradientstroke_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_fxg_lineargradientstroke_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_fxg_lineargradientstroke_miterLimit_setter(instance):
    original = instance.miterLimit
    instance.miterLimit = original
    assert instance.miterLimit == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_fxg_lineargradientstroke_pixelHinting_setter(instance):
    original = instance.pixelHinting
    instance.pixelHinting = original
    assert instance.pixelHinting == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_fxg_lineargradientstroke_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_fxg_lineargradientstroke_interpolationMethod_setter(instance):
    original = instance.interpolationMethod
    instance.interpolationMethod = original
    assert instance.interpolationMethod == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_fxg_lineargradientstroke_spreadMethod_setter(instance):
    original = instance.spreadMethod
    instance.spreadMethod = original
    assert instance.spreadMethod == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_fxg_lineargradientstroke_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_fxg_lineargradientstroke_scaleMode_setter(instance):
    original = instance.scaleMode
    instance.scaleMode = original
    assert instance.scaleMode == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_fxg_lineargradientstroke_joints_setter(instance):
    original = instance.joints
    instance.joints = original
    assert instance.joints == original



@given(instance=fxg_LinearGradientStroke_strategy)
def test_fxg_lineargradientstroke_caps_setter(instance):
    original = instance.caps
    instance.caps = original
    assert instance.caps == original

@given(instance=Stroke_strategy)
@settings(max_examples=50)
def test_stroke_instantiation(instance):
    assert isinstance(instance, Stroke)

@given(instance=fxg_SolidColorStroke_strategy)
@settings(max_examples=50)
def test_fxg_solidcolorstroke_instantiation(instance):
    assert isinstance(instance, fxg_SolidColorStroke)



@given(instance=fxg_SolidColorStroke_strategy)
def test_fxg_solidcolorstroke_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=fxg_SolidColorStroke_strategy)
def test_fxg_solidcolorstroke_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=fxg_SolidColorStroke_strategy)
def test_fxg_solidcolorstroke_scaleMode_setter(instance):
    original = instance.scaleMode
    instance.scaleMode = original
    assert instance.scaleMode == original



@given(instance=fxg_SolidColorStroke_strategy)
def test_fxg_solidcolorstroke_joints_setter(instance):
    original = instance.joints
    instance.joints = original
    assert instance.joints == original



@given(instance=fxg_SolidColorStroke_strategy)
def test_fxg_solidcolorstroke_miterLimit_setter(instance):
    original = instance.miterLimit
    instance.miterLimit = original
    assert instance.miterLimit == original



@given(instance=fxg_SolidColorStroke_strategy)
def test_fxg_solidcolorstroke_pixelHinting_setter(instance):
    original = instance.pixelHinting
    instance.pixelHinting = original
    assert instance.pixelHinting == original



@given(instance=fxg_SolidColorStroke_strategy)
def test_fxg_solidcolorstroke_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=fxg_SolidColorStroke_strategy)
def test_fxg_solidcolorstroke_caps_setter(instance):
    original = instance.caps
    instance.caps = original
    assert instance.caps == original

@given(instance=fxg_RadialGradientStroke_strategy)
@settings(max_examples=50)
def test_fxg_radialgradientstroke_instantiation(instance):
    assert isinstance(instance, fxg_RadialGradientStroke)



@given(instance=fxg_RadialGradientStroke_strategy)
def test_fxg_radialgradientstroke_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_fxg_radialgradientstroke_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_fxg_radialgradientstroke_focalPointRatio_setter(instance):
    original = instance.focalPointRatio
    instance.focalPointRatio = original
    assert instance.focalPointRatio == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_fxg_radialgradientstroke_joints_setter(instance):
    original = instance.joints
    instance.joints = original
    assert instance.joints == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_fxg_radialgradientstroke_scaleMode_setter(instance):
    original = instance.scaleMode
    instance.scaleMode = original
    assert instance.scaleMode == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_fxg_radialgradientstroke_pixelHinting_setter(instance):
    original = instance.pixelHinting
    instance.pixelHinting = original
    assert instance.pixelHinting == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_fxg_radialgradientstroke_interpolationMethod_setter(instance):
    original = instance.interpolationMethod
    instance.interpolationMethod = original
    assert instance.interpolationMethod == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_fxg_radialgradientstroke_caps_setter(instance):
    original = instance.caps
    instance.caps = original
    assert instance.caps == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_fxg_radialgradientstroke_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_fxg_radialgradientstroke_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_fxg_radialgradientstroke_miterLimit_setter(instance):
    original = instance.miterLimit
    instance.miterLimit = original
    assert instance.miterLimit == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_fxg_radialgradientstroke_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_fxg_radialgradientstroke_spreadMethod_setter(instance):
    original = instance.spreadMethod
    instance.spreadMethod = original
    assert instance.spreadMethod == original



@given(instance=fxg_RadialGradientStroke_strategy)
def test_fxg_radialgradientstroke_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original

@given(instance=fxg_RadialGradient_strategy)
@settings(max_examples=50)
def test_fxg_radialgradient_instantiation(instance):
    assert isinstance(instance, fxg_RadialGradient)



@given(instance=fxg_RadialGradient_strategy)
def test_fxg_radialgradient_focalPointRatio_setter(instance):
    original = instance.focalPointRatio
    instance.focalPointRatio = original
    assert instance.focalPointRatio == original



@given(instance=fxg_RadialGradient_strategy)
def test_fxg_radialgradient_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_RadialGradient_strategy)
def test_fxg_radialgradient_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original



@given(instance=fxg_RadialGradient_strategy)
def test_fxg_radialgradient_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_RadialGradient_strategy)
def test_fxg_radialgradient_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_RadialGradient_strategy)
def test_fxg_radialgradient_spreadMethod_setter(instance):
    original = instance.spreadMethod
    instance.spreadMethod = original
    assert instance.spreadMethod == original



@given(instance=fxg_RadialGradient_strategy)
def test_fxg_radialgradient_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_RadialGradient_strategy)
def test_fxg_radialgradient_interpolationMethod_setter(instance):
    original = instance.interpolationMethod
    instance.interpolationMethod = original
    assert instance.interpolationMethod == original

@given(instance=fxg_LinearGradient_strategy)
@settings(max_examples=50)
def test_fxg_lineargradient_instantiation(instance):
    assert isinstance(instance, fxg_LinearGradient)



@given(instance=fxg_LinearGradient_strategy)
def test_fxg_lineargradient_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_LinearGradient_strategy)
def test_fxg_lineargradient_interpolationMethod_setter(instance):
    original = instance.interpolationMethod
    instance.interpolationMethod = original
    assert instance.interpolationMethod == original



@given(instance=fxg_LinearGradient_strategy)
def test_fxg_lineargradient_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_LinearGradient_strategy)
def test_fxg_lineargradient_spreadMethod_setter(instance):
    original = instance.spreadMethod
    instance.spreadMethod = original
    assert instance.spreadMethod == original



@given(instance=fxg_LinearGradient_strategy)
def test_fxg_lineargradient_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_LinearGradient_strategy)
def test_fxg_lineargradient_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=Fill_strategy)
@settings(max_examples=50)
def test_fill_instantiation(instance):
    assert isinstance(instance, Fill)

@given(instance=fxg_SolidColor_strategy)
@settings(max_examples=50)
def test_fxg_solidcolor_instantiation(instance):
    assert isinstance(instance, fxg_SolidColor)



@given(instance=fxg_SolidColor_strategy)
def test_fxg_solidcolor_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=fxg_SolidColor_strategy)
def test_fxg_solidcolor_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original

@given(instance=fxg_linkActiveFormat_strategy)
@settings(max_examples=50)
def test_fxg_linkactiveformat_instantiation(instance):
    assert isinstance(instance, fxg_linkActiveFormat)

@given(instance=RichTextContentContainer_strategy)
@settings(max_examples=50)
def test_richtextcontentcontainer_instantiation(instance):
    assert isinstance(instance, RichTextContentContainer)

@given(instance=fxg_BitmapFill_strategy)
@settings(max_examples=50)
def test_fxg_bitmapfill_instantiation(instance):
    assert isinstance(instance, fxg_BitmapFill)



@given(instance=fxg_BitmapFill_strategy)
def test_fxg_bitmapfill_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_BitmapFill_strategy)
def test_fxg_bitmapfill_fillMode_setter(instance):
    original = instance.fillMode
    instance.fillMode = original
    assert instance.fillMode == original



@given(instance=fxg_BitmapFill_strategy)
def test_fxg_bitmapfill_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_BitmapFill_strategy)
def test_fxg_bitmapfill_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=fxg_BitmapFill_strategy)
def test_fxg_bitmapfill_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original



@given(instance=fxg_BitmapFill_strategy)
def test_fxg_bitmapfill_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_BitmapFill_strategy)
def test_fxg_bitmapfill_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=fxg_CharacterAttributes_strategy)
@settings(max_examples=50)
def test_fxg_characterattributes_instantiation(instance):
    assert isinstance(instance, fxg_CharacterAttributes)



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_backgroundAlpha_setter(instance):
    original = instance.backgroundAlpha
    instance.backgroundAlpha = original
    assert instance.backgroundAlpha == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_breakOpportunity_setter(instance):
    original = instance.breakOpportunity
    instance.breakOpportunity = original
    assert instance.breakOpportunity == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_digitWidth_setter(instance):
    original = instance.digitWidth
    instance.digitWidth = original
    assert instance.digitWidth == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_textDecoration_setter(instance):
    original = instance.textDecoration
    instance.textDecoration = original
    assert instance.textDecoration == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_alignmentBaseline_setter(instance):
    original = instance.alignmentBaseline
    instance.alignmentBaseline = original
    assert instance.alignmentBaseline == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_dominantBaseline_setter(instance):
    original = instance.dominantBaseline
    instance.dominantBaseline = original
    assert instance.dominantBaseline == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_baselineShift_setter(instance):
    original = instance.baselineShift
    instance.baselineShift = original
    assert instance.baselineShift == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_fontStyle_setter(instance):
    original = instance.fontStyle
    instance.fontStyle = original
    assert instance.fontStyle == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_fontWeight_setter(instance):
    original = instance.fontWeight
    instance.fontWeight = original
    assert instance.fontWeight == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_fontSize_setter(instance):
    original = instance.fontSize
    instance.fontSize = original
    assert instance.fontSize == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_fontFamily_setter(instance):
    original = instance.fontFamily
    instance.fontFamily = original
    assert instance.fontFamily == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_ligatureLevel_setter(instance):
    original = instance.ligatureLevel
    instance.ligatureLevel = original
    assert instance.ligatureLevel == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_lineHeight_setter(instance):
    original = instance.lineHeight
    instance.lineHeight = original
    assert instance.lineHeight == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_digitCase_setter(instance):
    original = instance.digitCase
    instance.digitCase = original
    assert instance.digitCase == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_kerning_setter(instance):
    original = instance.kerning
    instance.kerning = original
    assert instance.kerning == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_trackingLeft_setter(instance):
    original = instance.trackingLeft
    instance.trackingLeft = original
    assert instance.trackingLeft == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_locale_setter(instance):
    original = instance.locale
    instance.locale = original
    assert instance.locale == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_textRotation_setter(instance):
    original = instance.textRotation
    instance.textRotation = original
    assert instance.textRotation == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_textAlpha_setter(instance):
    original = instance.textAlpha
    instance.textAlpha = original
    assert instance.textAlpha == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_trackingRight_setter(instance):
    original = instance.trackingRight
    instance.trackingRight = original
    assert instance.trackingRight == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_whiteSpaceCollapse_setter(instance):
    original = instance.whiteSpaceCollapse
    instance.whiteSpaceCollapse = original
    assert instance.whiteSpaceCollapse == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_lineThrough_setter(instance):
    original = instance.lineThrough
    instance.lineThrough = original
    assert instance.lineThrough == original



@given(instance=fxg_CharacterAttributes_strategy)
def test_fxg_characterattributes_typographicCase_setter(instance):
    original = instance.typographicCase
    instance.typographicCase = original
    assert instance.typographicCase == original

@given(instance=fxg_ContainerAttributes_strategy)
@settings(max_examples=50)
def test_fxg_containerattributes_instantiation(instance):
    assert isinstance(instance, fxg_ContainerAttributes)



@given(instance=fxg_ContainerAttributes_strategy)
def test_fxg_containerattributes_paddingBottom_setter(instance):
    original = instance.paddingBottom
    instance.paddingBottom = original
    assert instance.paddingBottom == original



@given(instance=fxg_ContainerAttributes_strategy)
def test_fxg_containerattributes_paddingTop_setter(instance):
    original = instance.paddingTop
    instance.paddingTop = original
    assert instance.paddingTop == original



@given(instance=fxg_ContainerAttributes_strategy)
def test_fxg_containerattributes_columnWidth_setter(instance):
    original = instance.columnWidth
    instance.columnWidth = original
    assert instance.columnWidth == original



@given(instance=fxg_ContainerAttributes_strategy)
def test_fxg_containerattributes_blockProgression_setter(instance):
    original = instance.blockProgression
    instance.blockProgression = original
    assert instance.blockProgression == original



@given(instance=fxg_ContainerAttributes_strategy)
def test_fxg_containerattributes_paddingLeft_setter(instance):
    original = instance.paddingLeft
    instance.paddingLeft = original
    assert instance.paddingLeft == original



@given(instance=fxg_ContainerAttributes_strategy)
def test_fxg_containerattributes_firstBaselineOffset_setter(instance):
    original = instance.firstBaselineOffset
    instance.firstBaselineOffset = original
    assert instance.firstBaselineOffset == original



@given(instance=fxg_ContainerAttributes_strategy)
def test_fxg_containerattributes_verticalAlign_setter(instance):
    original = instance.verticalAlign
    instance.verticalAlign = original
    assert instance.verticalAlign == original



@given(instance=fxg_ContainerAttributes_strategy)
def test_fxg_containerattributes_paddingRight_setter(instance):
    original = instance.paddingRight
    instance.paddingRight = original
    assert instance.paddingRight == original



@given(instance=fxg_ContainerAttributes_strategy)
def test_fxg_containerattributes_columnCount_setter(instance):
    original = instance.columnCount
    instance.columnCount = original
    assert instance.columnCount == original



@given(instance=fxg_ContainerAttributes_strategy)
def test_fxg_containerattributes_lineBreak_setter(instance):
    original = instance.lineBreak
    instance.lineBreak = original
    assert instance.lineBreak == original



@given(instance=fxg_ContainerAttributes_strategy)
def test_fxg_containerattributes_columnGap_setter(instance):
    original = instance.columnGap
    instance.columnGap = original
    assert instance.columnGap == original

@given(instance=fxg_ParagraphAttributes_strategy)
@settings(max_examples=50)
def test_fxg_paragraphattributes_instantiation(instance):
    assert isinstance(instance, fxg_ParagraphAttributes)



@given(instance=fxg_ParagraphAttributes_strategy)
def test_fxg_paragraphattributes_paragraphSpaceBefore_setter(instance):
    original = instance.paragraphSpaceBefore
    instance.paragraphSpaceBefore = original
    assert instance.paragraphSpaceBefore == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_fxg_paragraphattributes_textAlign_setter(instance):
    original = instance.textAlign
    instance.textAlign = original
    assert instance.textAlign == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_fxg_paragraphattributes_paragraphSpaceAfter_setter(instance):
    original = instance.paragraphSpaceAfter
    instance.paragraphSpaceAfter = original
    assert instance.paragraphSpaceAfter == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_fxg_paragraphattributes_justificationStyle_setter(instance):
    original = instance.justificationStyle
    instance.justificationStyle = original
    assert instance.justificationStyle == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_fxg_paragraphattributes_leadingModel_setter(instance):
    original = instance.leadingModel
    instance.leadingModel = original
    assert instance.leadingModel == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_fxg_paragraphattributes_textIndent_setter(instance):
    original = instance.textIndent
    instance.textIndent = original
    assert instance.textIndent == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_fxg_paragraphattributes_tabStops_setter(instance):
    original = instance.tabStops
    instance.tabStops = original
    assert instance.tabStops == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_fxg_paragraphattributes_textAlignLast_setter(instance):
    original = instance.textAlignLast
    instance.textAlignLast = original
    assert instance.textAlignLast == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_fxg_paragraphattributes_paragraphEndIndent_setter(instance):
    original = instance.paragraphEndIndent
    instance.paragraphEndIndent = original
    assert instance.paragraphEndIndent == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_fxg_paragraphattributes_justificationRule_setter(instance):
    original = instance.justificationRule
    instance.justificationRule = original
    assert instance.justificationRule == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_fxg_paragraphattributes_paragraphStartIndent_setter(instance):
    original = instance.paragraphStartIndent
    instance.paragraphStartIndent = original
    assert instance.paragraphStartIndent == original



@given(instance=fxg_ParagraphAttributes_strategy)
def test_fxg_paragraphattributes_textJustify_setter(instance):
    original = instance.textJustify
    instance.textJustify = original
    assert instance.textJustify == original

@given(instance=RichTextContent_strategy)
@settings(max_examples=50)
def test_richtextcontent_instantiation(instance):
    assert isinstance(instance, RichTextContent)

@given(instance=fxg_a_strategy)
@settings(max_examples=50)
def test_fxg_a_instantiation(instance):
    assert isinstance(instance, fxg_a)

@given(instance=fxg_br_strategy)
@settings(max_examples=50)
def test_fxg_br_instantiation(instance):
    assert isinstance(instance, fxg_br)

@given(instance=fxg_rawtext_strategy)
@settings(max_examples=50)
def test_fxg_rawtext_instantiation(instance):
    assert isinstance(instance, fxg_rawtext)



@given(instance=fxg_rawtext_strategy)
def test_fxg_rawtext__text_setter(instance):
    original = instance._text
    instance._text = original
    assert instance._text == original

@given(instance=fxg_tab_strategy)
@settings(max_examples=50)
def test_fxg_tab_instantiation(instance):
    assert isinstance(instance, fxg_tab)

@given(instance=fxg_img_strategy)
@settings(max_examples=50)
def test_fxg_img_instantiation(instance):
    assert isinstance(instance, fxg_img)

@given(instance=fxg_span_strategy)
@settings(max_examples=50)
def test_fxg_span_instantiation(instance):
    assert isinstance(instance, fxg_span)

@given(instance=fxg_linkNormalFormat_strategy)
@settings(max_examples=50)
def test_fxg_linknormalformat_instantiation(instance):
    assert isinstance(instance, fxg_linkNormalFormat)

@given(instance=fxg_div_strategy)
@settings(max_examples=50)
def test_fxg_div_instantiation(instance):
    assert isinstance(instance, fxg_div)

@given(instance=fxg_linkHoverFormat_strategy)
@settings(max_examples=50)
def test_fxg_linkhoverformat_instantiation(instance):
    assert isinstance(instance, fxg_linkHoverFormat)

@given(instance=fxg_tcy_strategy)
@settings(max_examples=50)
def test_fxg_tcy_instantiation(instance):
    assert isinstance(instance, fxg_tcy)

@given(instance=fxg_RichTextContentContainer_strategy)
@settings(max_examples=50)
def test_fxg_richtextcontentcontainer_instantiation(instance):
    assert isinstance(instance, fxg_RichTextContentContainer)

@given(instance=fxg_RichTextContent_strategy)
@settings(max_examples=50)
def test_fxg_richtextcontent_instantiation(instance):
    assert isinstance(instance, fxg_RichTextContent)

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

@given(instance=fxg_p_strategy)
@settings(max_examples=50)
def test_fxg_p_instantiation(instance):
    assert isinstance(instance, fxg_p)

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=fxg_Line_strategy)
@settings(max_examples=50)
def test_fxg_line_instantiation(instance):
    assert isinstance(instance, fxg_Line)



@given(instance=fxg_Line_strategy)
def test_fxg_line_yFrom_setter(instance):
    original = instance.yFrom
    instance.yFrom = original
    assert instance.yFrom == original



@given(instance=fxg_Line_strategy)
def test_fxg_line_yTo_setter(instance):
    original = instance.yTo
    instance.yTo = original
    assert instance.yTo == original



@given(instance=fxg_Line_strategy)
def test_fxg_line_blendMode_setter(instance):
    original = instance.blendMode
    instance.blendMode = original
    assert instance.blendMode == original



@given(instance=fxg_Line_strategy)
def test_fxg_line_xTo_setter(instance):
    original = instance.xTo
    instance.xTo = original
    assert instance.xTo == original



@given(instance=fxg_Line_strategy)
def test_fxg_line_xFrom_setter(instance):
    original = instance.xFrom
    instance.xFrom = original
    assert instance.xFrom == original



@given(instance=fxg_Line_strategy)
def test_fxg_line_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=fxg_Line_strategy)
def test_fxg_line_maskType_setter(instance):
    original = instance.maskType
    instance.maskType = original
    assert instance.maskType == original



@given(instance=fxg_Line_strategy)
def test_fxg_line_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=fxg_Line_strategy)
def test_fxg_line_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_Line_strategy)
def test_fxg_line_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_Line_strategy)
def test_fxg_line_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_Line_strategy)
def test_fxg_line_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original



@given(instance=fxg_Line_strategy)
def test_fxg_line_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_Line_strategy)
def test_fxg_line_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=fxg_Ellipse_strategy)
@settings(max_examples=50)
def test_fxg_ellipse_instantiation(instance):
    assert isinstance(instance, fxg_Ellipse)



@given(instance=fxg_Ellipse_strategy)
def test_fxg_ellipse_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=fxg_Ellipse_strategy)
def test_fxg_ellipse_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_Ellipse_strategy)
def test_fxg_ellipse_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_Ellipse_strategy)
def test_fxg_ellipse_blendMode_setter(instance):
    original = instance.blendMode
    instance.blendMode = original
    assert instance.blendMode == original



@given(instance=fxg_Ellipse_strategy)
def test_fxg_ellipse_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=fxg_Ellipse_strategy)
def test_fxg_ellipse_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_Ellipse_strategy)
def test_fxg_ellipse_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original



@given(instance=fxg_Ellipse_strategy)
def test_fxg_ellipse_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=fxg_Ellipse_strategy)
def test_fxg_ellipse_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=fxg_Ellipse_strategy)
def test_fxg_ellipse_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original

@given(instance=fxg_Rect_strategy)
@settings(max_examples=50)
def test_fxg_rect_instantiation(instance):
    assert isinstance(instance, fxg_Rect)



@given(instance=fxg_Rect_strategy)
def test_fxg_rect_radiusX_setter(instance):
    original = instance.radiusX
    instance.radiusX = original
    assert instance.radiusX == original



@given(instance=fxg_Rect_strategy)
def test_fxg_rect_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_Rect_strategy)
def test_fxg_rect_blendMode_setter(instance):
    original = instance.blendMode
    instance.blendMode = original
    assert instance.blendMode == original



@given(instance=fxg_Rect_strategy)
def test_fxg_rect_topRightRadiusX_setter(instance):
    original = instance.topRightRadiusX
    instance.topRightRadiusX = original
    assert instance.topRightRadiusX == original



@given(instance=fxg_Rect_strategy)
def test_fxg_rect_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=fxg_Rect_strategy)
def test_fxg_rect_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=fxg_Rect_strategy)
def test_fxg_rect_radiusY_setter(instance):
    original = instance.radiusY
    instance.radiusY = original
    assert instance.radiusY == original



@given(instance=fxg_Rect_strategy)
def test_fxg_rect_bottomLeftRadiusX_setter(instance):
    original = instance.bottomLeftRadiusX
    instance.bottomLeftRadiusX = original
    assert instance.bottomLeftRadiusX == original



@given(instance=fxg_Rect_strategy)
def test_fxg_rect_topLeftRadiusY_setter(instance):
    original = instance.topLeftRadiusY
    instance.topLeftRadiusY = original
    assert instance.topLeftRadiusY == original



@given(instance=fxg_Rect_strategy)
def test_fxg_rect_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original



@given(instance=fxg_Rect_strategy)
def test_fxg_rect_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_Rect_strategy)
def test_fxg_rect_topLeftRadiusX_setter(instance):
    original = instance.topLeftRadiusX
    instance.topLeftRadiusX = original
    assert instance.topLeftRadiusX == original



@given(instance=fxg_Rect_strategy)
def test_fxg_rect_topRightRadiusY_setter(instance):
    original = instance.topRightRadiusY
    instance.topRightRadiusY = original
    assert instance.topRightRadiusY == original



@given(instance=fxg_Rect_strategy)
def test_fxg_rect_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=fxg_Rect_strategy)
def test_fxg_rect_bottomRightRadiusX_setter(instance):
    original = instance.bottomRightRadiusX
    instance.bottomRightRadiusX = original
    assert instance.bottomRightRadiusX == original



@given(instance=fxg_Rect_strategy)
def test_fxg_rect_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_Rect_strategy)
def test_fxg_rect_bottomRightRadiusY_setter(instance):
    original = instance.bottomRightRadiusY
    instance.bottomRightRadiusY = original
    assert instance.bottomRightRadiusY == original



@given(instance=fxg_Rect_strategy)
def test_fxg_rect_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=fxg_Rect_strategy)
def test_fxg_rect_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_Rect_strategy)
def test_fxg_rect_bottomLeftRadiusY_setter(instance):
    original = instance.bottomLeftRadiusY
    instance.bottomLeftRadiusY = original
    assert instance.bottomLeftRadiusY == original

@given(instance=fxg_Definition_strategy)
@settings(max_examples=50)
def test_fxg_definition_instantiation(instance):
    assert isinstance(instance, fxg_Definition)



@given(instance=fxg_Definition_strategy)
def test_fxg_definition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FXGElement_strategy)
@settings(max_examples=50)
def test_fxgelement_instantiation(instance):
    assert isinstance(instance, FXGElement)

@given(instance=fxg_PlaceObject_strategy)
@settings(max_examples=50)
def test_fxg_placeobject_instantiation(instance):
    assert isinstance(instance, fxg_PlaceObject)



@given(instance=fxg_PlaceObject_strategy)
def test_fxg_placeobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=fxg_Fill_strategy)
@settings(max_examples=50)
def test_fxg_fill_instantiation(instance):
    assert isinstance(instance, fxg_Fill)

@given(instance=fxg_Path_strategy)
@settings(max_examples=50)
def test_fxg_path_instantiation(instance):
    assert isinstance(instance, fxg_Path)



@given(instance=fxg_Path_strategy)
def test_fxg_path_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=fxg_Path_strategy)
def test_fxg_path_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original



@given(instance=fxg_Path_strategy)
def test_fxg_path_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_Path_strategy)
def test_fxg_path_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_Path_strategy)
def test_fxg_path_winding_setter(instance):
    original = instance.winding
    instance.winding = original
    assert instance.winding == original



@given(instance=fxg_Path_strategy)
def test_fxg_path_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_Path_strategy)
def test_fxg_path_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_Path_strategy)
def test_fxg_path_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original



@given(instance=fxg_Path_strategy)
def test_fxg_path_blendMode_setter(instance):
    original = instance.blendMode
    instance.blendMode = original
    assert instance.blendMode == original



@given(instance=fxg_Path_strategy)
def test_fxg_path_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=fxg_ContainerElement_strategy)
@settings(max_examples=50)
def test_fxg_containerelement_instantiation(instance):
    assert isinstance(instance, fxg_ContainerElement)

@given(instance=fxg_GradientEntry_strategy)
@settings(max_examples=50)
def test_fxg_gradiententry_instantiation(instance):
    assert isinstance(instance, fxg_GradientEntry)



@given(instance=fxg_GradientEntry_strategy)
def test_fxg_gradiententry_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=fxg_GradientEntry_strategy)
def test_fxg_gradiententry_ratio_setter(instance):
    original = instance.ratio
    instance.ratio = original
    assert instance.ratio == original



@given(instance=fxg_GradientEntry_strategy)
def test_fxg_gradiententry_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=fxg_BitmapImage_strategy)
@settings(max_examples=50)
def test_fxg_bitmapimage_instantiation(instance):
    assert isinstance(instance, fxg_BitmapImage)



@given(instance=fxg_BitmapImage_strategy)
def test_fxg_bitmapimage_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_BitmapImage_strategy)
def test_fxg_bitmapimage_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=fxg_BitmapImage_strategy)
def test_fxg_bitmapimage_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=fxg_BitmapImage_strategy)
def test_fxg_bitmapimage_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_BitmapImage_strategy)
def test_fxg_bitmapimage_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_BitmapImage_strategy)
def test_fxg_bitmapimage_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=fxg_BitmapImage_strategy)
def test_fxg_bitmapimage_blendMode_setter(instance):
    original = instance.blendMode
    instance.blendMode = original
    assert instance.blendMode == original



@given(instance=fxg_BitmapImage_strategy)
def test_fxg_bitmapimage_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original



@given(instance=fxg_BitmapImage_strategy)
def test_fxg_bitmapimage_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=fxg_BitmapImage_strategy)
def test_fxg_bitmapimage_fillMode_setter(instance):
    original = instance.fillMode
    instance.fillMode = original
    assert instance.fillMode == original



@given(instance=fxg_BitmapImage_strategy)
def test_fxg_bitmapimage_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_BitmapImage_strategy)
def test_fxg_bitmapimage_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=fxg_RichText_strategy)
@settings(max_examples=50)
def test_fxg_richtext_instantiation(instance):
    assert isinstance(instance, fxg_RichText)



@given(instance=fxg_RichText_strategy)
def test_fxg_richtext_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=fxg_RichText_strategy)
def test_fxg_richtext_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=fxg_RichText_strategy)
def test_fxg_richtext_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_RichText_strategy)
def test_fxg_richtext_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original



@given(instance=fxg_RichText_strategy)
def test_fxg_richtext__tempcontent_setter(instance):
    original = instance._tempcontent
    instance._tempcontent = original
    assert instance._tempcontent == original



@given(instance=fxg_RichText_strategy)
def test_fxg_richtext_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_RichText_strategy)
def test_fxg_richtext_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=fxg_RichText_strategy)
def test_fxg_richtext_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_RichText_strategy)
def test_fxg_richtext_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=fxg_RichText_strategy)
def test_fxg_richtext_maskType_setter(instance):
    original = instance.maskType
    instance.maskType = original
    assert instance.maskType == original



@given(instance=fxg_RichText_strategy)
def test_fxg_richtext_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_RichText_strategy)
def test_fxg_richtext_blendMode_setter(instance):
    original = instance.blendMode
    instance.blendMode = original
    assert instance.blendMode == original



@given(instance=fxg_RichText_strategy)
def test_fxg_richtext_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=fxg_Filter_strategy)
@settings(max_examples=50)
def test_fxg_filter_instantiation(instance):
    assert isinstance(instance, fxg_Filter)

@given(instance=fxg_Shape_strategy)
@settings(max_examples=50)
def test_fxg_shape_instantiation(instance):
    assert isinstance(instance, fxg_Shape)

@given(instance=fxg_Stroke_strategy)
@settings(max_examples=50)
def test_fxg_stroke_instantiation(instance):
    assert isinstance(instance, fxg_Stroke)

@given(instance=fxg_Transform_strategy)
@settings(max_examples=50)
def test_fxg_transform_instantiation(instance):
    assert isinstance(instance, fxg_Transform)

@given(instance=fxg_Private_strategy)
@settings(max_examples=50)
def test_fxg_private_instantiation(instance):
    assert isinstance(instance, fxg_Private)

@given(instance=fxg_Library_strategy)
@settings(max_examples=50)
def test_fxg_library_instantiation(instance):
    assert isinstance(instance, fxg_Library)

@given(instance=fxg_Group_strategy)
@settings(max_examples=50)
def test_fxg_group_instantiation(instance):
    assert isinstance(instance, fxg_Group)



@given(instance=fxg_Group_strategy)
def test_fxg_group_scaleGridLeft_setter(instance):
    original = instance.scaleGridLeft
    instance.scaleGridLeft = original
    assert instance.scaleGridLeft == original



@given(instance=fxg_Group_strategy)
def test_fxg_group_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=fxg_Group_strategy)
def test_fxg_group_scaleGridRight_setter(instance):
    original = instance.scaleGridRight
    instance.scaleGridRight = original
    assert instance.scaleGridRight == original



@given(instance=fxg_Group_strategy)
def test_fxg_group_blendMode_setter(instance):
    original = instance.blendMode
    instance.blendMode = original
    assert instance.blendMode == original



@given(instance=fxg_Group_strategy)
def test_fxg_group_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=fxg_Group_strategy)
def test_fxg_group_transformY_setter(instance):
    original = instance.transformY
    instance.transformY = original
    assert instance.transformY == original



@given(instance=fxg_Group_strategy)
def test_fxg_group_transformX_setter(instance):
    original = instance.transformX
    instance.transformX = original
    assert instance.transformX == original



@given(instance=fxg_Group_strategy)
def test_fxg_group_scaleGridTop_setter(instance):
    original = instance.scaleGridTop
    instance.scaleGridTop = original
    assert instance.scaleGridTop == original



@given(instance=fxg_Group_strategy)
def test_fxg_group_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=fxg_Group_strategy)
def test_fxg_group_maskType_setter(instance):
    original = instance.maskType
    instance.maskType = original
    assert instance.maskType == original



@given(instance=fxg_Group_strategy)
def test_fxg_group_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=fxg_Group_strategy)
def test_fxg_group_scaleGridBottom_setter(instance):
    original = instance.scaleGridBottom
    instance.scaleGridBottom = original
    assert instance.scaleGridBottom == original



@given(instance=fxg_Group_strategy)
def test_fxg_group_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=fxg_Group_strategy)
def test_fxg_group_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=fxg_Group_strategy)
def test_fxg_group_scaleX_setter(instance):
    original = instance.scaleX
    instance.scaleX = original
    assert instance.scaleX == original



@given(instance=fxg_Group_strategy)
def test_fxg_group_scaleY_setter(instance):
    original = instance.scaleY
    instance.scaleY = original
    assert instance.scaleY == original

@given(instance=fxg_Graphic_strategy)
@settings(max_examples=50)
def test_fxg_graphic_instantiation(instance):
    assert isinstance(instance, fxg_Graphic)



@given(instance=fxg_Graphic_strategy)
def test_fxg_graphic_viewHeight_setter(instance):
    original = instance.viewHeight
    instance.viewHeight = original
    assert instance.viewHeight == original



@given(instance=fxg_Graphic_strategy)
def test_fxg_graphic_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=fxg_Graphic_strategy)
def test_fxg_graphic_scaleGridRight_setter(instance):
    original = instance.scaleGridRight
    instance.scaleGridRight = original
    assert instance.scaleGridRight == original



@given(instance=fxg_Graphic_strategy)
def test_fxg_graphic_scaleGridTop_setter(instance):
    original = instance.scaleGridTop
    instance.scaleGridTop = original
    assert instance.scaleGridTop == original



@given(instance=fxg_Graphic_strategy)
def test_fxg_graphic_scaleGridBottom_setter(instance):
    original = instance.scaleGridBottom
    instance.scaleGridBottom = original
    assert instance.scaleGridBottom == original



@given(instance=fxg_Graphic_strategy)
def test_fxg_graphic_scaleGridLeft_setter(instance):
    original = instance.scaleGridLeft
    instance.scaleGridLeft = original
    assert instance.scaleGridLeft == original



@given(instance=fxg_Graphic_strategy)
def test_fxg_graphic_viewWidth_setter(instance):
    original = instance.viewWidth
    instance.viewWidth = original
    assert instance.viewWidth == original

@given(instance=fxg_ColorTransform_strategy)
@settings(max_examples=50)
def test_fxg_colortransform_instantiation(instance):
    assert isinstance(instance, fxg_ColorTransform)



@given(instance=fxg_ColorTransform_strategy)
def test_fxg_colortransform_blueOffset_setter(instance):
    original = instance.blueOffset
    instance.blueOffset = original
    assert instance.blueOffset == original



@given(instance=fxg_ColorTransform_strategy)
def test_fxg_colortransform_greenOffset_setter(instance):
    original = instance.greenOffset
    instance.greenOffset = original
    assert instance.greenOffset == original



@given(instance=fxg_ColorTransform_strategy)
def test_fxg_colortransform_redOffset_setter(instance):
    original = instance.redOffset
    instance.redOffset = original
    assert instance.redOffset == original



@given(instance=fxg_ColorTransform_strategy)
def test_fxg_colortransform_redMultiplier_setter(instance):
    original = instance.redMultiplier
    instance.redMultiplier = original
    assert instance.redMultiplier == original



@given(instance=fxg_ColorTransform_strategy)
def test_fxg_colortransform_alphaMultiplier_setter(instance):
    original = instance.alphaMultiplier
    instance.alphaMultiplier = original
    assert instance.alphaMultiplier == original



@given(instance=fxg_ColorTransform_strategy)
def test_fxg_colortransform_greenMultiplier_setter(instance):
    original = instance.greenMultiplier
    instance.greenMultiplier = original
    assert instance.greenMultiplier == original



@given(instance=fxg_ColorTransform_strategy)
def test_fxg_colortransform_alphaOffset_setter(instance):
    original = instance.alphaOffset
    instance.alphaOffset = original
    assert instance.alphaOffset == original



@given(instance=fxg_ColorTransform_strategy)
def test_fxg_colortransform_blueMultiplier_setter(instance):
    original = instance.blueMultiplier
    instance.blueMultiplier = original
    assert instance.blueMultiplier == original

@given(instance=fxg_Matrix_strategy)
@settings(max_examples=50)
def test_fxg_matrix_instantiation(instance):
    assert isinstance(instance, fxg_Matrix)



@given(instance=fxg_Matrix_strategy)
def test_fxg_matrix_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original



@given(instance=fxg_Matrix_strategy)
def test_fxg_matrix_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original



@given(instance=fxg_Matrix_strategy)
def test_fxg_matrix_ty_setter(instance):
    original = instance.ty
    instance.ty = original
    assert instance.ty == original



@given(instance=fxg_Matrix_strategy)
def test_fxg_matrix_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original



@given(instance=fxg_Matrix_strategy)
def test_fxg_matrix_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original



@given(instance=fxg_Matrix_strategy)
def test_fxg_matrix_tx_setter(instance):
    original = instance.tx
    instance.tx = original
    assert instance.tx == original
