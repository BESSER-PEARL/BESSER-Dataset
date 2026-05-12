import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    presentation_EStringToStringMapEntry,
    presentation_DocumentRoot,
    presentation_ShowTextType,
    presentation_ShowShapeType,
    presentation_PlayType,
    presentation_ShowType,
    presentation_SettingsType,
    presentation_PlaceholderType,
    presentation_CustomShapeType,
    presentation_SceneType,
    presentation_ControlType,
    presentation_ConnectorType,
    presentation_CaptionType,
    presentation_MeasureType,
    presentation_FrameType,
    presentation_PageThumbnailType,
    presentation_PathType,
    presentation_GType,
    presentation_EllipseType,
    presentation_CircleType,
    presentation_PolylineType,
    presentation_LineType,
    presentation_RegularPolygonType,
    presentation_PolygonType,
    presentation_NotesType,
    presentation_RectType,
    presentation_FormsType,
    presentation_HideTextType,
    presentation_FooterDeclType,
    presentation_HideShapeType,
    presentation_HeaderType,
    presentation_HeaderDeclType,
    presentation_FooterType,
    presentation_DimType,
    presentation_DateTimeType,
    presentation_EventListenerType,
    presentation_SoundType,
    presentation_AnimationsType1,
    presentation_EObject,
    presentation_DateTimeDeclType,
    presentation_AnimationGroupType,
    AnimationsType,
    VisibilityType,
    NodeTypeType,
    ActionType,
    PresetClassType,
    TransitionStyleType,
    SourceType,
    TransitionTypeType,
    TransitionOnClickType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_presentation_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(presentation_EStringToStringMapEntry)


def test_presentation_estringtostringmapentry_constructor_exists():
    assert callable(presentation_EStringToStringMapEntry.__init__)


def test_presentation_estringtostringmapentry_constructor_args():
    sig = inspect.signature(presentation_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_presentation_documentroot_is_not_abstract():
    assert not inspect.isabstract(presentation_DocumentRoot)


def test_presentation_documentroot_constructor_exists():
    assert callable(presentation_DocumentRoot.__init__)


def test_presentation_documentroot_constructor_args():
    sig = inspect.signature(presentation_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "startWithNavigator" in params, "Missing parameter 'startWithNavigator'"
    assert "source" in params, "Missing parameter 'source'"
    assert "displayFooter" in params, "Missing parameter 'displayFooter'"
    assert "forceManual" in params, "Missing parameter 'forceManual'"
    assert "useDateTimeName" in params, "Missing parameter 'useDateTimeName'"
    assert "displayPageNumber" in params, "Missing parameter 'displayPageNumber'"
    assert "delay" in params, "Missing parameter 'delay'"
    assert "transitionStyle" in params, "Missing parameter 'transitionStyle'"
    assert "displayDateTime" in params, "Missing parameter 'displayDateTime'"
    assert "transitionType" in params, "Missing parameter 'transitionType'"
    assert "transitionOnClick" in params, "Missing parameter 'transitionOnClick'"
    assert "showLogo" in params, "Missing parameter 'showLogo'"
    assert "pathId" in params, "Missing parameter 'pathId'"
    assert "displayHeader" in params, "Missing parameter 'displayHeader'"
    assert "masterElement" in params, "Missing parameter 'masterElement'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "useFooterName" in params, "Missing parameter 'useFooterName'"
    assert "show1" in params, "Missing parameter 'show1'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "startScale" in params, "Missing parameter 'startScale'"
    assert "fullScreen" in params, "Missing parameter 'fullScreen'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "nodeType" in params, "Missing parameter 'nodeType'"
    assert "mouseAsPen" in params, "Missing parameter 'mouseAsPen'"
    assert "mouseVisible" in params, "Missing parameter 'mouseVisible'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "userTransformed" in params, "Missing parameter 'userTransformed'"
    assert "backgroundObjectsVisible" in params, "Missing parameter 'backgroundObjectsVisible'"
    assert "transitionSpeed" in params, "Missing parameter 'transitionSpeed'"
    assert "name" in params, "Missing parameter 'name'"
    assert "presetClass" in params, "Missing parameter 'presetClass'"
    assert "endless" in params, "Missing parameter 'endless'"
    assert "action" in params, "Missing parameter 'action'"
    assert "stayOnTop" in params, "Missing parameter 'stayOnTop'"
    assert "verb" in params, "Missing parameter 'verb'"
    assert "presetSubType" in params, "Missing parameter 'presetSubType'"
    assert "placeholder1" in params, "Missing parameter 'placeholder1'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "animations1" in params, "Missing parameter 'animations1'"
    assert "startPage" in params, "Missing parameter 'startPage'"
    assert "groupId" in params, "Missing parameter 'groupId'"
    assert "speed" in params, "Missing parameter 'speed'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "styleName" in params, "Missing parameter 'styleName'"
    assert "useHeaderName" in params, "Missing parameter 'useHeaderName'"
    assert "playFull" in params, "Missing parameter 'playFull'"
    assert "backgroundVisible" in params, "Missing parameter 'backgroundVisible'"
    assert "presentationPageLayoutName" in params, "Missing parameter 'presentationPageLayoutName'"
    assert "showEndOfPresentationSlide" in params, "Missing parameter 'showEndOfPresentationSlide'"
    assert "presetId" in params, "Missing parameter 'presetId'"
    assert "classNames" in params, "Missing parameter 'classNames'"
    assert "pause" in params, "Missing parameter 'pause'"

def test_presentation_documentroot_has_startWithNavigator():
    assert hasattr(presentation_DocumentRoot, "startWithNavigator")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "startWithNavigator" in klass.__dict__:
            descriptor = klass.__dict__["startWithNavigator"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_source():
    assert hasattr(presentation_DocumentRoot, "source")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_displayFooter():
    assert hasattr(presentation_DocumentRoot, "displayFooter")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "displayFooter" in klass.__dict__:
            descriptor = klass.__dict__["displayFooter"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_forceManual():
    assert hasattr(presentation_DocumentRoot, "forceManual")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "forceManual" in klass.__dict__:
            descriptor = klass.__dict__["forceManual"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_useDateTimeName():
    assert hasattr(presentation_DocumentRoot, "useDateTimeName")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "useDateTimeName" in klass.__dict__:
            descriptor = klass.__dict__["useDateTimeName"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_displayPageNumber():
    assert hasattr(presentation_DocumentRoot, "displayPageNumber")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "displayPageNumber" in klass.__dict__:
            descriptor = klass.__dict__["displayPageNumber"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_delay():
    assert hasattr(presentation_DocumentRoot, "delay")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "delay" in klass.__dict__:
            descriptor = klass.__dict__["delay"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_transitionStyle():
    assert hasattr(presentation_DocumentRoot, "transitionStyle")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "transitionStyle" in klass.__dict__:
            descriptor = klass.__dict__["transitionStyle"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_displayDateTime():
    assert hasattr(presentation_DocumentRoot, "displayDateTime")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "displayDateTime" in klass.__dict__:
            descriptor = klass.__dict__["displayDateTime"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_transitionType():
    assert hasattr(presentation_DocumentRoot, "transitionType")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "transitionType" in klass.__dict__:
            descriptor = klass.__dict__["transitionType"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_transitionOnClick():
    assert hasattr(presentation_DocumentRoot, "transitionOnClick")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "transitionOnClick" in klass.__dict__:
            descriptor = klass.__dict__["transitionOnClick"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_showLogo():
    assert hasattr(presentation_DocumentRoot, "showLogo")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "showLogo" in klass.__dict__:
            descriptor = klass.__dict__["showLogo"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_pathId():
    assert hasattr(presentation_DocumentRoot, "pathId")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "pathId" in klass.__dict__:
            descriptor = klass.__dict__["pathId"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_displayHeader():
    assert hasattr(presentation_DocumentRoot, "displayHeader")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "displayHeader" in klass.__dict__:
            descriptor = klass.__dict__["displayHeader"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_masterElement():
    assert hasattr(presentation_DocumentRoot, "masterElement")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "masterElement" in klass.__dict__:
            descriptor = klass.__dict__["masterElement"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_visibility():
    assert hasattr(presentation_DocumentRoot, "visibility")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_useFooterName():
    assert hasattr(presentation_DocumentRoot, "useFooterName")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "useFooterName" in klass.__dict__:
            descriptor = klass.__dict__["useFooterName"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_show1():
    assert hasattr(presentation_DocumentRoot, "show1")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "show1" in klass.__dict__:
            descriptor = klass.__dict__["show1"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_duration():
    assert hasattr(presentation_DocumentRoot, "duration")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_startScale():
    assert hasattr(presentation_DocumentRoot, "startScale")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "startScale" in klass.__dict__:
            descriptor = klass.__dict__["startScale"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_fullScreen():
    assert hasattr(presentation_DocumentRoot, "fullScreen")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "fullScreen" in klass.__dict__:
            descriptor = klass.__dict__["fullScreen"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_effect():
    assert hasattr(presentation_DocumentRoot, "effect")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_direction():
    assert hasattr(presentation_DocumentRoot, "direction")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_nodeType():
    assert hasattr(presentation_DocumentRoot, "nodeType")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "nodeType" in klass.__dict__:
            descriptor = klass.__dict__["nodeType"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_mouseAsPen():
    assert hasattr(presentation_DocumentRoot, "mouseAsPen")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "mouseAsPen" in klass.__dict__:
            descriptor = klass.__dict__["mouseAsPen"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_mouseVisible():
    assert hasattr(presentation_DocumentRoot, "mouseVisible")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "mouseVisible" in klass.__dict__:
            descriptor = klass.__dict__["mouseVisible"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_mixed():
    assert hasattr(presentation_DocumentRoot, "mixed")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_userTransformed():
    assert hasattr(presentation_DocumentRoot, "userTransformed")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "userTransformed" in klass.__dict__:
            descriptor = klass.__dict__["userTransformed"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_backgroundObjectsVisible():
    assert hasattr(presentation_DocumentRoot, "backgroundObjectsVisible")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "backgroundObjectsVisible" in klass.__dict__:
            descriptor = klass.__dict__["backgroundObjectsVisible"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_transitionSpeed():
    assert hasattr(presentation_DocumentRoot, "transitionSpeed")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "transitionSpeed" in klass.__dict__:
            descriptor = klass.__dict__["transitionSpeed"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_name():
    assert hasattr(presentation_DocumentRoot, "name")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_presetClass():
    assert hasattr(presentation_DocumentRoot, "presetClass")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "presetClass" in klass.__dict__:
            descriptor = klass.__dict__["presetClass"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_endless():
    assert hasattr(presentation_DocumentRoot, "endless")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "endless" in klass.__dict__:
            descriptor = klass.__dict__["endless"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_action():
    assert hasattr(presentation_DocumentRoot, "action")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_stayOnTop():
    assert hasattr(presentation_DocumentRoot, "stayOnTop")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "stayOnTop" in klass.__dict__:
            descriptor = klass.__dict__["stayOnTop"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_verb():
    assert hasattr(presentation_DocumentRoot, "verb")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "verb" in klass.__dict__:
            descriptor = klass.__dict__["verb"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_presetSubType():
    assert hasattr(presentation_DocumentRoot, "presetSubType")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "presetSubType" in klass.__dict__:
            descriptor = klass.__dict__["presetSubType"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_placeholder1():
    assert hasattr(presentation_DocumentRoot, "placeholder1")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "placeholder1" in klass.__dict__:
            descriptor = klass.__dict__["placeholder1"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_pages():
    assert hasattr(presentation_DocumentRoot, "pages")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_animations1():
    assert hasattr(presentation_DocumentRoot, "animations1")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "animations1" in klass.__dict__:
            descriptor = klass.__dict__["animations1"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_startPage():
    assert hasattr(presentation_DocumentRoot, "startPage")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "startPage" in klass.__dict__:
            descriptor = klass.__dict__["startPage"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_groupId():
    assert hasattr(presentation_DocumentRoot, "groupId")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "groupId" in klass.__dict__:
            descriptor = klass.__dict__["groupId"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_speed():
    assert hasattr(presentation_DocumentRoot, "speed")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_class_():
    assert hasattr(presentation_DocumentRoot, "class_")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_styleName():
    assert hasattr(presentation_DocumentRoot, "styleName")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "styleName" in klass.__dict__:
            descriptor = klass.__dict__["styleName"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_useHeaderName():
    assert hasattr(presentation_DocumentRoot, "useHeaderName")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "useHeaderName" in klass.__dict__:
            descriptor = klass.__dict__["useHeaderName"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_playFull():
    assert hasattr(presentation_DocumentRoot, "playFull")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "playFull" in klass.__dict__:
            descriptor = klass.__dict__["playFull"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_backgroundVisible():
    assert hasattr(presentation_DocumentRoot, "backgroundVisible")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "backgroundVisible" in klass.__dict__:
            descriptor = klass.__dict__["backgroundVisible"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_presentationPageLayoutName():
    assert hasattr(presentation_DocumentRoot, "presentationPageLayoutName")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "presentationPageLayoutName" in klass.__dict__:
            descriptor = klass.__dict__["presentationPageLayoutName"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_showEndOfPresentationSlide():
    assert hasattr(presentation_DocumentRoot, "showEndOfPresentationSlide")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "showEndOfPresentationSlide" in klass.__dict__:
            descriptor = klass.__dict__["showEndOfPresentationSlide"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_presetId():
    assert hasattr(presentation_DocumentRoot, "presetId")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "presetId" in klass.__dict__:
            descriptor = klass.__dict__["presetId"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_classNames():
    assert hasattr(presentation_DocumentRoot, "classNames")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "classNames" in klass.__dict__:
            descriptor = klass.__dict__["classNames"]
            break
    assert isinstance(descriptor, property)

def test_presentation_documentroot_has_pause():
    assert hasattr(presentation_DocumentRoot, "pause")
    descriptor = None
    for klass in presentation_DocumentRoot.__mro__:
        if "pause" in klass.__dict__:
            descriptor = klass.__dict__["pause"]
            break
    assert isinstance(descriptor, property)



def test_presentation_showtexttype_is_not_abstract():
    assert not inspect.isabstract(presentation_ShowTextType)


def test_presentation_showtexttype_constructor_exists():
    assert callable(presentation_ShowTextType.__init__)


def test_presentation_showtexttype_constructor_args():
    sig = inspect.signature(presentation_ShowTextType.__init__)
    params = list(sig.parameters.keys())
    assert "delay" in params, "Missing parameter 'delay'"
    assert "pathId" in params, "Missing parameter 'pathId'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "shapeId" in params, "Missing parameter 'shapeId'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "startScale" in params, "Missing parameter 'startScale'"
    assert "speed" in params, "Missing parameter 'speed'"

def test_presentation_showtexttype_has_delay():
    assert hasattr(presentation_ShowTextType, "delay")
    descriptor = None
    for klass in presentation_ShowTextType.__mro__:
        if "delay" in klass.__dict__:
            descriptor = klass.__dict__["delay"]
            break
    assert isinstance(descriptor, property)

def test_presentation_showtexttype_has_pathId():
    assert hasattr(presentation_ShowTextType, "pathId")
    descriptor = None
    for klass in presentation_ShowTextType.__mro__:
        if "pathId" in klass.__dict__:
            descriptor = klass.__dict__["pathId"]
            break
    assert isinstance(descriptor, property)

def test_presentation_showtexttype_has_effect():
    assert hasattr(presentation_ShowTextType, "effect")
    descriptor = None
    for klass in presentation_ShowTextType.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_presentation_showtexttype_has_shapeId():
    assert hasattr(presentation_ShowTextType, "shapeId")
    descriptor = None
    for klass in presentation_ShowTextType.__mro__:
        if "shapeId" in klass.__dict__:
            descriptor = klass.__dict__["shapeId"]
            break
    assert isinstance(descriptor, property)

def test_presentation_showtexttype_has_direction():
    assert hasattr(presentation_ShowTextType, "direction")
    descriptor = None
    for klass in presentation_ShowTextType.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_presentation_showtexttype_has_startScale():
    assert hasattr(presentation_ShowTextType, "startScale")
    descriptor = None
    for klass in presentation_ShowTextType.__mro__:
        if "startScale" in klass.__dict__:
            descriptor = klass.__dict__["startScale"]
            break
    assert isinstance(descriptor, property)

def test_presentation_showtexttype_has_speed():
    assert hasattr(presentation_ShowTextType, "speed")
    descriptor = None
    for klass in presentation_ShowTextType.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)



def test_presentation_showshapetype_is_not_abstract():
    assert not inspect.isabstract(presentation_ShowShapeType)


def test_presentation_showshapetype_constructor_exists():
    assert callable(presentation_ShowShapeType.__init__)


def test_presentation_showshapetype_constructor_args():
    sig = inspect.signature(presentation_ShowShapeType.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "startScale" in params, "Missing parameter 'startScale'"
    assert "delay" in params, "Missing parameter 'delay'"
    assert "speed" in params, "Missing parameter 'speed'"
    assert "pathId" in params, "Missing parameter 'pathId'"
    assert "shapeId" in params, "Missing parameter 'shapeId'"
    assert "effect" in params, "Missing parameter 'effect'"

def test_presentation_showshapetype_has_direction():
    assert hasattr(presentation_ShowShapeType, "direction")
    descriptor = None
    for klass in presentation_ShowShapeType.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_presentation_showshapetype_has_startScale():
    assert hasattr(presentation_ShowShapeType, "startScale")
    descriptor = None
    for klass in presentation_ShowShapeType.__mro__:
        if "startScale" in klass.__dict__:
            descriptor = klass.__dict__["startScale"]
            break
    assert isinstance(descriptor, property)

def test_presentation_showshapetype_has_delay():
    assert hasattr(presentation_ShowShapeType, "delay")
    descriptor = None
    for klass in presentation_ShowShapeType.__mro__:
        if "delay" in klass.__dict__:
            descriptor = klass.__dict__["delay"]
            break
    assert isinstance(descriptor, property)

def test_presentation_showshapetype_has_speed():
    assert hasattr(presentation_ShowShapeType, "speed")
    descriptor = None
    for klass in presentation_ShowShapeType.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_presentation_showshapetype_has_pathId():
    assert hasattr(presentation_ShowShapeType, "pathId")
    descriptor = None
    for klass in presentation_ShowShapeType.__mro__:
        if "pathId" in klass.__dict__:
            descriptor = klass.__dict__["pathId"]
            break
    assert isinstance(descriptor, property)

def test_presentation_showshapetype_has_shapeId():
    assert hasattr(presentation_ShowShapeType, "shapeId")
    descriptor = None
    for klass in presentation_ShowShapeType.__mro__:
        if "shapeId" in klass.__dict__:
            descriptor = klass.__dict__["shapeId"]
            break
    assert isinstance(descriptor, property)

def test_presentation_showshapetype_has_effect():
    assert hasattr(presentation_ShowShapeType, "effect")
    descriptor = None
    for klass in presentation_ShowShapeType.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)



def test_presentation_playtype_is_not_abstract():
    assert not inspect.isabstract(presentation_PlayType)


def test_presentation_playtype_constructor_exists():
    assert callable(presentation_PlayType.__init__)


def test_presentation_playtype_constructor_args():
    sig = inspect.signature(presentation_PlayType.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"
    assert "shapeId" in params, "Missing parameter 'shapeId'"

def test_presentation_playtype_has_speed():
    assert hasattr(presentation_PlayType, "speed")
    descriptor = None
    for klass in presentation_PlayType.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_presentation_playtype_has_shapeId():
    assert hasattr(presentation_PlayType, "shapeId")
    descriptor = None
    for klass in presentation_PlayType.__mro__:
        if "shapeId" in klass.__dict__:
            descriptor = klass.__dict__["shapeId"]
            break
    assert isinstance(descriptor, property)



def test_presentation_showtype_is_not_abstract():
    assert not inspect.isabstract(presentation_ShowType)


def test_presentation_showtype_constructor_exists():
    assert callable(presentation_ShowType.__init__)


def test_presentation_showtype_constructor_args():
    sig = inspect.signature(presentation_ShowType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_presentation_showtype_has_name():
    assert hasattr(presentation_ShowType, "name")
    descriptor = None
    for klass in presentation_ShowType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_presentation_showtype_has_pages():
    assert hasattr(presentation_ShowType, "pages")
    descriptor = None
    for klass in presentation_ShowType.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)



def test_presentation_settingstype_is_not_abstract():
    assert not inspect.isabstract(presentation_SettingsType)


def test_presentation_settingstype_constructor_exists():
    assert callable(presentation_SettingsType.__init__)


def test_presentation_settingstype_constructor_args():
    sig = inspect.signature(presentation_SettingsType.__init__)
    params = list(sig.parameters.keys())
    assert "stayOnTop" in params, "Missing parameter 'stayOnTop'"
    assert "mouseVisible" in params, "Missing parameter 'mouseVisible'"
    assert "startWithNavigator" in params, "Missing parameter 'startWithNavigator'"
    assert "mouseAsPen" in params, "Missing parameter 'mouseAsPen'"
    assert "forceManual" in params, "Missing parameter 'forceManual'"
    assert "startPage" in params, "Missing parameter 'startPage'"
    assert "transitionOnClick" in params, "Missing parameter 'transitionOnClick'"
    assert "endless" in params, "Missing parameter 'endless'"
    assert "showLogo" in params, "Missing parameter 'showLogo'"
    assert "fullScreen" in params, "Missing parameter 'fullScreen'"
    assert "pause" in params, "Missing parameter 'pause'"
    assert "showEndOfPresentationSlide" in params, "Missing parameter 'showEndOfPresentationSlide'"
    assert "animations" in params, "Missing parameter 'animations'"
    assert "show1" in params, "Missing parameter 'show1'"

def test_presentation_settingstype_has_stayOnTop():
    assert hasattr(presentation_SettingsType, "stayOnTop")
    descriptor = None
    for klass in presentation_SettingsType.__mro__:
        if "stayOnTop" in klass.__dict__:
            descriptor = klass.__dict__["stayOnTop"]
            break
    assert isinstance(descriptor, property)

def test_presentation_settingstype_has_mouseVisible():
    assert hasattr(presentation_SettingsType, "mouseVisible")
    descriptor = None
    for klass in presentation_SettingsType.__mro__:
        if "mouseVisible" in klass.__dict__:
            descriptor = klass.__dict__["mouseVisible"]
            break
    assert isinstance(descriptor, property)

def test_presentation_settingstype_has_startWithNavigator():
    assert hasattr(presentation_SettingsType, "startWithNavigator")
    descriptor = None
    for klass in presentation_SettingsType.__mro__:
        if "startWithNavigator" in klass.__dict__:
            descriptor = klass.__dict__["startWithNavigator"]
            break
    assert isinstance(descriptor, property)

def test_presentation_settingstype_has_mouseAsPen():
    assert hasattr(presentation_SettingsType, "mouseAsPen")
    descriptor = None
    for klass in presentation_SettingsType.__mro__:
        if "mouseAsPen" in klass.__dict__:
            descriptor = klass.__dict__["mouseAsPen"]
            break
    assert isinstance(descriptor, property)

def test_presentation_settingstype_has_forceManual():
    assert hasattr(presentation_SettingsType, "forceManual")
    descriptor = None
    for klass in presentation_SettingsType.__mro__:
        if "forceManual" in klass.__dict__:
            descriptor = klass.__dict__["forceManual"]
            break
    assert isinstance(descriptor, property)

def test_presentation_settingstype_has_startPage():
    assert hasattr(presentation_SettingsType, "startPage")
    descriptor = None
    for klass in presentation_SettingsType.__mro__:
        if "startPage" in klass.__dict__:
            descriptor = klass.__dict__["startPage"]
            break
    assert isinstance(descriptor, property)

def test_presentation_settingstype_has_transitionOnClick():
    assert hasattr(presentation_SettingsType, "transitionOnClick")
    descriptor = None
    for klass in presentation_SettingsType.__mro__:
        if "transitionOnClick" in klass.__dict__:
            descriptor = klass.__dict__["transitionOnClick"]
            break
    assert isinstance(descriptor, property)

def test_presentation_settingstype_has_endless():
    assert hasattr(presentation_SettingsType, "endless")
    descriptor = None
    for klass in presentation_SettingsType.__mro__:
        if "endless" in klass.__dict__:
            descriptor = klass.__dict__["endless"]
            break
    assert isinstance(descriptor, property)

def test_presentation_settingstype_has_showLogo():
    assert hasattr(presentation_SettingsType, "showLogo")
    descriptor = None
    for klass in presentation_SettingsType.__mro__:
        if "showLogo" in klass.__dict__:
            descriptor = klass.__dict__["showLogo"]
            break
    assert isinstance(descriptor, property)

def test_presentation_settingstype_has_fullScreen():
    assert hasattr(presentation_SettingsType, "fullScreen")
    descriptor = None
    for klass in presentation_SettingsType.__mro__:
        if "fullScreen" in klass.__dict__:
            descriptor = klass.__dict__["fullScreen"]
            break
    assert isinstance(descriptor, property)

def test_presentation_settingstype_has_pause():
    assert hasattr(presentation_SettingsType, "pause")
    descriptor = None
    for klass in presentation_SettingsType.__mro__:
        if "pause" in klass.__dict__:
            descriptor = klass.__dict__["pause"]
            break
    assert isinstance(descriptor, property)

def test_presentation_settingstype_has_showEndOfPresentationSlide():
    assert hasattr(presentation_SettingsType, "showEndOfPresentationSlide")
    descriptor = None
    for klass in presentation_SettingsType.__mro__:
        if "showEndOfPresentationSlide" in klass.__dict__:
            descriptor = klass.__dict__["showEndOfPresentationSlide"]
            break
    assert isinstance(descriptor, property)

def test_presentation_settingstype_has_animations():
    assert hasattr(presentation_SettingsType, "animations")
    descriptor = None
    for klass in presentation_SettingsType.__mro__:
        if "animations" in klass.__dict__:
            descriptor = klass.__dict__["animations"]
            break
    assert isinstance(descriptor, property)

def test_presentation_settingstype_has_show1():
    assert hasattr(presentation_SettingsType, "show1")
    descriptor = None
    for klass in presentation_SettingsType.__mro__:
        if "show1" in klass.__dict__:
            descriptor = klass.__dict__["show1"]
            break
    assert isinstance(descriptor, property)



def test_presentation_placeholdertype_is_not_abstract():
    assert not inspect.isabstract(presentation_PlaceholderType)


def test_presentation_placeholdertype_constructor_exists():
    assert callable(presentation_PlaceholderType.__init__)


def test_presentation_placeholdertype_constructor_args():
    sig = inspect.signature(presentation_PlaceholderType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "object" in params, "Missing parameter 'object'"
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"
    assert "x" in params, "Missing parameter 'x'"

def test_presentation_placeholdertype_has_y():
    assert hasattr(presentation_PlaceholderType, "y")
    descriptor = None
    for klass in presentation_PlaceholderType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_presentation_placeholdertype_has_object():
    assert hasattr(presentation_PlaceholderType, "object")
    descriptor = None
    for klass in presentation_PlaceholderType.__mro__:
        if "object" in klass.__dict__:
            descriptor = klass.__dict__["object"]
            break
    assert isinstance(descriptor, property)

def test_presentation_placeholdertype_has_width():
    assert hasattr(presentation_PlaceholderType, "width")
    descriptor = None
    for klass in presentation_PlaceholderType.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_presentation_placeholdertype_has_height():
    assert hasattr(presentation_PlaceholderType, "height")
    descriptor = None
    for klass in presentation_PlaceholderType.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_presentation_placeholdertype_has_x():
    assert hasattr(presentation_PlaceholderType, "x")
    descriptor = None
    for klass in presentation_PlaceholderType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_presentation_customshapetype_is_not_abstract():
    assert not inspect.isabstract(presentation_CustomShapeType)


def test_presentation_customshapetype_constructor_exists():
    assert callable(presentation_CustomShapeType.__init__)


def test_presentation_customshapetype_constructor_args():
    sig = inspect.signature(presentation_CustomShapeType.__init__)
    params = list(sig.parameters.keys())



def test_presentation_scenetype_is_not_abstract():
    assert not inspect.isabstract(presentation_SceneType)


def test_presentation_scenetype_constructor_exists():
    assert callable(presentation_SceneType.__init__)


def test_presentation_scenetype_constructor_args():
    sig = inspect.signature(presentation_SceneType.__init__)
    params = list(sig.parameters.keys())



def test_presentation_controltype_is_not_abstract():
    assert not inspect.isabstract(presentation_ControlType)


def test_presentation_controltype_constructor_exists():
    assert callable(presentation_ControlType.__init__)


def test_presentation_controltype_constructor_args():
    sig = inspect.signature(presentation_ControlType.__init__)
    params = list(sig.parameters.keys())



def test_presentation_connectortype_is_not_abstract():
    assert not inspect.isabstract(presentation_ConnectorType)


def test_presentation_connectortype_constructor_exists():
    assert callable(presentation_ConnectorType.__init__)


def test_presentation_connectortype_constructor_args():
    sig = inspect.signature(presentation_ConnectorType.__init__)
    params = list(sig.parameters.keys())



def test_presentation_captiontype_is_not_abstract():
    assert not inspect.isabstract(presentation_CaptionType)


def test_presentation_captiontype_constructor_exists():
    assert callable(presentation_CaptionType.__init__)


def test_presentation_captiontype_constructor_args():
    sig = inspect.signature(presentation_CaptionType.__init__)
    params = list(sig.parameters.keys())



def test_presentation_measuretype_is_not_abstract():
    assert not inspect.isabstract(presentation_MeasureType)


def test_presentation_measuretype_constructor_exists():
    assert callable(presentation_MeasureType.__init__)


def test_presentation_measuretype_constructor_args():
    sig = inspect.signature(presentation_MeasureType.__init__)
    params = list(sig.parameters.keys())



def test_presentation_frametype_is_not_abstract():
    assert not inspect.isabstract(presentation_FrameType)


def test_presentation_frametype_constructor_exists():
    assert callable(presentation_FrameType.__init__)


def test_presentation_frametype_constructor_args():
    sig = inspect.signature(presentation_FrameType.__init__)
    params = list(sig.parameters.keys())



def test_presentation_pagethumbnailtype_is_not_abstract():
    assert not inspect.isabstract(presentation_PageThumbnailType)


def test_presentation_pagethumbnailtype_constructor_exists():
    assert callable(presentation_PageThumbnailType.__init__)


def test_presentation_pagethumbnailtype_constructor_args():
    sig = inspect.signature(presentation_PageThumbnailType.__init__)
    params = list(sig.parameters.keys())



def test_presentation_pathtype_is_not_abstract():
    assert not inspect.isabstract(presentation_PathType)


def test_presentation_pathtype_constructor_exists():
    assert callable(presentation_PathType.__init__)


def test_presentation_pathtype_constructor_args():
    sig = inspect.signature(presentation_PathType.__init__)
    params = list(sig.parameters.keys())



def test_presentation_gtype_is_not_abstract():
    assert not inspect.isabstract(presentation_GType)


def test_presentation_gtype_constructor_exists():
    assert callable(presentation_GType.__init__)


def test_presentation_gtype_constructor_args():
    sig = inspect.signature(presentation_GType.__init__)
    params = list(sig.parameters.keys())



def test_presentation_ellipsetype_is_not_abstract():
    assert not inspect.isabstract(presentation_EllipseType)


def test_presentation_ellipsetype_constructor_exists():
    assert callable(presentation_EllipseType.__init__)


def test_presentation_ellipsetype_constructor_args():
    sig = inspect.signature(presentation_EllipseType.__init__)
    params = list(sig.parameters.keys())



def test_presentation_circletype_is_not_abstract():
    assert not inspect.isabstract(presentation_CircleType)


def test_presentation_circletype_constructor_exists():
    assert callable(presentation_CircleType.__init__)


def test_presentation_circletype_constructor_args():
    sig = inspect.signature(presentation_CircleType.__init__)
    params = list(sig.parameters.keys())



def test_presentation_polylinetype_is_not_abstract():
    assert not inspect.isabstract(presentation_PolylineType)


def test_presentation_polylinetype_constructor_exists():
    assert callable(presentation_PolylineType.__init__)


def test_presentation_polylinetype_constructor_args():
    sig = inspect.signature(presentation_PolylineType.__init__)
    params = list(sig.parameters.keys())



def test_presentation_linetype_is_not_abstract():
    assert not inspect.isabstract(presentation_LineType)


def test_presentation_linetype_constructor_exists():
    assert callable(presentation_LineType.__init__)


def test_presentation_linetype_constructor_args():
    sig = inspect.signature(presentation_LineType.__init__)
    params = list(sig.parameters.keys())



def test_presentation_regularpolygontype_is_not_abstract():
    assert not inspect.isabstract(presentation_RegularPolygonType)


def test_presentation_regularpolygontype_constructor_exists():
    assert callable(presentation_RegularPolygonType.__init__)


def test_presentation_regularpolygontype_constructor_args():
    sig = inspect.signature(presentation_RegularPolygonType.__init__)
    params = list(sig.parameters.keys())



def test_presentation_polygontype_is_not_abstract():
    assert not inspect.isabstract(presentation_PolygonType)


def test_presentation_polygontype_constructor_exists():
    assert callable(presentation_PolygonType.__init__)


def test_presentation_polygontype_constructor_args():
    sig = inspect.signature(presentation_PolygonType.__init__)
    params = list(sig.parameters.keys())



def test_presentation_notestype_is_not_abstract():
    assert not inspect.isabstract(presentation_NotesType)


def test_presentation_notestype_constructor_exists():
    assert callable(presentation_NotesType.__init__)


def test_presentation_notestype_constructor_args():
    sig = inspect.signature(presentation_NotesType.__init__)
    params = list(sig.parameters.keys())
    assert "useHeaderName" in params, "Missing parameter 'useHeaderName'"
    assert "pageLayoutName" in params, "Missing parameter 'pageLayoutName'"
    assert "styleName" in params, "Missing parameter 'styleName'"
    assert "useDateTimeName" in params, "Missing parameter 'useDateTimeName'"
    assert "useFooterName" in params, "Missing parameter 'useFooterName'"
    assert "shape" in params, "Missing parameter 'shape'"

def test_presentation_notestype_has_useHeaderName():
    assert hasattr(presentation_NotesType, "useHeaderName")
    descriptor = None
    for klass in presentation_NotesType.__mro__:
        if "useHeaderName" in klass.__dict__:
            descriptor = klass.__dict__["useHeaderName"]
            break
    assert isinstance(descriptor, property)

def test_presentation_notestype_has_pageLayoutName():
    assert hasattr(presentation_NotesType, "pageLayoutName")
    descriptor = None
    for klass in presentation_NotesType.__mro__:
        if "pageLayoutName" in klass.__dict__:
            descriptor = klass.__dict__["pageLayoutName"]
            break
    assert isinstance(descriptor, property)

def test_presentation_notestype_has_styleName():
    assert hasattr(presentation_NotesType, "styleName")
    descriptor = None
    for klass in presentation_NotesType.__mro__:
        if "styleName" in klass.__dict__:
            descriptor = klass.__dict__["styleName"]
            break
    assert isinstance(descriptor, property)

def test_presentation_notestype_has_useDateTimeName():
    assert hasattr(presentation_NotesType, "useDateTimeName")
    descriptor = None
    for klass in presentation_NotesType.__mro__:
        if "useDateTimeName" in klass.__dict__:
            descriptor = klass.__dict__["useDateTimeName"]
            break
    assert isinstance(descriptor, property)

def test_presentation_notestype_has_useFooterName():
    assert hasattr(presentation_NotesType, "useFooterName")
    descriptor = None
    for klass in presentation_NotesType.__mro__:
        if "useFooterName" in klass.__dict__:
            descriptor = klass.__dict__["useFooterName"]
            break
    assert isinstance(descriptor, property)

def test_presentation_notestype_has_shape():
    assert hasattr(presentation_NotesType, "shape")
    descriptor = None
    for klass in presentation_NotesType.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_presentation_recttype_is_not_abstract():
    assert not inspect.isabstract(presentation_RectType)


def test_presentation_recttype_constructor_exists():
    assert callable(presentation_RectType.__init__)


def test_presentation_recttype_constructor_args():
    sig = inspect.signature(presentation_RectType.__init__)
    params = list(sig.parameters.keys())



def test_presentation_formstype_is_not_abstract():
    assert not inspect.isabstract(presentation_FormsType)


def test_presentation_formstype_constructor_exists():
    assert callable(presentation_FormsType.__init__)


def test_presentation_formstype_constructor_args():
    sig = inspect.signature(presentation_FormsType.__init__)
    params = list(sig.parameters.keys())



def test_presentation_hidetexttype_is_not_abstract():
    assert not inspect.isabstract(presentation_HideTextType)


def test_presentation_hidetexttype_constructor_exists():
    assert callable(presentation_HideTextType.__init__)


def test_presentation_hidetexttype_constructor_args():
    sig = inspect.signature(presentation_HideTextType.__init__)
    params = list(sig.parameters.keys())
    assert "shapeId" in params, "Missing parameter 'shapeId'"
    assert "startScale" in params, "Missing parameter 'startScale'"
    assert "speed" in params, "Missing parameter 'speed'"
    assert "delay" in params, "Missing parameter 'delay'"
    assert "pathId" in params, "Missing parameter 'pathId'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "direction" in params, "Missing parameter 'direction'"

def test_presentation_hidetexttype_has_shapeId():
    assert hasattr(presentation_HideTextType, "shapeId")
    descriptor = None
    for klass in presentation_HideTextType.__mro__:
        if "shapeId" in klass.__dict__:
            descriptor = klass.__dict__["shapeId"]
            break
    assert isinstance(descriptor, property)

def test_presentation_hidetexttype_has_startScale():
    assert hasattr(presentation_HideTextType, "startScale")
    descriptor = None
    for klass in presentation_HideTextType.__mro__:
        if "startScale" in klass.__dict__:
            descriptor = klass.__dict__["startScale"]
            break
    assert isinstance(descriptor, property)

def test_presentation_hidetexttype_has_speed():
    assert hasattr(presentation_HideTextType, "speed")
    descriptor = None
    for klass in presentation_HideTextType.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_presentation_hidetexttype_has_delay():
    assert hasattr(presentation_HideTextType, "delay")
    descriptor = None
    for klass in presentation_HideTextType.__mro__:
        if "delay" in klass.__dict__:
            descriptor = klass.__dict__["delay"]
            break
    assert isinstance(descriptor, property)

def test_presentation_hidetexttype_has_pathId():
    assert hasattr(presentation_HideTextType, "pathId")
    descriptor = None
    for klass in presentation_HideTextType.__mro__:
        if "pathId" in klass.__dict__:
            descriptor = klass.__dict__["pathId"]
            break
    assert isinstance(descriptor, property)

def test_presentation_hidetexttype_has_effect():
    assert hasattr(presentation_HideTextType, "effect")
    descriptor = None
    for klass in presentation_HideTextType.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_presentation_hidetexttype_has_direction():
    assert hasattr(presentation_HideTextType, "direction")
    descriptor = None
    for klass in presentation_HideTextType.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_presentation_footerdecltype_is_not_abstract():
    assert not inspect.isabstract(presentation_FooterDeclType)


def test_presentation_footerdecltype_constructor_exists():
    assert callable(presentation_FooterDeclType.__init__)


def test_presentation_footerdecltype_constructor_args():
    sig = inspect.signature(presentation_FooterDeclType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation_footerdecltype_has_name():
    assert hasattr(presentation_FooterDeclType, "name")
    descriptor = None
    for klass in presentation_FooterDeclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_presentation_footerdecltype_has_mixed():
    assert hasattr(presentation_FooterDeclType, "mixed")
    descriptor = None
    for klass in presentation_FooterDeclType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation_hideshapetype_is_not_abstract():
    assert not inspect.isabstract(presentation_HideShapeType)


def test_presentation_hideshapetype_constructor_exists():
    assert callable(presentation_HideShapeType.__init__)


def test_presentation_hideshapetype_constructor_args():
    sig = inspect.signature(presentation_HideShapeType.__init__)
    params = list(sig.parameters.keys())
    assert "effect" in params, "Missing parameter 'effect'"
    assert "startScale" in params, "Missing parameter 'startScale'"
    assert "pathId" in params, "Missing parameter 'pathId'"
    assert "speed" in params, "Missing parameter 'speed'"
    assert "shapeId" in params, "Missing parameter 'shapeId'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "delay" in params, "Missing parameter 'delay'"

def test_presentation_hideshapetype_has_effect():
    assert hasattr(presentation_HideShapeType, "effect")
    descriptor = None
    for klass in presentation_HideShapeType.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_presentation_hideshapetype_has_startScale():
    assert hasattr(presentation_HideShapeType, "startScale")
    descriptor = None
    for klass in presentation_HideShapeType.__mro__:
        if "startScale" in klass.__dict__:
            descriptor = klass.__dict__["startScale"]
            break
    assert isinstance(descriptor, property)

def test_presentation_hideshapetype_has_pathId():
    assert hasattr(presentation_HideShapeType, "pathId")
    descriptor = None
    for klass in presentation_HideShapeType.__mro__:
        if "pathId" in klass.__dict__:
            descriptor = klass.__dict__["pathId"]
            break
    assert isinstance(descriptor, property)

def test_presentation_hideshapetype_has_speed():
    assert hasattr(presentation_HideShapeType, "speed")
    descriptor = None
    for klass in presentation_HideShapeType.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_presentation_hideshapetype_has_shapeId():
    assert hasattr(presentation_HideShapeType, "shapeId")
    descriptor = None
    for klass in presentation_HideShapeType.__mro__:
        if "shapeId" in klass.__dict__:
            descriptor = klass.__dict__["shapeId"]
            break
    assert isinstance(descriptor, property)

def test_presentation_hideshapetype_has_direction():
    assert hasattr(presentation_HideShapeType, "direction")
    descriptor = None
    for klass in presentation_HideShapeType.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_presentation_hideshapetype_has_delay():
    assert hasattr(presentation_HideShapeType, "delay")
    descriptor = None
    for klass in presentation_HideShapeType.__mro__:
        if "delay" in klass.__dict__:
            descriptor = klass.__dict__["delay"]
            break
    assert isinstance(descriptor, property)



def test_presentation_headertype_is_not_abstract():
    assert not inspect.isabstract(presentation_HeaderType)


def test_presentation_headertype_constructor_exists():
    assert callable(presentation_HeaderType.__init__)


def test_presentation_headertype_constructor_args():
    sig = inspect.signature(presentation_HeaderType.__init__)
    params = list(sig.parameters.keys())



def test_presentation_headerdecltype_is_not_abstract():
    assert not inspect.isabstract(presentation_HeaderDeclType)


def test_presentation_headerdecltype_constructor_exists():
    assert callable(presentation_HeaderDeclType.__init__)


def test_presentation_headerdecltype_constructor_args():
    sig = inspect.signature(presentation_HeaderDeclType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "name" in params, "Missing parameter 'name'"

def test_presentation_headerdecltype_has_mixed():
    assert hasattr(presentation_HeaderDeclType, "mixed")
    descriptor = None
    for klass in presentation_HeaderDeclType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_presentation_headerdecltype_has_name():
    assert hasattr(presentation_HeaderDeclType, "name")
    descriptor = None
    for klass in presentation_HeaderDeclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_presentation_footertype_is_not_abstract():
    assert not inspect.isabstract(presentation_FooterType)


def test_presentation_footertype_constructor_exists():
    assert callable(presentation_FooterType.__init__)


def test_presentation_footertype_constructor_args():
    sig = inspect.signature(presentation_FooterType.__init__)
    params = list(sig.parameters.keys())



def test_presentation_dimtype_is_not_abstract():
    assert not inspect.isabstract(presentation_DimType)


def test_presentation_dimtype_constructor_exists():
    assert callable(presentation_DimType.__init__)


def test_presentation_dimtype_constructor_args():
    sig = inspect.signature(presentation_DimType.__init__)
    params = list(sig.parameters.keys())
    assert "shapeId" in params, "Missing parameter 'shapeId'"
    assert "color" in params, "Missing parameter 'color'"

def test_presentation_dimtype_has_shapeId():
    assert hasattr(presentation_DimType, "shapeId")
    descriptor = None
    for klass in presentation_DimType.__mro__:
        if "shapeId" in klass.__dict__:
            descriptor = klass.__dict__["shapeId"]
            break
    assert isinstance(descriptor, property)

def test_presentation_dimtype_has_color():
    assert hasattr(presentation_DimType, "color")
    descriptor = None
    for klass in presentation_DimType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_presentation_datetimetype_is_not_abstract():
    assert not inspect.isabstract(presentation_DateTimeType)


def test_presentation_datetimetype_constructor_exists():
    assert callable(presentation_DateTimeType.__init__)


def test_presentation_datetimetype_constructor_args():
    sig = inspect.signature(presentation_DateTimeType.__init__)
    params = list(sig.parameters.keys())



def test_presentation_eventlistenertype_is_not_abstract():
    assert not inspect.isabstract(presentation_EventListenerType)


def test_presentation_eventlistenertype_constructor_exists():
    assert callable(presentation_EventListenerType.__init__)


def test_presentation_eventlistenertype_constructor_args():
    sig = inspect.signature(presentation_EventListenerType.__init__)
    params = list(sig.parameters.keys())
    assert "show" in params, "Missing parameter 'show'"
    assert "startScale" in params, "Missing parameter 'startScale'"
    assert "href" in params, "Missing parameter 'href'"
    assert "speed" in params, "Missing parameter 'speed'"
    assert "verb" in params, "Missing parameter 'verb'"
    assert "action" in params, "Missing parameter 'action'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "type" in params, "Missing parameter 'type'"
    assert "actuate" in params, "Missing parameter 'actuate'"
    assert "eventName" in params, "Missing parameter 'eventName'"

def test_presentation_eventlistenertype_has_show():
    assert hasattr(presentation_EventListenerType, "show")
    descriptor = None
    for klass in presentation_EventListenerType.__mro__:
        if "show" in klass.__dict__:
            descriptor = klass.__dict__["show"]
            break
    assert isinstance(descriptor, property)

def test_presentation_eventlistenertype_has_startScale():
    assert hasattr(presentation_EventListenerType, "startScale")
    descriptor = None
    for klass in presentation_EventListenerType.__mro__:
        if "startScale" in klass.__dict__:
            descriptor = klass.__dict__["startScale"]
            break
    assert isinstance(descriptor, property)

def test_presentation_eventlistenertype_has_href():
    assert hasattr(presentation_EventListenerType, "href")
    descriptor = None
    for klass in presentation_EventListenerType.__mro__:
        if "href" in klass.__dict__:
            descriptor = klass.__dict__["href"]
            break
    assert isinstance(descriptor, property)

def test_presentation_eventlistenertype_has_speed():
    assert hasattr(presentation_EventListenerType, "speed")
    descriptor = None
    for klass in presentation_EventListenerType.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_presentation_eventlistenertype_has_verb():
    assert hasattr(presentation_EventListenerType, "verb")
    descriptor = None
    for klass in presentation_EventListenerType.__mro__:
        if "verb" in klass.__dict__:
            descriptor = klass.__dict__["verb"]
            break
    assert isinstance(descriptor, property)

def test_presentation_eventlistenertype_has_action():
    assert hasattr(presentation_EventListenerType, "action")
    descriptor = None
    for klass in presentation_EventListenerType.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_presentation_eventlistenertype_has_effect():
    assert hasattr(presentation_EventListenerType, "effect")
    descriptor = None
    for klass in presentation_EventListenerType.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_presentation_eventlistenertype_has_direction():
    assert hasattr(presentation_EventListenerType, "direction")
    descriptor = None
    for klass in presentation_EventListenerType.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_presentation_eventlistenertype_has_type():
    assert hasattr(presentation_EventListenerType, "type")
    descriptor = None
    for klass in presentation_EventListenerType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_presentation_eventlistenertype_has_actuate():
    assert hasattr(presentation_EventListenerType, "actuate")
    descriptor = None
    for klass in presentation_EventListenerType.__mro__:
        if "actuate" in klass.__dict__:
            descriptor = klass.__dict__["actuate"]
            break
    assert isinstance(descriptor, property)

def test_presentation_eventlistenertype_has_eventName():
    assert hasattr(presentation_EventListenerType, "eventName")
    descriptor = None
    for klass in presentation_EventListenerType.__mro__:
        if "eventName" in klass.__dict__:
            descriptor = klass.__dict__["eventName"]
            break
    assert isinstance(descriptor, property)



def test_presentation_soundtype_is_not_abstract():
    assert not inspect.isabstract(presentation_SoundType)


def test_presentation_soundtype_constructor_exists():
    assert callable(presentation_SoundType.__init__)


def test_presentation_soundtype_constructor_args():
    sig = inspect.signature(presentation_SoundType.__init__)
    params = list(sig.parameters.keys())
    assert "show" in params, "Missing parameter 'show'"
    assert "type" in params, "Missing parameter 'type'"
    assert "href" in params, "Missing parameter 'href'"
    assert "actuate" in params, "Missing parameter 'actuate'"
    assert "playFull" in params, "Missing parameter 'playFull'"

def test_presentation_soundtype_has_show():
    assert hasattr(presentation_SoundType, "show")
    descriptor = None
    for klass in presentation_SoundType.__mro__:
        if "show" in klass.__dict__:
            descriptor = klass.__dict__["show"]
            break
    assert isinstance(descriptor, property)

def test_presentation_soundtype_has_type():
    assert hasattr(presentation_SoundType, "type")
    descriptor = None
    for klass in presentation_SoundType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_presentation_soundtype_has_href():
    assert hasattr(presentation_SoundType, "href")
    descriptor = None
    for klass in presentation_SoundType.__mro__:
        if "href" in klass.__dict__:
            descriptor = klass.__dict__["href"]
            break
    assert isinstance(descriptor, property)

def test_presentation_soundtype_has_actuate():
    assert hasattr(presentation_SoundType, "actuate")
    descriptor = None
    for klass in presentation_SoundType.__mro__:
        if "actuate" in klass.__dict__:
            descriptor = klass.__dict__["actuate"]
            break
    assert isinstance(descriptor, property)

def test_presentation_soundtype_has_playFull():
    assert hasattr(presentation_SoundType, "playFull")
    descriptor = None
    for klass in presentation_SoundType.__mro__:
        if "playFull" in klass.__dict__:
            descriptor = klass.__dict__["playFull"]
            break
    assert isinstance(descriptor, property)



def test_presentation_animationstype1_is_not_abstract():
    assert not inspect.isabstract(presentation_AnimationsType1)


def test_presentation_animationstype1_constructor_exists():
    assert callable(presentation_AnimationsType1.__init__)


def test_presentation_animationstype1_constructor_args():
    sig = inspect.signature(presentation_AnimationsType1.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "presentationAnimationElementsGroup" in params, "Missing parameter 'presentationAnimationElementsGroup'"

def test_presentation_animationstype1_has_group():
    assert hasattr(presentation_AnimationsType1, "group")
    descriptor = None
    for klass in presentation_AnimationsType1.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation_animationstype1_has_presentationAnimationElementsGroup():
    assert hasattr(presentation_AnimationsType1, "presentationAnimationElementsGroup")
    descriptor = None
    for klass in presentation_AnimationsType1.__mro__:
        if "presentationAnimationElementsGroup" in klass.__dict__:
            descriptor = klass.__dict__["presentationAnimationElementsGroup"]
            break
    assert isinstance(descriptor, property)



def test_presentation_eobject_is_not_abstract():
    assert not inspect.isabstract(presentation_EObject)


def test_presentation_eobject_constructor_exists():
    assert callable(presentation_EObject.__init__)


def test_presentation_eobject_constructor_args():
    sig = inspect.signature(presentation_EObject.__init__)
    params = list(sig.parameters.keys())



def test_presentation_datetimedecltype_is_not_abstract():
    assert not inspect.isabstract(presentation_DateTimeDeclType)


def test_presentation_datetimedecltype_constructor_exists():
    assert callable(presentation_DateTimeDeclType.__init__)


def test_presentation_datetimedecltype_constructor_args():
    sig = inspect.signature(presentation_DateTimeDeclType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "source" in params, "Missing parameter 'source'"
    assert "dataStyleName" in params, "Missing parameter 'dataStyleName'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation_datetimedecltype_has_name():
    assert hasattr(presentation_DateTimeDeclType, "name")
    descriptor = None
    for klass in presentation_DateTimeDeclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_presentation_datetimedecltype_has_source():
    assert hasattr(presentation_DateTimeDeclType, "source")
    descriptor = None
    for klass in presentation_DateTimeDeclType.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_presentation_datetimedecltype_has_dataStyleName():
    assert hasattr(presentation_DateTimeDeclType, "dataStyleName")
    descriptor = None
    for klass in presentation_DateTimeDeclType.__mro__:
        if "dataStyleName" in klass.__dict__:
            descriptor = klass.__dict__["dataStyleName"]
            break
    assert isinstance(descriptor, property)

def test_presentation_datetimedecltype_has_mixed():
    assert hasattr(presentation_DateTimeDeclType, "mixed")
    descriptor = None
    for klass in presentation_DateTimeDeclType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation_animationgrouptype_is_not_abstract():
    assert not inspect.isabstract(presentation_AnimationGroupType)


def test_presentation_animationgrouptype_constructor_exists():
    assert callable(presentation_AnimationGroupType.__init__)


def test_presentation_animationgrouptype_constructor_args():
    sig = inspect.signature(presentation_AnimationGroupType.__init__)
    params = list(sig.parameters.keys())
    assert "presentationAnimationElementsGroup" in params, "Missing parameter 'presentationAnimationElementsGroup'"

def test_presentation_animationgrouptype_has_presentationAnimationElementsGroup():
    assert hasattr(presentation_AnimationGroupType, "presentationAnimationElementsGroup")
    descriptor = None
    for klass in presentation_AnimationGroupType.__mro__:
        if "presentationAnimationElementsGroup" in klass.__dict__:
            descriptor = klass.__dict__["presentationAnimationElementsGroup"]
            break
    assert isinstance(descriptor, property)

def test_animationstype_exists():
    # Check that the Enumeration exists
    assert AnimationsType is not None

def test_animationstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AnimationsType]
    expected_literals = [
        "enabled",
        "disabled",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AnimationsType"

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

def test_nodetypetype_exists():
    # Check that the Enumeration exists
    assert NodeTypeType is not None

def test_nodetypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NodeTypeType]
    expected_literals = [
        "afterPrevious",
        "mainSequence",
        "timingRoot",
        "withPrevious",
        "default",
        "onClick",
        "interactiveSequence",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NodeTypeType"

def test_actiontype_exists():
    # Check that the Enumeration exists
    assert ActionType is not None

def test_actiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionType]
    expected_literals = [
        "sound",
        "firstPage",
        "previousPage",
        "nextPage",
        "stop",
        "hide",
        "lastPage",
        "fadeOut",
        "verb",
        "none",
        "show",
        "execute",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionType"

def test_presetclasstype_exists():
    # Check that the Enumeration exists
    assert PresetClassType is not None

def test_presetclasstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PresetClassType]
    expected_literals = [
        "exit",
        "oleAction",
        "custom",
        "mediaCall",
        "motionPath",
        "entrance",
        "emphasis",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PresetClassType"

def test_transitionstyletype_exists():
    # Check that the Enumeration exists
    assert TransitionStyleType is not None

def test_transitionstyletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionStyleType]
    expected_literals = [
        "dissolve",
        "wavylineFromTop",
        "fadeFromTop",
        "rollFromBottom",
        "moveFromLowerright",
        "moveFromLeft",
        "fadeFromLowerleft",
        "stretchFromLeft",
        "fadeToCenter",
        "horizontalCheckerboard",
        "rollFromLeft",
        "openHorizontal",
        "counterclockwise",
        "fadeFromRight",
        "flyAway",
        "horizontalStripes",
        "closeVertical",
        "spiraloutLeft",
        "moveFromTop",
        "uncoverToRight",
        "melt",
        "verticalLines",
        "spiraloutRight",
        "rollFromTop",
        "verticalCheckerboard",
        "fadeFromCenter",
        "wavylineFromLeft",
        "moveFromBottom",
        "stretchFromRight",
        "fadeFromUpperright",
        "fadeFromLeft",
        "spiralinLeft",
        "uncoverToBottom",
        "uncoverToUpperleft",
        "none",
        "interlockingVerticalTop",
        "moveFromLowerleft",
        "open",
        "uncoverToLowerleft",
        "moveFromRight",
        "fadeFromLowerright",
        "rollFromRight",
        "closeHorizontal",
        "random",
        "clockwise",
        "uncoverToLowerright",
        "moveFromUpperright",
        "wavylineFromBottom",
        "moveFromUpperleft",
        "stretchFromTop",
        "interlockingVerticalBottom",
        "interlockingHorizontalLeft",
        "openVertical",
        "wavylineFromRight",
        "uncoverToUpperright",
        "verticalStripes",
        "close",
        "fadeFromBottom",
        "fadeFromUpperleft",
        "uncoverToLeft",
        "spiralinRight",
        "stretchFromBottom",
        "uncoverToTop",
        "interlockingHorizontalRight",
        "horizontalLines",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionStyleType"

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

def test_transitiontypetype_exists():
    # Check that the Enumeration exists
    assert TransitionTypeType is not None

def test_transitiontypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionTypeType]
    expected_literals = [
        "semiAutomatic",
        "manual",
        "automatic",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionTypeType"

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
presentation_EStringToStringMapEntry_strategy = st.builds(
    presentation_EStringToStringMapEntry,
)
presentation_DocumentRoot_strategy = st.builds(
    presentation_DocumentRoot,
    startWithNavigator=
        safe_text,
    source=
        safe_text,
    displayFooter=
        safe_text,
    forceManual=
        safe_text,
    useDateTimeName=
        safe_text,
    displayPageNumber=
        safe_text,
    delay=
        safe_text,
    transitionStyle=
        safe_text,
    displayDateTime=
        safe_text,
    transitionType=
        safe_text,
    transitionOnClick=
        safe_text,
    showLogo=
        safe_text,
    pathId=
        safe_text,
    displayHeader=
        safe_text,
    masterElement=
        safe_text,
    visibility=
        safe_text,
    useFooterName=
        safe_text,
    show1=
        safe_text,
    duration=
        safe_text,
    startScale=
        safe_text,
    fullScreen=
        safe_text,
    effect=
        safe_text,
    direction=
        safe_text,
    nodeType=
        safe_text,
    mouseAsPen=
        safe_text,
    mouseVisible=
        safe_text,
    mixed=
        safe_text,
    userTransformed=
        safe_text,
    backgroundObjectsVisible=
        safe_text,
    transitionSpeed=
        safe_text,
    name=
        safe_text,
    presetClass=
        safe_text,
    endless=
        safe_text,
    action=
        safe_text,
    stayOnTop=
        safe_text,
    verb=
        safe_text,
    presetSubType=
        safe_text,
    placeholder1=
        safe_text,
    pages=
        safe_text,
    animations1=
        safe_text,
    startPage=
        safe_text,
    groupId=
        safe_text,
    speed=
        safe_text,
    class_=
        safe_text,
    styleName=
        safe_text,
    useHeaderName=
        safe_text,
    playFull=
        safe_text,
    backgroundVisible=
        safe_text,
    presentationPageLayoutName=
        safe_text,
    showEndOfPresentationSlide=
        safe_text,
    presetId=
        safe_text,
    classNames=
        safe_text,
    pause=
        safe_text
)
presentation_ShowTextType_strategy = st.builds(
    presentation_ShowTextType,
    delay=
        safe_text,
    pathId=
        safe_text,
    effect=
        safe_text,
    shapeId=
        safe_text,
    direction=
        safe_text,
    startScale=
        safe_text,
    speed=
        safe_text
)
presentation_ShowShapeType_strategy = st.builds(
    presentation_ShowShapeType,
    direction=
        safe_text,
    startScale=
        safe_text,
    delay=
        safe_text,
    speed=
        safe_text,
    pathId=
        safe_text,
    shapeId=
        safe_text,
    effect=
        safe_text
)
presentation_PlayType_strategy = st.builds(
    presentation_PlayType,
    speed=
        safe_text,
    shapeId=
        safe_text
)
presentation_ShowType_strategy = st.builds(
    presentation_ShowType,
    name=
        safe_text,
    pages=
        safe_text
)
presentation_SettingsType_strategy = st.builds(
    presentation_SettingsType,
    stayOnTop=
        safe_text,
    mouseVisible=
        safe_text,
    startWithNavigator=
        safe_text,
    mouseAsPen=
        safe_text,
    forceManual=
        safe_text,
    startPage=
        safe_text,
    transitionOnClick=
        safe_text,
    endless=
        safe_text,
    showLogo=
        safe_text,
    fullScreen=
        safe_text,
    pause=
        safe_text,
    showEndOfPresentationSlide=
        safe_text,
    animations=
        safe_text,
    show1=
        safe_text
)
presentation_PlaceholderType_strategy = st.builds(
    presentation_PlaceholderType,
    y=
        safe_text,
    object=
        safe_text,
    width=
        safe_text,
    height=
        safe_text,
    x=
        safe_text
)
presentation_CustomShapeType_strategy = st.builds(
    presentation_CustomShapeType,
)
presentation_SceneType_strategy = st.builds(
    presentation_SceneType,
)
presentation_ControlType_strategy = st.builds(
    presentation_ControlType,
)
presentation_ConnectorType_strategy = st.builds(
    presentation_ConnectorType,
)
presentation_CaptionType_strategy = st.builds(
    presentation_CaptionType,
)
presentation_MeasureType_strategy = st.builds(
    presentation_MeasureType,
)
presentation_FrameType_strategy = st.builds(
    presentation_FrameType,
)
presentation_PageThumbnailType_strategy = st.builds(
    presentation_PageThumbnailType,
)
presentation_PathType_strategy = st.builds(
    presentation_PathType,
)
presentation_GType_strategy = st.builds(
    presentation_GType,
)
presentation_EllipseType_strategy = st.builds(
    presentation_EllipseType,
)
presentation_CircleType_strategy = st.builds(
    presentation_CircleType,
)
presentation_PolylineType_strategy = st.builds(
    presentation_PolylineType,
)
presentation_LineType_strategy = st.builds(
    presentation_LineType,
)
presentation_RegularPolygonType_strategy = st.builds(
    presentation_RegularPolygonType,
)
presentation_PolygonType_strategy = st.builds(
    presentation_PolygonType,
)
presentation_NotesType_strategy = st.builds(
    presentation_NotesType,
    useHeaderName=
        safe_text,
    pageLayoutName=
        safe_text,
    styleName=
        safe_text,
    useDateTimeName=
        safe_text,
    useFooterName=
        safe_text,
    shape=
        safe_text
)
presentation_RectType_strategy = st.builds(
    presentation_RectType,
)
presentation_FormsType_strategy = st.builds(
    presentation_FormsType,
)
presentation_HideTextType_strategy = st.builds(
    presentation_HideTextType,
    shapeId=
        safe_text,
    startScale=
        safe_text,
    speed=
        safe_text,
    delay=
        safe_text,
    pathId=
        safe_text,
    effect=
        safe_text,
    direction=
        safe_text
)
presentation_FooterDeclType_strategy = st.builds(
    presentation_FooterDeclType,
    name=
        safe_text,
    mixed=
        safe_text
)
presentation_HideShapeType_strategy = st.builds(
    presentation_HideShapeType,
    effect=
        safe_text,
    startScale=
        safe_text,
    pathId=
        safe_text,
    speed=
        safe_text,
    shapeId=
        safe_text,
    direction=
        safe_text,
    delay=
        safe_text
)
presentation_HeaderType_strategy = st.builds(
    presentation_HeaderType,
)
presentation_HeaderDeclType_strategy = st.builds(
    presentation_HeaderDeclType,
    mixed=
        safe_text,
    name=
        safe_text
)
presentation_FooterType_strategy = st.builds(
    presentation_FooterType,
)
presentation_DimType_strategy = st.builds(
    presentation_DimType,
    shapeId=
        safe_text,
    color=
        safe_text
)
presentation_DateTimeType_strategy = st.builds(
    presentation_DateTimeType,
)
presentation_EventListenerType_strategy = st.builds(
    presentation_EventListenerType,
    show=
        safe_text,
    startScale=
        safe_text,
    href=
        safe_text,
    speed=
        safe_text,
    verb=
        safe_text,
    action=
        safe_text,
    effect=
        safe_text,
    direction=
        safe_text,
    type=
        safe_text,
    actuate=
        safe_text,
    eventName=
        safe_text
)
presentation_SoundType_strategy = st.builds(
    presentation_SoundType,
    show=
        safe_text,
    type=
        safe_text,
    href=
        safe_text,
    actuate=
        safe_text,
    playFull=
        safe_text
)
presentation_AnimationsType1_strategy = st.builds(
    presentation_AnimationsType1,
    group=
        safe_text,
    presentationAnimationElementsGroup=
        safe_text
)
presentation_EObject_strategy = st.builds(
    presentation_EObject,
)
presentation_DateTimeDeclType_strategy = st.builds(
    presentation_DateTimeDeclType,
    name=
        safe_text,
    source=
        safe_text,
    dataStyleName=
        safe_text,
    mixed=
        safe_text
)
presentation_AnimationGroupType_strategy = st.builds(
    presentation_AnimationGroupType,
    presentationAnimationElementsGroup=
        safe_text
)

@given(instance=presentation_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_presentation_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, presentation_EStringToStringMapEntry)

@given(instance=presentation_DocumentRoot_strategy)
@settings(max_examples=50)
def test_presentation_documentroot_instantiation(instance):
    assert isinstance(instance, presentation_DocumentRoot)



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_startWithNavigator_setter(instance):
    original = instance.startWithNavigator
    instance.startWithNavigator = original
    assert instance.startWithNavigator == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_displayFooter_setter(instance):
    original = instance.displayFooter
    instance.displayFooter = original
    assert instance.displayFooter == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_forceManual_setter(instance):
    original = instance.forceManual
    instance.forceManual = original
    assert instance.forceManual == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_useDateTimeName_setter(instance):
    original = instance.useDateTimeName
    instance.useDateTimeName = original
    assert instance.useDateTimeName == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_displayPageNumber_setter(instance):
    original = instance.displayPageNumber
    instance.displayPageNumber = original
    assert instance.displayPageNumber == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_delay_setter(instance):
    original = instance.delay
    instance.delay = original
    assert instance.delay == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_transitionStyle_setter(instance):
    original = instance.transitionStyle
    instance.transitionStyle = original
    assert instance.transitionStyle == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_displayDateTime_setter(instance):
    original = instance.displayDateTime
    instance.displayDateTime = original
    assert instance.displayDateTime == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_transitionType_setter(instance):
    original = instance.transitionType
    instance.transitionType = original
    assert instance.transitionType == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_transitionOnClick_setter(instance):
    original = instance.transitionOnClick
    instance.transitionOnClick = original
    assert instance.transitionOnClick == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_showLogo_setter(instance):
    original = instance.showLogo
    instance.showLogo = original
    assert instance.showLogo == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_pathId_setter(instance):
    original = instance.pathId
    instance.pathId = original
    assert instance.pathId == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_displayHeader_setter(instance):
    original = instance.displayHeader
    instance.displayHeader = original
    assert instance.displayHeader == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_masterElement_setter(instance):
    original = instance.masterElement
    instance.masterElement = original
    assert instance.masterElement == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_useFooterName_setter(instance):
    original = instance.useFooterName
    instance.useFooterName = original
    assert instance.useFooterName == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_show1_setter(instance):
    original = instance.show1
    instance.show1 = original
    assert instance.show1 == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_startScale_setter(instance):
    original = instance.startScale
    instance.startScale = original
    assert instance.startScale == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_fullScreen_setter(instance):
    original = instance.fullScreen
    instance.fullScreen = original
    assert instance.fullScreen == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_nodeType_setter(instance):
    original = instance.nodeType
    instance.nodeType = original
    assert instance.nodeType == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_mouseAsPen_setter(instance):
    original = instance.mouseAsPen
    instance.mouseAsPen = original
    assert instance.mouseAsPen == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_mouseVisible_setter(instance):
    original = instance.mouseVisible
    instance.mouseVisible = original
    assert instance.mouseVisible == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_userTransformed_setter(instance):
    original = instance.userTransformed
    instance.userTransformed = original
    assert instance.userTransformed == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_backgroundObjectsVisible_setter(instance):
    original = instance.backgroundObjectsVisible
    instance.backgroundObjectsVisible = original
    assert instance.backgroundObjectsVisible == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_transitionSpeed_setter(instance):
    original = instance.transitionSpeed
    instance.transitionSpeed = original
    assert instance.transitionSpeed == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_presetClass_setter(instance):
    original = instance.presetClass
    instance.presetClass = original
    assert instance.presetClass == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_endless_setter(instance):
    original = instance.endless
    instance.endless = original
    assert instance.endless == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_stayOnTop_setter(instance):
    original = instance.stayOnTop
    instance.stayOnTop = original
    assert instance.stayOnTop == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_verb_setter(instance):
    original = instance.verb
    instance.verb = original
    assert instance.verb == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_presetSubType_setter(instance):
    original = instance.presetSubType
    instance.presetSubType = original
    assert instance.presetSubType == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_placeholder1_setter(instance):
    original = instance.placeholder1
    instance.placeholder1 = original
    assert instance.placeholder1 == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_animations1_setter(instance):
    original = instance.animations1
    instance.animations1 = original
    assert instance.animations1 == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_startPage_setter(instance):
    original = instance.startPage
    instance.startPage = original
    assert instance.startPage == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_groupId_setter(instance):
    original = instance.groupId
    instance.groupId = original
    assert instance.groupId == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_styleName_setter(instance):
    original = instance.styleName
    instance.styleName = original
    assert instance.styleName == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_useHeaderName_setter(instance):
    original = instance.useHeaderName
    instance.useHeaderName = original
    assert instance.useHeaderName == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_playFull_setter(instance):
    original = instance.playFull
    instance.playFull = original
    assert instance.playFull == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_backgroundVisible_setter(instance):
    original = instance.backgroundVisible
    instance.backgroundVisible = original
    assert instance.backgroundVisible == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_presentationPageLayoutName_setter(instance):
    original = instance.presentationPageLayoutName
    instance.presentationPageLayoutName = original
    assert instance.presentationPageLayoutName == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_showEndOfPresentationSlide_setter(instance):
    original = instance.showEndOfPresentationSlide
    instance.showEndOfPresentationSlide = original
    assert instance.showEndOfPresentationSlide == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_presetId_setter(instance):
    original = instance.presetId
    instance.presetId = original
    assert instance.presetId == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_classNames_setter(instance):
    original = instance.classNames
    instance.classNames = original
    assert instance.classNames == original



@given(instance=presentation_DocumentRoot_strategy)
def test_presentation_documentroot_pause_setter(instance):
    original = instance.pause
    instance.pause = original
    assert instance.pause == original

@given(instance=presentation_ShowTextType_strategy)
@settings(max_examples=50)
def test_presentation_showtexttype_instantiation(instance):
    assert isinstance(instance, presentation_ShowTextType)



@given(instance=presentation_ShowTextType_strategy)
def test_presentation_showtexttype_delay_setter(instance):
    original = instance.delay
    instance.delay = original
    assert instance.delay == original



@given(instance=presentation_ShowTextType_strategy)
def test_presentation_showtexttype_pathId_setter(instance):
    original = instance.pathId
    instance.pathId = original
    assert instance.pathId == original



@given(instance=presentation_ShowTextType_strategy)
def test_presentation_showtexttype_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original



@given(instance=presentation_ShowTextType_strategy)
def test_presentation_showtexttype_shapeId_setter(instance):
    original = instance.shapeId
    instance.shapeId = original
    assert instance.shapeId == original



@given(instance=presentation_ShowTextType_strategy)
def test_presentation_showtexttype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=presentation_ShowTextType_strategy)
def test_presentation_showtexttype_startScale_setter(instance):
    original = instance.startScale
    instance.startScale = original
    assert instance.startScale == original



@given(instance=presentation_ShowTextType_strategy)
def test_presentation_showtexttype_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=presentation_ShowShapeType_strategy)
@settings(max_examples=50)
def test_presentation_showshapetype_instantiation(instance):
    assert isinstance(instance, presentation_ShowShapeType)



@given(instance=presentation_ShowShapeType_strategy)
def test_presentation_showshapetype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=presentation_ShowShapeType_strategy)
def test_presentation_showshapetype_startScale_setter(instance):
    original = instance.startScale
    instance.startScale = original
    assert instance.startScale == original



@given(instance=presentation_ShowShapeType_strategy)
def test_presentation_showshapetype_delay_setter(instance):
    original = instance.delay
    instance.delay = original
    assert instance.delay == original



@given(instance=presentation_ShowShapeType_strategy)
def test_presentation_showshapetype_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original



@given(instance=presentation_ShowShapeType_strategy)
def test_presentation_showshapetype_pathId_setter(instance):
    original = instance.pathId
    instance.pathId = original
    assert instance.pathId == original



@given(instance=presentation_ShowShapeType_strategy)
def test_presentation_showshapetype_shapeId_setter(instance):
    original = instance.shapeId
    instance.shapeId = original
    assert instance.shapeId == original



@given(instance=presentation_ShowShapeType_strategy)
def test_presentation_showshapetype_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=presentation_PlayType_strategy)
@settings(max_examples=50)
def test_presentation_playtype_instantiation(instance):
    assert isinstance(instance, presentation_PlayType)



@given(instance=presentation_PlayType_strategy)
def test_presentation_playtype_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original



@given(instance=presentation_PlayType_strategy)
def test_presentation_playtype_shapeId_setter(instance):
    original = instance.shapeId
    instance.shapeId = original
    assert instance.shapeId == original

@given(instance=presentation_ShowType_strategy)
@settings(max_examples=50)
def test_presentation_showtype_instantiation(instance):
    assert isinstance(instance, presentation_ShowType)



@given(instance=presentation_ShowType_strategy)
def test_presentation_showtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=presentation_ShowType_strategy)
def test_presentation_showtype_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=presentation_SettingsType_strategy)
@settings(max_examples=50)
def test_presentation_settingstype_instantiation(instance):
    assert isinstance(instance, presentation_SettingsType)



@given(instance=presentation_SettingsType_strategy)
def test_presentation_settingstype_stayOnTop_setter(instance):
    original = instance.stayOnTop
    instance.stayOnTop = original
    assert instance.stayOnTop == original



@given(instance=presentation_SettingsType_strategy)
def test_presentation_settingstype_mouseVisible_setter(instance):
    original = instance.mouseVisible
    instance.mouseVisible = original
    assert instance.mouseVisible == original



@given(instance=presentation_SettingsType_strategy)
def test_presentation_settingstype_startWithNavigator_setter(instance):
    original = instance.startWithNavigator
    instance.startWithNavigator = original
    assert instance.startWithNavigator == original



@given(instance=presentation_SettingsType_strategy)
def test_presentation_settingstype_mouseAsPen_setter(instance):
    original = instance.mouseAsPen
    instance.mouseAsPen = original
    assert instance.mouseAsPen == original



@given(instance=presentation_SettingsType_strategy)
def test_presentation_settingstype_forceManual_setter(instance):
    original = instance.forceManual
    instance.forceManual = original
    assert instance.forceManual == original



@given(instance=presentation_SettingsType_strategy)
def test_presentation_settingstype_startPage_setter(instance):
    original = instance.startPage
    instance.startPage = original
    assert instance.startPage == original



@given(instance=presentation_SettingsType_strategy)
def test_presentation_settingstype_transitionOnClick_setter(instance):
    original = instance.transitionOnClick
    instance.transitionOnClick = original
    assert instance.transitionOnClick == original



@given(instance=presentation_SettingsType_strategy)
def test_presentation_settingstype_endless_setter(instance):
    original = instance.endless
    instance.endless = original
    assert instance.endless == original



@given(instance=presentation_SettingsType_strategy)
def test_presentation_settingstype_showLogo_setter(instance):
    original = instance.showLogo
    instance.showLogo = original
    assert instance.showLogo == original



@given(instance=presentation_SettingsType_strategy)
def test_presentation_settingstype_fullScreen_setter(instance):
    original = instance.fullScreen
    instance.fullScreen = original
    assert instance.fullScreen == original



@given(instance=presentation_SettingsType_strategy)
def test_presentation_settingstype_pause_setter(instance):
    original = instance.pause
    instance.pause = original
    assert instance.pause == original



@given(instance=presentation_SettingsType_strategy)
def test_presentation_settingstype_showEndOfPresentationSlide_setter(instance):
    original = instance.showEndOfPresentationSlide
    instance.showEndOfPresentationSlide = original
    assert instance.showEndOfPresentationSlide == original



@given(instance=presentation_SettingsType_strategy)
def test_presentation_settingstype_animations_setter(instance):
    original = instance.animations
    instance.animations = original
    assert instance.animations == original



@given(instance=presentation_SettingsType_strategy)
def test_presentation_settingstype_show1_setter(instance):
    original = instance.show1
    instance.show1 = original
    assert instance.show1 == original

@given(instance=presentation_PlaceholderType_strategy)
@settings(max_examples=50)
def test_presentation_placeholdertype_instantiation(instance):
    assert isinstance(instance, presentation_PlaceholderType)



@given(instance=presentation_PlaceholderType_strategy)
def test_presentation_placeholdertype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=presentation_PlaceholderType_strategy)
def test_presentation_placeholdertype_object_setter(instance):
    original = instance.object
    instance.object = original
    assert instance.object == original



@given(instance=presentation_PlaceholderType_strategy)
def test_presentation_placeholdertype_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=presentation_PlaceholderType_strategy)
def test_presentation_placeholdertype_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=presentation_PlaceholderType_strategy)
def test_presentation_placeholdertype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=presentation_CustomShapeType_strategy)
@settings(max_examples=50)
def test_presentation_customshapetype_instantiation(instance):
    assert isinstance(instance, presentation_CustomShapeType)

@given(instance=presentation_SceneType_strategy)
@settings(max_examples=50)
def test_presentation_scenetype_instantiation(instance):
    assert isinstance(instance, presentation_SceneType)

@given(instance=presentation_ControlType_strategy)
@settings(max_examples=50)
def test_presentation_controltype_instantiation(instance):
    assert isinstance(instance, presentation_ControlType)

@given(instance=presentation_ConnectorType_strategy)
@settings(max_examples=50)
def test_presentation_connectortype_instantiation(instance):
    assert isinstance(instance, presentation_ConnectorType)

@given(instance=presentation_CaptionType_strategy)
@settings(max_examples=50)
def test_presentation_captiontype_instantiation(instance):
    assert isinstance(instance, presentation_CaptionType)

@given(instance=presentation_MeasureType_strategy)
@settings(max_examples=50)
def test_presentation_measuretype_instantiation(instance):
    assert isinstance(instance, presentation_MeasureType)

@given(instance=presentation_FrameType_strategy)
@settings(max_examples=50)
def test_presentation_frametype_instantiation(instance):
    assert isinstance(instance, presentation_FrameType)

@given(instance=presentation_PageThumbnailType_strategy)
@settings(max_examples=50)
def test_presentation_pagethumbnailtype_instantiation(instance):
    assert isinstance(instance, presentation_PageThumbnailType)

@given(instance=presentation_PathType_strategy)
@settings(max_examples=50)
def test_presentation_pathtype_instantiation(instance):
    assert isinstance(instance, presentation_PathType)

@given(instance=presentation_GType_strategy)
@settings(max_examples=50)
def test_presentation_gtype_instantiation(instance):
    assert isinstance(instance, presentation_GType)

@given(instance=presentation_EllipseType_strategy)
@settings(max_examples=50)
def test_presentation_ellipsetype_instantiation(instance):
    assert isinstance(instance, presentation_EllipseType)

@given(instance=presentation_CircleType_strategy)
@settings(max_examples=50)
def test_presentation_circletype_instantiation(instance):
    assert isinstance(instance, presentation_CircleType)

@given(instance=presentation_PolylineType_strategy)
@settings(max_examples=50)
def test_presentation_polylinetype_instantiation(instance):
    assert isinstance(instance, presentation_PolylineType)

@given(instance=presentation_LineType_strategy)
@settings(max_examples=50)
def test_presentation_linetype_instantiation(instance):
    assert isinstance(instance, presentation_LineType)

@given(instance=presentation_RegularPolygonType_strategy)
@settings(max_examples=50)
def test_presentation_regularpolygontype_instantiation(instance):
    assert isinstance(instance, presentation_RegularPolygonType)

@given(instance=presentation_PolygonType_strategy)
@settings(max_examples=50)
def test_presentation_polygontype_instantiation(instance):
    assert isinstance(instance, presentation_PolygonType)

@given(instance=presentation_NotesType_strategy)
@settings(max_examples=50)
def test_presentation_notestype_instantiation(instance):
    assert isinstance(instance, presentation_NotesType)



@given(instance=presentation_NotesType_strategy)
def test_presentation_notestype_useHeaderName_setter(instance):
    original = instance.useHeaderName
    instance.useHeaderName = original
    assert instance.useHeaderName == original



@given(instance=presentation_NotesType_strategy)
def test_presentation_notestype_pageLayoutName_setter(instance):
    original = instance.pageLayoutName
    instance.pageLayoutName = original
    assert instance.pageLayoutName == original



@given(instance=presentation_NotesType_strategy)
def test_presentation_notestype_styleName_setter(instance):
    original = instance.styleName
    instance.styleName = original
    assert instance.styleName == original



@given(instance=presentation_NotesType_strategy)
def test_presentation_notestype_useDateTimeName_setter(instance):
    original = instance.useDateTimeName
    instance.useDateTimeName = original
    assert instance.useDateTimeName == original



@given(instance=presentation_NotesType_strategy)
def test_presentation_notestype_useFooterName_setter(instance):
    original = instance.useFooterName
    instance.useFooterName = original
    assert instance.useFooterName == original



@given(instance=presentation_NotesType_strategy)
def test_presentation_notestype_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=presentation_RectType_strategy)
@settings(max_examples=50)
def test_presentation_recttype_instantiation(instance):
    assert isinstance(instance, presentation_RectType)

@given(instance=presentation_FormsType_strategy)
@settings(max_examples=50)
def test_presentation_formstype_instantiation(instance):
    assert isinstance(instance, presentation_FormsType)

@given(instance=presentation_HideTextType_strategy)
@settings(max_examples=50)
def test_presentation_hidetexttype_instantiation(instance):
    assert isinstance(instance, presentation_HideTextType)



@given(instance=presentation_HideTextType_strategy)
def test_presentation_hidetexttype_shapeId_setter(instance):
    original = instance.shapeId
    instance.shapeId = original
    assert instance.shapeId == original



@given(instance=presentation_HideTextType_strategy)
def test_presentation_hidetexttype_startScale_setter(instance):
    original = instance.startScale
    instance.startScale = original
    assert instance.startScale == original



@given(instance=presentation_HideTextType_strategy)
def test_presentation_hidetexttype_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original



@given(instance=presentation_HideTextType_strategy)
def test_presentation_hidetexttype_delay_setter(instance):
    original = instance.delay
    instance.delay = original
    assert instance.delay == original



@given(instance=presentation_HideTextType_strategy)
def test_presentation_hidetexttype_pathId_setter(instance):
    original = instance.pathId
    instance.pathId = original
    assert instance.pathId == original



@given(instance=presentation_HideTextType_strategy)
def test_presentation_hidetexttype_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original



@given(instance=presentation_HideTextType_strategy)
def test_presentation_hidetexttype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=presentation_FooterDeclType_strategy)
@settings(max_examples=50)
def test_presentation_footerdecltype_instantiation(instance):
    assert isinstance(instance, presentation_FooterDeclType)



@given(instance=presentation_FooterDeclType_strategy)
def test_presentation_footerdecltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=presentation_FooterDeclType_strategy)
def test_presentation_footerdecltype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation_HideShapeType_strategy)
@settings(max_examples=50)
def test_presentation_hideshapetype_instantiation(instance):
    assert isinstance(instance, presentation_HideShapeType)



@given(instance=presentation_HideShapeType_strategy)
def test_presentation_hideshapetype_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original



@given(instance=presentation_HideShapeType_strategy)
def test_presentation_hideshapetype_startScale_setter(instance):
    original = instance.startScale
    instance.startScale = original
    assert instance.startScale == original



@given(instance=presentation_HideShapeType_strategy)
def test_presentation_hideshapetype_pathId_setter(instance):
    original = instance.pathId
    instance.pathId = original
    assert instance.pathId == original



@given(instance=presentation_HideShapeType_strategy)
def test_presentation_hideshapetype_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original



@given(instance=presentation_HideShapeType_strategy)
def test_presentation_hideshapetype_shapeId_setter(instance):
    original = instance.shapeId
    instance.shapeId = original
    assert instance.shapeId == original



@given(instance=presentation_HideShapeType_strategy)
def test_presentation_hideshapetype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=presentation_HideShapeType_strategy)
def test_presentation_hideshapetype_delay_setter(instance):
    original = instance.delay
    instance.delay = original
    assert instance.delay == original

@given(instance=presentation_HeaderType_strategy)
@settings(max_examples=50)
def test_presentation_headertype_instantiation(instance):
    assert isinstance(instance, presentation_HeaderType)

@given(instance=presentation_HeaderDeclType_strategy)
@settings(max_examples=50)
def test_presentation_headerdecltype_instantiation(instance):
    assert isinstance(instance, presentation_HeaderDeclType)



@given(instance=presentation_HeaderDeclType_strategy)
def test_presentation_headerdecltype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=presentation_HeaderDeclType_strategy)
def test_presentation_headerdecltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=presentation_FooterType_strategy)
@settings(max_examples=50)
def test_presentation_footertype_instantiation(instance):
    assert isinstance(instance, presentation_FooterType)

@given(instance=presentation_DimType_strategy)
@settings(max_examples=50)
def test_presentation_dimtype_instantiation(instance):
    assert isinstance(instance, presentation_DimType)



@given(instance=presentation_DimType_strategy)
def test_presentation_dimtype_shapeId_setter(instance):
    original = instance.shapeId
    instance.shapeId = original
    assert instance.shapeId == original



@given(instance=presentation_DimType_strategy)
def test_presentation_dimtype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=presentation_DateTimeType_strategy)
@settings(max_examples=50)
def test_presentation_datetimetype_instantiation(instance):
    assert isinstance(instance, presentation_DateTimeType)

@given(instance=presentation_EventListenerType_strategy)
@settings(max_examples=50)
def test_presentation_eventlistenertype_instantiation(instance):
    assert isinstance(instance, presentation_EventListenerType)



@given(instance=presentation_EventListenerType_strategy)
def test_presentation_eventlistenertype_show_setter(instance):
    original = instance.show
    instance.show = original
    assert instance.show == original



@given(instance=presentation_EventListenerType_strategy)
def test_presentation_eventlistenertype_startScale_setter(instance):
    original = instance.startScale
    instance.startScale = original
    assert instance.startScale == original



@given(instance=presentation_EventListenerType_strategy)
def test_presentation_eventlistenertype_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original



@given(instance=presentation_EventListenerType_strategy)
def test_presentation_eventlistenertype_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original



@given(instance=presentation_EventListenerType_strategy)
def test_presentation_eventlistenertype_verb_setter(instance):
    original = instance.verb
    instance.verb = original
    assert instance.verb == original



@given(instance=presentation_EventListenerType_strategy)
def test_presentation_eventlistenertype_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=presentation_EventListenerType_strategy)
def test_presentation_eventlistenertype_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original



@given(instance=presentation_EventListenerType_strategy)
def test_presentation_eventlistenertype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=presentation_EventListenerType_strategy)
def test_presentation_eventlistenertype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=presentation_EventListenerType_strategy)
def test_presentation_eventlistenertype_actuate_setter(instance):
    original = instance.actuate
    instance.actuate = original
    assert instance.actuate == original



@given(instance=presentation_EventListenerType_strategy)
def test_presentation_eventlistenertype_eventName_setter(instance):
    original = instance.eventName
    instance.eventName = original
    assert instance.eventName == original

@given(instance=presentation_SoundType_strategy)
@settings(max_examples=50)
def test_presentation_soundtype_instantiation(instance):
    assert isinstance(instance, presentation_SoundType)



@given(instance=presentation_SoundType_strategy)
def test_presentation_soundtype_show_setter(instance):
    original = instance.show
    instance.show = original
    assert instance.show == original



@given(instance=presentation_SoundType_strategy)
def test_presentation_soundtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=presentation_SoundType_strategy)
def test_presentation_soundtype_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original



@given(instance=presentation_SoundType_strategy)
def test_presentation_soundtype_actuate_setter(instance):
    original = instance.actuate
    instance.actuate = original
    assert instance.actuate == original



@given(instance=presentation_SoundType_strategy)
def test_presentation_soundtype_playFull_setter(instance):
    original = instance.playFull
    instance.playFull = original
    assert instance.playFull == original

@given(instance=presentation_AnimationsType1_strategy)
@settings(max_examples=50)
def test_presentation_animationstype1_instantiation(instance):
    assert isinstance(instance, presentation_AnimationsType1)



@given(instance=presentation_AnimationsType1_strategy)
def test_presentation_animationstype1_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=presentation_AnimationsType1_strategy)
def test_presentation_animationstype1_presentationAnimationElementsGroup_setter(instance):
    original = instance.presentationAnimationElementsGroup
    instance.presentationAnimationElementsGroup = original
    assert instance.presentationAnimationElementsGroup == original

@given(instance=presentation_EObject_strategy)
@settings(max_examples=50)
def test_presentation_eobject_instantiation(instance):
    assert isinstance(instance, presentation_EObject)

@given(instance=presentation_DateTimeDeclType_strategy)
@settings(max_examples=50)
def test_presentation_datetimedecltype_instantiation(instance):
    assert isinstance(instance, presentation_DateTimeDeclType)



@given(instance=presentation_DateTimeDeclType_strategy)
def test_presentation_datetimedecltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=presentation_DateTimeDeclType_strategy)
def test_presentation_datetimedecltype_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=presentation_DateTimeDeclType_strategy)
def test_presentation_datetimedecltype_dataStyleName_setter(instance):
    original = instance.dataStyleName
    instance.dataStyleName = original
    assert instance.dataStyleName == original



@given(instance=presentation_DateTimeDeclType_strategy)
def test_presentation_datetimedecltype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation_AnimationGroupType_strategy)
@settings(max_examples=50)
def test_presentation_animationgrouptype_instantiation(instance):
    assert isinstance(instance, presentation_AnimationGroupType)



@given(instance=presentation_AnimationGroupType_strategy)
def test_presentation_animationgrouptype_presentationAnimationElementsGroup_setter(instance):
    original = instance.presentationAnimationElementsGroup
    instance.presentationAnimationElementsGroup = original
    assert instance.presentationAnimationElementsGroup == original
