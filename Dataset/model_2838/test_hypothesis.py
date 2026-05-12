import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ck2gfx_Animation,
    ck2gfx_EMFXActorType,
    ck2gfx_ColorCode,
    ck2gfx_BitmapFont,
    ck2gfx_BitmapFonts,
    ck2gfx_ArrowType,
    ck2gfx_Pdxmesh,
    ck2gfx_PortraitType,
    ck2gfx_ObjectTypes,
    ck2gfx_CoatOfArmsLayer,
    ck2gfx_CoatOfArmsType,
    ck2gfx_LineChartType,
    ck2gfx_MaskedShieldType,
    ck2gfx_SpriteType,
    ck2gfx_SpriteTypes,
    ck2gfx_ProgressbarType,
    ck2gfx_CorneredTileSpriteType,
    ck2gfx_AnimatedSpriteType,
    ck2gfx_Coordinates,
    ck2gfx_ColorRatio,
    ck2gfx_Color,
    ck2gfx_EObject,
    ck2gfx_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ck2gfx_animation_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_Animation)


def test_ck2gfx_animation_constructor_exists():
    assert callable(ck2gfx_Animation.__init__)


def test_ck2gfx_animation_constructor_args():
    sig = inspect.signature(ck2gfx_Animation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "defaultAnimationTime" in params, "Missing parameter 'defaultAnimationTime'"
    assert "file" in params, "Missing parameter 'file'"

def test_ck2gfx_animation_has_name():
    assert hasattr(ck2gfx_Animation, "name")
    descriptor = None
    for klass in ck2gfx_Animation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_animation_has_defaultAnimationTime():
    assert hasattr(ck2gfx_Animation, "defaultAnimationTime")
    descriptor = None
    for klass in ck2gfx_Animation.__mro__:
        if "defaultAnimationTime" in klass.__dict__:
            descriptor = klass.__dict__["defaultAnimationTime"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_animation_has_file():
    assert hasattr(ck2gfx_Animation, "file")
    descriptor = None
    for klass in ck2gfx_Animation.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx_emfxactortype_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_EMFXActorType)


def test_ck2gfx_emfxactortype_constructor_exists():
    assert callable(ck2gfx_EMFXActorType.__init__)


def test_ck2gfx_emfxactortype_constructor_args():
    sig = inspect.signature(ck2gfx_EMFXActorType.__init__)
    params = list(sig.parameters.keys())
    assert "idle" in params, "Missing parameter 'idle'"
    assert "attack" in params, "Missing parameter 'attack'"
    assert "move" in params, "Missing parameter 'move'"
    assert "cullDistance" in params, "Missing parameter 'cullDistance'"
    assert "scaleOnCullDistance" in params, "Missing parameter 'scaleOnCullDistance'"
    assert "name" in params, "Missing parameter 'name'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "actorFile" in params, "Missing parameter 'actorFile'"
    assert "useAnimation" in params, "Missing parameter 'useAnimation'"

def test_ck2gfx_emfxactortype_has_idle():
    assert hasattr(ck2gfx_EMFXActorType, "idle")
    descriptor = None
    for klass in ck2gfx_EMFXActorType.__mro__:
        if "idle" in klass.__dict__:
            descriptor = klass.__dict__["idle"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_emfxactortype_has_attack():
    assert hasattr(ck2gfx_EMFXActorType, "attack")
    descriptor = None
    for klass in ck2gfx_EMFXActorType.__mro__:
        if "attack" in klass.__dict__:
            descriptor = klass.__dict__["attack"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_emfxactortype_has_move():
    assert hasattr(ck2gfx_EMFXActorType, "move")
    descriptor = None
    for klass in ck2gfx_EMFXActorType.__mro__:
        if "move" in klass.__dict__:
            descriptor = klass.__dict__["move"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_emfxactortype_has_cullDistance():
    assert hasattr(ck2gfx_EMFXActorType, "cullDistance")
    descriptor = None
    for klass in ck2gfx_EMFXActorType.__mro__:
        if "cullDistance" in klass.__dict__:
            descriptor = klass.__dict__["cullDistance"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_emfxactortype_has_scaleOnCullDistance():
    assert hasattr(ck2gfx_EMFXActorType, "scaleOnCullDistance")
    descriptor = None
    for klass in ck2gfx_EMFXActorType.__mro__:
        if "scaleOnCullDistance" in klass.__dict__:
            descriptor = klass.__dict__["scaleOnCullDistance"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_emfxactortype_has_name():
    assert hasattr(ck2gfx_EMFXActorType, "name")
    descriptor = None
    for klass in ck2gfx_EMFXActorType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_emfxactortype_has_scale():
    assert hasattr(ck2gfx_EMFXActorType, "scale")
    descriptor = None
    for klass in ck2gfx_EMFXActorType.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_emfxactortype_has_actorFile():
    assert hasattr(ck2gfx_EMFXActorType, "actorFile")
    descriptor = None
    for klass in ck2gfx_EMFXActorType.__mro__:
        if "actorFile" in klass.__dict__:
            descriptor = klass.__dict__["actorFile"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_emfxactortype_has_useAnimation():
    assert hasattr(ck2gfx_EMFXActorType, "useAnimation")
    descriptor = None
    for klass in ck2gfx_EMFXActorType.__mro__:
        if "useAnimation" in klass.__dict__:
            descriptor = klass.__dict__["useAnimation"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx_colorcode_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_ColorCode)


def test_ck2gfx_colorcode_constructor_exists():
    assert callable(ck2gfx_ColorCode.__init__)


def test_ck2gfx_colorcode_constructor_args():
    sig = inspect.signature(ck2gfx_ColorCode.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_ck2gfx_colorcode_has_key():
    assert hasattr(ck2gfx_ColorCode, "key")
    descriptor = None
    for klass in ck2gfx_ColorCode.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx_bitmapfont_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_BitmapFont)


def test_ck2gfx_bitmapfont_constructor_exists():
    assert callable(ck2gfx_BitmapFont.__init__)


def test_ck2gfx_bitmapfont_constructor_args():
    sig = inspect.signature(ck2gfx_BitmapFont.__init__)
    params = list(sig.parameters.keys())
    assert "fontName" in params, "Missing parameter 'fontName'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "color" in params, "Missing parameter 'color'"
    assert "name" in params, "Missing parameter 'name'"

def test_ck2gfx_bitmapfont_has_fontName():
    assert hasattr(ck2gfx_BitmapFont, "fontName")
    descriptor = None
    for klass in ck2gfx_BitmapFont.__mro__:
        if "fontName" in klass.__dict__:
            descriptor = klass.__dict__["fontName"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_bitmapfont_has_effect():
    assert hasattr(ck2gfx_BitmapFont, "effect")
    descriptor = None
    for klass in ck2gfx_BitmapFont.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_bitmapfont_has_color():
    assert hasattr(ck2gfx_BitmapFont, "color")
    descriptor = None
    for klass in ck2gfx_BitmapFont.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_bitmapfont_has_name():
    assert hasattr(ck2gfx_BitmapFont, "name")
    descriptor = None
    for klass in ck2gfx_BitmapFont.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx_bitmapfonts_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_BitmapFonts)


def test_ck2gfx_bitmapfonts_constructor_exists():
    assert callable(ck2gfx_BitmapFonts.__init__)


def test_ck2gfx_bitmapfonts_constructor_args():
    sig = inspect.signature(ck2gfx_BitmapFonts.__init__)
    params = list(sig.parameters.keys())



def test_ck2gfx_arrowtype_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_ArrowType)


def test_ck2gfx_arrowtype_constructor_exists():
    assert callable(ck2gfx_ArrowType.__init__)


def test_ck2gfx_arrowtype_constructor_args():
    sig = inspect.signature(ck2gfx_ArrowType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "type" in params, "Missing parameter 'type'"
    assert "endAt" in params, "Missing parameter 'endAt'"
    assert "heading" in params, "Missing parameter 'heading'"
    assert "name" in params, "Missing parameter 'name'"
    assert "bodyTexture" in params, "Missing parameter 'bodyTexture'"
    assert "textureFile" in params, "Missing parameter 'textureFile'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "height" in params, "Missing parameter 'height'"

def test_ck2gfx_arrowtype_has_size():
    assert hasattr(ck2gfx_ArrowType, "size")
    descriptor = None
    for klass in ck2gfx_ArrowType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_arrowtype_has_type():
    assert hasattr(ck2gfx_ArrowType, "type")
    descriptor = None
    for klass in ck2gfx_ArrowType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_arrowtype_has_endAt():
    assert hasattr(ck2gfx_ArrowType, "endAt")
    descriptor = None
    for klass in ck2gfx_ArrowType.__mro__:
        if "endAt" in klass.__dict__:
            descriptor = klass.__dict__["endAt"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_arrowtype_has_heading():
    assert hasattr(ck2gfx_ArrowType, "heading")
    descriptor = None
    for klass in ck2gfx_ArrowType.__mro__:
        if "heading" in klass.__dict__:
            descriptor = klass.__dict__["heading"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_arrowtype_has_name():
    assert hasattr(ck2gfx_ArrowType, "name")
    descriptor = None
    for klass in ck2gfx_ArrowType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_arrowtype_has_bodyTexture():
    assert hasattr(ck2gfx_ArrowType, "bodyTexture")
    descriptor = None
    for klass in ck2gfx_ArrowType.__mro__:
        if "bodyTexture" in klass.__dict__:
            descriptor = klass.__dict__["bodyTexture"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_arrowtype_has_textureFile():
    assert hasattr(ck2gfx_ArrowType, "textureFile")
    descriptor = None
    for klass in ck2gfx_ArrowType.__mro__:
        if "textureFile" in klass.__dict__:
            descriptor = klass.__dict__["textureFile"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_arrowtype_has_effect():
    assert hasattr(ck2gfx_ArrowType, "effect")
    descriptor = None
    for klass in ck2gfx_ArrowType.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_arrowtype_has_height():
    assert hasattr(ck2gfx_ArrowType, "height")
    descriptor = None
    for klass in ck2gfx_ArrowType.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx_pdxmesh_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_Pdxmesh)


def test_ck2gfx_pdxmesh_constructor_exists():
    assert callable(ck2gfx_Pdxmesh.__init__)


def test_ck2gfx_pdxmesh_constructor_args():
    sig = inspect.signature(ck2gfx_Pdxmesh.__init__)
    params = list(sig.parameters.keys())
    assert "scale" in params, "Missing parameter 'scale'"
    assert "scaleOnCullDistance" in params, "Missing parameter 'scaleOnCullDistance'"
    assert "actorFile" in params, "Missing parameter 'actorFile'"
    assert "name" in params, "Missing parameter 'name'"
    assert "cullDistance" in params, "Missing parameter 'cullDistance'"

def test_ck2gfx_pdxmesh_has_scale():
    assert hasattr(ck2gfx_Pdxmesh, "scale")
    descriptor = None
    for klass in ck2gfx_Pdxmesh.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_pdxmesh_has_scaleOnCullDistance():
    assert hasattr(ck2gfx_Pdxmesh, "scaleOnCullDistance")
    descriptor = None
    for klass in ck2gfx_Pdxmesh.__mro__:
        if "scaleOnCullDistance" in klass.__dict__:
            descriptor = klass.__dict__["scaleOnCullDistance"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_pdxmesh_has_actorFile():
    assert hasattr(ck2gfx_Pdxmesh, "actorFile")
    descriptor = None
    for klass in ck2gfx_Pdxmesh.__mro__:
        if "actorFile" in klass.__dict__:
            descriptor = klass.__dict__["actorFile"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_pdxmesh_has_name():
    assert hasattr(ck2gfx_Pdxmesh, "name")
    descriptor = None
    for klass in ck2gfx_Pdxmesh.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_pdxmesh_has_cullDistance():
    assert hasattr(ck2gfx_Pdxmesh, "cullDistance")
    descriptor = None
    for klass in ck2gfx_Pdxmesh.__mro__:
        if "cullDistance" in klass.__dict__:
            descriptor = klass.__dict__["cullDistance"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx_portraittype_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_PortraitType)


def test_ck2gfx_portraittype_constructor_exists():
    assert callable(ck2gfx_PortraitType.__init__)


def test_ck2gfx_portraittype_constructor_args():
    sig = inspect.signature(ck2gfx_PortraitType.__init__)
    params = list(sig.parameters.keys())
    assert "effectFile" in params, "Missing parameter 'effectFile'"
    assert "layers" in params, "Missing parameter 'layers'"
    assert "hairColorIndex" in params, "Missing parameter 'hairColorIndex'"
    assert "name" in params, "Missing parameter 'name'"
    assert "eyeColorIndex" in params, "Missing parameter 'eyeColorIndex'"
    assert "headgearThatHidesHair" in params, "Missing parameter 'headgearThatHidesHair'"

def test_ck2gfx_portraittype_has_effectFile():
    assert hasattr(ck2gfx_PortraitType, "effectFile")
    descriptor = None
    for klass in ck2gfx_PortraitType.__mro__:
        if "effectFile" in klass.__dict__:
            descriptor = klass.__dict__["effectFile"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_portraittype_has_layers():
    assert hasattr(ck2gfx_PortraitType, "layers")
    descriptor = None
    for klass in ck2gfx_PortraitType.__mro__:
        if "layers" in klass.__dict__:
            descriptor = klass.__dict__["layers"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_portraittype_has_hairColorIndex():
    assert hasattr(ck2gfx_PortraitType, "hairColorIndex")
    descriptor = None
    for klass in ck2gfx_PortraitType.__mro__:
        if "hairColorIndex" in klass.__dict__:
            descriptor = klass.__dict__["hairColorIndex"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_portraittype_has_name():
    assert hasattr(ck2gfx_PortraitType, "name")
    descriptor = None
    for klass in ck2gfx_PortraitType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_portraittype_has_eyeColorIndex():
    assert hasattr(ck2gfx_PortraitType, "eyeColorIndex")
    descriptor = None
    for klass in ck2gfx_PortraitType.__mro__:
        if "eyeColorIndex" in klass.__dict__:
            descriptor = klass.__dict__["eyeColorIndex"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_portraittype_has_headgearThatHidesHair():
    assert hasattr(ck2gfx_PortraitType, "headgearThatHidesHair")
    descriptor = None
    for klass in ck2gfx_PortraitType.__mro__:
        if "headgearThatHidesHair" in klass.__dict__:
            descriptor = klass.__dict__["headgearThatHidesHair"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx_objecttypes_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_ObjectTypes)


def test_ck2gfx_objecttypes_constructor_exists():
    assert callable(ck2gfx_ObjectTypes.__init__)


def test_ck2gfx_objecttypes_constructor_args():
    sig = inspect.signature(ck2gfx_ObjectTypes.__init__)
    params = list(sig.parameters.keys())



def test_ck2gfx_coatofarmslayer_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_CoatOfArmsLayer)


def test_ck2gfx_coatofarmslayer_constructor_exists():
    assert callable(ck2gfx_CoatOfArmsLayer.__init__)


def test_ck2gfx_coatofarmslayer_constructor_args():
    sig = inspect.signature(ck2gfx_CoatOfArmsLayer.__init__)
    params = list(sig.parameters.keys())
    assert "scale" in params, "Missing parameter 'scale'"
    assert "mask" in params, "Missing parameter 'mask'"

def test_ck2gfx_coatofarmslayer_has_scale():
    assert hasattr(ck2gfx_CoatOfArmsLayer, "scale")
    descriptor = None
    for klass in ck2gfx_CoatOfArmsLayer.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_coatofarmslayer_has_mask():
    assert hasattr(ck2gfx_CoatOfArmsLayer, "mask")
    descriptor = None
    for klass in ck2gfx_CoatOfArmsLayer.__mro__:
        if "mask" in klass.__dict__:
            descriptor = klass.__dict__["mask"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx_coatofarmstype_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_CoatOfArmsType)


def test_ck2gfx_coatofarmstype_constructor_exists():
    assert callable(ck2gfx_CoatOfArmsType.__init__)


def test_ck2gfx_coatofarmstype_constructor_args():
    sig = inspect.signature(ck2gfx_CoatOfArmsType.__init__)
    params = list(sig.parameters.keys())
    assert "mask" in params, "Missing parameter 'mask'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "frame" in params, "Missing parameter 'frame'"
    assert "name" in params, "Missing parameter 'name'"
    assert "sealOverlay" in params, "Missing parameter 'sealOverlay'"

def test_ck2gfx_coatofarmstype_has_mask():
    assert hasattr(ck2gfx_CoatOfArmsType, "mask")
    descriptor = None
    for klass in ck2gfx_CoatOfArmsType.__mro__:
        if "mask" in klass.__dict__:
            descriptor = klass.__dict__["mask"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_coatofarmstype_has_effect():
    assert hasattr(ck2gfx_CoatOfArmsType, "effect")
    descriptor = None
    for klass in ck2gfx_CoatOfArmsType.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_coatofarmstype_has_frame():
    assert hasattr(ck2gfx_CoatOfArmsType, "frame")
    descriptor = None
    for klass in ck2gfx_CoatOfArmsType.__mro__:
        if "frame" in klass.__dict__:
            descriptor = klass.__dict__["frame"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_coatofarmstype_has_name():
    assert hasattr(ck2gfx_CoatOfArmsType, "name")
    descriptor = None
    for klass in ck2gfx_CoatOfArmsType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_coatofarmstype_has_sealOverlay():
    assert hasattr(ck2gfx_CoatOfArmsType, "sealOverlay")
    descriptor = None
    for klass in ck2gfx_CoatOfArmsType.__mro__:
        if "sealOverlay" in klass.__dict__:
            descriptor = klass.__dict__["sealOverlay"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx_linecharttype_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_LineChartType)


def test_ck2gfx_linecharttype_constructor_exists():
    assert callable(ck2gfx_LineChartType.__init__)


def test_ck2gfx_linecharttype_constructor_args():
    sig = inspect.signature(ck2gfx_LineChartType.__init__)
    params = list(sig.parameters.keys())
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"
    assert "name" in params, "Missing parameter 'name'"

def test_ck2gfx_linecharttype_has_lineWidth():
    assert hasattr(ck2gfx_LineChartType, "lineWidth")
    descriptor = None
    for klass in ck2gfx_LineChartType.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_linecharttype_has_name():
    assert hasattr(ck2gfx_LineChartType, "name")
    descriptor = None
    for klass in ck2gfx_LineChartType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx_maskedshieldtype_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_MaskedShieldType)


def test_ck2gfx_maskedshieldtype_constructor_exists():
    assert callable(ck2gfx_MaskedShieldType.__init__)


def test_ck2gfx_maskedshieldtype_constructor_args():
    sig = inspect.signature(ck2gfx_MaskedShieldType.__init__)
    params = list(sig.parameters.keys())
    assert "textureFile1" in params, "Missing parameter 'textureFile1'"
    assert "textureFile2" in params, "Missing parameter 'textureFile2'"
    assert "effectFile" in params, "Missing parameter 'effectFile'"
    assert "name" in params, "Missing parameter 'name'"
    assert "clickSound" in params, "Missing parameter 'clickSound'"
    assert "allwaysTransparent" in params, "Missing parameter 'allwaysTransparent'"

def test_ck2gfx_maskedshieldtype_has_textureFile1():
    assert hasattr(ck2gfx_MaskedShieldType, "textureFile1")
    descriptor = None
    for klass in ck2gfx_MaskedShieldType.__mro__:
        if "textureFile1" in klass.__dict__:
            descriptor = klass.__dict__["textureFile1"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_maskedshieldtype_has_textureFile2():
    assert hasattr(ck2gfx_MaskedShieldType, "textureFile2")
    descriptor = None
    for klass in ck2gfx_MaskedShieldType.__mro__:
        if "textureFile2" in klass.__dict__:
            descriptor = klass.__dict__["textureFile2"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_maskedshieldtype_has_effectFile():
    assert hasattr(ck2gfx_MaskedShieldType, "effectFile")
    descriptor = None
    for klass in ck2gfx_MaskedShieldType.__mro__:
        if "effectFile" in klass.__dict__:
            descriptor = klass.__dict__["effectFile"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_maskedshieldtype_has_name():
    assert hasattr(ck2gfx_MaskedShieldType, "name")
    descriptor = None
    for klass in ck2gfx_MaskedShieldType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_maskedshieldtype_has_clickSound():
    assert hasattr(ck2gfx_MaskedShieldType, "clickSound")
    descriptor = None
    for klass in ck2gfx_MaskedShieldType.__mro__:
        if "clickSound" in klass.__dict__:
            descriptor = klass.__dict__["clickSound"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_maskedshieldtype_has_allwaysTransparent():
    assert hasattr(ck2gfx_MaskedShieldType, "allwaysTransparent")
    descriptor = None
    for klass in ck2gfx_MaskedShieldType.__mro__:
        if "allwaysTransparent" in klass.__dict__:
            descriptor = klass.__dict__["allwaysTransparent"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx_spritetype_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_SpriteType)


def test_ck2gfx_spritetype_constructor_exists():
    assert callable(ck2gfx_SpriteType.__init__)


def test_ck2gfx_spritetype_constructor_args():
    sig = inspect.signature(ck2gfx_SpriteType.__init__)
    params = list(sig.parameters.keys())
    assert "textureFile" in params, "Missing parameter 'textureFile'"
    assert "name" in params, "Missing parameter 'name'"
    assert "effectFile" in params, "Missing parameter 'effectFile'"
    assert "canBeLowres" in params, "Missing parameter 'canBeLowres'"
    assert "noOfFrames" in params, "Missing parameter 'noOfFrames'"
    assert "loadType" in params, "Missing parameter 'loadType'"
    assert "transparenceCheck" in params, "Missing parameter 'transparenceCheck'"
    assert "clickSound" in params, "Missing parameter 'clickSound'"
    assert "allwaysTransparent" in params, "Missing parameter 'allwaysTransparent'"
    assert "noRefCount" in params, "Missing parameter 'noRefCount'"

def test_ck2gfx_spritetype_has_textureFile():
    assert hasattr(ck2gfx_SpriteType, "textureFile")
    descriptor = None
    for klass in ck2gfx_SpriteType.__mro__:
        if "textureFile" in klass.__dict__:
            descriptor = klass.__dict__["textureFile"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_spritetype_has_name():
    assert hasattr(ck2gfx_SpriteType, "name")
    descriptor = None
    for klass in ck2gfx_SpriteType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_spritetype_has_effectFile():
    assert hasattr(ck2gfx_SpriteType, "effectFile")
    descriptor = None
    for klass in ck2gfx_SpriteType.__mro__:
        if "effectFile" in klass.__dict__:
            descriptor = klass.__dict__["effectFile"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_spritetype_has_canBeLowres():
    assert hasattr(ck2gfx_SpriteType, "canBeLowres")
    descriptor = None
    for klass in ck2gfx_SpriteType.__mro__:
        if "canBeLowres" in klass.__dict__:
            descriptor = klass.__dict__["canBeLowres"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_spritetype_has_noOfFrames():
    assert hasattr(ck2gfx_SpriteType, "noOfFrames")
    descriptor = None
    for klass in ck2gfx_SpriteType.__mro__:
        if "noOfFrames" in klass.__dict__:
            descriptor = klass.__dict__["noOfFrames"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_spritetype_has_loadType():
    assert hasattr(ck2gfx_SpriteType, "loadType")
    descriptor = None
    for klass in ck2gfx_SpriteType.__mro__:
        if "loadType" in klass.__dict__:
            descriptor = klass.__dict__["loadType"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_spritetype_has_transparenceCheck():
    assert hasattr(ck2gfx_SpriteType, "transparenceCheck")
    descriptor = None
    for klass in ck2gfx_SpriteType.__mro__:
        if "transparenceCheck" in klass.__dict__:
            descriptor = klass.__dict__["transparenceCheck"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_spritetype_has_clickSound():
    assert hasattr(ck2gfx_SpriteType, "clickSound")
    descriptor = None
    for klass in ck2gfx_SpriteType.__mro__:
        if "clickSound" in klass.__dict__:
            descriptor = klass.__dict__["clickSound"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_spritetype_has_allwaysTransparent():
    assert hasattr(ck2gfx_SpriteType, "allwaysTransparent")
    descriptor = None
    for klass in ck2gfx_SpriteType.__mro__:
        if "allwaysTransparent" in klass.__dict__:
            descriptor = klass.__dict__["allwaysTransparent"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_spritetype_has_noRefCount():
    assert hasattr(ck2gfx_SpriteType, "noRefCount")
    descriptor = None
    for klass in ck2gfx_SpriteType.__mro__:
        if "noRefCount" in klass.__dict__:
            descriptor = klass.__dict__["noRefCount"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx_spritetypes_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_SpriteTypes)


def test_ck2gfx_spritetypes_constructor_exists():
    assert callable(ck2gfx_SpriteTypes.__init__)


def test_ck2gfx_spritetypes_constructor_args():
    sig = inspect.signature(ck2gfx_SpriteTypes.__init__)
    params = list(sig.parameters.keys())



def test_ck2gfx_progressbartype_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_ProgressbarType)


def test_ck2gfx_progressbartype_constructor_exists():
    assert callable(ck2gfx_ProgressbarType.__init__)


def test_ck2gfx_progressbartype_constructor_args():
    sig = inspect.signature(ck2gfx_ProgressbarType.__init__)
    params = list(sig.parameters.keys())
    assert "noRefCount" in params, "Missing parameter 'noRefCount'"
    assert "textureFile2" in params, "Missing parameter 'textureFile2'"
    assert "allwaysTransparent" in params, "Missing parameter 'allwaysTransparent'"
    assert "name" in params, "Missing parameter 'name'"
    assert "textureFile1" in params, "Missing parameter 'textureFile1'"
    assert "effectFile" in params, "Missing parameter 'effectFile'"
    assert "horizontal" in params, "Missing parameter 'horizontal'"
    assert "maxValue" in params, "Missing parameter 'maxValue'"
    assert "loadType" in params, "Missing parameter 'loadType'"

def test_ck2gfx_progressbartype_has_noRefCount():
    assert hasattr(ck2gfx_ProgressbarType, "noRefCount")
    descriptor = None
    for klass in ck2gfx_ProgressbarType.__mro__:
        if "noRefCount" in klass.__dict__:
            descriptor = klass.__dict__["noRefCount"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_progressbartype_has_textureFile2():
    assert hasattr(ck2gfx_ProgressbarType, "textureFile2")
    descriptor = None
    for klass in ck2gfx_ProgressbarType.__mro__:
        if "textureFile2" in klass.__dict__:
            descriptor = klass.__dict__["textureFile2"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_progressbartype_has_allwaysTransparent():
    assert hasattr(ck2gfx_ProgressbarType, "allwaysTransparent")
    descriptor = None
    for klass in ck2gfx_ProgressbarType.__mro__:
        if "allwaysTransparent" in klass.__dict__:
            descriptor = klass.__dict__["allwaysTransparent"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_progressbartype_has_name():
    assert hasattr(ck2gfx_ProgressbarType, "name")
    descriptor = None
    for klass in ck2gfx_ProgressbarType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_progressbartype_has_textureFile1():
    assert hasattr(ck2gfx_ProgressbarType, "textureFile1")
    descriptor = None
    for klass in ck2gfx_ProgressbarType.__mro__:
        if "textureFile1" in klass.__dict__:
            descriptor = klass.__dict__["textureFile1"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_progressbartype_has_effectFile():
    assert hasattr(ck2gfx_ProgressbarType, "effectFile")
    descriptor = None
    for klass in ck2gfx_ProgressbarType.__mro__:
        if "effectFile" in klass.__dict__:
            descriptor = klass.__dict__["effectFile"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_progressbartype_has_horizontal():
    assert hasattr(ck2gfx_ProgressbarType, "horizontal")
    descriptor = None
    for klass in ck2gfx_ProgressbarType.__mro__:
        if "horizontal" in klass.__dict__:
            descriptor = klass.__dict__["horizontal"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_progressbartype_has_maxValue():
    assert hasattr(ck2gfx_ProgressbarType, "maxValue")
    descriptor = None
    for klass in ck2gfx_ProgressbarType.__mro__:
        if "maxValue" in klass.__dict__:
            descriptor = klass.__dict__["maxValue"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_progressbartype_has_loadType():
    assert hasattr(ck2gfx_ProgressbarType, "loadType")
    descriptor = None
    for klass in ck2gfx_ProgressbarType.__mro__:
        if "loadType" in klass.__dict__:
            descriptor = klass.__dict__["loadType"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx_corneredtilespritetype_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_CorneredTileSpriteType)


def test_ck2gfx_corneredtilespritetype_constructor_exists():
    assert callable(ck2gfx_CorneredTileSpriteType.__init__)


def test_ck2gfx_corneredtilespritetype_constructor_args():
    sig = inspect.signature(ck2gfx_CorneredTileSpriteType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "noRefCount" in params, "Missing parameter 'noRefCount'"
    assert "allwaysTransparent" in params, "Missing parameter 'allwaysTransparent'"
    assert "texturefile" in params, "Missing parameter 'texturefile'"
    assert "loadType" in params, "Missing parameter 'loadType'"
    assert "tilingCenter" in params, "Missing parameter 'tilingCenter'"

def test_ck2gfx_corneredtilespritetype_has_name():
    assert hasattr(ck2gfx_CorneredTileSpriteType, "name")
    descriptor = None
    for klass in ck2gfx_CorneredTileSpriteType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_corneredtilespritetype_has_noRefCount():
    assert hasattr(ck2gfx_CorneredTileSpriteType, "noRefCount")
    descriptor = None
    for klass in ck2gfx_CorneredTileSpriteType.__mro__:
        if "noRefCount" in klass.__dict__:
            descriptor = klass.__dict__["noRefCount"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_corneredtilespritetype_has_allwaysTransparent():
    assert hasattr(ck2gfx_CorneredTileSpriteType, "allwaysTransparent")
    descriptor = None
    for klass in ck2gfx_CorneredTileSpriteType.__mro__:
        if "allwaysTransparent" in klass.__dict__:
            descriptor = klass.__dict__["allwaysTransparent"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_corneredtilespritetype_has_texturefile():
    assert hasattr(ck2gfx_CorneredTileSpriteType, "texturefile")
    descriptor = None
    for klass in ck2gfx_CorneredTileSpriteType.__mro__:
        if "texturefile" in klass.__dict__:
            descriptor = klass.__dict__["texturefile"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_corneredtilespritetype_has_loadType():
    assert hasattr(ck2gfx_CorneredTileSpriteType, "loadType")
    descriptor = None
    for klass in ck2gfx_CorneredTileSpriteType.__mro__:
        if "loadType" in klass.__dict__:
            descriptor = klass.__dict__["loadType"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_corneredtilespritetype_has_tilingCenter():
    assert hasattr(ck2gfx_CorneredTileSpriteType, "tilingCenter")
    descriptor = None
    for klass in ck2gfx_CorneredTileSpriteType.__mro__:
        if "tilingCenter" in klass.__dict__:
            descriptor = klass.__dict__["tilingCenter"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx_animatedspritetype_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_AnimatedSpriteType)


def test_ck2gfx_animatedspritetype_constructor_exists():
    assert callable(ck2gfx_AnimatedSpriteType.__init__)


def test_ck2gfx_animatedspritetype_constructor_args():
    sig = inspect.signature(ck2gfx_AnimatedSpriteType.__init__)
    params = list(sig.parameters.keys())
    assert "looping" in params, "Missing parameter 'looping'"
    assert "animationRateFps" in params, "Missing parameter 'animationRateFps'"
    assert "noOfFrames" in params, "Missing parameter 'noOfFrames'"
    assert "texturefile" in params, "Missing parameter 'texturefile'"
    assert "playOnShow" in params, "Missing parameter 'playOnShow'"
    assert "name" in params, "Missing parameter 'name'"

def test_ck2gfx_animatedspritetype_has_looping():
    assert hasattr(ck2gfx_AnimatedSpriteType, "looping")
    descriptor = None
    for klass in ck2gfx_AnimatedSpriteType.__mro__:
        if "looping" in klass.__dict__:
            descriptor = klass.__dict__["looping"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_animatedspritetype_has_animationRateFps():
    assert hasattr(ck2gfx_AnimatedSpriteType, "animationRateFps")
    descriptor = None
    for klass in ck2gfx_AnimatedSpriteType.__mro__:
        if "animationRateFps" in klass.__dict__:
            descriptor = klass.__dict__["animationRateFps"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_animatedspritetype_has_noOfFrames():
    assert hasattr(ck2gfx_AnimatedSpriteType, "noOfFrames")
    descriptor = None
    for klass in ck2gfx_AnimatedSpriteType.__mro__:
        if "noOfFrames" in klass.__dict__:
            descriptor = klass.__dict__["noOfFrames"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_animatedspritetype_has_texturefile():
    assert hasattr(ck2gfx_AnimatedSpriteType, "texturefile")
    descriptor = None
    for klass in ck2gfx_AnimatedSpriteType.__mro__:
        if "texturefile" in klass.__dict__:
            descriptor = klass.__dict__["texturefile"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_animatedspritetype_has_playOnShow():
    assert hasattr(ck2gfx_AnimatedSpriteType, "playOnShow")
    descriptor = None
    for klass in ck2gfx_AnimatedSpriteType.__mro__:
        if "playOnShow" in klass.__dict__:
            descriptor = klass.__dict__["playOnShow"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_animatedspritetype_has_name():
    assert hasattr(ck2gfx_AnimatedSpriteType, "name")
    descriptor = None
    for klass in ck2gfx_AnimatedSpriteType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx_coordinates_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_Coordinates)


def test_ck2gfx_coordinates_constructor_exists():
    assert callable(ck2gfx_Coordinates.__init__)


def test_ck2gfx_coordinates_constructor_args():
    sig = inspect.signature(ck2gfx_Coordinates.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_ck2gfx_coordinates_has_x():
    assert hasattr(ck2gfx_Coordinates, "x")
    descriptor = None
    for klass in ck2gfx_Coordinates.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_coordinates_has_y():
    assert hasattr(ck2gfx_Coordinates, "y")
    descriptor = None
    for klass in ck2gfx_Coordinates.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx_colorratio_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_ColorRatio)


def test_ck2gfx_colorratio_constructor_exists():
    assert callable(ck2gfx_ColorRatio.__init__)


def test_ck2gfx_colorratio_constructor_args():
    sig = inspect.signature(ck2gfx_ColorRatio.__init__)
    params = list(sig.parameters.keys())
    assert "g" in params, "Missing parameter 'g'"
    assert "r" in params, "Missing parameter 'r'"
    assert "b" in params, "Missing parameter 'b'"

def test_ck2gfx_colorratio_has_g():
    assert hasattr(ck2gfx_ColorRatio, "g")
    descriptor = None
    for klass in ck2gfx_ColorRatio.__mro__:
        if "g" in klass.__dict__:
            descriptor = klass.__dict__["g"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_colorratio_has_r():
    assert hasattr(ck2gfx_ColorRatio, "r")
    descriptor = None
    for klass in ck2gfx_ColorRatio.__mro__:
        if "r" in klass.__dict__:
            descriptor = klass.__dict__["r"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_colorratio_has_b():
    assert hasattr(ck2gfx_ColorRatio, "b")
    descriptor = None
    for klass in ck2gfx_ColorRatio.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx_color_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_Color)


def test_ck2gfx_color_constructor_exists():
    assert callable(ck2gfx_Color.__init__)


def test_ck2gfx_color_constructor_args():
    sig = inspect.signature(ck2gfx_Color.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"
    assert "r" in params, "Missing parameter 'r'"
    assert "g" in params, "Missing parameter 'g'"

def test_ck2gfx_color_has_b():
    assert hasattr(ck2gfx_Color, "b")
    descriptor = None
    for klass in ck2gfx_Color.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_color_has_r():
    assert hasattr(ck2gfx_Color, "r")
    descriptor = None
    for klass in ck2gfx_Color.__mro__:
        if "r" in klass.__dict__:
            descriptor = klass.__dict__["r"]
            break
    assert isinstance(descriptor, property)

def test_ck2gfx_color_has_g():
    assert hasattr(ck2gfx_Color, "g")
    descriptor = None
    for klass in ck2gfx_Color.__mro__:
        if "g" in klass.__dict__:
            descriptor = klass.__dict__["g"]
            break
    assert isinstance(descriptor, property)



def test_ck2gfx_eobject_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_EObject)


def test_ck2gfx_eobject_constructor_exists():
    assert callable(ck2gfx_EObject.__init__)


def test_ck2gfx_eobject_constructor_args():
    sig = inspect.signature(ck2gfx_EObject.__init__)
    params = list(sig.parameters.keys())



def test_ck2gfx_model_is_not_abstract():
    assert not inspect.isabstract(ck2gfx_Model)


def test_ck2gfx_model_constructor_exists():
    assert callable(ck2gfx_Model.__init__)


def test_ck2gfx_model_constructor_args():
    sig = inspect.signature(ck2gfx_Model.__init__)
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
ck2gfx_Animation_strategy = st.builds(
    ck2gfx_Animation,
    name=
        safe_text,
    defaultAnimationTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    file=
        safe_text
)
ck2gfx_EMFXActorType_strategy = st.builds(
    ck2gfx_EMFXActorType,
    idle=
        safe_text,
    attack=
        safe_text,
    move=
        safe_text,
    cullDistance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    scaleOnCullDistance=
        st.booleans(),
    name=
        safe_text,
    scale=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    actorFile=
        safe_text,
    useAnimation=
        st.booleans()
)
ck2gfx_ColorCode_strategy = st.builds(
    ck2gfx_ColorCode,
    key=
        safe_text
)
ck2gfx_BitmapFont_strategy = st.builds(
    ck2gfx_BitmapFont,
    fontName=
        safe_text,
    effect=
        st.booleans(),
    color=
        st.integers(),
    name=
        safe_text
)
ck2gfx_BitmapFonts_strategy = st.builds(
    ck2gfx_BitmapFonts,
)
ck2gfx_ArrowType_strategy = st.builds(
    ck2gfx_ArrowType,
    size=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        st.integers(),
    endAt=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    heading=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    bodyTexture=
        safe_text,
    textureFile=
        safe_text,
    effect=
        safe_text,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ck2gfx_Pdxmesh_strategy = st.builds(
    ck2gfx_Pdxmesh,
    scale=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    scaleOnCullDistance=
        st.booleans(),
    actorFile=
        safe_text,
    name=
        safe_text,
    cullDistance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ck2gfx_PortraitType_strategy = st.builds(
    ck2gfx_PortraitType,
    effectFile=
        safe_text,
    layers=
        safe_text,
    hairColorIndex=
        st.integers(),
    name=
        safe_text,
    eyeColorIndex=
        st.integers(),
    headgearThatHidesHair=
        st.integers()
)
ck2gfx_ObjectTypes_strategy = st.builds(
    ck2gfx_ObjectTypes,
)
ck2gfx_CoatOfArmsLayer_strategy = st.builds(
    ck2gfx_CoatOfArmsLayer,
    scale=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    mask=
        safe_text
)
ck2gfx_CoatOfArmsType_strategy = st.builds(
    ck2gfx_CoatOfArmsType,
    mask=
        safe_text,
    effect=
        safe_text,
    frame=
        safe_text,
    name=
        safe_text,
    sealOverlay=
        safe_text
)
ck2gfx_LineChartType_strategy = st.builds(
    ck2gfx_LineChartType,
    lineWidth=
        st.integers(),
    name=
        safe_text
)
ck2gfx_MaskedShieldType_strategy = st.builds(
    ck2gfx_MaskedShieldType,
    textureFile1=
        safe_text,
    textureFile2=
        safe_text,
    effectFile=
        safe_text,
    name=
        safe_text,
    clickSound=
        safe_text,
    allwaysTransparent=
        st.booleans()
)
ck2gfx_SpriteType_strategy = st.builds(
    ck2gfx_SpriteType,
    textureFile=
        safe_text,
    name=
        safe_text,
    effectFile=
        safe_text,
    canBeLowres=
        st.booleans(),
    noOfFrames=
        st.integers(),
    loadType=
        safe_text,
    transparenceCheck=
        st.booleans(),
    clickSound=
        safe_text,
    allwaysTransparent=
        st.booleans(),
    noRefCount=
        st.booleans()
)
ck2gfx_SpriteTypes_strategy = st.builds(
    ck2gfx_SpriteTypes,
)
ck2gfx_ProgressbarType_strategy = st.builds(
    ck2gfx_ProgressbarType,
    noRefCount=
        st.booleans(),
    textureFile2=
        safe_text,
    allwaysTransparent=
        st.booleans(),
    name=
        safe_text,
    textureFile1=
        safe_text,
    effectFile=
        safe_text,
    horizontal=
        st.booleans(),
    maxValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    loadType=
        safe_text
)
ck2gfx_CorneredTileSpriteType_strategy = st.builds(
    ck2gfx_CorneredTileSpriteType,
    name=
        safe_text,
    noRefCount=
        st.booleans(),
    allwaysTransparent=
        st.booleans(),
    texturefile=
        safe_text,
    loadType=
        safe_text,
    tilingCenter=
        st.booleans()
)
ck2gfx_AnimatedSpriteType_strategy = st.builds(
    ck2gfx_AnimatedSpriteType,
    looping=
        st.booleans(),
    animationRateFps=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    noOfFrames=
        st.integers(),
    texturefile=
        safe_text,
    playOnShow=
        st.booleans(),
    name=
        safe_text
)
ck2gfx_Coordinates_strategy = st.builds(
    ck2gfx_Coordinates,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ck2gfx_ColorRatio_strategy = st.builds(
    ck2gfx_ColorRatio,
    g=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    r=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    b=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ck2gfx_Color_strategy = st.builds(
    ck2gfx_Color,
    b=
        st.integers(),
    r=
        st.integers(),
    g=
        st.integers()
)
ck2gfx_EObject_strategy = st.builds(
    ck2gfx_EObject,
)
ck2gfx_Model_strategy = st.builds(
    ck2gfx_Model,
)

@given(instance=ck2gfx_Animation_strategy)
@settings(max_examples=50)
def test_ck2gfx_animation_instantiation(instance):
    assert isinstance(instance, ck2gfx_Animation)



@given(instance=ck2gfx_Animation_strategy)
def test_ck2gfx_animation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ck2gfx_Animation_strategy)
def test_ck2gfx_animation_defaultAnimationTime_setter(instance):
    original = instance.defaultAnimationTime
    instance.defaultAnimationTime = original
    assert instance.defaultAnimationTime == original



@given(instance=ck2gfx_Animation_strategy)
def test_ck2gfx_animation_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=ck2gfx_EMFXActorType_strategy)
@settings(max_examples=50)
def test_ck2gfx_emfxactortype_instantiation(instance):
    assert isinstance(instance, ck2gfx_EMFXActorType)



@given(instance=ck2gfx_EMFXActorType_strategy)
def test_ck2gfx_emfxactortype_idle_setter(instance):
    original = instance.idle
    instance.idle = original
    assert instance.idle == original



@given(instance=ck2gfx_EMFXActorType_strategy)
def test_ck2gfx_emfxactortype_attack_setter(instance):
    original = instance.attack
    instance.attack = original
    assert instance.attack == original



@given(instance=ck2gfx_EMFXActorType_strategy)
def test_ck2gfx_emfxactortype_move_setter(instance):
    original = instance.move
    instance.move = original
    assert instance.move == original



@given(instance=ck2gfx_EMFXActorType_strategy)
def test_ck2gfx_emfxactortype_cullDistance_setter(instance):
    original = instance.cullDistance
    instance.cullDistance = original
    assert instance.cullDistance == original



@given(instance=ck2gfx_EMFXActorType_strategy)
def test_ck2gfx_emfxactortype_scaleOnCullDistance_setter(instance):
    original = instance.scaleOnCullDistance
    instance.scaleOnCullDistance = original
    assert instance.scaleOnCullDistance == original



@given(instance=ck2gfx_EMFXActorType_strategy)
def test_ck2gfx_emfxactortype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ck2gfx_EMFXActorType_strategy)
def test_ck2gfx_emfxactortype_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original



@given(instance=ck2gfx_EMFXActorType_strategy)
def test_ck2gfx_emfxactortype_actorFile_setter(instance):
    original = instance.actorFile
    instance.actorFile = original
    assert instance.actorFile == original



@given(instance=ck2gfx_EMFXActorType_strategy)
def test_ck2gfx_emfxactortype_useAnimation_setter(instance):
    original = instance.useAnimation
    instance.useAnimation = original
    assert instance.useAnimation == original

@given(instance=ck2gfx_ColorCode_strategy)
@settings(max_examples=50)
def test_ck2gfx_colorcode_instantiation(instance):
    assert isinstance(instance, ck2gfx_ColorCode)



@given(instance=ck2gfx_ColorCode_strategy)
def test_ck2gfx_colorcode_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=ck2gfx_BitmapFont_strategy)
@settings(max_examples=50)
def test_ck2gfx_bitmapfont_instantiation(instance):
    assert isinstance(instance, ck2gfx_BitmapFont)



@given(instance=ck2gfx_BitmapFont_strategy)
def test_ck2gfx_bitmapfont_fontName_setter(instance):
    original = instance.fontName
    instance.fontName = original
    assert instance.fontName == original



@given(instance=ck2gfx_BitmapFont_strategy)
def test_ck2gfx_bitmapfont_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original



@given(instance=ck2gfx_BitmapFont_strategy)
def test_ck2gfx_bitmapfont_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=ck2gfx_BitmapFont_strategy)
def test_ck2gfx_bitmapfont_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ck2gfx_BitmapFonts_strategy)
@settings(max_examples=50)
def test_ck2gfx_bitmapfonts_instantiation(instance):
    assert isinstance(instance, ck2gfx_BitmapFonts)

@given(instance=ck2gfx_ArrowType_strategy)
@settings(max_examples=50)
def test_ck2gfx_arrowtype_instantiation(instance):
    assert isinstance(instance, ck2gfx_ArrowType)



@given(instance=ck2gfx_ArrowType_strategy)
def test_ck2gfx_arrowtype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=ck2gfx_ArrowType_strategy)
def test_ck2gfx_arrowtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=ck2gfx_ArrowType_strategy)
def test_ck2gfx_arrowtype_endAt_setter(instance):
    original = instance.endAt
    instance.endAt = original
    assert instance.endAt == original



@given(instance=ck2gfx_ArrowType_strategy)
def test_ck2gfx_arrowtype_heading_setter(instance):
    original = instance.heading
    instance.heading = original
    assert instance.heading == original



@given(instance=ck2gfx_ArrowType_strategy)
def test_ck2gfx_arrowtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ck2gfx_ArrowType_strategy)
def test_ck2gfx_arrowtype_bodyTexture_setter(instance):
    original = instance.bodyTexture
    instance.bodyTexture = original
    assert instance.bodyTexture == original



@given(instance=ck2gfx_ArrowType_strategy)
def test_ck2gfx_arrowtype_textureFile_setter(instance):
    original = instance.textureFile
    instance.textureFile = original
    assert instance.textureFile == original



@given(instance=ck2gfx_ArrowType_strategy)
def test_ck2gfx_arrowtype_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original



@given(instance=ck2gfx_ArrowType_strategy)
def test_ck2gfx_arrowtype_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=ck2gfx_Pdxmesh_strategy)
@settings(max_examples=50)
def test_ck2gfx_pdxmesh_instantiation(instance):
    assert isinstance(instance, ck2gfx_Pdxmesh)



@given(instance=ck2gfx_Pdxmesh_strategy)
def test_ck2gfx_pdxmesh_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original



@given(instance=ck2gfx_Pdxmesh_strategy)
def test_ck2gfx_pdxmesh_scaleOnCullDistance_setter(instance):
    original = instance.scaleOnCullDistance
    instance.scaleOnCullDistance = original
    assert instance.scaleOnCullDistance == original



@given(instance=ck2gfx_Pdxmesh_strategy)
def test_ck2gfx_pdxmesh_actorFile_setter(instance):
    original = instance.actorFile
    instance.actorFile = original
    assert instance.actorFile == original



@given(instance=ck2gfx_Pdxmesh_strategy)
def test_ck2gfx_pdxmesh_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ck2gfx_Pdxmesh_strategy)
def test_ck2gfx_pdxmesh_cullDistance_setter(instance):
    original = instance.cullDistance
    instance.cullDistance = original
    assert instance.cullDistance == original

@given(instance=ck2gfx_PortraitType_strategy)
@settings(max_examples=50)
def test_ck2gfx_portraittype_instantiation(instance):
    assert isinstance(instance, ck2gfx_PortraitType)



@given(instance=ck2gfx_PortraitType_strategy)
def test_ck2gfx_portraittype_effectFile_setter(instance):
    original = instance.effectFile
    instance.effectFile = original
    assert instance.effectFile == original



@given(instance=ck2gfx_PortraitType_strategy)
def test_ck2gfx_portraittype_layers_setter(instance):
    original = instance.layers
    instance.layers = original
    assert instance.layers == original



@given(instance=ck2gfx_PortraitType_strategy)
def test_ck2gfx_portraittype_hairColorIndex_setter(instance):
    original = instance.hairColorIndex
    instance.hairColorIndex = original
    assert instance.hairColorIndex == original



@given(instance=ck2gfx_PortraitType_strategy)
def test_ck2gfx_portraittype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ck2gfx_PortraitType_strategy)
def test_ck2gfx_portraittype_eyeColorIndex_setter(instance):
    original = instance.eyeColorIndex
    instance.eyeColorIndex = original
    assert instance.eyeColorIndex == original



@given(instance=ck2gfx_PortraitType_strategy)
def test_ck2gfx_portraittype_headgearThatHidesHair_setter(instance):
    original = instance.headgearThatHidesHair
    instance.headgearThatHidesHair = original
    assert instance.headgearThatHidesHair == original

@given(instance=ck2gfx_ObjectTypes_strategy)
@settings(max_examples=50)
def test_ck2gfx_objecttypes_instantiation(instance):
    assert isinstance(instance, ck2gfx_ObjectTypes)

@given(instance=ck2gfx_CoatOfArmsLayer_strategy)
@settings(max_examples=50)
def test_ck2gfx_coatofarmslayer_instantiation(instance):
    assert isinstance(instance, ck2gfx_CoatOfArmsLayer)



@given(instance=ck2gfx_CoatOfArmsLayer_strategy)
def test_ck2gfx_coatofarmslayer_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original



@given(instance=ck2gfx_CoatOfArmsLayer_strategy)
def test_ck2gfx_coatofarmslayer_mask_setter(instance):
    original = instance.mask
    instance.mask = original
    assert instance.mask == original

@given(instance=ck2gfx_CoatOfArmsType_strategy)
@settings(max_examples=50)
def test_ck2gfx_coatofarmstype_instantiation(instance):
    assert isinstance(instance, ck2gfx_CoatOfArmsType)



@given(instance=ck2gfx_CoatOfArmsType_strategy)
def test_ck2gfx_coatofarmstype_mask_setter(instance):
    original = instance.mask
    instance.mask = original
    assert instance.mask == original



@given(instance=ck2gfx_CoatOfArmsType_strategy)
def test_ck2gfx_coatofarmstype_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original



@given(instance=ck2gfx_CoatOfArmsType_strategy)
def test_ck2gfx_coatofarmstype_frame_setter(instance):
    original = instance.frame
    instance.frame = original
    assert instance.frame == original



@given(instance=ck2gfx_CoatOfArmsType_strategy)
def test_ck2gfx_coatofarmstype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ck2gfx_CoatOfArmsType_strategy)
def test_ck2gfx_coatofarmstype_sealOverlay_setter(instance):
    original = instance.sealOverlay
    instance.sealOverlay = original
    assert instance.sealOverlay == original

@given(instance=ck2gfx_LineChartType_strategy)
@settings(max_examples=50)
def test_ck2gfx_linecharttype_instantiation(instance):
    assert isinstance(instance, ck2gfx_LineChartType)



@given(instance=ck2gfx_LineChartType_strategy)
def test_ck2gfx_linecharttype_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original



@given(instance=ck2gfx_LineChartType_strategy)
def test_ck2gfx_linecharttype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ck2gfx_MaskedShieldType_strategy)
@settings(max_examples=50)
def test_ck2gfx_maskedshieldtype_instantiation(instance):
    assert isinstance(instance, ck2gfx_MaskedShieldType)



@given(instance=ck2gfx_MaskedShieldType_strategy)
def test_ck2gfx_maskedshieldtype_textureFile1_setter(instance):
    original = instance.textureFile1
    instance.textureFile1 = original
    assert instance.textureFile1 == original



@given(instance=ck2gfx_MaskedShieldType_strategy)
def test_ck2gfx_maskedshieldtype_textureFile2_setter(instance):
    original = instance.textureFile2
    instance.textureFile2 = original
    assert instance.textureFile2 == original



@given(instance=ck2gfx_MaskedShieldType_strategy)
def test_ck2gfx_maskedshieldtype_effectFile_setter(instance):
    original = instance.effectFile
    instance.effectFile = original
    assert instance.effectFile == original



@given(instance=ck2gfx_MaskedShieldType_strategy)
def test_ck2gfx_maskedshieldtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ck2gfx_MaskedShieldType_strategy)
def test_ck2gfx_maskedshieldtype_clickSound_setter(instance):
    original = instance.clickSound
    instance.clickSound = original
    assert instance.clickSound == original



@given(instance=ck2gfx_MaskedShieldType_strategy)
def test_ck2gfx_maskedshieldtype_allwaysTransparent_setter(instance):
    original = instance.allwaysTransparent
    instance.allwaysTransparent = original
    assert instance.allwaysTransparent == original

@given(instance=ck2gfx_SpriteType_strategy)
@settings(max_examples=50)
def test_ck2gfx_spritetype_instantiation(instance):
    assert isinstance(instance, ck2gfx_SpriteType)



@given(instance=ck2gfx_SpriteType_strategy)
def test_ck2gfx_spritetype_textureFile_setter(instance):
    original = instance.textureFile
    instance.textureFile = original
    assert instance.textureFile == original



@given(instance=ck2gfx_SpriteType_strategy)
def test_ck2gfx_spritetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ck2gfx_SpriteType_strategy)
def test_ck2gfx_spritetype_effectFile_setter(instance):
    original = instance.effectFile
    instance.effectFile = original
    assert instance.effectFile == original



@given(instance=ck2gfx_SpriteType_strategy)
def test_ck2gfx_spritetype_canBeLowres_setter(instance):
    original = instance.canBeLowres
    instance.canBeLowres = original
    assert instance.canBeLowres == original



@given(instance=ck2gfx_SpriteType_strategy)
def test_ck2gfx_spritetype_noOfFrames_setter(instance):
    original = instance.noOfFrames
    instance.noOfFrames = original
    assert instance.noOfFrames == original



@given(instance=ck2gfx_SpriteType_strategy)
def test_ck2gfx_spritetype_loadType_setter(instance):
    original = instance.loadType
    instance.loadType = original
    assert instance.loadType == original



@given(instance=ck2gfx_SpriteType_strategy)
def test_ck2gfx_spritetype_transparenceCheck_setter(instance):
    original = instance.transparenceCheck
    instance.transparenceCheck = original
    assert instance.transparenceCheck == original



@given(instance=ck2gfx_SpriteType_strategy)
def test_ck2gfx_spritetype_clickSound_setter(instance):
    original = instance.clickSound
    instance.clickSound = original
    assert instance.clickSound == original



@given(instance=ck2gfx_SpriteType_strategy)
def test_ck2gfx_spritetype_allwaysTransparent_setter(instance):
    original = instance.allwaysTransparent
    instance.allwaysTransparent = original
    assert instance.allwaysTransparent == original



@given(instance=ck2gfx_SpriteType_strategy)
def test_ck2gfx_spritetype_noRefCount_setter(instance):
    original = instance.noRefCount
    instance.noRefCount = original
    assert instance.noRefCount == original

@given(instance=ck2gfx_SpriteTypes_strategy)
@settings(max_examples=50)
def test_ck2gfx_spritetypes_instantiation(instance):
    assert isinstance(instance, ck2gfx_SpriteTypes)

@given(instance=ck2gfx_ProgressbarType_strategy)
@settings(max_examples=50)
def test_ck2gfx_progressbartype_instantiation(instance):
    assert isinstance(instance, ck2gfx_ProgressbarType)



@given(instance=ck2gfx_ProgressbarType_strategy)
def test_ck2gfx_progressbartype_noRefCount_setter(instance):
    original = instance.noRefCount
    instance.noRefCount = original
    assert instance.noRefCount == original



@given(instance=ck2gfx_ProgressbarType_strategy)
def test_ck2gfx_progressbartype_textureFile2_setter(instance):
    original = instance.textureFile2
    instance.textureFile2 = original
    assert instance.textureFile2 == original



@given(instance=ck2gfx_ProgressbarType_strategy)
def test_ck2gfx_progressbartype_allwaysTransparent_setter(instance):
    original = instance.allwaysTransparent
    instance.allwaysTransparent = original
    assert instance.allwaysTransparent == original



@given(instance=ck2gfx_ProgressbarType_strategy)
def test_ck2gfx_progressbartype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ck2gfx_ProgressbarType_strategy)
def test_ck2gfx_progressbartype_textureFile1_setter(instance):
    original = instance.textureFile1
    instance.textureFile1 = original
    assert instance.textureFile1 == original



@given(instance=ck2gfx_ProgressbarType_strategy)
def test_ck2gfx_progressbartype_effectFile_setter(instance):
    original = instance.effectFile
    instance.effectFile = original
    assert instance.effectFile == original



@given(instance=ck2gfx_ProgressbarType_strategy)
def test_ck2gfx_progressbartype_horizontal_setter(instance):
    original = instance.horizontal
    instance.horizontal = original
    assert instance.horizontal == original



@given(instance=ck2gfx_ProgressbarType_strategy)
def test_ck2gfx_progressbartype_maxValue_setter(instance):
    original = instance.maxValue
    instance.maxValue = original
    assert instance.maxValue == original



@given(instance=ck2gfx_ProgressbarType_strategy)
def test_ck2gfx_progressbartype_loadType_setter(instance):
    original = instance.loadType
    instance.loadType = original
    assert instance.loadType == original

@given(instance=ck2gfx_CorneredTileSpriteType_strategy)
@settings(max_examples=50)
def test_ck2gfx_corneredtilespritetype_instantiation(instance):
    assert isinstance(instance, ck2gfx_CorneredTileSpriteType)



@given(instance=ck2gfx_CorneredTileSpriteType_strategy)
def test_ck2gfx_corneredtilespritetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ck2gfx_CorneredTileSpriteType_strategy)
def test_ck2gfx_corneredtilespritetype_noRefCount_setter(instance):
    original = instance.noRefCount
    instance.noRefCount = original
    assert instance.noRefCount == original



@given(instance=ck2gfx_CorneredTileSpriteType_strategy)
def test_ck2gfx_corneredtilespritetype_allwaysTransparent_setter(instance):
    original = instance.allwaysTransparent
    instance.allwaysTransparent = original
    assert instance.allwaysTransparent == original



@given(instance=ck2gfx_CorneredTileSpriteType_strategy)
def test_ck2gfx_corneredtilespritetype_texturefile_setter(instance):
    original = instance.texturefile
    instance.texturefile = original
    assert instance.texturefile == original



@given(instance=ck2gfx_CorneredTileSpriteType_strategy)
def test_ck2gfx_corneredtilespritetype_loadType_setter(instance):
    original = instance.loadType
    instance.loadType = original
    assert instance.loadType == original



@given(instance=ck2gfx_CorneredTileSpriteType_strategy)
def test_ck2gfx_corneredtilespritetype_tilingCenter_setter(instance):
    original = instance.tilingCenter
    instance.tilingCenter = original
    assert instance.tilingCenter == original

@given(instance=ck2gfx_AnimatedSpriteType_strategy)
@settings(max_examples=50)
def test_ck2gfx_animatedspritetype_instantiation(instance):
    assert isinstance(instance, ck2gfx_AnimatedSpriteType)



@given(instance=ck2gfx_AnimatedSpriteType_strategy)
def test_ck2gfx_animatedspritetype_looping_setter(instance):
    original = instance.looping
    instance.looping = original
    assert instance.looping == original



@given(instance=ck2gfx_AnimatedSpriteType_strategy)
def test_ck2gfx_animatedspritetype_animationRateFps_setter(instance):
    original = instance.animationRateFps
    instance.animationRateFps = original
    assert instance.animationRateFps == original



@given(instance=ck2gfx_AnimatedSpriteType_strategy)
def test_ck2gfx_animatedspritetype_noOfFrames_setter(instance):
    original = instance.noOfFrames
    instance.noOfFrames = original
    assert instance.noOfFrames == original



@given(instance=ck2gfx_AnimatedSpriteType_strategy)
def test_ck2gfx_animatedspritetype_texturefile_setter(instance):
    original = instance.texturefile
    instance.texturefile = original
    assert instance.texturefile == original



@given(instance=ck2gfx_AnimatedSpriteType_strategy)
def test_ck2gfx_animatedspritetype_playOnShow_setter(instance):
    original = instance.playOnShow
    instance.playOnShow = original
    assert instance.playOnShow == original



@given(instance=ck2gfx_AnimatedSpriteType_strategy)
def test_ck2gfx_animatedspritetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ck2gfx_Coordinates_strategy)
@settings(max_examples=50)
def test_ck2gfx_coordinates_instantiation(instance):
    assert isinstance(instance, ck2gfx_Coordinates)



@given(instance=ck2gfx_Coordinates_strategy)
def test_ck2gfx_coordinates_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=ck2gfx_Coordinates_strategy)
def test_ck2gfx_coordinates_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=ck2gfx_ColorRatio_strategy)
@settings(max_examples=50)
def test_ck2gfx_colorratio_instantiation(instance):
    assert isinstance(instance, ck2gfx_ColorRatio)



@given(instance=ck2gfx_ColorRatio_strategy)
def test_ck2gfx_colorratio_g_setter(instance):
    original = instance.g
    instance.g = original
    assert instance.g == original



@given(instance=ck2gfx_ColorRatio_strategy)
def test_ck2gfx_colorratio_r_setter(instance):
    original = instance.r
    instance.r = original
    assert instance.r == original



@given(instance=ck2gfx_ColorRatio_strategy)
def test_ck2gfx_colorratio_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=ck2gfx_Color_strategy)
@settings(max_examples=50)
def test_ck2gfx_color_instantiation(instance):
    assert isinstance(instance, ck2gfx_Color)



@given(instance=ck2gfx_Color_strategy)
def test_ck2gfx_color_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original



@given(instance=ck2gfx_Color_strategy)
def test_ck2gfx_color_r_setter(instance):
    original = instance.r
    instance.r = original
    assert instance.r == original



@given(instance=ck2gfx_Color_strategy)
def test_ck2gfx_color_g_setter(instance):
    original = instance.g
    instance.g = original
    assert instance.g == original

@given(instance=ck2gfx_EObject_strategy)
@settings(max_examples=50)
def test_ck2gfx_eobject_instantiation(instance):
    assert isinstance(instance, ck2gfx_EObject)

@given(instance=ck2gfx_Model_strategy)
@settings(max_examples=50)
def test_ck2gfx_model_instantiation(instance):
    assert isinstance(instance, ck2gfx_Model)
