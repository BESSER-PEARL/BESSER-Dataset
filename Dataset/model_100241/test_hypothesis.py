import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    presentation::EStringToStringMapEntry,
    presentation::DocumentRoot,
    presentation::ShowTextType,
    presentation::ShowShapeType,
    presentation::PlayType,
    presentation::ShowType,
    presentation::SettingsType,
    presentation::PlaceholderType,
    presentation::CustomShapeType,
    presentation::SceneType,
    presentation::ControlType,
    presentation::ConnectorType,
    presentation::CaptionType,
    presentation::MeasureType,
    presentation::FrameType,
    presentation::PageThumbnailType,
    presentation::PathType,
    presentation::GType,
    presentation::EllipseType,
    presentation::CircleType,
    presentation::PolylineType,
    presentation::LineType,
    presentation::RegularPolygonType,
    presentation::PolygonType,
    presentation::NotesType,
    presentation::RectType,
    presentation::FormsType,
    presentation::HideTextType,
    presentation::FooterDeclType,
    presentation::HideShapeType,
    presentation::HeaderType,
    presentation::HeaderDeclType,
    presentation::FooterType,
    presentation::DimType,
    presentation::DateTimeType,
    presentation::EventListenerType,
    presentation::SoundType,
    presentation::AnimationsType1,
    presentation::EObject,
    presentation::DateTimeDeclType,
    presentation::AnimationGroupType,
    TransitionOnClickType,
    VisibilityType,
    SourceType,
    PresetClassType,
    AnimationsType,
    TransitionStyleType,
    ActionType,
    TransitionTypeType,
    NodeTypeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_presentation::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(presentation::EStringToStringMapEntry)


def test_presentation::estringtostringmapentry_constructor_exists():
    assert callable(presentation::EStringToStringMapEntry.__init__)


def test_presentation::estringtostringmapentry_constructor_args():
    sig = inspect.signature(presentation::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_presentation::documentroot_is_not_abstract():
    assert not inspect.isabstract(presentation::DocumentRoot)


def test_presentation::documentroot_constructor_exists():
    assert callable(presentation::DocumentRoot.__init__)


def test_presentation::documentroot_constructor_args():
    sig = inspect.signature(presentation::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "pause" in params, "Missing parameter 'pause'"
    assert "displayHeader" in params, "Missing parameter 'displayHeader'"
    assert "pathId" in params, "Missing parameter 'pathId'"
    assert "displayDateTime" in params, "Missing parameter 'displayDateTime'"
    assert "source" in params, "Missing parameter 'source'"
    assert "action" in params, "Missing parameter 'action'"
    assert "animations1" in params, "Missing parameter 'animations1'"
    assert "transitionSpeed" in params, "Missing parameter 'transitionSpeed'"
    assert "name" in params, "Missing parameter 'name'"
    assert "delay" in params, "Missing parameter 'delay'"
    assert "presetClass" in params, "Missing parameter 'presetClass'"
    assert "transitionType" in params, "Missing parameter 'transitionType'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "placeholder1" in params, "Missing parameter 'placeholder1'"
    assert "endless" in params, "Missing parameter 'endless'"
    assert "startPage" in params, "Missing parameter 'startPage'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "displayPageNumber" in params, "Missing parameter 'displayPageNumber'"
    assert "displayFooter" in params, "Missing parameter 'displayFooter'"
    assert "playFull" in params, "Missing parameter 'playFull'"
    assert "presetSubType" in params, "Missing parameter 'presetSubType'"
    assert "userTransformed" in params, "Missing parameter 'userTransformed'"
    assert "transitionStyle" in params, "Missing parameter 'transitionStyle'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "stayOnTop" in params, "Missing parameter 'stayOnTop'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "showLogo" in params, "Missing parameter 'showLogo'"
    assert "mouseAsPen" in params, "Missing parameter 'mouseAsPen'"
    assert "styleName" in params, "Missing parameter 'styleName'"
    assert "presetId" in params, "Missing parameter 'presetId'"
    assert "startWithNavigator" in params, "Missing parameter 'startWithNavigator'"
    assert "masterElement" in params, "Missing parameter 'masterElement'"
    assert "presentationPageLayoutName" in params, "Missing parameter 'presentationPageLayoutName'"
    assert "forceManual" in params, "Missing parameter 'forceManual'"
    assert "groupId" in params, "Missing parameter 'groupId'"
    assert "useDateTimeName" in params, "Missing parameter 'useDateTimeName'"
    assert "showEndOfPresentationSlide" in params, "Missing parameter 'showEndOfPresentationSlide'"
    assert "show1" in params, "Missing parameter 'show1'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "useFooterName" in params, "Missing parameter 'useFooterName'"
    assert "backgroundVisible" in params, "Missing parameter 'backgroundVisible'"
    assert "fullScreen" in params, "Missing parameter 'fullScreen'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "startScale" in params, "Missing parameter 'startScale'"
    assert "useHeaderName" in params, "Missing parameter 'useHeaderName'"
    assert "mouseVisible" in params, "Missing parameter 'mouseVisible'"
    assert "verb" in params, "Missing parameter 'verb'"
    assert "classNames" in params, "Missing parameter 'classNames'"
    assert "backgroundObjectsVisible" in params, "Missing parameter 'backgroundObjectsVisible'"
    assert "nodeType" in params, "Missing parameter 'nodeType'"
    assert "transitionOnClick" in params, "Missing parameter 'transitionOnClick'"
    assert "speed" in params, "Missing parameter 'speed'"

def test_presentation::documentroot_has_pause():
    assert hasattr(presentation::DocumentRoot, "pause")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "pause" in klass.__dict__:
            descriptor = klass.__dict__["pause"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_displayHeader():
    assert hasattr(presentation::DocumentRoot, "displayHeader")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "displayHeader" in klass.__dict__:
            descriptor = klass.__dict__["displayHeader"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_pathId():
    assert hasattr(presentation::DocumentRoot, "pathId")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "pathId" in klass.__dict__:
            descriptor = klass.__dict__["pathId"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_displayDateTime():
    assert hasattr(presentation::DocumentRoot, "displayDateTime")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "displayDateTime" in klass.__dict__:
            descriptor = klass.__dict__["displayDateTime"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_source():
    assert hasattr(presentation::DocumentRoot, "source")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_action():
    assert hasattr(presentation::DocumentRoot, "action")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_animations1():
    assert hasattr(presentation::DocumentRoot, "animations1")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "animations1" in klass.__dict__:
            descriptor = klass.__dict__["animations1"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_transitionSpeed():
    assert hasattr(presentation::DocumentRoot, "transitionSpeed")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "transitionSpeed" in klass.__dict__:
            descriptor = klass.__dict__["transitionSpeed"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_name():
    assert hasattr(presentation::DocumentRoot, "name")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_delay():
    assert hasattr(presentation::DocumentRoot, "delay")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "delay" in klass.__dict__:
            descriptor = klass.__dict__["delay"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_presetClass():
    assert hasattr(presentation::DocumentRoot, "presetClass")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "presetClass" in klass.__dict__:
            descriptor = klass.__dict__["presetClass"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_transitionType():
    assert hasattr(presentation::DocumentRoot, "transitionType")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "transitionType" in klass.__dict__:
            descriptor = klass.__dict__["transitionType"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_visibility():
    assert hasattr(presentation::DocumentRoot, "visibility")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_placeholder1():
    assert hasattr(presentation::DocumentRoot, "placeholder1")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "placeholder1" in klass.__dict__:
            descriptor = klass.__dict__["placeholder1"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_endless():
    assert hasattr(presentation::DocumentRoot, "endless")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "endless" in klass.__dict__:
            descriptor = klass.__dict__["endless"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_startPage():
    assert hasattr(presentation::DocumentRoot, "startPage")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "startPage" in klass.__dict__:
            descriptor = klass.__dict__["startPage"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_class_():
    assert hasattr(presentation::DocumentRoot, "class_")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_displayPageNumber():
    assert hasattr(presentation::DocumentRoot, "displayPageNumber")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "displayPageNumber" in klass.__dict__:
            descriptor = klass.__dict__["displayPageNumber"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_displayFooter():
    assert hasattr(presentation::DocumentRoot, "displayFooter")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "displayFooter" in klass.__dict__:
            descriptor = klass.__dict__["displayFooter"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_playFull():
    assert hasattr(presentation::DocumentRoot, "playFull")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "playFull" in klass.__dict__:
            descriptor = klass.__dict__["playFull"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_presetSubType():
    assert hasattr(presentation::DocumentRoot, "presetSubType")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "presetSubType" in klass.__dict__:
            descriptor = klass.__dict__["presetSubType"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_userTransformed():
    assert hasattr(presentation::DocumentRoot, "userTransformed")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "userTransformed" in klass.__dict__:
            descriptor = klass.__dict__["userTransformed"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_transitionStyle():
    assert hasattr(presentation::DocumentRoot, "transitionStyle")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "transitionStyle" in klass.__dict__:
            descriptor = klass.__dict__["transitionStyle"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_pages():
    assert hasattr(presentation::DocumentRoot, "pages")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_stayOnTop():
    assert hasattr(presentation::DocumentRoot, "stayOnTop")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "stayOnTop" in klass.__dict__:
            descriptor = klass.__dict__["stayOnTop"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_effect():
    assert hasattr(presentation::DocumentRoot, "effect")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_showLogo():
    assert hasattr(presentation::DocumentRoot, "showLogo")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "showLogo" in klass.__dict__:
            descriptor = klass.__dict__["showLogo"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_mouseAsPen():
    assert hasattr(presentation::DocumentRoot, "mouseAsPen")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "mouseAsPen" in klass.__dict__:
            descriptor = klass.__dict__["mouseAsPen"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_styleName():
    assert hasattr(presentation::DocumentRoot, "styleName")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "styleName" in klass.__dict__:
            descriptor = klass.__dict__["styleName"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_presetId():
    assert hasattr(presentation::DocumentRoot, "presetId")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "presetId" in klass.__dict__:
            descriptor = klass.__dict__["presetId"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_startWithNavigator():
    assert hasattr(presentation::DocumentRoot, "startWithNavigator")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "startWithNavigator" in klass.__dict__:
            descriptor = klass.__dict__["startWithNavigator"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_masterElement():
    assert hasattr(presentation::DocumentRoot, "masterElement")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "masterElement" in klass.__dict__:
            descriptor = klass.__dict__["masterElement"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_presentationPageLayoutName():
    assert hasattr(presentation::DocumentRoot, "presentationPageLayoutName")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "presentationPageLayoutName" in klass.__dict__:
            descriptor = klass.__dict__["presentationPageLayoutName"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_forceManual():
    assert hasattr(presentation::DocumentRoot, "forceManual")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "forceManual" in klass.__dict__:
            descriptor = klass.__dict__["forceManual"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_groupId():
    assert hasattr(presentation::DocumentRoot, "groupId")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "groupId" in klass.__dict__:
            descriptor = klass.__dict__["groupId"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_useDateTimeName():
    assert hasattr(presentation::DocumentRoot, "useDateTimeName")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "useDateTimeName" in klass.__dict__:
            descriptor = klass.__dict__["useDateTimeName"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_showEndOfPresentationSlide():
    assert hasattr(presentation::DocumentRoot, "showEndOfPresentationSlide")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "showEndOfPresentationSlide" in klass.__dict__:
            descriptor = klass.__dict__["showEndOfPresentationSlide"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_show1():
    assert hasattr(presentation::DocumentRoot, "show1")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "show1" in klass.__dict__:
            descriptor = klass.__dict__["show1"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_duration():
    assert hasattr(presentation::DocumentRoot, "duration")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_useFooterName():
    assert hasattr(presentation::DocumentRoot, "useFooterName")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "useFooterName" in klass.__dict__:
            descriptor = klass.__dict__["useFooterName"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_backgroundVisible():
    assert hasattr(presentation::DocumentRoot, "backgroundVisible")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "backgroundVisible" in klass.__dict__:
            descriptor = klass.__dict__["backgroundVisible"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_fullScreen():
    assert hasattr(presentation::DocumentRoot, "fullScreen")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "fullScreen" in klass.__dict__:
            descriptor = klass.__dict__["fullScreen"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_direction():
    assert hasattr(presentation::DocumentRoot, "direction")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_mixed():
    assert hasattr(presentation::DocumentRoot, "mixed")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_startScale():
    assert hasattr(presentation::DocumentRoot, "startScale")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "startScale" in klass.__dict__:
            descriptor = klass.__dict__["startScale"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_useHeaderName():
    assert hasattr(presentation::DocumentRoot, "useHeaderName")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "useHeaderName" in klass.__dict__:
            descriptor = klass.__dict__["useHeaderName"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_mouseVisible():
    assert hasattr(presentation::DocumentRoot, "mouseVisible")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "mouseVisible" in klass.__dict__:
            descriptor = klass.__dict__["mouseVisible"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_verb():
    assert hasattr(presentation::DocumentRoot, "verb")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "verb" in klass.__dict__:
            descriptor = klass.__dict__["verb"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_classNames():
    assert hasattr(presentation::DocumentRoot, "classNames")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "classNames" in klass.__dict__:
            descriptor = klass.__dict__["classNames"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_backgroundObjectsVisible():
    assert hasattr(presentation::DocumentRoot, "backgroundObjectsVisible")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "backgroundObjectsVisible" in klass.__dict__:
            descriptor = klass.__dict__["backgroundObjectsVisible"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_nodeType():
    assert hasattr(presentation::DocumentRoot, "nodeType")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "nodeType" in klass.__dict__:
            descriptor = klass.__dict__["nodeType"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_transitionOnClick():
    assert hasattr(presentation::DocumentRoot, "transitionOnClick")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "transitionOnClick" in klass.__dict__:
            descriptor = klass.__dict__["transitionOnClick"]
            break
    assert isinstance(descriptor, property)

def test_presentation::documentroot_has_speed():
    assert hasattr(presentation::DocumentRoot, "speed")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::showtexttype_is_not_abstract():
    assert not inspect.isabstract(presentation::ShowTextType)


def test_presentation::showtexttype_constructor_exists():
    assert callable(presentation::ShowTextType.__init__)


def test_presentation::showtexttype_constructor_args():
    sig = inspect.signature(presentation::ShowTextType.__init__)
    params = list(sig.parameters.keys())
    assert "shapeId" in params, "Missing parameter 'shapeId'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "startScale" in params, "Missing parameter 'startScale'"
    assert "delay" in params, "Missing parameter 'delay'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "speed" in params, "Missing parameter 'speed'"
    assert "pathId" in params, "Missing parameter 'pathId'"

def test_presentation::showtexttype_has_shapeId():
    assert hasattr(presentation::ShowTextType, "shapeId")
    descriptor = None
    for klass in presentation::ShowTextType.__mro__:
        if "shapeId" in klass.__dict__:
            descriptor = klass.__dict__["shapeId"]
            break
    assert isinstance(descriptor, property)

def test_presentation::showtexttype_has_effect():
    assert hasattr(presentation::ShowTextType, "effect")
    descriptor = None
    for klass in presentation::ShowTextType.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_presentation::showtexttype_has_startScale():
    assert hasattr(presentation::ShowTextType, "startScale")
    descriptor = None
    for klass in presentation::ShowTextType.__mro__:
        if "startScale" in klass.__dict__:
            descriptor = klass.__dict__["startScale"]
            break
    assert isinstance(descriptor, property)

def test_presentation::showtexttype_has_delay():
    assert hasattr(presentation::ShowTextType, "delay")
    descriptor = None
    for klass in presentation::ShowTextType.__mro__:
        if "delay" in klass.__dict__:
            descriptor = klass.__dict__["delay"]
            break
    assert isinstance(descriptor, property)

def test_presentation::showtexttype_has_direction():
    assert hasattr(presentation::ShowTextType, "direction")
    descriptor = None
    for klass in presentation::ShowTextType.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_presentation::showtexttype_has_speed():
    assert hasattr(presentation::ShowTextType, "speed")
    descriptor = None
    for klass in presentation::ShowTextType.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_presentation::showtexttype_has_pathId():
    assert hasattr(presentation::ShowTextType, "pathId")
    descriptor = None
    for klass in presentation::ShowTextType.__mro__:
        if "pathId" in klass.__dict__:
            descriptor = klass.__dict__["pathId"]
            break
    assert isinstance(descriptor, property)



def test_presentation::showshapetype_is_not_abstract():
    assert not inspect.isabstract(presentation::ShowShapeType)


def test_presentation::showshapetype_constructor_exists():
    assert callable(presentation::ShowShapeType.__init__)


def test_presentation::showshapetype_constructor_args():
    sig = inspect.signature(presentation::ShowShapeType.__init__)
    params = list(sig.parameters.keys())
    assert "effect" in params, "Missing parameter 'effect'"
    assert "speed" in params, "Missing parameter 'speed'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "startScale" in params, "Missing parameter 'startScale'"
    assert "pathId" in params, "Missing parameter 'pathId'"
    assert "shapeId" in params, "Missing parameter 'shapeId'"
    assert "delay" in params, "Missing parameter 'delay'"

def test_presentation::showshapetype_has_effect():
    assert hasattr(presentation::ShowShapeType, "effect")
    descriptor = None
    for klass in presentation::ShowShapeType.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_presentation::showshapetype_has_speed():
    assert hasattr(presentation::ShowShapeType, "speed")
    descriptor = None
    for klass in presentation::ShowShapeType.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_presentation::showshapetype_has_direction():
    assert hasattr(presentation::ShowShapeType, "direction")
    descriptor = None
    for klass in presentation::ShowShapeType.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_presentation::showshapetype_has_startScale():
    assert hasattr(presentation::ShowShapeType, "startScale")
    descriptor = None
    for klass in presentation::ShowShapeType.__mro__:
        if "startScale" in klass.__dict__:
            descriptor = klass.__dict__["startScale"]
            break
    assert isinstance(descriptor, property)

def test_presentation::showshapetype_has_pathId():
    assert hasattr(presentation::ShowShapeType, "pathId")
    descriptor = None
    for klass in presentation::ShowShapeType.__mro__:
        if "pathId" in klass.__dict__:
            descriptor = klass.__dict__["pathId"]
            break
    assert isinstance(descriptor, property)

def test_presentation::showshapetype_has_shapeId():
    assert hasattr(presentation::ShowShapeType, "shapeId")
    descriptor = None
    for klass in presentation::ShowShapeType.__mro__:
        if "shapeId" in klass.__dict__:
            descriptor = klass.__dict__["shapeId"]
            break
    assert isinstance(descriptor, property)

def test_presentation::showshapetype_has_delay():
    assert hasattr(presentation::ShowShapeType, "delay")
    descriptor = None
    for klass in presentation::ShowShapeType.__mro__:
        if "delay" in klass.__dict__:
            descriptor = klass.__dict__["delay"]
            break
    assert isinstance(descriptor, property)



def test_presentation::playtype_is_not_abstract():
    assert not inspect.isabstract(presentation::PlayType)


def test_presentation::playtype_constructor_exists():
    assert callable(presentation::PlayType.__init__)


def test_presentation::playtype_constructor_args():
    sig = inspect.signature(presentation::PlayType.__init__)
    params = list(sig.parameters.keys())
    assert "shapeId" in params, "Missing parameter 'shapeId'"
    assert "speed" in params, "Missing parameter 'speed'"

def test_presentation::playtype_has_shapeId():
    assert hasattr(presentation::PlayType, "shapeId")
    descriptor = None
    for klass in presentation::PlayType.__mro__:
        if "shapeId" in klass.__dict__:
            descriptor = klass.__dict__["shapeId"]
            break
    assert isinstance(descriptor, property)

def test_presentation::playtype_has_speed():
    assert hasattr(presentation::PlayType, "speed")
    descriptor = None
    for klass in presentation::PlayType.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::showtype_is_not_abstract():
    assert not inspect.isabstract(presentation::ShowType)


def test_presentation::showtype_constructor_exists():
    assert callable(presentation::ShowType.__init__)


def test_presentation::showtype_constructor_args():
    sig = inspect.signature(presentation::ShowType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_presentation::showtype_has_name():
    assert hasattr(presentation::ShowType, "name")
    descriptor = None
    for klass in presentation::ShowType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_presentation::showtype_has_pages():
    assert hasattr(presentation::ShowType, "pages")
    descriptor = None
    for klass in presentation::ShowType.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)



def test_presentation::settingstype_is_not_abstract():
    assert not inspect.isabstract(presentation::SettingsType)


def test_presentation::settingstype_constructor_exists():
    assert callable(presentation::SettingsType.__init__)


def test_presentation::settingstype_constructor_args():
    sig = inspect.signature(presentation::SettingsType.__init__)
    params = list(sig.parameters.keys())
    assert "show1" in params, "Missing parameter 'show1'"
    assert "endless" in params, "Missing parameter 'endless'"
    assert "animations" in params, "Missing parameter 'animations'"
    assert "mouseAsPen" in params, "Missing parameter 'mouseAsPen'"
    assert "fullScreen" in params, "Missing parameter 'fullScreen'"
    assert "transitionOnClick" in params, "Missing parameter 'transitionOnClick'"
    assert "mouseVisible" in params, "Missing parameter 'mouseVisible'"
    assert "startWithNavigator" in params, "Missing parameter 'startWithNavigator'"
    assert "showLogo" in params, "Missing parameter 'showLogo'"
    assert "showEndOfPresentationSlide" in params, "Missing parameter 'showEndOfPresentationSlide'"
    assert "forceManual" in params, "Missing parameter 'forceManual'"
    assert "pause" in params, "Missing parameter 'pause'"
    assert "startPage" in params, "Missing parameter 'startPage'"
    assert "stayOnTop" in params, "Missing parameter 'stayOnTop'"

def test_presentation::settingstype_has_show1():
    assert hasattr(presentation::SettingsType, "show1")
    descriptor = None
    for klass in presentation::SettingsType.__mro__:
        if "show1" in klass.__dict__:
            descriptor = klass.__dict__["show1"]
            break
    assert isinstance(descriptor, property)

def test_presentation::settingstype_has_endless():
    assert hasattr(presentation::SettingsType, "endless")
    descriptor = None
    for klass in presentation::SettingsType.__mro__:
        if "endless" in klass.__dict__:
            descriptor = klass.__dict__["endless"]
            break
    assert isinstance(descriptor, property)

def test_presentation::settingstype_has_animations():
    assert hasattr(presentation::SettingsType, "animations")
    descriptor = None
    for klass in presentation::SettingsType.__mro__:
        if "animations" in klass.__dict__:
            descriptor = klass.__dict__["animations"]
            break
    assert isinstance(descriptor, property)

def test_presentation::settingstype_has_mouseAsPen():
    assert hasattr(presentation::SettingsType, "mouseAsPen")
    descriptor = None
    for klass in presentation::SettingsType.__mro__:
        if "mouseAsPen" in klass.__dict__:
            descriptor = klass.__dict__["mouseAsPen"]
            break
    assert isinstance(descriptor, property)

def test_presentation::settingstype_has_fullScreen():
    assert hasattr(presentation::SettingsType, "fullScreen")
    descriptor = None
    for klass in presentation::SettingsType.__mro__:
        if "fullScreen" in klass.__dict__:
            descriptor = klass.__dict__["fullScreen"]
            break
    assert isinstance(descriptor, property)

def test_presentation::settingstype_has_transitionOnClick():
    assert hasattr(presentation::SettingsType, "transitionOnClick")
    descriptor = None
    for klass in presentation::SettingsType.__mro__:
        if "transitionOnClick" in klass.__dict__:
            descriptor = klass.__dict__["transitionOnClick"]
            break
    assert isinstance(descriptor, property)

def test_presentation::settingstype_has_mouseVisible():
    assert hasattr(presentation::SettingsType, "mouseVisible")
    descriptor = None
    for klass in presentation::SettingsType.__mro__:
        if "mouseVisible" in klass.__dict__:
            descriptor = klass.__dict__["mouseVisible"]
            break
    assert isinstance(descriptor, property)

def test_presentation::settingstype_has_startWithNavigator():
    assert hasattr(presentation::SettingsType, "startWithNavigator")
    descriptor = None
    for klass in presentation::SettingsType.__mro__:
        if "startWithNavigator" in klass.__dict__:
            descriptor = klass.__dict__["startWithNavigator"]
            break
    assert isinstance(descriptor, property)

def test_presentation::settingstype_has_showLogo():
    assert hasattr(presentation::SettingsType, "showLogo")
    descriptor = None
    for klass in presentation::SettingsType.__mro__:
        if "showLogo" in klass.__dict__:
            descriptor = klass.__dict__["showLogo"]
            break
    assert isinstance(descriptor, property)

def test_presentation::settingstype_has_showEndOfPresentationSlide():
    assert hasattr(presentation::SettingsType, "showEndOfPresentationSlide")
    descriptor = None
    for klass in presentation::SettingsType.__mro__:
        if "showEndOfPresentationSlide" in klass.__dict__:
            descriptor = klass.__dict__["showEndOfPresentationSlide"]
            break
    assert isinstance(descriptor, property)

def test_presentation::settingstype_has_forceManual():
    assert hasattr(presentation::SettingsType, "forceManual")
    descriptor = None
    for klass in presentation::SettingsType.__mro__:
        if "forceManual" in klass.__dict__:
            descriptor = klass.__dict__["forceManual"]
            break
    assert isinstance(descriptor, property)

def test_presentation::settingstype_has_pause():
    assert hasattr(presentation::SettingsType, "pause")
    descriptor = None
    for klass in presentation::SettingsType.__mro__:
        if "pause" in klass.__dict__:
            descriptor = klass.__dict__["pause"]
            break
    assert isinstance(descriptor, property)

def test_presentation::settingstype_has_startPage():
    assert hasattr(presentation::SettingsType, "startPage")
    descriptor = None
    for klass in presentation::SettingsType.__mro__:
        if "startPage" in klass.__dict__:
            descriptor = klass.__dict__["startPage"]
            break
    assert isinstance(descriptor, property)

def test_presentation::settingstype_has_stayOnTop():
    assert hasattr(presentation::SettingsType, "stayOnTop")
    descriptor = None
    for klass in presentation::SettingsType.__mro__:
        if "stayOnTop" in klass.__dict__:
            descriptor = klass.__dict__["stayOnTop"]
            break
    assert isinstance(descriptor, property)



def test_presentation::placeholdertype_is_not_abstract():
    assert not inspect.isabstract(presentation::PlaceholderType)


def test_presentation::placeholdertype_constructor_exists():
    assert callable(presentation::PlaceholderType.__init__)


def test_presentation::placeholdertype_constructor_args():
    sig = inspect.signature(presentation::PlaceholderType.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"
    assert "object" in params, "Missing parameter 'object'"

def test_presentation::placeholdertype_has_height():
    assert hasattr(presentation::PlaceholderType, "height")
    descriptor = None
    for klass in presentation::PlaceholderType.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_presentation::placeholdertype_has_width():
    assert hasattr(presentation::PlaceholderType, "width")
    descriptor = None
    for klass in presentation::PlaceholderType.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_presentation::placeholdertype_has_y():
    assert hasattr(presentation::PlaceholderType, "y")
    descriptor = None
    for klass in presentation::PlaceholderType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_presentation::placeholdertype_has_x():
    assert hasattr(presentation::PlaceholderType, "x")
    descriptor = None
    for klass in presentation::PlaceholderType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_presentation::placeholdertype_has_object():
    assert hasattr(presentation::PlaceholderType, "object")
    descriptor = None
    for klass in presentation::PlaceholderType.__mro__:
        if "object" in klass.__dict__:
            descriptor = klass.__dict__["object"]
            break
    assert isinstance(descriptor, property)



def test_presentation::customshapetype_is_not_abstract():
    assert not inspect.isabstract(presentation::CustomShapeType)


def test_presentation::customshapetype_constructor_exists():
    assert callable(presentation::CustomShapeType.__init__)


def test_presentation::customshapetype_constructor_args():
    sig = inspect.signature(presentation::CustomShapeType.__init__)
    params = list(sig.parameters.keys())



def test_presentation::scenetype_is_not_abstract():
    assert not inspect.isabstract(presentation::SceneType)


def test_presentation::scenetype_constructor_exists():
    assert callable(presentation::SceneType.__init__)


def test_presentation::scenetype_constructor_args():
    sig = inspect.signature(presentation::SceneType.__init__)
    params = list(sig.parameters.keys())



def test_presentation::controltype_is_not_abstract():
    assert not inspect.isabstract(presentation::ControlType)


def test_presentation::controltype_constructor_exists():
    assert callable(presentation::ControlType.__init__)


def test_presentation::controltype_constructor_args():
    sig = inspect.signature(presentation::ControlType.__init__)
    params = list(sig.parameters.keys())



def test_presentation::connectortype_is_not_abstract():
    assert not inspect.isabstract(presentation::ConnectorType)


def test_presentation::connectortype_constructor_exists():
    assert callable(presentation::ConnectorType.__init__)


def test_presentation::connectortype_constructor_args():
    sig = inspect.signature(presentation::ConnectorType.__init__)
    params = list(sig.parameters.keys())



def test_presentation::captiontype_is_not_abstract():
    assert not inspect.isabstract(presentation::CaptionType)


def test_presentation::captiontype_constructor_exists():
    assert callable(presentation::CaptionType.__init__)


def test_presentation::captiontype_constructor_args():
    sig = inspect.signature(presentation::CaptionType.__init__)
    params = list(sig.parameters.keys())



def test_presentation::measuretype_is_not_abstract():
    assert not inspect.isabstract(presentation::MeasureType)


def test_presentation::measuretype_constructor_exists():
    assert callable(presentation::MeasureType.__init__)


def test_presentation::measuretype_constructor_args():
    sig = inspect.signature(presentation::MeasureType.__init__)
    params = list(sig.parameters.keys())



def test_presentation::frametype_is_not_abstract():
    assert not inspect.isabstract(presentation::FrameType)


def test_presentation::frametype_constructor_exists():
    assert callable(presentation::FrameType.__init__)


def test_presentation::frametype_constructor_args():
    sig = inspect.signature(presentation::FrameType.__init__)
    params = list(sig.parameters.keys())



def test_presentation::pagethumbnailtype_is_not_abstract():
    assert not inspect.isabstract(presentation::PageThumbnailType)


def test_presentation::pagethumbnailtype_constructor_exists():
    assert callable(presentation::PageThumbnailType.__init__)


def test_presentation::pagethumbnailtype_constructor_args():
    sig = inspect.signature(presentation::PageThumbnailType.__init__)
    params = list(sig.parameters.keys())



def test_presentation::pathtype_is_not_abstract():
    assert not inspect.isabstract(presentation::PathType)


def test_presentation::pathtype_constructor_exists():
    assert callable(presentation::PathType.__init__)


def test_presentation::pathtype_constructor_args():
    sig = inspect.signature(presentation::PathType.__init__)
    params = list(sig.parameters.keys())



def test_presentation::gtype_is_not_abstract():
    assert not inspect.isabstract(presentation::GType)


def test_presentation::gtype_constructor_exists():
    assert callable(presentation::GType.__init__)


def test_presentation::gtype_constructor_args():
    sig = inspect.signature(presentation::GType.__init__)
    params = list(sig.parameters.keys())



def test_presentation::ellipsetype_is_not_abstract():
    assert not inspect.isabstract(presentation::EllipseType)


def test_presentation::ellipsetype_constructor_exists():
    assert callable(presentation::EllipseType.__init__)


def test_presentation::ellipsetype_constructor_args():
    sig = inspect.signature(presentation::EllipseType.__init__)
    params = list(sig.parameters.keys())



def test_presentation::circletype_is_not_abstract():
    assert not inspect.isabstract(presentation::CircleType)


def test_presentation::circletype_constructor_exists():
    assert callable(presentation::CircleType.__init__)


def test_presentation::circletype_constructor_args():
    sig = inspect.signature(presentation::CircleType.__init__)
    params = list(sig.parameters.keys())



def test_presentation::polylinetype_is_not_abstract():
    assert not inspect.isabstract(presentation::PolylineType)


def test_presentation::polylinetype_constructor_exists():
    assert callable(presentation::PolylineType.__init__)


def test_presentation::polylinetype_constructor_args():
    sig = inspect.signature(presentation::PolylineType.__init__)
    params = list(sig.parameters.keys())



def test_presentation::linetype_is_not_abstract():
    assert not inspect.isabstract(presentation::LineType)


def test_presentation::linetype_constructor_exists():
    assert callable(presentation::LineType.__init__)


def test_presentation::linetype_constructor_args():
    sig = inspect.signature(presentation::LineType.__init__)
    params = list(sig.parameters.keys())



def test_presentation::regularpolygontype_is_not_abstract():
    assert not inspect.isabstract(presentation::RegularPolygonType)


def test_presentation::regularpolygontype_constructor_exists():
    assert callable(presentation::RegularPolygonType.__init__)


def test_presentation::regularpolygontype_constructor_args():
    sig = inspect.signature(presentation::RegularPolygonType.__init__)
    params = list(sig.parameters.keys())



def test_presentation::polygontype_is_not_abstract():
    assert not inspect.isabstract(presentation::PolygonType)


def test_presentation::polygontype_constructor_exists():
    assert callable(presentation::PolygonType.__init__)


def test_presentation::polygontype_constructor_args():
    sig = inspect.signature(presentation::PolygonType.__init__)
    params = list(sig.parameters.keys())



def test_presentation::notestype_is_not_abstract():
    assert not inspect.isabstract(presentation::NotesType)


def test_presentation::notestype_constructor_exists():
    assert callable(presentation::NotesType.__init__)


def test_presentation::notestype_constructor_args():
    sig = inspect.signature(presentation::NotesType.__init__)
    params = list(sig.parameters.keys())
    assert "useFooterName" in params, "Missing parameter 'useFooterName'"
    assert "pageLayoutName" in params, "Missing parameter 'pageLayoutName'"
    assert "styleName" in params, "Missing parameter 'styleName'"
    assert "shape" in params, "Missing parameter 'shape'"
    assert "useHeaderName" in params, "Missing parameter 'useHeaderName'"
    assert "useDateTimeName" in params, "Missing parameter 'useDateTimeName'"

def test_presentation::notestype_has_useFooterName():
    assert hasattr(presentation::NotesType, "useFooterName")
    descriptor = None
    for klass in presentation::NotesType.__mro__:
        if "useFooterName" in klass.__dict__:
            descriptor = klass.__dict__["useFooterName"]
            break
    assert isinstance(descriptor, property)

def test_presentation::notestype_has_pageLayoutName():
    assert hasattr(presentation::NotesType, "pageLayoutName")
    descriptor = None
    for klass in presentation::NotesType.__mro__:
        if "pageLayoutName" in klass.__dict__:
            descriptor = klass.__dict__["pageLayoutName"]
            break
    assert isinstance(descriptor, property)

def test_presentation::notestype_has_styleName():
    assert hasattr(presentation::NotesType, "styleName")
    descriptor = None
    for klass in presentation::NotesType.__mro__:
        if "styleName" in klass.__dict__:
            descriptor = klass.__dict__["styleName"]
            break
    assert isinstance(descriptor, property)

def test_presentation::notestype_has_shape():
    assert hasattr(presentation::NotesType, "shape")
    descriptor = None
    for klass in presentation::NotesType.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)

def test_presentation::notestype_has_useHeaderName():
    assert hasattr(presentation::NotesType, "useHeaderName")
    descriptor = None
    for klass in presentation::NotesType.__mro__:
        if "useHeaderName" in klass.__dict__:
            descriptor = klass.__dict__["useHeaderName"]
            break
    assert isinstance(descriptor, property)

def test_presentation::notestype_has_useDateTimeName():
    assert hasattr(presentation::NotesType, "useDateTimeName")
    descriptor = None
    for klass in presentation::NotesType.__mro__:
        if "useDateTimeName" in klass.__dict__:
            descriptor = klass.__dict__["useDateTimeName"]
            break
    assert isinstance(descriptor, property)



def test_presentation::recttype_is_not_abstract():
    assert not inspect.isabstract(presentation::RectType)


def test_presentation::recttype_constructor_exists():
    assert callable(presentation::RectType.__init__)


def test_presentation::recttype_constructor_args():
    sig = inspect.signature(presentation::RectType.__init__)
    params = list(sig.parameters.keys())



def test_presentation::formstype_is_not_abstract():
    assert not inspect.isabstract(presentation::FormsType)


def test_presentation::formstype_constructor_exists():
    assert callable(presentation::FormsType.__init__)


def test_presentation::formstype_constructor_args():
    sig = inspect.signature(presentation::FormsType.__init__)
    params = list(sig.parameters.keys())



def test_presentation::hidetexttype_is_not_abstract():
    assert not inspect.isabstract(presentation::HideTextType)


def test_presentation::hidetexttype_constructor_exists():
    assert callable(presentation::HideTextType.__init__)


def test_presentation::hidetexttype_constructor_args():
    sig = inspect.signature(presentation::HideTextType.__init__)
    params = list(sig.parameters.keys())
    assert "shapeId" in params, "Missing parameter 'shapeId'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "pathId" in params, "Missing parameter 'pathId'"
    assert "startScale" in params, "Missing parameter 'startScale'"
    assert "delay" in params, "Missing parameter 'delay'"
    assert "speed" in params, "Missing parameter 'speed'"
    assert "effect" in params, "Missing parameter 'effect'"

def test_presentation::hidetexttype_has_shapeId():
    assert hasattr(presentation::HideTextType, "shapeId")
    descriptor = None
    for klass in presentation::HideTextType.__mro__:
        if "shapeId" in klass.__dict__:
            descriptor = klass.__dict__["shapeId"]
            break
    assert isinstance(descriptor, property)

def test_presentation::hidetexttype_has_direction():
    assert hasattr(presentation::HideTextType, "direction")
    descriptor = None
    for klass in presentation::HideTextType.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_presentation::hidetexttype_has_pathId():
    assert hasattr(presentation::HideTextType, "pathId")
    descriptor = None
    for klass in presentation::HideTextType.__mro__:
        if "pathId" in klass.__dict__:
            descriptor = klass.__dict__["pathId"]
            break
    assert isinstance(descriptor, property)

def test_presentation::hidetexttype_has_startScale():
    assert hasattr(presentation::HideTextType, "startScale")
    descriptor = None
    for klass in presentation::HideTextType.__mro__:
        if "startScale" in klass.__dict__:
            descriptor = klass.__dict__["startScale"]
            break
    assert isinstance(descriptor, property)

def test_presentation::hidetexttype_has_delay():
    assert hasattr(presentation::HideTextType, "delay")
    descriptor = None
    for klass in presentation::HideTextType.__mro__:
        if "delay" in klass.__dict__:
            descriptor = klass.__dict__["delay"]
            break
    assert isinstance(descriptor, property)

def test_presentation::hidetexttype_has_speed():
    assert hasattr(presentation::HideTextType, "speed")
    descriptor = None
    for klass in presentation::HideTextType.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_presentation::hidetexttype_has_effect():
    assert hasattr(presentation::HideTextType, "effect")
    descriptor = None
    for klass in presentation::HideTextType.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)



def test_presentation::footerdecltype_is_not_abstract():
    assert not inspect.isabstract(presentation::FooterDeclType)


def test_presentation::footerdecltype_constructor_exists():
    assert callable(presentation::FooterDeclType.__init__)


def test_presentation::footerdecltype_constructor_args():
    sig = inspect.signature(presentation::FooterDeclType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "name" in params, "Missing parameter 'name'"

def test_presentation::footerdecltype_has_mixed():
    assert hasattr(presentation::FooterDeclType, "mixed")
    descriptor = None
    for klass in presentation::FooterDeclType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_presentation::footerdecltype_has_name():
    assert hasattr(presentation::FooterDeclType, "name")
    descriptor = None
    for klass in presentation::FooterDeclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_presentation::hideshapetype_is_not_abstract():
    assert not inspect.isabstract(presentation::HideShapeType)


def test_presentation::hideshapetype_constructor_exists():
    assert callable(presentation::HideShapeType.__init__)


def test_presentation::hideshapetype_constructor_args():
    sig = inspect.signature(presentation::HideShapeType.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "pathId" in params, "Missing parameter 'pathId'"
    assert "speed" in params, "Missing parameter 'speed'"
    assert "delay" in params, "Missing parameter 'delay'"
    assert "shapeId" in params, "Missing parameter 'shapeId'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "startScale" in params, "Missing parameter 'startScale'"

def test_presentation::hideshapetype_has_direction():
    assert hasattr(presentation::HideShapeType, "direction")
    descriptor = None
    for klass in presentation::HideShapeType.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_presentation::hideshapetype_has_pathId():
    assert hasattr(presentation::HideShapeType, "pathId")
    descriptor = None
    for klass in presentation::HideShapeType.__mro__:
        if "pathId" in klass.__dict__:
            descriptor = klass.__dict__["pathId"]
            break
    assert isinstance(descriptor, property)

def test_presentation::hideshapetype_has_speed():
    assert hasattr(presentation::HideShapeType, "speed")
    descriptor = None
    for klass in presentation::HideShapeType.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_presentation::hideshapetype_has_delay():
    assert hasattr(presentation::HideShapeType, "delay")
    descriptor = None
    for klass in presentation::HideShapeType.__mro__:
        if "delay" in klass.__dict__:
            descriptor = klass.__dict__["delay"]
            break
    assert isinstance(descriptor, property)

def test_presentation::hideshapetype_has_shapeId():
    assert hasattr(presentation::HideShapeType, "shapeId")
    descriptor = None
    for klass in presentation::HideShapeType.__mro__:
        if "shapeId" in klass.__dict__:
            descriptor = klass.__dict__["shapeId"]
            break
    assert isinstance(descriptor, property)

def test_presentation::hideshapetype_has_effect():
    assert hasattr(presentation::HideShapeType, "effect")
    descriptor = None
    for klass in presentation::HideShapeType.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_presentation::hideshapetype_has_startScale():
    assert hasattr(presentation::HideShapeType, "startScale")
    descriptor = None
    for klass in presentation::HideShapeType.__mro__:
        if "startScale" in klass.__dict__:
            descriptor = klass.__dict__["startScale"]
            break
    assert isinstance(descriptor, property)



def test_presentation::headertype_is_not_abstract():
    assert not inspect.isabstract(presentation::HeaderType)


def test_presentation::headertype_constructor_exists():
    assert callable(presentation::HeaderType.__init__)


def test_presentation::headertype_constructor_args():
    sig = inspect.signature(presentation::HeaderType.__init__)
    params = list(sig.parameters.keys())



def test_presentation::headerdecltype_is_not_abstract():
    assert not inspect.isabstract(presentation::HeaderDeclType)


def test_presentation::headerdecltype_constructor_exists():
    assert callable(presentation::HeaderDeclType.__init__)


def test_presentation::headerdecltype_constructor_args():
    sig = inspect.signature(presentation::HeaderDeclType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::headerdecltype_has_name():
    assert hasattr(presentation::HeaderDeclType, "name")
    descriptor = None
    for klass in presentation::HeaderDeclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_presentation::headerdecltype_has_mixed():
    assert hasattr(presentation::HeaderDeclType, "mixed")
    descriptor = None
    for klass in presentation::HeaderDeclType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::footertype_is_not_abstract():
    assert not inspect.isabstract(presentation::FooterType)


def test_presentation::footertype_constructor_exists():
    assert callable(presentation::FooterType.__init__)


def test_presentation::footertype_constructor_args():
    sig = inspect.signature(presentation::FooterType.__init__)
    params = list(sig.parameters.keys())



def test_presentation::dimtype_is_not_abstract():
    assert not inspect.isabstract(presentation::DimType)


def test_presentation::dimtype_constructor_exists():
    assert callable(presentation::DimType.__init__)


def test_presentation::dimtype_constructor_args():
    sig = inspect.signature(presentation::DimType.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "shapeId" in params, "Missing parameter 'shapeId'"

def test_presentation::dimtype_has_color():
    assert hasattr(presentation::DimType, "color")
    descriptor = None
    for klass in presentation::DimType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_presentation::dimtype_has_shapeId():
    assert hasattr(presentation::DimType, "shapeId")
    descriptor = None
    for klass in presentation::DimType.__mro__:
        if "shapeId" in klass.__dict__:
            descriptor = klass.__dict__["shapeId"]
            break
    assert isinstance(descriptor, property)



def test_presentation::datetimetype_is_not_abstract():
    assert not inspect.isabstract(presentation::DateTimeType)


def test_presentation::datetimetype_constructor_exists():
    assert callable(presentation::DateTimeType.__init__)


def test_presentation::datetimetype_constructor_args():
    sig = inspect.signature(presentation::DateTimeType.__init__)
    params = list(sig.parameters.keys())



def test_presentation::eventlistenertype_is_not_abstract():
    assert not inspect.isabstract(presentation::EventListenerType)


def test_presentation::eventlistenertype_constructor_exists():
    assert callable(presentation::EventListenerType.__init__)


def test_presentation::eventlistenertype_constructor_args():
    sig = inspect.signature(presentation::EventListenerType.__init__)
    params = list(sig.parameters.keys())
    assert "verb" in params, "Missing parameter 'verb'"
    assert "eventName" in params, "Missing parameter 'eventName'"
    assert "actuate" in params, "Missing parameter 'actuate'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "speed" in params, "Missing parameter 'speed'"
    assert "show" in params, "Missing parameter 'show'"
    assert "type" in params, "Missing parameter 'type'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "startScale" in params, "Missing parameter 'startScale'"
    assert "href" in params, "Missing parameter 'href'"
    assert "action" in params, "Missing parameter 'action'"

def test_presentation::eventlistenertype_has_verb():
    assert hasattr(presentation::EventListenerType, "verb")
    descriptor = None
    for klass in presentation::EventListenerType.__mro__:
        if "verb" in klass.__dict__:
            descriptor = klass.__dict__["verb"]
            break
    assert isinstance(descriptor, property)

def test_presentation::eventlistenertype_has_eventName():
    assert hasattr(presentation::EventListenerType, "eventName")
    descriptor = None
    for klass in presentation::EventListenerType.__mro__:
        if "eventName" in klass.__dict__:
            descriptor = klass.__dict__["eventName"]
            break
    assert isinstance(descriptor, property)

def test_presentation::eventlistenertype_has_actuate():
    assert hasattr(presentation::EventListenerType, "actuate")
    descriptor = None
    for klass in presentation::EventListenerType.__mro__:
        if "actuate" in klass.__dict__:
            descriptor = klass.__dict__["actuate"]
            break
    assert isinstance(descriptor, property)

def test_presentation::eventlistenertype_has_direction():
    assert hasattr(presentation::EventListenerType, "direction")
    descriptor = None
    for klass in presentation::EventListenerType.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_presentation::eventlistenertype_has_speed():
    assert hasattr(presentation::EventListenerType, "speed")
    descriptor = None
    for klass in presentation::EventListenerType.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_presentation::eventlistenertype_has_show():
    assert hasattr(presentation::EventListenerType, "show")
    descriptor = None
    for klass in presentation::EventListenerType.__mro__:
        if "show" in klass.__dict__:
            descriptor = klass.__dict__["show"]
            break
    assert isinstance(descriptor, property)

def test_presentation::eventlistenertype_has_type():
    assert hasattr(presentation::EventListenerType, "type")
    descriptor = None
    for klass in presentation::EventListenerType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_presentation::eventlistenertype_has_effect():
    assert hasattr(presentation::EventListenerType, "effect")
    descriptor = None
    for klass in presentation::EventListenerType.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_presentation::eventlistenertype_has_startScale():
    assert hasattr(presentation::EventListenerType, "startScale")
    descriptor = None
    for klass in presentation::EventListenerType.__mro__:
        if "startScale" in klass.__dict__:
            descriptor = klass.__dict__["startScale"]
            break
    assert isinstance(descriptor, property)

def test_presentation::eventlistenertype_has_href():
    assert hasattr(presentation::EventListenerType, "href")
    descriptor = None
    for klass in presentation::EventListenerType.__mro__:
        if "href" in klass.__dict__:
            descriptor = klass.__dict__["href"]
            break
    assert isinstance(descriptor, property)

def test_presentation::eventlistenertype_has_action():
    assert hasattr(presentation::EventListenerType, "action")
    descriptor = None
    for klass in presentation::EventListenerType.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_presentation::soundtype_is_not_abstract():
    assert not inspect.isabstract(presentation::SoundType)


def test_presentation::soundtype_constructor_exists():
    assert callable(presentation::SoundType.__init__)


def test_presentation::soundtype_constructor_args():
    sig = inspect.signature(presentation::SoundType.__init__)
    params = list(sig.parameters.keys())
    assert "href" in params, "Missing parameter 'href'"
    assert "type" in params, "Missing parameter 'type'"
    assert "actuate" in params, "Missing parameter 'actuate'"
    assert "show" in params, "Missing parameter 'show'"
    assert "playFull" in params, "Missing parameter 'playFull'"

def test_presentation::soundtype_has_href():
    assert hasattr(presentation::SoundType, "href")
    descriptor = None
    for klass in presentation::SoundType.__mro__:
        if "href" in klass.__dict__:
            descriptor = klass.__dict__["href"]
            break
    assert isinstance(descriptor, property)

def test_presentation::soundtype_has_type():
    assert hasattr(presentation::SoundType, "type")
    descriptor = None
    for klass in presentation::SoundType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_presentation::soundtype_has_actuate():
    assert hasattr(presentation::SoundType, "actuate")
    descriptor = None
    for klass in presentation::SoundType.__mro__:
        if "actuate" in klass.__dict__:
            descriptor = klass.__dict__["actuate"]
            break
    assert isinstance(descriptor, property)

def test_presentation::soundtype_has_show():
    assert hasattr(presentation::SoundType, "show")
    descriptor = None
    for klass in presentation::SoundType.__mro__:
        if "show" in klass.__dict__:
            descriptor = klass.__dict__["show"]
            break
    assert isinstance(descriptor, property)

def test_presentation::soundtype_has_playFull():
    assert hasattr(presentation::SoundType, "playFull")
    descriptor = None
    for klass in presentation::SoundType.__mro__:
        if "playFull" in klass.__dict__:
            descriptor = klass.__dict__["playFull"]
            break
    assert isinstance(descriptor, property)



def test_presentation::animationstype1_is_not_abstract():
    assert not inspect.isabstract(presentation::AnimationsType1)


def test_presentation::animationstype1_constructor_exists():
    assert callable(presentation::AnimationsType1.__init__)


def test_presentation::animationstype1_constructor_args():
    sig = inspect.signature(presentation::AnimationsType1.__init__)
    params = list(sig.parameters.keys())
    assert "presentationAnimationElementsGroup" in params, "Missing parameter 'presentationAnimationElementsGroup'"
    assert "group" in params, "Missing parameter 'group'"

def test_presentation::animationstype1_has_presentationAnimationElementsGroup():
    assert hasattr(presentation::AnimationsType1, "presentationAnimationElementsGroup")
    descriptor = None
    for klass in presentation::AnimationsType1.__mro__:
        if "presentationAnimationElementsGroup" in klass.__dict__:
            descriptor = klass.__dict__["presentationAnimationElementsGroup"]
            break
    assert isinstance(descriptor, property)

def test_presentation::animationstype1_has_group():
    assert hasattr(presentation::AnimationsType1, "group")
    descriptor = None
    for klass in presentation::AnimationsType1.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_presentation::eobject_is_not_abstract():
    assert not inspect.isabstract(presentation::EObject)


def test_presentation::eobject_constructor_exists():
    assert callable(presentation::EObject.__init__)


def test_presentation::eobject_constructor_args():
    sig = inspect.signature(presentation::EObject.__init__)
    params = list(sig.parameters.keys())



def test_presentation::datetimedecltype_is_not_abstract():
    assert not inspect.isabstract(presentation::DateTimeDeclType)


def test_presentation::datetimedecltype_constructor_exists():
    assert callable(presentation::DateTimeDeclType.__init__)


def test_presentation::datetimedecltype_constructor_args():
    sig = inspect.signature(presentation::DateTimeDeclType.__init__)
    params = list(sig.parameters.keys())
    assert "dataStyleName" in params, "Missing parameter 'dataStyleName'"
    assert "source" in params, "Missing parameter 'source'"
    assert "name" in params, "Missing parameter 'name'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::datetimedecltype_has_dataStyleName():
    assert hasattr(presentation::DateTimeDeclType, "dataStyleName")
    descriptor = None
    for klass in presentation::DateTimeDeclType.__mro__:
        if "dataStyleName" in klass.__dict__:
            descriptor = klass.__dict__["dataStyleName"]
            break
    assert isinstance(descriptor, property)

def test_presentation::datetimedecltype_has_source():
    assert hasattr(presentation::DateTimeDeclType, "source")
    descriptor = None
    for klass in presentation::DateTimeDeclType.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_presentation::datetimedecltype_has_name():
    assert hasattr(presentation::DateTimeDeclType, "name")
    descriptor = None
    for klass in presentation::DateTimeDeclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_presentation::datetimedecltype_has_mixed():
    assert hasattr(presentation::DateTimeDeclType, "mixed")
    descriptor = None
    for klass in presentation::DateTimeDeclType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::animationgrouptype_is_not_abstract():
    assert not inspect.isabstract(presentation::AnimationGroupType)


def test_presentation::animationgrouptype_constructor_exists():
    assert callable(presentation::AnimationGroupType.__init__)


def test_presentation::animationgrouptype_constructor_args():
    sig = inspect.signature(presentation::AnimationGroupType.__init__)
    params = list(sig.parameters.keys())
    assert "presentationAnimationElementsGroup" in params, "Missing parameter 'presentationAnimationElementsGroup'"

def test_presentation::animationgrouptype_has_presentationAnimationElementsGroup():
    assert hasattr(presentation::AnimationGroupType, "presentationAnimationElementsGroup")
    descriptor = None
    for klass in presentation::AnimationGroupType.__mro__:
        if "presentationAnimationElementsGroup" in klass.__dict__:
            descriptor = klass.__dict__["presentationAnimationElementsGroup"]
            break
    assert isinstance(descriptor, property)

def test_transitiononclicktype_exists():
    # Check that the Enumeration exists
    assert TransitionOnClickType is not None

def test_transitiononclicktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionOnClickType]
    expected_literals = [
        "disabled",
        "enabled",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionOnClickType"

def test_visibilitytype_exists():
    # Check that the Enumeration exists
    assert VisibilityType is not None

def test_visibilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityType]
    expected_literals = [
        "hidden",
        "visible",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityType"

def test_sourcetype_exists():
    # Check that the Enumeration exists
    assert SourceType is not None

def test_sourcetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SourceType]
    expected_literals = [
        "currentDate",
        "fixed",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SourceType"

def test_presetclasstype_exists():
    # Check that the Enumeration exists
    assert PresetClassType is not None

def test_presetclasstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PresetClassType]
    expected_literals = [
        "mediaCall",
        "exit",
        "oleAction",
        "emphasis",
        "custom",
        "entrance",
        "motionPath",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PresetClassType"

def test_animationstype_exists():
    # Check that the Enumeration exists
    assert AnimationsType is not None

def test_animationstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AnimationsType]
    expected_literals = [
        "disabled",
        "enabled",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AnimationsType"

def test_transitionstyletype_exists():
    # Check that the Enumeration exists
    assert TransitionStyleType is not None

def test_transitionstyletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionStyleType]
    expected_literals = [
        "moveFromLowerleft",
        "fadeFromLeft",
        "melt",
        "uncoverToLowerright",
        "fadeFromRight",
        "moveFromUpperleft",
        "closeHorizontal",
        "none",
        "fadeFromUpperleft",
        "rollFromLeft",
        "spiraloutRight",
        "closeVertical",
        "stretchFromLeft",
        "open",
        "stretchFromBottom",
        "verticalStripes",
        "random",
        "fadeToCenter",
        "clockwise",
        "fadeFromBottom",
        "wavylineFromTop",
        "moveFromRight",
        "openHorizontal",
        "close",
        "moveFromBottom",
        "moveFromLeft",
        "horizontalCheckerboard",
        "counterclockwise",
        "moveFromUpperright",
        "uncoverToRight",
        "fadeFromTop",
        "fadeFromLowerright",
        "moveFromLowerright",
        "rollFromTop",
        "dissolve",
        "interlockingVerticalTop",
        "stretchFromTop",
        "uncoverToLeft",
        "moveFromTop",
        "horizontalStripes",
        "fadeFromCenter",
        "verticalLines",
        "interlockingVerticalBottom",
        "fadeFromUpperright",
        "uncoverToBottom",
        "wavylineFromBottom",
        "horizontalLines",
        "fadeFromLowerleft",
        "rollFromBottom",
        "interlockingHorizontalLeft",
        "uncoverToLowerleft",
        "uncoverToTop",
        "spiralinRight",
        "rollFromRight",
        "interlockingHorizontalRight",
        "openVertical",
        "wavylineFromRight",
        "uncoverToUpperleft",
        "flyAway",
        "wavylineFromLeft",
        "spiralinLeft",
        "spiraloutLeft",
        "uncoverToUpperright",
        "stretchFromRight",
        "verticalCheckerboard",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionStyleType"

def test_actiontype_exists():
    # Check that the Enumeration exists
    assert ActionType is not None

def test_actiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionType]
    expected_literals = [
        "fadeOut",
        "nextPage",
        "execute",
        "sound",
        "hide",
        "verb",
        "show",
        "lastPage",
        "stop",
        "none",
        "previousPage",
        "firstPage",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionType"

def test_transitiontypetype_exists():
    # Check that the Enumeration exists
    assert TransitionTypeType is not None

def test_transitiontypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionTypeType]
    expected_literals = [
        "semiAutomatic",
        "automatic",
        "manual",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionTypeType"

def test_nodetypetype_exists():
    # Check that the Enumeration exists
    assert NodeTypeType is not None

def test_nodetypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NodeTypeType]
    expected_literals = [
        "timingRoot",
        "interactiveSequence",
        "default",
        "afterPrevious",
        "mainSequence",
        "withPrevious",
        "onClick",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NodeTypeType"


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
presentation::EStringToStringMapEntry_strategy = st.builds(
    presentation::EStringToStringMapEntry,
)
presentation::DocumentRoot_strategy = st.builds(
    presentation::DocumentRoot,
    pause=
        safe_text,
    displayHeader=
        safe_text,
    pathId=
        safe_text,
    displayDateTime=
        safe_text,
    source=
        safe_text,
    action=
        safe_text,
    animations1=
        safe_text,
    transitionSpeed=
        safe_text,
    name=
        safe_text,
    delay=
        safe_text,
    presetClass=
        safe_text,
    transitionType=
        safe_text,
    visibility=
        safe_text,
    placeholder1=
        safe_text,
    endless=
        safe_text,
    startPage=
        safe_text,
    class_=
        safe_text,
    displayPageNumber=
        safe_text,
    displayFooter=
        safe_text,
    playFull=
        safe_text,
    presetSubType=
        safe_text,
    userTransformed=
        safe_text,
    transitionStyle=
        safe_text,
    pages=
        safe_text,
    stayOnTop=
        safe_text,
    effect=
        safe_text,
    showLogo=
        safe_text,
    mouseAsPen=
        safe_text,
    styleName=
        safe_text,
    presetId=
        safe_text,
    startWithNavigator=
        safe_text,
    masterElement=
        safe_text,
    presentationPageLayoutName=
        safe_text,
    forceManual=
        safe_text,
    groupId=
        safe_text,
    useDateTimeName=
        safe_text,
    showEndOfPresentationSlide=
        safe_text,
    show1=
        safe_text,
    duration=
        safe_text,
    useFooterName=
        safe_text,
    backgroundVisible=
        safe_text,
    fullScreen=
        safe_text,
    direction=
        safe_text,
    mixed=
        safe_text,
    startScale=
        safe_text,
    useHeaderName=
        safe_text,
    mouseVisible=
        safe_text,
    verb=
        safe_text,
    classNames=
        safe_text,
    backgroundObjectsVisible=
        safe_text,
    nodeType=
        safe_text,
    transitionOnClick=
        safe_text,
    speed=
        safe_text
)
presentation::ShowTextType_strategy = st.builds(
    presentation::ShowTextType,
    shapeId=
        safe_text,
    effect=
        safe_text,
    startScale=
        safe_text,
    delay=
        safe_text,
    direction=
        safe_text,
    speed=
        safe_text,
    pathId=
        safe_text
)
presentation::ShowShapeType_strategy = st.builds(
    presentation::ShowShapeType,
    effect=
        safe_text,
    speed=
        safe_text,
    direction=
        safe_text,
    startScale=
        safe_text,
    pathId=
        safe_text,
    shapeId=
        safe_text,
    delay=
        safe_text
)
presentation::PlayType_strategy = st.builds(
    presentation::PlayType,
    shapeId=
        safe_text,
    speed=
        safe_text
)
presentation::ShowType_strategy = st.builds(
    presentation::ShowType,
    name=
        safe_text,
    pages=
        safe_text
)
presentation::SettingsType_strategy = st.builds(
    presentation::SettingsType,
    show1=
        safe_text,
    endless=
        safe_text,
    animations=
        safe_text,
    mouseAsPen=
        safe_text,
    fullScreen=
        safe_text,
    transitionOnClick=
        safe_text,
    mouseVisible=
        safe_text,
    startWithNavigator=
        safe_text,
    showLogo=
        safe_text,
    showEndOfPresentationSlide=
        safe_text,
    forceManual=
        safe_text,
    pause=
        safe_text,
    startPage=
        safe_text,
    stayOnTop=
        safe_text
)
presentation::PlaceholderType_strategy = st.builds(
    presentation::PlaceholderType,
    height=
        safe_text,
    width=
        safe_text,
    y=
        safe_text,
    x=
        safe_text,
    object=
        safe_text
)
presentation::CustomShapeType_strategy = st.builds(
    presentation::CustomShapeType,
)
presentation::SceneType_strategy = st.builds(
    presentation::SceneType,
)
presentation::ControlType_strategy = st.builds(
    presentation::ControlType,
)
presentation::ConnectorType_strategy = st.builds(
    presentation::ConnectorType,
)
presentation::CaptionType_strategy = st.builds(
    presentation::CaptionType,
)
presentation::MeasureType_strategy = st.builds(
    presentation::MeasureType,
)
presentation::FrameType_strategy = st.builds(
    presentation::FrameType,
)
presentation::PageThumbnailType_strategy = st.builds(
    presentation::PageThumbnailType,
)
presentation::PathType_strategy = st.builds(
    presentation::PathType,
)
presentation::GType_strategy = st.builds(
    presentation::GType,
)
presentation::EllipseType_strategy = st.builds(
    presentation::EllipseType,
)
presentation::CircleType_strategy = st.builds(
    presentation::CircleType,
)
presentation::PolylineType_strategy = st.builds(
    presentation::PolylineType,
)
presentation::LineType_strategy = st.builds(
    presentation::LineType,
)
presentation::RegularPolygonType_strategy = st.builds(
    presentation::RegularPolygonType,
)
presentation::PolygonType_strategy = st.builds(
    presentation::PolygonType,
)
presentation::NotesType_strategy = st.builds(
    presentation::NotesType,
    useFooterName=
        safe_text,
    pageLayoutName=
        safe_text,
    styleName=
        safe_text,
    shape=
        safe_text,
    useHeaderName=
        safe_text,
    useDateTimeName=
        safe_text
)
presentation::RectType_strategy = st.builds(
    presentation::RectType,
)
presentation::FormsType_strategy = st.builds(
    presentation::FormsType,
)
presentation::HideTextType_strategy = st.builds(
    presentation::HideTextType,
    shapeId=
        safe_text,
    direction=
        safe_text,
    pathId=
        safe_text,
    startScale=
        safe_text,
    delay=
        safe_text,
    speed=
        safe_text,
    effect=
        safe_text
)
presentation::FooterDeclType_strategy = st.builds(
    presentation::FooterDeclType,
    mixed=
        safe_text,
    name=
        safe_text
)
presentation::HideShapeType_strategy = st.builds(
    presentation::HideShapeType,
    direction=
        safe_text,
    pathId=
        safe_text,
    speed=
        safe_text,
    delay=
        safe_text,
    shapeId=
        safe_text,
    effect=
        safe_text,
    startScale=
        safe_text
)
presentation::HeaderType_strategy = st.builds(
    presentation::HeaderType,
)
presentation::HeaderDeclType_strategy = st.builds(
    presentation::HeaderDeclType,
    name=
        safe_text,
    mixed=
        safe_text
)
presentation::FooterType_strategy = st.builds(
    presentation::FooterType,
)
presentation::DimType_strategy = st.builds(
    presentation::DimType,
    color=
        safe_text,
    shapeId=
        safe_text
)
presentation::DateTimeType_strategy = st.builds(
    presentation::DateTimeType,
)
presentation::EventListenerType_strategy = st.builds(
    presentation::EventListenerType,
    verb=
        safe_text,
    eventName=
        safe_text,
    actuate=
        safe_text,
    direction=
        safe_text,
    speed=
        safe_text,
    show=
        safe_text,
    type=
        safe_text,
    effect=
        safe_text,
    startScale=
        safe_text,
    href=
        safe_text,
    action=
        safe_text
)
presentation::SoundType_strategy = st.builds(
    presentation::SoundType,
    href=
        safe_text,
    type=
        safe_text,
    actuate=
        safe_text,
    show=
        safe_text,
    playFull=
        safe_text
)
presentation::AnimationsType1_strategy = st.builds(
    presentation::AnimationsType1,
    presentationAnimationElementsGroup=
        safe_text,
    group=
        safe_text
)
presentation::EObject_strategy = st.builds(
    presentation::EObject,
)
presentation::DateTimeDeclType_strategy = st.builds(
    presentation::DateTimeDeclType,
    dataStyleName=
        safe_text,
    source=
        safe_text,
    name=
        safe_text,
    mixed=
        safe_text
)
presentation::AnimationGroupType_strategy = st.builds(
    presentation::AnimationGroupType,
    presentationAnimationElementsGroup=
        safe_text
)

@given(instance=presentation::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_presentation::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, presentation::EStringToStringMapEntry)

@given(instance=presentation::DocumentRoot_strategy)
@settings(max_examples=50)
def test_presentation::documentroot_instantiation(instance):
    assert isinstance(instance, presentation::DocumentRoot)

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_pause_type(instance):
    assert isinstance(instance.pause, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_pause_setter(instance):
    original = instance.pause
    instance.pause = original
    assert instance.pause == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_displayHeader_type(instance):
    assert isinstance(instance.displayHeader, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_displayHeader_setter(instance):
    original = instance.displayHeader
    instance.displayHeader = original
    assert instance.displayHeader == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_pathId_type(instance):
    assert isinstance(instance.pathId, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_pathId_setter(instance):
    original = instance.pathId
    instance.pathId = original
    assert instance.pathId == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_displayDateTime_type(instance):
    assert isinstance(instance.displayDateTime, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_displayDateTime_setter(instance):
    original = instance.displayDateTime
    instance.displayDateTime = original
    assert instance.displayDateTime == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_animations1_type(instance):
    assert isinstance(instance.animations1, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_animations1_setter(instance):
    original = instance.animations1
    instance.animations1 = original
    assert instance.animations1 == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_transitionSpeed_type(instance):
    assert isinstance(instance.transitionSpeed, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_transitionSpeed_setter(instance):
    original = instance.transitionSpeed
    instance.transitionSpeed = original
    assert instance.transitionSpeed == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_delay_type(instance):
    assert isinstance(instance.delay, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_delay_setter(instance):
    original = instance.delay
    instance.delay = original
    assert instance.delay == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_presetClass_type(instance):
    assert isinstance(instance.presetClass, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_presetClass_setter(instance):
    original = instance.presetClass
    instance.presetClass = original
    assert instance.presetClass == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_transitionType_type(instance):
    assert isinstance(instance.transitionType, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_transitionType_setter(instance):
    original = instance.transitionType
    instance.transitionType = original
    assert instance.transitionType == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_placeholder1_type(instance):
    assert isinstance(instance.placeholder1, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_placeholder1_setter(instance):
    original = instance.placeholder1
    instance.placeholder1 = original
    assert instance.placeholder1 == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_endless_type(instance):
    assert isinstance(instance.endless, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_endless_setter(instance):
    original = instance.endless
    instance.endless = original
    assert instance.endless == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_startPage_type(instance):
    assert isinstance(instance.startPage, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_startPage_setter(instance):
    original = instance.startPage
    instance.startPage = original
    assert instance.startPage == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_displayPageNumber_type(instance):
    assert isinstance(instance.displayPageNumber, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_displayPageNumber_setter(instance):
    original = instance.displayPageNumber
    instance.displayPageNumber = original
    assert instance.displayPageNumber == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_displayFooter_type(instance):
    assert isinstance(instance.displayFooter, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_displayFooter_setter(instance):
    original = instance.displayFooter
    instance.displayFooter = original
    assert instance.displayFooter == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_playFull_type(instance):
    assert isinstance(instance.playFull, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_playFull_setter(instance):
    original = instance.playFull
    instance.playFull = original
    assert instance.playFull == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_presetSubType_type(instance):
    assert isinstance(instance.presetSubType, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_presetSubType_setter(instance):
    original = instance.presetSubType
    instance.presetSubType = original
    assert instance.presetSubType == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_userTransformed_type(instance):
    assert isinstance(instance.userTransformed, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_userTransformed_setter(instance):
    original = instance.userTransformed
    instance.userTransformed = original
    assert instance.userTransformed == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_transitionStyle_type(instance):
    assert isinstance(instance.transitionStyle, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_transitionStyle_setter(instance):
    original = instance.transitionStyle
    instance.transitionStyle = original
    assert instance.transitionStyle == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_stayOnTop_type(instance):
    assert isinstance(instance.stayOnTop, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_stayOnTop_setter(instance):
    original = instance.stayOnTop
    instance.stayOnTop = original
    assert instance.stayOnTop == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_effect_type(instance):
    assert isinstance(instance.effect, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_showLogo_type(instance):
    assert isinstance(instance.showLogo, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_showLogo_setter(instance):
    original = instance.showLogo
    instance.showLogo = original
    assert instance.showLogo == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_mouseAsPen_type(instance):
    assert isinstance(instance.mouseAsPen, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_mouseAsPen_setter(instance):
    original = instance.mouseAsPen
    instance.mouseAsPen = original
    assert instance.mouseAsPen == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_styleName_type(instance):
    assert isinstance(instance.styleName, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_styleName_setter(instance):
    original = instance.styleName
    instance.styleName = original
    assert instance.styleName == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_presetId_type(instance):
    assert isinstance(instance.presetId, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_presetId_setter(instance):
    original = instance.presetId
    instance.presetId = original
    assert instance.presetId == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_startWithNavigator_type(instance):
    assert isinstance(instance.startWithNavigator, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_startWithNavigator_setter(instance):
    original = instance.startWithNavigator
    instance.startWithNavigator = original
    assert instance.startWithNavigator == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_masterElement_type(instance):
    assert isinstance(instance.masterElement, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_masterElement_setter(instance):
    original = instance.masterElement
    instance.masterElement = original
    assert instance.masterElement == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_presentationPageLayoutName_type(instance):
    assert isinstance(instance.presentationPageLayoutName, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_presentationPageLayoutName_setter(instance):
    original = instance.presentationPageLayoutName
    instance.presentationPageLayoutName = original
    assert instance.presentationPageLayoutName == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_forceManual_type(instance):
    assert isinstance(instance.forceManual, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_forceManual_setter(instance):
    original = instance.forceManual
    instance.forceManual = original
    assert instance.forceManual == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_groupId_type(instance):
    assert isinstance(instance.groupId, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_groupId_setter(instance):
    original = instance.groupId
    instance.groupId = original
    assert instance.groupId == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_useDateTimeName_type(instance):
    assert isinstance(instance.useDateTimeName, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_useDateTimeName_setter(instance):
    original = instance.useDateTimeName
    instance.useDateTimeName = original
    assert instance.useDateTimeName == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_showEndOfPresentationSlide_type(instance):
    assert isinstance(instance.showEndOfPresentationSlide, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_showEndOfPresentationSlide_setter(instance):
    original = instance.showEndOfPresentationSlide
    instance.showEndOfPresentationSlide = original
    assert instance.showEndOfPresentationSlide == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_show1_type(instance):
    assert isinstance(instance.show1, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_show1_setter(instance):
    original = instance.show1
    instance.show1 = original
    assert instance.show1 == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_duration_type(instance):
    assert isinstance(instance.duration, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_useFooterName_type(instance):
    assert isinstance(instance.useFooterName, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_useFooterName_setter(instance):
    original = instance.useFooterName
    instance.useFooterName = original
    assert instance.useFooterName == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_backgroundVisible_type(instance):
    assert isinstance(instance.backgroundVisible, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_backgroundVisible_setter(instance):
    original = instance.backgroundVisible
    instance.backgroundVisible = original
    assert instance.backgroundVisible == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_fullScreen_type(instance):
    assert isinstance(instance.fullScreen, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_fullScreen_setter(instance):
    original = instance.fullScreen
    instance.fullScreen = original
    assert instance.fullScreen == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_startScale_type(instance):
    assert isinstance(instance.startScale, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_startScale_setter(instance):
    original = instance.startScale
    instance.startScale = original
    assert instance.startScale == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_useHeaderName_type(instance):
    assert isinstance(instance.useHeaderName, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_useHeaderName_setter(instance):
    original = instance.useHeaderName
    instance.useHeaderName = original
    assert instance.useHeaderName == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_mouseVisible_type(instance):
    assert isinstance(instance.mouseVisible, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_mouseVisible_setter(instance):
    original = instance.mouseVisible
    instance.mouseVisible = original
    assert instance.mouseVisible == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_verb_type(instance):
    assert isinstance(instance.verb, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_verb_setter(instance):
    original = instance.verb
    instance.verb = original
    assert instance.verb == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_classNames_type(instance):
    assert isinstance(instance.classNames, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_classNames_setter(instance):
    original = instance.classNames
    instance.classNames = original
    assert instance.classNames == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_backgroundObjectsVisible_type(instance):
    assert isinstance(instance.backgroundObjectsVisible, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_backgroundObjectsVisible_setter(instance):
    original = instance.backgroundObjectsVisible
    instance.backgroundObjectsVisible = original
    assert instance.backgroundObjectsVisible == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_nodeType_type(instance):
    assert isinstance(instance.nodeType, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_nodeType_setter(instance):
    original = instance.nodeType
    instance.nodeType = original
    assert instance.nodeType == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_transitionOnClick_type(instance):
    assert isinstance(instance.transitionOnClick, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_transitionOnClick_setter(instance):
    original = instance.transitionOnClick
    instance.transitionOnClick = original
    assert instance.transitionOnClick == original

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_speed_type(instance):
    assert isinstance(instance.speed, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=presentation::ShowTextType_strategy)
@settings(max_examples=50)
def test_presentation::showtexttype_instantiation(instance):
    assert isinstance(instance, presentation::ShowTextType)

@given(instance=presentation::ShowTextType_strategy)
def test_presentation::showtexttype_shapeId_type(instance):
    assert isinstance(instance.shapeId, str)


@given(instance=presentation::ShowTextType_strategy)
def test_presentation::showtexttype_shapeId_setter(instance):
    original = instance.shapeId
    instance.shapeId = original
    assert instance.shapeId == original

@given(instance=presentation::ShowTextType_strategy)
def test_presentation::showtexttype_effect_type(instance):
    assert isinstance(instance.effect, str)


@given(instance=presentation::ShowTextType_strategy)
def test_presentation::showtexttype_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=presentation::ShowTextType_strategy)
def test_presentation::showtexttype_startScale_type(instance):
    assert isinstance(instance.startScale, str)


@given(instance=presentation::ShowTextType_strategy)
def test_presentation::showtexttype_startScale_setter(instance):
    original = instance.startScale
    instance.startScale = original
    assert instance.startScale == original

@given(instance=presentation::ShowTextType_strategy)
def test_presentation::showtexttype_delay_type(instance):
    assert isinstance(instance.delay, str)


@given(instance=presentation::ShowTextType_strategy)
def test_presentation::showtexttype_delay_setter(instance):
    original = instance.delay
    instance.delay = original
    assert instance.delay == original

@given(instance=presentation::ShowTextType_strategy)
def test_presentation::showtexttype_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=presentation::ShowTextType_strategy)
def test_presentation::showtexttype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=presentation::ShowTextType_strategy)
def test_presentation::showtexttype_speed_type(instance):
    assert isinstance(instance.speed, str)


@given(instance=presentation::ShowTextType_strategy)
def test_presentation::showtexttype_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=presentation::ShowTextType_strategy)
def test_presentation::showtexttype_pathId_type(instance):
    assert isinstance(instance.pathId, str)


@given(instance=presentation::ShowTextType_strategy)
def test_presentation::showtexttype_pathId_setter(instance):
    original = instance.pathId
    instance.pathId = original
    assert instance.pathId == original

@given(instance=presentation::ShowShapeType_strategy)
@settings(max_examples=50)
def test_presentation::showshapetype_instantiation(instance):
    assert isinstance(instance, presentation::ShowShapeType)

@given(instance=presentation::ShowShapeType_strategy)
def test_presentation::showshapetype_effect_type(instance):
    assert isinstance(instance.effect, str)


@given(instance=presentation::ShowShapeType_strategy)
def test_presentation::showshapetype_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=presentation::ShowShapeType_strategy)
def test_presentation::showshapetype_speed_type(instance):
    assert isinstance(instance.speed, str)


@given(instance=presentation::ShowShapeType_strategy)
def test_presentation::showshapetype_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=presentation::ShowShapeType_strategy)
def test_presentation::showshapetype_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=presentation::ShowShapeType_strategy)
def test_presentation::showshapetype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=presentation::ShowShapeType_strategy)
def test_presentation::showshapetype_startScale_type(instance):
    assert isinstance(instance.startScale, str)


@given(instance=presentation::ShowShapeType_strategy)
def test_presentation::showshapetype_startScale_setter(instance):
    original = instance.startScale
    instance.startScale = original
    assert instance.startScale == original

@given(instance=presentation::ShowShapeType_strategy)
def test_presentation::showshapetype_pathId_type(instance):
    assert isinstance(instance.pathId, str)


@given(instance=presentation::ShowShapeType_strategy)
def test_presentation::showshapetype_pathId_setter(instance):
    original = instance.pathId
    instance.pathId = original
    assert instance.pathId == original

@given(instance=presentation::ShowShapeType_strategy)
def test_presentation::showshapetype_shapeId_type(instance):
    assert isinstance(instance.shapeId, str)


@given(instance=presentation::ShowShapeType_strategy)
def test_presentation::showshapetype_shapeId_setter(instance):
    original = instance.shapeId
    instance.shapeId = original
    assert instance.shapeId == original

@given(instance=presentation::ShowShapeType_strategy)
def test_presentation::showshapetype_delay_type(instance):
    assert isinstance(instance.delay, str)


@given(instance=presentation::ShowShapeType_strategy)
def test_presentation::showshapetype_delay_setter(instance):
    original = instance.delay
    instance.delay = original
    assert instance.delay == original

@given(instance=presentation::PlayType_strategy)
@settings(max_examples=50)
def test_presentation::playtype_instantiation(instance):
    assert isinstance(instance, presentation::PlayType)

@given(instance=presentation::PlayType_strategy)
def test_presentation::playtype_shapeId_type(instance):
    assert isinstance(instance.shapeId, str)


@given(instance=presentation::PlayType_strategy)
def test_presentation::playtype_shapeId_setter(instance):
    original = instance.shapeId
    instance.shapeId = original
    assert instance.shapeId == original

@given(instance=presentation::PlayType_strategy)
def test_presentation::playtype_speed_type(instance):
    assert isinstance(instance.speed, str)


@given(instance=presentation::PlayType_strategy)
def test_presentation::playtype_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=presentation::ShowType_strategy)
@settings(max_examples=50)
def test_presentation::showtype_instantiation(instance):
    assert isinstance(instance, presentation::ShowType)

@given(instance=presentation::ShowType_strategy)
def test_presentation::showtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=presentation::ShowType_strategy)
def test_presentation::showtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=presentation::ShowType_strategy)
def test_presentation::showtype_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=presentation::ShowType_strategy)
def test_presentation::showtype_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=presentation::SettingsType_strategy)
@settings(max_examples=50)
def test_presentation::settingstype_instantiation(instance):
    assert isinstance(instance, presentation::SettingsType)

@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_show1_type(instance):
    assert isinstance(instance.show1, str)


@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_show1_setter(instance):
    original = instance.show1
    instance.show1 = original
    assert instance.show1 == original

@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_endless_type(instance):
    assert isinstance(instance.endless, str)


@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_endless_setter(instance):
    original = instance.endless
    instance.endless = original
    assert instance.endless == original

@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_animations_type(instance):
    assert isinstance(instance.animations, str)


@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_animations_setter(instance):
    original = instance.animations
    instance.animations = original
    assert instance.animations == original

@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_mouseAsPen_type(instance):
    assert isinstance(instance.mouseAsPen, str)


@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_mouseAsPen_setter(instance):
    original = instance.mouseAsPen
    instance.mouseAsPen = original
    assert instance.mouseAsPen == original

@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_fullScreen_type(instance):
    assert isinstance(instance.fullScreen, str)


@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_fullScreen_setter(instance):
    original = instance.fullScreen
    instance.fullScreen = original
    assert instance.fullScreen == original

@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_transitionOnClick_type(instance):
    assert isinstance(instance.transitionOnClick, str)


@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_transitionOnClick_setter(instance):
    original = instance.transitionOnClick
    instance.transitionOnClick = original
    assert instance.transitionOnClick == original

@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_mouseVisible_type(instance):
    assert isinstance(instance.mouseVisible, str)


@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_mouseVisible_setter(instance):
    original = instance.mouseVisible
    instance.mouseVisible = original
    assert instance.mouseVisible == original

@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_startWithNavigator_type(instance):
    assert isinstance(instance.startWithNavigator, str)


@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_startWithNavigator_setter(instance):
    original = instance.startWithNavigator
    instance.startWithNavigator = original
    assert instance.startWithNavigator == original

@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_showLogo_type(instance):
    assert isinstance(instance.showLogo, str)


@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_showLogo_setter(instance):
    original = instance.showLogo
    instance.showLogo = original
    assert instance.showLogo == original

@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_showEndOfPresentationSlide_type(instance):
    assert isinstance(instance.showEndOfPresentationSlide, str)


@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_showEndOfPresentationSlide_setter(instance):
    original = instance.showEndOfPresentationSlide
    instance.showEndOfPresentationSlide = original
    assert instance.showEndOfPresentationSlide == original

@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_forceManual_type(instance):
    assert isinstance(instance.forceManual, str)


@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_forceManual_setter(instance):
    original = instance.forceManual
    instance.forceManual = original
    assert instance.forceManual == original

@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_pause_type(instance):
    assert isinstance(instance.pause, str)


@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_pause_setter(instance):
    original = instance.pause
    instance.pause = original
    assert instance.pause == original

@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_startPage_type(instance):
    assert isinstance(instance.startPage, str)


@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_startPage_setter(instance):
    original = instance.startPage
    instance.startPage = original
    assert instance.startPage == original

@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_stayOnTop_type(instance):
    assert isinstance(instance.stayOnTop, str)


@given(instance=presentation::SettingsType_strategy)
def test_presentation::settingstype_stayOnTop_setter(instance):
    original = instance.stayOnTop
    instance.stayOnTop = original
    assert instance.stayOnTop == original

@given(instance=presentation::PlaceholderType_strategy)
@settings(max_examples=50)
def test_presentation::placeholdertype_instantiation(instance):
    assert isinstance(instance, presentation::PlaceholderType)

@given(instance=presentation::PlaceholderType_strategy)
def test_presentation::placeholdertype_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=presentation::PlaceholderType_strategy)
def test_presentation::placeholdertype_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=presentation::PlaceholderType_strategy)
def test_presentation::placeholdertype_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=presentation::PlaceholderType_strategy)
def test_presentation::placeholdertype_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=presentation::PlaceholderType_strategy)
def test_presentation::placeholdertype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=presentation::PlaceholderType_strategy)
def test_presentation::placeholdertype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=presentation::PlaceholderType_strategy)
def test_presentation::placeholdertype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=presentation::PlaceholderType_strategy)
def test_presentation::placeholdertype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=presentation::PlaceholderType_strategy)
def test_presentation::placeholdertype_object_type(instance):
    assert isinstance(instance.object, str)


@given(instance=presentation::PlaceholderType_strategy)
def test_presentation::placeholdertype_object_setter(instance):
    original = instance.object
    instance.object = original
    assert instance.object == original

@given(instance=presentation::CustomShapeType_strategy)
@settings(max_examples=50)
def test_presentation::customshapetype_instantiation(instance):
    assert isinstance(instance, presentation::CustomShapeType)

@given(instance=presentation::SceneType_strategy)
@settings(max_examples=50)
def test_presentation::scenetype_instantiation(instance):
    assert isinstance(instance, presentation::SceneType)

@given(instance=presentation::ControlType_strategy)
@settings(max_examples=50)
def test_presentation::controltype_instantiation(instance):
    assert isinstance(instance, presentation::ControlType)

@given(instance=presentation::ConnectorType_strategy)
@settings(max_examples=50)
def test_presentation::connectortype_instantiation(instance):
    assert isinstance(instance, presentation::ConnectorType)

@given(instance=presentation::CaptionType_strategy)
@settings(max_examples=50)
def test_presentation::captiontype_instantiation(instance):
    assert isinstance(instance, presentation::CaptionType)

@given(instance=presentation::MeasureType_strategy)
@settings(max_examples=50)
def test_presentation::measuretype_instantiation(instance):
    assert isinstance(instance, presentation::MeasureType)

@given(instance=presentation::FrameType_strategy)
@settings(max_examples=50)
def test_presentation::frametype_instantiation(instance):
    assert isinstance(instance, presentation::FrameType)

@given(instance=presentation::PageThumbnailType_strategy)
@settings(max_examples=50)
def test_presentation::pagethumbnailtype_instantiation(instance):
    assert isinstance(instance, presentation::PageThumbnailType)

@given(instance=presentation::PathType_strategy)
@settings(max_examples=50)
def test_presentation::pathtype_instantiation(instance):
    assert isinstance(instance, presentation::PathType)

@given(instance=presentation::GType_strategy)
@settings(max_examples=50)
def test_presentation::gtype_instantiation(instance):
    assert isinstance(instance, presentation::GType)

@given(instance=presentation::EllipseType_strategy)
@settings(max_examples=50)
def test_presentation::ellipsetype_instantiation(instance):
    assert isinstance(instance, presentation::EllipseType)

@given(instance=presentation::CircleType_strategy)
@settings(max_examples=50)
def test_presentation::circletype_instantiation(instance):
    assert isinstance(instance, presentation::CircleType)

@given(instance=presentation::PolylineType_strategy)
@settings(max_examples=50)
def test_presentation::polylinetype_instantiation(instance):
    assert isinstance(instance, presentation::PolylineType)

@given(instance=presentation::LineType_strategy)
@settings(max_examples=50)
def test_presentation::linetype_instantiation(instance):
    assert isinstance(instance, presentation::LineType)

@given(instance=presentation::RegularPolygonType_strategy)
@settings(max_examples=50)
def test_presentation::regularpolygontype_instantiation(instance):
    assert isinstance(instance, presentation::RegularPolygonType)

@given(instance=presentation::PolygonType_strategy)
@settings(max_examples=50)
def test_presentation::polygontype_instantiation(instance):
    assert isinstance(instance, presentation::PolygonType)

@given(instance=presentation::NotesType_strategy)
@settings(max_examples=50)
def test_presentation::notestype_instantiation(instance):
    assert isinstance(instance, presentation::NotesType)

@given(instance=presentation::NotesType_strategy)
def test_presentation::notestype_useFooterName_type(instance):
    assert isinstance(instance.useFooterName, str)


@given(instance=presentation::NotesType_strategy)
def test_presentation::notestype_useFooterName_setter(instance):
    original = instance.useFooterName
    instance.useFooterName = original
    assert instance.useFooterName == original

@given(instance=presentation::NotesType_strategy)
def test_presentation::notestype_pageLayoutName_type(instance):
    assert isinstance(instance.pageLayoutName, str)


@given(instance=presentation::NotesType_strategy)
def test_presentation::notestype_pageLayoutName_setter(instance):
    original = instance.pageLayoutName
    instance.pageLayoutName = original
    assert instance.pageLayoutName == original

@given(instance=presentation::NotesType_strategy)
def test_presentation::notestype_styleName_type(instance):
    assert isinstance(instance.styleName, str)


@given(instance=presentation::NotesType_strategy)
def test_presentation::notestype_styleName_setter(instance):
    original = instance.styleName
    instance.styleName = original
    assert instance.styleName == original

@given(instance=presentation::NotesType_strategy)
def test_presentation::notestype_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=presentation::NotesType_strategy)
def test_presentation::notestype_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=presentation::NotesType_strategy)
def test_presentation::notestype_useHeaderName_type(instance):
    assert isinstance(instance.useHeaderName, str)


@given(instance=presentation::NotesType_strategy)
def test_presentation::notestype_useHeaderName_setter(instance):
    original = instance.useHeaderName
    instance.useHeaderName = original
    assert instance.useHeaderName == original

@given(instance=presentation::NotesType_strategy)
def test_presentation::notestype_useDateTimeName_type(instance):
    assert isinstance(instance.useDateTimeName, str)


@given(instance=presentation::NotesType_strategy)
def test_presentation::notestype_useDateTimeName_setter(instance):
    original = instance.useDateTimeName
    instance.useDateTimeName = original
    assert instance.useDateTimeName == original

@given(instance=presentation::RectType_strategy)
@settings(max_examples=50)
def test_presentation::recttype_instantiation(instance):
    assert isinstance(instance, presentation::RectType)

@given(instance=presentation::FormsType_strategy)
@settings(max_examples=50)
def test_presentation::formstype_instantiation(instance):
    assert isinstance(instance, presentation::FormsType)

@given(instance=presentation::HideTextType_strategy)
@settings(max_examples=50)
def test_presentation::hidetexttype_instantiation(instance):
    assert isinstance(instance, presentation::HideTextType)

@given(instance=presentation::HideTextType_strategy)
def test_presentation::hidetexttype_shapeId_type(instance):
    assert isinstance(instance.shapeId, str)


@given(instance=presentation::HideTextType_strategy)
def test_presentation::hidetexttype_shapeId_setter(instance):
    original = instance.shapeId
    instance.shapeId = original
    assert instance.shapeId == original

@given(instance=presentation::HideTextType_strategy)
def test_presentation::hidetexttype_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=presentation::HideTextType_strategy)
def test_presentation::hidetexttype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=presentation::HideTextType_strategy)
def test_presentation::hidetexttype_pathId_type(instance):
    assert isinstance(instance.pathId, str)


@given(instance=presentation::HideTextType_strategy)
def test_presentation::hidetexttype_pathId_setter(instance):
    original = instance.pathId
    instance.pathId = original
    assert instance.pathId == original

@given(instance=presentation::HideTextType_strategy)
def test_presentation::hidetexttype_startScale_type(instance):
    assert isinstance(instance.startScale, str)


@given(instance=presentation::HideTextType_strategy)
def test_presentation::hidetexttype_startScale_setter(instance):
    original = instance.startScale
    instance.startScale = original
    assert instance.startScale == original

@given(instance=presentation::HideTextType_strategy)
def test_presentation::hidetexttype_delay_type(instance):
    assert isinstance(instance.delay, str)


@given(instance=presentation::HideTextType_strategy)
def test_presentation::hidetexttype_delay_setter(instance):
    original = instance.delay
    instance.delay = original
    assert instance.delay == original

@given(instance=presentation::HideTextType_strategy)
def test_presentation::hidetexttype_speed_type(instance):
    assert isinstance(instance.speed, str)


@given(instance=presentation::HideTextType_strategy)
def test_presentation::hidetexttype_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=presentation::HideTextType_strategy)
def test_presentation::hidetexttype_effect_type(instance):
    assert isinstance(instance.effect, str)


@given(instance=presentation::HideTextType_strategy)
def test_presentation::hidetexttype_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=presentation::FooterDeclType_strategy)
@settings(max_examples=50)
def test_presentation::footerdecltype_instantiation(instance):
    assert isinstance(instance, presentation::FooterDeclType)

@given(instance=presentation::FooterDeclType_strategy)
def test_presentation::footerdecltype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::FooterDeclType_strategy)
def test_presentation::footerdecltype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::FooterDeclType_strategy)
def test_presentation::footerdecltype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=presentation::FooterDeclType_strategy)
def test_presentation::footerdecltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=presentation::HideShapeType_strategy)
@settings(max_examples=50)
def test_presentation::hideshapetype_instantiation(instance):
    assert isinstance(instance, presentation::HideShapeType)

@given(instance=presentation::HideShapeType_strategy)
def test_presentation::hideshapetype_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=presentation::HideShapeType_strategy)
def test_presentation::hideshapetype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=presentation::HideShapeType_strategy)
def test_presentation::hideshapetype_pathId_type(instance):
    assert isinstance(instance.pathId, str)


@given(instance=presentation::HideShapeType_strategy)
def test_presentation::hideshapetype_pathId_setter(instance):
    original = instance.pathId
    instance.pathId = original
    assert instance.pathId == original

@given(instance=presentation::HideShapeType_strategy)
def test_presentation::hideshapetype_speed_type(instance):
    assert isinstance(instance.speed, str)


@given(instance=presentation::HideShapeType_strategy)
def test_presentation::hideshapetype_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=presentation::HideShapeType_strategy)
def test_presentation::hideshapetype_delay_type(instance):
    assert isinstance(instance.delay, str)


@given(instance=presentation::HideShapeType_strategy)
def test_presentation::hideshapetype_delay_setter(instance):
    original = instance.delay
    instance.delay = original
    assert instance.delay == original

@given(instance=presentation::HideShapeType_strategy)
def test_presentation::hideshapetype_shapeId_type(instance):
    assert isinstance(instance.shapeId, str)


@given(instance=presentation::HideShapeType_strategy)
def test_presentation::hideshapetype_shapeId_setter(instance):
    original = instance.shapeId
    instance.shapeId = original
    assert instance.shapeId == original

@given(instance=presentation::HideShapeType_strategy)
def test_presentation::hideshapetype_effect_type(instance):
    assert isinstance(instance.effect, str)


@given(instance=presentation::HideShapeType_strategy)
def test_presentation::hideshapetype_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=presentation::HideShapeType_strategy)
def test_presentation::hideshapetype_startScale_type(instance):
    assert isinstance(instance.startScale, str)


@given(instance=presentation::HideShapeType_strategy)
def test_presentation::hideshapetype_startScale_setter(instance):
    original = instance.startScale
    instance.startScale = original
    assert instance.startScale == original

@given(instance=presentation::HeaderType_strategy)
@settings(max_examples=50)
def test_presentation::headertype_instantiation(instance):
    assert isinstance(instance, presentation::HeaderType)

@given(instance=presentation::HeaderDeclType_strategy)
@settings(max_examples=50)
def test_presentation::headerdecltype_instantiation(instance):
    assert isinstance(instance, presentation::HeaderDeclType)

@given(instance=presentation::HeaderDeclType_strategy)
def test_presentation::headerdecltype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=presentation::HeaderDeclType_strategy)
def test_presentation::headerdecltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=presentation::HeaderDeclType_strategy)
def test_presentation::headerdecltype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::HeaderDeclType_strategy)
def test_presentation::headerdecltype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::FooterType_strategy)
@settings(max_examples=50)
def test_presentation::footertype_instantiation(instance):
    assert isinstance(instance, presentation::FooterType)

@given(instance=presentation::DimType_strategy)
@settings(max_examples=50)
def test_presentation::dimtype_instantiation(instance):
    assert isinstance(instance, presentation::DimType)

@given(instance=presentation::DimType_strategy)
def test_presentation::dimtype_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=presentation::DimType_strategy)
def test_presentation::dimtype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=presentation::DimType_strategy)
def test_presentation::dimtype_shapeId_type(instance):
    assert isinstance(instance.shapeId, str)


@given(instance=presentation::DimType_strategy)
def test_presentation::dimtype_shapeId_setter(instance):
    original = instance.shapeId
    instance.shapeId = original
    assert instance.shapeId == original

@given(instance=presentation::DateTimeType_strategy)
@settings(max_examples=50)
def test_presentation::datetimetype_instantiation(instance):
    assert isinstance(instance, presentation::DateTimeType)

@given(instance=presentation::EventListenerType_strategy)
@settings(max_examples=50)
def test_presentation::eventlistenertype_instantiation(instance):
    assert isinstance(instance, presentation::EventListenerType)

@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_verb_type(instance):
    assert isinstance(instance.verb, str)


@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_verb_setter(instance):
    original = instance.verb
    instance.verb = original
    assert instance.verb == original

@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_eventName_type(instance):
    assert isinstance(instance.eventName, str)


@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_eventName_setter(instance):
    original = instance.eventName
    instance.eventName = original
    assert instance.eventName == original

@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_actuate_type(instance):
    assert isinstance(instance.actuate, str)


@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_actuate_setter(instance):
    original = instance.actuate
    instance.actuate = original
    assert instance.actuate == original

@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_speed_type(instance):
    assert isinstance(instance.speed, str)


@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_show_type(instance):
    assert isinstance(instance.show, str)


@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_show_setter(instance):
    original = instance.show
    instance.show = original
    assert instance.show == original

@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_effect_type(instance):
    assert isinstance(instance.effect, str)


@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_startScale_type(instance):
    assert isinstance(instance.startScale, str)


@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_startScale_setter(instance):
    original = instance.startScale
    instance.startScale = original
    assert instance.startScale == original

@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_href_type(instance):
    assert isinstance(instance.href, str)


@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original

@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=presentation::EventListenerType_strategy)
def test_presentation::eventlistenertype_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=presentation::SoundType_strategy)
@settings(max_examples=50)
def test_presentation::soundtype_instantiation(instance):
    assert isinstance(instance, presentation::SoundType)

@given(instance=presentation::SoundType_strategy)
def test_presentation::soundtype_href_type(instance):
    assert isinstance(instance.href, str)


@given(instance=presentation::SoundType_strategy)
def test_presentation::soundtype_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original

@given(instance=presentation::SoundType_strategy)
def test_presentation::soundtype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=presentation::SoundType_strategy)
def test_presentation::soundtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=presentation::SoundType_strategy)
def test_presentation::soundtype_actuate_type(instance):
    assert isinstance(instance.actuate, str)


@given(instance=presentation::SoundType_strategy)
def test_presentation::soundtype_actuate_setter(instance):
    original = instance.actuate
    instance.actuate = original
    assert instance.actuate == original

@given(instance=presentation::SoundType_strategy)
def test_presentation::soundtype_show_type(instance):
    assert isinstance(instance.show, str)


@given(instance=presentation::SoundType_strategy)
def test_presentation::soundtype_show_setter(instance):
    original = instance.show
    instance.show = original
    assert instance.show == original

@given(instance=presentation::SoundType_strategy)
def test_presentation::soundtype_playFull_type(instance):
    assert isinstance(instance.playFull, str)


@given(instance=presentation::SoundType_strategy)
def test_presentation::soundtype_playFull_setter(instance):
    original = instance.playFull
    instance.playFull = original
    assert instance.playFull == original

@given(instance=presentation::AnimationsType1_strategy)
@settings(max_examples=50)
def test_presentation::animationstype1_instantiation(instance):
    assert isinstance(instance, presentation::AnimationsType1)

@given(instance=presentation::AnimationsType1_strategy)
def test_presentation::animationstype1_presentationAnimationElementsGroup_type(instance):
    assert isinstance(instance.presentationAnimationElementsGroup, str)


@given(instance=presentation::AnimationsType1_strategy)
def test_presentation::animationstype1_presentationAnimationElementsGroup_setter(instance):
    original = instance.presentationAnimationElementsGroup
    instance.presentationAnimationElementsGroup = original
    assert instance.presentationAnimationElementsGroup == original

@given(instance=presentation::AnimationsType1_strategy)
def test_presentation::animationstype1_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::AnimationsType1_strategy)
def test_presentation::animationstype1_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::EObject_strategy)
@settings(max_examples=50)
def test_presentation::eobject_instantiation(instance):
    assert isinstance(instance, presentation::EObject)

@given(instance=presentation::DateTimeDeclType_strategy)
@settings(max_examples=50)
def test_presentation::datetimedecltype_instantiation(instance):
    assert isinstance(instance, presentation::DateTimeDeclType)

@given(instance=presentation::DateTimeDeclType_strategy)
def test_presentation::datetimedecltype_dataStyleName_type(instance):
    assert isinstance(instance.dataStyleName, str)


@given(instance=presentation::DateTimeDeclType_strategy)
def test_presentation::datetimedecltype_dataStyleName_setter(instance):
    original = instance.dataStyleName
    instance.dataStyleName = original
    assert instance.dataStyleName == original

@given(instance=presentation::DateTimeDeclType_strategy)
def test_presentation::datetimedecltype_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=presentation::DateTimeDeclType_strategy)
def test_presentation::datetimedecltype_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=presentation::DateTimeDeclType_strategy)
def test_presentation::datetimedecltype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=presentation::DateTimeDeclType_strategy)
def test_presentation::datetimedecltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=presentation::DateTimeDeclType_strategy)
def test_presentation::datetimedecltype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::DateTimeDeclType_strategy)
def test_presentation::datetimedecltype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::AnimationGroupType_strategy)
@settings(max_examples=50)
def test_presentation::animationgrouptype_instantiation(instance):
    assert isinstance(instance, presentation::AnimationGroupType)

@given(instance=presentation::AnimationGroupType_strategy)
def test_presentation::animationgrouptype_presentationAnimationElementsGroup_type(instance):
    assert isinstance(instance.presentationAnimationElementsGroup, str)


@given(instance=presentation::AnimationGroupType_strategy)
def test_presentation::animationgrouptype_presentationAnimationElementsGroup_setter(instance):
    original = instance.presentationAnimationElementsGroup
    instance.presentationAnimationElementsGroup = original
    assert instance.presentationAnimationElementsGroup == original
