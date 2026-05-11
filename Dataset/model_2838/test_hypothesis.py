import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ck2gfx::Animation,
    ck2gfx::EMFXActorType,
    ck2gfx::ColorCode,
    ck2gfx::BitmapFont,
    ck2gfx::BitmapFonts,
    ck2gfx::ArrowType,
    ck2gfx::Pdxmesh,
    ck2gfx::PortraitType,
    ck2gfx::ObjectTypes,
    ck2gfx::CoatOfArmsLayer,
    ck2gfx::CoatOfArmsType,
    ck2gfx::LineChartType,
    ck2gfx::MaskedShieldType,
    ck2gfx::SpriteType,
    ck2gfx::SpriteTypes,
    ck2gfx::ProgressbarType,
    ck2gfx::CorneredTileSpriteType,
    ck2gfx::AnimatedSpriteType,
    ck2gfx::Coordinates,
    ck2gfx::ColorRatio,
    ck2gfx::Color,
    ck2gfx::EObject,
    ck2gfx::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ck2gfx::animation_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::Animation)


def test_ck2gfx::animation_constructor_exists():
    assert callable(ck2gfx::Animation.__init__)


def test_ck2gfx::animation_constructor_args():
    sig = inspect.signature(ck2gfx::Animation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "file" in params, "Missing parameter 'file'"
    assert "defaultAnimationTime" in params, "Missing parameter 'defaultAnimationTime'"

def test_ck2gfx::animation_has_name():
    assert hasattr(ck2gfx::Animation, "name")
    descriptor = None
    for klass in ck2gfx::Animation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::animation_has_file():
    assert hasattr(ck2gfx::Animation, "file")
    descriptor = None
    for klass in ck2gfx::Animation.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::animation_has_defaultAnimationTime():
    assert hasattr(ck2gfx::Animation, "defaultAnimationTime")
    descriptor = None
    for klass in ck2gfx::Animation.__mro__:
        if "defaultAnimationTime" in klass.__dict__:
            descriptor = klass.__dict__["defaultAnimationTime"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx::emfxactortype_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::EMFXActorType)


def test_ck2gfx::emfxactortype_constructor_exists():
    assert callable(ck2gfx::EMFXActorType.__init__)


def test_ck2gfx::emfxactortype_constructor_args():
    sig = inspect.signature(ck2gfx::EMFXActorType.__init__)
    params = list(sig.parameters.keys())
    assert "actorFile" in params, "Missing parameter 'actorFile'"
    assert "attack" in params, "Missing parameter 'attack'"
    assert "move" in params, "Missing parameter 'move'"
    assert "idle" in params, "Missing parameter 'idle'"
    assert "name" in params, "Missing parameter 'name'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "useAnimation" in params, "Missing parameter 'useAnimation'"
    assert "scaleOnCullDistance" in params, "Missing parameter 'scaleOnCullDistance'"
    assert "cullDistance" in params, "Missing parameter 'cullDistance'"

def test_ck2gfx::emfxactortype_has_actorFile():
    assert hasattr(ck2gfx::EMFXActorType, "actorFile")
    descriptor = None
    for klass in ck2gfx::EMFXActorType.__mro__:
        if "actorFile" in klass.__dict__:
            descriptor = klass.__dict__["actorFile"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::emfxactortype_has_attack():
    assert hasattr(ck2gfx::EMFXActorType, "attack")
    descriptor = None
    for klass in ck2gfx::EMFXActorType.__mro__:
        if "attack" in klass.__dict__:
            descriptor = klass.__dict__["attack"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::emfxactortype_has_move():
    assert hasattr(ck2gfx::EMFXActorType, "move")
    descriptor = None
    for klass in ck2gfx::EMFXActorType.__mro__:
        if "move" in klass.__dict__:
            descriptor = klass.__dict__["move"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::emfxactortype_has_idle():
    assert hasattr(ck2gfx::EMFXActorType, "idle")
    descriptor = None
    for klass in ck2gfx::EMFXActorType.__mro__:
        if "idle" in klass.__dict__:
            descriptor = klass.__dict__["idle"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::emfxactortype_has_name():
    assert hasattr(ck2gfx::EMFXActorType, "name")
    descriptor = None
    for klass in ck2gfx::EMFXActorType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::emfxactortype_has_scale():
    assert hasattr(ck2gfx::EMFXActorType, "scale")
    descriptor = None
    for klass in ck2gfx::EMFXActorType.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::emfxactortype_has_useAnimation():
    assert hasattr(ck2gfx::EMFXActorType, "useAnimation")
    descriptor = None
    for klass in ck2gfx::EMFXActorType.__mro__:
        if "useAnimation" in klass.__dict__:
            descriptor = klass.__dict__["useAnimation"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::emfxactortype_has_scaleOnCullDistance():
    assert hasattr(ck2gfx::EMFXActorType, "scaleOnCullDistance")
    descriptor = None
    for klass in ck2gfx::EMFXActorType.__mro__:
        if "scaleOnCullDistance" in klass.__dict__:
            descriptor = klass.__dict__["scaleOnCullDistance"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::emfxactortype_has_cullDistance():
    assert hasattr(ck2gfx::EMFXActorType, "cullDistance")
    descriptor = None
    for klass in ck2gfx::EMFXActorType.__mro__:
        if "cullDistance" in klass.__dict__:
            descriptor = klass.__dict__["cullDistance"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx::colorcode_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::ColorCode)


def test_ck2gfx::colorcode_constructor_exists():
    assert callable(ck2gfx::ColorCode.__init__)


def test_ck2gfx::colorcode_constructor_args():
    sig = inspect.signature(ck2gfx::ColorCode.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_ck2gfx::colorcode_has_key():
    assert hasattr(ck2gfx::ColorCode, "key")
    descriptor = None
    for klass in ck2gfx::ColorCode.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx::bitmapfont_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::BitmapFont)


def test_ck2gfx::bitmapfont_constructor_exists():
    assert callable(ck2gfx::BitmapFont.__init__)


def test_ck2gfx::bitmapfont_constructor_args():
    sig = inspect.signature(ck2gfx::BitmapFont.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "fontName" in params, "Missing parameter 'fontName'"
    assert "name" in params, "Missing parameter 'name'"

def test_ck2gfx::bitmapfont_has_color():
    assert hasattr(ck2gfx::BitmapFont, "color")
    descriptor = None
    for klass in ck2gfx::BitmapFont.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::bitmapfont_has_effect():
    assert hasattr(ck2gfx::BitmapFont, "effect")
    descriptor = None
    for klass in ck2gfx::BitmapFont.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::bitmapfont_has_fontName():
    assert hasattr(ck2gfx::BitmapFont, "fontName")
    descriptor = None
    for klass in ck2gfx::BitmapFont.__mro__:
        if "fontName" in klass.__dict__:
            descriptor = klass.__dict__["fontName"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::bitmapfont_has_name():
    assert hasattr(ck2gfx::BitmapFont, "name")
    descriptor = None
    for klass in ck2gfx::BitmapFont.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx::bitmapfonts_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::BitmapFonts)


def test_ck2gfx::bitmapfonts_constructor_exists():
    assert callable(ck2gfx::BitmapFonts.__init__)


def test_ck2gfx::bitmapfonts_constructor_args():
    sig = inspect.signature(ck2gfx::BitmapFonts.__init__)
    params = list(sig.parameters.keys())



def test_ck2gfx::arrowtype_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::ArrowType)


def test_ck2gfx::arrowtype_constructor_exists():
    assert callable(ck2gfx::ArrowType.__init__)


def test_ck2gfx::arrowtype_constructor_args():
    sig = inspect.signature(ck2gfx::ArrowType.__init__)
    params = list(sig.parameters.keys())
    assert "effect" in params, "Missing parameter 'effect'"
    assert "height" in params, "Missing parameter 'height'"
    assert "size" in params, "Missing parameter 'size'"
    assert "endAt" in params, "Missing parameter 'endAt'"
    assert "textureFile" in params, "Missing parameter 'textureFile'"
    assert "name" in params, "Missing parameter 'name'"
    assert "bodyTexture" in params, "Missing parameter 'bodyTexture'"
    assert "type" in params, "Missing parameter 'type'"
    assert "heading" in params, "Missing parameter 'heading'"

def test_ck2gfx::arrowtype_has_effect():
    assert hasattr(ck2gfx::ArrowType, "effect")
    descriptor = None
    for klass in ck2gfx::ArrowType.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::arrowtype_has_height():
    assert hasattr(ck2gfx::ArrowType, "height")
    descriptor = None
    for klass in ck2gfx::ArrowType.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::arrowtype_has_size():
    assert hasattr(ck2gfx::ArrowType, "size")
    descriptor = None
    for klass in ck2gfx::ArrowType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::arrowtype_has_endAt():
    assert hasattr(ck2gfx::ArrowType, "endAt")
    descriptor = None
    for klass in ck2gfx::ArrowType.__mro__:
        if "endAt" in klass.__dict__:
            descriptor = klass.__dict__["endAt"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::arrowtype_has_textureFile():
    assert hasattr(ck2gfx::ArrowType, "textureFile")
    descriptor = None
    for klass in ck2gfx::ArrowType.__mro__:
        if "textureFile" in klass.__dict__:
            descriptor = klass.__dict__["textureFile"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::arrowtype_has_name():
    assert hasattr(ck2gfx::ArrowType, "name")
    descriptor = None
    for klass in ck2gfx::ArrowType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::arrowtype_has_bodyTexture():
    assert hasattr(ck2gfx::ArrowType, "bodyTexture")
    descriptor = None
    for klass in ck2gfx::ArrowType.__mro__:
        if "bodyTexture" in klass.__dict__:
            descriptor = klass.__dict__["bodyTexture"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::arrowtype_has_type():
    assert hasattr(ck2gfx::ArrowType, "type")
    descriptor = None
    for klass in ck2gfx::ArrowType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::arrowtype_has_heading():
    assert hasattr(ck2gfx::ArrowType, "heading")
    descriptor = None
    for klass in ck2gfx::ArrowType.__mro__:
        if "heading" in klass.__dict__:
            descriptor = klass.__dict__["heading"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx::pdxmesh_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::Pdxmesh)


def test_ck2gfx::pdxmesh_constructor_exists():
    assert callable(ck2gfx::Pdxmesh.__init__)


def test_ck2gfx::pdxmesh_constructor_args():
    sig = inspect.signature(ck2gfx::Pdxmesh.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "scaleOnCullDistance" in params, "Missing parameter 'scaleOnCullDistance'"
    assert "cullDistance" in params, "Missing parameter 'cullDistance'"
    assert "actorFile" in params, "Missing parameter 'actorFile'"
    assert "scale" in params, "Missing parameter 'scale'"

def test_ck2gfx::pdxmesh_has_name():
    assert hasattr(ck2gfx::Pdxmesh, "name")
    descriptor = None
    for klass in ck2gfx::Pdxmesh.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::pdxmesh_has_scaleOnCullDistance():
    assert hasattr(ck2gfx::Pdxmesh, "scaleOnCullDistance")
    descriptor = None
    for klass in ck2gfx::Pdxmesh.__mro__:
        if "scaleOnCullDistance" in klass.__dict__:
            descriptor = klass.__dict__["scaleOnCullDistance"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::pdxmesh_has_cullDistance():
    assert hasattr(ck2gfx::Pdxmesh, "cullDistance")
    descriptor = None
    for klass in ck2gfx::Pdxmesh.__mro__:
        if "cullDistance" in klass.__dict__:
            descriptor = klass.__dict__["cullDistance"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::pdxmesh_has_actorFile():
    assert hasattr(ck2gfx::Pdxmesh, "actorFile")
    descriptor = None
    for klass in ck2gfx::Pdxmesh.__mro__:
        if "actorFile" in klass.__dict__:
            descriptor = klass.__dict__["actorFile"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::pdxmesh_has_scale():
    assert hasattr(ck2gfx::Pdxmesh, "scale")
    descriptor = None
    for klass in ck2gfx::Pdxmesh.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx::portraittype_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::PortraitType)


def test_ck2gfx::portraittype_constructor_exists():
    assert callable(ck2gfx::PortraitType.__init__)


def test_ck2gfx::portraittype_constructor_args():
    sig = inspect.signature(ck2gfx::PortraitType.__init__)
    params = list(sig.parameters.keys())
    assert "hairColorIndex" in params, "Missing parameter 'hairColorIndex'"
    assert "layers" in params, "Missing parameter 'layers'"
    assert "eyeColorIndex" in params, "Missing parameter 'eyeColorIndex'"
    assert "name" in params, "Missing parameter 'name'"
    assert "headgearThatHidesHair" in params, "Missing parameter 'headgearThatHidesHair'"
    assert "effectFile" in params, "Missing parameter 'effectFile'"

def test_ck2gfx::portraittype_has_hairColorIndex():
    assert hasattr(ck2gfx::PortraitType, "hairColorIndex")
    descriptor = None
    for klass in ck2gfx::PortraitType.__mro__:
        if "hairColorIndex" in klass.__dict__:
            descriptor = klass.__dict__["hairColorIndex"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::portraittype_has_layers():
    assert hasattr(ck2gfx::PortraitType, "layers")
    descriptor = None
    for klass in ck2gfx::PortraitType.__mro__:
        if "layers" in klass.__dict__:
            descriptor = klass.__dict__["layers"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::portraittype_has_eyeColorIndex():
    assert hasattr(ck2gfx::PortraitType, "eyeColorIndex")
    descriptor = None
    for klass in ck2gfx::PortraitType.__mro__:
        if "eyeColorIndex" in klass.__dict__:
            descriptor = klass.__dict__["eyeColorIndex"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::portraittype_has_name():
    assert hasattr(ck2gfx::PortraitType, "name")
    descriptor = None
    for klass in ck2gfx::PortraitType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::portraittype_has_headgearThatHidesHair():
    assert hasattr(ck2gfx::PortraitType, "headgearThatHidesHair")
    descriptor = None
    for klass in ck2gfx::PortraitType.__mro__:
        if "headgearThatHidesHair" in klass.__dict__:
            descriptor = klass.__dict__["headgearThatHidesHair"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::portraittype_has_effectFile():
    assert hasattr(ck2gfx::PortraitType, "effectFile")
    descriptor = None
    for klass in ck2gfx::PortraitType.__mro__:
        if "effectFile" in klass.__dict__:
            descriptor = klass.__dict__["effectFile"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx::objecttypes_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::ObjectTypes)


def test_ck2gfx::objecttypes_constructor_exists():
    assert callable(ck2gfx::ObjectTypes.__init__)


def test_ck2gfx::objecttypes_constructor_args():
    sig = inspect.signature(ck2gfx::ObjectTypes.__init__)
    params = list(sig.parameters.keys())



def test_ck2gfx::coatofarmslayer_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::CoatOfArmsLayer)


def test_ck2gfx::coatofarmslayer_constructor_exists():
    assert callable(ck2gfx::CoatOfArmsLayer.__init__)


def test_ck2gfx::coatofarmslayer_constructor_args():
    sig = inspect.signature(ck2gfx::CoatOfArmsLayer.__init__)
    params = list(sig.parameters.keys())
    assert "mask" in params, "Missing parameter 'mask'"
    assert "scale" in params, "Missing parameter 'scale'"

def test_ck2gfx::coatofarmslayer_has_mask():
    assert hasattr(ck2gfx::CoatOfArmsLayer, "mask")
    descriptor = None
    for klass in ck2gfx::CoatOfArmsLayer.__mro__:
        if "mask" in klass.__dict__:
            descriptor = klass.__dict__["mask"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::coatofarmslayer_has_scale():
    assert hasattr(ck2gfx::CoatOfArmsLayer, "scale")
    descriptor = None
    for klass in ck2gfx::CoatOfArmsLayer.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx::coatofarmstype_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::CoatOfArmsType)


def test_ck2gfx::coatofarmstype_constructor_exists():
    assert callable(ck2gfx::CoatOfArmsType.__init__)


def test_ck2gfx::coatofarmstype_constructor_args():
    sig = inspect.signature(ck2gfx::CoatOfArmsType.__init__)
    params = list(sig.parameters.keys())
    assert "effect" in params, "Missing parameter 'effect'"
    assert "mask" in params, "Missing parameter 'mask'"
    assert "name" in params, "Missing parameter 'name'"
    assert "sealOverlay" in params, "Missing parameter 'sealOverlay'"
    assert "frame" in params, "Missing parameter 'frame'"

def test_ck2gfx::coatofarmstype_has_effect():
    assert hasattr(ck2gfx::CoatOfArmsType, "effect")
    descriptor = None
    for klass in ck2gfx::CoatOfArmsType.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::coatofarmstype_has_mask():
    assert hasattr(ck2gfx::CoatOfArmsType, "mask")
    descriptor = None
    for klass in ck2gfx::CoatOfArmsType.__mro__:
        if "mask" in klass.__dict__:
            descriptor = klass.__dict__["mask"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::coatofarmstype_has_name():
    assert hasattr(ck2gfx::CoatOfArmsType, "name")
    descriptor = None
    for klass in ck2gfx::CoatOfArmsType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::coatofarmstype_has_sealOverlay():
    assert hasattr(ck2gfx::CoatOfArmsType, "sealOverlay")
    descriptor = None
    for klass in ck2gfx::CoatOfArmsType.__mro__:
        if "sealOverlay" in klass.__dict__:
            descriptor = klass.__dict__["sealOverlay"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::coatofarmstype_has_frame():
    assert hasattr(ck2gfx::CoatOfArmsType, "frame")
    descriptor = None
    for klass in ck2gfx::CoatOfArmsType.__mro__:
        if "frame" in klass.__dict__:
            descriptor = klass.__dict__["frame"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx::linecharttype_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::LineChartType)


def test_ck2gfx::linecharttype_constructor_exists():
    assert callable(ck2gfx::LineChartType.__init__)


def test_ck2gfx::linecharttype_constructor_args():
    sig = inspect.signature(ck2gfx::LineChartType.__init__)
    params = list(sig.parameters.keys())
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"
    assert "name" in params, "Missing parameter 'name'"

def test_ck2gfx::linecharttype_has_lineWidth():
    assert hasattr(ck2gfx::LineChartType, "lineWidth")
    descriptor = None
    for klass in ck2gfx::LineChartType.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::linecharttype_has_name():
    assert hasattr(ck2gfx::LineChartType, "name")
    descriptor = None
    for klass in ck2gfx::LineChartType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx::maskedshieldtype_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::MaskedShieldType)


def test_ck2gfx::maskedshieldtype_constructor_exists():
    assert callable(ck2gfx::MaskedShieldType.__init__)


def test_ck2gfx::maskedshieldtype_constructor_args():
    sig = inspect.signature(ck2gfx::MaskedShieldType.__init__)
    params = list(sig.parameters.keys())
    assert "textureFile2" in params, "Missing parameter 'textureFile2'"
    assert "textureFile1" in params, "Missing parameter 'textureFile1'"
    assert "clickSound" in params, "Missing parameter 'clickSound'"
    assert "name" in params, "Missing parameter 'name'"
    assert "allwaysTransparent" in params, "Missing parameter 'allwaysTransparent'"
    assert "effectFile" in params, "Missing parameter 'effectFile'"

def test_ck2gfx::maskedshieldtype_has_textureFile2():
    assert hasattr(ck2gfx::MaskedShieldType, "textureFile2")
    descriptor = None
    for klass in ck2gfx::MaskedShieldType.__mro__:
        if "textureFile2" in klass.__dict__:
            descriptor = klass.__dict__["textureFile2"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::maskedshieldtype_has_textureFile1():
    assert hasattr(ck2gfx::MaskedShieldType, "textureFile1")
    descriptor = None
    for klass in ck2gfx::MaskedShieldType.__mro__:
        if "textureFile1" in klass.__dict__:
            descriptor = klass.__dict__["textureFile1"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::maskedshieldtype_has_clickSound():
    assert hasattr(ck2gfx::MaskedShieldType, "clickSound")
    descriptor = None
    for klass in ck2gfx::MaskedShieldType.__mro__:
        if "clickSound" in klass.__dict__:
            descriptor = klass.__dict__["clickSound"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::maskedshieldtype_has_name():
    assert hasattr(ck2gfx::MaskedShieldType, "name")
    descriptor = None
    for klass in ck2gfx::MaskedShieldType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::maskedshieldtype_has_allwaysTransparent():
    assert hasattr(ck2gfx::MaskedShieldType, "allwaysTransparent")
    descriptor = None
    for klass in ck2gfx::MaskedShieldType.__mro__:
        if "allwaysTransparent" in klass.__dict__:
            descriptor = klass.__dict__["allwaysTransparent"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::maskedshieldtype_has_effectFile():
    assert hasattr(ck2gfx::MaskedShieldType, "effectFile")
    descriptor = None
    for klass in ck2gfx::MaskedShieldType.__mro__:
        if "effectFile" in klass.__dict__:
            descriptor = klass.__dict__["effectFile"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx::spritetype_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::SpriteType)


def test_ck2gfx::spritetype_constructor_exists():
    assert callable(ck2gfx::SpriteType.__init__)


def test_ck2gfx::spritetype_constructor_args():
    sig = inspect.signature(ck2gfx::SpriteType.__init__)
    params = list(sig.parameters.keys())
    assert "noRefCount" in params, "Missing parameter 'noRefCount'"
    assert "effectFile" in params, "Missing parameter 'effectFile'"
    assert "clickSound" in params, "Missing parameter 'clickSound'"
    assert "name" in params, "Missing parameter 'name'"
    assert "loadType" in params, "Missing parameter 'loadType'"
    assert "transparenceCheck" in params, "Missing parameter 'transparenceCheck'"
    assert "textureFile" in params, "Missing parameter 'textureFile'"
    assert "canBeLowres" in params, "Missing parameter 'canBeLowres'"
    assert "allwaysTransparent" in params, "Missing parameter 'allwaysTransparent'"
    assert "noOfFrames" in params, "Missing parameter 'noOfFrames'"

def test_ck2gfx::spritetype_has_noRefCount():
    assert hasattr(ck2gfx::SpriteType, "noRefCount")
    descriptor = None
    for klass in ck2gfx::SpriteType.__mro__:
        if "noRefCount" in klass.__dict__:
            descriptor = klass.__dict__["noRefCount"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::spritetype_has_effectFile():
    assert hasattr(ck2gfx::SpriteType, "effectFile")
    descriptor = None
    for klass in ck2gfx::SpriteType.__mro__:
        if "effectFile" in klass.__dict__:
            descriptor = klass.__dict__["effectFile"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::spritetype_has_clickSound():
    assert hasattr(ck2gfx::SpriteType, "clickSound")
    descriptor = None
    for klass in ck2gfx::SpriteType.__mro__:
        if "clickSound" in klass.__dict__:
            descriptor = klass.__dict__["clickSound"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::spritetype_has_name():
    assert hasattr(ck2gfx::SpriteType, "name")
    descriptor = None
    for klass in ck2gfx::SpriteType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::spritetype_has_loadType():
    assert hasattr(ck2gfx::SpriteType, "loadType")
    descriptor = None
    for klass in ck2gfx::SpriteType.__mro__:
        if "loadType" in klass.__dict__:
            descriptor = klass.__dict__["loadType"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::spritetype_has_transparenceCheck():
    assert hasattr(ck2gfx::SpriteType, "transparenceCheck")
    descriptor = None
    for klass in ck2gfx::SpriteType.__mro__:
        if "transparenceCheck" in klass.__dict__:
            descriptor = klass.__dict__["transparenceCheck"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::spritetype_has_textureFile():
    assert hasattr(ck2gfx::SpriteType, "textureFile")
    descriptor = None
    for klass in ck2gfx::SpriteType.__mro__:
        if "textureFile" in klass.__dict__:
            descriptor = klass.__dict__["textureFile"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::spritetype_has_canBeLowres():
    assert hasattr(ck2gfx::SpriteType, "canBeLowres")
    descriptor = None
    for klass in ck2gfx::SpriteType.__mro__:
        if "canBeLowres" in klass.__dict__:
            descriptor = klass.__dict__["canBeLowres"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::spritetype_has_allwaysTransparent():
    assert hasattr(ck2gfx::SpriteType, "allwaysTransparent")
    descriptor = None
    for klass in ck2gfx::SpriteType.__mro__:
        if "allwaysTransparent" in klass.__dict__:
            descriptor = klass.__dict__["allwaysTransparent"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::spritetype_has_noOfFrames():
    assert hasattr(ck2gfx::SpriteType, "noOfFrames")
    descriptor = None
    for klass in ck2gfx::SpriteType.__mro__:
        if "noOfFrames" in klass.__dict__:
            descriptor = klass.__dict__["noOfFrames"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx::spritetypes_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::SpriteTypes)


def test_ck2gfx::spritetypes_constructor_exists():
    assert callable(ck2gfx::SpriteTypes.__init__)


def test_ck2gfx::spritetypes_constructor_args():
    sig = inspect.signature(ck2gfx::SpriteTypes.__init__)
    params = list(sig.parameters.keys())



def test_ck2gfx::progressbartype_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::ProgressbarType)


def test_ck2gfx::progressbartype_constructor_exists():
    assert callable(ck2gfx::ProgressbarType.__init__)


def test_ck2gfx::progressbartype_constructor_args():
    sig = inspect.signature(ck2gfx::ProgressbarType.__init__)
    params = list(sig.parameters.keys())
    assert "loadType" in params, "Missing parameter 'loadType'"
    assert "maxValue" in params, "Missing parameter 'maxValue'"
    assert "name" in params, "Missing parameter 'name'"
    assert "effectFile" in params, "Missing parameter 'effectFile'"
    assert "textureFile2" in params, "Missing parameter 'textureFile2'"
    assert "noRefCount" in params, "Missing parameter 'noRefCount'"
    assert "allwaysTransparent" in params, "Missing parameter 'allwaysTransparent'"
    assert "textureFile1" in params, "Missing parameter 'textureFile1'"
    assert "horizontal" in params, "Missing parameter 'horizontal'"

def test_ck2gfx::progressbartype_has_loadType():
    assert hasattr(ck2gfx::ProgressbarType, "loadType")
    descriptor = None
    for klass in ck2gfx::ProgressbarType.__mro__:
        if "loadType" in klass.__dict__:
            descriptor = klass.__dict__["loadType"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::progressbartype_has_maxValue():
    assert hasattr(ck2gfx::ProgressbarType, "maxValue")
    descriptor = None
    for klass in ck2gfx::ProgressbarType.__mro__:
        if "maxValue" in klass.__dict__:
            descriptor = klass.__dict__["maxValue"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::progressbartype_has_name():
    assert hasattr(ck2gfx::ProgressbarType, "name")
    descriptor = None
    for klass in ck2gfx::ProgressbarType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::progressbartype_has_effectFile():
    assert hasattr(ck2gfx::ProgressbarType, "effectFile")
    descriptor = None
    for klass in ck2gfx::ProgressbarType.__mro__:
        if "effectFile" in klass.__dict__:
            descriptor = klass.__dict__["effectFile"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::progressbartype_has_textureFile2():
    assert hasattr(ck2gfx::ProgressbarType, "textureFile2")
    descriptor = None
    for klass in ck2gfx::ProgressbarType.__mro__:
        if "textureFile2" in klass.__dict__:
            descriptor = klass.__dict__["textureFile2"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::progressbartype_has_noRefCount():
    assert hasattr(ck2gfx::ProgressbarType, "noRefCount")
    descriptor = None
    for klass in ck2gfx::ProgressbarType.__mro__:
        if "noRefCount" in klass.__dict__:
            descriptor = klass.__dict__["noRefCount"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::progressbartype_has_allwaysTransparent():
    assert hasattr(ck2gfx::ProgressbarType, "allwaysTransparent")
    descriptor = None
    for klass in ck2gfx::ProgressbarType.__mro__:
        if "allwaysTransparent" in klass.__dict__:
            descriptor = klass.__dict__["allwaysTransparent"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::progressbartype_has_textureFile1():
    assert hasattr(ck2gfx::ProgressbarType, "textureFile1")
    descriptor = None
    for klass in ck2gfx::ProgressbarType.__mro__:
        if "textureFile1" in klass.__dict__:
            descriptor = klass.__dict__["textureFile1"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::progressbartype_has_horizontal():
    assert hasattr(ck2gfx::ProgressbarType, "horizontal")
    descriptor = None
    for klass in ck2gfx::ProgressbarType.__mro__:
        if "horizontal" in klass.__dict__:
            descriptor = klass.__dict__["horizontal"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx::corneredtilespritetype_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::CorneredTileSpriteType)


def test_ck2gfx::corneredtilespritetype_constructor_exists():
    assert callable(ck2gfx::CorneredTileSpriteType.__init__)


def test_ck2gfx::corneredtilespritetype_constructor_args():
    sig = inspect.signature(ck2gfx::CorneredTileSpriteType.__init__)
    params = list(sig.parameters.keys())
    assert "texturefile" in params, "Missing parameter 'texturefile'"
    assert "name" in params, "Missing parameter 'name'"
    assert "tilingCenter" in params, "Missing parameter 'tilingCenter'"
    assert "noRefCount" in params, "Missing parameter 'noRefCount'"
    assert "allwaysTransparent" in params, "Missing parameter 'allwaysTransparent'"
    assert "loadType" in params, "Missing parameter 'loadType'"

def test_ck2gfx::corneredtilespritetype_has_texturefile():
    assert hasattr(ck2gfx::CorneredTileSpriteType, "texturefile")
    descriptor = None
    for klass in ck2gfx::CorneredTileSpriteType.__mro__:
        if "texturefile" in klass.__dict__:
            descriptor = klass.__dict__["texturefile"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::corneredtilespritetype_has_name():
    assert hasattr(ck2gfx::CorneredTileSpriteType, "name")
    descriptor = None
    for klass in ck2gfx::CorneredTileSpriteType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::corneredtilespritetype_has_tilingCenter():
    assert hasattr(ck2gfx::CorneredTileSpriteType, "tilingCenter")
    descriptor = None
    for klass in ck2gfx::CorneredTileSpriteType.__mro__:
        if "tilingCenter" in klass.__dict__:
            descriptor = klass.__dict__["tilingCenter"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::corneredtilespritetype_has_noRefCount():
    assert hasattr(ck2gfx::CorneredTileSpriteType, "noRefCount")
    descriptor = None
    for klass in ck2gfx::CorneredTileSpriteType.__mro__:
        if "noRefCount" in klass.__dict__:
            descriptor = klass.__dict__["noRefCount"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::corneredtilespritetype_has_allwaysTransparent():
    assert hasattr(ck2gfx::CorneredTileSpriteType, "allwaysTransparent")
    descriptor = None
    for klass in ck2gfx::CorneredTileSpriteType.__mro__:
        if "allwaysTransparent" in klass.__dict__:
            descriptor = klass.__dict__["allwaysTransparent"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::corneredtilespritetype_has_loadType():
    assert hasattr(ck2gfx::CorneredTileSpriteType, "loadType")
    descriptor = None
    for klass in ck2gfx::CorneredTileSpriteType.__mro__:
        if "loadType" in klass.__dict__:
            descriptor = klass.__dict__["loadType"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx::animatedspritetype_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::AnimatedSpriteType)


def test_ck2gfx::animatedspritetype_constructor_exists():
    assert callable(ck2gfx::AnimatedSpriteType.__init__)


def test_ck2gfx::animatedspritetype_constructor_args():
    sig = inspect.signature(ck2gfx::AnimatedSpriteType.__init__)
    params = list(sig.parameters.keys())
    assert "texturefile" in params, "Missing parameter 'texturefile'"
    assert "animationRateFps" in params, "Missing parameter 'animationRateFps'"
    assert "looping" in params, "Missing parameter 'looping'"
    assert "name" in params, "Missing parameter 'name'"
    assert "playOnShow" in params, "Missing parameter 'playOnShow'"
    assert "noOfFrames" in params, "Missing parameter 'noOfFrames'"

def test_ck2gfx::animatedspritetype_has_texturefile():
    assert hasattr(ck2gfx::AnimatedSpriteType, "texturefile")
    descriptor = None
    for klass in ck2gfx::AnimatedSpriteType.__mro__:
        if "texturefile" in klass.__dict__:
            descriptor = klass.__dict__["texturefile"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::animatedspritetype_has_animationRateFps():
    assert hasattr(ck2gfx::AnimatedSpriteType, "animationRateFps")
    descriptor = None
    for klass in ck2gfx::AnimatedSpriteType.__mro__:
        if "animationRateFps" in klass.__dict__:
            descriptor = klass.__dict__["animationRateFps"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::animatedspritetype_has_looping():
    assert hasattr(ck2gfx::AnimatedSpriteType, "looping")
    descriptor = None
    for klass in ck2gfx::AnimatedSpriteType.__mro__:
        if "looping" in klass.__dict__:
            descriptor = klass.__dict__["looping"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::animatedspritetype_has_name():
    assert hasattr(ck2gfx::AnimatedSpriteType, "name")
    descriptor = None
    for klass in ck2gfx::AnimatedSpriteType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::animatedspritetype_has_playOnShow():
    assert hasattr(ck2gfx::AnimatedSpriteType, "playOnShow")
    descriptor = None
    for klass in ck2gfx::AnimatedSpriteType.__mro__:
        if "playOnShow" in klass.__dict__:
            descriptor = klass.__dict__["playOnShow"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::animatedspritetype_has_noOfFrames():
    assert hasattr(ck2gfx::AnimatedSpriteType, "noOfFrames")
    descriptor = None
    for klass in ck2gfx::AnimatedSpriteType.__mro__:
        if "noOfFrames" in klass.__dict__:
            descriptor = klass.__dict__["noOfFrames"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx::coordinates_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::Coordinates)


def test_ck2gfx::coordinates_constructor_exists():
    assert callable(ck2gfx::Coordinates.__init__)


def test_ck2gfx::coordinates_constructor_args():
    sig = inspect.signature(ck2gfx::Coordinates.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_ck2gfx::coordinates_has_x():
    assert hasattr(ck2gfx::Coordinates, "x")
    descriptor = None
    for klass in ck2gfx::Coordinates.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::coordinates_has_y():
    assert hasattr(ck2gfx::Coordinates, "y")
    descriptor = None
    for klass in ck2gfx::Coordinates.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx::colorratio_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::ColorRatio)


def test_ck2gfx::colorratio_constructor_exists():
    assert callable(ck2gfx::ColorRatio.__init__)


def test_ck2gfx::colorratio_constructor_args():
    sig = inspect.signature(ck2gfx::ColorRatio.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"
    assert "r" in params, "Missing parameter 'r'"
    assert "g" in params, "Missing parameter 'g'"

def test_ck2gfx::colorratio_has_b():
    assert hasattr(ck2gfx::ColorRatio, "b")
    descriptor = None
    for klass in ck2gfx::ColorRatio.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::colorratio_has_r():
    assert hasattr(ck2gfx::ColorRatio, "r")
    descriptor = None
    for klass in ck2gfx::ColorRatio.__mro__:
        if "r" in klass.__dict__:
            descriptor = klass.__dict__["r"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::colorratio_has_g():
    assert hasattr(ck2gfx::ColorRatio, "g")
    descriptor = None
    for klass in ck2gfx::ColorRatio.__mro__:
        if "g" in klass.__dict__:
            descriptor = klass.__dict__["g"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx::color_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::Color)


def test_ck2gfx::color_constructor_exists():
    assert callable(ck2gfx::Color.__init__)


def test_ck2gfx::color_constructor_args():
    sig = inspect.signature(ck2gfx::Color.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"
    assert "r" in params, "Missing parameter 'r'"
    assert "g" in params, "Missing parameter 'g'"

def test_ck2gfx::color_has_b():
    assert hasattr(ck2gfx::Color, "b")
    descriptor = None
    for klass in ck2gfx::Color.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::color_has_r():
    assert hasattr(ck2gfx::Color, "r")
    descriptor = None
    for klass in ck2gfx::Color.__mro__:
        if "r" in klass.__dict__:
            descriptor = klass.__dict__["r"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx::color_has_g():
    assert hasattr(ck2gfx::Color, "g")
    descriptor = None
    for klass in ck2gfx::Color.__mro__:
        if "g" in klass.__dict__:
            descriptor = klass.__dict__["g"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx::eobject_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::EObject)


def test_ck2gfx::eobject_constructor_exists():
    assert callable(ck2gfx::EObject.__init__)


def test_ck2gfx::eobject_constructor_args():
    sig = inspect.signature(ck2gfx::EObject.__init__)
    params = list(sig.parameters.keys())



def test_ck2gfx::model_is_not_abstract():
    assert not inspect.isabstract(ck2gfx::Model)


def test_ck2gfx::model_constructor_exists():
    assert callable(ck2gfx::Model.__init__)


def test_ck2gfx::model_constructor_args():
    sig = inspect.signature(ck2gfx::Model.__init__)
    params = list(sig.parameters.keys())


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
ck2gfx::Animation_strategy = st.builds(
    ck2gfx::Animation,
    name=
        safe_text,
    file=
        safe_text,
    defaultAnimationTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ck2gfx::EMFXActorType_strategy = st.builds(
    ck2gfx::EMFXActorType,
    actorFile=
        safe_text,
    attack=
        safe_text,
    move=
        safe_text,
    idle=
        safe_text,
    name=
        safe_text,
    scale=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    useAnimation=
        st.booleans(),
    scaleOnCullDistance=
        st.booleans(),
    cullDistance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ck2gfx::ColorCode_strategy = st.builds(
    ck2gfx::ColorCode,
    key=
        safe_text
)
ck2gfx::BitmapFont_strategy = st.builds(
    ck2gfx::BitmapFont,
    color=
        st.integers(),
    effect=
        st.booleans(),
    fontName=
        safe_text,
    name=
        safe_text
)
ck2gfx::BitmapFonts_strategy = st.builds(
    ck2gfx::BitmapFonts,
)
ck2gfx::ArrowType_strategy = st.builds(
    ck2gfx::ArrowType,
    effect=
        safe_text,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    size=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    endAt=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    textureFile=
        safe_text,
    name=
        safe_text,
    bodyTexture=
        safe_text,
    type=
        st.integers(),
    heading=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ck2gfx::Pdxmesh_strategy = st.builds(
    ck2gfx::Pdxmesh,
    name=
        safe_text,
    scaleOnCullDistance=
        st.booleans(),
    cullDistance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    actorFile=
        safe_text,
    scale=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ck2gfx::PortraitType_strategy = st.builds(
    ck2gfx::PortraitType,
    hairColorIndex=
        st.integers(),
    layers=
        safe_text,
    eyeColorIndex=
        st.integers(),
    name=
        safe_text,
    headgearThatHidesHair=
        st.integers(),
    effectFile=
        safe_text
)
ck2gfx::ObjectTypes_strategy = st.builds(
    ck2gfx::ObjectTypes,
)
ck2gfx::CoatOfArmsLayer_strategy = st.builds(
    ck2gfx::CoatOfArmsLayer,
    mask=
        safe_text,
    scale=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ck2gfx::CoatOfArmsType_strategy = st.builds(
    ck2gfx::CoatOfArmsType,
    effect=
        safe_text,
    mask=
        safe_text,
    name=
        safe_text,
    sealOverlay=
        safe_text,
    frame=
        safe_text
)
ck2gfx::LineChartType_strategy = st.builds(
    ck2gfx::LineChartType,
    lineWidth=
        st.integers(),
    name=
        safe_text
)
ck2gfx::MaskedShieldType_strategy = st.builds(
    ck2gfx::MaskedShieldType,
    textureFile2=
        safe_text,
    textureFile1=
        safe_text,
    clickSound=
        safe_text,
    name=
        safe_text,
    allwaysTransparent=
        st.booleans(),
    effectFile=
        safe_text
)
ck2gfx::SpriteType_strategy = st.builds(
    ck2gfx::SpriteType,
    noRefCount=
        st.booleans(),
    effectFile=
        safe_text,
    clickSound=
        safe_text,
    name=
        safe_text,
    loadType=
        safe_text,
    transparenceCheck=
        st.booleans(),
    textureFile=
        safe_text,
    canBeLowres=
        st.booleans(),
    allwaysTransparent=
        st.booleans(),
    noOfFrames=
        st.integers()
)
ck2gfx::SpriteTypes_strategy = st.builds(
    ck2gfx::SpriteTypes,
)
ck2gfx::ProgressbarType_strategy = st.builds(
    ck2gfx::ProgressbarType,
    loadType=
        safe_text,
    maxValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    effectFile=
        safe_text,
    textureFile2=
        safe_text,
    noRefCount=
        st.booleans(),
    allwaysTransparent=
        st.booleans(),
    textureFile1=
        safe_text,
    horizontal=
        st.booleans()
)
ck2gfx::CorneredTileSpriteType_strategy = st.builds(
    ck2gfx::CorneredTileSpriteType,
    texturefile=
        safe_text,
    name=
        safe_text,
    tilingCenter=
        st.booleans(),
    noRefCount=
        st.booleans(),
    allwaysTransparent=
        st.booleans(),
    loadType=
        safe_text
)
ck2gfx::AnimatedSpriteType_strategy = st.builds(
    ck2gfx::AnimatedSpriteType,
    texturefile=
        safe_text,
    animationRateFps=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    looping=
        st.booleans(),
    name=
        safe_text,
    playOnShow=
        st.booleans(),
    noOfFrames=
        st.integers()
)
ck2gfx::Coordinates_strategy = st.builds(
    ck2gfx::Coordinates,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ck2gfx::ColorRatio_strategy = st.builds(
    ck2gfx::ColorRatio,
    b=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    r=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    g=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ck2gfx::Color_strategy = st.builds(
    ck2gfx::Color,
    b=
        st.integers(),
    r=
        st.integers(),
    g=
        st.integers()
)
ck2gfx::EObject_strategy = st.builds(
    ck2gfx::EObject,
)
ck2gfx::Model_strategy = st.builds(
    ck2gfx::Model,
)

@given(instance=ck2gfx::Animation_strategy)
@settings(max_examples=50)
def test_ck2gfx::animation_instantiation(instance):
    assert isinstance(instance, ck2gfx::Animation)

@given(instance=ck2gfx::Animation_strategy)
def test_ck2gfx::animation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ck2gfx::Animation_strategy)
def test_ck2gfx::animation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ck2gfx::Animation_strategy)
def test_ck2gfx::animation_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=ck2gfx::Animation_strategy)
def test_ck2gfx::animation_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=ck2gfx::Animation_strategy)
def test_ck2gfx::animation_defaultAnimationTime_type(instance):
    assert isinstance(instance.defaultAnimationTime, float)


@given(instance=ck2gfx::Animation_strategy)
def test_ck2gfx::animation_defaultAnimationTime_setter(instance):
    original = instance.defaultAnimationTime
    instance.defaultAnimationTime = original
    assert instance.defaultAnimationTime == original

@given(instance=ck2gfx::EMFXActorType_strategy)
@settings(max_examples=50)
def test_ck2gfx::emfxactortype_instantiation(instance):
    assert isinstance(instance, ck2gfx::EMFXActorType)

@given(instance=ck2gfx::EMFXActorType_strategy)
def test_ck2gfx::emfxactortype_actorFile_type(instance):
    assert isinstance(instance.actorFile, str)


@given(instance=ck2gfx::EMFXActorType_strategy)
def test_ck2gfx::emfxactortype_actorFile_setter(instance):
    original = instance.actorFile
    instance.actorFile = original
    assert instance.actorFile == original

@given(instance=ck2gfx::EMFXActorType_strategy)
def test_ck2gfx::emfxactortype_attack_type(instance):
    assert isinstance(instance.attack, str)


@given(instance=ck2gfx::EMFXActorType_strategy)
def test_ck2gfx::emfxactortype_attack_setter(instance):
    original = instance.attack
    instance.attack = original
    assert instance.attack == original

@given(instance=ck2gfx::EMFXActorType_strategy)
def test_ck2gfx::emfxactortype_move_type(instance):
    assert isinstance(instance.move, str)


@given(instance=ck2gfx::EMFXActorType_strategy)
def test_ck2gfx::emfxactortype_move_setter(instance):
    original = instance.move
    instance.move = original
    assert instance.move == original

@given(instance=ck2gfx::EMFXActorType_strategy)
def test_ck2gfx::emfxactortype_idle_type(instance):
    assert isinstance(instance.idle, str)


@given(instance=ck2gfx::EMFXActorType_strategy)
def test_ck2gfx::emfxactortype_idle_setter(instance):
    original = instance.idle
    instance.idle = original
    assert instance.idle == original

@given(instance=ck2gfx::EMFXActorType_strategy)
def test_ck2gfx::emfxactortype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ck2gfx::EMFXActorType_strategy)
def test_ck2gfx::emfxactortype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ck2gfx::EMFXActorType_strategy)
def test_ck2gfx::emfxactortype_scale_type(instance):
    assert isinstance(instance.scale, float)


@given(instance=ck2gfx::EMFXActorType_strategy)
def test_ck2gfx::emfxactortype_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=ck2gfx::EMFXActorType_strategy)
def test_ck2gfx::emfxactortype_useAnimation_type(instance):
    assert isinstance(instance.useAnimation, bool)


@given(instance=ck2gfx::EMFXActorType_strategy)
def test_ck2gfx::emfxactortype_useAnimation_setter(instance):
    original = instance.useAnimation
    instance.useAnimation = original
    assert instance.useAnimation == original

@given(instance=ck2gfx::EMFXActorType_strategy)
def test_ck2gfx::emfxactortype_scaleOnCullDistance_type(instance):
    assert isinstance(instance.scaleOnCullDistance, bool)


@given(instance=ck2gfx::EMFXActorType_strategy)
def test_ck2gfx::emfxactortype_scaleOnCullDistance_setter(instance):
    original = instance.scaleOnCullDistance
    instance.scaleOnCullDistance = original
    assert instance.scaleOnCullDistance == original

@given(instance=ck2gfx::EMFXActorType_strategy)
def test_ck2gfx::emfxactortype_cullDistance_type(instance):
    assert isinstance(instance.cullDistance, float)


@given(instance=ck2gfx::EMFXActorType_strategy)
def test_ck2gfx::emfxactortype_cullDistance_setter(instance):
    original = instance.cullDistance
    instance.cullDistance = original
    assert instance.cullDistance == original

@given(instance=ck2gfx::ColorCode_strategy)
@settings(max_examples=50)
def test_ck2gfx::colorcode_instantiation(instance):
    assert isinstance(instance, ck2gfx::ColorCode)

@given(instance=ck2gfx::ColorCode_strategy)
def test_ck2gfx::colorcode_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=ck2gfx::ColorCode_strategy)
def test_ck2gfx::colorcode_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=ck2gfx::BitmapFont_strategy)
@settings(max_examples=50)
def test_ck2gfx::bitmapfont_instantiation(instance):
    assert isinstance(instance, ck2gfx::BitmapFont)

@given(instance=ck2gfx::BitmapFont_strategy)
def test_ck2gfx::bitmapfont_color_type(instance):
    assert isinstance(instance.color, int)


@given(instance=ck2gfx::BitmapFont_strategy)
def test_ck2gfx::bitmapfont_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=ck2gfx::BitmapFont_strategy)
def test_ck2gfx::bitmapfont_effect_type(instance):
    assert isinstance(instance.effect, bool)


@given(instance=ck2gfx::BitmapFont_strategy)
def test_ck2gfx::bitmapfont_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=ck2gfx::BitmapFont_strategy)
def test_ck2gfx::bitmapfont_fontName_type(instance):
    assert isinstance(instance.fontName, str)


@given(instance=ck2gfx::BitmapFont_strategy)
def test_ck2gfx::bitmapfont_fontName_setter(instance):
    original = instance.fontName
    instance.fontName = original
    assert instance.fontName == original

@given(instance=ck2gfx::BitmapFont_strategy)
def test_ck2gfx::bitmapfont_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ck2gfx::BitmapFont_strategy)
def test_ck2gfx::bitmapfont_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ck2gfx::BitmapFonts_strategy)
@settings(max_examples=50)
def test_ck2gfx::bitmapfonts_instantiation(instance):
    assert isinstance(instance, ck2gfx::BitmapFonts)

@given(instance=ck2gfx::ArrowType_strategy)
@settings(max_examples=50)
def test_ck2gfx::arrowtype_instantiation(instance):
    assert isinstance(instance, ck2gfx::ArrowType)

@given(instance=ck2gfx::ArrowType_strategy)
def test_ck2gfx::arrowtype_effect_type(instance):
    assert isinstance(instance.effect, str)


@given(instance=ck2gfx::ArrowType_strategy)
def test_ck2gfx::arrowtype_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=ck2gfx::ArrowType_strategy)
def test_ck2gfx::arrowtype_height_type(instance):
    assert isinstance(instance.height, float)


@given(instance=ck2gfx::ArrowType_strategy)
def test_ck2gfx::arrowtype_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=ck2gfx::ArrowType_strategy)
def test_ck2gfx::arrowtype_size_type(instance):
    assert isinstance(instance.size, float)


@given(instance=ck2gfx::ArrowType_strategy)
def test_ck2gfx::arrowtype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=ck2gfx::ArrowType_strategy)
def test_ck2gfx::arrowtype_endAt_type(instance):
    assert isinstance(instance.endAt, float)


@given(instance=ck2gfx::ArrowType_strategy)
def test_ck2gfx::arrowtype_endAt_setter(instance):
    original = instance.endAt
    instance.endAt = original
    assert instance.endAt == original

@given(instance=ck2gfx::ArrowType_strategy)
def test_ck2gfx::arrowtype_textureFile_type(instance):
    assert isinstance(instance.textureFile, str)


@given(instance=ck2gfx::ArrowType_strategy)
def test_ck2gfx::arrowtype_textureFile_setter(instance):
    original = instance.textureFile
    instance.textureFile = original
    assert instance.textureFile == original

@given(instance=ck2gfx::ArrowType_strategy)
def test_ck2gfx::arrowtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ck2gfx::ArrowType_strategy)
def test_ck2gfx::arrowtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ck2gfx::ArrowType_strategy)
def test_ck2gfx::arrowtype_bodyTexture_type(instance):
    assert isinstance(instance.bodyTexture, str)


@given(instance=ck2gfx::ArrowType_strategy)
def test_ck2gfx::arrowtype_bodyTexture_setter(instance):
    original = instance.bodyTexture
    instance.bodyTexture = original
    assert instance.bodyTexture == original

@given(instance=ck2gfx::ArrowType_strategy)
def test_ck2gfx::arrowtype_type_type(instance):
    assert isinstance(instance.type, int)


@given(instance=ck2gfx::ArrowType_strategy)
def test_ck2gfx::arrowtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ck2gfx::ArrowType_strategy)
def test_ck2gfx::arrowtype_heading_type(instance):
    assert isinstance(instance.heading, float)


@given(instance=ck2gfx::ArrowType_strategy)
def test_ck2gfx::arrowtype_heading_setter(instance):
    original = instance.heading
    instance.heading = original
    assert instance.heading == original

@given(instance=ck2gfx::Pdxmesh_strategy)
@settings(max_examples=50)
def test_ck2gfx::pdxmesh_instantiation(instance):
    assert isinstance(instance, ck2gfx::Pdxmesh)

@given(instance=ck2gfx::Pdxmesh_strategy)
def test_ck2gfx::pdxmesh_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ck2gfx::Pdxmesh_strategy)
def test_ck2gfx::pdxmesh_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ck2gfx::Pdxmesh_strategy)
def test_ck2gfx::pdxmesh_scaleOnCullDistance_type(instance):
    assert isinstance(instance.scaleOnCullDistance, bool)


@given(instance=ck2gfx::Pdxmesh_strategy)
def test_ck2gfx::pdxmesh_scaleOnCullDistance_setter(instance):
    original = instance.scaleOnCullDistance
    instance.scaleOnCullDistance = original
    assert instance.scaleOnCullDistance == original

@given(instance=ck2gfx::Pdxmesh_strategy)
def test_ck2gfx::pdxmesh_cullDistance_type(instance):
    assert isinstance(instance.cullDistance, float)


@given(instance=ck2gfx::Pdxmesh_strategy)
def test_ck2gfx::pdxmesh_cullDistance_setter(instance):
    original = instance.cullDistance
    instance.cullDistance = original
    assert instance.cullDistance == original

@given(instance=ck2gfx::Pdxmesh_strategy)
def test_ck2gfx::pdxmesh_actorFile_type(instance):
    assert isinstance(instance.actorFile, str)


@given(instance=ck2gfx::Pdxmesh_strategy)
def test_ck2gfx::pdxmesh_actorFile_setter(instance):
    original = instance.actorFile
    instance.actorFile = original
    assert instance.actorFile == original

@given(instance=ck2gfx::Pdxmesh_strategy)
def test_ck2gfx::pdxmesh_scale_type(instance):
    assert isinstance(instance.scale, float)


@given(instance=ck2gfx::Pdxmesh_strategy)
def test_ck2gfx::pdxmesh_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=ck2gfx::PortraitType_strategy)
@settings(max_examples=50)
def test_ck2gfx::portraittype_instantiation(instance):
    assert isinstance(instance, ck2gfx::PortraitType)

@given(instance=ck2gfx::PortraitType_strategy)
def test_ck2gfx::portraittype_hairColorIndex_type(instance):
    assert isinstance(instance.hairColorIndex, int)


@given(instance=ck2gfx::PortraitType_strategy)
def test_ck2gfx::portraittype_hairColorIndex_setter(instance):
    original = instance.hairColorIndex
    instance.hairColorIndex = original
    assert instance.hairColorIndex == original

@given(instance=ck2gfx::PortraitType_strategy)
def test_ck2gfx::portraittype_layers_type(instance):
    assert isinstance(instance.layers, str)


@given(instance=ck2gfx::PortraitType_strategy)
def test_ck2gfx::portraittype_layers_setter(instance):
    original = instance.layers
    instance.layers = original
    assert instance.layers == original

@given(instance=ck2gfx::PortraitType_strategy)
def test_ck2gfx::portraittype_eyeColorIndex_type(instance):
    assert isinstance(instance.eyeColorIndex, int)


@given(instance=ck2gfx::PortraitType_strategy)
def test_ck2gfx::portraittype_eyeColorIndex_setter(instance):
    original = instance.eyeColorIndex
    instance.eyeColorIndex = original
    assert instance.eyeColorIndex == original

@given(instance=ck2gfx::PortraitType_strategy)
def test_ck2gfx::portraittype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ck2gfx::PortraitType_strategy)
def test_ck2gfx::portraittype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ck2gfx::PortraitType_strategy)
def test_ck2gfx::portraittype_headgearThatHidesHair_type(instance):
    assert isinstance(instance.headgearThatHidesHair, int)


@given(instance=ck2gfx::PortraitType_strategy)
def test_ck2gfx::portraittype_headgearThatHidesHair_setter(instance):
    original = instance.headgearThatHidesHair
    instance.headgearThatHidesHair = original
    assert instance.headgearThatHidesHair == original

@given(instance=ck2gfx::PortraitType_strategy)
def test_ck2gfx::portraittype_effectFile_type(instance):
    assert isinstance(instance.effectFile, str)


@given(instance=ck2gfx::PortraitType_strategy)
def test_ck2gfx::portraittype_effectFile_setter(instance):
    original = instance.effectFile
    instance.effectFile = original
    assert instance.effectFile == original

@given(instance=ck2gfx::ObjectTypes_strategy)
@settings(max_examples=50)
def test_ck2gfx::objecttypes_instantiation(instance):
    assert isinstance(instance, ck2gfx::ObjectTypes)

@given(instance=ck2gfx::CoatOfArmsLayer_strategy)
@settings(max_examples=50)
def test_ck2gfx::coatofarmslayer_instantiation(instance):
    assert isinstance(instance, ck2gfx::CoatOfArmsLayer)

@given(instance=ck2gfx::CoatOfArmsLayer_strategy)
def test_ck2gfx::coatofarmslayer_mask_type(instance):
    assert isinstance(instance.mask, str)


@given(instance=ck2gfx::CoatOfArmsLayer_strategy)
def test_ck2gfx::coatofarmslayer_mask_setter(instance):
    original = instance.mask
    instance.mask = original
    assert instance.mask == original

@given(instance=ck2gfx::CoatOfArmsLayer_strategy)
def test_ck2gfx::coatofarmslayer_scale_type(instance):
    assert isinstance(instance.scale, float)


@given(instance=ck2gfx::CoatOfArmsLayer_strategy)
def test_ck2gfx::coatofarmslayer_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=ck2gfx::CoatOfArmsType_strategy)
@settings(max_examples=50)
def test_ck2gfx::coatofarmstype_instantiation(instance):
    assert isinstance(instance, ck2gfx::CoatOfArmsType)

@given(instance=ck2gfx::CoatOfArmsType_strategy)
def test_ck2gfx::coatofarmstype_effect_type(instance):
    assert isinstance(instance.effect, str)


@given(instance=ck2gfx::CoatOfArmsType_strategy)
def test_ck2gfx::coatofarmstype_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=ck2gfx::CoatOfArmsType_strategy)
def test_ck2gfx::coatofarmstype_mask_type(instance):
    assert isinstance(instance.mask, str)


@given(instance=ck2gfx::CoatOfArmsType_strategy)
def test_ck2gfx::coatofarmstype_mask_setter(instance):
    original = instance.mask
    instance.mask = original
    assert instance.mask == original

@given(instance=ck2gfx::CoatOfArmsType_strategy)
def test_ck2gfx::coatofarmstype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ck2gfx::CoatOfArmsType_strategy)
def test_ck2gfx::coatofarmstype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ck2gfx::CoatOfArmsType_strategy)
def test_ck2gfx::coatofarmstype_sealOverlay_type(instance):
    assert isinstance(instance.sealOverlay, str)


@given(instance=ck2gfx::CoatOfArmsType_strategy)
def test_ck2gfx::coatofarmstype_sealOverlay_setter(instance):
    original = instance.sealOverlay
    instance.sealOverlay = original
    assert instance.sealOverlay == original

@given(instance=ck2gfx::CoatOfArmsType_strategy)
def test_ck2gfx::coatofarmstype_frame_type(instance):
    assert isinstance(instance.frame, str)


@given(instance=ck2gfx::CoatOfArmsType_strategy)
def test_ck2gfx::coatofarmstype_frame_setter(instance):
    original = instance.frame
    instance.frame = original
    assert instance.frame == original

@given(instance=ck2gfx::LineChartType_strategy)
@settings(max_examples=50)
def test_ck2gfx::linecharttype_instantiation(instance):
    assert isinstance(instance, ck2gfx::LineChartType)

@given(instance=ck2gfx::LineChartType_strategy)
def test_ck2gfx::linecharttype_lineWidth_type(instance):
    assert isinstance(instance.lineWidth, int)


@given(instance=ck2gfx::LineChartType_strategy)
def test_ck2gfx::linecharttype_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original

@given(instance=ck2gfx::LineChartType_strategy)
def test_ck2gfx::linecharttype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ck2gfx::LineChartType_strategy)
def test_ck2gfx::linecharttype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ck2gfx::MaskedShieldType_strategy)
@settings(max_examples=50)
def test_ck2gfx::maskedshieldtype_instantiation(instance):
    assert isinstance(instance, ck2gfx::MaskedShieldType)

@given(instance=ck2gfx::MaskedShieldType_strategy)
def test_ck2gfx::maskedshieldtype_textureFile2_type(instance):
    assert isinstance(instance.textureFile2, str)


@given(instance=ck2gfx::MaskedShieldType_strategy)
def test_ck2gfx::maskedshieldtype_textureFile2_setter(instance):
    original = instance.textureFile2
    instance.textureFile2 = original
    assert instance.textureFile2 == original

@given(instance=ck2gfx::MaskedShieldType_strategy)
def test_ck2gfx::maskedshieldtype_textureFile1_type(instance):
    assert isinstance(instance.textureFile1, str)


@given(instance=ck2gfx::MaskedShieldType_strategy)
def test_ck2gfx::maskedshieldtype_textureFile1_setter(instance):
    original = instance.textureFile1
    instance.textureFile1 = original
    assert instance.textureFile1 == original

@given(instance=ck2gfx::MaskedShieldType_strategy)
def test_ck2gfx::maskedshieldtype_clickSound_type(instance):
    assert isinstance(instance.clickSound, str)


@given(instance=ck2gfx::MaskedShieldType_strategy)
def test_ck2gfx::maskedshieldtype_clickSound_setter(instance):
    original = instance.clickSound
    instance.clickSound = original
    assert instance.clickSound == original

@given(instance=ck2gfx::MaskedShieldType_strategy)
def test_ck2gfx::maskedshieldtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ck2gfx::MaskedShieldType_strategy)
def test_ck2gfx::maskedshieldtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ck2gfx::MaskedShieldType_strategy)
def test_ck2gfx::maskedshieldtype_allwaysTransparent_type(instance):
    assert isinstance(instance.allwaysTransparent, bool)


@given(instance=ck2gfx::MaskedShieldType_strategy)
def test_ck2gfx::maskedshieldtype_allwaysTransparent_setter(instance):
    original = instance.allwaysTransparent
    instance.allwaysTransparent = original
    assert instance.allwaysTransparent == original

@given(instance=ck2gfx::MaskedShieldType_strategy)
def test_ck2gfx::maskedshieldtype_effectFile_type(instance):
    assert isinstance(instance.effectFile, str)


@given(instance=ck2gfx::MaskedShieldType_strategy)
def test_ck2gfx::maskedshieldtype_effectFile_setter(instance):
    original = instance.effectFile
    instance.effectFile = original
    assert instance.effectFile == original

@given(instance=ck2gfx::SpriteType_strategy)
@settings(max_examples=50)
def test_ck2gfx::spritetype_instantiation(instance):
    assert isinstance(instance, ck2gfx::SpriteType)

@given(instance=ck2gfx::SpriteType_strategy)
def test_ck2gfx::spritetype_noRefCount_type(instance):
    assert isinstance(instance.noRefCount, bool)


@given(instance=ck2gfx::SpriteType_strategy)
def test_ck2gfx::spritetype_noRefCount_setter(instance):
    original = instance.noRefCount
    instance.noRefCount = original
    assert instance.noRefCount == original

@given(instance=ck2gfx::SpriteType_strategy)
def test_ck2gfx::spritetype_effectFile_type(instance):
    assert isinstance(instance.effectFile, str)


@given(instance=ck2gfx::SpriteType_strategy)
def test_ck2gfx::spritetype_effectFile_setter(instance):
    original = instance.effectFile
    instance.effectFile = original
    assert instance.effectFile == original

@given(instance=ck2gfx::SpriteType_strategy)
def test_ck2gfx::spritetype_clickSound_type(instance):
    assert isinstance(instance.clickSound, str)


@given(instance=ck2gfx::SpriteType_strategy)
def test_ck2gfx::spritetype_clickSound_setter(instance):
    original = instance.clickSound
    instance.clickSound = original
    assert instance.clickSound == original

@given(instance=ck2gfx::SpriteType_strategy)
def test_ck2gfx::spritetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ck2gfx::SpriteType_strategy)
def test_ck2gfx::spritetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ck2gfx::SpriteType_strategy)
def test_ck2gfx::spritetype_loadType_type(instance):
    assert isinstance(instance.loadType, str)


@given(instance=ck2gfx::SpriteType_strategy)
def test_ck2gfx::spritetype_loadType_setter(instance):
    original = instance.loadType
    instance.loadType = original
    assert instance.loadType == original

@given(instance=ck2gfx::SpriteType_strategy)
def test_ck2gfx::spritetype_transparenceCheck_type(instance):
    assert isinstance(instance.transparenceCheck, bool)


@given(instance=ck2gfx::SpriteType_strategy)
def test_ck2gfx::spritetype_transparenceCheck_setter(instance):
    original = instance.transparenceCheck
    instance.transparenceCheck = original
    assert instance.transparenceCheck == original

@given(instance=ck2gfx::SpriteType_strategy)
def test_ck2gfx::spritetype_textureFile_type(instance):
    assert isinstance(instance.textureFile, str)


@given(instance=ck2gfx::SpriteType_strategy)
def test_ck2gfx::spritetype_textureFile_setter(instance):
    original = instance.textureFile
    instance.textureFile = original
    assert instance.textureFile == original

@given(instance=ck2gfx::SpriteType_strategy)
def test_ck2gfx::spritetype_canBeLowres_type(instance):
    assert isinstance(instance.canBeLowres, bool)


@given(instance=ck2gfx::SpriteType_strategy)
def test_ck2gfx::spritetype_canBeLowres_setter(instance):
    original = instance.canBeLowres
    instance.canBeLowres = original
    assert instance.canBeLowres == original

@given(instance=ck2gfx::SpriteType_strategy)
def test_ck2gfx::spritetype_allwaysTransparent_type(instance):
    assert isinstance(instance.allwaysTransparent, bool)


@given(instance=ck2gfx::SpriteType_strategy)
def test_ck2gfx::spritetype_allwaysTransparent_setter(instance):
    original = instance.allwaysTransparent
    instance.allwaysTransparent = original
    assert instance.allwaysTransparent == original

@given(instance=ck2gfx::SpriteType_strategy)
def test_ck2gfx::spritetype_noOfFrames_type(instance):
    assert isinstance(instance.noOfFrames, int)


@given(instance=ck2gfx::SpriteType_strategy)
def test_ck2gfx::spritetype_noOfFrames_setter(instance):
    original = instance.noOfFrames
    instance.noOfFrames = original
    assert instance.noOfFrames == original

@given(instance=ck2gfx::SpriteTypes_strategy)
@settings(max_examples=50)
def test_ck2gfx::spritetypes_instantiation(instance):
    assert isinstance(instance, ck2gfx::SpriteTypes)

@given(instance=ck2gfx::ProgressbarType_strategy)
@settings(max_examples=50)
def test_ck2gfx::progressbartype_instantiation(instance):
    assert isinstance(instance, ck2gfx::ProgressbarType)

@given(instance=ck2gfx::ProgressbarType_strategy)
def test_ck2gfx::progressbartype_loadType_type(instance):
    assert isinstance(instance.loadType, str)


@given(instance=ck2gfx::ProgressbarType_strategy)
def test_ck2gfx::progressbartype_loadType_setter(instance):
    original = instance.loadType
    instance.loadType = original
    assert instance.loadType == original

@given(instance=ck2gfx::ProgressbarType_strategy)
def test_ck2gfx::progressbartype_maxValue_type(instance):
    assert isinstance(instance.maxValue, float)


@given(instance=ck2gfx::ProgressbarType_strategy)
def test_ck2gfx::progressbartype_maxValue_setter(instance):
    original = instance.maxValue
    instance.maxValue = original
    assert instance.maxValue == original

@given(instance=ck2gfx::ProgressbarType_strategy)
def test_ck2gfx::progressbartype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ck2gfx::ProgressbarType_strategy)
def test_ck2gfx::progressbartype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ck2gfx::ProgressbarType_strategy)
def test_ck2gfx::progressbartype_effectFile_type(instance):
    assert isinstance(instance.effectFile, str)


@given(instance=ck2gfx::ProgressbarType_strategy)
def test_ck2gfx::progressbartype_effectFile_setter(instance):
    original = instance.effectFile
    instance.effectFile = original
    assert instance.effectFile == original

@given(instance=ck2gfx::ProgressbarType_strategy)
def test_ck2gfx::progressbartype_textureFile2_type(instance):
    assert isinstance(instance.textureFile2, str)


@given(instance=ck2gfx::ProgressbarType_strategy)
def test_ck2gfx::progressbartype_textureFile2_setter(instance):
    original = instance.textureFile2
    instance.textureFile2 = original
    assert instance.textureFile2 == original

@given(instance=ck2gfx::ProgressbarType_strategy)
def test_ck2gfx::progressbartype_noRefCount_type(instance):
    assert isinstance(instance.noRefCount, bool)


@given(instance=ck2gfx::ProgressbarType_strategy)
def test_ck2gfx::progressbartype_noRefCount_setter(instance):
    original = instance.noRefCount
    instance.noRefCount = original
    assert instance.noRefCount == original

@given(instance=ck2gfx::ProgressbarType_strategy)
def test_ck2gfx::progressbartype_allwaysTransparent_type(instance):
    assert isinstance(instance.allwaysTransparent, bool)


@given(instance=ck2gfx::ProgressbarType_strategy)
def test_ck2gfx::progressbartype_allwaysTransparent_setter(instance):
    original = instance.allwaysTransparent
    instance.allwaysTransparent = original
    assert instance.allwaysTransparent == original

@given(instance=ck2gfx::ProgressbarType_strategy)
def test_ck2gfx::progressbartype_textureFile1_type(instance):
    assert isinstance(instance.textureFile1, str)


@given(instance=ck2gfx::ProgressbarType_strategy)
def test_ck2gfx::progressbartype_textureFile1_setter(instance):
    original = instance.textureFile1
    instance.textureFile1 = original
    assert instance.textureFile1 == original

@given(instance=ck2gfx::ProgressbarType_strategy)
def test_ck2gfx::progressbartype_horizontal_type(instance):
    assert isinstance(instance.horizontal, bool)


@given(instance=ck2gfx::ProgressbarType_strategy)
def test_ck2gfx::progressbartype_horizontal_setter(instance):
    original = instance.horizontal
    instance.horizontal = original
    assert instance.horizontal == original

@given(instance=ck2gfx::CorneredTileSpriteType_strategy)
@settings(max_examples=50)
def test_ck2gfx::corneredtilespritetype_instantiation(instance):
    assert isinstance(instance, ck2gfx::CorneredTileSpriteType)

@given(instance=ck2gfx::CorneredTileSpriteType_strategy)
def test_ck2gfx::corneredtilespritetype_texturefile_type(instance):
    assert isinstance(instance.texturefile, str)


@given(instance=ck2gfx::CorneredTileSpriteType_strategy)
def test_ck2gfx::corneredtilespritetype_texturefile_setter(instance):
    original = instance.texturefile
    instance.texturefile = original
    assert instance.texturefile == original

@given(instance=ck2gfx::CorneredTileSpriteType_strategy)
def test_ck2gfx::corneredtilespritetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ck2gfx::CorneredTileSpriteType_strategy)
def test_ck2gfx::corneredtilespritetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ck2gfx::CorneredTileSpriteType_strategy)
def test_ck2gfx::corneredtilespritetype_tilingCenter_type(instance):
    assert isinstance(instance.tilingCenter, bool)


@given(instance=ck2gfx::CorneredTileSpriteType_strategy)
def test_ck2gfx::corneredtilespritetype_tilingCenter_setter(instance):
    original = instance.tilingCenter
    instance.tilingCenter = original
    assert instance.tilingCenter == original

@given(instance=ck2gfx::CorneredTileSpriteType_strategy)
def test_ck2gfx::corneredtilespritetype_noRefCount_type(instance):
    assert isinstance(instance.noRefCount, bool)


@given(instance=ck2gfx::CorneredTileSpriteType_strategy)
def test_ck2gfx::corneredtilespritetype_noRefCount_setter(instance):
    original = instance.noRefCount
    instance.noRefCount = original
    assert instance.noRefCount == original

@given(instance=ck2gfx::CorneredTileSpriteType_strategy)
def test_ck2gfx::corneredtilespritetype_allwaysTransparent_type(instance):
    assert isinstance(instance.allwaysTransparent, bool)


@given(instance=ck2gfx::CorneredTileSpriteType_strategy)
def test_ck2gfx::corneredtilespritetype_allwaysTransparent_setter(instance):
    original = instance.allwaysTransparent
    instance.allwaysTransparent = original
    assert instance.allwaysTransparent == original

@given(instance=ck2gfx::CorneredTileSpriteType_strategy)
def test_ck2gfx::corneredtilespritetype_loadType_type(instance):
    assert isinstance(instance.loadType, str)


@given(instance=ck2gfx::CorneredTileSpriteType_strategy)
def test_ck2gfx::corneredtilespritetype_loadType_setter(instance):
    original = instance.loadType
    instance.loadType = original
    assert instance.loadType == original

@given(instance=ck2gfx::AnimatedSpriteType_strategy)
@settings(max_examples=50)
def test_ck2gfx::animatedspritetype_instantiation(instance):
    assert isinstance(instance, ck2gfx::AnimatedSpriteType)

@given(instance=ck2gfx::AnimatedSpriteType_strategy)
def test_ck2gfx::animatedspritetype_texturefile_type(instance):
    assert isinstance(instance.texturefile, str)


@given(instance=ck2gfx::AnimatedSpriteType_strategy)
def test_ck2gfx::animatedspritetype_texturefile_setter(instance):
    original = instance.texturefile
    instance.texturefile = original
    assert instance.texturefile == original

@given(instance=ck2gfx::AnimatedSpriteType_strategy)
def test_ck2gfx::animatedspritetype_animationRateFps_type(instance):
    assert isinstance(instance.animationRateFps, float)


@given(instance=ck2gfx::AnimatedSpriteType_strategy)
def test_ck2gfx::animatedspritetype_animationRateFps_setter(instance):
    original = instance.animationRateFps
    instance.animationRateFps = original
    assert instance.animationRateFps == original

@given(instance=ck2gfx::AnimatedSpriteType_strategy)
def test_ck2gfx::animatedspritetype_looping_type(instance):
    assert isinstance(instance.looping, bool)


@given(instance=ck2gfx::AnimatedSpriteType_strategy)
def test_ck2gfx::animatedspritetype_looping_setter(instance):
    original = instance.looping
    instance.looping = original
    assert instance.looping == original

@given(instance=ck2gfx::AnimatedSpriteType_strategy)
def test_ck2gfx::animatedspritetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ck2gfx::AnimatedSpriteType_strategy)
def test_ck2gfx::animatedspritetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ck2gfx::AnimatedSpriteType_strategy)
def test_ck2gfx::animatedspritetype_playOnShow_type(instance):
    assert isinstance(instance.playOnShow, bool)


@given(instance=ck2gfx::AnimatedSpriteType_strategy)
def test_ck2gfx::animatedspritetype_playOnShow_setter(instance):
    original = instance.playOnShow
    instance.playOnShow = original
    assert instance.playOnShow == original

@given(instance=ck2gfx::AnimatedSpriteType_strategy)
def test_ck2gfx::animatedspritetype_noOfFrames_type(instance):
    assert isinstance(instance.noOfFrames, int)


@given(instance=ck2gfx::AnimatedSpriteType_strategy)
def test_ck2gfx::animatedspritetype_noOfFrames_setter(instance):
    original = instance.noOfFrames
    instance.noOfFrames = original
    assert instance.noOfFrames == original

@given(instance=ck2gfx::Coordinates_strategy)
@settings(max_examples=50)
def test_ck2gfx::coordinates_instantiation(instance):
    assert isinstance(instance, ck2gfx::Coordinates)

@given(instance=ck2gfx::Coordinates_strategy)
def test_ck2gfx::coordinates_x_type(instance):
    assert isinstance(instance.x, float)


@given(instance=ck2gfx::Coordinates_strategy)
def test_ck2gfx::coordinates_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=ck2gfx::Coordinates_strategy)
def test_ck2gfx::coordinates_y_type(instance):
    assert isinstance(instance.y, float)


@given(instance=ck2gfx::Coordinates_strategy)
def test_ck2gfx::coordinates_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=ck2gfx::ColorRatio_strategy)
@settings(max_examples=50)
def test_ck2gfx::colorratio_instantiation(instance):
    assert isinstance(instance, ck2gfx::ColorRatio)

@given(instance=ck2gfx::ColorRatio_strategy)
def test_ck2gfx::colorratio_b_type(instance):
    assert isinstance(instance.b, float)


@given(instance=ck2gfx::ColorRatio_strategy)
def test_ck2gfx::colorratio_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=ck2gfx::ColorRatio_strategy)
def test_ck2gfx::colorratio_r_type(instance):
    assert isinstance(instance.r, float)


@given(instance=ck2gfx::ColorRatio_strategy)
def test_ck2gfx::colorratio_r_setter(instance):
    original = instance.r
    instance.r = original
    assert instance.r == original

@given(instance=ck2gfx::ColorRatio_strategy)
def test_ck2gfx::colorratio_g_type(instance):
    assert isinstance(instance.g, float)


@given(instance=ck2gfx::ColorRatio_strategy)
def test_ck2gfx::colorratio_g_setter(instance):
    original = instance.g
    instance.g = original
    assert instance.g == original

@given(instance=ck2gfx::Color_strategy)
@settings(max_examples=50)
def test_ck2gfx::color_instantiation(instance):
    assert isinstance(instance, ck2gfx::Color)

@given(instance=ck2gfx::Color_strategy)
def test_ck2gfx::color_b_type(instance):
    assert isinstance(instance.b, int)


@given(instance=ck2gfx::Color_strategy)
def test_ck2gfx::color_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=ck2gfx::Color_strategy)
def test_ck2gfx::color_r_type(instance):
    assert isinstance(instance.r, int)


@given(instance=ck2gfx::Color_strategy)
def test_ck2gfx::color_r_setter(instance):
    original = instance.r
    instance.r = original
    assert instance.r == original

@given(instance=ck2gfx::Color_strategy)
def test_ck2gfx::color_g_type(instance):
    assert isinstance(instance.g, int)


@given(instance=ck2gfx::Color_strategy)
def test_ck2gfx::color_g_setter(instance):
    original = instance.g
    instance.g = original
    assert instance.g == original

@given(instance=ck2gfx::EObject_strategy)
@settings(max_examples=50)
def test_ck2gfx::eobject_instantiation(instance):
    assert isinstance(instance, ck2gfx::EObject)

@given(instance=ck2gfx::Model_strategy)
@settings(max_examples=50)
def test_ck2gfx::model_instantiation(instance):
    assert isinstance(instance, ck2gfx::Model)
